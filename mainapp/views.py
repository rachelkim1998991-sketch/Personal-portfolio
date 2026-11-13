import os
from django.contrib import messages
from django.shortcuts import redirect, render
from dotenv import load_dotenv
from .forms import MessageForm
from .models import Project, Skill

load_dotenv()
PROFILE = {
    "name": os.getenv('PROFILE_NAME'),
    "role": "Backend developer",
    "tagline": "Django bilan veb-ilovalar yarataman.",
    "about": "Bu yerga o'zingiz haqingizda 3-4 jumla yozing.",
    "phone": os.getenv('PHONE_NUMBER'),
    "email": os.getenv('EMAIL_ADDRESS'),
    "github": os.getenv('GITHUB_USERNAME'),
    "linkedin": "",
    "telegram": os.getenv('TELEGRAM_USERNAME'),
    "cv_url": "",    
}


def index(request):
    skills = {}
    for s in Skill.objects.all():
        skills.setdefault(s.category, []).append(s)
    return render(request, "index.html", {
        "profile": PROFILE,
        "skills": skills,
        "projects": Project.objects.filter(is_published=True),
    })


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz yuborildi. Rahmat!")
            return redirect("contact")
    else:
        form = MessageForm()
    return render(request, "contact.html", {"profile": PROFILE, "form": form})
