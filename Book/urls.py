from django.urls import path
from Book import views



urlpatterns = [
  path('',views.Login,name='Login'),
  path('Booking',views.Booking,name='Booking'),
  path('Register',views.Register,name='Register'),
  path('Home',views.Home,name='Home'),
  path('Booking_histroy',views.Booking_histroy,name='Booking_histroy'),
  path('payment_histroy',views.payment_histroy,name='payment_histroy'),
  path('pending_invoice',views.pending_invoice,name='pending_invoice'),
  path('vendor_home',views.vendor_home,name='vendor_home'),
  path('Product_Histroy',views.Product_Histroy,name='Product_Histroy'),
  path('Payment_Histroy',views.Payment_Histroy,name='Payment_Histroy'),
  path('Admin',views.Admin,name='Admin'),
  path('cust_Booking_histroy1',views.cust_Booking_histroy1,name='cust_Booking_histroy1'),
  path('cust_payment_histroy1',views.cust_payment_histroy1,name='cust_payment_histroy1'),
  path('cust_pending_invoice1',views.cust_pending_invoice1,name='cust_pending_invoice1'),
  path('vendor_home2',views.vendor_home2,name='vendor_home2'),
  path('vendor_Product_Histroy2',views.vendor_Product_Histroy2,name='vendor_Product_Histroy2'),
  path('vendor_Payment_Histroy2',views.vendor_Payment_Histroy2,name='vendor_Payment_Histroy2'),
  path('add_products',views.add_products,name='add_products'),
]