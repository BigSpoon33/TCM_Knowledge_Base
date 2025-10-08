---
# 🔹 Core Metadata (Universal Fields)
id: "disease-20251006000001"
name: "Wind Stroke"
type: "disease"
aliases: ["Zhong Feng", "中風", "Stroke", "Cerebrovascular Accident", "CVA"]
tags: [TCM, Disease, Internal, Neurological, Emergency]

# 🔹 Cross-Link Fields (Universal Relationship Slots)
category: ["Internal Diseases", "Emergency Diseases"]
related: ["Syncope", "Epilepsy", "Headache"]
symptoms: ["Loss of consciousness", "Hemiplegia", "Slurred speech", "Deviated mouth", "Dizziness", "Pallor", "Clenched jaws", "Rattling in throat"]
patterns: ["Wind Stroke - Tense Syndrome", "Wind Stroke - Flaccid Syndrome", "Wind Stroke - Meridian Attack"]
western_conditions: ["Cerebral hemorrhage", "Cerebral thrombosis", "Cerebral embolism", "Subarachnoid hemorrhage", "Stroke", "CVA"]
formulas: []
herbs: []
points: ["DU-20", "DU-26", "ST-40", "LIV-3", "KID-1", "LU-11", "HE-9", "P-9", "L.I.-1", "SJ-1", "S.I.-1", "DU-15", "REN-23", "HE-5", "L.I.-4", "ST-7", "ST-6", "REN-8", "REN-6", "REN-4", "BL-7", "DU-16", "L.I.-15", "L.I.-11", "SJ-5", "GB-30", "GB-34", "ST-36", "ST-41", "GB-20", "KID-3", "SP-6", "P-7", "LIV-2", "ST-4"]
nutrition: []
tests: []

