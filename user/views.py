from django.shortcuts import render
from .models import Image,Profile,User
from django.template.context_processors import request
from .forms import ImageUploadForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    users=User.objects.all()
    return render(request,'users.html',{'users':users})

def user_profile(request):
    user = Profile.objects.all()
    return render(request,'profile.html',{'user':user})


def search_results(request):
    if 'users' in request.GET['users']:
        users = request.GET.get('users')
        results = Profile.search_user(users)
        message = f'{users}'
        title=f'{users}'
        return render(request,'results.html',{'message':message,'users':results,'title':title})

    else:
        message= 'Choose an option to search'
        render(request,'results.html',{'message':message})
    
def update_prof(request):
    return render(request,'update_prof.html')

def all_posts(request):
    images=Image.objects.all()

    return render(request,'posts.html',{'images':images})
def post_image(request):
    form=ImageUploadForm
    return render(request,'uploads.html',{'form':form})
