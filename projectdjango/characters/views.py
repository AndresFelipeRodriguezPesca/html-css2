from django.shortcuts import render, redirect
from django.http import HttpResponse
from characters.models import Character

def list(request):
    print(request.method)
    list_=Character.objects.all()
    return  render(request, 'characters/index.html', {'list':list_})



def save(request):

    if request.method == "GET":
        return render(request, 'characters/save.html')

    name_=request.POST["name"]
    description_=request.POST["description"]

    character =Character(name=name_, description=description_)
    character.save()
    #file=request.FILES["file"]
    return redirect("Lo que obtenemos del formulario", description_)


def detail(request):
    try:
        character= Character.objects.get(id=id)
    except Character.DoesNotExist:
        return HttpResponse("Not found register")
    return render(request, 'characters/detail.html',{"character":character})

def edit(request, id):
    return HttpResponse(id)