# 🔹 Disease-Specific Data
disease_data:
  chapter: "17"
  chapter_name: "Internal Diseases"
  disease_category: "internal"

  overview:
    description: "An emergency condition manifested by falling down in a fit with loss of consciousness, or hemiplegia, slurred speech and deviated mouth. Characterized by abrupt onset with pathological changes varying quickly like the wind."
    key_features: ["Sudden onset", "Loss of consciousness", "Hemiplegia", "Facial paralysis", "Speech disturbance"]
    onset_characteristics: "Abrupt, acute, emergency presentation"

  western_correlation:
    conditions: ["Cerebral hemorrhage", "Cerebral thrombosis", "Cerebral embolism", "Subarachnoid hemorrhage"]
    notes: "May result in sequelae such as hemiplegia, monoplegia, and aphasia after acute stage"

  etiology:
    primary_causes: ["Deficiency of kidney yin due to sexual indulgence", "Irregular food intake impairing spleen transportation", "Accumulated dampness transforming to phlegm and heat", "Exasperation and agitation", "Alcohol indulgence or overeating", "Overstrain and stress", "Invasion of exogenous pathogenic wind"]
    contributing_factors: ["Old age", "Poor health", "Deficiency of qi and blood", "Deficiency in lower body with excess in upper body"]
    pathogenesis: "Imbalance of yin and yang in zang-fu organs leads to upsurge of liver yang and heart fire, causing qi and blood to rush upward together with turbid phlegm, disturbing the mind."
    affected_organs: ["Heart", "Liver", "Kidney", "Spleen"]

  pattern_differentiation:
    - pattern_name: "Attack on Zang-Fu Organs - Tense Syndrome"
      pattern_type: "excess"
      subcategory: "tense"

      manifestations:
        main_symptoms: ["Falling down in fit", "Loss of consciousness", "Tightly closed hands", "Clenched jaws", "Flushed face", "Coarse breathing", "Rattling in throat", "Retention of urine", "Constipation"]
        accompanying_symptoms: []
        tongue: "Red tongue with thick yellow or dark grey coating"
        pulse: "String-taut, rolling and forceful pulse"

      analysis: "Wind stirred up by upsurge of liver yang sends qi and blood upwards, which together with accumulated phlegm fire disturb the mind, leading to sudden loss of consciousness. Excessive wind phlegm brings about rattling in throat. Red tongue with thick yellow coating, string-taut rolling and forceful pulse are signs of wind combined with phlegm fire."

      treatment:
        principle: "Promote resuscitation, reduce wind and fire, resolve phlegm"
        method: "Points of Du Meridian, Liver Meridian of Foot-Jueyin and twelve Jing-Well points"
        needle_technique: "reducing"

        primary_points:
          - code: "DU-20"
            name: "Baihui"
            function: "Regulate qi of Du Meridian, effect resuscitation"
            technique: "Reducing method"
          - code: "DU-26"
            name: "Shuigou"
            function: "Regulate qi of Du Meridian, effect resuscitation"
            technique: "Reducing method"
          - code: "ST-40"
            name: "Fenglong"
            function: "Invigorate spleen and stomach functions, resolve turbid phlegm"
            technique: "Reducing method"
          - code: "LIV-3"
            name: "Taichong"
            function: "Subdue upsurging qi in Liver Meridian, pacify liver yang"
            technique: "Reducing method"
          - code: "KID-1"
            name: "Yongquan"
            function: "Conduct heat downward"
            technique: "Reducing method"

        supplementary_points:
          - condition: "Clenched jaws"
            points:
              - code: "ST-7"
                name: "Xiaguan"
                function: "Promote circulation of qi and blood"
              - code: "ST-6"
                name: "Jiache"
                function: "Relieve clenched jaws"
              - code: "L.I.-4"
                name: "Hegu"
                function: "Yangming meridian supply to cheeks"
          - condition: "Aphasia and stiffness of tongue"
            points:
              - code: "DU-15"
                name: "Yamen"
                function: "Local point for tongue"
              - code: "REN-23"
                name: "Lianquan"
                function: "Adjacent point for tongue"
              - code: "HE-5"
                name: "Tongli"
                function: "Luo-Connecting point of Heart Meridian"

        explanation: "The condition is due to disturbance of the heart by phlegm fire associated with upsurging of liver yang and upward flowing of qi and blood. Baihui (Du 20) and Shuigou (Du 26) regulate qi of Du Meridian and effect resuscitation. Yongquan (K 1) conducts heat downward. Taichong (Liv 3) subdues upsurging qi in Liver Meridian and pacifies liver yang. Pricking the twelve Jing-Well points on both hands, where qi of three yin and three yang meridians meet, dispels heat and regains consciousness. The spleen and stomach are source of phlegm production. Fenglong (S 40), the Luo-Connecting point of Stomach Meridian, invigorates functions of spleen and stomach and helps resolve turbid phlegm. Yangming Meridians of Hand and Foot supply the cheeks, so Xiaguan (S 7), Jiache (S 6) and Hegu (LI 4) promote circulation of qi and blood for relieving clenched jaws. Yamen (Du 15) and Lianquan (Ren 23) are local and adjacent points of tongue, and Tongli (H 5), the Luo-Connecting point of Heart Meridian, relieves stiffness of tongue."

        modifications:
          - condition: "Severe phlegm heat"
            add_points: ["LU-11", "HE-9", "P-9", "L.I.-1", "SJ-1", "S.I.-1"]
            remove_points: []

    - pattern_name: "Attack on Zang-Fu Organs - Flaccid Syndrome"
      pattern_type: "deficiency"
      subcategory: "flaccid"

      manifestations:
        main_symptoms: ["Falling down in fit", "Sudden loss of consciousness", "Mouth agape", "Eyes closed", "Snoring but feeble breathing", "Flaccid paralysis of limbs", "Incontinence of urine"]
        accompanying_symptoms: ["Cold limbs", "Flushing of face as rouged"]
        tongue: "Flaccid tongue"
        pulse: "Thready, weak pulse (or fading, big floating pulse in severe cases)"

      analysis: "Severe weakness of primary qi, separation of yin and yang, and exhaustion of qi in zang organs are indicated. Flaccid tongue and thready weak pulse suggest deficiency of blood and prostration of kidney yang. If complicated with cold limbs, flushed face, fading or big floating pulse, it indicates exhaustion of yin in lower portion and upward going of isolated yang - a critical case."

      treatment:
        principle: "Restore yang from collapse"
        method: "Points of Ren Meridian"
        needle_technique: "moxibustion"

        primary_points:
          - code: "REN-8"
            name: "Shenque"
            function: "Restore yang from collapse"
            technique: "Indirect moxibustion with salt"
          - code: "REN-6"
            name: "Qihai"
            function: "Strengthen primary qi, restore yang"
            technique: "Heavy moxibustion"
          - code: "REN-4"
            name: "Guanyuan"
            function: "Meeting point of Ren and three yin meridians, restore yang"
            technique: "Heavy moxibustion"

        supplementary_points: []

        explanation: "Shenque (Ren 8), Qihai (Ren 6) and Guanyuan (Ren 4) are located on lower abdomen along Ren Meridian and are main points effective for collapse. Heavy moxibustion applied on Guanyuan (Ren 4), a meeting point of Ren Meridian and three yin meridians, can strengthen primary qi and restore yang from collapse."

        modifications: []

    - pattern_name: "Attack on Meridians and Collaterals"
      pattern_type: "mixed"
      subcategory: "sequelae"

      manifestations:
        main_symptoms: ["Hemiplegia", "Numbness of limbs", "Deviated mouth", "Slurring of speech"]
        accompanying_symptoms: ["Headache", "Dizziness", "Vertigo", "Twitching of muscles", "Red eyes", "Flushed face", "Thirst", "Dryness of throat", "Irritability"]
        tongue: "Variable"
        pulse: "String-taut and rolling pulse"

      analysis: "Wind phlegm enters meridians and collaterals due to imbalance of yin and yang, or after treatment the functions of affected zang-fu organs have been restored but wind phlegm still blocks meridians and collaterals, causing retarded circulation of qi and blood. If complicated with upsurging of liver yang, symptoms include headache, dizziness, vertigo. If excessive fire in heart and liver, there may be red eyes, flushed face, thirst and irritability."

      treatment:
        principle: "Regulate qi and blood, remove obstruction from meridians and collaterals, reduce wind"
        method: "Points along Du Meridian and yang meridians of affected side"
        needle_technique: "even"

        primary_points:
          - code: "DU-20"
            name: "Baihui"
            function: "Eliminate wind, remove obstruction from meridians"
            technique: "Even movement, needle healthy side first then affected side"
          - code: "BL-7"
            name: "Tongtian"
            function: "Eliminate wind, remove obstruction"
            technique: "Even movement"
          - code: "DU-16"
            name: "Fengfu"
            function: "Du Meridian is sea of all yang meridians"
            technique: "Even movement"
          - code: "L.I.-15"
            name: "Jianyu"
            function: "Upper limb yang meridian point"
            technique: "Even movement"
          - code: "L.I.-11"
            name: "Quchi"
            function: "Upper limb yang meridian point"
            technique: "Even movement"
          - code: "SJ-5"
            name: "Waiguan"
            function: "Upper limb yang meridian point"
            technique: "Even movement"
          - code: "L.I.-4"
            name: "Hegu"
            function: "Upper limb yang meridian point"
            technique: "Even movement"
          - code: "GB-30"
            name: "Huantiao"
            function: "Lower limb yang meridian point"
            technique: "Even movement"
          - code: "GB-34"
            name: "Yanglingquan"
            function: "Lower limb yang meridian point"
            technique: "Even movement"
          - code: "ST-36"
            name: "Zusanli"
            function: "Lower limb yang meridian point"
            technique: "Even movement"
          - code: "ST-41"
            name: "Jiexi"
            function: "Lower limb yang meridian point"
            technique: "Even movement"

        supplementary_points:
          - condition: "Upward disturbance of wind yang"
            points:
              - code: "GB-20"
                name: "Fengchi"
                function: "Reduce wind and pacify liver"
              - code: "LIV-3"
                name: "Taichong"
                function: "Pacify liver (reducing)"
              - code: "KID-3"
                name: "Taixi"
                function: "Nourish kidney yin to support liver (reinforcing)"
              - code: "SP-6"
                name: "Sanyinjiao"
                function: "Nourish yin and pacify yang (reinforcing)"
          - condition: "Excessive fire in heart and liver"
            points:
              - code: "P-7"
                name: "Daling"
                function: "Eliminate fire (reducing)"
              - code: "LIV-2"
                name: "Xingjian"
                function: "Eliminate fire (reducing)"
              - code: "KID-3"
                name: "Taixi"
                function: "Nourish yin to reduce fire (reinforcing)"
          - condition: "Deviated mouth"
            points:
              - code: "ST-4"
                name: "Dicang"
                function: "Promote qi circulation in facial meridians"
              - code: "ST-6"
                name: "Jiache"
                function: "Promote qi circulation in facial region"

        explanation: "Du Meridian is sea of all yang meridians. Baihui (Du 20), Fengfu (Du 16) combined with Tongtian (B 7) eliminate wind and remove obstruction from meridians and collaterals. Yang meridians dominate exterior of body and qi, so points of yang meridians are selected to regulate qi and blood and promote smooth circulation in upper and lower portions of body. For upper disturbance of wind yang, Fengchi (G 20) and Taichong (Liv 3) reduce wind and pacify liver. Reinforcing Taixi (K 3) promotes production of kidney yin to nourish liver. Reinforcing Sanyinjiao (Sp 6) nourishes yin and pacifies yang. For excessive fire in heart and liver, reducing Daling (P 7) and Xingjian (Liv 2) eliminates fire, while reinforcing Taixi (K 3) nourishes yin to reduce fire. Dicang (S 4) and Jiache (S 6) promote free circulation of qi in meridians and collaterals around facial region."

        modifications: []

  differential_diagnosis:
    - disease: "Syncope"
      distinguishing_features: "Syncope involves sudden fainting with loss of consciousness but NO hemiplegia or deviated mouth. Consciousness is regained relatively quickly with no sequelae."
    - disease: "Epilepsy"
      distinguishing_features: "Epilepsy involves loss of consciousness accompanied by convulsions, expectoration of frothy saliva or yelling. When consciousness is regained, patient becomes normal as usual. Wind stroke has hemiplegia and facial paralysis."

  prognosis:
    general: "Prognosis varies. Attack on meridians and collaterals only has better prognosis. Tense syndrome may improve with treatment. Flaccid syndrome has poor prognosis, especially if untreated or improperly treated - tense syndrome tends to become flaccid."
    favorable_signs: ["Attack limited to meridians and collaterals", "Tense syndrome responding to treatment", "Younger patient", "Good underlying constitution"]
    unfavorable_signs: ["Flaccid syndrome", "Cold limbs with flushed face", "Fading or big floating pulse", "Both zang-fu organs and meridians affected", "Advanced age with multiple deficiencies"]

  prevention:
    lifestyle: ["Avoid overstraining", "Moderate diet", "Regulate emotions", "Limit alcohol", "Regular moderate exercise"]
    prophylactic_treatment: "Old aged with deficiency of qi and excessive phlegm, or manifestations of upsurging liver yang marked by dizziness and palpitations, may have premonitory symptoms such as stiff tongue, slurred speech and numbness of finger tips. Frequent moxibustion on Zusanli (S 36) and Xuanzhong (G 39) may prevent attack of wind stroke."

  remarks: "Wind stroke is an emergency case requiring immediate treatment. Attack on zang-fu organs is more severe than attack on meridians and collaterals. Among attacks on zang-fu organs, tense syndrome is excess-type while flaccid syndrome is deficiency-type, with flaccid syndrome having worse prognosis. After acute stage, sequelae such as hemiplegia, monoplegia, and aphasia may persist and require long-term rehabilitation treatment."

