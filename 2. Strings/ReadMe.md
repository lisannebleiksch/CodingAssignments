# Assignment 2: Strings (Football Match Report)

**Goal**  
Get a first real feeling for programming by working with **strings**, **integers**, and basic string operations in Python.

You will write a small script that:
- prints a football scorers line
- prints a short match report
- manipulates player names using slicing and string methods
- generates a simple football chant

You may choose **any footballers** you like.

---

## How to run

Python is already installed.

From the folder containing `main.py`, run:

```bash
python main.py
```

---

## Part 1: Match scorers and report

Create variables for:
both footballer first and last name, goal 1 was in the 32th minut and goal 2 in the 54th minute
- `scored_player_1` (string)
- `scored_player_2` (string)
- `goal_0` (integer)
- `goal_1` (integer)

### 1. Scorers line

Print **one line** with the scorers and minutes.

Format:

```
<Player 1> <minute>, <Player 2> <minute>
```

Rules:
- Goal minutes must remain **integers**
- Convert them to strings using `str(...)` when concatenating

---

### 2. Match report

Print a **two-line** report using an **f-string** and a newline (`\n`).

---

## Part 2: String slicing and methods

Create a variable:

- `player` containing a full name with **exactly one space**, for example:

### 1. Find the space

Use `.find(" ")` to find the index of the space and store it in `find_space`.

### 2. First name

Use slicing to extract the first name from `player`.

### 3. Last name length

Calculate how many characters the last name has  
(hint: use `len()` and slicing).

### 4. Short name

Create a short name like:

```
R. Koeman
```

Rules:
- Use slicing
- Use `.find(" ")`
- Do not hardcode indexes

### 5. Chant

Create a chant where:
- the first name followed by `!` is repeated `len(first_name)` times
- there is **one space** between repetitions
- the chant does **not** end with a space

Example for `Ronald`:

```
Ronald! Ronald! Ronald! Ronald! Ronald! Ronald!
```

### 6. Validation

Create a boolean variable `good_chant` that checks whether your chant is **exactly equal** to the expected chant for your chosen name.

Print the result. It should be `True` if everything is correct.

---
