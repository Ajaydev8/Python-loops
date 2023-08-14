#  In this code we're going to calculate the addition of all the even number in the range of 100.

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(f"The total of the even number is {total}")