created: 2025-10-06
updated: 2025-10-06
---

# 🩺 Wind Stroke (中風)

## 📖 Overview

Wind stroke is an emergency condition characterized by **sudden onset** with loss of consciousness, or hemiplegia, slurred speech, and deviated mouth. The term "wind stroke" comes from the abrupt onset and rapidly changing pathological manifestations, similar to the nature of wind.

**Key Characteristics:**
- Abrupt, sudden onset (like wind)
- Loss of consciousness (in severe cases)
- Hemiplegia (paralysis of one side of body)
- Facial paralysis (deviated mouth and eye)
- Speech disturbance (slurred speech or aphasia)

**Onset:** Acute emergency presentation

---

## 🏥 Western Medicine Correlation

**Modern Diagnosis:**
- Cerebral hemorrhage
- Cerebral thrombosis
- Cerebral embolism
- Subarachnoid hemorrhage
- Stroke / CVA (Cerebrovascular Accident)

**Notes:**
After the acute stage is over, there may be sequelae such as hemiplegia, monoplegia, and aphasia requiring long-term rehabilitation.

---

## 🧬 Etiology & Pathogenesis

### Primary Causes

Wind stroke often occurs in the **aged who are in poor health**, with deficiency of qi and blood, or deficiency in the lower part of the body and excess in the upper part.

