
user_num = int(input("Enter a number: "))


odd_numbers = [num for num in range(user_num) if num % 2 != 0]

print("Odd numbers list:", odd_numbers)

fruits=['apple','orange','bannana','kiwi','mango','peach']
capitalised_fruits=[fruit.capitalize()  for fruit in fruits]
print("Original fruits:",fruits)
print("Updated fruits:",capitalised_fruits)