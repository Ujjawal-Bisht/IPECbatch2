from django.shortcuts import render

# Create your views here.


#changes

def home(request):
    # info = ["Ujjawal Bisht", "Delhi", 20, "Python", "Django"]
    info = {
        'personal_info': {
            'name': 'Ujjawal Bisht',
            'city': 'Delhi',
            'age': 20,
            'Gender': 'M'
        },
        'skills': ['Python', 'Django']
    }

    # newInfo = [{"name": "Ujjawal Bisht", "city": "Delhi", "age": 20, "Gender": "M"}, ["Python", "Django"], {"name": "Ujjawal Bisht", "city": "Delhi", "age": 20, "Gender": "M"}, ["Python", "Django"]]
    return render(request, "home.html", {"info": info})

def profile(request):
    return render(request, "profile.html")

def skills(request):
    return render(request, "skills.html")

def project(request):
    return render(request, "project.html")