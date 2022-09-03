from django.shortcuts import render
from docx import Document
import os
from django.http import HttpResponse
from .cmdEx import Exec 
from .entry import gg
from .models import Questions,Details
def index(request):

    Exec("A")
    
    return HttpResponse("done1")