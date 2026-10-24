# Scroll Math

Daily screen-time budget: named app minutes against a budget, shares, weekly pace and even split. The 3 apps take 80 minutes of the 90-minute budget, 10 minutes left.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The budget truth** - the entered apps' minutes (each 1 to 1440, 1 to 12 apps) added up against the day's budget (1 to 1440), with the minutes left or over.
- **The share truth** - each app's minutes as a share of the day's total, half rounded up to a whole percent.
- **The week truth** - today's total times seven, in minutes and in hours and minutes.
- **The split truth** - the budget divided evenly over the entered apps, with the spare minutes left over.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any phone, app or day and does not know whether minutes are really spent the way they are entered, a budget is right for anyone or tomorrow will look like today, and it gives no verdict that an app is worth its minutes or a budget is healthy. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; add, name and remove apps, every keystroke recomputes.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
