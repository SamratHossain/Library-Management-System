from django.urls import path
from django.contrib.auth import views as auth_views
from library import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.home, name='admin'),
    path('addNewBook/', views.addNewBook, name='addNewBook'),
    path('viewBook/', views.viewBook, name='viewBook'),
    path('issueNewBook/', views.issueNewBook, name='issueNewBook'),
    path('viewIssueBook/', views.viewIssueBook, name='viewIssueBook'),
    path('registerNewStudent/', views.registerNewStudent, name='registerNewStudent'),
    path('viewStudentDetails/', views.viewStudentDetails, name='viewStudentDetails'),
    path('updateStudentDetails/<int:student_id>', views.updateStudentDetails, name='updateStudentDetails'),
    path('deletStudentDetails/<int:student_id>', views.deletStudentDetails, name='deletStudentDetails'),
    path('viewBook/', views.viewBook, name='viewBook'),
    path('updateBook/<str:book_isbn>', views.updateBook, name='updateBook'),
    path('deletBook/<str:book_isbn>', views.deletBook, name='deletBook'),
    path('fine/<int:id>', views.fine, name='fine'),
    path('return/<int:id>', views.ReturnBook, name='returnbook'),
    path('login/', auth_views.LoginView.as_view(template_name = 'library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'library/logout.html'), name='logout'),
    path('viewStudentDetails/search-student/', views.SearchStudent, name='SearchStudent'),
    path('viewBook/search-book/', views.SearchBook, name='SearchBook'),
    path('viewIssueBook/search-issue-book', views.SearchIssueBook, name='SearchIssueBook'),
    path('Change_Password/', views.PasswordChange, name="PasswordChange"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]