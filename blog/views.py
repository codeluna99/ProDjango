from django.shortcuts import render

posts = [
    {
        'author': 'writer-one',
        'title' : 'Blog-1',
        'date' : '24th august,2020',
        'content': 'Here will be the content of the first blog',
    },
    {
        'author': 'writer-two',
        'title' : 'Blog-2',
        'date' : '25th august,2020',
        'content': 'Here will be the content of the SECOND blog',
    }
]

def home(request):

    context = {
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})