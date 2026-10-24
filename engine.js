// Scroll Math engine: a day's screen minutes against a budget - what is left or over, each app's share, the weekly pace, and an even split. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
function _nm(name) {
  var t = typeof name === "string" ? name.trim() : "";
  if (t.length < 1 || t.length > 24) throw new Error(_N);
  return t;
}
var _B = "the budget must be from 1 to 1440 with no decimal places";
var _M = "the minutes must be from 1 to 1440 with no decimal places";
var _C = "enter from 1 to 12 apps";
var _N = "the app name must be 1 to 24 characters";
var _T = "the total must be at least 1 minute";

function _mins(mins) {
  if (!Array.isArray(mins) || mins.length < 1 || mins.length > 12) throw new Error(_C);
  var t = 0;
  for (var i = 0; i < mins.length; i++) t += _i(mins[i], _M, 4, 1, 1440);
  return t;
}
function budgetTruth(budget, mins) {
  var b = _i(budget, _B, 4, 1, 1440), t = _mins(mins), k = mins.length;
  if (t <= b) {
    return "The " + _pl(k, " app", " apps") + " " + _v(k, "takes", "take") + " " + _pl(t, " minute", " minutes") + " of the " + b + "-minute budget, " + _pl(b - t, " minute", " minutes") + " left.";
  }
  return "The " + _pl(k, " app", " apps") + " " + _v(k, "takes", "take") + " " + _pl(t, " minute", " minutes") + " of the " + b + "-minute budget, " + _pl(t - b, " minute", " minutes") + " over.";
}
function shareTruth(name, minutes, total) {
  var n = _nm(name), m = _i(minutes, _M, 4, 1, 1440), t = _i(total, _T, 5, 1, 17280);
  var p = Math.floor((200 * m + t) / (2 * t));
  return n + " " + _v(1, "takes", "take") + " " + _pl(m, " minute", " minutes") + ", " + p + "% of the total.";
}
function weekTruth(mins) {
  var t = _mins(mins), w = t * 7, h = Math.floor(w / 60), r = w % 60;
  return "At this pace the week takes " + _pl(w, " minute", " minutes") + ", " + _pl(h, " hour", " hours") + " " + _pl(r, " minute", " minutes") + ".";
}
function splitTruth(budget, count) {
  var b = _i(budget, _B, 4, 1, 1440), k = _i(count, _C, 2, 1, 12);
  var q = Math.floor(b / k), r = b - q * k;
  return "An even split of the " + b + "-minute budget over the " + _pl(k, " app", " apps") + " gives " + _pl(q, " minute", " minutes") + " each, " + _pl(r, " minute", " minutes") + " spare.";
}
