from django.db import models

# Neues Modell "Contact" anlegen ...
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
