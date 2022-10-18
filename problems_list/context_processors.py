from .models import Problem, Links


def problems_count_by_difficulty(request):
    easy_count = Problem.objects.filter(difficulty__name__contains="Easy").count()
    medium_count = Problem.objects.filter(difficulty__name__contains="Medium").count()
    hard_count = Problem.objects.filter(difficulty__name__contains="Hard").count()

    context = {
        'easy_count': easy_count,
        'medium_count': medium_count,
        'hard_count': hard_count
    }
    return context


def links(request):
    github = Links.objects.get(name="github")
    leetcode_github = Links.objects.get(name="leetcode_github")
    medium = Links.objects.get(name="medium")
    linkedin = Links.objects.get(name="linkedin")

    context = {
        'github': github,
        'leetcode_github': leetcode_github,
        'medium': medium,
        'linkedin': linkedin
    }
    return context
