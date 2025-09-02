from django.shortcuts import render
from website.admin import HeroModel
# Create your views here.

def index(request):
    hero = HeroModel.objects.all()
    packages = {"hero":hero}
    return render(request, 'index.html', packages)

# about
def about(request):
    return render(request, 'about.html')

# blog
def blog(request):
    return render(request, 'blog.html')

#careers
def careers(request):
    return render(request, 'careers.html')

# contact
def contact(request):
    return render(request, 'contact.html')

#footer
def footer(request):
    return render(request, 'footer.html')

#gallery
def gallery(request):
    return render(request, 'gallery.html')

#projects
def projects(request):
    return render(request, 'projects.html')

# services
def services(request):
    return render(request, 'services.html')

#navbar
def navbar(request):
    return render(request, 'navbar.html')

#services
def services(request):
    return render(request, 'services.html')

#navbar
def navbar(request):
    return render(request, 'navbar.html')

#footer
def footer(request):
    return render(request, 'footer.html')

