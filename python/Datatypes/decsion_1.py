def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


num = int(input("Enter a number: "))
result = check_odd_even(num)
print(f"The number {num} is {result}.")

print()
days = int(input('Enter the day betweeen 1 to 7 : '))
if days == 1:
    print('Monday ')
elif days == 2:
    print('Tuesday')
elif days == 3:
    print('Wednesday')
elif days == 4:
    print('THrusday')
elif days == 5:
    print('Friday')
elif days == 6:
    print('Saturday')
elif days == 7:
    print('Sunday')
