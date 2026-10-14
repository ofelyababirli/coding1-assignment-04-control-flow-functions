def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 1st part of the code means add 1 to the value ( whatever the value is). 
#The second condition part means, numbers are to be selected among 1 2 3 and it puts if condition,
# if it is bigger than 1, so it means it will choose 2 and 3. So python will print 3 and 4 in order. 

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: The value equals to 2, and 2+1 it will be 3. It keeps 3 in mind but does not print it unless written print.
