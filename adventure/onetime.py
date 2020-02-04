from django.shortcuts import render
from django.http import HttpResponse

hotnotes = [
    {
        'subject': 'Math',
        'author': 'Albert Einstein',
        'note': 'E is equal to MC squared',
        'date_posted': 'should use datetime package to generate this!'
    },
    {
        'subject': 'Science',
        'author': 'Stephen Hawking',
        'note': 'Intelligence is the ability to adapt to change.',
        'date_posted': 'As stated before, should use datetime package to generate this!'
    },
]

def home(request):
    # context = {
    #     'mynotes': hotnotes
    # }
    return HttpResponse("hello")
    # return render(request, 'notes/home.html', context)

def onetimer():
    print('testing here')
    return HttpResponse("TESTING")
    # return render(request, 'notes/about.html')