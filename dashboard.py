import pandas as pd
import random
from datetime import datetime, timedelta

# توليد بيانات مبيعات وهمية
products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Smartwatch']
regions = ['North', 'South', 'East', 'West']

data = []
start_date = datetime(2024, 1, 1)

for i in range(200):
    date = start_date + timedelta(days=random.randint(0, 364))
    product = random.choice(products)
    region = random.choice(regions)
    quantity = random.randint(1, 20)
    price = {'Laptop': 1200, 'Phone': 800, 'Tablet': 500, 'Headphones': 150, 'Smartwatch': 300}[product]
    revenue = quantity * price

    data.append({
        'Date': date.strftime('%Y-%m-%d'),
        'Product': product,
        'Region': region,
        'Quantity': quantity,
        'Price': price,
        'Revenue': revenue
    })

df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("✅ Data created successfully!")
print(df.head())