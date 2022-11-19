from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        get_description = request.POST.get('description').strip().strip('.')
        if request.POST.get('hiddenid'):
            data_id = request.POST.get('hiddenid')
            try:
                data = Todo.objects.get(id=data_id)
                if len(get_description) <= 5:
                    messages.warning(request,'Dostum,simvol sayi 5 dən cox olmalidir')
                    return redirect('home')
                if Todo.objects.filter(description=get_description).first():
                    messages.warning(request,'Hey,bu planını əvvəlcədən əlavə etmisən !')
                    return redirect('home')
                data.description = get_description
                data.save()
                messages.success(request,'Planın uğurla yeniləndi :)')
            except:
                pass
        else:
            if len(get_description) <= 5:
                messages.warning(request,'Dostum,simvol sayi 5 dən cox olmalidir')
            else:
                if Todo.objects.filter(description=get_description).first():
                    messages.warning(request,'Hey,bu planını əvvəlcədən əlavə etmisən !')
                else:
                    new_todo = Todo(description = get_description)
                    new_todo.save()
                    messages.success(request,'Afərin,planın uğurla əlavə olundu')
        
    data = {
        'todos':Todo.objects.all()
    }
    return render(request,'index.html',context=data)


def delete(request,id):
    try:
        data = Todo.objects.get(id=id)
        data.delete()
        messages.success(request,'Planın uğurla silindi')
    except:
        messages.error('Eh yox, sistemdə nəsə bir xəta baş verdi :( ')
        
    return redirect ('home')

def deleteAll(request):
    count = Todo.objects.all().count()
    if count > 0:
        Todo.objects.all().delete()
    messages.success(request,f'Deyəsən günlüy planlarını bitirmisən,{count} sayda element silindi')
    return redirect ('home')