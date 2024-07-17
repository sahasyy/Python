num=int(input("enter a number"))
num_digits=len(str(num))
sum=0
a=num
while a>0:
    digit=a%10
    sum+=digit**num_digits
    a=a//10
if num==sum:
    print("armstrong number")
else:
    print("not an armstrong number")
