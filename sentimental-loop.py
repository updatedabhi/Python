#WAP to calculate sum and average of n random number. using sentinel controled loop
print("Enter any +ve number and -1 to exit: ")
n = int(input("Enter any number"))
sum = 0
count = 0
while(n != -1):
    sum = sum + n
    n = int(input("Enter any number"))
    count = count + 1
print(sum)
avg = sum / count
print(avg)
    
