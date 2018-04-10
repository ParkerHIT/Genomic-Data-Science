# Python program to check if the input number is prime or not


# Input from the user
num = int(input("Enter a number: "))

# check if prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a Prime Number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a Prime Number")
       
# if input number is less than or equal to 1, it is not prime
else:
   print(num,"is not a Prime Number")