1. **Kidney Yin Deficiency:** Due to sexual indulgence, leading to deficiency of kidney yin
2. **Spleen Dysfunction:** Irregular food intake impedes transportation and transformation function of spleen, leading to production of phlegm from accumulated dampness and transformation into heat
3. **Emotional Triggers:** Exasperation, agitation leading to upsurge of liver yang and heart fire
4. **Dietary Excess:** Alcohol indulgence or overeating
5. **Overstrain and Stress:** Physical or mental exhaustion
6. **Exogenous Wind:** Invasion of exogenous pathogenic wind

### Contributing Factors
- Advanced age
- Poor underlying health
- Constitutional deficiency of qi and blood
- Imbalance pattern: deficiency in lower body with excess in upper body

### Pathological Mechanism

There appears **imbalance of yin and yang in the zang-fu organs**. Causative factors lead to **upsurge of liver yang and heart fire**, which makes qi and blood go upward together with turbid phlegm, **disturbing the mind** and resulting in this disease.

**In mild cases:** Only symptoms showing dysfunction of meridians and collaterals

**In severe cases:** Both dysfunction of zang-fu organs AND dysfunction of meridians and collaterals are manifested

**Affected Organs:**
- **Liver:** Liver yang upsurging, liver wind stirring
- **Heart:** Heart fire disturbing the mind
- **Kidney:** Kidney yin deficiency failing to anchor yang
- **Spleen:** Spleen dysfunction producing phlegm and dampness

