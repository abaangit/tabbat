# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Sale
from django.db.models import Sum
from datetime import date
from decimal import Decimal

def dashboard(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity_sold = int(request.POST.get("quantity_sold"))
        price = int(request.POST.get("price"))

        product = Product.objects.get(id=product_id)
        sale = Sale(product=product, quantity_sold=quantity_sold,price=price)
        sale.save()

        return redirect('dashboard')
    return render(request, 'inventory/dashboard.html', {'products': products})



def sales_report(request):
    sales_by_date = {}
    total_per_day = {}

    all_sales = Sale.objects.all().order_by('-date')
    
    for sale in all_sales:
        date_str = sale.date.strftime('%d-%m-%Y')  # Format date as string
        if date_str not in sales_by_date:
            sales_by_date[date_str] = []
            total_per_day = 0
        sales_by_date[date_str].append({
            'product': sale.product.name,
            'quantity_sold': sale.quantity_sold,
            'price': sale.price,
            'total': sale.quantity_sold * sale.price
        })
        total_per_day += sale.quantity_sold * sale.price

    context = {
        'sales_by_date': sales_by_date,
        'total_per_day': total_per_day
    }
    return render(request, 'inventory/sales_report.html', context)