# Arithmetic Operators ..! (Mathematical operations)

a = 20
b = 40

print (a + b)        # Addition 
print (a - b)          # Subtraction
print (a * b)          # Multiplication
print (a / b)          # Division
print (a % b)          # Reminder
print (a // b)         # Floor Division 
print (a ** b)         # Power star (Trying to calculate a^b)

# Relational Operators ..! (Give Boolean values as output)

print (a == b )         # Equal to
print (a != b)          # Not equal to
print (a > b)           # Greater than
print (a < b)           # Less than
print (a >= b)          # Greater than or equal to
print (a <= b)          # Less than or equal to

# Assignment Operators ..! (Assign values to variables)

num = a
num -=10                                # 20 - 10 = 10
print ("New value of num:", num)
num +=10                                # 10 + 10 = 20
print ("New value of num:", num)
num *=10                                # 20 * 10 = 200  
print ("New value of num:", num)
num /=10                                # 200 / 10 = 20 
print ("New value of num:", num)
num %=40                                # 20 % 40 = 20       
print ("New value of num:", num)
num **=5                               # 20 ^ 5 = 3200000
print ("New value of num:", num)              

# Logical Operators ..! (Give Boolean values as output)

# 1. NOT Operator
x = 4
y = 8 
print (not x < y)          # Not operator (if the condition is true then it will return false and if the condition is false then it will return true)
print (not x > y)          # Not operator (if the condition is true then it will return false and if the condition is false then it will return true)

# AND Operator
val1 = True
val2 = True
age = 16
print (age > 18 and age < 30)
print ("And Operator:", val1 and val2)      # And operator (if both the conditions are true then it will return true and if any of the conditions is false then it will return false)
print ("And Operator:", x==y and x<y)       # And operator (if both the conditions are true then it will return true and if any of the conditions is false then it will return false) 

# OR Operator
print ("OR Operator:", val1 or val2)        # Or operator (if any of the conditions is true then it will return true and if both are false then it will return false)
print ("OR Operator:", x==y or x>y)         # Or operator (if any of the conditions is true then it will return true and if both are false then it will return false)