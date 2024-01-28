from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
from .models import Warehouse, Dailysheet, Brands, Dailysales, Bills
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request,'index.html')
def regemp(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        username=request.POST['username']
        password=request.POST['password']     
        email=request.POST['email']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
          
        mycursor.execute("insert into employee (username,password,email,mobile,dob) values('"+username+"','"+password+"','"+email+"','"+mobile+"','"+dob+"')")
        conn.commit()
        return redirect('regemp')
    elif "username" in request.session:
        
        username=request.session['username']
    
        return render(request,'regemp.html')
    else:
         return render(request,'adminlogin.html')
        
def regacc(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        username=request.POST['username']
        password=request.POST['password']     
        email=request.POST['email']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
          
        mycursor.execute("insert into accountant (username,password,email,mobile,dob) values('"+username+"','"+password+"','"+email+"','"+mobile+"','"+dob+"')")
        conn.commit()
        return redirect('regacc')
    elif "username" in request.session:
        
        username=request.session['username']
    
        return render(request,'regacc.html')
    else:
         return render(request,'adminlogin.html')
        
def adminlogin(request):

    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        username=request.POST['username']
        password=request.POST['password']     
           
        mycursor.execute("select * from admin where username='"+username+"' and password='"+password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session["username"]=username
            return render(request, 'admindashboard.html')
        else:
            return render(request,'adminlogin.html')  
    else:
        return render(request,'adminlogin.html')
    
    
def logout(request):
    try:
        del request.session['username']
        request.session.modified= True
        return render(request,'adminlogin.html')
    except KeyError:
        return redirect('adminlogin')

  
def emplogin(request):

    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        username=request.POST['username']
        password=request.POST['password']     
           
        mycursor.execute("select * from employee where username='"+username+"' and password='"+password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session["username"]=username
            return render(request, 'empdashboard.html')
            
        else:
            return render(request,'emplogin.html')  
    else:
        return render(request,'emplogin.html') 

def acclogin(request):

    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        username=request.POST['username']
        password=request.POST['password']     
           
        mycursor.execute("select * from accountant where username='"+username+"' and password='"+password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            return render(request, 'accdashboard.html', {"username" : username})
        else:
            return render(request,'acclogin.html',{'status':'invalid credentials'})  
    else:
        return render(request,'acclogin.html')   

def about(request):
    return render(request,"about.html")

def pricing(request):
    return render(request,"pricing.html")

def employee(request):
    return render(request,"employee.html")

def contact(request):
    return render(request,"contact.html")

def admindashboard(request):
    if "username" in request.session:
        username=request.session['username']
        return render(request, "admindashboard.html")
    else:
        return render(request,'adminlogin.html')

def empdashboard(request):
    return render(request, "empdashboard.html")

def accdashboard(request):
    return render(request, "accdashboard.html")




def brandsandpriceadmin(request):
    if request.method=='POST':
        conn= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='inventorymanagement'
    )
    elif "username" in request.session:
        
        username=request.session['username']
    
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from brands")
        result = mycursor.fetchall()
        b=[] 
        for row in result:
            obj=Brands()
            obj.bid=row[0]
            obj.brand_no=row[1] 
            obj.brand_name = row[2]
            obj.ML = row[3]
            obj.issue_price= row[4]
            obj.MRP= row[5]
            b.append(obj)
        return render(request, 'brandsandpriceadmin.html', {'brands': b})
    else:
         return render(request,'adminlogin.html')
        
    
    
def brandsandpriceemp(request):
    if request.method=='POST':
        conn= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='inventorymanagement'
    )
    else:
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from brands")
        result = mycursor.fetchall()
        b=[] 
        for row in result:
            obj=Brands()
            obj.bid=row[0]
            obj.brand_no=row[1] 
            obj.brand_name = row[2]
            obj.ML = row[3]
            obj.issue_price= row[4]
            obj.MRP= row[5]
            b.append(obj)
        return render(request, 'brandsandpriceemp.html', {'brands': b})
            
            

def challanandbills(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
    )
    mycursor=conn.cursor()
    mycursor.execute("select * from challan_details")
    result=mycursor.fetchall()
    files=[]
    for x in result:
        f=Bills()
        f.cid=x[0]
        f.date=x[1]
        f.bill=x[2]   
        files.append(f) 
    return render(request,'challanandbills.html',{"files":files})
  
def load(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorymanagement"
    )
    mycursor = mydb.cursor()
    #retrive post details       
    mycursor.execute("select * from  challan_details")
    result=mycursor.fetchall()
    files=[]
    for x in result:
        f=Bills()
        f.name=x[0]      
        files.append(f)    
    return render(request,'load.html',{"files":files})
   

 
def others(request):
    return render(request, "others.html")

def members(request):
    return render(request, "members.html")
 
def addsheet(request):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        date=request.POST['date']
        bname=request.POST['brandname']
        ml=request.POST['ml']
        ob=request.POST['Openingbal']
        Plant=request.POST['plant']
        total=request.POST['total']
        cb=request.POST['Closingbal']
        sales=request.POST['sale']
        mrp=request.POST['rate']
        amt=request.POST['amount']
        query.execute("insert into daily_sheet (date,brand_name,ML,Opening_bal, plant, ob_total, Closing_bal, sales, MRP, amount)  values('"+date+"','"+bname+"','"+ml+"','"+ob+"','"+Plant+"','"+total+"','"+cb+"','"+sales+"','"+mrp+"', '"+amt+"') ")
        conn.commit()
        return redirect('dailysheetemp')
    else:
        return render(request, 'addsheet.html')

def addbrands(request):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        bn=request.POST['brandnumber']
        bname=request.POST['brandname']
        ml=request.POST['ML']
        price=request.POST['issue_price']
        mrp=request.POST['MRP']
        
        query.execute("insert into brands (brand_no,brand_name,ML,issue_price,MRP)  values('"+bn+"', '"+bname+"','"+ml+"','"+price+"','"+mrp+"') ")

        conn.commit()
        return redirect('brandsandpriceadmin')
    else:
        return render(request, 'addbrands.html')
        
     

def stockmanagementemp(request):
    if request.method=='POST':
        conn= mysql.connector.connect(
        host='localhost',
        user='root',
            password='',
            database='inventorymanagement'
    )
    
    else:
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from warehouse")
        result = mycursor.fetchall()
        w=[] 
        for row in result:
            obj=Warehouse()
            obj.w_id=row[0]
            obj.brand_no=row[1] 
            obj.brand_name = row[2]
            obj.size = row[3]
            obj.quantity_boxes= row[4]
            obj.quantity_bottles= row[5]
            w.append(obj)
        #print(e)
        
        return render(request, 'stockmanagementemp.html', {'warehouse': w})
#else:
    #return render(request, 'adminapp/stockmanagement.html')


def stockmanagementadmin(request):
    
    
    if "username" in request.session:
        username=request.session['username']
    
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from warehouse")
        result = mycursor.fetchall()
        w=[] 
        for row in result:
            obj=Warehouse()
            obj.w_id=row[0]
            obj.brand_no=row[1] 
            obj.brand_name = row[2]
            obj.size = row[3]
            obj.quantity_boxes= row[4]
            obj.quantity_bottles= row[5]
            w.append(obj)
        #print(e)
        
        return render(request, 'stockmanagementadmin.html', {'warehouse': w})
    else:
        return render(request,'adminlogin.html')

def addstock(request):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        brandno=request.POST['brandnumber']
        brandname=request.POST['brandname']
        size=request.POST['size']
        bottles=request.POST['quantityinbottles']
        boxes=request.POST['quantityincases']
        query.execute("insert into warehouse (brand_no,brand_name,size,quantity_boxes,quantity_bottles)  values('"+brandno+"', '"+brandname+"','"+size+"','"+boxes+"','"+bottles+"') ")
        conn.commit()
        return redirect('stockmanagementemp')
    else:
        return render(request, 'addstock.html')
      

   
def editstock(request,w_id):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        brandnumber = request.POST['brandnumber']
        brandname = request.POST['brandname']
        brandsize = request.POST['size']
        quantity_boxes = request.POST['quantityincases']
        quantity_bottles = request.POST['quantityinbottles']
        
        
        query.execute("update warehouse set brand_no ='"+brandnumber+"',brand_name='"+brandname+"',size='"+brandsize+"',quantity_boxes='"+quantity_boxes+"',quantity_bottles='"+quantity_bottles+"'  where w_id='"+w_id+"'")
        conn.commit()
        return redirect(stockmanagementemp)
    else:
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from warehouse where w_id='"+w_id+"'")
        result = mycursor.fetchall()
        w=[] 
        for row in result:
            obj= Warehouse()
            obj.w_id=row[0]
            obj.brand_no=row[1] 
            obj.brand_name= row[2]
            obj.size = row[3]
            obj.quantity_boxes	= row[4]
            obj.quantity_bottles= row[5]  
            w.append(obj)
        #print(e)
        
        return render(request, 'editstock.html', {'ware': w})
        #return render(request,'editstock.html',{'status': ' Editing failed.'}) 
        
def editbrands(request,bid):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        
        brn = request.POST['brandnumber']
        brandname = request.POST['brandname']
        ml = request.POST['ML']
        price = request.POST['issue_price']
        mrp = request.POST['MRP']
        
        
        query.execute("update brands set brand_no ='"+brn+"',brand_name='"+brandname+"',ML='"+ml+"',issue_price='"+price+"',MRP='"+mrp+"'  where bid='"+bid+"'")
        conn.commit()
        return redirect('brandsandpriceadmin')
    else:
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from brands where bid='"+bid+"'")
        result = mycursor.fetchall()
        b=[] 
        for row in result:
            obj= Brands()
            obj.bid=row[0]
            obj.brand_no=row[1] 
            obj.brand_name= row[2]
            obj.ML = row[3]
            obj.issue_price	= row[4]
            obj.MRP= row[5]  
            b.append(obj)
        #print(e)
        
        return render(request, 'editbrands.html', {'brand': b})
    
def dailysheetemp(request):
    if request.method=='POST':
        conn= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='inventorymanagement'
        )
        query = conn.cursor()
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']
       
        rsale=request.POST['R_Sale']
        exp=request.POST['Exp']
        bal=request.POST['Bal']
        cashob=request.POST['cashob']
        total=request.POST['total']
        recash=request.POST['recash']
        cash=request.POST['cash']
      
        query.execute("insert into dailysales (date,retail_sale,expenditure,balance,cashob, total, recash,handcash)  values('"+fromdate+"', '"+rsale+"','"+exp+"','"+bal+"','"+cashob+"', '"+total+"', '"+recash+"', '"+cash+"') ")

        conn.commit()
        return redirect('dailysheetemp')
         
    else:
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from daily_sheet")
        result = mycursor.fetchall()
        d=[]
        R_sale=0 
        for row in result:
            obj= Dailysheet()
            obj.date=row[1] 
            obj.brand_name	 = row[2]
            obj.ML = row[3]
            obj.Opening_bal	= row[4]
            obj.plant= row[5]
            obj.ob_total= row[6]
            obj.Closing_bal	= row[7]
            obj.sales= row[8]
            obj.MRP= row[9]
            obj.amount= row[10] 
            R_sale=R_sale+int(obj.amount)
            
            d.append(obj)
        #print(e)
        
        return render(request, 'dailysheetemp.html', {'dailysheet': d, 'Rsale' : R_sale })
 
 
def dailysheetadmin(request):
    
    
    if "username" in request.session:
        username=request.session['username']
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from daily_sheet")
        result = mycursor.fetchall()
        d=[] 
        R_sale=0
        for row in result:
            obj= Dailysheet()
            obj.d_id=row[0]
            obj.date=row[1]
            obj.brand_name	 = row[2]
            obj.ML = row[3]
            obj.Opening_bal	= row[4]
            obj.plant= row[5]
            obj.ob_total= row[6]
            obj.Closing_bal	= row[7]
            obj.sales= row[8]
            obj.MRP= row[9]
            obj.amount= row[10]
            R_sale=R_sale+int(obj.amount)  
          
            d.append(obj)
        #print(e)
        
        return render(request, 'dailysheetadmin.html', {'dailysheet': d, 'Rsale' : R_sale})
    else:
        return render(request,'adminlogin.html')
    
def deletestock(request , brand_no):
    if request.method=='POST':
        obj.delete()
        return render(request,"stockmanagementemp.html")
    
def deletesheet(request , brand_name):
    if request.method=='POST':
        obj.delete()
        return render(request,"dailysheet.html")

def editsheet(request,d_id):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        query = conn.cursor()
        did= request.POST['d_id']
        date = request.POST['date']
        brandname = request.POST['brand_name']
        ml = request.POST['ML']
        O.B	 = request.POST['Opening_bal']
        plant = request.POST['plant']
        Total = request.POST['ob_total']
        C.B	 = request.POST['Closing_bal']
        Sale = request.POST['sales']
        Rate = request.POST['MRP']
        Amount = request.POST['amount']
         
        query.execute("update daily_sheet set brand_name='"+brandname+"',ML='"+ml+"',Opening_bal='"+O.B+"',plant='"+plant+"', ob_total='"+Total+"',Closing_bal='"+C.B+"',sales='"+Sale+"',MRP='"+Rate+"',amount='"+Amount+"'  where d_id='"+did+"'")
        conn.commit()
        return render(request, 'editsheet.html',{'status': ' Edited successfully.'})
    else:
            
        conn= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='inventorymanagement'
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from daily_sheet where d_id='"+d_id+"'")
        result = mycursor.fetchall()
        s=[] 
        for row in result:
            obj= Dailysheet()
            obj.date=row[1] 
            obj.brand_name= row[2]
            obj.ML = row[3]
            obj.Opening_bal	= row[4]
            obj.Plant= row[5]  
            obj.ob_total= row[6]  
            obj.Closing_bal= row[7]  
            obj.sales= row[8]  
            obj.MRP= row[9]  
            obj.amount= row[10]  
            s.append(obj)
        #print(e)
        
        return render(request, 'editsheet.html', {'sheet': s})
    
def deletebrands(request):  
    return render(request, 'brandsandpriceadmin.html')

def addfiles(request):
    if request.method=='POST' and request.FILES['myfile']:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'inventorymanagement'
        )
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        date=request.POST['date']
        query = conn.cursor()
        query.execute("insert into challan_details(date,bill,fileurl) values('"+date+"', '"+filename+"','"+uploaded_file_url+"')")
        conn.commit()
        return redirect('challanandbills')
    else:
        return render(request, 'addfiles.html')
             
        
       


    
  
    














    


