# Python Coding Challenge

## PRODUCT PRICE UPDATE SCRIPT

This python script reads csv files (products.csv, sales.csv) and analyzes the stock and quantity sold details, to generate new prices for the products based on the conditions applied.
The new price which is calculated is then added to the "updated_prices.csv" file, along with the product's "sku" and "current price" values.

### Pricing Logic
The new price is determined using the following rules:

1. High Demand & Low Stock -->
If stock < 20 and quantity_sold > 30, increase price by 15%.

2. Excess Stock & No Sales -->
If stock > 200 and quantity_sold == 0, reduce price by 30%.

3. Moderate Stock & Low Sales -->
If stock > 100 and quantity_sold < 20, reduce price by 10%.

4. Minimum Price Check -->
After calculation, the new price is adjusted to ensure it's at least 120% of the product's cost price.

### Steps involved

<img src="https://github.com/user-attachments/assets/f3e23249-1349-4525-afcf-82e4d380b14b" alt="Icon" width="28"/> 1. import csv module
