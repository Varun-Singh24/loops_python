#  sum of n natural number 
sum = 0  
for i in range (1, number): 
    sum = sum + i 
    if sum > 30 : 
        break
    print (i, sum)


# USING While Loop 

number = int(input("Enter the Number : "))
sum = 0 
i = 1 
while (sum < number ): 
    print(i, sum ) 
    sum = sum + i
    i += 1 

# Reverse the Number using while Loop 

num = int(input("Enter a number to reverse: "))
reverse = 0

while num > 0:
    last_digit = num % 10          # Get the last digit
    reverse = (reverse * 10) + last_digit  # Build the reversed number
    num = num // 10                # Remove the last digit
    
print(f"Reversed Number: {reverse}")

