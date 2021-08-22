from django.shortcuts import render, get_object_or_404

from .models import (
    Portfolio,
    Skill,
    Project,
    Blog,
)


def portfolio(request):
    my_portfolio = get_object_or_404(Portfolio, id=1)
    my_skill = Skill.objects.all()
    my_project = Project.objects.all()
    my_blog = Blog.objects.all()
    context = {
        'portfolio': my_portfolio,
        'skills': my_skill,
        'projects': my_project,
        'blogs': my_blog,
        }
    return render(request, "portfolio/portfolio_page.html", context)
