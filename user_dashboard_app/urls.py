from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('create', views.create),
    path('all_users', views.all_users),
    path('login', views.login),
    path('remove/<int:user_id>', views.remove),
    path('logout', views.logout),
    path('add_new', views.add_new),
    path('add_new_user', views.add_new_user),
    path('admin_edit/<int:user_id>', views.admin_edit),
    path('admin_edit_user/<int:user_id>', views.admin_edit_user),
    path('admin_edit_password/<int:user_id>', views.admin_edit_password),
    path('show_user', views.show_user),
    path('show_user/<int:user_id>', views.show_user_id ),
    path('create_message/<int:user_id>', views.create_message),
    path('create_comment/<int:user_id>/<int:id>', views.create_comment)
]