from re import search
from django.shortcuts import render
from dashboard.models import Medicine
from .filters import CustomSearchMedicine

def index(request):
    return render(request, 'main/index.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')
    
def custom_search(request):
    medicines = Medicine.objects.all()
    myFilter = CustomSearchMedicine(request.GET, queryset=medicines)
    medicines = myFilter.qs
    for info in medicines:
        print(info.id)
    context = {'myFilter':myFilter, 'medicines':medicines}
    return render(request, 'main/custom_search.html', context)

def search(request):
    if request.method == 'POST': 
        searched = request.POST['searched']
        medicines = Medicine.objects.filter(medicine_name__contains=searched)

        if len(list(medicines)) == 0:
            searched = ''
 
        context = {'searched':searched, 'medicines':medicines}
        return render(request, 'main/search.html', context)
    else:
        context = {}
        return render(request, 'main/search.html', context)




def medicin_request(request):
    return render(request, 'main/medicin_request.html')



def login(request):
    return render(request, 'main/login.html')

def topics(request):
    return render(request, 'main/topics.html')