from django.shortcuts import render
from django.db.models import Q
from .utils.problems_list.paginate import try_page
from .models import Problem


def problems_list(request):
    problems_list = Problem.objects.all().order_by('-add_date')
    problems_count = problems_list.count()
    
    problems = try_page(request, problems_list)

    context = {
        'problems': problems,
        'problems_count': problems_count,
    }
    return render(request, 'problems_list/list.html', context)


def search(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''

    problems_list = Problem.objects.filter(
        Q(name__icontains=query) |
        Q(topic__icontains=query) |
        Q(difficulty__name__icontains=query)
    ).order_by('-add_date')

    problems_count = problems_list.count()

    problems = try_page(request, problems_list)

    context = {
        'problems': problems,
        'problems_count': problems_count,
        'query': query,
    }

    return render(request, 'problems_list/search.html', context)


def note(request, pk):
    problem = Problem.objects.get(id=pk)

    context = {
        'problem': problem,
    }
    return render(request, 'problems_list/note.html', context)


def about(request):
    return render(request, 'problems_list/about.html')
