from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name= 'image'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    path('add/', login_required(views.ImageCreate.as_view()), name='add-image'),
    path('add/<int:pk>/', login_required(views.ImageUpdate.as_view()), name='update-image'),
    path('add/<int:pk>/delete/', login_required(views.ImageDelete.as_view()), name='delete-image'),

]
