from django.db import models

# Create your models here.



class Warehouse: 
    w_id: str 
    brand_no : str
    brand_name : str
    size : str
    quantity_boxes : str 
    quantity_bottles : str
    
class Dailysheet:
    d_id :str
    date: str
    brand_name: str
    ML: str
    Opening_bal	: str
    plant: str
    ob_total: str
    Closing_bal	:str
    sales: str
    MRP: str
    amount: str

    
class Brands:
    bid : int
    brand_no : str
    brand_name : str
    ML:str
    issue_price:str
    MRP:str
    
class Dailysales:
    date : str
    retail_sale : str
    expenditure : str
    balance : str
    cashob : str
    total : str
    recash : str
    handcash : str
    
class Bills:
    cid :str
    date : str
    bill : str

    
    
    
    
            
    
    

