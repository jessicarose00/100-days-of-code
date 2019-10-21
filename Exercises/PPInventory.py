#Petal Power Inventory: Data Analysis with Pandas
#credit: Codecademy (Data Science Career Path)

import pandas as pd

inventory = pd.read_csv('inventory.csv')
inventory.head(10)

# Create a table to store the inventory from the Staten Island location
staten_island = inventory.iloc[0:10]

# What products are sold at the Staten Island location?
product_request = staten_island['product_description']

# What types of seeds are sold at the Brooklyn location?
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# What's in stock?
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

# How valuable is our inventory?
inventory['total_value'] = inventory['price'] * inventory['quantity']

# Prepare full description for each product
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)
                