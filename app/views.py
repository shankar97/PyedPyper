"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django import forms
from forms import attrForm
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def data(request):
    """Renders the data page."""
    assert isinstance(request, HttpRequest)
    form = attrForm();
    if request.method == 'POST':
        form = attrForm(request.POST);
        return render(
            request, 
            'app/data.html',
            {
                'forms': form, 
                'title':'Data Representation',
            }
        )
    else:
        return render(
            request,
            'app/data.html',
            {   
                'title':'Data',
                'year':datetime.now().year,
            }
        )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'PyedPypers history',
            'year':datetime.now().year,
        }
    )
