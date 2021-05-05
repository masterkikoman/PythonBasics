val = 4

while val > 1:
    print(val)
    val = val - 1

print("while loop execution is done")

print("****************************************printing 4 and 2 only***************************************************")

val2 = 4
while val2 > 1:
    if val2 != 3:
        print(val2)

    val2 = val2 - 1

print("while loop execution is done")

print("****************************************break keyword***************************************************")
val3 = 4
while val3 > 1:
    if val3 == 3:
        break
    print(val3)

    val3 = val3 - 1
print("while loop execution is done")

print("****************************************continue keyword***************************************************")
val4 = 10
while val4 > 1:
    if val4 == 9:
        val4 = val4 -1
        continue
    if val4 == 3:
        break
    print(val4)

    val4 = val4 - 1
print("while loop execution is done")