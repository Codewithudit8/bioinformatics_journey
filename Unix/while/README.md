Bash Basics: Loops, Arithmetic, and Arrays
A quick, practical Bash script demonstrating fundamental shell scripting concepts. This script serves as a handy reference for standard while loops, math operations, and array manipulation in Unix-like environments.

What's Inside
This script covers four key Bash concepts in a single file:

While Loops & Decrementing: Uses a standard while [[ condition ]] loop to create a countdown, modifying variables on the fly using the let command.

Factorial Calculation (Arithmetic Expansion): Calculates the factorial of a number (5) by using $(( ... )) to perform math operations safely inside a loop.

Array Manipulation:

Creating arrays and accessing specific elements by index (e.g., ${heroes[0]}).

Fetching all elements at once using the * wildcard.

Appending new elements to an existing array using the += operator.

Array Length & Dynamic Math: Demonstrates how to count the total number of items in an array using ${#array[*]} and perform arithmetic to sum the lengths of two different arrays (heroes and villains).

How to Run
Save the code to a file, for example, basics.sh.

Make the script executable by modifying its permissions:

Bash
chmod +x basics.sh
Run the script from your terminal:

Bash
./basics.sh
The terminal will output the countdown, the calculated factorial (120), and the step-by-step modifications made to the superhero and villain arrays.
