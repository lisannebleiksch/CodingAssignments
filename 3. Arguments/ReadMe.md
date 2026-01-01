# Assignment 3: Arguments

You are going to practice **function arguments** and using a **dictionary** to look up values.

## What you will build

You will implement three functions:

1. `greet(name, greeting=...)`
2. `force(mass, body=...)` using a `gravity_by_body` dictionary
3. `pull(m1, m2, d)` (Newton’s law of gravitation)

Keep your code clean and readable. Use `return` values, not only `print`.

## Tasks

### 1) Greet someone
Create a function:

- **Name:** `greet`
- **Arguments:**
  - `name` (required)
  - `greeting` (optional, default: `"Hello, <name>!"`)
- **Behavior:**
  - Replace the substring `"<name>"` in `greeting` with the value of `name`
  - Return the final string

### 2) Calculate weight on a planet using a dictionary
Create a function:

- **Name:** `force`
- **Arguments:**
  - `mass` (required, in kg)
  - `body` (optional, default: `"earth"`)
- **Use a dictionary:**
  - `gravity_by_body` maps a planet name (string) to gravity (m/s²)
- **Behavior:**
  - Look up `g` using `gravity_by_body[body]`
  - Compute weight: `weight = mass * g`
  - Return `weight` rounded to **2 decimals**
- **Extra:**
  - If `body` is not in the dictionary, raise a `ValueError` with a clear message.

### 3) Calculate gravitational pull between two masses
Create a function:

- **Name:** `pull`
- **Arguments:**
  - `m1` (required, kg)
  - `m2` (required, kg)
  - `d` (required, meters)
- **Behavior:**
  - Use the gravitational constant `G = 6.674e-11`
  - Compute: `F = G * (m1 * m2) / (d ** 2)`
  - Return `F` (a float)
- **Extra:**
  - If `d <= 0`, raise a `ValueError`

## What to run

When you run `python main.py`, your script should:

- Print a greeting for one person
- Print the weight for one mass on one body
- Print one gravitational pull calculation
