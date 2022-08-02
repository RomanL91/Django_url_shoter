import random
import string
import tldextract

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from authnapp.forms import CustomUserCreationForm
from link_shortener.forms import UrlUserForm
from link_shortener.models import ClippedLinks
from link_shortener.models import ThroughModel



UNIQUE_STRING_LENGTH = 6


def get_homepage(request):
    title = 'Main_page'
    content = {'title': title}
    return render(request, 'authnapp/index.html', content)


def logout_user(request):
    logout(request)
    title = 'Main_page'
    content = {'title': title}
    return render(request, 'authnapp/index.html', content)


def redirect_original_page(request, unique_string=None):
    try:
        full_url_short_link = request.build_absolute_uri()
        original_link = ClippedLinks.objects.get(shortened_link = full_url_short_link).original_link
        return HttpResponseRedirect(original_link)
    except ObjectDoesNotExist:
        return redirect('homepage')


def get_unique_string():
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    random_string = ''.join(random.choice(char) for x in range(UNIQUE_STRING_LENGTH))
    return random_string
    

class Profile(LoginRequiredMixin, CreateView):
    form_class = UrlUserForm
    success_url = reverse_lazy('profile')
    template_name = 'authnapp/profile.html'


    def get(self, request, *args, **kwargs):
        title = 'Profile'
        form = UrlUserForm(request.GET)
        authent_user = request.user
        list_user_links = ClippedLinks.objects.filter(creator_link = authent_user)
        content = {'title': title, 'form': form, 'list_user_links': list_user_links, 'authent_user': authent_user}
        return render(request, self.template_name, content)


    def post(self, request, *args, **kwargs):          
        form = UrlUserForm(request.POST)
        link_creator = request.user
        original_link = form.data['original_link']
        list_links_in_database = ClippedLinks.objects.filter(original_link=original_link)
        # думаю можно переделать логику по другому, через try и может меньше дергать БД, может через get_or_create
        # еще как-нибудь, если ссылка будет, то добавлять в кортеж(возрат от get_or_create) при помощи __add__, 
        # затем это еще ...в общем пока так норм=)
        if form.is_valid() and not list_links_in_database.exists():
            extracted = tldextract.extract(original_link)
            domain = "{}.{}".format(extracted.domain, extracted.suffix)
            u_id = get_unique_string()
            short_url = 'http://' + request.get_host() + "/" + u_id

            new_short_link = ClippedLinks.objects.create(
                original_link = original_link,
                shortened_link = short_url
            )
            new_short_link.creator_link.add(link_creator)           
            return HttpResponseRedirect(request.path)
        else:
            ThroughModel.objects.get_or_create(
                user = link_creator,
                link = list_links_in_database[0]
            )
            return HttpResponseRedirect(request.path)        


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'authnapp/register.html'
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('sign_in')
        else:
            return render(request, self.template_name, {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authnapp/sign_in.html'

    def get_success_url(self):
        return reverse_lazy('profile')
