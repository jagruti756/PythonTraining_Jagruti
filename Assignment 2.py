#1 Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.

a = int(input("Enter a value: "))
x = a
if x%3 == 0 and x%5 == 0:
    print("consultadd - Python Training")

elif x%3 == 0:
    print("consultadd")

elif x%5 == 0:
    print("Python Training")



#2 Write a program in Python to perform the following operator based task:

Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.

option = eval(input("enter number between 1 to 5"))
num1 = eval(input("Enter num1"))
num2 = eval(input("Enter num2"))
if option <=5 and option >=0:
    if option == 1:
        add = num1+num2
        print(add)
    elif option == 2:
        sub = num1-num2
        print(sub)
    elif option == 3:
        div = num1/num2
        print(div)
    elif option == 4:
        multiplication = num1*num2
        print(multiplication)
    elif option == 5:
        num3= eval(input("enter the number to calculate average"))
        num4= eval(input("enter the 2nd value to calculate the average"))
        avg = (num1+num2+num3+num4)/4
        print(avg)
    elif add or sub or div or multiplication or avg <=0:
        print("negative")

#3 #3.Write a program in Python to implement the given flowchart:
a,b,c = 10,20,30
avg = (a+b+c)/3
print("avg =",avg)
if avg > a and avg>b and avg>c:    
   print("avg is higher than a,b,c")
elif avg > a and avg>b:    
   print("avg is higher than a,b")
elif avg > a and avg>c:    
   print("avg is higher than a,c")
elif avg>b and avg>c:    
   print("avg is higher than b,c")
elif avg > a:    
   print("avg is just higher than a")
elif avg > b:    
   print("avg is just higher than b")
elif avg > c:    
   print("avg is just higher than c")


#4 Write a program in Python to break and continue if the following cases occurs:

If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”

while True:
    a = eval(input("enter the value "))
    if a>0:
        print("keep going")
        continue

    if a<0:
        print("it's over")
        break

#5 Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

a =[]
for x in range(2000,3000):
    if(x % 7==0) and (x % 5 != 0):
        a.append(str(x))
print ((a))

#6  What is the output of the following code examples?
x = 123
for i in x:
    print(i)

    #'int' object is not iterable



# 0
#error
#1
#error
#2


#name 'true' not defined

#7 Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement

for i in range(0,6):
    if i==3 or i==6:continue
    print(i)

#8. Write a program that accepts a string as an input from the user and calculatethe number of digits and letters.

digits = letters = 0
raw = input("enter a string:")
for c in raw:    
  if c.isdigit():        
     digits = digits + 1    
  elif c.isalpha():        
     letters = letters + 1
print("Letters", letters)
print("Digits", digits)

#9 Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)


lucky_num = 3
while True:
    number =eval(input("guess the lucky number"))
    if number != lucky_num:continue
    else:
         print("congratulations you have guessed it correct : ")
    break

lucky_num = 3
while True:
    number =eval(input("guess the lucky number"))
    if number != lucky_num:
        print("sorry you have guessed it wrong")
        answer = eval(input(" enter 1 if you want to guess it again , other wise enter 0"))
        if answer == 0:break
        elif answer == 1:continue
    else:
         print("congratulations you have guessed it correct : ")
    break


#10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.


counter = 1
lucky_num = 1
while counter <=6:
    number = eval(input("Enter the lucky number"))
    counter = counter+1
    if counter == 6:
        print("game over")
        break
    if counter != lucky_num:
        print("try again")
    else:
        print("Good guess")

#11 In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.


counter = 1
lucky_num = 1
while counter <=6:
    number = eval(input("Enter the lucky number"))
    counter = counter+1
    if counter == 6:
        print("Sorry that was not very succesful")
        break
    if counter != lucky_num:
        print("try again")
    else:
        print("Good guess")
        break

