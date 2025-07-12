from django.db import models

# Create your models here.
from django.db import models

CATEGORY_CHOICES = [
    ('kids', 'Kids Rakhi'),
    ('midrange', 'Mid-range Rakhi'),
    ('bhaiya_bhabhi', 'Bhaiya-Bhabhi Set'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='rakhis/')

    def __str__(self):
        return self.name

    def get_whatsapp_link(self):
        msg = f"Hi, I want to order the {self.name} Rakhi from Jill Creation."
        return f"https://wa.me/919136083495?text={msg.replace(' ', '%20')}"
