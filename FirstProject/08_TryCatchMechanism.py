# write a code the code and you think a code may fail
# but you don't want the test case to stop in a specific failure

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Reached Test Case")

# printing the actual error Python throws in an exception
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

# finally Keyword
# will run whether there is a pass or failure in a try block
finally:
    print("you have reached finally block")


