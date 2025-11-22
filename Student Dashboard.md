---
id: patient-dashboard
type: patient
name: New Patient
age: 30
gender: Male
chief_complaint: palpitations
symptoms: headache, irritability, enuresis
tongue: purple
pulse: knotted
diagnosis: Liver Meridian Pattern
created: 2025-11-19
---

# TCM Diagnostic Dashboard

## 1. Patient Details
**Name:** `INPUT[text:name]`
**Age:** `INPUT[number:age]`
**Gender:** `INPUT[inlineSelect(option(Male), option(Female), option(Other)):gender]`

---

## 2. Intake
**Chief Complaint:**
`INPUT[textArea:chief_complaint]`

**Symptoms:**
*(Enter one symptom per line. You can use [[WikiLinks]].)*
`INPUT[textArea:symptoms]`

---

## 3. Examination
**Tongue:** `INPUT[text:tongue]`
**Pulse:** `INPUT[text:pulse]`

---

## 4. Diagnosis & Treatment
**Selected Diagnosis:**
*(Copy the exact pattern name from the results below)*
`INPUT[text(placeholder(Paste Pattern Name Here)):diagnosis]`

```dataviewjs
// ---- CONFIGURATION ----
const patient = dv.current();

// 1. Clean Inputs Helper
const clean = (str) => String(str || "").toLowerCase().trim();
const linkToText = (v) => {
    if (!v) return "";
    if (v.path) return v.path; 
    return String(v).replace(/[\[\]]/g, "").trim();
};

// 2. Parse Symptoms
let symptoms = [];
if (patient.symptoms) {
    symptoms = String(patient.symptoms)
        .split(/[\r\n,]+/)
        .map(s => s.trim())
        .filter(s => s.length > 0)
        .map(linkToText);
}

const tongue = clean(patient.tongue);
const pulse = clean(patient.pulse);
const complaint = clean(patient.chief_complaint);

// 3. Run Matcher
if (symptoms.length === 0 && !tongue && !pulse && !complaint) {
    dv.paragraph("⬇️ **Fill out the Intake sections above to see results.**");
} else {
    const patterns = dv.pages('"TCM_Patterns"'); 
    
    // Score Patterns
    const results = patterns.map(p => {
        let score = 0;
        let matches = [];
        
        const pSymptoms = (p.symptoms || []).map(linkToText).map(s => s.toLowerCase());
        for (let s of symptoms) {
            let sClean = String(s).toLowerCase();
            if (pSymptoms.some(ps => ps.includes(sClean) || sClean.includes(ps))) {
                score += 3; 
                matches.push(s);
            }
        }
        
        const pTongue = String(p.pattern_data?.tongue || "").toLowerCase();
        if (tongue && pTongue.includes(tongue)) { score += 2; matches.push("Tongue"); }
        
        const pPulse = String(p.pattern_data?.pulse || "").toLowerCase();
        if (pulse && pPulse.includes(pulse)) { score += 2; matches.push("Pulse"); }
        
        return { file: p.file, score, matches, name: p.file.name };
    })
    .filter(r => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .limit(10);
    
    if (results.length === 0) {
        dv.paragraph("❌ No direct pattern matches found.");
    } else {
        dv.header(3, "🔍 Pattern Matches");
        dv.table(
            ["Score", "Pattern Link", "Matches", "Name to Copy"],
            results.map(r => [
                r.score,
                r.file.link, 
                r.matches.join(", "),
                `**${r.name}**` 
            ])
        );
        
        // --- EMOJI-PROOF DIFFERENTIAL EXTRACTION ---
        const top3 = results.slice(0, 3);
        
        if (top3.length > 0) {
             dv.header(2, "⚖️ Differential Diagnosis (Top 3)");
             
             for(let res of top3) {
                 const tFile = app.vault.getAbstractFileByPath(res.file.path);
                 // Add newline to ensure we catch the very first header if it's at the top
                 const rawContent = "\n" + await app.vault.read(tFile);
                 
                 // 1. Split by Level 2 Headings (##)
                 const sections = rawContent.split(/\n##\s/);
                 
                 // 2. Find section where the FIRST LINE contains "differential"
                 const diffSection = sections.find(s => {
                     // Get the title line (everything before the first newline)
                     let titleLine = s.split("\n")[0].toLowerCase();
                     return titleLine.includes("differential");
                 });
                 
                 dv.header(3, "For: " + res.name);
                                  
                 if (diffSection) {
                     // Remove the title line (so we don't duplicate the header/emoji)
                     let contentBody = diffSection.split("\n").slice(1).join("\n");
                     
                     // Render!
                     dv.paragraph(contentBody);
                 } else {
                     // FALLBACK
                     let p = dv.page(res.file.path);
                     let sList = (p.symptoms || []).map(linkToText);
                     let ask = sList.filter(s => !JSON.stringify(symptoms).toLowerCase().includes(String(s).toLowerCase()));
                     
                     if(ask.length > 0) {
                        dv.paragraph(`*No differential section found. Check against:* ${ask.slice(0,5).join(", ")}`);
                     } else {
                         dv.paragraph("*No specific differential info found.*");
                     }
                 }
                 dv.paragraph("---"); 
             }
        }
    }
}
```

