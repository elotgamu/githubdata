import json
import requests
from django.contrib import messages
from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('Hello World!')


def test(request):
    return HttpResponse('My second view, the Test!')


def profile(request):
    parsed_data = []

    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        user_data = {}
        if req.status_code == 404:
            messages.info(request, 'Sorry, username not found')
        else:
            json_list = []
            json_list.append(json.loads(req.content))
            # user_data = {}

            for data in json_list:
                user_data['name'] = data['name']
                user_data['blog'] = data['blog']
                user_data['email'] = data['email']
                user_data['public_gists'] = data['public_gists']
                user_data['public_repos'] = data['public_repos']
                user_data['avatar_url'] = data['avatar_url']
                user_data['followers'] = data['followers']
                user_data['following'] = data['following']

        parsed_data.append(user_data)

    return render(request, 'ghdata/profile.html', {'data': parsed_data})
