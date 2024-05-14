from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def Login(requset):
    
    return render(requset,'Login.html')


def Booking(requset):
    
    return render(requset,'Booking.html')

def Register(requset):
    
    return render(requset,'Register.html')


def Home(requset):
    
    return render(requset,'Home.html')

def payment_histroy(request):
    return render(request,'customer/cust_payment_histroy.html')

def pending_invoice(request):
    return render(request,'customer/cust_pending_invoice.html')

def Booking_histroy(request):
    return render(request,'customer/cust_Booking_histroy.html')

def vendor_home(request):
    return render(request,'vendor/vendor_home.html')


def Product_Histroy(request):
    return render(request,'vendor/vendor_Product_Histroy.html')

def Payment_Histroy(request):
    return render(request,'vendor/vendor_Payment_Histroy.html')

def Admin(request):
    return render(request,'Admin/Admin.html')

def cust_Booking_histroy1(request):
    return render(request,'Admin/customers/cust_Booking_histroy1.html')

def cust_payment_histroy1(request):
    return render(request,'Admin/customers/cust_payment_histroy1.html')

def cust_pending_invoice1(request):
    return render(request,'Admin/customers/cust_pending_invoice1.html')

def vendor_home2(request):
    return render(request,'Admin/vendors/vendor_home2.html')

def vendor_Product_Histroy2(request):
    return render(request,'Admin/vendors/vendor_Product_Histroy2.html')

def vendor_Payment_Histroy2(request):
    return render(request,'Admin/vendors/vendor_Payment_Histroy2.html')


def add_products(request):
    return render(request,'Admin/add_products.html')