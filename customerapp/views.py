from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_tbl

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def about(hello):
    return HttpResponse("About page")

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        ue = request.POST.get('email')
        upass = request.POST.get('password')

        # print(ue,upass)
        obj = Customer_tbl.objects.filter(
            email = ue,
            password = upass
        )
        if obj:
            # print(obj.__dict__)
            for i in obj:
                request.session['user_id'] = i.id
            return render(request,'index.html')
        return render(request, 'login.html')
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        un = request.POST['user_name']
        ue = request.POST['email']
        up = request.POST['phone']
        upass = request.POST['password']

        obj = Customer_tbl.objects.create(
            username = un,
            email = ue,
            phone_no = up,
            password = upass
        )

        if obj:
            return render(request,'login.html')
        return render(request,'register.html')
    return render(request,'register.html')

from adminapp.models import cake_tbl

def view_products(request):
    cakes = cake_tbl.objects.all()
    # print(cakes.__dict__)
    return render(request,'products.html',{'cakes':cakes})



from .models import cart_tbl

def add_to_cart(request, cake_id):
    if 'user_id' not in request.session:
        return redirect('home-page')
    cake = cake_tbl.objects.get(id = cake_id)
    customer = Customer_tbl.objects.get(id = request.session['user_id'])

    cart_item, created = cart_tbl.objects.get_or_create(
        customer = customer,
        cake = cake
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view-products')

def view_cart(request):
    customer = Customer_tbl.objects.get(id = request.session['user_id'])

    cart_obj = cart_tbl.objects.filter(customer = customer)
    # print(cart_obj.__dict__)

    grand_total = sum(item.total_amount() for item in cart_obj)
    return render(request,'cart.html',{
            'cart_obj':cart_obj, 
            "grand_total":grand_total
        }
    )