**Qi & Blood Dynamics:**
Qi and blood rush upward together with turbid phlegm, causing obstruction and disturbance. In deficiency cases, qi is exhausted and fails to support consciousness. In excess cases, phlegm-fire blocks the orifices of the heart.

---

## 🔬 Pattern Differentiation

### Pattern 1: Attack on Zang-Fu Organs - Tense Syndrome (Excess Type)

**Type:** Excess
**Subcategory:** Tense

#### Main Manifestations
- Falling down in a fit with loss of consciousness
- Tightly closed hands and clenched jaws
- Flushed face
- Coarse breathing
- Rattling in the throat
- Retention of urine
- Constipation

**Tongue:** Red tongue with thick yellow or dark grey coating
**Pulse:** String-taut, rolling and forceful pulse

#### TCM Analysis

Wind stirred up by upsurge of liver yang sends qi and blood upwards, which together with the accumulated phlegm fire disturb the mind, leading to **sudden loss of consciousness** with tightly closed hands and clenched jaws, flushed face, coarse breathing, retention of urine and constipation.

Excessive wind phlegm brings about **rattling in the throat**.

Red tongue with thick yellow coating or dark grey coating, string-taut, rolling and forceful pulse are the signs of **wind combined with phlegm fire**.

---

### Pattern 2: Attack on Zang-Fu Organs - Flaccid Syndrome (Deficiency Type)

**Type:** Deficiency
**Subcategory:** Flaccid

#### Main Manifestations
- Falling down in a fit and sudden loss of consciousness
- Mouth agape and eyes closed
- Snoring but feeble breathing
- Flaccid paralysis of limbs
- Incontinence of urine

**Tongue:** Flaccid tongue
**Pulse:** Thready, weak pulse (or fading/big floating pulse in severe cases)

#### TCM Analysis

Severe weakness of primary qi, separation of yin and yang, and exhaustion of qi in the zang organs are indicated in mouth agape, eyes closed, snoring but feeble breathing, flaccid paralysis, and incontinence of urine.

Flaccid tongue and thready weak pulse suggest the **deficiency of blood and prostration of the kidney yang**.

If complicated with cold limbs, flushed face, fading or big floating pulse, it is a **critical case**, indicating exhaustion of yin in the lower portion of the body and upward going of the isolated yang.

---

### Pattern 3: Attack on Meridians and Collaterals

**Type:** Mixed

#### Main Manifestations
- Hemiplegia (paralysis of one side)
- Numbness of the limbs
- Deviated mouth
- Slurring of speech
- Headache, dizziness, vertigo (if liver yang upsurging)
- Twitching of muscles, red eyes, flushed face, thirst, dryness of throat, irritability (if fire in heart and liver)

