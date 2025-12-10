numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
variable = 0

while numbers[variable] is not None:
  variable += 1

sum_ = sum(numbers[:variable]) + sum(numbers[variable + 1:])
average_numbers = sum_ / len(numbers)
numbers[variable] = average_numbers

print("Измененный список:", numbers)