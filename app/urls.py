from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerSupplier/', views.registerSupplier),
    path('editSupplier/<str:name>', views.editSupplier, name='editSupplier'),
    path('editionSupplier/<str:name>/', views.editionSupplier, name='editionSupplier'),
    path('deleteSupplier/<int:id>', views.deleteSupplier, name='deleteSupplier'),
    
    path('registerProduct/', views.registerProduct),
    path('editProduct/<int:id>/', views.editProduct, name='editProduct'),
    path('updateProduct/<int:id>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('products/', views.registerProduct, name='registerProduct'),
]
