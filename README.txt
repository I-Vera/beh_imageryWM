# Cognitive Tasks Dataset: Working Memory and Mental Imagery

## 1. OVERVIEW

This dataset contains behavioral data from 21 participants who completed four cognitive tasks designed to assess working memory, mental imagery, and color discrimination abilities. All tasks were administered on the same day using PsychoPy software (version 2022.5.5).

The study focuses on object and spatial imagery capabilities, working memory capacity (both spatial and object-based), and mental rotation abilities. Participants were screened for normal color vision and absence of aphantasia/hyperphantasia using the Farnsworth-Munsell 100 Hue Test and Vividness of Object and Spatial Imagery (VOSI) questionnaire.

**Key Dataset Characteristics:**

| Attribute | Value |
|-----------|-------|
| Number of participants | 21 (7 male, 16 female) |
| Age range | 22–39 years (M = 26.05, SD = 4.60) |
| Participant population | University students |
| Data collection date | [Insert date(s)] |
| Total procedure duration | ~70–75 minutes |
| Software | PsychoPy 2022.5.5 |
| Effect sizes | Mental rotation f = 0.365; Spatial n-back f = 0.3–0.7 |
| Statistical power | 75% (for f = 0.25, α = 0.05, ANOVA repeated measures) |

---

2. EXPERIMENT DETAILS

### Participant Screening

All participants were recruited from social media networks and underwent a qualification stage before the main experiment:

1. **Demographic information collection**
2. **VOSI questionnaire** (69 questions): Screened for aphantasia/hyperphantasia; participants with scores below 1.5 or above 4.5 on both object and spatial vividness scales were excluded
3. **Farnsworth-Munsell 100 Hue Test**: Screened for color discrimination ability; participants with Total Error Score (TES) > 100 were excluded (2 participants excluded out of 23 original)

**Exclusion criteria:** Neurodegenerative diseases, affective disorders, epilepsy, color vision disorders (color blindness), aphantasia, hyperphantasia, autism spectrum disorders, schizophrenia spectrum disorders.

---

### Tasks

#### 1. Spatial n-back (SS)

**Purpose:** Assess spatial working memory and the ability to update/manipulate spatial information over time.

**Procedure:**
- 4×5 grid (20 possible locations) with a red dot appearing at one cell
- Dot appears for 3 seconds, 8 times per series (changing locations)
- **2-back variation**: Participants press "left" or "right" if the location 2 steps back was the same or different
- Response expected starting from 3rd location
- Fixation cross displayed for 6 seconds between series
- 1 training series + 36 main series
- One series: 24 seconds; Total task: ~20 minutes

**Expected effect size:** Medium to large (f = 0.3–0.7 in large samples)

---

#### 2. Color-Matching Task (CMT)

**Purpose:** Measure mental attentional capacity and object working memory capacity through parametric manipulation of task difficulty.

**Procedure:**
- **CMT-balloon version** only (cosidering misleading features not a concern)
- 3×3 grids of colored squares, each presented for 2 seconds
- Participants press "left" or "right" if the set of colors matches the previous figure (positions irrelevant)
- Fixation cross displayed for 1 second between series
- 1 training series + 6 main series in blocks:
  - Block 1: 4 color sets (2 relevant colors)
  - Block 2: 5 color sets (3 relevant colors)
  - Block 3: 6 color sets (4 relevant colors)
- Total task: ~8 minutes

**Reference:** Arsalidou et al. (2010)

---

#### 3. Missing Color Task (MCT)

**Purpose:** Assess individual ability for object imagination (novel task developed for this study).

**Procedure:**
- Two color sequences presented sequentially:
  - Reference set: 4 stimulus colors
  - Test set: 4 colors with one "missing" (empty square) in position 2 or 3
- Both sequences follow the same logical rule (dark→light, light→dark, or random tone order)
- Colors from "2014 Material Design color palettes" library (17 shades × 4 tones: 50, 300, 600, 900)
- Sequences presented for 2.5 seconds each, masked for 1 second, fixation cross for 0.5 seconds
- Two answer options presented; participant chooses the logically missing color ("left" or "right")
- Response time limited to 5 seconds
- **Difficulty levels:**
  - High: distractor 100 points from correct (same shade)
  - Low: distractor 200 points from correct (same shade)
  - No difficulty: distractor 2 shades away
- 4 training probes (with feedback) + 120 main trials (no feedback)
- Training: 1 minute; Main part: 24 minutes; Total: ~25 minutes

**Design criteria:**
- Only object representations (color, texture) involved; no spatial/location information
- Non-verbalized colors to avoid verbal categorization
- Minimizes memory/perception effects (edge, contrast, novelty)

---

#### 4. Mental Rotation (MR)

**Purpose:** Measure ability to mentally manipulate and rotate 2D/3D objects.

**Procedure:**
- Pairs of 3D geometric shapes presented at various rotation angles
- Participants press "left" if figures are the same, "right" if mirror images
- **Angle disparities:** 60°, 105°, 150° (avoiding 180° and <40° effects)
- Figures presented for 5 seconds
- Fixation cross: 0.5 seconds between trials
- 6 training problems (1 reference figure) + 216 main trials
  - 9 standard figures × 2 variations (clockwise/counterclockwise) × 2 answers (same/different) × 3 angles
- Total task: ~19.8 minutes (20.4 with training)

**Expected effect size:** f = 0.365

**Reference:** Shepard & Metzler (1971); Kessler & Thomson (2010)

---

### Procedure Timeline

| Stage | Duration |
|-------|----------|
| Qualification (VOSI + FM 100 Hue) | Variable |
| Spatial n-back + Color-matching (Block 1) | ~28 minutes |
| Missing color + Mental rotation (Block 2) | ~45 minutes |
| Breaks between sections | 10–30 minutes (optional) |
| **Total** | **70–75 minutes** |

**Instructions:**
- Tasks presented on black background with white text
- Viewing distance: 45–65 cm from screen
- All inputs from keyboard
- Random task order within blocks to avoid sequence effects
- Training + instruction before each task

---

### References

- Arsalidou, M., et al. (2010). Visuospatial working memory task.
- Blazhenkova, O., et al. (2025). VOSI questionnaire development.
- Farnsworth, M. (1943). Farnsworth-Munsell 100 Hue Test.
- Farah, M., et al. (1984). Object vs. spatial imagery.
- Kinnear, K., & Sahraie, A. (2002). Color vision assessment standards.
- Kessler, G., & Thomson, L. (2010). Mental rotation angle effects.
- Lejbak, L., et al. (2011). Spatial n-back task.
- Pierce, J., et al. (2019). PsychoPy software.
- Shepard, R., & Metzler, J. (1971). Mental Rotation Test.

---
