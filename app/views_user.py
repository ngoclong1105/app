from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Media1,Spiderman,Ironman,Thor,Daredevil,Doctor,Inf1,Hulk,Inf2,Comment
from django.contrib.auth import login,authenticate
from time import time
from . import db
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comic
from .forms import PaymentForm
import smtplib, ssl
from email.mime.text import MIMEText

# Create your views here.
def login(request):
    if request.POST:            
        username=request.POST.get("username")
        password = request.POST.get("password")                     
        user = UniversityDetails.objects.filter(username=username,password=password)          
        if(not user):
            return render(request,"registration/login.html") 
        else:
            return render(request,"home")

def index(request):
    return render(request, 'user/index.html')
def media(request):
    return render(request, 'user/media.html')
def comic(request):
        return render(request,'user/comic.html')
def about(request):
        return render(request,'user/about.html')
def media1(request):
        return render(request,'user/media1.html', {'images' : Media1.objects.all()})
def media2(request):
        return render(request,'user/media2.html')

def signup(request):
    form=CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            password=form.cleaned_data['password1']
            CustomUser.objects.create(username=username,email=email,password=make_password(password),mobile=mobile)
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')

    return render(request,'registration/signup.html',{'form':form})



def buy(request):
    keyword = request.GET.get('keyword', '')
    products = db.getProducts(keyword)
    return render(request, 'user/buy.html', {'products' : products, 'keyword' : keyword})

def productDetail(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('buy'))
    product = get_object_or_404(Comic, pk=id)
    return render(request, 'user/buy1.html', {'product' : product, 'backURL' : backURL})

def findItem(cart, productId):
    for item in cart:
        if item['id'] == productId:
            return item

def getTotal(cart):
    return int(sum([x['qty'] * x['unitPrice'] for x in cart]))

def addToCart(request):
    productId = int(request.GET['productId'])    
    qty = int(request.GET['qty'])

    product = get_object_or_404(Comic, pk=productId)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    item = findItem(cart, productId)

    if item:
        item['qty'] += qty
        item['total'] = int(item['qty'] * item['unitPrice'])
    else:
        cart.append({
                    'id' : productId, 
                    'name': product.name,
                    'url': product.imageURL,
                    'unitPrice': product.unitPrice, 
                    'qty' : qty,
                    'total': int(qty * product.unitPrice)
                })

    request.session['cartTotal'] = getTotal(cart)

    return redirect(request.GET.get('back_url', reverse_lazy('buy')))

def viewCart(request):
    return render(request, 'user/view_cart.html')

def paymentInfo(request):
        form = PaymentForm()

        if request.method == 'POST':
                form = PaymentForm(request.POST)
                if form.is_valid():
                        fields = ('fullname', 'mobile', 'email', 'address')
                        paymentInfo = {field : form.cleaned_data[field] for field in fields }
                        request.session['paymentInfo'] = paymentInfo
                        return redirect('confirmPayment')
        return render(request, 'user/payment_info.html', {'form' : form})

def updateCartItem(request):
    productId = int(request.GET['productId'])
    qty = int(request.GET['qty'])

    if 'cart' in request.session:
        cart = request.session['cart']
        item = findItem(cart, productId)
        if item:
            item['qty'] = qty
            item['total'] = int(qty * item['unitPrice'])
        
        request.session['cart'] = cart
        request.session['cartTotal'] = getTotal(cart)

    return HttpResponse("OK")

def deleteCartItem(request):
    productId = int(request.GET['productId'])

    if 'cart' in request.session:
        cart = request.session['cart']
        item = findItem(cart, productId)
        
        if item:
            cart.remove(item)

        if len(cart) > 0:
            request.session['cart'] = cart
            request.session['cartTotal'] = getTotal(cart)
        else:
            del request.session['cart']
            del request.session['cartTotal']

    return HttpResponse("OK")

def clearCart(request):
    del request.session['cartTotal']
    del request.session['cart']
    return redirect('buy')
      

    return render(request, 'user/payment_info.html', {'form' : form})

def confirmPayment(request):
    return render(request, 'user/confirm_payment.html')

def thankYou(request):
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender = 'bighead19980@gmail.com'
    receiver = 'bighead19980@gmail.com'
    password = 'bighead123'
    cart = str(request.session['cart'])
    paymentInfo = str(request.session['paymentInfo'])
    message = cart + paymentInfo
    msg = MIMEText(message)
    msg['Subject'] = 'Thong bao dang ki mua hang'
    msg['From'] = 'Web abc'
    msg['To'] =' Nguyen van a'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    del request.session['cart']
    del request.session['cartTotal']
    del request.session['paymentInfo']
    return render(request, 'user/thankyou.html')

def spiderman(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/spiderman.html',{'images' : Spiderman.objects.all(),'comment':Comment.objects.all()})

def ironman(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/ironman.html',{'images' : Ironman.objects.all(),'comment':Comment.objects.all()})

def daredevil(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/daredevil.html',{'images' : Daredevil.objects.all(),'comment':Comment.objects.all()})

def thor(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/thor.html',{'images' : Thor.objects.all(),'comment':Comment.objects.all()})

def doctor(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/doctor.html',{'images' : Doctor.objects.all(),'comment':Comment.objects.all()})

def hulk(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/hulk.html',{'images' : Hulk.objects.all(),'comment':Comment.objects.all()})

def inf1(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/inf1.html',{'images' : Inf1.objects.all(),'comment':Comment.objects.all()})

def inf2(request):
    if request.POST:
        username=request.POST.get("username")
        cmt=request.POST.get("submit")
        db.addComment(cmt,username)
    return render(request,'user/inf2.html',{'images' : Inf2.objects.all(),'comment':Comment.objects.all()})

def comic2(request):
    return render(request,'user/comic2.html')

def base1(request):
    if request.POST:
        cmt=request.POST.get("submit")
        db.addComment(cmt)
    return render(request,'user/base1.html')

