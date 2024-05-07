import os
from django.http import FileResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    pass_error = None
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        account = request.POST['account']
        acctype = request.POST['accType']
        credit = request.POST['credit']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if not CustomLogin.objects.filter(username = email).exists():
            if password == confirm:
                login_query = CustomLogin.objects.create_user(username = email,password = password,userType = "USER",viewPass = password,is_active = 0)
                login_query.save()
                register_query = Register.objects.create(name = name,email = email,phone = phone,accountNum = account,accountType = acctype,credit = credit,balance = 20000,login_id = login_query)
                register_query.save()
                return redirect('/signin')
            else:
                pass_error = "Wrong password"

        else:
            return HttpResponse('<script>alert("Email already exists");window.location.href="/register"</script>')
        

    return render(request,'register.html',{"pass_error":pass_error})

def signin(request):
    pass_error = None
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email, password = password)

        if user is not None:
            if not user.check_password(password):
                pass_error = "Wrong password"
            else:
                login(request,user)
                if user.userType == "USER":
                    request.session['userid'] = user.id
                    return redirect('/user_index')
                elif user.userType == "ADMIN":
                    request.session['admin'] = user.id
                    return redirect('/admin_index')
        else:
            pass_error = "Invalid email or password"
    return render(request,"signin.html",{"pass_error":pass_error})

def user_index(request):
    user = request.session['userid']
    return render(request, "user_index.html")

def signout(request):
    logout(request)
    request.session.flush()
    return redirect('/signin')

def user_services(request):
    user = request.session['userid']
    data = Register.objects.get(login_id = user)
    return render(request,'user_services.html',{"data":data})

def user_profile(request):
    user = request.session['userid']
    profile = Register.objects.get(login_id = user)
    try:
        complaints_data = Complaints.objects.get(login_id=user)
        complaint = complaints_data.complaint
        replied_msg = complaints_data.complaint_reply
        if replied_msg is None:
            message = "Your complaint is not yet replied"
        else:
            message = replied_msg
    except Complaints.DoesNotExist:
        complaint = None
        message = "No complaints found for the logged-in user."
    return render(request,'user_profile.html',{"profile":profile,"message":message,"complaint":complaint})

def userprofile_update(request):
    id = request.GET['id']
    data = Register.objects.get(login_id = id)
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        update_query = Register.objects.filter(login_id = id).update(name = name, email = email, phone = phone)
        if password:
            hashed_password = make_password(password)
            CustomLogin.objects.filter(id=id).update(password=hashed_password, viewPass=password)
            
        return redirect('/user_services')
    return render(request,'userprofile_update.html',{"data":data})

def user_deposit(request):
    error_msg = None
    user = request.session.get('userid')
    user_id = CustomLogin.objects.get(id=user)
    credit_id = Register.objects.get(login_id = user)
    print(user)
    if request.POST:
        account = request.POST['account']
        amount = request.POST['amount']
        message = request.POST['message']
        if Register.objects.filter(accountNum = account).exists():
            register_entry = Register.objects.get(accountNum=account)
            current_amount = register_entry.balance
            new_amount = current_amount + int(amount)

            dec_entry = Register.objects.get(login_id = user)
            balance = dec_entry.balance
            dec_amount = balance - int(amount)

            update_query = Register.objects.filter(accountNum = account).update(balance = new_amount)

            up_query = Register.objects.filter(login_id = user).update(balance = dec_amount)

            create_query = Deposits.objects.create(user_id = user_id,account = register_entry,amount = amount,message = message)
            create_query.save()
            return redirect('/payment_success')
        else:
            error_msg = "Account number is invalid"
    return render(request, 'user_deposit.html',{"error_msg":error_msg,"credit":credit_id})

def user_depositView(request):
    user = request.session.get('userid')
    user_account = CustomLogin.objects.get(id = user)
    deposits = Deposits.objects.filter(user_id = user_account)
    sender = Register.objects.filter(login_id = user)
    return render(request, 'user_depositView.html',{"deposits":deposits,"sender":sender})

def payment_success(request):
    return render(request,'payment_success.html')

