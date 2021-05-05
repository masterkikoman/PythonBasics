str = "MasterKikoMan"

print(str[1]) # a

# Extracting substring from whole string
print(str[6:10]) # Kiko

#Concatinate 2 Strings
str1 = "The Greatest"
str2 = "of them all"

print(str1+str2)

# Checking if a string is present or not

str4 = "KikoMan"

print(str4 in str)  # Substring check ->True


# Splitting a string
var = str.split("r")
print(var) # ['Maste', 'KikoMan']

# Trim a string
str5 = " Wooleybully "
print(str5.strip())  # removing left and right spaces
print(str5.lstrip())  # removing left spaces
print(str5.rstrip())  # removing right spaces
