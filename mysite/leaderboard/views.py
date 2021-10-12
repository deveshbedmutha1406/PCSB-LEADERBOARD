from django.shortcuts import render
from numpy import empty
from numpy.lib.polynomial import polyint
from numpy.lib.utils import safe_eval
import pandas as pd
from .models import Leader,Attendace
from django.core.files.storage import FileSystemStorage
# Create your views here.

def score(request):

    d1 = {} # d1 is having key value pairs

    data = Leader.objects.all()  # bring all student data.

    for objects in data:
        d1[objects.name] = objects.points
    print(d1)
    context = {
        "dict":d1
    }

    return render(request, 'leaderboard/score.html', context)


def main(request):
    # taking form from front end file
    if request.method == "POST":
        # for programmers sake
        print('file uploaded')
        uploadedfile = request.FILES['document']
        print(uploadedfile)
        print(uploadedfile.name)
        print(uploadedfile.size)

        # using django file storage for that set path

        fs = FileSystemStorage()
        # created object and then save file
        name_of_file = fs.save(uploadedfile.name, uploadedfile)
        url = fs.url(name_of_file)  # gives us path to access reaad

        # code to read csv file
        data = pd.read_csv(url)
        name=data["Name"]
        n_list=[]
        for i in name:
            n_list.append(i)
        print(n_list)

        # code to check name and if found increment points else create new entry
        for ele in n_list:

            z = Leader.objects.filter(name=ele)
            print(z)
            print(z.exists())

            # if name already present
            if z.exists():
                print("if part")
                for item in z:
                    # access object and increment points
                    item.points += 10
                    print(item.points)
                    
                    item.save()
            else:
                # if new name then create object and save.
                print("else part")
                m = Leader.objects.create(name=ele,points=0)
                m.save()

 

        # sorting of dicitoinary remaining.



    return render(request, 'leaderboard/main.html')


# trial downside code.
def home(request):

    b = Leader.objects.get(name='akhilesh')
    a = Leader(name='akhilesh',points=30)
    print(b.name)
    print(a.name)
    if b.name == a.name:
        print('repeated')  
        return render(request, 'leaderboard/home.html')
      
        
    read()
    return render(request, 'leaderboard/home.html')

def read():
    data = pd.read_csv("/Users/devesh/Downloads/PCSB/mysite/file/Demo_attendance .csv")
    name=data["Name"]
    n_list=[]
    for i in name:
        n_list.append(i)
    print(n_list)

    a = Leader.objects.all()    #give all object
    print(a)

    for temp in a:
        print(temp.name)
        print(temp.points)

    a = Leader.objects.get(name='person1')
    print(a.points)

        