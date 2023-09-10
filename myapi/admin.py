from django.contrib import admin

# Register your models here.
from .models import users,dsa,visits


# Register your models here.

admin.site.register(users)
admin.site.register(dsa)
admin.site.register(visits)
