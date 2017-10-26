
# coding: utf-8

# # Chapter 5 Exercise 2 

# In[1]:


def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


# In[4]:


check_fermat(1,1,1,1)


# # Chapter 5 Exercise 3

# In[103]:


def triangle(x,y,z):
    if x + y <= z:
        print("No")    
    elif x + z <= y:
        print("No")  
    elif y + z <= x:
        print("No")
    else: 
        print("Yes")   


# In[108]:


triangle(1,1,5)


# # Chapter 6 Exercise 2

# In[42]:


def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))
print(ackermann(3, 4))


# In[ ]:


#I think I copied in the solution that was given from the Excersice... Not sure what to do. ( I understand the problem though it's just showing the if this happens then return this type of thing.)


# In[111]:


def ack(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    return ack(m-1, ack(m,n-1))
print(ack(3,4))


# # Chapter 6 Exercise 5
# 

# In[55]:


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    


# In[60]:


gcd(50,15)


# # Chapter 10 Exercise 2

# In[76]:


def cumsum(t):
    mysum = 0
    new_list = []
    for i in t:
        mysum += i
        new_list.append(mysum)
    return new_list


# In[74]:


t=[1,2,3]


# In[75]:


cumsum(t)

