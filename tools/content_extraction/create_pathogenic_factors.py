#!/usr/bin/env python3
"""
Create individual Pathogenic Factor pattern files.
"""

from datetime import datetime
from pathlib import Path


def create_pathogenic_factor_notes():
    """Create 6 individual pathogenic factor pattern files."""

    base_dir = Path(__file__).parent.parent
    output_dir = base_dir / "TCM_Patterns" / "Pathogenic Factor Patterns"

    # Define the 6 pathogenic factors with their data
    factors = {
        "Wind": {
            "yin_yang": "Yang",
            "season": "Spring",
            "element": "Liver",
            "subtypes": ["External Wind", "Wind-Cold", "Wind-Heat", "Wind-Damp", "Wind-Water", "Internal Wind"],
            "symptoms_skin": [
                "Aversion to cold",
                "Fever",
                "Sore throat",
                "Sneezing",
                "Runny nose",
                "Occipital stiffness",
                "Floating pulse",
            ],
            "symptoms_channel": ["Stiffness", "Rigidity", "Sudden muscle contraction"],
            "symptoms_joint": [
                "Joint pain that moves from place to place, especially in the upper part of the body (Wind-Bi)"
            ],
        },
        "Cold": {
            "yin_yang": "Yin",
            "season": "Winter",
            "element": "Kidney",
            "subtypes": ["External Cold", "Internal Cold"],
            "symptoms_stomach": ["Sudden epigastric pain with vomiting"],
            "symptoms_intestine": ["Sudden abdominal pain with diarrhea"],
            "symptoms_uterus": ["Acute dysmenorrhea"],
        },
        "Summer-Heat": {
            "yin_yang": "Yang",
            "season": "Summer",
            "element": "Heart",
            "subtypes": [],
            "symptoms": ["Aversion to heat", "Sweating", "Headache", "Scanty-dark urine", "Dry lips", "Thirst"],
            "tongue": "Red tongue on the sides and tip",
            "pulse": "Rapid",
        },
        "Dampness": {
            "yin_yang": "Yin",
            "season": "Late Summer",
            "element": "Spleen",
            "subtypes": ["External Dampness", "Internal Dampness"],
            "symptoms_sinew": ["Heavy limbs", "Dull ache of the muscles"],
            "symptoms_joint": [
                "Pain",
                "Heaviness and swelling of the joints, especially of the lower part of the body (Damp-Bi)",
            ],
            "symptoms_other": [
                "Acute urinary discomfort",
                "Acute vaginal discharge",
                "Acute skin disease with vesicles or papules",
                "Acute digestive upsets",
            ],
        },
        "Dryness": {
            "yin_yang": "Yang",
            "season": "Autumn",
            "element": "Lung",
            "subtypes": ["External Dryness", "Internal Dryness"],
            "symptoms_general": ["Acute dry cough", "Aversion to cold", "Fever", "Dry mouth and nose"],
            "symptoms_sinew": ["Stiffness", "Contraction of muscles", "Pain", "Chilliness"],
            "symptoms_joint": ["Severe pain in a joint (Cold-Bi)"],
        },
        "Fire": {
            "yin_yang": "Yang",
            "season": "Summer",
            "element": "Heart",
            "subtypes": ["External Fire", "Internal Fire"],
            "symptoms": [
                "Aversion to heat",
                "High fever",
                "Sweating",
                "Mental confusion",
                "Thirst",
                "Overflowing-rapid pulse",
            ],
            "tongue": "Red tongue with yellow coating",
            "pulse": "Overflowing-rapid pulse",
        },
    }

    created = []
    for name, data in factors.items():
        content = create_factor_content(name, data)
        filepath = output_dir / f"{name} Pathogenic Factor.md"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        created.append(name)
        print(f"✅ Created: {name} Pathogenic Factor")

    return created


def create_factor_content(name: str, data: dict) -> str:
    """Create content for individual pathogenic factor file."""

    now = datetime.now()

    # Build symptoms list
    all_symptoms = []
    for key, value in data.items():
        if key.startswith("symptoms") and isinstance(value, list):
            all_symptoms.extend(value)

    # Build symptom sections
    symptom_sections = ""
    for key, value in data.items():
        if key.startswith("symptoms") and isinstance(value, list):
            section_name = key.replace("symptoms_", "").replace("_", " ").title()
            if section_name == "Symptoms":
                section_name = "General Symptoms"
            symptom_sections += f"\n**{section_name}:**\n"
            for symptom in value:
                symptom_sections += f"- {symptom}\n"

    # Subtypes section
    subtypes_text = ""
    if data.get("subtypes"):
        subtypes_text = f"""
## Pattern Subtypes

This pathogenic factor manifests in the following patterns:
{chr(10).join("- " + s for s in data["subtypes"])}
"""

    # Tongue and Pulse
    tongue_pulse = ""
    if data.get("tongue"):
        tongue_pulse += f"\n**Tongue:** {data['tongue']}"
    if data.get("pulse"):
        tongue_pulse += f"\n**Pulse:** {data['pulse']}"

    content = f"""---
# =9 Core Metadata (Universal Fields)
id: "pattern-{now.strftime("%Y%m%d%H%M%S")}"
name: "{name} Pathogenic Factor"
type: "pattern"
aliases: ["{name}"]
tags: [TCM, Pattern, Pathogenic_Factor]

# =9 Cross-Link Fields (Universal Relationship Slots)
category: [Pathogenic Factor]
related: []
symptoms: {all_symptoms}
patterns: []
western_conditions: []
formulas: []
herbs: []
points: []
nutrition: []
tests: []

# =9 Pattern-Specific Data
pattern_data:
  pattern_type: "Pathogenic Factor"
  pattern_subtype: "{name}"
  excess_deficiency: "Excess"
  hot_cold: "{"Hot" if data["yin_yang"] == "Yang" else "Cold"}"
  interior_exterior: "Exterior"
  yin_yang: "{data["yin_yang"]}"
  etiology: ["{name} invasion"]
  pathomechanisms: []
  disease_progression: ""
  cardinal_symptoms: {all_symptoms[:5] if len(all_symptoms) >= 5 else all_symptoms}
  tongue: "{data.get("tongue", "")}"
  pulse: "{data.get("pulse", "")}"
  treatment_principle: ["Expel {name}", "Support Zheng Qi"]
  contraindications: []

created: {now.strftime("%Y-%m-%d")}
updated: {now.strftime("%Y-%m-%d")}
---

# {name} Pathogenic Factor

## Overview

**Nature:** {data["yin_yang"]} Pathogenic Factor
**Season:** {data["season"]}
**Five Element:** {data["element"]}
**Pattern Type:** Always corresponds to an EXCESS pattern according to the Eight Principles

{name} is one of the Six Pathogenic Factors in Traditional Chinese Medicine. As a {data["yin_yang"].lower()} pathogenic factor, it is primarily associated with the {data["season"].lower()} season and relates to the {data["element"]} element in Five Element theory.

## Key Characteristics

1. **Nature:** {data["yin_yang"]} pathogenic factor
2. **Seasonality:** Most prevalent in {data["season"].lower()}
3. **Pattern Type:** Always presents as an EXCESS pattern
4. **Diagnosis:** Made on the basis of symptoms and signs, not patient history

{subtypes_text}

## Clinical Manifestations

{symptom_sections}
{tongue_pulse}

## Diagnostic Notes

The diagnosis of {name} pathogenic factor is made not on the basis of the patient's history, but on the basis of the pattern of symptoms and signs presented. {name} as a pathogenic factor is more important as a pattern of disharmony than as a cause of disease.

## Additional Information

**Original Source Data:**
This pattern file was extracted from the Pathogenic Factors differentiation system, which recognizes 6 main pathogenic factors: Wind, Cold, Dampness, Heat (Summer-Heat), Dryness, and Fire. All pathogenic factors correspond to EXCESS patterns according to the Eight Principles.
"""

    return content


def main():
    """Main function."""
    print("🔧 Creating individual Pathogenic Factor pattern files...")
    print("=" * 70)

    created = create_pathogenic_factor_notes()

    print("\n" + "=" * 70)
    print(f"✅ Created {len(created)} pathogenic factor patterns!")
    print("=" * 70)
    print("\n💡 Files created in: TCM_Patterns/Pathogenic Factor Patterns/")
    print("   Next: Enhance with enhance_pattern_single_call.py")


if __name__ == "__main__":
    main()
