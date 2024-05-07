"""
URL configuration for banking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('contact/',views.contact),
    path('register/',views.register),
    path('signin/',views.signin),
    path('user_index/',views.user_index),
    path('signout/',views.signout),
    path('user_services/',views.user_services),
    path('user_profile/',views.user_profile),
    path('userprofile_update/',views.userprofile_update),
    path('user_deposit/',views.user_deposit),
    path('user_depositView/',views.user_depositView),
    path('payment_success/',views.payment_success),
    path('loan_application/',views.loan_application),
    path('application_success/',views.application_success),
    path('loanTable_view/',views.loanTable_view),
    path('admin_index/',views.admin_index),
    path('loanApplicationView/',views.loanApplicationView),
    path('approveLoan/',views.approveLoan),
    path('rejectLoan/',views.rejectLoan),
    path('userLoan_status/',views.userLoan_status),
    path('userView/',views.userView),
    path('userRequests/',views.userRequests),
    path('approveUser/',views.approveUser),
    path('rejectUser/',views.rejectUser),
    path('user_complaints/',views.user_complaints),
    path('complaintSuccess/',views.complaintSuccess),
    path('complaintViewTable/',views.complaintViewTable),
    path('complaintView/',views.complaintView),
    path('replySuccess/',views.replySuccess),
    path('notifications/',views.notifications),
]
