import json
from django.shortcuts import render

json_data = open("json_file.json")
data = json.load(json_data)


def index(request):

    context = {'datas':data}


    return render(request, 'index.html', context)