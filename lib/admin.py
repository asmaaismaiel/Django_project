from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

from .models import Auther
admin.site.register(Auther)

from .models import User
admin.site.register(User)