def loan_application(request):
    user = request.session.get('userid')
    user_id = CustomLogin.objects.get(id = user)
    if request.POST:
        loan_amount = request.POST['loan_amount']
        annual_income = request.POST['annual_income']
        loan_type = request.POST['loan_type']
        title = request.POST['title']
        first = request.POST['first']
        last = request.POST['last']
        name = f"{title} {first} {last}"
        dob = request.POST['dob']
        marital = request.POST['marital']
        email = request.POST['email']
        phone = request.POST['phone']
        address1 = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        postal = request.POST['postal']
        address = f"{address1} {address2} {city} {state} {postal}"
        year = request.POST['year']
        employer_first = request.POST['employer_first']
        employer_last = request.POST['employer_last']
        employer_name = f"{employer_first} {employer_last}"
        occupation = request.POST['occupation']
        experience = request.POST['exp']
        income = request.POST['income']
        mortgage = request.POST['mortgage']
        comments = request.POST['comments']
        bank_name = request.POST['bank']
        bank_address = request.POST['bank_address']
        bank = f"{bank_name} {bank_address}"
        accountNum = request.POST['account']
        aadhar = request.FILES['aadhar']
        pan = request.FILES['pan']
        
        create_query = LoanApplication.objects.create(
            loan_amount = loan_amount,
            annual_income = annual_income,
            loan_type = loan_type,
            name = name,
            dob = dob,
            marital_status = marital,
            email = email,
            phone = phone,
            address = address,
            address_year = year,
            employer = employer_name,
            occupation = occupation,
            experience = experience,
            income = income,
            mortgage = mortgage,
            comments = comments,
            bank = bank,
            accountNum = accountNum,
            aadhar = aadhar,
            pan = pan,
            login_id = user_id,
            status = "Pending"
            )
        create_query.save()
        return redirect('/application_success')

    return render(request,'loan_application.html')

def application_success(request):
    return render(request,'application_success.html')

def admin_index(request):
    user = request.session['admin']
    return render(request,'admin_index.html')

def loanTable_view(request):
    data = LoanApplication.objects.filter(status = "Pending")
    return render(request,'loanTable_view.html',{"data":data})

def loanApplicationView(request):
    id = request.GET['id']
    data = LoanApplication.objects.get(id=id)
    return render(request,'loanApplicationView.html',{"data":data})

def approveLoan(request):
    id = request.GET['id']
    data = LoanApplication.objects.get(id=id)
    login_id = data.login_id
    register_id = data.register_id
    balance =register_id.balance
    loan_amount = data.loan_amount
    total = int(balance)+int(loan_amount)
    balance_query = Register.objects.filter(login_id=login_id).update(balance=total)
    status_query = LoanApplication.objects.filter(id=id).update(status = "Approved")
    return redirect('/loanTable_view')

def rejectLoan(request):
    id = request.GET['id']
    data = LoanApplication.objects.filter(id=id).update(status = "Rejected")
    return redirect('/loanTable_view')

def userLoan_status(request):
    user = request.session['userid']
    data = LoanApplication.objects.filter(login_id = user,status = "Pending")
    return render(request,'userLoan_status.html',{"data":data})

def userView(request):
    data = Register.objects.all()
    return render(request,'userview.html',{"data":data})

def userRequests(request):
    data = Register.objects.filter(login_id__is_active = 0)
    return render(request,'userRequests.html',{"data":data})

def approveUser(request):
    id = request.GET['id']
    data = CustomLogin.objects.filter(id = id).update(is_active = 1)
    return redirect('/userRequests')

def rejectUser(request):
    id = request.GET['id']
    data = CustomLogin.objects.filter(id=id).delete()
    return redirect('/userRequests')

def user_complaints(request):
    user = request.session['userid']
    data = Register.objects.get(login_id = user)
    user_id = CustomLogin.objects.get(id = user)
    if request.POST:
        complaint = request.POST['message']
        complaint_query = Complaints.objects.create(user_id = data,complaint = complaint,login_id = user_id)
        complaint_query.save()
        return redirect('/complaintSuccess')
    return render(request,'user_complaints.html',{"data":data})
    
def complaintSuccess(request):
    return render(request,'complaintSuccess.html')

def complaintViewTable(request):
    user = request.session['admin']
    data = Complaints.objects.filter(complaint_reply__isnull = True)
    return render(request,'complaintViewTable.html',{"data":data})

def complaintView(request):
    id = request.GET['id']
    data = Complaints.objects.get(id = id)
    if request.POST:
        reply = request.POST['reply']
        reply_query = Complaints.objects.filter(id = id).update(complaint_reply = reply)
        return redirect('/replySuccess')
    return render(request,'complaintView.html',{"data":data})

def replySuccess(request):
    return render(request,'replySuccess.html')

from django.core.exceptions import ObjectDoesNotExist

def notifications(request):
    user_id = request.session.get('userid')
    
    # Get deposits made today
    current_date = timezone.now().date()
    try:
        deposits_today = Deposits.objects.filter(user_id=user_id, timestamp__date=current_date)
    except Deposits.DoesNotExist:
        deposits_today = None
    
    return render(request, 'notifications.html', {
        "deposits_today": deposits_today
    })