**Tongue:** Variable
**Pulse:** String-taut and rolling pulse

#### TCM Analysis

Wind phlegm enters the meridians and collaterals due to imbalance of yin and yang, OR after treatment the functions of the affected zang-fu organs have been restored, but wind phlegm still blocks the meridians and collaterals, causing retarded circulation of qi and blood. Hence appears hemiplegia, numbness of the limbs, deviated mouth and slurring of speech.

If complicated with **upsurging of liver yang**, and upward disturbance of wind yang, the symptoms are headache, dizziness, vertigo and twitching of muscles.

If there is **excessive fire in the heart and liver**, there may be red eyes and flushed face, thirst, dryness of the throat and irritability.

Stagnation of wind phlegm in the meridians and collaterals leads to a string-taut and rolling pulse.

---

## 💉 Treatment Protocols

### Pattern: Tense Syndrome (Excess)

#### Treatment Principle
Promote resuscitation, reduce wind and fire, resolve phlegm

#### Method
Points of the Du Meridian, the Liver Meridian of Foot-Jueyin and the twelve Jing-Well points are selected as the main points

**Needle Technique:** Reducing method or pricking to cause little bleeding

#### Primary Points

| Point | Name | Function | Technique |
|-------|------|----------|-----------|
| [[DU-20]] | Baihui | Regulate qi of Du Meridian, effect resuscitation | Reducing |
| [[DU-26]] | Shuigou | Regulate qi of Du Meridian, effect resuscitation | Reducing |
| [[ST-40]] | Fenglong | Invigorate spleen/stomach functions, resolve turbid phlegm | Reducing |
| [[LIV-3]] | Taichong | Subdue upsurging qi in Liver Meridian, pacify liver yang | Reducing |
| [[KID-1]] | Yongquan | Conduct heat downward | Reducing |
| [[LU-11]] | Shaoshang | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |
| [[HE-9]] | Shaochong | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |
| [[P-9]] | Zhongchong | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |
| [[LI-1]] | Shangyang | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |
| [[SJ-1]] | Guanchong | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |
| [[SI-1]] | Shaoze | Dispel heat, regain consciousness (Jing-Well point) | Prick to bleed |

#### Supplementary Points

**For Clenched Jaws:**
- [[ST-7]] (Xiaguan) - Promote circulation of qi and blood
- [[ST-6]] (Jiache) - Relieve clenched jaws
- [[LI-4]] (Hegu) - Yangming meridian supply to cheeks

**For Aphasia and Stiffness of Tongue:**
- [[DU-15]] (Yamen) - Local point of tongue
- [[REN-23]] (Lianquan) - Adjacent point of tongue
- [[HE-5]] (Tongli) - Luo-Connecting point of Heart Meridian

#### Explanation

As the condition is due to **disturbance of the heart by phlegm fire** associated with upsurging of liver yang and upward flowing of qi and blood:

- **Baihui (Du 20) and Shuigou (Du 26)** are selected to regulate qi of the Du Meridian, effecting resuscitation
- **Yongquan (K 1)** is selected to conduct the heat downward
- **Taichong (Liv 3)** subdues the upsurging of qi in the Liver Meridian and pacifies the liver yang
- **Pricking the twelve Jing-Well points on both hands**, where qi of the three yin and three yang meridians meet, dispels heat and regains consciousness
- **The spleen and stomach are the source of phlegm production**. Fenglong (S 40), the Luo-Connecting point of the Stomach Meridian, can invigorate the functions of the spleen and stomach and help to resolve the turbid phlegm
- Since the **Yangming Meridians of Hand and Foot supply the cheeks**, Xiaguan (S 7), Jiache (S 6) and Hegu (LI 4) are chosen to promote the circulation of qi and blood for relieving the clenched jaws
- **Yamen (Du 15) and Lianquan (Ren 23)**, being local and adjacent points of the tongue, and **Tongli (H 5)**, the Luo-Connecting point of the Heart Meridian, may relieve stiffness of tongue

---

### Pattern: Flaccid Syndrome (Deficiency)

#### Treatment Principle
Restore yang from collapse

#### Method
Moxibustion is applied to points of the Ren Meridian

**Needle Technique:** Heavy moxibustion

#### Primary Points

