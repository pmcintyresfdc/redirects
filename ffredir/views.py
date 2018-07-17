from django.shortcuts import render, Http404

# Create your views here.
def idx(request):
    return Http404("Something's amiss")
