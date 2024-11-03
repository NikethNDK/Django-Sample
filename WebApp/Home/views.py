from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if  request.session.get('is_logged_in'):
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            if username=='admin' and password=='admin':
                request.session['is_logged_in'] = True
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password.'})

        return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')
    response = render(request, 'home.html')
    return response

def logout_view(request):
    if request.method=='POST':
        request.session.flush()
    return redirect('login')



# def home(request):
#     print(request.COOKIES)
#     visit=(request.COOKIES.get('visits',0))
#     visits=int(visit)
#     visits+=1
#     response=render(request,'home.html')
#     response.set_cookie('visits',visits)
#     return response