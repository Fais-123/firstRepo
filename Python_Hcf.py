#Hcf and Gcd is same
#we are evaluating HCF/ GCD of two numbers.
#Take 2 numbers
num1=int(input("enter num:"))
num2=int(input("enter num:"))

#find least number of both
if(num1<num2):
    least=num1
else:
    least=num2

#loop through untill find largest number or factor which divides both values completely.
for i in range(1,least+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
        
#printing he GCD / HCF
print(f"HCF/GCD of {num1} and {num2} is {hcf}")
