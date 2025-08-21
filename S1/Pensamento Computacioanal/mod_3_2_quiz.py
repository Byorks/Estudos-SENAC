# 3.2.17 SECTION QUIZ

# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
for i in range(1, 11):
    if i % 2 != 0:  print(i)


# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
x = 1
while x < 11:
    if i % 2 != 0: print(i)
    x +=1
    
# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

email = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        email +=ch