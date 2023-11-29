full_name=input('Please Enter Your Name : ')
print(full_name)


num1 = input("whats the first number?")
num2 = input ("whats the second number?")
num3= int(num1)+int(num2)
print(num3)


'this is the Restaurant Calculator'

print("you wnet to the restaurant")
questionOne = input("what did you eat?")
questionTwo = input("how much was the food?")
questionThree = input("how much tip you give?")
result = int(questionThree) + int(questionTwo)

print(result)


food = int(input("how much was the food?"))
tip = int(input("what was your Tip Percentage?: ")) / food
tip_amount = food * tip


total = food + tip_amount
print(f'tip Amount: ${tip_amount}')
print(f'Food Amount: ${food}')


print('$' + str(total))
