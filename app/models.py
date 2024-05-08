from django.db import models

# Create your models here.
class suppliers(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField(max_length=50)
      phone =models.IntegerField()

      def __str__(self):
            text = "{0} ({1})"
            return text.format(self.name, self.email, self.phone)
      
class products(models.Model):
      name = models.CharField(max_length=300)
      quantity = models.PositiveIntegerField()
      supplier = models.ForeignKey(suppliers, on_delete=models.CASCADE)    
    
      def __str__(self):
            return self.name  