n = int(input("Enter your number "))
rev = 0
temp = n
while(n > 0):
    last = n % 10
    print(last)
    rev = rev * 10 + last
    #print(rev)
    n = n //10
#print("Orignal number is ", temp ,"\nReverse number is " ,rev)
