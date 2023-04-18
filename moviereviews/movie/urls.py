from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.home, name="home"),
    path('about/',views.about,name="about"),
    path('signup/', views.signup, name='signup'),
    path('movie/<int:movie_id>', views.detail, name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)