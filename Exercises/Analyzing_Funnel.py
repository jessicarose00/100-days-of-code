#Page Visits Funnel: Data Analysis with Pandas
#credit: Codecademy (Data Science Career Path)

# Visits lists all users who have visited the website
visits = pd.read_csv('visits.csv', parse_dates=[1])

# Cart lists all users who have added a t-shirt to their cart
cart = pd.read_csv('cart.csv', parse_dates=[1])

# Checkout lists all users who have started the checkout
checkout = pd.read_csv('checkout.csv', parse_dates=[1])

# Purchase lists all the users who have purchased a t-shirt
purchase = pd.read_csv('purchase.csv', parse_dates=[1])


# Inspect the dataframes
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Merge data on visits and cart
visit_to_cart = pd.merge(visits, cart, how='left')

# How many rows are in the new dataframe? (2052 rows)
total_visits = len(visit_to_cart)
print(total_visits)

# How many timestamps are null in the cart column? (1652 rows)
null_cart_time = len(visit_to_cart[visit_to_cart.cart_time.isnull()])
print(null_cart_time)

# What percentage of users who visited the site did not place a t-shirt in the cart? (80.5%)
viewing_only = float(null_cart_time) / total_visits * 100
print(viewing_only)

# Merge data on cart and checkout
cart_to_checkout = pd.merge(cart, checkout, how='left')

# How many rows are in the new dataframe? (602 rows)
total_cart = len(cart_to_checkout)
print(total_cart)

# How many timestamps are null in the checkout column? (126 rows)
null_checkout = len(cart_to_checkout[cart_to_checkout.checkout_time.isnull()])
print(null_checkout)

#What percentage of users put items in their cart but didn't proceed to checkout? (20.9%)
cart_only = float(null_checkout) / total_cart * 100
print(cart_only)

# Merge all four steps of the funnel in order
all_data = visit_to_cart.merge( cart_to_checkout, how='left').merge(purchase, how='left')
print(all_data.head())

# How many rows in the new dataframe? (2614 rows)
total_checkout = len(all_data)
print(total_checkout)

# How many timestamps are null in the purchased column? (1898 rows)
null_purchase = len(all_data[all_data.purchase_time.isnull()])
print(null_purchase)

# What percentage of users proceeded to checkout, but did not purchase a shirt? (72.6%)
checkout_only = float(null_purchase) / total_checkout * 100
print(checkout_only)

# Calculate average time on site, from inital visit to final purchase (approx 00:44:12.99)
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase.mean())

