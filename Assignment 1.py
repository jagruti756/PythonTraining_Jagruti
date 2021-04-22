#Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
a,b,c = 1 , 2.0 , "Jagruti"
print(a,b,c)

#2. Create a variable of type complex and swap it with another variable of type integer.
a = 1+1j
b = 2
a,b = b,a
print('a:',a,'b:',b)

#Swap two numbers using a third variable and do the same task without using any third variable.
#swaping using third value
a = 12
b = 10
c = 20
c = a
a = b
b = c
print('a=', a, 'b=', b)
#swaping without using third value
a = 12
b = 10
a,b = b,a
print(a,b)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
#version 3.x
a = input('Enter your age: ')
print(a)
#version 2.x
print user_input

#5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
a = int(input('Enter the first number between 1 to 10 :'))
b = int(input('Enter the second number between 1 and 10 :'))
z = a + b
result = z + 30
print("Final output: ", result)

#6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc

a = eval(input('Enter your value'));
print('The data type of the input value is :',type(a))

#7 Create variables using format such as
#Upper CamelCase
UserName = "John"

#Lower CamelCase
UserLastName = "Windsor"

#Snakecase
user_email_address = "john.windsor@gmail.com"

#Uppercase
PHONENUMBER = 6579876543


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?
a = 'count'
a = 5
print(a)

The value will change because the value to variable a is reassigned.As Python is interpreted language and it runs line by line.
So the latest value is being assigned irrespective of the data type

