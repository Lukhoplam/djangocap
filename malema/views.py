from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='')

def biography(request):
    return render(request, 'biography.html')

@login_required(login_url='')
def life_and_education(request):
    return render(request, 'life_and_education.html')

@login_required(login_url='')
def anc_youth(request):
    """
    View function that renders the 'anc_youth.html' template.

    This view is protected by login authentication. If the user is not logged in,
    they will be redirected to the specified login URL.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'anc_youth.html' template as an HTTP response.
    """
    return render(request, 'anc_youth.html')



