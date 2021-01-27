from django import forms
from library.models import Student, Book

class updateStudentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = "__all__"

class updateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"