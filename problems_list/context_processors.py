from .models import Links

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
