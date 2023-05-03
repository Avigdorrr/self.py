input_bricks = int(input("Enter three digits (each digit for one pig): "))
first_pig = input_bricks // 100
second_pig = input_bricks // 10 % 10
third_pig = input_bricks % 10
sum_of_bricks = first_pig + second_pig + third_pig

print(sum_of_bricks)
print(sum_of_bricks // 3)
print(sum_of_bricks % 3)
print(sum_of_bricks % 3 == 0)