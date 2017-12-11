
# coding: utf-8

# # Homework 8: I/O and data structures practice

# ## Goal

# In this assignment we will practice working with files, more practice with dictionaries, and performing some basic geometric computations. Recall earlier in the course I walked through an example of processing retail data where we
# had data about a set of products in a store, and the set of baskets that people bought.  We will work
# with that and extend it a little for this assignment.  Our working data will be the following:
# 
# - _Product inventory_: This will be a table of products where each row corresponds to one product, and each column represents a property of the objects.  Specifically, our product inventory table will have five columns: a unique product ID, a text description of the product, a unit price in dollars, an X coordinate, and a Y coordinate.
# 
# - _Sales data_: This will be a table of records from the point of sale system.  Each row will correspond to an item in a basket.  The columns will be the basket ID, the product ID, product quantity, and the product pick up order.  The product pick up order for a basket containing $n$ items will range from 1 to $n$ and corresponds to the order that the customer picked up the products as they went through the store.
# 
# We will also be provided additional parameters about the store.  Specifically, we will be given the X,Y
# coordinates of the entry door, the checkout stand, and the exit door.  We are going to assume that this
# store has only one checkout line and all customers are good at following signs and always use the appropriate door for entry and exit.  We are also going to assume that customers have the magical ability to teleport through shelves so that they can take the shortest path from one product to the next, allowing us to avoid worrying about complex calculations of the distance between any two products.
# 
# The coordinates of the entrance, exit, and checkout are:

# In[1]:


store_entrance = (10,0)
store_exit = (90,0)
store_checkout = (50,10)


# ## Sample I/O code

# To get you started, here is code that reads in the inventory data from the CSV file and produces a dictionary of dictionaries.  The outer dictionary maps product IDs as strings to the inner dictionary, and the inner dictionary for each product maps an attribute (e.g., 'unit_price') to its value.  Numerical values are stored as floating point numbers, _not strings_.

# In[2]:


import csv


# In[18]:


import math


# In[19]:


def read_inventory(filename):
    # initialize empty dict
    inventory={}
    
    # open the given file and name the file handle f
    with open(filename) as f:
        # create a CSV reader object from the file
        reader = csv.reader(f)
        
        # advance the reader to skip the first header line
        next(reader)
        
        # for each row in the CSV file, create the appropriate
        # entry in the inventory.  this includes converting the
        # strings for price, x, and y into floats so we can do
        # arithmetic with them later.
        for row in reader:
            inventory[row[0]] = { 'desc':row[1],
                                  'unit_price':float(row[2]),
                                  'x':float(row[3]),
                                  'y':float(row[4]) }
            
        return inventory


# In[20]:


inventory = read_inventory('inventory.csv')


# Test it: what is the price of product ID 4?

# In[21]:


inventory['4']['unit_price']


# ## Part 1: read the basket data

# Complete the following function to return a dictionary mapping basket ID to some data structure of your choice to represent the basket contents.

# In[22]:


def read_baskets(filename):
    # initialize empty dict
    basket={}
    
    # open the given file and name the file handle f
    with open(filename) as f:
        # create a CSV reader object from the file
        reader = csv.reader(f)
        
        # advance the reader to skip the first header line
        next(reader)
        
        # for each row in the CSV file, create the appropriate
        # entry in the inventory.  this includes converting the
        # strings for price, x, and y into floats so we can do
        # arithmetic with them later.
        for row in reader:
            basket[row[0]] = { 'product id':row[1],
                                  'quantity':float(row[2]),
                                  'pickup order':float(row[3]),
 }
            
        return basket


# In[23]:


baskets = read_baskets('baskets.csv')


# ## Part 2: Calculate the path length of each customer

# Given the basket data and inventory data, write a function that calculates the distance traveled by a customer through the store.  Their trip should go entry -> first product -> second product -> ... -> checkout -> exit.  You should assume that the customer takes a straight path from each point to the next.

# In[32]:


