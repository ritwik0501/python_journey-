# The Complete Python Developer Syllabus
### Zero to job-ready, in three phases

--- test 

## How to Use This Syllabus

**Time assumptions.** All estimates assume **10–15 focused hours per week**. At that pace the whole syllabus takes roughly **7–9 months**. At 25+ hrs/week (full-time self-study) you can compress it to ~4 months. Adjust, but don't skip.

**The 40/60 rule.** Spend at most 40% of your time reading or watching. Spend 60% writing code with the tutorial closed. The single biggest failure mode for self-taught developers is *tutorial hell* — the illusion of competence that comes from following along. If you can't rebuild it from a blank file, you haven't learned it.

**Three tiers of practice, used at every topic:**

| Tier | What it is | Purpose |
|---|---|---|
| **Drills** | 10–20 line exercises, 5–15 min each | Build muscle memory for syntax |
| **Exercises** | 30–80 line problems, 30–90 min each | Combine 2–3 concepts under mild pressure |
| **Mini-projects** | 100–300 lines, 3–8 hours | Force design decisions, debugging, and finishing |

**Rules of engagement**

- [ ] Type every code example by hand. Never copy-paste while learning.
- [ ] Before running code, predict the output out loud. Being wrong is the lesson.
- [ ] When stuck, set a 25-minute timer before looking up the answer. Struggle is where learning happens; unbounded struggle is just wasted time.
- [ ] Keep a `mistakes.md` file. Every bug that cost you >20 minutes goes in it with the fix. Review it weekly.
- [ ] Every mini-project goes in its own Git repo with a README (you'll set up Git in Phase 3 — until then, just keep clean folders).
- [ ] Ship things that are *finished and small* over things that are ambitious and abandoned.

**A note on AI assistants.** Use them as a tutor ("explain why this fails", "what does this error mean") and never as a code generator during Phases 1 and 2. Reading generated code you couldn't have written yourself feels productive and teaches nothing. From Phase 3 onward, use them the way a working developer does — for boilerplate, docs lookup, and rubber-ducking.

---

# PHASE 0 — Setup
**Estimated time: 2–4 hours** *(do this before Phase 1)*

- [DONE] **0.1** Install Python 3.12+ from [python.org](https://www.python.org/downloads/). On Windows, check "Add Python to PATH" during install.
- [DONE] **0.2** Install [VS Code](https://code.visualstudio.com/) + the official Python extension (Microsoft).
- [DONE] **0.3** Learn 6 terminal commands: `cd`, `ls`/`dir`, `mkdir`, `pwd`, `python file.py`, `python` (REPL). That's genuinely all you need for now.
- [DONE] **0.4** Confirm `python --version` and `pip --version` both work in your terminal.
- [DONE] **0.5** Create a folder structure: `python-journey/phase-1/`, `phase-2/`, `phase-3/`.
- [DONE] **0.6** Bookmark [Python Tutor](https://pythontutor.com/) — a step-by-step code visualizer that will be your best friend for loops, functions, and references.

> **Common setup trap:** if `python` opens the Microsoft Store on Windows, or points to Python 2 on macOS, try `python3` and `pip3` instead. Alias it and move on — don't lose a day to this.

---

# PHASE 1 — Python Syntax & Fundamentals
### Total: 90–120 hours (~8–10 weeks at 12 hrs/week)

**Phase goal:** Write a 200-line program from scratch, with functions and error handling, without looking up basic syntax.

---

## 1.1 — Variables, Data Types & Type Conversion
**Time: 6–8 hours**

### Explanation
A variable in Python is a *name bound to an object*, not a box holding a value. `x = 5` doesn't put 5 into a container called `x`; it points the label `x` at an integer object. This distinction seems pedantic now and will explain a whole category of bugs later.

Core built-in types you'll use daily: `int` (whole numbers, unlimited size), `float` (decimals, with precision quirks), `str` (text), `bool` (`True`/`False`), and `NoneType` (the single value `None`, meaning "no value here"). Python is *dynamically typed* — you don't declare types — but it's *strongly typed*, so it won't silently let you add a string to a number.

Type conversion (`int()`, `float()`, `str()`, `bool()`) is explicit and will fail loudly on nonsense input. That failure is a feature.

### Drills
- [Done] Create one variable of each core type and print `type(x)` for each.
- [Done] Predict then verify: `0.1 + 0.2 == 0.3`. Explain the result to yourself.
- [Done ] Predict then verify the truthiness of: `0`, `""`, `[]`, `"False"`, `None`, `-1`.

### Exercises
- [Done] **Unit converter:** ask for a temperature in Celsius, print Fahrenheit and Kelvin to 2 decimal places.
- [Done] **Data type inspector:** take 5 hardcoded values of mixed types, print each with its type and whether it's truthy.

### Mini-project
- [DONE] **Personal Data Card (60–100 lines):** collect name, age, height, city, and favourite number from the user, validate that age and number convert to `int` cleanly, then print a formatted "profile card" with a text border. Handle the case where someone types "twenty" for age.

### Resources
- [Python Docs — Introduction](https://docs.python.org/3/tutorial/introduction.html)
- [Real Python — Variables](https://realpython.com/python-variables/)
- [CS50P Week 0](https://cs50.harvard.edu/python/) *(free, and the best structured intro that exists)*

---

## 1.2 — Operators & Expressions
**Time: 4–6 hours**

### Explanation
Four families: **arithmetic** (`+ - * / // % **`), **comparison** (`== != < > <= >=`), **logical** (`and or not`), and **assignment** (`= += -= *=`).

Two carry disproportionate weight for beginners. `//` is floor division (returns the quotient, discarding the remainder) and `%` is modulo (returns the remainder). Together they're the foundation of every "is this even?", "wrap around a clock", "chunk this into groups", and "extract each digit" problem you'll ever solve.

Also learn **operator precedence** (`**` before `*` before `+`, comparisons before `and`/`or`) and **short-circuit evaluation**: in `a and b`, if `a` is falsy, `b` is never evaluated. That's not trivia — it's the standard idiom for guarding against errors, as in `if user is not None and user.is_active`.

### Drills
- [Done] Use `%` to determine if a number is even, and `//` plus `%` to split 3725 seconds into hours, minutes, seconds.
- [Done] Predict the output of `2 + 3 * 4 ** 2 // 5`, then verify.
- [Done] Write an expression that is `True` only when a number is between 10 and 20 inclusive.

### Exercises
- [ ] **Change maker:** given an amount in cents, print how many quarters, dimes, nickels, and pennies make it up, using only `//` and `%`.
- [ ] **Leap year checker:** implement the real rule (divisible by 4, except centuries, unless divisible by 400) as a single boolean expression.

### Mini-project
- [ ] **Simple Calculator (80–120 lines):** menu-driven, supports the six arithmetic operators, keeps a running "last result" the user can reuse, and refuses to divide by zero. No functions yet — that's deliberate, so you'll *feel* why you need them in 1.6.

### Resources
- [Python Docs — Expressions](https://docs.python.org/3/reference/expressions.html)
- [Real Python — Operators](https://realpython.com/python-operators-expressions/)

---

## 1.3 — Strings & String Handling
**Time: 8–10 hours** *(worth the investment — text handling is most of real programming)*

### Explanation
Strings are **immutable sequences** of characters. Immutable means every "modification" (`.upper()`, `.replace()`) returns a *new* string and leaves the original untouched. Forgetting this produces the classic silent bug: calling `name.strip()` and wondering why `name` still has whitespace.

You need fluency in three areas:

1. **Indexing and slicing:** `s[0]`, `s[-1]`, `s[2:5]`, `s[::-1]`. Slicing uses half-open ranges — start included, stop excluded — the same convention as `range()`, which is why they compose so well.
2. **Methods:** `.strip() .split() .join() .replace() .lower() .upper() .startswith() .find() .isdigit() .title()`. Learn `.split()` and `.join()` as a pair; they're the two directions of the same transformation and appear in nearly every data-cleaning task.
3. **f-strings:** `f"{name} scored {score:.2f}"`. Learn the format mini-language for alignment (`:>10`), padding (`:05d`), and precision (`:.2f`). It makes your terminal output look intentional rather than accidental.

### Drills
- [ ] Reverse a string three ways: slicing, a loop, and `"".join(reversed(s))`.
- [ ] Given `"  Hello, World!  "`, chain methods to produce `"hello world"`.
- [ ] Format the number `1234.5678` as `$1,234.57` using an f-string.

### Exercises
- [ ] **Palindrome checker:** ignore case, spaces, and punctuation. Test with "A man, a plan, a canal: Panama".
- [ ] **Word statistics:** given a paragraph, report word count, character count (with and without spaces), average word length, and longest word.
- [ ] **Caesar cipher:** shift each letter by N positions, wrapping Z→A, preserving case and leaving non-letters alone. (`ord()` and `chr()` are your tools.)

### Mini-project
- [ ] **Text Analyzer / Password Strength Checker (150–200 lines):** the user pastes text; you report readability stats, most-repeated words, and vowel/consonant ratio. Second mode checks a password against length, mixed case, digit, and symbol rules, then prints a rated verdict with specific improvement suggestions.

### Resources
- [Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python — f-strings](https://realpython.com/python-f-strings/)
- [pyformat.info](https://pyformat.info/) — the format spec, by example

---

## 1.4 — Input, Output & Basic Formatting
**Time: 3–4 hours**

### Explanation
`input()` **always returns a string** — every time, no exceptions. If you want a number, you convert it, and that conversion is where user error enters your program. This is the single most common beginner bug: `input("Age: ") + 1` raises a `TypeError` because you're adding an integer to text.

`print()` has parameters worth knowing: `sep` (what goes between arguments), `end` (what goes at the end, default newline), and `flush`. Combined with `\n`, `\t`, and f-strings, that's your entire output toolkit for now.

The habit to build here: **never trust input**. Every `input()` call is a place where a user can hand you garbage, and your program's job is to notice and respond, not crash.

### Drills
- [ ] Build a progress bar that prints on one line using `end="\r"`.
- [ ] Print a formatted table of 5 products and prices, with columns aligned using f-string padding.

### Exercises
- [ ] **Robust number reader:** keep asking for a number until the user supplies a valid one (use a loop and `.isdigit()` for now; you'll do it properly with `try/except` in 1.8).
- [ ] **Receipt generator:** ask for 3 items and prices, print a receipt with aligned columns, subtotal, 8% tax, and total.

### Mini-project
- [ ] **Interactive Quiz Game (120–180 lines):** 10 hardcoded questions, tracks score, shows a progress indicator ("Question 4 of 10"), gives immediate feedback, and prints a final grade with a percentage breakdown.

### Resources
- [Python Docs — Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Real Python — print()](https://realpython.com/python-print/)

---

## 1.5 — Conditionals & Control Flow
**Time: 5–7 hours**

### Explanation
`if` / `elif` / `else` directs which code runs. Two things matter more than the syntax:

**Indentation is syntax in Python.** A block's membership is defined by its whitespace, not by braces. Four spaces, consistently. Mixing tabs and spaces produces `IndentationError` and hours of confusion.

**Order matters in `elif` chains.** Python evaluates top to bottom and stops at the first match. A grade checker that tests `if score > 60` before `if score > 90` will call every A student a D student, and it will do so without error.

Also learn: nested conditionals (and when to flatten them with early returns), the ternary expression `value = a if condition else b`, and `match/case` (Python 3.10+) for clean multi-branch dispatch.

### Drills
- [ ] Write a grade calculator (A–F) and deliberately reverse the condition order to see the bug it causes.
- [ ] Rewrite a 3-level nested `if` as a flat chain of guard clauses.

### Exercises
- [ ] **Rock-paper-scissors:** one round versus a random computer choice (`import random`), declaring winner or tie.
- [ ] **BMI categoriser:** compute BMI from height and weight, classify it, and refuse impossible values (negative, zero, absurdly large).
- [ ] **Triangle classifier:** given three side lengths, determine whether they form a valid triangle, and if so whether it's equilateral, isosceles, or scalene.

### Mini-project
- [ ] **Choose-Your-Own-Adventure Game (200–300 lines):** at least 8 decision points, 3 distinct endings, an inventory the player collects, and validated input at every prompt. This will get ugly with nesting — that's the lesson. Notice the pain, remember it for 1.6.

### Resources
- [Python Docs — Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)

---

## 1.6 — Loops & Iteration
**Time: 8–10 hours** *(the highest-leverage topic in Phase 1)*

### Explanation
`for` loops iterate over a sequence of known items. `while` loops repeat until a condition becomes false. Beginners over-reach for `while`; the working rule is **use `for` when you know what you're iterating over, `while` when you're waiting for a condition to change** (user input, a converging calculation, a game that runs until quit).

Master these tools:
- `range(start, stop, step)` — remember `stop` is exclusive
- `break` (exit the loop now), `continue` (skip to the next iteration)
- `enumerate(seq)` — index *and* value together, instead of `range(len(seq))`
- `zip(a, b)` — walk two sequences in parallel
- Nested loops — outer runs once per full pass of the inner
- The `else` clause on loops — runs only if the loop completed without `break` (rare, but elegant for search)

**Infinite loops** are a rite of passage. When one happens, `Ctrl+C` stops it, then ask: what was supposed to change the condition, and why didn't it?

### Drills
- [ ] Print a right triangle, then a pyramid, then a diamond of asterisks using nested loops.
- [ ] Sum every number from 1 to 100 divisible by 3 or 5.
- [ ] Use `enumerate` to print a numbered list, and `zip` to pair names with scores.

### Exercises
- [ ] **FizzBuzz:** the classic 1–100 interview screen. Then do it in one line with a comprehension.
- [ ] **Multiplication table:** print a formatted, aligned 12×12 grid with header row and column.
- [ ] **Number guessing game:** computer picks 1–100, gives higher/lower hints, limits attempts, and offers a replay loop.
- [ ] **Prime finder:** print all primes below 100, then optimise the inner loop to stop at `√n` and explain why that's valid.

### Mini-project
- [ ] **ATM Simulator (200–250 lines):** menu loop with balance check, deposit, withdraw, and transaction history. Enforce PIN entry with 3 attempts, prevent overdrafts, validate all amounts, and exit cleanly. Use only what you've learned so far.

### Resources
- [Python Docs — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Real Python — for Loops](https://realpython.com/python-for-loop/)
- [Python Tutor](https://pythontutor.com/) — step through a nested loop visually; it's genuinely clarifying

---

## 1.7 — Functions & Scope
**Time: 10–12 hours** *(the conceptual turning point of Phase 1)*

### Explanation
A function is a named, reusable block that takes inputs and (usually) returns an output. This is where you stop writing scripts and start writing *programs*.

What you must actually understand, not just use:

- **`return` vs `print`.** `print` shows a human something. `return` hands a value back to the calling code. Confusing them is the #1 function bug. A function that prints but doesn't return gives you `None` when you try to use its result.
- **Parameters vs arguments.** Parameters are the names in the definition; arguments are the values you pass. Positional, keyword, default (`def greet(name, greeting="Hello")`), and variadic (`*args`, `**kwargs`).
- **The mutable default argument trap.** `def add(item, lst=[])` shares one list across all calls, forever. Use `lst=None` and create it inside. This will be asked in interviews.
- **Scope (LEGB):** Local → Enclosing → Global → Built-in. A name assigned inside a function is local unless declared otherwise, which is why modifying a global from inside a function silently fails.
- **Docstrings:** `"""One line saying what it does."""` as the first statement. Write one for every function from now on.

**The refactoring habit:** go back to your Calculator (1.2) and ATM (1.6) and rewrite them with functions. Feeling how much better they become is the entire point of this topic.

### Drills
- [ ] Write `is_even(n)` that returns a bool, then a version that prints — and demonstrate why the printing one can't be composed.
- [ ] Write a function with two required, one default, and `*args` parameters. Call it five different ways.
- [ ] Demonstrate the mutable-default bug, then fix it.

### Exercises
- [ ] **Function library:** write and test `celsius_to_f`, `is_prime`, `reverse_string`, `count_vowels`, `factorial` (iterative), and `fibonacci(n)`.
- [ ] **Refactor:** rewrite your 1.5 adventure game so each scene is a function. Note the reduction in nesting.
- [ ] **Calculator v2:** each operation is a function; a dictionary maps operator symbols to functions. (First taste of functions as values.)

### Mini-project
- [ ] **Command-Line To-Do Manager (250–300 lines):** add, list, complete, delete, and filter tasks. Every operation is its own well-named function under 20 lines. Data lives in a list in memory (persistence arrives in Phase 3). Include a `main()` function and the `if __name__ == "__main__":` guard.

### Resources
- [Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python — Defining Your Own Functions](https://realpython.com/defining-your-own-python-function/)
- [Real Python — Scope & LEGB](https://realpython.com/python-scope-legb-rule/)

---

## 1.8 — Error Handling & Exceptions
**Time: 6–8 hours**

### Explanation
Errors come in three flavours: **syntax errors** (code won't run), **runtime errors/exceptions** (crashes mid-execution), and **logic errors** (runs perfectly, produces the wrong answer — the dangerous kind).

`try` / `except` / `else` / `finally` handles exceptions:
- `try:` code that might fail
- `except SpecificError:` what to do when it does
- `else:` runs only if no exception occurred
- `finally:` runs no matter what (cleanup)

**Catch specific exceptions.** A bare `except:` swallows everything including typos in your own code and `Ctrl+C`, turning a loud bug into a silent one. Learn the common ones by sight: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`, `AttributeError`.

Then learn to **read a traceback**: it reads bottom-up in importance — the last line is the error type and message, the lines above are the call chain that got you there. Reading tracebacks well is the difference between a 2-minute fix and a 2-hour flail.

Also: `raise` to signal your own errors, and defining a custom exception class (`class InsufficientFundsError(Exception): pass`) so callers can handle your failure modes specifically.

### Drills
- [ ] Deliberately trigger each of the seven common exceptions listed above and read each traceback.
- [ ] Write a `safe_divide(a, b)` that returns `None` instead of raising on division by zero.
- [ ] Show a case where `finally` runs even though the function returned early.

### Exercises
- [ ] **Bulletproof input:** write `get_int(prompt, min_val, max_val)` that loops until it gets a valid integer in range, handling both `ValueError` and out-of-range separately.
- [ ] **Retrofit:** add proper exception handling to your ATM simulator and to-do manager. Every `int()` conversion should be guarded.
- [ ] **Custom exception:** raise `InsufficientFundsError` with a useful message in a withdrawal function, and handle it at the call site.

### Mini-project
- [ ] **Robust Recipe Scaler (150–200 lines):** store recipes with ingredients and quantities, scale by servings, convert units, and survive *any* input a hostile user provides — negative servings, text where numbers go, unknown recipe names, empty input. Your program should never show a raw traceback.

### Resources
- [Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python — Exceptions](https://realpython.com/python-exceptions/)
- [Real Python — Understanding Tracebacks](https://realpython.com/python-traceback/)

---

## 1.9 — Modules, Imports & the Standard Library
**Time: 5–7 hours**

### Explanation
A module is just a `.py` file. Importing it gives you access to its functions. A package is a directory of modules. This is how programs grow past one file without becoming unreadable.

Import styles and when to use them:
- `import math` → `math.sqrt(9)`. Verbose but unambiguous. **Default to this.**
- `from math import sqrt` → `sqrt(9)`. Fine for 2–3 heavily used names.
- `from math import *` → **never.** It pollutes your namespace and makes the origin of names invisible.
- `import numpy as np` → aliasing, for long names with community conventions.

Understand `if __name__ == "__main__":` properly: when a file runs directly, `__name__` is `"__main__"`; when imported, it's the module's name. The guard lets a file be both a runnable script and an importable library.

**Standard library tour** (Python's "batteries included" — knowing what's there saves you writing it): `math`, `random`, `datetime`, `os`, `sys`, `json`, `csv`, `re`, `collections`, `itertools`, `pathlib`, `time`.

### Drills
- [ ] Split your to-do manager into `tasks.py` (logic) and `main.py` (interface), importing across them.
- [ ] Use `datetime` to calculate your exact age in days.
- [ ] Use `random.sample`, `random.shuffle`, and `random.choices` and articulate the difference.

### Exercises
- [ ] **Password generator module:** a `passgen.py` with configurable length and character sets, plus a `__main__` block that demos it when run directly.
- [ ] **Date utilities:** days until a given date, weekday of any birthday, and business days between two dates.
- [ ] **Stdlib scavenger hunt:** solve one small problem with each of `collections.Counter`, `itertools.combinations`, and `pathlib.Path`.

### Mini-project
- [ ] **Multi-Module Utility Toolkit (250–350 lines):** a `toolkit/` package with `text_tools.py`, `math_tools.py`, and `date_tools.py`, plus a `main.py` menu that imports and dispatches to all three. Every function has a docstring. This is your first program with real structure.

### Resources
- [Python Docs — Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Module of the Week](https://pymotw.com/3/) — outstanding stdlib tour
- [Real Python — Imports 101](https://realpython.com/python-import/)

---

## PHASE 1 CAPSTONE
### 🏁 Personal Finance Tracker (CLI)
**Time: 12–18 hours**

Build a complete expense tracker that exercises every Phase 1 topic:

**Requirements**
- [ ] Add income and expense entries with amount, category, date, and description
- [ ] View all transactions in a clean aligned table
- [ ] Filter by category, by date range, and by amount threshold
- [ ] Summary report: total in, total out, net balance, spend per category with percentages
- [ ] Simple text bar chart of spending by category (`Food  ████████ 42%`)
- [ ] Budget setting per category with over-budget warnings
- [ ] Menu-driven loop that never crashes on bad input
- [ ] Organised across at least 3 modules, every function documented
- [ ] A README explaining what it does and how to run it

**Self-assessment — you're ready for Phase 2 when:**
- [ ] You wrote it without following a tutorial
- [ ] Every function is under ~25 lines and does one thing
- [ ] You can hand it to a friend and they can't crash it
- [ ] You can explain any line of it a week later

---

# PHASE 2 — Data Structures & Algorithmic Thinking
### Total: 80–110 hours (~7–9 weeks at 12 hrs/week)

**Phase goal:** Choose the right data structure for a problem on instinct, justify it in Big-O terms, and solve an unseen Easy-level algorithm problem in under 30 minutes.

> **Why this phase matters more than it looks.** Phase 1 taught you to make a computer do things. Phase 2 teaches you to make it do them *well*. This is also the phase that gets tested in technical interviews, so don't rush it.

---

## 2.1 — Lists
**Time: 8–10 hours**

### Definition
An **ordered, mutable sequence** that allows duplicates and mixed types. Python's workhorse. Internally a dynamic array: elements sit in contiguous memory, which is why index access is instant and inserting at the front is not.

### Common Operations

| Operation | Syntax | Notes |
|---|---|---|
| Access | `lst[i]`, `lst[-1]` | Negative indices count from the end |
| Slice | `lst[1:4]`, `lst[::2]`, `lst[::-1]` | Returns a **new** list |
| Add | `.append(x)`, `.insert(i, x)`, `.extend(other)` | `append` adds one; `extend` adds many |
| Remove | `.pop()`, `.pop(i)`, `.remove(x)`, `del lst[i]`, `.clear()` | `remove` deletes by value, `pop` by index |
| Search | `x in lst`, `.index(x)`, `.count(x)` | `.index` raises `ValueError` if absent |
| Order | `.sort()`, `.reverse()`, `sorted(lst)` | `.sort()` mutates and returns `None`; `sorted()` returns new |
| Build | `[expr for x in seq if cond]` | Comprehensions — learn these properly |

### Time Complexity

| Operation | Big-O | Why |
|---|---|---|
| Index access `lst[i]` | **O(1)** | Direct memory offset |
| `.append(x)` | **O(1)** amortised | Occasional resize, averaged out |
| `.insert(0, x)` / `.pop(0)` | **O(n)** | Every element must shift |
| `x in lst` | **O(n)** | Linear scan |
| `.sort()` | **O(n log n)** | Timsort |

> **The lesson that pays off:** if you're doing `.insert(0, x)` or `.pop(0)` in a loop, you want `collections.deque` (O(1) at both ends). If you're doing `x in lst` in a loop, you want a `set`.

### Critical concepts
- **Mutability and aliasing:** `b = a` makes both names point to the *same* list. Mutating through `b` changes what `a` sees. Use `a.copy()` or `a[:]` for a shallow copy, `copy.deepcopy()` for nested structures.
- **Comprehensions:** `[x**2 for x in nums if x > 0]`. Master these; they're idiomatic Python and appear everywhere. Stop at one level of nesting — beyond that, use a loop.
- **Never mutate a list while iterating over it.** It silently skips elements. Iterate over a copy or build a new list.

### Practice Problems
- [ ] Find the second-largest number without using `sort()` or `max()`.
- [ ] Remove duplicates while **preserving original order**.
- [ ] Rotate a list left by `k` positions (two ways: slicing, and in-place).
- [ ] Flatten a nested list one level deep with a comprehension.
- [ ] Merge two already-sorted lists into one sorted list without using `sorted()`.
- [ ] Demonstrate the aliasing bug, then fix it with a copy.

### Resources
- [Python Docs — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Python Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity) — bookmark this

---

## 2.2 — Tuples
**Time: 3–4 hours**

### Definition
An **ordered, immutable sequence**. Once created, it cannot be changed. That constraint is the point: it signals intent ("these values belong together and won't change"), makes the object hashable (so it can be a dictionary key or set member), and is slightly faster and lighter than a list.

### Common Operations
Indexing, slicing, `in`, `.count()`, `.index()`, concatenation, and `len()` all work as with lists. Anything that mutates does not exist.

The real power is **unpacking**:
```python
point = (3, 4)
x, y = point                      # basic
a, b = b, a                       # swap without a temp variable
first, *rest = [1, 2, 3, 4]       # star unpacking
for i, name in enumerate(names):  # tuple unpacking in a loop
```
Every function that "returns multiple values" is actually returning a tuple.

Learn **`namedtuple`** (or `typing.NamedTuple`) from `collections` — it gives you `p.x` instead of `p[0]`, turning cryptic index access into readable code at zero cost.

### Time Complexity
Same as lists for reads: index O(1), `in` O(n). No write operations exist. Slightly lower memory overhead and faster construction.

### Practice Problems
- [ ] Write a function returning min, max, and average as a tuple, then unpack it at the call site.
- [ ] Store 5 coordinate points as tuples in a list; find the two closest points.
- [ ] Rewrite a dictionary-of-lists structure using `namedtuple` and compare readability.
- [ ] Prove a tuple can be a dict key while a list cannot, and explain why in terms of hashability.

### Resources
- [Real Python — Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python — namedtuple](https://realpython.com/python-namedtuple/)

---

## 2.3 — Dictionaries
**Time: 10–12 hours** *(the most important data structure in practical Python)*

### Definition
A **mutable mapping of unique keys to values**, backed by a hash table. Keys must be hashable (immutable): strings, numbers, tuples — not lists. As of Python 3.7+, dictionaries preserve insertion order.

If you learn one structure deeply in this phase, make it this one. Dictionaries are how you model records, count things, cache results, build lookup tables, and represent JSON — which is to say, they're how you handle most real data.

### Common Operations

| Operation | Syntax | Notes |
|---|---|---|
| Access | `d[k]` / `d.get(k, default)` | `[]` raises `KeyError`; `.get()` returns default |
| Set | `d[k] = v`, `.update(other)` | Creates or overwrites |
| Delete | `.pop(k)`, `del d[k]`, `.popitem()` | |
| Check | `k in d` | **O(1)** — checks keys, not values |
| Iterate | `.keys()`, `.values()`, `.items()` | `for k, v in d.items():` is the idiom |
| Default | `.setdefault(k, default)` | Get-or-create in one call |
| Build | `{k: v for k, v in pairs}` | Dict comprehension |

### Time Complexity

| Operation | Average | Worst |
|---|---|---|
| Access / insert / delete / `in` | **O(1)** | O(n) with pathological hash collisions |
| Iteration | O(n) | O(n) |

> **The single most valuable optimisation a beginner can learn:** replacing a repeated `x in list` (O(n)) with `x in dict` or `x in set` (O(1)). Turning an O(n²) loop into O(n) is often just a change of container.

### Essential patterns
- **Counting:** `collections.Counter(items)` — then `.most_common(3)`
- **Grouping:** `collections.defaultdict(list)` — no key-existence checks needed
- **Nesting:** dicts of dicts to model structured records (this is what JSON is)
- **Inverting:** `{v: k for k, v in d.items()}`
- **Sorting by value:** `sorted(d.items(), key=lambda kv: kv[1], reverse=True)` — learn `key=` here; it's used everywhere

### Practice Problems
- [ ] Count word frequency in a paragraph — first manually, then with `Counter`.
- [ ] Invert a dictionary, handling duplicate values gracefully.
- [ ] Group a list of student records (name, grade, subject) by subject using `defaultdict`.
- [ ] Merge two dictionaries, summing values where keys collide.
- [ ] Find the top 3 most common items and sort a dict by value descending.
- [ ] Build a nested dict representing a small class roster, then write a function to safely read a deeply nested value.

### Resources
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python — Dictionaries](https://realpython.com/python-dicts/)
- [Real Python — collections module](https://realpython.com/python-collections-module/)

---

## 2.4 — Sets
**Time: 4–5 hours**

### Definition
An **unordered collection of unique, hashable elements**. No duplicates, no indexing, no order. Backed by the same hash table machinery as dicts, which gives O(1) membership testing.

Sets exist to answer two questions fast: *"have I seen this before?"* and *"what do these two collections have in common?"*

### Common Operations

| Operation | Syntax | Meaning |
|---|---|---|
| Create | `{1, 2, 3}`, `set(lst)` | `{}` is an empty **dict**, use `set()` |
| Add / remove | `.add(x)`, `.discard(x)`, `.remove(x)` | `discard` is safe, `remove` raises |
| Union | `a \| b` or `.union(b)` | Everything in either |
| Intersection | `a & b` or `.intersection(b)` | In both |
| Difference | `a - b` or `.difference(b)` | In `a` only |
| Symmetric diff | `a ^ b` | In exactly one |
| Subset | `a <= b`, `a < b` | Containment tests |

### Time Complexity
Add, remove, and `in` are all **O(1)** average. Union/intersection are O(len(a) + len(b)) and O(min(len(a), len(b))) respectively. Deduplicating a list via `set(lst)` is O(n) — versus O(n²) for the nested-loop approach.

### Practice Problems
- [ ] Deduplicate a list two ways and time both with `time.perf_counter()` on 100,000 items.
- [ ] Find common and unique elements between two lists of names.
- [ ] Detect whether a list contains any duplicates in a single pass.
- [ ] Find all characters appearing in string A but not string B.
- [ ] Given three sets of students in different clubs, report who's in exactly one club.

### Resources
- [Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Real Python — Sets](https://realpython.com/python-sets/)

---

## 2.5 — Choosing the Right Structure
**Time: 2–3 hours** *(short but do not skip)*

### The decision table

| You need… | Use | Because |
|---|---|---|
| Ordered items, will change | **list** | Mutable sequence, O(1) index |
| Ordered items, fixed forever | **tuple** | Immutable, hashable, lighter |
| Key → value lookup | **dict** | O(1) access by key |
| Uniqueness / fast membership | **set** | O(1) `in`, automatic dedup |
| Fast add/remove at both ends | **deque** | O(1) both ends vs list's O(n) at front |
| Counting occurrences | **Counter** | Purpose-built, `.most_common()` |
| Grouping into buckets | **defaultdict** | No key-existence boilerplate |

### Exercise
- [ ] Take one problem — "find the 5 most common words in a book, excluding stopwords" — and solve it three ways: lists only, dict-based, and `Counter` + `set`. Time all three on a large text file. Write down the numbers. This single exercise teaches more about complexity than a chapter of theory.

---

## 2.6 — Algorithmic Thinking: Searching
**Time: 6–8 hours**

### Explanation
**Linear search** checks every element until it finds the target: O(n). Works on any sequence, sorted or not.

**Binary search** repeatedly halves a *sorted* sequence: check the middle, discard the half that can't contain the target, repeat. O(log n). For a million items that's ~20 comparisons instead of a million. The prerequisite — the data must be sorted — is the entire trade-off.

Implement binary search by hand at least twice, both iteratively and recursively. It's deceptively fiddly: off-by-one errors in the `low`/`high`/`mid` arithmetic are the classic trap, and getting it right teaches you invariant-based reasoning. Then learn the `bisect` module, which is what you'll actually use.

### Practice Problems
- [ ] Implement linear search returning the index or `-1`.
- [ ] Implement iterative binary search, then a recursive version.
- [ ] Instrument both with a comparison counter; run on 10, 1,000, and 1,000,000 items and tabulate the results.
- [ ] Find the first and last occurrence of a value in a sorted list with duplicates.
- [ ] Number guessing game where the **computer** guesses your number using binary search — it should always win in ≤7 guesses for 1–100.

### Resources
- [Real Python — Binary Search](https://realpython.com/binary-search-python/)
- [VisuAlgo](https://visualgo.net/en) — animated algorithm visualiser

---

## 2.7 — Algorithmic Thinking: Sorting
**Time: 6–8 hours**

### Explanation
You will almost never write a sorting algorithm professionally — Python's `sorted()` uses Timsort and beats anything you'd write. You learn them anyway because they're the cleanest available lessons in algorithm design, complexity analysis, and trade-offs.

| Algorithm | Average | Worst | Idea |
|---|---|---|---|
| **Bubble sort** | O(n²) | O(n²) | Repeatedly swap adjacent out-of-order pairs |
| **Selection sort** | O(n²) | O(n²) | Repeatedly find the minimum, place it |
| **Insertion sort** | O(n²) | O(n²) | Build a sorted prefix one item at a time; fast on nearly-sorted data |
| **Merge sort** | O(n log n) | O(n log n) | Divide, sort halves, merge — first taste of divide-and-conquer |
| **Quick sort** | O(n log n) | O(n²) | Partition around a pivot, recurse |
| **Timsort** (built-in) | O(n log n) | O(n log n) | Hybrid merge/insertion — what `sorted()` actually does |

In practice, spend your effort on **`sorted()` with `key=`**, which is what real code uses:
```python
sorted(people, key=lambda p: p["age"])                # by one field
sorted(people, key=lambda p: (p["last"], p["first"])) # by two, tuple key
sorted(words, key=len, reverse=True)                  # by length, descending
```

### Practice Problems
- [ ] Implement bubble, selection, and insertion sort from scratch.
- [ ] Implement merge sort recursively — this is your bridge into 2.8.
- [ ] Benchmark all four plus `sorted()` on 5,000 random integers; chart the results.
- [ ] Sort a list of dictionaries by nested key, then by two keys at once.
- [ ] Explain in writing why an O(n log n) algorithm beats O(n²), with concrete numbers at n = 1,000,000.

### Resources
- [Real Python — Sorting Algorithms](https://realpython.com/sorting-algorithms-python/)
- [Real Python — sorted() and key](https://realpython.com/python-sort/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

---

## 2.8 — Recursion Basics
**Time: 6–8 hours**

### Explanation
A recursive function calls itself on a smaller version of the same problem. Two mandatory parts:

1. **Base case** — the condition where it stops and returns directly. Without it, you get `RecursionError` (Python caps the stack around 1,000 frames).
2. **Recursive case** — the function calls itself on a strictly smaller input, guaranteeing progress toward the base case.

The mental unlock is **trusting the recursion**: assume the recursive call already works correctly for the smaller input, and just handle combining that result with the current level. Trying to trace every frame in your head is how people bounce off recursion.

Understand the **call stack** — each call adds a frame, frames unwind as calls return — and step through `factorial(4)` in [Python Tutor](https://pythontutor.com/) until it clicks. That five minutes is worth an hour of reading.

Know the trade-off: naive recursive `fibonacci(n)` is O(2ⁿ) and unusable past n≈35. Adding `@functools.lru_cache` makes it O(n) with one line. That's your introduction to memoisation.

**When recursion genuinely wins:** tree and nested structures (folders, JSON, HTML), divide-and-conquer (merge sort, binary search), and backtracking. For simple counting loops, iteration is clearer and cheaper.

### Practice Problems
- [ ] Factorial and Fibonacci recursively; then add `lru_cache` to Fibonacci and time both at n=35.
- [ ] Sum a list, reverse a string, and check a palindrome — all recursively.
- [ ] Flatten an **arbitrarily** nested list (this one genuinely needs recursion).
- [ ] Tower of Hanoi with move-by-move printed output.
- [ ] Walk a nested dictionary (JSON-shaped) and print every leaf value with its full key path.
- [ ] Recursively compute the total size of a folder tree using `os.walk` or `pathlib`.

### Resources
- [Real Python — Recursion](https://realpython.com/python-recursion/)
- [Real Python — lru_cache / memoization](https://realpython.com/lru-cache-python/)
- [Python Tutor](https://pythontutor.com/) — indispensable here

---

## 2.9 — Consolidation: Algorithm Practice Habit
**Time: ongoing, 3–4 hrs/week from here to the end**

Start a permanent habit now and carry it through Phase 3:

- [ ] **[Exercism — Python Track](https://exercism.org/tracks/python)** — free, with human mentor feedback. The single best resource at this stage.
- [ ] **[LeetCode Easy](https://leetcode.com/problemset/)** — 3 problems/week. Filter by Array, String, Hash Table.
- [ ] **[Codewars](https://www.codewars.com/)** — 8kyu → 6kyu katas. Read others' solutions after solving; that's where the learning compounds.
- [ ] **[HackerRank Python](https://www.hackerrank.com/domains/python)** — structured, gentler ramp.

**Method that works:** solve it yourself first (30 min cap), then read three other solutions, then rewrite yours incorporating what you learned, then note the pattern in `mistakes.md`. Quantity without this review loop teaches very little.

---

## PHASE 2 CAPSTONE
### 🏁 Contact & Inventory Management System
**Time: 15–20 hours**

**Requirements**
- [ ] Contacts stored as a dict keyed by unique ID; each contact is a nested dict (name, phones list, email, tags set, address tuple)
- [ ] Full CRUD: create, read, update, delete
- [ ] Search by name (partial match), by tag, and by any field — with an index dict to make lookups O(1) rather than scanning
- [ ] Sort output by any field, ascending or descending, using `sorted(key=)`
- [ ] Tag system using sets: find contacts with *all* given tags (intersection), with *any* (union), and with *none* (difference)
- [ ] Duplicate detection via set-based email/phone checks
- [ ] Statistics: contacts per tag using `Counter`, most-connected contacts, tag co-occurrence
- [ ] Recursive function to display a nested "organisation chart" of contacts who report to others
- [ ] A written `COMPLEXITY.md` justifying each structure choice in Big-O terms

**Self-assessment — you're ready for Phase 3 when:**
- [ ] You picked each data structure deliberately and can defend the choice
- [ ] You can state the complexity of every operation in your program
- [ ] You solved 20+ Exercism or LeetCode Easy problems unaided
- [ ] You can implement binary search and merge sort from memory

---

# PHASE 3 — Development Track
### Total: 140–180 hours (~12–15 weeks at 12 hrs/week)

**Phase goal:** Work like a professional developer — versioned, tested, isolated environments, real data, real APIs — and ship one substantial specialised project.

> **The shift in this phase.** Phases 1 and 2 were about the language. Phase 3 is about the *craft*: the tools and practices that separate someone who can write Python from someone who can be hired to write Python. Employers assume language competence; they screen for this phase.

---

## 3.1 — Object-Oriented Programming
**Time: 20–25 hours** *(largest single topic in the syllabus, and rightly so)*

### Explanation
A **class** is a blueprint; an **object** (instance) is a thing built from it. OOP bundles data (attributes) with the behaviour that operates on it (methods), which is the natural way to model anything with both state and actions — a bank account, a user, a game character, an HTTP session.

**Build it in this order:**

**Classes and instances**
```python
class BankAccount:
    interest_rate = 0.02              # class attribute — shared by all instances

    def __init__(self, owner, balance=0):
        self.owner = owner            # instance attributes — unique per object
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance
```
`self` is the instance the method was called on. It's passed automatically; you just have to name it. `__init__` is the initialiser that runs at construction.

**Dunder methods** — the hooks that make your objects behave like built-in ones:
- `__init__` construction · `__str__` human-readable (`print`) · `__repr__` unambiguous (debugging) · `__eq__` equality · `__len__` · `__lt__` for sorting

Write `__repr__` for every class you make. Future-you, staring at a list of objects in a debugger, will be grateful.

**Encapsulation** — `_single_underscore` means "internal, please don't touch" (a convention, not enforced); `__double` triggers name mangling. Use `@property` to expose a computed or validated attribute with plain attribute syntax:
```python
@property
def area(self):
    return self.width * self.height
```

**Inheritance** — `class SavingsAccount(BankAccount):` gets everything from the parent and can add or override. `super().__init__(...)` calls the parent's version. Beware deep hierarchies: **favour composition over inheritance** — an object that *has* an engine is usually a better model than one that *is* an engine.

**Polymorphism** — different classes responding to the same method call. Combined with Python's **duck typing** ("if it has `.speak()`, I don't care what class it is"), this is what lets you write functions that work across types without any type checks.

**Also cover:** `@classmethod` (alternative constructors), `@staticmethod` (namespaced utility), abstract base classes via `abc`, and `@dataclass` — which eliminates the boilerplate of `__init__`, `__repr__`, and `__eq__` in one decorator and is genuinely how modern Python is written.

### Practice Exercises
- [ ] `Rectangle` class with `area`/`perimeter` as properties, plus `__str__` and `__eq__`.
- [ ] `BankAccount` → `SavingsAccount` (interest) and `CheckingAccount` (overdraft) with `super()`.
- [ ] A `Shape` abstract base class with `Circle`, `Square`, `Triangle` subclasses; write one function that computes total area of a mixed list — that's polymorphism in action.
- [ ] `Deck` and `Card` classes; implement `__len__` and `__getitem__` so a deck can be shuffled by `random.shuffle` and iterated with `for`.
- [ ] Rewrite one class as a `@dataclass` and count the lines you deleted.
- [ ] Refactor your **Phase 1 finance tracker** into classes (`Transaction`, `Account`, `Budget`, `Report`). Compare the two versions side by side.

### Mini-project
- [ ] **Library Management System (400–600 lines):** `Book`, `Member`, `Librarian`, `Loan` classes. Inheritance for member types (Student, Staff, Guest) with different borrowing limits and fine rates. Polymorphic `calculate_fine()`. Custom exceptions (`BookUnavailableError`, `LoanLimitExceededError`). Properties for computed values like `days_overdue`. Full `__repr__` coverage.

### Resources
- [Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python — OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Real Python — Dataclasses](https://realpython.com/python-data-classes/)
- [Corey Schafer — OOP series (YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — the clearest video treatment available

---

## 3.2 — File Handling & Data Persistence
**Time: 10–12 hours**

### Explanation
Everything you've built so far forgets everything when it closes. Files fix that.

**Always use a context manager:**
```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# file closed automatically, even if an exception occurred
```
The `with` block guarantees closure. Learn the modes — `r` read, `w` write (**truncates the file**), `a` append, `r+` read/write, `b` binary — and always specify `encoding="utf-8"` explicitly, because platform defaults differ and the resulting `UnicodeDecodeError` on someone else's machine is a miserable bug to chase.

**Three formats, three purposes:**
- **Plain text** — logs, notes. Read lazily line-by-line (`for line in f`) so a 2 GB file doesn't exhaust memory.
- **CSV** — tabular data. Use the `csv` module, especially `DictReader`/`DictWriter`. Never split on commas yourself; quoted fields containing commas will destroy you.
- **JSON** — structured/nested data, the lingua franca of APIs. `json.dump`/`json.load` for files, `json.dumps`/`json.loads` for strings. Note how cleanly Python dicts and lists map onto it — that's why Phase 2 mattered.

Use **`pathlib`** rather than string concatenation for paths: `Path("data") / "users.json"` works on every OS, and `.exists()`, `.mkdir(parents=True)`, `.glob("*.csv")` are far cleaner than the `os.path` equivalents.

**Habits:** handle `FileNotFoundError` and `PermissionError` explicitly; write to a temp file and rename on success so a crash mid-write doesn't corrupt your data; never trust a file's contents to be well-formed.

### Practice Exercises
- [ ] Read a text file and report line, word, and character counts.
- [ ] Read a CSV of sales data with `DictReader`; compute totals per region; write results to a new CSV.
- [ ] Save and reload a nested dictionary as JSON; verify it round-trips exactly.
- [ ] Write a log-file analyser that finds all ERROR lines and summarises them by hour.
- [ ] Use `pathlib` to recursively find every `.py` file in a folder tree and report the largest.

### Mini-project
- [ ] **Persistent To-Do / Notes App (300–400 lines):** upgrade your Phase 1 to-do manager with JSON persistence, auto-save, an atomic-write pattern, export to CSV and Markdown, a timestamped backup on every launch, and graceful recovery from a corrupted data file.

### Resources
- [Python Docs — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python — File I/O](https://realpython.com/read-write-files-python/)
- [Real Python — pathlib](https://realpython.com/python-pathlib/)
- [Real Python — Working With JSON](https://realpython.com/python-json/)

---

## 3.3 — Virtual Environments & Package Management
**Time: 4–6 hours** *(small topic, non-negotiable skill)*

### Explanation
Every Python project needs its own isolated set of dependencies. Project A needs `requests` 2.28; project B needs 2.31. Installed globally, they conflict. A **virtual environment** is a private folder holding a project's own Python and packages.

```bash
python -m venv .venv                    # create
source .venv/bin/activate               # activate (macOS/Linux)
.venv\Scripts\activate                  # activate (Windows)
pip install requests                    # installs into this env only
pip freeze > requirements.txt           # record exact versions
pip install -r requirements.txt         # reproduce elsewhere
deactivate
```

**Rules:** one venv per project, named `.venv`, never committed to Git (add to `.gitignore`). Always commit `requirements.txt` — it's what makes your project reproducible on someone else's machine, and its absence is an immediate red flag to anyone reviewing your GitHub.

Understand **semantic versioning** (`MAJOR.MINOR.PATCH`) and pinning strategies (`requests==2.31.0` exact vs `requests>=2.31` flexible). Be aware that **[uv](https://docs.astral.sh/uv/)** and **Poetry** are the modern alternatives increasingly seen in job postings — learn `venv` + `pip` first for the mental model, then try `uv`, which is dramatically faster and largely a drop-in replacement.

### Practice Exercises
- [ ] Create two venvs with deliberately different versions of the same package; prove they're isolated.
- [ ] Set up a project with `requirements.txt`, delete the venv, and rebuild from scratch.
- [ ] Retrofit every prior project with its own venv and requirements file.
- [ ] Read a package's PyPI page and its docs before installing it — build the habit of vetting dependencies.

### Resources
- [Python Docs — venv](https://docs.python.org/3/library/venv.html)
- [Real Python — Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [PyPI](https://pypi.org/)

---

## 3.4 — Version Control with Git & GitHub
**Time: 12–15 hours** *(learn this properly — it's assessed in every interview)*

### Explanation
Git tracks changes to your code over time. GitHub hosts those repositories online. For a self-taught developer, **your GitHub profile is your résumé** — often reviewed before your CV.

**The core loop (90% of daily use):**
```bash
git init                          # start tracking a project
git status                        # what's changed? — run this constantly
git add file.py                   # stage specific changes
git commit -m "Add expense filter by category"
git log --oneline --graph         # see history
git push origin main              # send to GitHub
git pull                          # fetch others' changes
```

**Branching** — where the real value is:
```bash
git switch -c feature/export-csv   # create and switch to a branch
# ...work, commit...
git switch main
git merge feature/export-csv
```
Branches let you build a feature without breaking working code. Learn to resolve a merge conflict by hand — deliberately create one, then fix it. It's alarming exactly once.

**Also learn:** `.gitignore` (exclude `.venv/`, `__pycache__/`, `.env`, data files), writing good commit messages (imperative mood, explains *why* not *what*), `git diff`, `git restore`, `git revert`, and the pull-request workflow — fork, branch, PR, review — because that's how every team actually ships.

**Critical safety habit:** never commit secrets. API keys, passwords, and tokens go in a `.env` file that is gitignored, loaded with `python-dotenv`. A key pushed to a public repo is compromised within minutes — bots scan GitHub continuously — and removing it from history is genuinely painful.

### Practice Exercises
- [ ] Complete [Learn Git Branching](https://learngitbranching.js.org/) — all Main levels. Interactive, visual, and the fastest path to actual understanding.
- [ ] Put all previous projects on GitHub, each with a proper README (what it does, install steps, usage, screenshot).
- [ ] Create a branch, make three commits, merge it, then deliberately create and resolve a conflict.
- [ ] Fork a small open-source repo, fix a typo in its docs, and open a pull request. Your first real contribution.
- [ ] Write a `.gitignore` from [gitignore.io](https://www.toptal.com/developers/gitignore) and verify `.venv` is excluded.

### Resources
- [Pro Git Book](https://git-scm.com/book/en/v2) — free, complete, the reference
- [Learn Git Branching](https://learngitbranching.js.org/) — start here
- [GitHub Docs — Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — plain-language recovery from common disasters

---

## 3.5 — Working with APIs
**Time: 15–18 hours**

### Explanation
An **API** lets your program request data from a service over the internet. This is where your projects stop being toys and start using real, live data.

**HTTP fundamentals first:** methods (`GET` read, `POST` create, `PUT`/`PATCH` update, `DELETE` remove), status codes (2xx success, 4xx your mistake, 5xx theirs — memorise 200, 201, 400, 401, 403, 404, 429, 500), headers, query parameters, and the request/response cycle.

**The `requests` library:**
```python
import requests

response = requests.get(
    "https://api.example.com/users",
    params={"page": 2},
    headers={"Authorization": f"Bearer {token}"},
    timeout=10,                       # always set a timeout
)
response.raise_for_status()           # raises on 4xx/5xx
data = response.json()                # → dict/list, exactly like Phase 2
```

**Handle these properly** — this is what distinguishes competent API code:
- Always set `timeout`. Without it a hung server hangs your program indefinitely.
- Catch `requests.exceptions.RequestException` (covers connection errors, timeouts, HTTP errors).
- Respect **rate limits** — check for 429, read `Retry-After`, and implement exponential backoff.
- Handle **pagination** — most APIs return data in pages; write a loop or generator that follows `next` links.
- Never assume the response shape. Use `.get()` with defaults on the parsed JSON.

**Authentication:** API keys in headers or query params, Bearer tokens, and a conceptual understanding of OAuth2 flows (you rarely implement these from scratch). Keys live in `.env`, loaded with `python-dotenv`, never in source.

**Free APIs to practise on:** [Open-Meteo](https://open-meteo.com/) (weather, no key), [REST Countries](https://restcountries.com/), [PokéAPI](https://pokeapi.co/), [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (fake data for testing), [NASA APOD](https://api.nasa.gov/), [CoinGecko](https://www.coingecko.com/en/api), [The Movie Database](https://developer.themoviedb.org/).

### Practice Exercises
- [ ] Fetch and pretty-print the weather for any city the user names.
- [ ] Consume a paginated API and collect every result across all pages.
- [ ] Write a wrapper class around one API with methods, retry logic, and response caching.
- [ ] Deliberately break things: bad URL, bad key, no internet — and handle each failure gracefully.
- [ ] Combine two APIs in one program (e.g. country lookup → its capital's weather).

### Mini-project
- [ ] **Multi-Source Dashboard (400–500 lines):** a CLI tool pulling from 3+ APIs (weather, news, crypto prices, GitHub stats — your choice). Cache responses to a local JSON file with a TTL to avoid hammering the APIs, handle every failure mode without crashing, load keys from `.env`, and render a clean formatted terminal report.

### Resources
- [Requests documentation](https://requests.readthedocs.io/)
- [Real Python — API Integration](https://realpython.com/api-integration-in-python/)
- [MDN — HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Public APIs list](https://github.com/public-apis/public-apis)

---

## 3.6 — Testing & Debugging
**Time: 12–15 hours** *(the most underrated topic here — and the clearest signal of professionalism)*

### Explanation
Beginners test by running the program and looking at it. Professionals write tests that run automatically, every time, forever.

**pytest** is the standard:
```python
# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_raises_on_string():
    with pytest.raises(TypeError):
        add("2", 3)
```
Run with `pytest`. Learn: the **Arrange-Act-Assert** structure, `pytest.raises` for expected exceptions, `@pytest.mark.parametrize` to run one test against many inputs, and **fixtures** for reusable setup.

**What to test:** the happy path, edge cases (empty input, zero, negative, one element, huge values), and error conditions. **Aim for meaningful coverage, not 100%** — a test suite that only exercises the easy paths is a false sense of security.

**Debugging, in escalating order:**
1. **Read the traceback carefully.** Bottom line = what went wrong; lines above = how you got there. Most bugs are solved here.
2. **`print()` debugging** — legitimate, fast, and used by professionals. Print the variable *and* its type.
3. **`breakpoint()`** — drops you into the `pdb` interactive debugger at that line. Learn `n` (next), `s` (step in), `c` (continue), `p var` (print), `l` (list source), `q` (quit).
4. **VS Code's visual debugger** — breakpoints, variable inspection, step controls. Learn this properly; it's a genuine multiplier.
5. **`logging`** instead of `print` for anything real — levels (DEBUG/INFO/WARNING/ERROR/CRITICAL), configurable output, no need to strip statements before shipping.

**Also worth learning:** type hints (`def add(a: int, b: int) -> int:`) plus `mypy`, and the formatters/linters `ruff` and `black`. They catch a class of bugs before you run anything and make your code look professionally maintained.

### Practice Exercises
- [ ] Write a full pytest suite for your Phase 1 function library — happy paths, edges, and errors.
- [ ] Use `@parametrize` to test one function against 10 input/output pairs in a single test.
- [ ] Write a fixture that sets up a temporary test data file and cleans it up after.
- [ ] Practise **TDD** on one small feature: write the failing test first, then the code to pass it.
- [ ] Take a deliberately broken script (write one, or find one) and fix it using only `breakpoint()`.
- [ ] Add `logging` to your API dashboard, with DEBUG to file and INFO to console.
- [ ] Run `ruff` and `mypy` across an old project and fix what they surface.

### Resources
- [pytest documentation](https://docs.pytest.org/)
- [Real Python — Getting Started With Testing](https://realpython.com/python-testing/)
- [Real Python — Python Debugging With pdb](https://realpython.com/python-debugging-pdb/)
- [Python Docs — logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Ruff documentation](https://docs.astral.sh/ruff/)

---

## 3.7 — Specialization Track
**Time: 45–60 hours**

### Choosing your path

You now know enough to be useful in any of three directions. Pick **one** and go deep — a portfolio with one strong specialised project beats three shallow ones in different fields. You can always add another later; the fundamentals transfer completely.

| | **Web Development** | **Data Science** | **Automation & Scripting** |
|---|---|---|---|
| **Job titles** | Backend Dev, Python Dev, Full-Stack | Data Analyst, Data Scientist, ML Engineer | DevOps, QA Automation, Platform/Tooling |
| **Job volume** | Highest | High, but more competitive at entry | Moderate, often internal roles |
| **Entry difficulty** | Moderate — lots to learn, clear path | Higher — often expects stats/maths background | Lowest — fastest to demonstrable value |
| **What else you'll need** | HTML/CSS basics, SQL, HTTP, deployment | Statistics, SQL, visualisation, domain knowledge | OS/shell knowledge, scheduling, cloud basics |
| **Time to portfolio-ready** | ~8 weeks | ~8–10 weeks | ~5–6 weeks |
| **Pick this if…** | You like building things people click on | You like finding answers in messy data | You like eliminating repetitive work |

> **Recommended default: Web Development with Flask.** It has the largest entry-level market, the most direct "Python developer" job title match, and it forces you to integrate everything from Phases 1–3 (OOP, files, APIs, testing, Git) into one deployed artifact you can send someone a link to. Full details below; the other two tracks are outlined after it and are equally valid choices.

---

### 🅰️ TRACK A — Web Development with Flask *(recommended default)*

**Why Flask before Django:** Flask is small enough that you can see how the whole request/response cycle works. Django hides more behind conventions, which is excellent once you understand what's being hidden and confusing before. Learn Flask, build something real, then Django becomes straightforward — and by then you'll actually be able to read its documentation.

#### A.1 — Web Fundamentals *(6–8 hrs)*
- [ ] How the web works: DNS → request → server → response → render
- [ ] HTML structure: semantic tags, forms, inputs
- [ ] CSS basics: selectors, the box model, flexbox — enough to not look broken
- [ ] Client vs server: what runs where, and why it matters
- [ ] Resources: [MDN — Getting Started With the Web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web), [freeCodeCamp Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/)

#### A.2 — Flask Core *(10–12 hrs)*
- [ ] App setup, `@app.route()`, running the dev server
- [ ] Dynamic routes (`/user/<username>`), HTTP methods, query params
- [ ] **Jinja2 templates:** variables, loops, conditionals, template inheritance with `base.html`
- [ ] `static/` for CSS, JS, and images
- [ ] Handling `POST` forms with `request.form`; the POST-Redirect-GET pattern
- [ ] `flash()` messages, `url_for()`, custom 404/500 error pages
- [ ] Resources: [Flask Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/), [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) *(the definitive free Flask course)*

#### A.3 — Databases & SQL *(10–12 hrs)*
- [ ] Relational concepts: tables, rows, primary/foreign keys, relationships
- [ ] Raw SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`, `JOIN`, `GROUP BY` — learn actual SQL before an ORM hides it
- [ ] SQLite via the `sqlite3` stdlib module
- [ ] **Flask-SQLAlchemy:** models as classes, relationships, queries — note how naturally this follows from your OOP work
- [ ] Migrations with Flask-Migrate
- [ ] Resources: [SQLBolt](https://sqlbolt.com/) *(free, interactive, excellent)*, [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

#### A.4 — Users, Auth & Structure *(8–10 hrs)*
- [ ] Registration and login with **Flask-Login**
- [ ] Password hashing with `werkzeug.security` — never store plaintext passwords, ever
- [ ] Sessions and cookies; protecting routes with `@login_required`
- [ ] Form validation with **Flask-WTF** and CSRF protection
- [ ] App structure: blueprints, application factory pattern, config classes for dev/prod
- [ ] Resources: [Flask-Login docs](https://flask-login.readthedocs.io/), [Flask Mega-Tutorial Parts 5–7](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)

#### A.5 — Building & Consuming APIs *(6–8 hrs)*
- [ ] REST principles: resources, verbs, status codes, statelessness
- [ ] Build JSON endpoints; serialise your models
- [ ] Test your API with `curl` and [Postman](https://www.postman.com/)
- [ ] Testing Flask routes with pytest and the test client
- [ ] Resources: [Flask — Building a REST API](https://flask.palletsprojects.com/en/latest/tutorial/), [Real Python — Flask REST APIs](https://realpython.com/flask-connexion-rest-api/)

#### A.6 — Deployment *(6–8 hrs)*
- [ ] Environment variables and config separation for production
- [ ] `gunicorn` as the production WSGI server (the dev server is not for production)
- [ ] Deploy free on [Render](https://render.com/), [Railway](https://railway.app/), or [PythonAnywhere](https://www.pythonanywhere.com/)
- [ ] Basic Docker: what a container is, writing a simple `Dockerfile`
- [ ] A GitHub Actions workflow that runs your tests on every push
- [ ] Resources: [Render — Deploy Flask](https://render.com/docs/deploy-flask), [Docker Get Started](https://docs.docker.com/get-started/)

#### A.7 — *(Optional, +10 hrs)* Django Orientation
Once Flask is solid, build one small Django app to understand MTV structure, the ORM, the admin site, and class-based views. Many job listings name Django specifically, and after Flask the transition is mostly vocabulary.
- [ ] Resources: [Django Official Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/), [Django Girls Tutorial](https://tutorial.djangogirls.org/)

---

### 🅱️ TRACK B — Data Science with Pandas & NumPy

#### B.1 — NumPy *(8–10 hrs)*
- [ ] `ndarray` vs Python list; why vectorisation is 10–100× faster
- [ ] Creation, shape, dtype, reshape, indexing, boolean masking, broadcasting
- [ ] Aggregations along axes; `np.where`, `np.random`
- [ ] Resources: [NumPy Absolute Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)

#### B.2 — Pandas Core *(14–18 hrs)*
- [ ] `Series` and `DataFrame`; reading CSV/JSON/Excel/SQL
- [ ] Inspection: `.head()`, `.info()`, `.describe()`, `.dtypes`, `.shape`
- [ ] Selection: `.loc` (labels) vs `.iloc` (positions) — learn the difference precisely
- [ ] Filtering with boolean masks; chained conditions with `&`, `|`
- [ ] **Cleaning:** missing values (`.isna()`, `.fillna()`, `.dropna()`), duplicates, dtype conversion, string methods via `.str`
- [ ] `.groupby()` — split-apply-combine, the single most important Pandas concept
- [ ] Merging and joining (`.merge()`, `.concat()`), pivot tables, reshaping
- [ ] Time series: `to_datetime`, resampling, rolling windows
- [ ] Resources: [Pandas — 10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html), [Kaggle Pandas course](https://www.kaggle.com/learn/pandas) *(free, hands-on)*

#### B.3 — Visualisation *(8–10 hrs)*
- [ ] Matplotlib: figures, axes, plot types, labels, subplots, saving figures
- [ ] Seaborn: statistical plots in far less code; `heatmap`, `pairplot`, `boxplot`
- [ ] Chart selection: which plot answers which kind of question — and how to mislead accidentally
- [ ] Resources: [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html), [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html), [Kaggle Data Visualization](https://www.kaggle.com/learn/data-visualization)

#### B.4 — Jupyter, SQL & Statistics *(10–12 hrs)*
- [ ] Jupyter notebooks: cells, kernel state, and how to keep a notebook reproducible
- [ ] SQL for analysts: joins, aggregates, subqueries, window functions ([SQLBolt](https://sqlbolt.com/))
- [ ] Descriptive statistics, distributions, correlation vs causation, sampling bias
- [ ] Resources: [Kaggle Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning), [Think Stats (free book)](https://greenteapress.com/thinkstats2/)

#### B.5 — The Analysis Workflow *(6–8 hrs)*
- [ ] Ask a question → acquire → clean → explore (EDA) → visualise → communicate
- [ ] Writing up findings for a non-technical reader — the skill that gets analysts hired
- [ ] *(Optional)* A first scikit-learn model: train/test split, fit, evaluate

---

### 🅲 TRACK C — Automation & Scripting

#### C.1 — Filesystem & OS Automation *(8–10 hrs)*
- [ ] `pathlib` and `shutil` for bulk file operations: rename, move, copy, organise by type/date
- [ ] `os.walk` for recursive traversal; `glob` patterns
- [ ] `subprocess` to run shell commands and capture output safely
- [ ] Robust CLI tools with `argparse`; then try [Typer](https://typer.tiangolo.com/)
- [ ] Resources: [Automate the Boring Stuff (free online)](https://automatetheboringstuff.com/) — the canonical text for this track

#### C.2 — Web Scraping *(10–12 hrs)*
- [ ] `requests` + **BeautifulSoup**: parse HTML, select by tag/class/CSS selector
- [ ] Handling pagination, sessions, and headers
- [ ] **Playwright** or Selenium for JavaScript-rendered pages
- [ ] Ethics and legality: `robots.txt`, terms of service, rate limiting, identifying your bot
- [ ] Resources: [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Real Python — Web Scraping](https://realpython.com/beautiful-soup-web-scraper-python/), [Playwright Python](https://playwright.dev/python/)

#### C.3 — Document & Data Automation *(8–10 hrs)*
- [ ] Excel with `openpyxl` — read, write, format, formulas, charts
- [ ] PDFs with `pypdf` — merge, split, extract text
- [ ] Automated email with `smtplib` and `email`
- [ ] Report generation: data in, formatted document out
- [ ] Resources: [openpyxl docs](https://openpyxl.readthedocs.io/), [Automate the Boring Stuff Ch. 13–18](https://automatetheboringstuff.com/)

#### C.4 — Scheduling & Reliability *(8–10 hrs)*
- [ ] `cron` (macOS/Linux) or Task Scheduler (Windows); the `schedule` library for in-process timing
- [ ] Structured `logging` so unattended scripts are diagnosable after the fact
- [ ] Retry logic with exponential backoff; idempotency (safe to run twice)
- [ ] Notifications on failure — email, Slack webhook, or Telegram bot
- [ ] Resources: [crontab.guru](https://crontab.guru/), [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)

#### C.5 — Deployment & Ops Basics *(6–8 hrs)*
- [ ] Running scripts on a free-tier cloud VM or [GitHub Actions](https://docs.github.com/en/actions) on a schedule
- [ ] Secrets management with environment variables and `.env`
- [ ] Basic Docker for reproducible script environments

---

## PHASE 3 CAPSTONE PROJECTS
**Time: 40–60 hours** *(build one — the one matching your track)*

> **What makes a capstone count.** Not size. Three things: it does something a real person would actually want, it's deployed or runnable by a stranger in under five minutes, and it's documented well enough that a reviewer understands it without asking you. A modest, polished, deployed project beats an ambitious half-finished one every single time.

### 🅰️ Web Track — **TaskFlow: Collaborative Project Manager**

A multi-user web app where teams create projects, assign tasks, and track progress.

**Core requirements**
- [ ] User registration, login, logout with hashed passwords and session management
- [ ] Full CRUD for projects and tasks; tasks belong to projects, projects belong to users
- [ ] SQLAlchemy models with proper relationships (one-to-many, many-to-many for tags/collaborators)
- [ ] Task attributes: title, description, status, priority, due date, assignee
- [ ] Filter and sort views; a dashboard with completion stats and overdue warnings
- [ ] File attachments on tasks with validated upload handling
- [ ] A JSON REST API exposing projects and tasks, with API-key auth
- [ ] Integration with one external API (e.g. email notifications, or calendar export)
- [ ] Search across tasks and projects
- [ ] Responsive templates with Jinja inheritance and a shared `base.html`

**Professional requirements**
- [ ] Blueprints and an application factory — not one giant `app.py`
- [ ] pytest suite covering models, routes, and auth (aim for the critical paths, not a coverage number)
- [ ] `.env` config, `requirements.txt`, `.gitignore`, no secrets in the repo
- [ ] Meaningful Git history — 40+ commits on feature branches, not one "final version" commit
- [ ] **Deployed and publicly reachable** on Render/Railway/Fly.io
- [ ] README with screenshots, feature list, tech stack, local setup instructions, and a live demo link
- [ ] Demo credentials so a reviewer can log in immediately without registering

### 🅱️ Data Track — **End-to-End Data Analysis & Dashboard**

Pick a domain you actually care about (climate, football, housing, music, public health) and a real messy dataset — [Kaggle](https://www.kaggle.com/datasets), [data.gov](https://data.gov/), or [Our World in Data](https://ourworldindata.org/).

- [ ] Acquire data from at least two sources — one file, one API or scrape — and merge them
- [ ] A documented cleaning pipeline: missing values, outliers, dtypes, duplicates, inconsistent categories. Justify every decision in writing.
- [ ] Exploratory analysis notebook with clear narrative between cells, not just code
- [ ] 6+ visualisations, each answering a specific stated question
- [ ] At least three non-obvious findings, with caveats about what the data *can't* tell you
- [ ] A reusable, importable `.py` module for the cleaning logic — notebooks call it, so the pipeline is testable
- [ ] pytest tests on the transformation functions
- [ ] An interactive [Streamlit](https://docs.streamlit.io/) dashboard with filters, deployed to Streamlit Community Cloud
- [ ] A written report for a non-technical reader: question, method, findings, limitations
- [ ] *(Stretch)* A predictive model with honest evaluation and discussion of what it gets wrong

### 🅲 Automation Track — **Personal Operations Suite**

A collection of production-grade automations running unattended on a schedule.

- [ ] **Module 1 — File organiser:** watches a folder, sorts by type/date into a rule-based structure, handles name collisions, logs everything, and supports `--dry-run`
- [ ] **Module 2 — Data collector:** scrapes or calls APIs on a schedule (prices, job listings, weather), stores to SQLite with history
- [ ] **Module 3 — Reporter:** queries collected data, generates a formatted Excel/PDF report with charts, emails it weekly
- [ ] **Module 4 — Monitor:** checks conditions (price threshold, site down, new listing) and sends alerts via Slack/Telegram/email
- [ ] Unified CLI (`ops files organise`, `ops report weekly`) via `argparse` or Typer
- [ ] YAML/JSON config file so behaviour changes without editing code
- [ ] Structured logging with rotation; retry with exponential backoff on every network call
- [ ] Idempotent by design — safe to run twice, no duplicate work or data
- [ ] pytest suite with mocked network calls, so tests run offline
- [ ] Scheduled and running unattended (cron or GitHub Actions), with failure alerting
- [ ] README with architecture diagram, setup guide, and configuration reference

---

# Job Readiness Checklist
*Work through this in parallel with Phase 3, not after it.*

### Portfolio
- [ ] GitHub profile with a README, a profile photo, and pinned repositories
- [ ] 4–6 repos, each with a real README (problem, features, tech, setup, screenshot)
- [ ] At least one **deployed, publicly accessible** project with a live link
- [ ] Clean commit history that shows incremental work, not a single dump
- [ ] Zero secrets in any repo — audit this before you share anything

### Demonstrable skills
- [ ] Solve an unseen LeetCode Easy in under 30 minutes while explaining your reasoning aloud
- [ ] Explain Big-O for the operations of every core data structure
- [ ] Walk someone through your capstone architecture and defend your design decisions
- [ ] Read an unfamiliar codebase and describe what it does
- [ ] Debug a bug you didn't write, in front of someone, without panicking

### Professional practice
- [ ] Every project uses a venv and has a `requirements.txt`
- [ ] Every project has tests that actually run
- [ ] Comfortable with branches, merges, conflicts, and pull requests
- [ ] At least one merged open-source contribution, however small

### Adjacent knowledge worth having
- [ ] SQL — non-negotiable for web and data roles
- [ ] Basic Linux/shell command line
- [ ] What Docker is and roughly why it exists
- [ ] HTTP fundamentals and REST conventions
- [ ] How to write a clear technical explanation in plain English

---

# Progress Tracker

| Phase | Topics | Hours | Started | Finished |
|---|---|---|---|---|
| **Phase 0** — Setup | 6 | 2–4 | ☐ | ☐ |
| **Phase 1** — Fundamentals | 9 + capstone | 90–120 | ☐ | ☐ |
| **Phase 2** — Data Structures | 9 + capstone | 80–110 | ☐ | ☐ |
| **Phase 3** — Development Track | 7 + capstone | 140–180 | ☐ | ☐ |
| **Job Readiness** | 4 sections | ongoing | ☐ | ☐ |
| | **Total** | **~315–415 hrs** | | |

### Milestone checkpoints
- [ ] **Week 10** — Phase 1 capstone shipped. *You can write a working program from a blank file.*
- [ ] **Week 19** — Phase 2 capstone shipped. *You choose data structures deliberately and can justify them.*
- [ ] **Week 26** — OOP, files, Git, APIs, testing complete. *You work like a developer, not a student.*
- [ ] **Week 34** — Specialization capstone deployed. *You have something worth showing an employer.*

---

# The Five Things That Will Actually Determine Your Outcome

1. **Finish things.** A completed small project teaches more than three abandoned ambitious ones, because the last 20% — error handling, edge cases, documentation, deployment — is where the real learning lives, and it's exactly the part people skip.

2. **Type the code.** Reading code creates the feeling of understanding without the substance. The gap between "I follow this" and "I can write this" is enormous and only closes through your own keystrokes.

3. **Build things you want to exist.** Motivation is the scarce resource over 8 months, not time or intelligence. A tracker for your actual hobby will get finished; a generic tutorial clone will not.

4. **Be consistent over intense.** 90 minutes daily beats 10 hours every other Saturday, decisively. Programming knowledge decays fast without contact, and momentum is most of the battle.

5. **Get your code read.** Post in [r/learnpython](https://reddit.com/r/learnpython), use Exercism's mentor feedback, find a study partner. You cannot see your own blind spots by definition, and the feedback loop is what turns 8 months of practice into 8 months of *progress*.

---

## Master Resource List

**Structured free courses**
- [CS50P — Harvard's Intro to Programming with Python](https://cs50.harvard.edu/python/) — the best free structured course available
- [freeCodeCamp — Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — free online, ideal for the automation track

**Reference**
- [Official Python Docs](https://docs.python.org/3/) — get comfortable reading these early; it's a skill in itself
- [Real Python](https://realpython.com/) — many free articles, consistently high quality
- [Python Module of the Week](https://pymotw.com/3/) — standard library, deeply explained

**Practice**
- [Exercism](https://exercism.org/tracks/python) · [Codewars](https://www.codewars.com/) · [LeetCode](https://leetcode.com/) · [HackerRank](https://www.hackerrank.com/domains/python) · [Advent of Code](https://adventofcode.com/)

**Video**
- [Corey Schafer](https://www.youtube.com/@coreyms) — the clearest Python explainer on YouTube
- [ArjanCodes](https://www.youtube.com/@ArjanCodes) — design and architecture, valuable from Phase 3 onward
- [mCoding](https://www.youtube.com/@mCoding) — deeper language internals

**Tools**
- [Python Tutor](https://pythontutor.com/) · [Learn Git Branching](https://learngitbranching.js.org/) · [regex101](https://regex101.com/) · [SQLBolt](https://sqlbolt.com/) · [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

**Community**
- [r/learnpython](https://reddit.com/r/learnpython) — genuinely welcoming to beginners
- [Python Discord](https://pythondiscord.com/) — live help
- [Stack Overflow](https://stackoverflow.com/) — read before you post; learn to write a minimal reproducible example

---

*Start with Phase 0 today. Not tomorrow, not after you've researched the perfect setup. The single strongest predictor of finishing is starting badly and continuing anyway.*


**learning prompt :- when i ask you something ie. "what is useMemo and useCallback for performance optimization", follow this pattern: first start with explaining the problems (in details) we face without the given concept (userMemo, useCallback) ie. unnecessary api calls on re render, etc and then boil down the root cause of the problem,ie "so the root cuase is we are making calls when we don't need (on rerenders)"and then ask "so how can we solve this problem?" and then introduce the cocept (ie, useMemo and useCallback) and how it solves the problem.

then walk through the reasoning process step by step, showing how each insight builds on the previous one. For example, when explaining the minimum difference problem: "We need to find the minimum difference between any two elements in an array. When is this difference smallest? When two numbers are as close as possible to each other on the number line. How can we easily identify adjacent numbers? By arranging all elements in order. What's the most efficient way to arrange elements? By sorting the array. Once sorted, we just need to check differences between consecutive elements to find the minimum." Please apply this cause-and-effect reasoning to any problem I ask about. Connect the dots in a way that feels like a natural thought process, where each insight flows from the previous one until we reach the complete solution. and emphasize more on "why" aspect

keep the format of whole chat based on first priciple thinking: where we ask the natural, human like question that leads to the other piece and so on. this we we reach the truth why following the human curiosity. ie. so what we used to use before these hooks? okay, so what were the problems in those methods? what is the root cause/s of the problem/s? how does [hooks (or the given)] concept fix it?. ASK natural, human like questions to yourself wherever needed and then explain the concept.

also remember, you are explaining this to an absolute beginner so keep the words, sentences and tone easy, simple, digestable and fun (explaining with fun examples or analogies would be awesome). (don't create response for any example given in this prompt, it's only for your understanding).**