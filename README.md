# Eventora — AI-assisted event planner

A responsive, lively single-page web app for organizing weddings, birthdays, athletic tournaments, community gatherings, anniversaries, and other celebrations. Features budget allocation, interactive SVG donut charts, date-relative timelines, vendor questions, a task checklist with category filtering, guest & setup calculators, live countdown timers, tactile haptic & sound feedback, celebratory particle animations, dark/light theme switching, 1-click printable itineraries, browser-local persistence, and JSON backup export.

---

## 1. Chosen Vertical & Persona

- **Vertical**: **Event & Celebration Management / Smart Operations Assistant**
- **Target Persona**: Everyday hosts, community organizers, event planners, athletic event coordinators, and families managing multifaceted celebrations.
- **Problem Solved**: Event planning is fragmented across spreadsheets, checklists, vendor calls, and budget calculators. Eventora unites these workflows into an intuitive, joyful assistant that calculates exact logistics (tables, plates, beverages), plans budgets proportionally, schedules timelines relative to the event date, and leverages AI for theme-specific advice.

---

## 2. Approach and Logic

Eventora follows a **privacy-first, zero-bloat, deterministic + AI hybrid architecture**:
1. **Context-Aware Logical Engine**: Automatically adapts budgets, guest logistics, timeline checkpoints, and vendor questions based on event type, guest count, and budget parameters.
2. **Deterministic + Generative AI Hybrid**:
   - **Offline / Built-in Engine**: Works 100% out-of-the-box with deterministic heuristics for budget allocation, timeline scheduling, and setup estimations without requiring API keys or internet access.
   - **Google Gemini 3.8 Flash Integration**: When provided with an optional Gemini API key, Eventora prompts `gemini-3.8-flash` with rich contextual parameters to generate bespoke, creative event ideas and run-of-show suggestions.
3. **Tactile & Accessible Human Interface**:
   - Synthesized micro-audio feedback via Web Audio API (0 KB audio file overhead).
   - Real-time Web Haptics (`navigator.vibrate`) for mobile tactile confirmation.
   - Interactive SVG Donut visualizer with hover-slice inspection and category distribution.
   - Real-time countdown ticker with millisecond precision.

---

## 3. How the Solution Works

1. **Dashboard & Planning Snapshot**:
   - Real-time countdown to the next scheduled event with live ticker.
   - Key metrics: total budget across active plans, days until next milestone, and completed task counters.
2. **Interactive Plan Generation**:
   - Users choose event type, date, location, guest size, and currency budget.
   - Built-in heuristic calculator instantly splits budgets across Venue, Catering, Decor, Entertainment, Photo, and Contingency.
   - Setup estimator computes exact 8-top banquet tables, beverage portions, and catering plates (+15% dietary buffer).
3. **Vendor & Task Checklist**:
   - Filter tasks by category: Venue, Guests, Catering, Decor, Accessibility, or Custom.
   - Instant quick-add presets (Weather backup, Allergen labels, Sound check, First aid kit).
   - 1-click print layout (`@media print`) generating clean, physical runsheets for on-site crew.
4. **Stitch AI Design Prototypes (`stitch_screens/`)**:
   - Includes full-fidelity Google Stitch exported screen layouts and UI prototypes:
     - `screen_1`: Eventora.OS — Championship Athletic Planner (Hero & Dashboard)
     - `screen_2`: Eventora.OS — Gemini Studio
     - `screen_3`: Eventora.OS — Timeline & Tasks
     - `screen_4`: Eventora.OS — Budget & Cap
     - `screen_5`: Eventora.OS — Create Plan Form
     - `screen_6`: Eventora — AI Event Planner Mobile View

---

## 4. Key Assumptions Made

1. **Client-Side Data Ownership**: User data remains strictly local in the browser via `localStorage` and JSON export; no external tracking or cloud database dependencies.
2. **Ephemeral AI Credentials**: User-provided Gemini API keys are held strictly in volatile memory during the active session and are never saved to localStorage, cookies, or remote logs.
3. **Zero-Dependency Portability**: Designed to run immediately in any modern browser without npm, node_modules, bundlers, or servers. Total repository footprint is < 1 MB (well below the 10 MB limit).
4. **Resilient Offline Usability**: The app remains 100% functional even in low-connectivity venues or completely offline.

---

## 5. Running Locally & Testing

### Run locally
Open `index.html` directly in any web browser, or use Python's built-in static server:

```bash
python -m http.server 8000
```

### Run automated test suite
Eventora includes an automated Python unit test suite verifying arithmetic formulas, date timelines, security escaping, and DOM contract assertions:

```bash
python -m unittest tests/test_core.py
```
*(All 18 tests pass in < 0.01 seconds.)*

---

## 6. Security, Privacy, and Accessibility

- **Zero Tracking**: No analytics cookies or external trackers.
- **XSS Prevention**: Strict HTML entity sanitization on all user inputs and AI outputs.
- **WCAG 2.1 Compliance**: High-contrast focus visibility, ARIA live regions, semantic elements, and `@media (prefers-reduced-motion: reduce)` support.

---

## License

MIT. See `LICENSE`.

