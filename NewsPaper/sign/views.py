from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from news.models import Author
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
#from news.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


# @login_required
# def upgrade_me(request):
#     user = request.user
#     author_group = Group.objects.get(name='author')
#     if not request.user.groups.filter(name='author').exists():
#         author_group.user_set.add(user)
#     return redirect('/')

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        authors_group.user_set.add(user)
    author= Author.objects.filter(user=user)
    if not author:
        Author.objects.create(user=user)
    return redirect('post_list')