from django.shortcuts import render


def blog(request):
    context = {

    }
    return render(request, 'store/blog.html', context)
