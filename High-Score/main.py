# This code was copied from the coding exercise website of Angela Yu 100 days of python code.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# This is my code

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score is {high_score}")