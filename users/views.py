from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#locals
from users.models import Profile
from users.forms import ProfileForm, SignupForm

#exceptions
from django.db.utils import IntegrityError


def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.bio = data['biography']
            profile.phone = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
            
    else:
        form = ProfileForm()

    return render(request=request,
    template_name='users/update_profile.html',
    context={
        'profile': profile,
        'user': request.user,
        'form': form
    })


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        us = authenticate(request,username=username,password=password)
        if us:
            login(request, us)
            # eso es lo mismo que users/posts/
            return redirect('/posts/')
        else:
            return render(request, 'users/login.html', {'error' :'Invalid username and password' })
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    ''' esta es la forma anterior
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password!=confirm_password:
            return render(request,'users/signup.html',{'error':'error: the passwords doesn\'t match '})

        try:
            us = User.objects.create_user(username=username, password=password)
            us.first_name = first_name
            us.last_name = last_name
            us.email = email

            us.save()

            profile = Profile(user=us)
            profile.save()
        except IntegrityError:
            return render(request,'users/signup.html',{'error':'error: User already exists '})        


        return redirect('login')
    return render(request,'users/signup.html')
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request=request, template_name='users/signup.html', context={'form': form})
