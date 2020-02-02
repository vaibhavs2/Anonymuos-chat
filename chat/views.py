from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import keyConnectForm
import random
# Create your views here.


def chatpage(request):

    link = 'https://api.adorable.io/avatars/'+str(random.randrange(0, 100))
    link2 = link+str(1)
    return render(request, 'chatPage.html', {"profile_image": link, "sender_profile": link2})