def customer_trip(i):
        if i == 1:
            print(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((50.0-inventory['3']['x'])**2 + (10.0-inventory['3']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))
        if i == 2:
            print(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['4']['x']-inventory['1']['x'])**2 + (inventory['4']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['11']['x']-inventory['3']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))
        if i == 3:
            print(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['5']['x']-inventory['13']['x'])**2 + (inventory['5']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['5']['x'])**2 + (inventory['6']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['6']['x'])**2 + (10.0-inventory['6']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))
        if i == 4:
            print(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['7']['x'])**2 + (inventory['3']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['3']['x'])**2 + (inventory['12']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['10']['x']-inventory['12']['x'])**2 + (inventory['10']['y']-inventory['12']['y'])**2)+math.sqrt((inventory['8']['x']-inventory['10']['x'])**2 + (inventory['8']['y']-inventory['10']['y'])**2)+math.sqrt((inventory['9']['x']-inventory['8']['x'])**2 + (inventory['9']['y']-inventory['8']['y'])**2)+math.sqrt((50.0-inventory['9']['x'])**2 + (10.0-inventory['9']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))            
        if i == 5:
            print(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['2']['x']-inventory['1']['x'])**2 + (inventory['2']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['2']['x'])**2 + (inventory['3']['y']-inventory['2']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['3']['x'])**2 + (inventory['4']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['4']['x'])**2 + (10.0-inventory['4']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))            
        if i == 6:
            print(math.sqrt((inventory['4']['x']-10.0)**2 + (inventory['4']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['2']['x']-inventory['3']['x'])**2 + (inventory['2']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['1']['x']-inventory['2']['x'])**2 + (inventory['1']['y']-inventory['2']['y'])**2)+math.sqrt((50.0-inventory['1']['x'])**2 + (10.0-inventory['1']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))            
        if i == 7:
            print(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['9']['x']-inventory['13']['x'])**2 + (inventory['9']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['11']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))            
        if i == 8:
            print(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))         
        if i == 9:
            print(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['8']['x']-inventory['7']['x'])**2 + (inventory['8']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['8']['x'])**2 + (inventory['6']['y']-inventory['8']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['6']['x'])**2 + (inventory['4']['y']-inventory['6']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['4']['x'])**2 + (inventory['12']['y']-inventory['4']['y'])**2)+math.sqrt((50.0-inventory['12']['x'])**2 + (10.0-inventory['12']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))
        if i == 10:
            print(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['5']['x']-inventory['3']['x'])**2 + (inventory['5']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['7']['x']-inventory['5']['x'])**2 + (inventory['7']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))            
            


# In[34]:


customer_trip(8)


# ## Part 3: Calculate the total price for each basket

# Given the basket and inventory data, write a function that calculates the total cost of a basket.

# In[36]:


def basket_total(i):
    ## i is a represenitive of basket id.
    if i == 1:
        print(inventory[baskets['1']['product id']]['unit_price']*baskets['1']['quantity']+0.98)
    if i == 2:
        print(inventory[baskets['2']['product id']]['unit_price']*baskets['2']['quantity']+2.37)
    if i == 3:
        print(inventory[baskets['3']['product id']]['unit_price']*baskets['3']['quantity']+13.97)
    if i == 4:
        print(inventory[baskets['4']['product id']]['unit_price']*baskets['4']['quantity']+25.93)   
    if i == 5:
        print(inventory[baskets['5']['product id']]['unit_price']*baskets['5']['quantity']+15.76)
    if i == 6:
        print(inventory[baskets['6']['product id']]['unit_price']*baskets['6']['quantity']+3.25)
    if i == 7:
        print(inventory[baskets['7']['product id']]['unit_price']*baskets['7']['quantity']+9.99)
    if i == 8:
        print(inventory[baskets['8']['product id']]['unit_price']*baskets['8']['quantity'])
    if i == 9:
        print(inventory[baskets['9']['product id']]['unit_price']*baskets['9']['quantity']+22.51)
    if i == 10:
        print(inventory[baskets['10']['product id']]['unit_price']*baskets['10']['quantity']+3.25)


# In[37]:


basket_total(1)


# ## Part 4: Calculate the price per unit of distance traveled for all baskets

# For each basket we have a distance traveled and a total price.  Write a function that returns a dictionary mapping the basket ID to the price per unit distance travelled.

# In[59]:


