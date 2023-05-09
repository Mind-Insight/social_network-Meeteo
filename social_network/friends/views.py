from django.shortcuts import render


def friends_list(request):
    return render(request, 'friends/friends_list.html')