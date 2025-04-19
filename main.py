import csv

# open products, sales csv file in read mode
products = csv.DictReader(open('products.csv','r'))
sales = csv.DictReader(open('sales.csv','r'))

# create and open updated_prices csv file in write mode
updatedPrices = csv.writer(open("updated_prices.csv",'w',newline=''))
fieldNames = ['sku','old_price','new_price']
updatedPrices.writerow(fieldNames)

# function to check if new price is atleast 120% of cost price
def checkNewPrice(costPrice: float, newPrice: float) -> float:    
  return max(newPrice, costPrice*1.2)

# function to write datas to updated_price csv file
def writeFile(sku:str, currentPrice:float, newPrice:float):
    currentPrice="{:.2f}".format(currentPrice)
    newPrice="{:.2f}".format(newPrice)
    
    subList = [sku,currentPrice,newPrice]
    updatedPrices.writerow(subList)

# function to calculate new price
def getNewPrice(stock:int,quantitySold:int,currentPrice:float) -> float:
    if product["stock"] < '20' and sale["quantity_sold"] > '30':
        newPrice = currentPrice*1.15                        
        
    elif product["stock"] > '200' and sale["quantity_sold"] == '0':
        newPrice = currentPrice*0.70           
                    
    elif product["stock"] > '100' and sale["quantity_sold"] < '20':
        newPrice = currentPrice*0.90 
     
    newPrice = checkNewPrice(costPrice,newPrice)    
    return newPrice                      
                
    
# iterate through datas to check condition and calculate new price
for product, sale in zip(products, sales):
    if product["sku"] == sale["sku"]:
        
        stock, quantitySold = int(product["stock"]),int(sale["quantity_sold"])
        currentPrice, costPrice = float(product["current_price"]),float(product["cost_price"])
        
        newPrice = getNewPrice(stock,quantitySold,currentPrice)
        writeFile(product["sku"],currentPrice,newPrice)            


    
        
    