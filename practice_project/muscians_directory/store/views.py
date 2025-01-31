from django.shortcuts import render,redirect
from .forms import user_muscian_from, user_album_from
from .models import muscian_model,album_model
from django.db import connection
# Create your views here.
def homepage(request):
    mus_data = muscian_model.objects.all()
    alb_data = album_model.objects.all()

    return render(request,'base.html',{'mus_data':mus_data , 'alb_data':alb_data})

def muscianpage(request):

    if request.method=='POST':
        from_data = user_muscian_from(request.POST)
        if from_data.is_valid():
            from_data.save()
            return redirect('home_page')
        
    ms_form = user_muscian_from()
    return render(request, 'add_muscian.html' , {'form': ms_form})


def albumpage(request):

    if request.method=='POST':
        from_data = user_album_from(request.POST)
        if from_data.is_valid():
            from_data.save()
            return redirect('home_page')
        
    alb_form = user_album_from()
    return render(request, 'add_album.html' , {'form': alb_form})

def editalbum(request,id):
    album_id = album_model.objects.get(pk=id)
    album_form = user_album_from(instance=album_id)
    if request.method =='POST':
        album_form = user_album_from(request.POST, instance= album_id)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    else:
        return render(request,'add_album.html',{'form':album_form})

def deletedata(request,id):
    user_data=album_model.objects.get(pk=id)
    user_data.delete()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM store_album_model) WHERE name = 'store_album_model'")
    return redirect('home_page')


def editmuscian(request,id):
    muscian_data = album_model.objects.get(pk=id)
    mus_form = user_muscian_from(instance=muscian_data.relation)

    if request.method =="POST":
        mus_form = user_muscian_from(request.POST, instance=muscian_data.relation)
        if mus_form.is_valid():
            mus_form.save()
            return redirect('home_page')
    else:
        return render(request,'add_muscian.html',{'form': mus_form})

    


