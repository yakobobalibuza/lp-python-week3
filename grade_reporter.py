
scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} | Grade: {grade}")

    total += score

    if score >= 50:
        passed += 1
    else:
        failed += 1

average = total / len(scores)

print("\n--- Grade Report Summary ---")
print(f"Number passed: {passed}")
print(f"Number failed: {failed}")
print(f"Average score: {round(average, 1)}")
