from django.shortcuts import render,redirect
from .models import Image,Profile,User
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm,ProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url = "accounts/login")
def users(request):
    users=User.objects.all()
    return render(request,'users.html',{'users':users})

@login_required(login_url = "accounts/login")
def user_profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})

@login_required(login_url = "accounts/login")
def search_results(request):
    if "users" in request.GET and request.GET["users"]:
        username = request.GET.get("users")
        users = Profile.search_user(username)
        return render(request, "results.html", {"users":users,"user":username})

@login_required(login_url = "accounts/login")
def update_prof(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            photo = form.cleaned_data["profile_photo"]
            email=form.cleaned_data['email']
            bio = form.cleaned_data["bio"]
            profile = Profile.objects.get(user)
            profile.profile_photo = photo
            profile.email=email
            profile.bio = bio
            profile.save()
            return redirect('user_profile')
    else:
        form = ProfileForm()
    return render(request, "update_prof.html", {"form":form})  

@login_required(login_url = "accounts/login")
def all_posts(request):
    images=Image.objects.all()

    return render(request,'posts.html',{'images':images})

@login_required(login_url = "accounts/login")   
def post_image(request):
    user = request.user
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = user
            image.save()
            return redirect("all_posts")
    else:
        form = ImageUploadForm()
    return render(request, "uploads.html", {"form":form})
