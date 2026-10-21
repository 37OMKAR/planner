"""Small, dependency-free source-contract checks for Eventora's static app."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

class EventoraSourceTests(unittest.TestCase):
    def test_document_has_responsive_viewport_and_language(self):
        self.assertIn('<html lang="en">', HTML)
        self.assertIn('name="viewport"', HTML)
        self.assertIn('@media(max-width:660px)', HTML)

    def test_every_navigation_target_exists(self):
        targets = re.findall(r'data-page="([^"]+)"', HTML)
        for target in targets:
            self.assertRegex(HTML, rf'<section class="page(?: active)?" id="{re.escape(target)}"')

    def test_budget_percentages_sum_to_100(self):
        nums = [int(x) for x in re.findall(r"\['[^']+',\s*(\d+),\s*'#[0-9a-f]+'\]", HTML)]
        self.assertEqual(nums, [30, 28, 15, 10, 9, 8])
        self.assertEqual(sum(nums), 100)

    def test_input_validation_exists(self):
        for text in ['Choose today or a future date.', 'Budget must be between', 'Guest count must be from 2']:
            self.assertIn(text, HTML)

    def test_client_key_not_written_to_storage(self):
        self.assertIn("const STORAGE_KEY='eventora.v1'", HTML)
        self.assertNotIn("localStorage.setItem('geminiKey'", HTML)
        self.assertIn("document.getElementById('geminiKey').value.trim()", HTML)

    def test_html_escaping_covers_common_special_characters(self):
        self.assertIn('function esc(s)', HTML)
        self.assertIn("'&amp;'", HTML)
        self.assertIn("'&#39;'", HTML)

    def test_export_and_task_actions_are_present(self):
        self.assertIn('function exportData()', HTML)
        self.assertIn("addTaskForm').addEventListener('submit'", HTML)
        self.assertIn('data-remove-task', HTML)

    def test_accessibility_support_is_present(self):
        self.assertIn('aria-live="polite"', HTML)
        self.assertIn('prefers-reduced-motion:reduce', HTML)
        self.assertIn(':focus-visible', HTML)
        self.assertIn('class="sr-only"', HTML)

    def test_ai_response_is_parsed_and_validated(self):
        self.assertIn("JSON.parse(text.replace", HTML)
        self.assertIn("!Array.isArray(out.ideas)", HTML)
        self.assertIn("responseMimeType:'application/json'", HTML)

    def test_no_external_runtime_dependencies(self):
        self.assertNotIn('<script src=', HTML)
        self.assertNotIn('<link rel="stylesheet" href="http', HTML)

    def test_plan_sections_and_vendors_exist(self):
        for key in ['budget distribution', 'timeline to event day', 'Vendor checklist', 'Accessibility']:
            self.assertIn(key.lower(), HTML.lower())

    def test_tactile_feedback_and_sound_synthesis_present(self):
        self.assertIn("const Haptics={", HTML)
        self.assertIn("vibrate(pattern)", HTML)
        self.assertIn("playClick()", HTML)
        self.assertIn("playSuccess()", HTML)
        self.assertIn("hapticsToggle", HTML)

    def test_celebration_confetti_engine_present(self):
        self.assertIn("function triggerConfetti()", HTML)
        self.assertIn("confettiCanvas", HTML)
        self.assertIn("sparkConfetti", HTML)

    def test_theme_switcher_supported(self):
        self.assertIn('[data-theme="dark"]', HTML)
        self.assertIn("id=\"themeToggle\"", HTML)
        self.assertIn("eventora.theme", HTML)

    def test_live_countdown_ticker_present(self):
        self.assertIn("countdownWidget", HTML)
        self.assertIn("cdDays", HTML)
        self.assertIn("cdHours", HTML)
        self.assertIn("updateCountdown()", HTML)

    def test_interactive_budget_donut_chart_present(self):
        self.assertIn("budgetDonutSvg", HTML)
        self.assertIn("renderDonutChart(", HTML)
        self.assertIn("donut-slice", HTML)

    def test_guest_and_setup_quick_estimator_present(self):
        self.assertIn("quickEstimator", HTML)
        self.assertIn("calcTables", HTML)
        self.assertIn("calcDrinks", HTML)
        self.assertIn("calcPlates", HTML)

    def test_print_media_stylesheet_present(self):
        self.assertIn("@media print", HTML)
        self.assertIn("printPlanBtn", HTML)

if __name__ == '__main__':
    unittest.main(verbosity=2)
