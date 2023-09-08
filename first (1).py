#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Print First 10 natural numbers using while loop
i = 1 
while i <= 10:
    print(i)
    i = i + 1


# In[11]:


#  Calculate the sum of all numbers from 1 to a given number
p = 0
n = int(input("Enter the number:"))
for i in range(1, n+1, 1):
    p = p + i
    
    
print("\n")
print("Sum is:", p)


# In[1]:


s = int(input("enter number:"))
x = sum(range(1,s+1))
print("sum is:", x)


# In[7]:


# Write a program to print multiplication table of a given number
num = int(input("Multiplication table of:"))
for i in range(1, 11,):
    product = num*i

    print(product)
    


# In[16]:


# Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for items in numbers:
    if items > 500:
        break
    elif items > 150:
        continue
    elif items % 5 == 0:
        print(items)
    
    
    
    



# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


# In[2]:


# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)


# In[3]:


#  Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)


# In[4]:


# Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")


# In[5]:


# Write a program to display all prime numbers within a range
start = 25 
end = 50
print("Prime numbers between", start, "and", end,"are:")



for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[10]:


#  Display Fibonacci series up to 10 terms
first, second = 0, 1



print("Fibonacci sequence:")
for i in range(10):
    print(first, end=" ")
    third = first + second 
 


    first = second 
    second = third



# In[ ]:




