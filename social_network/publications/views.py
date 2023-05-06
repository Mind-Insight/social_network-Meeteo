from django.shortcuts import render


publications = [
    {
        'id': 0,
        'title': 'First publication',
        'main': 'hello everyone! I make social network!',
        'description': 'this is my first publication',
        'date': '06-05-2023',
        'likes': 0,
    },
    {
        'id': 1,
        'title': 'Dogs',
        'main': 'Dogs are really cute and necessary. You have to take care of them!',
        'description': 'dog post',
        'date': '12-06-2023',
        'likes': 0,
    }
]


def publications_list(request):
    context = {
        'publications': publications,
        'title': 'Publications',
    }
    return render(request, 'publications/publications_list.html', context)


def publication_detail(request, publication_id):
    context = {
        'title': 'publication',
        'publication': publications[publication_id],
    }
    return render(request, 'publications/publication_detail.html', context)
