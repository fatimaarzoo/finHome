"""
URL configuration for finhome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rental.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from chatbot.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('contact/', contact , name='contact'),
    path('about/', about , name='about'),
    path('house/', house , name="house"),
    path('detail/<id>/', detail , name="detail"),
    path('fdetail/<id>/', fdetail,name='fdetail'),
    path('food/', food , name="food"),
    path('register/student/', register_student, name='register_student'),
    path('register/renter/', register_renter, name='register_renter'),
    path('register/seller/', register_seller, name='register_seller'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('addrooms/',addroom,name='addrooms'),
    path('addeatery/',addfood,name='addfood'),
    path('update_room/<id>/',update_room,name='update_room'),
    path('delete_room/<id>/',delete_room,name='delete_room'),
    path('update_food/<id>/',update_food,name="update_food"),
    path('delete_food/<id>/',delete_food,name="delete_food"),
    path('profile/renter/',  rntprofile, name="profile_renter"),
    path('profile/seller/', slrprofile, name="profile_seller"),
    path('profile/student/', stdprofile , name="profile_student"),
    path('user_update/',user_update,name='user_update'),
    path('changepassword/',ChangePasswordView.as_view(),name='password_change'),
    path('<pk>/delete/',UserDeleteView.as_view(),name="delete_user"),
    path('choose_register/',choose_register,name="choose_register"),
    path('check_weather/', check_weather),
    path('chatbot/',chatbot,name="chatbot"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


