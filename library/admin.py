from django.contrib import admin
from .models import Student, Book, IssueBook

# Register your models here.


admin.site.register(Student)
admin.site.register(Book)
admin.site.register(IssueBook)
