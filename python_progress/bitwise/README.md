# Python Bitwise Operations & Masking

A quick, practical script demonstrating how to manipulate individual bits using Python's built-in bitwise operators. This is a great reference for understanding low-level data manipulation, binary flags, and bit masking.

## What's Inside

This script breaks down four fundamental bitwise operations:

* **Bitwise XOR (`^`):** Compares two binary numbers and outputs `1` only where the bits differ. The script also shows how to convert the integer result back into a readable binary string using `bin()`.
* **Bitwise NOT (`~`):** Inverts the bits of a number. The script demonstrates how Python handles this mathematically using two's complement (where `~x` equals `-(x+1)`).
* **Bit Checking (AND `&`):** Uses a binary mask (like `0b1000`) to query the state of a specific bit. The script includes two functions (`check_bit4` and `check`) to safely determine if the 4th bit is currently "ON" or "OFF".
* **Setting Bits (OR `|`):** Uses a mask (`0b100`) alongside the OR operator to force a specific bit to turn "ON" while leaving the rest of the original binary sequence completely unchanged.

## How to Run

1. Save the code to a file named `bitwise_demo.py`.
2. Open your terminal or command prompt.
3. Run the script using Python:
```bash
python bitwise_demo.py
````



The terminal will output the results of the XOR and NOT operations, followed by the ON/OFF evaluations from the bit-checking functions.
