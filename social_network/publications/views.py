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
    },
    {
        'id': 2,
        'title': 'Cats',
        'main': """В русском языке слово «кошка» означает либо представителя биологического вида Felis<br>
                   catus вообще независимо от пола, либо самку этого вида. Самца называют кот, а детёныша кошки — котёнок<br>
                   (мн. ч. котя́та).Слово «кошка» в русском языке является диминутивом от др.-русск. слова «котъка»[13],<br>
                   которое в свою очередь происходит от существительного «кот» и является родственным лат. cattus — кошка[14]<br>
                   (так в поздней латыни, начиная с V века, в отличие от классического латинского felis)<br>
                   и близким названиям во многих языках Европы и Ближнего Востокаasdf
                   a
                   sd
                   f
                   a
                   x = {'apple', 'banana', 'cherry'}
                   y = {'google', 'microsoft', 'apple'}
                   z = x.difference(y)
                   print(z)f
                   asdf
                   
                   asd
                   f
                   a
                   x = {'apple', 'banana', 'cherry'}
                   y = {'google', 'microsoft', 'apple'}
                   z = x.difference(y)
                   print(z)f
                   as
                   df
                   asdfsd
                   fas
                   d
                   f
                   as
                   d
                   f
                   as
                   df
                   
                   asdf
                   asd
                   f
                   as
                   df
                   asdf
                   a
                   s
                   d
                   f
                   as
                   df
                   as
                   df
                   
                   sd
                   f
                   """,
        'description': 'cat post',
        'date': '01-09-2023',
        'likes': 0,
    },
    {
        'id': 3,
        'title': 'Dogs',
        'main': 'Dogs are really cute and necessary. You have to take care of them!',
        'description': 'dog post',
        'date': '12-06-2023',
        'likes': 0,
    },
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
