
# creating Array or List
# Data types that allows multiple values and can be different

values = [1, 2, "Taki", 4.4, 5]

# printing per index

print(values[0])  # 1
print(values[3])  # 4.4
print(values[-1])  # 5
print(values[1:4])  # 2 Taki 4.4

# inserting values inside the list or array
values.insert(3, "Mitsuha")

print(values)  # [1, 2, 'Taki', 'Mitsuha', 4.4, 5]

# inserting value at the end of the list
values.append("Hello")  # [1, 2, 'Taki', 'Mitsuha', 4.4, 5, 'Hello']
print(values)

# editing/updating values inside the List and Array
values[2] = "Chihiro"  # [1, 2, 'Chihiro', 'Mitsuha', 4.4, 5, 'Hello']

print(values)

# deleting value
del values[0]
print(values)  # [2, 'Chihiro', 'Mitsuha', 4.4, 5, 'Hello']

# Tuple - same as list but immutable updating of values is not possible

print("TUPLE")
value = (1, 2, "Taki", 4.4, 5)
print(value[2])


# Dictionary - Key value pair
print("Dictionary")
dic = {"a": 2, 4: "abc", "c": "Haku"}
print(dic[4])
print(dic["c"])

# Creating Dictionary Dynamically

dict = {}
dict["firstName"] = "Totoro"
dict["lastName"] = "Mizuki"
dict["gender"] = "N/A"
print(dict)