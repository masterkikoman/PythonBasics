#Looping in Python

obj = [9, 8, 7, 6, 5]
for i in obj:
    print(i)


# sum of First Natural numbers 1+2+3+4+5=15
value = 0
for j in range(1, 6):  # range (i,j) -> i to j-1
    value = value + j

print("final output", value)

print("*************************printing 2 indexes difference****************************************************")
for k in range(1, 10, 2):  # printing 2 indexes difference
    print(k)


print("************************printing 0 - 9 index*****************************************************")
for m in range(10):
    print(m)
