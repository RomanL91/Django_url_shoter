from django.urls import path, re_path

import authnapp.views as authnapp



urlpatterns = [
    path('', authnapp.get_homepage, name='homepage'),
    path('sign_in/', authnapp.LoginUser.as_view(), name='sign_in'),
    path('logout/', authnapp.logout_user, name='logout'),
    path('register_in_service/', authnapp.RegisterUser.as_view(), name='register'),
    path('profile/', authnapp.Profile.as_view(), name='profile'),
    re_path(r'\b(?P<unique_string>\w{6})', authnapp.redirect_original_page, name='redirect_original_page')
]