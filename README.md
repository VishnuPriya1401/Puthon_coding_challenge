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
 
1. import csv module
2. Open "products.csv" and "sales.csv" files in read mode using variable products, sales
3. Create "updated_prices.csv", open it in write mode.
4. Add column headers using "fieldNames" list datas
5. Using for loop iterate thourgh the datas and check if the "product["sku"] == sales["sku"]
6. If matched, "getNewPrice()" function is called, which takes product details like "stock","quantity sold" and "current price" as arguments to calculate new price
7. Then the calculated price is checked if it is atleast 120% of the product's cost price, if not, the new price value id changed to 120% of the product'c cost price using "checkNewPrice()"
8. Finally "writeFile()" function is called to write the updated "new price", along with the "product's sku" and "old price" into the "updated_prices.csv" file
