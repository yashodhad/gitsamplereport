#5=1*2*3*4*5= 120
# Prints the status of the git repository
# Initialize the repo
fact=1
num=5

if num<0:
    print("Factorial does not exist for negative number")
if num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact=fact *i
    print("the fact of ",num, "is",fact)

