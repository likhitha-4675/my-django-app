from django.shortcuts import render

def login_page(request):
    return render(request, 'login_page.html')

def check_username(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        if uname == 'admin':
            return render(request, 'success.html', {'field': 'Username'})
        else:
            return render(request, 'invalid.html', {'field': 'Username'})

def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == 'admin@example.com':
            return render(request, 'success.html', {'field': 'Email'})
        else:
            return render(request, 'invalid.html', {'field': 'Email'})

def check_password(request):
    if request.method == 'POST':
        pwd = request.POST.get('password')
        if pwd == 'admin123':
            return render(request, 'success.html', {'field': 'Password'})
        else:
            return render(request, 'invalid.html', {'field': 'Password'})
