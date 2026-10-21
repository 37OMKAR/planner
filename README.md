# Eventora — AI-assisted event planner

A responsive, lively single-page web app for organizing weddings, birthdays, community gatherings, anniversaries, and other celebrations. Features budget allocation, interactive SVG donut charts, date-relative timelines, vendor questions, a task checklist with category filtering, guest & setup calculators, live countdown timers, tactile haptic & sound feedback, celebratory particle animations, dark/light theme switching, 1-click printable itineraries, browser-local persistence, and JSON backup export.

## Key Features

- **Lively & Tactile UX**: Integrated click haptics (`navigator.vibrate`) and synthesized Web Audio micro-clicks (zero audio files, zero network overhead) with a 1-click toggle.
- **Celebratory Moments**: In-house lightweight 60fps canvas confetti engine celebrating plan generation and task list completion.
- **Interactive Budget Visualizer**: SVG donut chart with interactive slice tooltips, center summary, and horizontal category distribution progress bar.
- **Live Event Countdown**: Real-time ticker counting days, hours, minutes, and seconds until the next celebration.
- **Guest & Setup Quick Estimator**: Live calculation of banquet tables (8-top), beverage servings, catering plates (+15% dietary buffer), and accessible/quiet seating.
- **Refined Typography & Themes**: Open-source Google Fonts (*Plus Jakarta Sans* and *Playfair Display*) with native fallback, paired with warm paper and midnight dark themes.
- **Vendor Checklist & Category Filters**: Filter by Venue, Catering, Decor, Accessibility, or Custom tasks with quick-add preset buttons.
- **1-Click Print & PDF Mode**: Dedicated `@media print` stylesheet producing clean physical event run-of-show sheets for hosts and on-site staff.
- **AI-Powered or Offline Templates**: Generates personalized plans via Google's `gemini-3.8-flash` or built-in deterministic planning templates when offline or without an API key.

## Run locally

No Node.js, build step, or package manager is required. Open `index.html` in any modern web browser, or serve the directory with any static web server:

```bash
# Python built-in static server
python -m http.server 8000
```

The entire application runs under 65 KB, respects offline execution, and requires zero external runtime scripts.

## Run automated tests

Run standard-library contract and unit tests verifying accessibility, arithmetic, input validations, security boundaries, and interactive features:

```bash
python -m unittest tests/test_core.py
```

## Optional Gemini AI

1. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. Select **Plan an event**, enter your event details, paste your key in the optional Gemini API key field, and generate the plan.
3. The app sends event details to Google's Gemini API using `gemini-3.8-flash`. The key is kept strictly in memory for the session and is never saved to local storage, cookies, or source code.
4. No key? The built-in deterministic event planning templates ensure 100% full functionality.

Official model reference: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

## Deploy to GitHub Pages

1. Create a **public** repository named `eventora-ai-planner` on GitHub (total repo size is < 100 KB, well under the 10 MB limit).
2. Push or upload `index.html`, `README.md`, `LICENSE`, and `tests/` at the repository root.
3. Go to **Settings → Pages**, select **Deploy from a branch**, choose `main` and `/ (root)`, then save.
4. Wait for the GitHub Pages deployment to complete.

## Security, Privacy, and Accessibility

- **Zero Tracking**: No tracking beacons, analytics scripts, or cookies.
- **Data Protection**: Event plans are stored solely in the user's browser `localStorage`.
- **Ephemeral Credentials**: Gemini API keys exist only in transient memory during requests and are never persisted.
- **XSS Prevention**: All dynamic fields and AI outputs are strictly sanitized via HTML entity escaping.
- **WCAG 2.1 Compliance**: High-contrast focus outlines (`:focus-visible`), ARIA live regions, semantic landmarks, and full `@media (prefers-reduced-motion: reduce)` support.

## License

MIT. See `LICENSE`.
