from django.shortcuts import render,redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')

    all_users = User.objects.all()

    if len(all_users)<1:
        user_lvl = 9
    else:
        user_lvl = 1

    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode('utf8')

    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        user_lvl = user_lvl,
        password = hash_pw
    )

    return redirect('/')

def all_users(request):
    if 'user_id' not in request.session:
        return redirect('/')

    all_users = User.objects.all()
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'all_users' : all_users,
        'current_user' : current_user
    }
    return render(request, 'all_users.html', context)

def login(request):
    post_data = request.POST
    results = User.objects.filter(email = post_data['email'])
    
    if len(results)> 0:

        if bcrypt.checkpw(post_data['password'].encode(), results[0].password.encode()):
            request.session['user_id'] = results[0].id
            return redirect('/all_users')
        else:
            messages.error(request, 'Email/Password incorrect')
            return redirect('/')
    else:
        messages.error(request, 'Email not found')
        return redirect('/')
    

def remove(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/all_users')

def logout(request):
    request.session.flush()
    return redirect('/')

def add_new(request):
    return render(request, 'add_new.html')

def add_new_user(request):
    errors = User.objects.basic_validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_new')

    all_users = User.objects.all()

    if len(all_users)<1:
        user_lvl = 9
    else:
        user_lvl = 1

    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode('utf8')

    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        user_lvl = user_lvl,
        password = hash_pw
    )

    return redirect('/all_users')

def admin_edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user' : user
    }
    return render(request, 'admin_edit.html', context)

def admin_edit_user(request, user_id):
    errors = User.objects.admin_edit_user(request.POST)
    user = User.objects.get(id=user_id)


    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/admin_edit/{user.id}')


    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    return redirect(f'/admin_edit/{user.id}')

def admin_edit_password(request, user_id):
    errors = User.objects.admin_edit_password(request.POST)
    user = User.objects.get(id=user_id)
    

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/admin_edit/{user.id}')

    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode('utf8')
    user.password = hash_pw
    user.save()
    return redirect(f'/admin_edit/{user.id}')

def show_user(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }
    return render(request, 'show_user.html', context)

def show_user_id(request,user_id):
    user = User.objects.get(id=user_id)
    
    context = {
        'user' : user,
    }
    return render(request, 'test_app.html', context)

def create_message(request, user_id):
    if request.method == 'POST':
        for_user = User.objects.get(id =user_id)
        from_user = User.objects.get(id = request.session['user_id'])
        Message.objects.create(
            message = request.POST['message'],
            from_user= from_user,
            for_user = for_user
        )
    return redirect(f'/show_user/{for_user.id}')

def create_comment(request, user_id ,id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        from_user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=id)
        Comment.objects.create(
            comment = request.POST['comment'],
            user= from_user,
            message = message
        )
    return redirect(f'/show_user/{user.id}')