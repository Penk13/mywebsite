from django.shortcuts import render, get_object_or_404, redirect

from .models import (
    Portfolio,
    Skill,
    Project,
    Blog,
    Contact,
)
from .forms import ContactForm


def portfolio(request):
    my_portfolio = get_object_or_404(Portfolio, id=1)
    my_skill = Skill.objects.all()
    my_project = Project.objects.all()
    my_blog = Blog.objects.all()
    my_contact = Contact.objects.get(id=1)

    form = ContactForm()
    if request.method == "POST":
        return redirect("portfolio:homepage")

    context = {
        'portfolio': my_portfolio,
        'skills': my_skill,
        'projects': my_project,
        'blogs': my_blog,
        'contact': my_contact,
        'form': form,
        }
    return render(request, "portfolio/portfolio_page.html", context)
