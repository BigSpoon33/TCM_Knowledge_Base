#!/usr/bin/env python3
"""
Pattern Clustering Analyzer - Phase 2.1
Analyzes diseases to find patterns and similarities based on:
- Symptoms
- Treatment approaches (points, herbs)
- Pathogenic factors
- Affected organs
"""

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import yaml


class PatternClusteringAnalyzer:
    """Analyzes disease patterns and finds similarities"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.diseases_dir = self.base_dir / "TCM_Diseases"

        # Disease data storage
        self.diseases = {}  # disease_name -> full data dict

        # Index structures for fast lookup
        self.symptom_index = defaultdict(set)  # symptom -> set of diseases
        self.point_index = defaultdict(set)  # point -> set of diseases
        self.concept_index = defaultdict(set)  # concept -> set of diseases
        self.pattern_index = defaultdict(set)  # pattern -> set of diseases

        # Similarity cache
        self.similarity_cache = {}

    def load_diseases(self):
        """Load all disease files and build indices"""
        print("\n📚 Loading disease data...")
        print("=" * 80)

        if not self.diseases_dir.exists():
            print("❌ Diseases directory not found!")
            return

        for disease_file in self.diseases_dir.glob("*.md"):
            if disease_file.stem in ["TEMPLATE_Disease", "EXAMPLE_Wind_Stroke"]:
                continue

            disease_data = self._load_disease_file(disease_file)
            if disease_data:
                disease_name = disease_data["name"]
                self.diseases[disease_name] = disease_data

                # Build indices
                for symptom in disease_data.get("symptoms", []):
                    self.symptom_index[symptom].add(disease_name)

                for point in disease_data.get("points", []):
                    self.point_index[point].add(disease_name)

                for concept in disease_data.get("related", []):
                    self.concept_index[concept].add(disease_name)

                for pattern in disease_data.get("patterns", []):
                    self.pattern_index[pattern].add(disease_name)

        print(f"✓ Loaded {len(self.diseases)} diseases")
        print(f"✓ Indexed {len(self.symptom_index)} unique symptoms")
        print(f"✓ Indexed {len(self.point_index)} unique points")
        print(f"✓ Indexed {len(self.concept_index)} unique concepts")
        print(f"✓ Indexed {len(self.pattern_index)} unique patterns")

    def _load_disease_file(self, file_path: Path) -> dict:
        """Load and parse a disease file"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Extract frontmatter
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not match:
                # Try to get name from heading
                heading_match = re.search(r"^#\s+🩺?\s*(.+?)$", content, re.MULTILINE)
                if heading_match:
                    return {
                        "name": heading_match.group(1).strip(),
                        "symptoms": [],
                        "points": [],
                        "herbs": [],
                        "related": [],
                        "patterns": [],
                        "western_conditions": [],
                        "file_path": str(file_path),
                    }
                return None

            frontmatter_text = match.group(1).strip()
            if not frontmatter_text:
                return None

            frontmatter = yaml.safe_load(frontmatter_text)

            return {
                "name": frontmatter.get("name", file_path.stem.replace("_", " ")),
                "symptoms": frontmatter.get("symptoms", []),
                "points": frontmatter.get("points", []),
                "herbs": frontmatter.get("herbs", []),
                "related": frontmatter.get("related", []),
                "patterns": frontmatter.get("patterns", []),
                "western_conditions": frontmatter.get("western_conditions", []),
                "category": frontmatter.get("category", []),
                "file_path": str(file_path),
            }

        except Exception:
            return None

    def calculate_symptom_similarity(self, disease1: str, disease2: str) -> float:
        """Calculate Jaccard similarity based on shared symptoms"""
        if disease1 not in self.diseases or disease2 not in self.diseases:
            return 0.0

        symptoms1 = set(self.diseases[disease1].get("symptoms", []))
        symptoms2 = set(self.diseases[disease2].get("symptoms", []))

        if not symptoms1 or not symptoms2:
            return 0.0

        intersection = len(symptoms1 & symptoms2)
        union = len(symptoms1 | symptoms2)

        return intersection / union if union > 0 else 0.0

    def calculate_treatment_similarity(self, disease1: str, disease2: str) -> float:
        """Calculate similarity based on treatment approaches (points + herbs)"""
        if disease1 not in self.diseases or disease2 not in self.diseases:
            return 0.0

        d1 = self.diseases[disease1]
        d2 = self.diseases[disease2]

        # Combine points and herbs for treatment signature
        treatment1 = set(d1.get("points", [])) | set(d1.get("herbs", []))
        treatment2 = set(d2.get("points", [])) | set(d2.get("herbs", []))

        if not treatment1 or not treatment2:
            return 0.0

        intersection = len(treatment1 & treatment2)
        union = len(treatment1 | treatment2)

        return intersection / union if union > 0 else 0.0

    def calculate_concept_similarity(self, disease1: str, disease2: str) -> float:
        """Calculate similarity based on shared pathogenic factors/concepts"""
        if disease1 not in self.diseases or disease2 not in self.diseases:
            return 0.0

        concepts1 = set(self.diseases[disease1].get("related", []))
        concepts2 = set(self.diseases[disease2].get("related", []))

        if not concepts1 or not concepts2:
            return 0.0

        intersection = len(concepts1 & concepts2)
        union = len(concepts1 | concepts2)

        return intersection / union if union > 0 else 0.0

    def calculate_overall_similarity(self, disease1: str, disease2: str, weights: dict[str, float] = None) -> float:
        """Calculate weighted overall similarity"""
        if weights is None:
            weights = {"symptoms": 0.4, "treatment": 0.4, "concepts": 0.2}

        symptom_sim = self.calculate_symptom_similarity(disease1, disease2)
        treatment_sim = self.calculate_treatment_similarity(disease1, disease2)
        concept_sim = self.calculate_concept_similarity(disease1, disease2)

        overall = (
            weights["symptoms"] * symptom_sim + weights["treatment"] * treatment_sim + weights["concepts"] * concept_sim
        )

        return overall

    def find_similar_diseases(
        self, disease_name: str, top_n: int = 5, min_similarity: float = 0.1
    ) -> list[tuple[str, float, dict]]:
        """Find the most similar diseases to a given disease"""
        if disease_name not in self.diseases:
            return []

        similarities = []

        for other_disease in self.diseases:
            if other_disease == disease_name:
                continue

            overall_sim = self.calculate_overall_similarity(disease_name, other_disease)

            if overall_sim >= min_similarity:
                # Get component similarities for breakdown
                breakdown = {
                    "symptom_similarity": self.calculate_symptom_similarity(disease_name, other_disease),
                    "treatment_similarity": self.calculate_treatment_similarity(disease_name, other_disease),
                    "concept_similarity": self.calculate_concept_similarity(disease_name, other_disease),
                    "shared_symptoms": list(
                        set(self.diseases[disease_name].get("symptoms", []))
                        & set(self.diseases[other_disease].get("symptoms", []))
                    ),
                    "shared_points": list(
                        set(self.diseases[disease_name].get("points", []))
                        & set(self.diseases[other_disease].get("points", []))
                    ),
                    "shared_concepts": list(
                        set(self.diseases[disease_name].get("related", []))
                        & set(self.diseases[other_disease].get("related", []))
                    ),
                }

                similarities.append((other_disease, overall_sim, breakdown))

        # Sort by similarity score
        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_n]

    def cluster_by_symptoms(self, min_shared_symptoms: int = 3) -> dict[str, list[str]]:
        """Cluster diseases that share significant symptoms"""
        clusters = defaultdict(list)

        for symptom, diseases in self.symptom_index.items():
            if len(diseases) >= min_shared_symptoms:
                cluster_key = f"Symptom: {symptom}"
                clusters[cluster_key] = sorted(list(diseases))

        return dict(clusters)

    def cluster_by_treatment(self, min_shared_points: int = 2) -> dict[str, list[str]]:
        """Cluster diseases treated with similar points"""
        clusters = defaultdict(list)

        for point, diseases in self.point_index.items():
            if len(diseases) >= min_shared_points:
                cluster_key = f"Point: {point}"
                clusters[cluster_key] = sorted(list(diseases))

        return dict(clusters)

    def cluster_by_concepts(self) -> dict[str, list[str]]:
        """Cluster diseases by pathogenic factors/concepts"""
        clusters = {}

        for concept, diseases in self.concept_index.items():
            if len(diseases) > 1:
                clusters[f"Concept: {concept}"] = sorted(list(diseases))

        return clusters

    def generate_similarity_report(self, output_file: Path = None):
        """Generate comprehensive similarity analysis report"""
        if output_file is None:
            output_file = self.base_dir / "PATTERN_ANALYSIS_REPORT.md"

        report = []
        report.append("# 🔍 TCM Disease Pattern Clustering Analysis")
        report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"\n**Diseases Analyzed:** {len(self.diseases)}")
        report.append("\n---\n")

        # Similar Disease Pairs
        report.append("## 🔗 Most Similar Disease Pairs\n")

        all_pairs = []
        diseases_list = list(self.diseases.keys())

        for i, disease1 in enumerate(diseases_list):
            for disease2 in diseases_list[i + 1 :]:
                sim = self.calculate_overall_similarity(disease1, disease2)
                if sim > 0.2:  # Only significant similarities
                    all_pairs.append((disease1, disease2, sim))

        all_pairs.sort(key=lambda x: x[2], reverse=True)

        for disease1, disease2, sim in all_pairs[:20]:
            report.append(f"### {disease1} ↔ {disease2}")
            report.append(f"**Overall Similarity:** {sim:.2%}\n")

            # Get breakdown
            breakdown = {
                "symptom": self.calculate_symptom_similarity(disease1, disease2),
                "treatment": self.calculate_treatment_similarity(disease1, disease2),
                "concept": self.calculate_concept_similarity(disease1, disease2),
            }

            report.append(f"- Symptom Similarity: {breakdown['symptom']:.2%}")
            report.append(f"- Treatment Similarity: {breakdown['treatment']:.2%}")
            report.append(f"- Concept Similarity: {breakdown['concept']:.2%}")

            # Shared elements
            shared_symptoms = list(
                set(self.diseases[disease1].get("symptoms", [])) & set(self.diseases[disease2].get("symptoms", []))
            )
            if shared_symptoms:
                report.append(f"\n**Shared Symptoms:** {', '.join(shared_symptoms[:5])}")
                if len(shared_symptoms) > 5:
                    report.append(f" _(+{len(shared_symptoms) - 5} more)_")

            report.append("\n")

        # Symptom Clusters
        report.append("\n---\n")
        report.append("## 🎯 Symptom-Based Clusters\n")

        symptom_clusters = self.cluster_by_symptoms(min_shared_symptoms=2)
        for cluster_name, diseases in sorted(symptom_clusters.items(), key=lambda x: len(x[1]), reverse=True)[:15]:
            report.append(f"### {cluster_name}")
            report.append(f"**Diseases ({len(diseases)}):** {', '.join(diseases)}\n")

        # Concept Clusters
        report.append("\n---\n")
        report.append("## 🧠 Pathogenic Factor Clusters\n")

        concept_clusters = self.cluster_by_concepts()
        for cluster_name, diseases in sorted(concept_clusters.items(), key=lambda x: len(x[1]), reverse=True):
            report.append(f"### {cluster_name}")
            report.append(f"**Diseases ({len(diseases)}):** {', '.join(diseases)}\n")

        # Treatment Clusters
        report.append("\n---\n")
        report.append("## ⚡ Treatment Approach Clusters\n")

        treatment_clusters = self.cluster_by_treatment(min_shared_points=2)
        for cluster_name, diseases in sorted(treatment_clusters.items(), key=lambda x: len(x[1]), reverse=True)[:15]:
            report.append(f"### {cluster_name}")
            report.append(f"**Diseases ({len(diseases)}):** {', '.join(diseases)}\n")

        # Write report
        report_text = "\n".join(report)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report_text)

        print(f"\n✅ Pattern analysis report generated: {output_file}")
        return output_file

    def run(self):
        """Run complete pattern clustering analysis"""
        print("=" * 80)
        print("🔍 PATTERN CLUSTERING ANALYZER - PHASE 2.1")
        print("=" * 80)

        self.load_diseases()

        print("\n🔬 Analyzing patterns...")
        print("=" * 80)

        # Generate report
        self.generate_similarity_report()

        print("\n" + "=" * 80)
        print("✅ PATTERN CLUSTERING COMPLETE")
        print("=" * 80)


def main():
    base_dir = Path(__file__).parent.parent
    analyzer = PatternClusteringAnalyzer(base_dir)
    analyzer.run()


if __name__ == "__main__":
    main()
