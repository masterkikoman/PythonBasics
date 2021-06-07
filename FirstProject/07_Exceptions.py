# Forcing test to fail in the scripts

# Scenario Checking if items in cart iw not 0
ItemsInCart = 0

if ItemsInCart !=2:
    # raise keyword is used in excption error
    # raise Exception("Products Cart count not matching")
    pass
print("**********************Assertions************************")

#Assertions
assert(ItemsInCart == 0)