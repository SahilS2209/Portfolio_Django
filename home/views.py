from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        
        ins = Contact(name=name, email=email, phone=phone, desc=desc) # take the data from the user
        ins.save() # save it in the db
        print("The data has been saved to the database")
        
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')