```dataviewjs
// ---- TREATMENT PLAN RENDERER (UNIVERSAL SPLITTER VERSION) ----
const currentDx = String(dv.current().diagnosis || "").trim();

if(!currentDx) {
    // Do nothing until selected
} else {
    const page = dv.pages('"TCM_Patterns"').where(p => p.file.name.toLowerCase() === currentDx.toLowerCase() || p.file.name.toLowerCase().includes(currentDx.toLowerCase())).first();
    
    if(!page) {
        dv.paragraph(`⚠️ Diagnosis entered but no matching file found for: "${currentDx}"`);
    } else {
        // 1. GET FILE CONTENT
        const tFile = app.vault.getAbstractFileByPath(page.file.path);
        // Add newline to ensure first header is caught
        const rawContent = "\n" + await app.vault.read(tFile);
        
        dv.header(2, "Treatment for: " + page.file.name);
        
        // ---- PART A: FRONTMATTER DATA ----
        const flat = (arr) => (!arr ? [] : (Array.isArray(arr) ? arr : Array.from(arr)));

        // Formula
        dv.header(3, "🍵 Formula");
        const forms = page.formulas || page.formula;
        if(forms && flat(forms).length > 0) {
            dv.paragraph(flat(forms).map(f => "- " + f).join("\n"));
        } else {
            dv.paragraph("_No formula listed._");
        }
        
        // Herbs (Fixed empty table issue)
        dv.header(3, "🌿 Key Herbs");
        if(page.herbs && flat(page.herbs).length > 0) {
            let herbList = flat(page.herbs).map(h => {
                if (h.name && h.dose) return [h.name, h.dose]; 
                return [h, ""]; 
            });
            dv.table(["Herb", "Dose"], herbList);
        } else {
             dv.paragraph("_No herbs listed._");
        }
        
        // Acupuncture
        dv.header(3, "📍 Acupuncture");
        const points = page.points || page.acupuncture;
        if(points && flat(points).length > 0) {
             dv.paragraph(flat(points).map(p => "- " + p).join("\n"));
        }

        dv.paragraph("---");

        // ---- PART B: BODY CONTENT (ROBUST SPLIT METHOD) ----

        // 1. Split file by ANY Level 2 or 3 Header (## or ###)
        const sections = rawContent.split(/\n#{2,3}\s/);

        // 2. Helper to find a section containing a keyword in its title
        const findSection = (keyword) => {
            const found = sections.find(s => {
                // Grab just the first line (the header title)
                const title = s.split("\n")[0].toLowerCase();
                return title.includes(keyword.toLowerCase());
            });
            
            if (found) {
                // Return everything AFTER the title line
                return found.split("\n").slice(1).join("\n").trim();
            }
            return null;
        };

        // --- SECTION FINDER ---
        
        // Principles
        const principles = findSection("Principles");
        if (principles) {
            dv.header(3, "🛡️ Treatment Principles");
            dv.paragraph(principles);
        }

        // Contraindications
        const contra = findSection("Contraindications");
        if (contra) {
            dv.header(3, "⛔ Contraindications & Cautions");
            dv.paragraph(contra);
        }

        // Variations
        const variations = findSection("Variations");
        if (variations) {
            dv.header(3, "🔀 Common Variations");
            dv.paragraph(variations);
        }

        // Combinations
        const combos = findSection("Combinations");
        if (combos) {
            dv.header(3, "🔗 Common Combinations");
            dv.paragraph(combos);
        }
        
        // Western
        const western = findSection("Western");
        if (western) {
            dv.paragraph("---");
            dv.header(3, "🩺 Western Medical Correlates");
            dv.paragraph(western);
        }

        // Clinical Pearls
        // Look for "Pearls" OR "Experience" OR "Tips"
        const pearls = findSection("Pearls") || findSection("Experience") || findSection("Tips"); 
        
        if (pearls) {
            dv.paragraph("---");
            dv.header(3, "💡 Clinical Pearls & Experience");
            dv.paragraph(pearls);
        }
    }
}
```

