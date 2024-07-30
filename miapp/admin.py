from django.contrib import admin

# Register your models here.
# vanos a registrar el modelo

# con esto impprtamos el modelo
from .models import Board

admin.site.register(Board)

