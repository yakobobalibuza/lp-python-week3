
# Grade Reporter & Bug Hunt

PLP Python Week 3 assignment: Practising loops, conditions, counters, and debugging in Python.

## Project Files

- **grade_reporter.py:** Uses a for loop and conditional statements to calculate learner grades, pass and fail counts, and the average score.
- **bug_hunt.py:** Demonstrates debugging by fixing three errors in a while loop program that calculates the sum of numbers from 1 to 5.

## Reflection

The hardest bug to find was the incorrect while loop condition because it did not produce an error message. The program ran successfully but printed 10 instead of the expected answer, 15. I knew something was wrong by comparing the program's output with the expected sum of 1 + 2 + 3 + 4 + 5. I fixed the condition by changing `count < 5` to `count <= 5`.
