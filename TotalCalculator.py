import json
import csv
import os
import time
import shutil 

def get_bill_data(filename):
    #final code to get bill data from the billdetails
    filename_bills=('C:\\Users\\Kirthi\\OneDrive\\Desktop\\HelloWorld\\python\\Billing\\Billing\\bills\\'+filename)
    with open(filename_bills) as json_file:
        data = json.load(json_file)
    return data

def get_bill_details(data):
    #get only product_id and unit_price
    bill_data={}
    for i in data['BillDetails']:
        bill_data[i] = data['BillDetails'][i]
    #print(bill_data)
    return bill_data

def get_masterdata():
    #masterdata of price from store
    with open('C:\\Users\\Kirthi\\OneDrive\\Desktop\\HelloWorld\\python\\Billing\\Billing\\masterdata\\products.csv','r') as file:
        csv_data=csv.DictReader(file)
        product_price={}
        for i in csv_data:
            product_price[i['product_id']]=i['unit_price']
           #print(product_price)        
    return product_price

def calc_total(bill_data,product_price):
    #calculate total
    grand_total=0
    for i in bill_data:
        #print(i,"PP=",product_price[i],'qty',bill_data[i])
        try:
            pp=int(product_price[i])
        except:
            pp=float(product_price[i])

        total=pp*int(bill_data[i])
        #print("Total:",total)
        grand_total+=total
    print("Total:",grand_total)
    return grand_total
   
def move_files_to_processed(filename):
    # Source path 
    source = 'C:\\Users\\Kirthi\\OneDrive\\Desktop\\HelloWorld\\python\\Billing\\Billing\\bills\\'+filename
    # Destination path 
    destination = 'C:\\Users\\Kirthi\\OneDrive\\Desktop\\HelloWorld\\python\\Billing\\Billing\\processed\\'+filename
    shutil.move(source, destination) 

while True:                               
    path_to_json = 'C:\\Users\\Kirthi\\OneDrive\\Desktop\\HelloWorld\\python\\Billing\\Billing\\bills\\'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    if json_files:
        print(json_files[0])
        bill_data=get_bill_data(json_files[0])
        data=get_bill_details(bill_data)
        product_price=get_masterdata()
        grand_total=calc_total(data,product_price)
        entry={"Total":grand_total}
        data.update(entry)
        move_files_to_processed(json_files[0])
        #move_file(json_files[0],grand_total,data)
    else:
        print('Finished Processing..')    
        break
    time.sleep(2)









