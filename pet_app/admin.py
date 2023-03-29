from django.contrib import admin

# Register your models here.
from pet_app import models

admin.site.register(models.Login)
admin.site.register(models.PetRegister)
admin.site.register(models.Appointment)
admin.site.register(models.Schedule)