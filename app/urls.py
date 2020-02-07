from django.urls import path
from . import views_user, views_staff
urlpatterns = [
    path('',views_user.index,name='home'),
    path('signup',views_user.signup,name='signup'),
    path('login',views_user.login),
    path('comic',views_user.comic,name='comic'),
    path('comic2',views_user.comic2,name='comic2'),
    path('about',views_user.about,name='about'),
    path('media',views_user.media,name='media'),
    path('media1',views_user.media1,name='media1'),
    path('media2',views_user.media2,name='media2'),
    path('buy',views_user.buy,name='buy'),
    path('product/<int:id>/', views_user.productDetail, name='productDetail'),
    path('add_to_cart/', views_user.addToCart, name='addToCart'),
    path('view_cart/', views_user.viewCart, name='viewCart'),
    path('payment_info/', views_user.paymentInfo, name='paymentInfo'),
    path('update_cart_item/', views_user.updateCartItem, name='updateCartItem'),
    path('delete_cart_item/', views_user.deleteCartItem, name='deleteCartItem'),
    path('clear_cart/', views_user.clearCart, name='clearCart'),
    path('confirm_payment/', views_user.confirmPayment, name='confirmPayment'),
    path('thankyou/', views_user.thankYou, name='thankYou'),
    path('spiderman/', views_user.spiderman, name='spiderman'),
    path('thor/', views_user.thor, name='thor'),
    path('daredevil/', views_user.daredevil, name='daredevil'),
    path('ironman/', views_user.ironman, name='ironman'),
    path('doctor/', views_user.doctor, name='doctor'),
    path('hulk/', views_user.hulk, name='hulk'),
    path('inf1/', views_user.inf1, name='inf1'),
    path('inf2/', views_user.inf2, name='inf2'),
    path('base1/', views_user.base1),







    path('staff/', views_staff.listProduct, name='listProduct'),
    path('staff/add_product/', views_staff.addProduct, name='addProduct'),
    path('staff/edit_product/<int:id>/', views_staff.editProduct, name='editProduct'),
    path('staff/delete_product/<int:id>/', views_staff.deleteProduct, name='deleteProduct'),


]