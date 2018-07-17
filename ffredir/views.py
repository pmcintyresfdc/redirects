from django.shortcuts import render, Http404


# Create your views here.
def idx(request):
    raise Http404("Something's amiss")
