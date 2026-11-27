function creation and adding sum of input number .
# Bash Revision: Loops, Brace Expansion & Functions

A practical Bash script reviewing core shell scripting concepts alongside custom functions. It is a clean reference for practicing control flow, sequence generation, and passing arguments to functions.

## What's Inside

* **Loops & Conditionals:** Runs a `for` loop with OR logic (`||`) to print numbers less than 3 or greater than 8, followed by a `while` loop countdown.
* **Arrays & Command Substitution:** Iterates through a DNA sequence array (`${dna[*]}`) and lists files in the current directory using `$(ls)`.
* **Brace Expansion:** Demonstrates generating combinations (`{1..10}{A..J}`), grouped lists (`{{1..10},{A..C}}`), and using `eval` to expand variables inside braces (`{$start..$end}`).
* **Custom Functions & Variable Scope:**
* `cal_sum` & `cal_sum1`: Add all passed arguments (`$@`), showing the difference between global and `local` variables.
* `plier`: Multiplies all passed arguments together.
* `isiteven`: Checks whether a number is even (prints `1`) or odd (prints `2`) using modulo arithmetic.



## How to Run

1. Save the script to a file (for example, `revision_27nov.sh`).
2. Run the script to see the loop and brace expansion outputs:
```bash
bash revision_27nov.sh

```


3. To load and test the functions directly in your terminal, use `source`:
```bash
source revision_27nov.sh
cal_sum1 4 5 6
plier 2 3 4
isiteven 8

```