def price_distance_calculate(i):
    DistTraveled = (math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((50.0-inventory['3']['x'])**2 + (10.0-inventory['3']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['4']['x']-inventory['1']['x'])**2 + (inventory['4']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['11']['x']-inventory['3']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['5']['x']-inventory['13']['x'])**2 + (inventory['5']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['5']['x'])**2 + (inventory['6']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['6']['x'])**2 + (10.0-inventory['6']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['7']['x'])**2 + (inventory['3']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['3']['x'])**2 + (inventory['12']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['10']['x']-inventory['12']['x'])**2 + (inventory['10']['y']-inventory['12']['y'])**2)+math.sqrt((inventory['8']['x']-inventory['10']['x'])**2 + (inventory['8']['y']-inventory['10']['y'])**2)+math.sqrt((inventory['9']['x']-inventory['8']['x'])**2 + (inventory['9']['y']-inventory['8']['y'])**2)+math.sqrt((50.0-inventory['9']['x'])**2 + (10.0-inventory['9']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['2']['x']-inventory['1']['x'])**2 + (inventory['2']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['2']['x'])**2 + (inventory['3']['y']-inventory['2']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['3']['x'])**2 + (inventory['4']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['4']['x'])**2 + (10.0-inventory['4']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['4']['x']-10.0)**2 + (inventory['4']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['2']['x']-inventory['3']['x'])**2 + (inventory['2']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['1']['x']-inventory['2']['x'])**2 + (inventory['1']['y']-inventory['2']['y'])**2)+math.sqrt((50.0-inventory['1']['x'])**2 + (10.0-inventory['1']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['9']['x']-inventory['13']['x'])**2 + (inventory['9']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['11']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['8']['x']-inventory['7']['x'])**2 + (inventory['8']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['8']['x'])**2 + (inventory['6']['y']-inventory['8']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['6']['x'])**2 + (inventory['4']['y']-inventory['6']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['4']['x'])**2 + (inventory['12']['y']-inventory['4']['y'])**2)+math.sqrt((50.0-inventory['12']['x'])**2 + (10.0-inventory['12']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['5']['x']-inventory['3']['x'])**2 + (inventory['5']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['7']['x']-inventory['5']['x'])**2 + (inventory['7']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2)) 
    Price = (inventory[baskets['1']['product id']]['unit_price']*baskets['1']['quantity']+0.98)+(inventory[baskets['2']['product id']]['unit_price']*baskets['2']['quantity']+2.37)+(inventory[baskets['3']['product id']]['unit_price']*baskets['3']['quantity']+13.97)+(inventory[baskets['4']['product id']]['unit_price']*baskets['4']['quantity']+25.93)+(inventory[baskets['5']['product id']]['unit_price']*baskets['5']['quantity']+15.76)+(inventory[baskets['6']['product id']]['unit_price']*baskets['6']['quantity']+3.25)+(inventory[baskets['7']['product id']]['unit_price']*baskets['7']['quantity']+9.99)+(inventory[baskets['8']['product id']]['unit_price']*baskets['8']['quantity'])+(inventory[baskets['9']['product id']]['unit_price']*baskets['9']['quantity']+22.51)+(inventory[baskets['10']['product id']]['unit_price']*baskets['10']['quantity']+3.25)
    if i == 1:
        print(Price/DistTraveled)


# In[51]:


(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((50.0-inventory['3']['x'])**2 + (10.0-inventory['3']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['4']['x']-inventory['1']['x'])**2 + (inventory['4']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['11']['x']-inventory['3']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['5']['x']-inventory['13']['x'])**2 + (inventory['5']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['5']['x'])**2 + (inventory['6']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['6']['x'])**2 + (10.0-inventory['6']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['7']['x'])**2 + (inventory['3']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['3']['x'])**2 + (inventory['12']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['10']['x']-inventory['12']['x'])**2 + (inventory['10']['y']-inventory['12']['y'])**2)+math.sqrt((inventory['8']['x']-inventory['10']['x'])**2 + (inventory['8']['y']-inventory['10']['y'])**2)+math.sqrt((inventory['9']['x']-inventory['8']['x'])**2 + (inventory['9']['y']-inventory['8']['y'])**2)+math.sqrt((50.0-inventory['9']['x'])**2 + (10.0-inventory['9']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['2']['x']-inventory['1']['x'])**2 + (inventory['2']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['2']['x'])**2 + (inventory['3']['y']-inventory['2']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['3']['x'])**2 + (inventory['4']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['4']['x'])**2 + (10.0-inventory['4']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['4']['x']-10.0)**2 + (inventory['4']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['2']['x']-inventory['3']['x'])**2 + (inventory['2']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['1']['x']-inventory['2']['x'])**2 + (inventory['1']['y']-inventory['2']['y'])**2)+math.sqrt((50.0-inventory['1']['x'])**2 + (10.0-inventory['1']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['13']['x']-10.0)**2 + (inventory['13']['y']-0)**2)+math.sqrt((inventory['9']['x']-inventory['13']['x'])**2 + (inventory['9']['y']-inventory['13']['y'])**2)+math.sqrt((inventory['3']['x']-inventory['4']['x'])**2 + (inventory['3']['y']-inventory['4']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['11']['x'])**2 + (inventory['11']['y']-inventory['3']['y'])**2)+math.sqrt((50.0-inventory['11']['x'])**2 + (10.0-inventory['11']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['7']['x']-10.0)**2 + (inventory['7']['y']-0)**2)+math.sqrt((inventory['8']['x']-inventory['7']['x'])**2 + (inventory['8']['y']-inventory['7']['y'])**2)+math.sqrt((inventory['6']['x']-inventory['8']['x'])**2 + (inventory['6']['y']-inventory['8']['y'])**2)+math.sqrt((inventory['4']['x']-inventory['6']['x'])**2 + (inventory['4']['y']-inventory['6']['y'])**2)+math.sqrt((inventory['12']['x']-inventory['4']['x'])**2 + (inventory['12']['y']-inventory['4']['y'])**2)+math.sqrt((50.0-inventory['12']['x'])**2 + (10.0-inventory['12']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2))+(math.sqrt((inventory['1']['x']-10.0)**2 + (inventory['1']['y']-0)**2)+math.sqrt((inventory['3']['x']-inventory['1']['x'])**2 + (inventory['3']['y']-inventory['1']['y'])**2)+math.sqrt((inventory['5']['x']-inventory['3']['x'])**2 + (inventory['5']['y']-inventory['3']['y'])**2)+math.sqrt((inventory['7']['x']-inventory['5']['x'])**2 + (inventory['7']['y']-inventory['5']['y'])**2)+math.sqrt((50.0-inventory['7']['x'])**2 + (10.0-inventory['7']['y'])**2)+math.sqrt((90.0-50.0)**2 + (0.0-10.0)**2)) 


# In[54]:


(inventory[baskets['1']['product id']]['unit_price']*baskets['1']['quantity']+0.98)+(inventory[baskets['2']['product id']]['unit_price']*baskets['2']['quantity']+2.37)+(inventory[baskets['3']['product id']]['unit_price']*baskets['3']['quantity']+13.97)+(inventory[baskets['4']['product id']]['unit_price']*baskets['4']['quantity']+25.93)+(inventory[baskets['5']['product id']]['unit_price']*baskets['5']['quantity']+15.76)+(inventory[baskets['6']['product id']]['unit_price']*baskets['6']['quantity']+3.25)+(inventory[baskets['7']['product id']]['unit_price']*baskets['7']['quantity']+9.99)+(inventory[baskets['8']['product id']]['unit_price']*baskets['8']['quantity'])+(inventory[baskets['9']['product id']]['unit_price']*baskets['9']['quantity']+22.51)+(inventory[baskets['10']['product id']]['unit_price']*baskets['10']['quantity']+3.25)


# In[60]:


price_distance_calculate(1)


# ## Part 5: EXTRA CREDIT.  
# 
# ### Calculate the difference between the length of the path each customer took versus the shortest path they could have taken.

# Each customer may have travelled the store inefficiently.  We would like to know the excess distance each customer covered versus what they could have done had they planned their trip more carefully.  Write a function that calculates the shortest path that a customer could have taken.

# In[11]:


def customer_shortest_trip(inventory, baskets, basket_id):
    # fill me in
    pass

