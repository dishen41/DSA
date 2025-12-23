num = int(input("Enter the Number: "))

## Brote Force Solution
# a = 1
# result = []

# while a <= num:
#     if num % a == 0:
#         result.append(a)
#     a+=1

# print(result)

## Best solution 
result = []
from math import sqrt
for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num//i!=i:
            result.append(num//i)

print(result)