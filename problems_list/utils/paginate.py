from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

OBJECTS_PER_PAGE = 15

def try_page(request, problems_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(problems_list, OBJECTS_PER_PAGE)

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return problems
