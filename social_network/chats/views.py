from django.shortcuts import render



def chats_list(request):
    context = {}
    return render(request, 'chats/chats_list.html', context)
