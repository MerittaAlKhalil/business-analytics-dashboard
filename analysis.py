import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('sales_data.csv')

# General settings
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Business Analytics Dashboard 2024', fontsize=18, fontweight='bold')

# 1. Revenue by product
revenue_by_product = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
axes[0, 0].bar(revenue_by_product.index, revenue_by_product.values, color='steelblue')
axes[0, 0].set_title('Revenue by Product')
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Total Revenue ($)')

# 2. Revenue by region
revenue_by_region = df.groupby('Region')['Revenue'].sum()
axes[0, 1].pie(revenue_by_region.values, labels=revenue_by_region.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Revenue by Region')

# 3. Monthly revenue trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly = df.groupby('Month')['Revenue'].sum().reindex(month_order)
axes[1, 0].plot(monthly.index, monthly.values, marker='o', color='green', linewidth=2)
axes[1, 0].set_title('Monthly Revenue Trend')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Revenue ($)')

# 4. Units sold by product
qty_by_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
axes[1, 1].barh(qty_by_product.index, qty_by_product.values, color='coral')
axes[1, 1].set_title('Units Sold by Product')
axes[1, 1].set_xlabel('Total Units')

plt.tight_layout()
plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Dashboard created successfully!")