| Point | Name | Function |
|-------|------|----------|
| [[REN-8]] | Shenque | Restore yang from collapse (indirect moxibustion with salt) |
| [[REN-6]] | Qihai | Strengthen primary qi, restore yang |
| [[REN-4]] | Guanyuan | Meeting point of Ren and three yin meridians, restore yang |

#### Explanation

Shenque (Ren 8), Qihai (Ren 6) and Guanyuan (Ren 4) are located on the lower abdomen along the Ren Meridian and are the **main points effective for collapse**.

Heavy moxibustion applied on **Guanyuan (Ren 4)**, a meeting point of the Ren Meridian and three yin meridians, can **strengthen the primary qi, and restore yang from collapse**.

---

### Pattern: Attack on Meridians and Collaterals

#### Treatment Principle
Regulate qi and blood, remove obstruction from the meridians and collaterals, reduce the wind

#### Method
Points along the Du Meridian and the yang meridians of the affected side are mainly used

**Needle Technique:** Even movement first from the healthy side and then the affected side

#### Primary Points

**Head:**

| Point | Name | Function |
|-------|------|----------|
| [[DU-20]] | Baihui | Eliminate wind, remove obstruction from meridians |
| [[BL-7]] | Tongtian | Eliminate wind, remove obstruction |
| [[DU-16]] | Fengfu | Du Meridian is sea of all yang meridians |

**Upper Limbs:**

| Point | Name | Function |
|-------|------|----------|
| [[LI-15]] | Jianyu | Regulate qi and blood in upper limb yang meridians |
| [[LI-11]] | Quchi | Regulate qi and blood in upper limb yang meridians |
| [[SJ-5]] | Waiguan | Regulate qi and blood in upper limb yang meridians |
| [[LI-4]] | Hegu | Regulate qi and blood in upper limb yang meridians |

**Lower Limbs:**

| Point | Name | Function |
|-------|------|----------|
| [[GB-30]] | Huantiao | Regulate qi and blood in lower limb yang meridians |
| [[GB-34]] | Yanglingquan | Regulate qi and blood in lower limb yang meridians |
| [[ST-36]] | Zusanli | Regulate qi and blood in lower limb yang meridians |
| [[ST-41]] | Jiexi | Regulate qi and blood in lower limb yang meridians |

#### Supplementary Points

**For Upward Disturbance of Wind Yang:**
- [[GB-20]] (Fengchi) - Reduce wind and pacify liver (reducing)
- [[LIV-3]] (Taichong) - Pacify liver (reducing)
- [[KID-3]] (Taixi) - Nourish kidney yin to support liver (reinforcing)
- [[SP-6]] (Sanyinjiao) - Nourish yin and pacify yang (reinforcing)

**For Excessive Fire in Heart and Liver:**
- [[P-7]] (Daling) - Eliminate fire (reducing)
- [[LIV-2]] (Xingjian) - Eliminate fire (reducing)
- [[KID-3]] (Taixi) - Nourish yin to reduce fire (reinforcing)

**For Deviated Mouth:**
- [[ST-4]] (Dicang) - Promote qi circulation in facial meridians
- [[ST-6]] (Jiache) - Promote qi circulation in facial region

#### Explanation

**Du Meridian is the sea of all yang meridians.** Baihui (Du 20), Fengfu (Du 16) combined with Tongtian (B 7) can eliminate wind and remove obstruction from the meridians and collaterals.

Since the **yang meridians dominate the exterior of the body and qi**, points of the yang meridians are selected to regulate qi and blood of the body and promote smooth circulation in the upper and lower portions of the body.

For the **upper disturbance of wind yang**, Fengchi (G 20) and Taichong (Liv 3) are selected to reduce the wind and pacify the liver. Reinforcing applied to Taixi (K 3) promotes the production of the kidney yin to nourish the liver. Reinforcing applied to Sanyinjiao (Sp 6) nourishes yin and pacifies yang.

For **excessive fire in the heart and liver**, reducing Daling (P 7) and Xingjian (Liv 2) can eliminate the fire, while reinforcing to Taixi (K 3) nourishes yin to reduce the fire.

Dicang (S 4) and Jiache (S 6) are selected for the purpose of promoting a free circulation of qi in the meridians and collaterals around the facial region.

---

## 🔍 Differential Diagnosis

### vs. [[Syncope]]

