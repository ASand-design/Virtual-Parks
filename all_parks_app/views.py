from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login(request):
    
    user, errors = User.objects.login_validate(request.POST)

    if errors:
        for user,error in errors.items():
            messages.error(request, error)
        return redirect("/login")
    else:
        request.session['user_id'] = user.id
        return redirect("/welcome")

def register(request):
    
    errors = User.objects.register_validate(request.POST)

    if errors:
        for user,error in errors.items():
            messages.error(request, error)
        return redirect("/login")
    else:
        user = User.objects.create(first_name=request.POST['first_name'], 
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email'],
                                    password=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode())
        request.session['user_id'] = user.id
        return redirect("/welcome")

def about(request):
    return render(request, 'about.html')

def disney(request):
    return render(request, 'disney.html')

def universal(request):
    return render(request, 'universal.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')
