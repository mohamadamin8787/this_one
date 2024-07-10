from django.shortcuts import render,redirect , get_object_or_404
from .forms import LoginForm , RegisterForm , Change_passwordForm , ResetPassForm , ResetPassComfirm , EditProfileForm
from django.contrib.auth import login , logout, authenticate , password_validation
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token

User = get_user_model()

def login_user(request):
    
    if request.method == 'GET':
        form = LoginForm()
        context = {
             'form' : form             
        }
        return render(request,'register/login.html', context=context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username , password=password)
         
        
            if user is not None :
                login(request,user)
                return redirect('/')
        
            else:
                messages.add_message(request,messages.ERROR,'?')
                return redirect('/')
            
        else:
            messages.add_message(request,messages.ERROR,'?')
            return redirect('/')


@login_required

def logout_user(request):
    logout(request)
    return redirect('/')

def signap_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'created sucessfully')
            return redirect('/')
        else:
            messages.add_message(request,messages.SUCCESS,'not valid') 
            return redirect('accounts:signup')

        
    else:
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request,'register/signup.html',context=context)
    
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.method == 'POST':
                form = Change_passwordForm(request.POST)
                if form.is_valid():
                    old_pass = request.POST.get('old_pass')
                    new_pass1 = request.POST.get('new_pass1')
                    new_pass2 = request.POST.get('new_pass2')
                    user = request.user
                    if user.check_password(old_pass):
                        if (new_pass1==new_pass2) and (new_pass1 and new_pass2) and old_pass!=new_pass1:
                            try:
                                password_validation.validate_password(old_pass)
                                password_validation.validate_password(new_pass1)
                                user.set_password(new_pass1)
                                user.save()
                                login(request,user)
                                messages.add_message(request,messages.SUCCESS, 'your password change sucessfully')
                                return redirect('/')
                            except:
                                messages.add_message(request,messages.ERROR, 'your password is not valid')
                                return redirect('accounts:change_password')
                        else:
                            messages.add_message(request,messages.ERROR, 'your password is not valid')
                            return redirect('accounts:change_password')
                    else:
                        messages.add_message(request,messages.ERROR, 'your old_password is not valid')
                        return redirect('accounts:change_password')
        else:            
            form = Change_passwordForm()
            context = {
                'form' : form
            }
            return render(request,'register/change_pass.html',context=context)

    else:
        return render(request,'register/login.html')

def reset_password(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST.get('email'))
            token , creat = Token.objects.get_or_create(user=user)
            send_mail(
                'reset_password',
                f'http://127.0.0.1:800/accounts/reset_password_confirm/{token.key}/',
                from_email={'noreply@locationhost'},
                recipient_list=[user.email],
                # fail_silently= True,
            )
            return redirect('accounts:reset_password_done')
            
        except:
            messages.add_message(request,messages.ERROR, 'your email was not exist!!!')
            return redirect('accounts:reset_password')
    
    else:
        form = ResetPassForm()
        context = {
            'form' : form
        }
        return render(request,'register/reset_pass.html',context=context)


def reset_password_done(request):
    return render(request,'register/reset_password_done.html')

def reset_password_confirm(request,token):
        if request.method == 'POST':
            user_name = Token.objects.get(key = token).user
            user = User.objects.get(username = user_name)
            pass1  = request.POST.get('password1')
            pass2  = request.POST.get('password2')
            if (pass1 == pass2) and (pass1 and pass2):                    
                password_validation.validate_password(pass1)
                user.set_password(pass1)
                user.save()

                return render(request,'reset_password_complete.html')
            # else:
            #     return redirect('accounts:log_in')
               
        else:
            form = ResetPassComfirm()
            context = {
                'form' : form
            }
            return render(request,'register/reset_password_confirm.html',context=context)
               

def reset_password_complete(request):
    return render(request,'reset_password_complete.html')

# def change_profile(request,id):
#     if request.user.is_authenticated:
#     user = get_object_or_404(User , id = id)
#     if request.method == 'POST':
#        form = EditProfileForm(request.POST , instance=user)
#        if form.is_valid():
#            form.save()
#            return redirect('/')
    
#     else:
#         form = EditProfileForm(instance=user)
#         context = {
#             'form' : form
#         }
#         return render(request, 'register/edit_profile.html',context=context)
def change_profile(request,id):
        if request.user.is_authenticated:
            user = get_object_or_404(User , id=id)
            if request.method == 'POST':
                form = EditProfileForm(request.POST , instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('/')  
            else:
                form = EditProfileForm(instance=user)
                context = {
                    'form' : form
                }
                return render(request, 'register/edit_profile.html',context=context)
        
        else:
            return redirect('accounts:log_in')
            

