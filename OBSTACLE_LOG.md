# Obstacle Log

1. **Problem:** Searching by company failed when I typed the name in a different case (e.g. "zoho" vs "Zoho").
   **Fix:** Used `.lower()` on both sides while comparing.

2. **Problem:** A wrong status like "Intreview" crashed the summary with a KeyError.
   **Fix:** Added a check against the `statuses` list in `add_application` and `update_status`.

3. **Problem:** The text file had everything on one line at first.
   **Fix:** Added `\n` at the end of every `f.write()`.

4. **Problem:** `update_status` did nothing when the company didn't exist, with no message.
   **Fix:** Added a print message after the loop if no match was found.
