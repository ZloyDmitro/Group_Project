from django.shortcuts import render, redirect, get_object_or_404
from .models import products, suppliers
from django.contrib import messages

# Create your views here.
def home(request):
    supplierslist = suppliers.objects.all()
    return render(request, "gestionsuppliers.html", {"suppliers": supplierslist})

def registerSupplier(request):
    name=request.POST['txtname']
    email=request.POST['txtemail']
    phone=request.POST['numphone']

    supplier = suppliers.objects.create(name=name, email=email, phone=phone)
    messages.success(request, 'Registered supplier')
    return redirect('/')

def editSupplier(request, name):
    supplier = get_object_or_404(suppliers, name=name)
    return render(request, "editSupplier.html", {"supplier": supplier})

def editionSupplier(request, name):
    supplier = get_object_or_404(suppliers, name=name)

    if request.method == 'POST':
        new_name = request.POST['txtname']
        email = request.POST['txtemail']
        phone = request.POST['numphone']

        supplier.name = new_name
        supplier.email = email
        supplier.phone = phone
        supplier.save()
        messages.success(request, 'Edited supplier')
        return redirect('/')

    return render(request, "editSupplier.html", {"supplier": supplier})

def deleteSupplier(request, id):
    supplier = get_object_or_404(suppliers, id=id)
    supplier.delete()
    messages.success(request, 'Supplier deleted')
    return redirect('/')

# products ---------------------------------------------------------------------------------------------------------------------

def registerProduct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        supplier_id = request.POST.get('supplier')

        # Obtener el proveedor asociado al ID
        supplier = suppliers.objects.get(pk=supplier_id)

        product = products.objects.create(name=name, quantity=quantity, supplier=supplier)
        messages.success(request, 'Registered Product')
        return redirect('registerProduct')  # Redirige de vuelta a la página de registro de productos después de crear uno nuevo
        
    
    suppliers_list = suppliers.objects.all()
    products_list = products.objects.all()
    return render(request, 'products.html', {'suppliers': suppliers_list, 'products': products_list})

def editProduct(request, id):
    product = get_object_or_404(products, id=id)
    supplier_list = suppliers.objects.all()  # Obtener todos los proveedores
    return render(request, "editproduct.html", {"product": product, "suppliers": supplier_list})

def updateProduct(request, id):
    product = get_object_or_404(products, id=id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        supplier_id = request.POST['supplier']
        supplier = get_object_or_404(suppliers, id=supplier_id)  # Obtener el objeto del proveedor
        product.supplier = supplier  # Asignar el proveedor al producto
        product.save()
        messages.success(request, 'Product updated')
        return redirect('/products')
    
    return render(request, "editproduct.html", {"product": product})

def deleteProduct(request, id):
    product = get_object_or_404(products, id=id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect('/products')