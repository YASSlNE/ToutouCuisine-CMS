from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
# def get_cli(request):
#     if request.method=='POST':
#         form=ClientForm(request.POST)
#         # if form.is_valid():
#     return render(request,'index.html',{'form':form})
def getCommandes(request,client_id):
    commandes=Commande.objects.filter(client=client_id)
    context={'commandes':commandes}
    return render(request,'accounts/get-commandes.html',context)
def delete(request,client_id):
    client=Clients.objects.get(pk=client_id)
    client.delete()
    return HttpResponseRedirect('/')
def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
# def home(request):
#     orders = Order.objects.all()
#     customers = Customer.objects.all()

#     total_customers = customers.count()

#     total_orders = orders.count()
#     delivered = orders.filter(status='Delivered').count()
#     pending = orders.filter(status='Pending').count()

#     context = {'orders': orders, 'customers': customers,
#                'total_orders': total_orders, 'delivered': delivered,
#                'pending': pending}

#     return render(request, 'accounts/dashboard.html', context)
@login_required(login_url='login')
def home(request):
    clients=Clients.objects.all()
    # commandes=Commande.objects.all()
    total_clients=clients.count()
    form=ClientForm()
    form2=CommandeForm()
    # context={'clients':clients,'total':total_clients,'form':form,'form2':form2}
    if request.method=='POST':
        form=ClientForm(request.POST)
        form2=CommandeForm(request.POST)
        if form.is_valid():
            full_name=form.cleaned_data['full_name']
            num_tel=form.cleaned_data['num_tel']
            lien_prof=form.cleaned_data['lien_prof']
            # nouv_client=Clients()
            nouv_client=Clients(name=full_name,phone=num_tel,profile_link=lien_prof)
            nouv_client.save()
            form=ClientForm()
            # form2=CommandeForm()
            return HttpResponseRedirect('/')
        elif(form2.is_valid()):
            # print(request.POST['field'])
            # print(form2.cleaned_data)
            about=form2.cleaned_data['about']
            cout=form2.cleaned_data['cout']
            prix=form2.cleaned_data['prix']
            k=Clients.objects.filter(id=int(request.POST['field']))[0]
            nouv_commande=Commande(about=about,cout=cout,prix=prix,client=k)
            nouv_commande.save()
            form2=CommandeForm()
            return HttpResponseRedirect('/')
    context={'clients':clients,'total':total_clients,'form':form,'form2':form2}
    return render(request,'accounts/index.html',context)
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ClientForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             print("a7a")
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect('/thanks/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ClientForm()
#     return render(request, 'name.html', {'form': form})
@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
               'customer': customer,
               'orders': orders,
               'order_count': order_count,
               }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)



@login_required(login_url='login')
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)