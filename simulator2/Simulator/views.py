from django.shortcuts import render
from django.http import HttpResponse
#from simulator2 import inferene as infer


def index(request):

    return render(request,'carhtml.html')


def ajaxrequest(request):

    #df = pd.read_csv('output.csv')
    #df.iat[0,0]
    f = open("simulator2/eyestatus.txt","r")
    csv = f.readline()
    f.close()
    print(csv)
    return HttpResponse(csv)