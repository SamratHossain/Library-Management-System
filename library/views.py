from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from .models import Student, Book, IssueBook
from .forms import updateStudentForm, updateBookForm
from django.contrib import messages

# Create your views here.
# @login_required(login_url="/login/")
def home(request):
    student = Student.objects.all()
    total_students = len(student)
    book = Book.objects.all()
    total_books = len(book)
    issuebook = IssueBook.objects.all()
    total_issue_book = len(issuebook)
    context = {'total_students':total_students, 'total_books':total_books, 'total_issue_book':total_issue_book}
    return render(request, 'library/home.html', context)

@login_required(login_url="/login/")
def addNewBook(request):
    if request.method == 'POST':
        bookName = request.POST['bookName']
        authorName = request.POST['authorName']
        category = request.POST['category']
        isbnNumber = request.POST['isbnNumber']
        quantity = request.POST['quantity']

        bookInfo = Book(bookName=bookName, authorName=authorName, category=category, isbnNumber=isbnNumber, quantity=quantity)

        bookInfo.save()
        messages.success(request, "Add New Book Successfully!")

    return render(request, 'library/addNewBook.html')

# @login_required(login_url="/login/")
def viewBook(request):
    bookDetails = Book.objects.order_by('-id')
    paginator = Paginator(bookDetails, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/viewBook.html', {'page_obj':page_obj})


@login_required(login_url="/login/")
def updateBook(request, book_isbn):
    updateBook = Book.objects.get(isbnNumber=book_isbn)
    if request.method == 'POST':
        updateBook = Book.objects.get(isbnNumber=book_isbn)
        bookForm = updateBookForm(request.POST, instance=updateBook)
        if bookForm.is_valid():
            bookForm.save()
            messages.success(request, "Book Updated Successfully!")
    return render(request, 'library/updateBook.html',{'updateBook':updateBook})

@login_required(login_url="/login/")
def deletBook(request, book_isbn):
    deletBook = Book.objects.get(isbnNumber=book_isbn)
    deletBook.delete()
    messages.success(request, "Book Deleted Successfully!")
    return viewBook(request)

@login_required(login_url="/login/")
def issueNewBook(request):
    if request.method == 'POST':
        StudentName = request.POST['StudentName']
        StudentID = request.POST['StudentID']
        BookName = request.POST['BookName']
        ISBN_Number = request.POST['ISBN_Number']
        issuebook = IssueBook(StudentName=StudentName, StudentID=StudentID, BookName=BookName, ISBN_Number=ISBN_Number)
        issuebook.save()
        messages.success(request, "New Book Issued Successfully")
    student = Student.objects.all()
    book = Book.objects.all()
    context = {'students':student, 'books':book}
    
    return render(request, 'library/issueNewBook.html', context)

@login_required(login_url="/login/")
def viewIssueBook(request):
    currentuser = request.user
    print(currentuser.first_name)  
    issuebook = IssueBook.objects.order_by('-id')
    paginator = Paginator(issuebook, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/viewIssueBook.html', {'page_obj':page_obj})

@login_required(login_url="/login/")
def registerNewStudent(request):
    if request.method == 'POST':
        studentName = request.POST['studentName']
        rollNo = request.POST['rollNo']
        departmentName = request.POST['departmentName']
        session = request.POST['session']

        studentInfo = Student(studentName=studentName, rollNo=rollNo, departmentName=departmentName, session=session )

        studentInfo.save()
        messages.success(request, "Registered Successfully!") 


    return render(request, 'library/registerNewStudent.html')

@login_required(login_url="/login/")  
def viewStudentDetails(request):
    
    studentDetails = Student.objects.order_by('-id')
    paginator = Paginator(studentDetails, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/viewStudentDetails.html', {'page_obj':page_obj})

@login_required(login_url="/login/")
def updateStudentDetails(request, student_id):
    updateStudentDetails = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        updateStudentDetails = Student.objects.get(id=student_id)
        studentForm = updateStudentForm(request.POST, instance=updateStudentDetails)
        if studentForm.is_valid():
            studentForm.save()
            messages.success(request, "Updated Successfully!") 
    return render(request, 'library/updateStudentDetails.html', {'updateStudentDetails':updateStudentDetails})

@login_required(login_url="/login/")
def deletStudentDetails(request, student_id):
    deletStudentDetails = Student.objects.get(id=student_id)
    deletStudentDetails.delete()
    messages.success(request, "Deleted Successfully!")
    return viewStudentDetails(request)

@login_required(login_url="/login/")
def fine(request, id):
    fine_count = IssueBook.objects.get(pk=id)
    ReturnDate = fine_count.return_date
    CurrentDate = date.today()
    if  ReturnDate < CurrentDate:
        delay = CurrentDate - ReturnDate
        delay_days = delay.days
        fine = delay_days * 2
    else:
        delay_days = 0
        fine = 0

    return render(request, 'library/fine.html',{'delay_days':delay_days, 'fine':fine})

@login_required(login_url="/login/")
def ReturnBook(request, id):
    return_book = IssueBook.objects.get(pk=id)
    return_book.delete()
    return viewIssueBook(request)


@login_required(login_url="/login/")
def SearchStudent(request):
    query_student = request.GET['query-student']
    print(query_student)
    try:
        student = Student.objects.get(pk=query_student)
        return render(request, 'library/SearchStudent.html',{'student':student})
    except ObjectDoesNotExist:
        return render(request, 'library/SearchStudent.html')
    

@login_required(login_url="/login/")
def SearchBook(request):
    book_id = request.GET['query-book']
    print(book_id)
    try:
        book = Book.objects.get(id=book_id)
        return render(request, 'library/SearchBook.html', {'book':book})
    except ObjectDoesNotExist:
        return render(request, 'library/SearchBook.html')

@login_required(login_url="/login/")   
def SearchIssueBook(request):
    student_id = request.GET['query-student']
    try:
        student = IssueBook.objects.filter(StudentID=student_id)
        return render(request, 'library/SearchIssueBook.html', {'students':student})
    except ObjectDoesNotExist:
        return render(request, 'library/SearchIssueBook.html')
        

def PasswordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return home(request)
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'library/password_change.html', {'form':form}) 