# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# To take input from the user
nterms = int(input("How many terms? "))

# first two terms
num1 = 0
num2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(num1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(num1)#end=' , ')
       nthnum = num1 + num2
       # update values
       num1 = num2
       num2 = nthnum
       count += 1
