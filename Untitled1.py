#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


products = pd.read_csv('products.csv')
sales = pd.read_csv('sales.csv')


# In[3]:


df = pd.merge(products,sales,on='sku')


# In[4]:


def calculate(record):
    price = record['current_price']
    cost = record['cost_price']
    stock = record['stock']
    sold = record['quantity_sold']
    
    if stock <20 and sold >30:
        price*= 1.15
    elif stock >200 and sold == 0:
        price*= 0.70
    elif stock >100 and sold <20:
        price*= 0.90
    
    below_price = cost*1.2
    if price< below_price:
        price = below_price
    return round(price,2)

df['new_price'] = df.apply(calculate,axis=1)
units = lambda x:f"{x:.2f} INR"
df['old_price'] = df['current_price'].apply(units)
df['new_price'] = df['new_price'].apply(units)

result = df[['sku','old_price','new_price']]
result.to_csv('updated_prices.csv',index=False)
    


# In[ ]:




