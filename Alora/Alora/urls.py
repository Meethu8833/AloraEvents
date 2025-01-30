"""
URL configuration for Alora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resetpassword',views.password_reset_request,name='resetpassword'),
    path('verifyotp',views.verify_otp,name='verifyotp'),
    path('newpassword',views.set_new_password,name='newpassword'),
    path('',views.index),
    path('reg',views.user_registration,name='reg'),
    path('log',views.user_login,name='log'),
    path('userhome',views.user_home,name='userhome'),
    path('viewuser',views.view_user,name='viewuser'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('edituser',views.edit_user,name='edituser'),
    path('userdetails',views.user_details,name='userdetails'),
    path('halldetails',views.hall_details,name='halldetails'),
    path('addhall',views.add_hall,name='addhall'),
    path('admin_viewHall/<int:id>',views.admin_viewHall,name='admin_viewHall'),
    path('fooddetails',views.food_details,name='fooddetails'),
    path('addfood',views.add_food,name='addfood'),
    path('deletefood/<int:id>',views.delete_food,name='deletefood'),
    path('decorationdetails',views.decoration_details,name='decorationdetails'),
    path('adddecoration',views.add_decoration,name='adddecoration'),
    path('logoutuser',views.logout_user,name='logoutuser'),
    path('book',views.booking,name='book'),
    path('userviewbooking',views.user_view_booking,name='userviewbooking'),
    path('adminviewbooking',views.admin_view_booking,name='adminviewbooking'),
    path('acceptrejectbooking/<int:id>',views.accept_reject_booking,name='acceptrejectbooking'),
    path('stripe_payments/<int:id>',views.stripe_payments,name='stripe_payments'),
    path('payment_status/<int:id>',views.payment_status,name='payment_status'),

    path('ind',views.ind),
    path('ind2',views.ind2),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)