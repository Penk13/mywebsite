from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

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
    my_contact = get_object_or_404(Contact, id=1)

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

            send_mail(
                name,  # subject
                'From : ' + email + '\n' + message,  # message
                email,  # from : ...
                ['natanaelsteven109@gmail.com']  # to : ...
                )
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


def read_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {'blog': blog}
    return render(request, "portfolio/blog.html", context)
