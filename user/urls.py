from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
  url('^$',views.index,name='home'),
  url(r'^users/',views.users, name='users'),
  url(r'^user_profile/',views.user_profile,name='user_profile'),
  url(r'^search_results/',views.search_results,name='search_results'),
  url(r'^all_posts/',views.all_posts, name='posts'),
  url(r'^update_prof/',views.update_prof,name='update'),
  url(r'^upload/',views.post_image,name='upload')
  
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
