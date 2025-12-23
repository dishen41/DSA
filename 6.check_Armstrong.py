n = int(input("Enter the number: "))
num = n 
total = 0
length = len(str(n))

while num > 0:
    ld = num % 10
    total = total + (ld**length)
    num = num//10

print(num == total)
