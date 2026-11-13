
count = 1
total = 0

# BUG: Added the missing colon after the while condition.
# BUG: Changed < 5 to <= 5 so the loop includes number 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total to a string using an f-string
# so Python can display the number together with text.
print(f"Sum of 1 to 5 is: {total}")
