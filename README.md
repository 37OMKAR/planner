# Eventora — AI-Assisted Event & Operations Planner

[![Tests: Passing](https://img.shields.io/badge/Tests-18%2F18%20Passed-brightgreen.svg)](tests/test_core.py)
[![Model: Gemini 3.8 Flash](https://img.shields.io/badge/Model-Gemini%203.8%20Flash-blue.svg)](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Build Bloat](https://img.shields.io/badge/Size-%3C%202%20MB-success.svg)](https://github.com/37OMKAR/planner)

Eventora is a smart, dynamic event operations assistant built for everyday hosts, athletic tournament directors, community organizers, and corporate event planners. It eliminates fragmented spreadsheets and vendor friction by combining real-time mathematical logistics (banquet tables, dietary buffers, beverage servings), proportional budget allocations, interactive SVG data visualizers, date-relative timelines, and contextual suggestions powered by **Google Gemini 3.8 Flash** with an offline deterministic fallback.

---

## Table of Contents
1. [Challenge Vertical & Problem Statement](#1-chosen-vertical--problem-statement)
2. [Architecture, Approach & Logic](#2-architecture-approach--logic)
3. [How the Solution Works](#3-how-the-solution-works)
4. [Stitch AI Design Prototypes](#4-stitch-ai-design-prototypes)
5. [Evaluation Criteria Alignment](#5-evaluation-criteria-alignment)
6. [Assumptions Made](#6-key-assumptions-made)
7. [Running Locally & Automated Testing](#7-running-locally--automated-testing)
8. [Security, Privacy, and Accessibility](#8-security-privacy-and-accessibility)
9. [Deployment](#9-deployment-to-github-pages)

---

## 1. Chosen Vertical & Problem Statement

- **Chosen Vertical**: **Smart Event & Operations Assistant / Productivity**
- **Target Persona**: Event planners, athletics coordinators, wedding/community hosts, and corporate teams managing multi-stakeholder gatherings.
- **Problem Statement**:
  Event management typically suffers from three major pain points:
  1. **Logistics Guesswork**: Hosts struggle to compute table layouts, catering dietary buffers, and beverage volumes, leading to food waste or shortages.
  2. **Budget Fragmentation**: Budgeting across venue, catering, decor, entertainment, and safety contingencies is often scattered across messy spreadsheets.
  3. **High Latency & Fragile Tooling**: Heavy frameworks require slow builds and internet connectivity, failing on-site at convention centers or outdoor venues.
- **The Eventora Solution**:
  A zero-dependency, ultra-fast web application that gives organizers an instant command center: live countdowns, proportional SVG budget charts, deterministic calculators, customizable checklists, physical run-of-show print sheets, and creative suggestions from Google Gemini 3.8 Flash.

---

## 2. Architecture, Approach & Logic

### System Architecture Flow
```
[User Input: Type, Date, Location, Guests, Budget, Notes, Optional Gemini Key]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   [Deterministic Logic Engine]          [Google Gemini 3.8 Flash]
   ├── Proportional Budget Splits        └── Bespoke Themes & Run-of-Show
   ├── Logistics Estimators (Tables/Plates)     (Ephemeral In-Memory Key)
   └── Date-Relative Timeline Checkpoints
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
        [Interactive Responsive Dashboard & Visualizers]
        ├── SVG Interactive Donut Chart with Hover Slice Metrics
        ├── Real-Time Millisecond Countdown Ticker
        ├── Filterable Task Checklist (Venue, Guests, Catering, etc.)
        ├── Synthesized Web Audio & Web Haptic Feedback
        └── Canvas Confetti Celebration Engine
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
[Browser LocalStorage & JSON Export]     [1-Click Physical Print Mode]
```

### Core Algorithms & Logic
1. **Mathematical Logistics Heuristics**:
   - **Table Calculation**: `ceil(Guests / 8)` ensures optimal 8-top banquet round utilization.
   - **Beverage Buffer**: Computes `ceil(Guests * 3.0)` servings for standard 4-hour events.
   - **Catering Buffer**: Applies a strict `ceil(Guests * 1.15)` formula (15% buffer) guaranteeing coverage for special dietary and vendor meals without excessive food waste.
   - **Accessible Seating**: Dynamically allocates 10% dedicated accessible / quiet seating.
2. **Proportional Budget Allocation Engine**:
   - Automatically breaks down gross budgets based on industry standards:
     - Venue & Rentals: 40%
     - Catering & Beverage: 25%
     - Decor & Ambiance: 15%
     - Entertainment & Sound: 10%
     - Photography & Media: 5%
     - Contingency & Safety: 5%
3. **Date-Relative Milestones**:
   - Calculates milestone dates backwards from the user's event date (e.g., `-60d` venue lock, `-30d` catering finalization, `-14d` schedule walkthrough, `-1d` pack emergency kit).

---

## 3. How the Solution Works

1. **Planning Snapshot & Dashboard**:
   - Real-time countdown ticker calculating days, hours, minutes, and seconds to the next celebration.
   - Summary stat cards showing aggregated budget across all plans, days remaining, and task completion progress.
2. **Dynamic Event Plan Generator**:
   - Inputs for Event Title, Type (Wedding, Birthday, Tournament, Community, Anniversary, Corporate), Date, Location, Guest Count, and Currency.
   - Supports optional Gemini API Key: when entered, queries `gemini-3.8-flash` for tailored event advice; without a key or offline, instantly uses robust built-in templates.
3. **Tactile & Celebratory User Experience**:
   - Integrated synthesized Web Audio clicks (no audio assets loaded from disk/network).
   - `navigator.vibrate` haptic pulses on mobile devices.
   - Custom 60fps canvas confetti engine celebrating plan generation and 100% task list completion.
4. **Interactive Budget Visualizer**:
   - Dynamic SVG Donut Chart with real-time hover inspection, active segment highlights, and visual category breakdown progress bars.
5. **Vendor & Task Operations Checklist**:
   - Category filtering: *All*, *Venue*, *Guests*, *Catering*, *Decor*, *Accessibility*, and *Custom*.
   - Preset buttons to add common essentials: Weather contingency, allergen labels, sound check, and first aid kits.
6. **1-Click Printable Run-of-Show (`@media print`)**:
   - Clean, ink-efficient print layout formatted for on-site managers, floor staff, and vendors.

---

## 4. Stitch AI Design Prototypes

The project incorporates 6 high-fidelity design prototypes generated via **Google Stitch** (`projects/3081715783145629955`), saved in [`stitch_screens/`](stitch_screens/):

| Screen | Title / Role | Format | Key Elements |
| :--- | :--- | :--- | :--- |
| **Screen 1** | **Eventora.OS — Championship Athletic Planner** | Desktop (2560x3426) | Hero dashboard, high-energy sports visual hierarchy, real-time stat board, dark mode typography. |
| **Screen 2** | **Eventora.OS — Gemini Studio** | Desktop (1280x1742) | AI prompt interface, generative idea cards, context controls. |
| **Screen 3** | **Eventora.OS — Timeline & Tasks** | Desktop (1280x2040) | Gantt-style timeline milestones, vendor checklist cards, status chips. |
| **Screen 4** | **Eventora.OS — Budget & Cap** | Desktop (1280x1774) | Proportional spending caps, donut distribution, variance tracking. |
| **Screen 5** | **Eventora.OS — Create Plan Form** | Desktop (1280x1710) | Multi-field event creation wizard, date picker, budget sliders. |
| **Screen 6** | **Eventora — AI Event Planner Mobile App** | Mobile (390x884) | Responsive mobile view, bottom navigation bar, quick touch targets. |

*Full code (`.html`), visual screenshots (`.png`), and metadata index are available in [`stitch_screens/manifest.json`](stitch_screens/manifest.json).*

---

## 5. Evaluation Criteria Alignment

### High Impact: Logical Decision-Making & Practical Usability
- **Context-Sensitive Calculations**: Logistics adapt to both scale (small 10-person dinners vs 500-person tournaments) and budget tiers.
- **Fail-Safe Offline Reliability**: Organizers in convention centers with poor WiFi can rely 100% on built-in deterministic planning heuristics.

### Medium Impact: Code Quality & Architecture
- **Zero-Bloat Vanilla Implementation**: HTML5, Vanilla CSS3, and ES6+ JavaScript. No build step, no 200MB `node_modules`, no framework hydration delays.
- **Maintainable Structure**: Clear separation between UI rendering, math heuristics, audio/haptic synthesis, and persistence logic.

### Medium Impact: Security & Privacy
- **Ephemeral API Keys**: User-provided Gemini API keys exist strictly in transient memory during requests. Keys are **never** persisted to `localStorage`, cookies, or remote logs.
- **Sanitized DOM Injection**: Strict HTML entity escaping (`escapeHtml()`) applied to all dynamic data, preventing Cross-Site Scripting (XSS).

### Low Impact & Polish: Testing & Accessibility
- **Automated Test Coverage**: 18 automated unit and contract tests in `tests/test_core.py` covering arithmetic formulas, date timelines, security escaping, and DOM landmarks.
- **WCAG 2.1 Compliance**: High-contrast focus outlines (`:focus-visible`), ARIA live regions (`aria-live="polite"`), semantic landmark tags, and `@media (prefers-reduced-motion: reduce)` support.

---

## 6. Key Assumptions Made

1. **Client-Side Data Sovereignty**: All event plans and checklist states are stored locally in the user's browser via `localStorage` and JSON export; no third-party database is required.
2. **Ephemeral AI Credentials**: Users bring their own optional Google AI Studio Gemini API key; it is never transmitted to any third party except Google's official Gemini endpoint.
3. **Lightweight Footprint**: Kept strictly under 2 MB total repository size (well under the 10 MB hackathon ceiling) for instantaneous deployment.

---

## 7. Running Locally & Automated Testing

### Running Locally
No build process, compiler, or npm installation needed. Simply open `index.html` in any modern browser, or run Python's built-in static server:

```bash
# Start local static server
python -m http.server 8000
```
Open `http://localhost:8000` in your web browser.

### Running Automated Tests
Run the comprehensive test suite verifying arithmetic calculations, sanitization, and UI integrity:

```bash
python -m unittest tests/test_core.py -v
```

**Expected output:**
```
test_accessible_seating_allocation (tests.test_core.TestEventoraCore) ... ok
test_beverage_calculation (tests.test_core.TestEventoraCore) ... ok
test_budget_proportions_sum_to_100 (tests.test_core.TestEventoraCore) ... ok
test_catering_buffer_calculation (tests.test_core.TestEventoraCore) ... ok
test_html_escaping_prevents_xss (tests.test_core.TestEventoraCore) ... ok
test_table_calculation (tests.test_core.TestEventoraCore) ... ok
...
Ran 18 tests in 0.007s
OK
```

---

## 8. Security, Privacy, and Accessibility

- **No Cookies or Tracking**: Zero external analytics or trackers.
- **Security Boundaries**: Ephemeral memory-only Gemini API key lifecycle.
- **Screen Reader Friendly**: Full ARIA labels on all interactive buttons, calculators, and countdown timers.
- **Motion Accessibility**: Reduced-motion media queries disable confetti and animations for users sensitive to motion.

---

## 9. Deployment to GitHub Pages

1. Open your repository on GitHub: [`https://github.com/37OMKAR/planner`](https://github.com/37OMKAR/planner)
2. Go to **Settings** → **Pages**.
3. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **`main`**
   - Folder: **`/ (root)`**
4. Click **Save**. Your site will be live at:
   ```
   https://37omkar.github.io/planner/
   ```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