**Distinguishing Features:**
- **Syncope:** Loss of consciousness is brief and temporary. NO hemiplegia or deviated mouth. Usually there are NO sequelae after restoration to consciousness.
- **Wind Stroke:** Loss of consciousness is complicated by hemiplegia and deviated mouth. Usually there ARE sequelae after restoration to consciousness.

### vs. [[Epilepsy]]

**Distinguishing Features:**
- **Epilepsy:** Loss of consciousness is accompanied by convulsions, expectoration of frothy saliva or yelling. When the consciousness is regained the patient becomes as normal as usual. NO hemiplegia or facial paralysis.
- **Wind Stroke:** Has hemiplegia, deviated mouth, and sequelae persist after consciousness returns.

---

## 📊 Prognosis

Prognosis varies depending on severity and pattern.

**General Outlook:**
- Attack limited to meridians and collaterals: Better prognosis
- Tense syndrome (excess): May improve with proper treatment
- Flaccid syndrome (deficiency): Poor prognosis
- **Untreated or improperly treated tense syndrome tends to become flaccid** - prognosis is often poor

**Favorable Signs:**
- Attack limited to meridians and collaterals only (no zang-fu organ involvement)
- Tense syndrome responding well to treatment
- Younger patient age
- Good underlying constitution
- No critical signs (normal pulse, no extreme flushing)

**Unfavorable Signs:**
- Flaccid syndrome manifestation
- Cold limbs with flushed face
- Fading or big floating pulse
- Both zang-fu organs and meridians affected
- Advanced age with multiple deficiencies
- Exhaustion of yin with upward-going isolated yang

---

## 🛡️ Prevention & Prophylaxis

### Lifestyle Recommendations
- Pay attention to diet and lifestyle
- Avoid overstraining and overstress
- Moderate alcohol consumption (or abstain)
- Regulate food intake - avoid overeating
- Manage emotional stress and agitation
- Regular moderate physical activity

### Prophylactic Treatment

**High-Risk Individuals:**
The old aged with:
- Deficiency of qi and excessive phlegm
- Manifestations of upsurging of liver yang marked by dizziness and palpitations
- **Premonitory symptoms**: stiff tongue, slurred speech, numbness of the finger tips

**Preventive Acupuncture:**
Frequent moxibustion on:
- [[ST-36]] (Zusanli) - Strengthen qi and blood
- [[GB-39]] (Xuanzhong) - Nourish marrow, benefit brain

This prophylactic moxibustion may **prevent an attack of wind stroke**.

---

## ⚠️ Clinical Remarks

**Emergency Treatment:**
Wind stroke is an **emergency case** requiring immediate treatment. Do not delay.

**Severity Levels:**
- **Attack on zang-fu organs** is MORE severe than attack on meridians and collaterals
- Among attacks on zang-fu organs:
  - **Tense syndrome** = excess-type (better prognosis)
  - **Flaccid syndrome** = deficiency-type (poor prognosis)

**Sequelae:**
After the acute stage is over, there may be sequelae such as:
- Hemiplegia (paralysis of one side)
- Monoplegia (paralysis of one limb)
- Aphasia (loss of speech)
- Facial paralysis

These require **long-term rehabilitation treatment** focusing on attack on meridians and collaterals protocol.

**Pattern Transformation:**
In untreated or improperly treated cases, the tense syndrome tends to become flaccid and the prognosis is often poor. Close monitoring is essential.

---

## 📚 Related Information

**Related Patterns:** [[Liver Yang Rising]] | [[Phlegm-Fire Disturbing the Heart]] | [[Kidney Yin Deficiency]]
**Related Diseases:** [[Syncope]] | [[Epilepsy]] | [[Headache]] | [[Dizziness]]
**Key Concepts:** [[Wind (Exogenous Factor)]] | [[Phlegm]] | [[Liver Qi Stagnation]]
**Common Formulas:** (TCM herbal formulas would be listed here if mentioned in source text)

**Chapter Reference:** Chapter 17 - Internal Diseases

---

## 📖 Case Studies / Clinical Notes

*This section can be used for recording personal clinical observations, treatment outcomes, and patient case studies.*

---

*Source: Chinese Acupuncture and Moxibustion (Xinnong), Chapter 17*
*Last updated: 2025-10-06*
