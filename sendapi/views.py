from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SendapiForm
import http.client
import hashlib
import json

def contact(request):
    if request.method=="POST":
        form=SendapiForm(request.POST)
        if form.is_valid():
            vid=form.cleaned_data['vid']
            reference=form.cleaned_data['reference']
            phone=form.cleaned_data['phone']
            amount=form.cleaned_data['amount']
            hash=""
            datatohash="vid="+str(vid)+"&reference="+str(reference)+"&phone="+str(phone)+"&amount="+str(amount)
            encoded=datatohash.encode()
            result = hashlib.sha256(encoded)
            result=result.hexdigest()
            hash=result
            
            dic={'vid':vid,'reference':reference,'phone':phone,'amount':amount,'phone':phone,'hash':hash}
            jsonStr = json.dumps(dic)
            baseurl="apis.staging.ipayafrica.com"
            conn = http.client.HTTPSConnection(baseurl)
            payload = jsonStr
            headers = {'Content-Type': 'application/json'}
            conn.request("POST", "/b2c/v3/mobile/mpesa", payload, headers)
            res = conn.getresponse()
            data = res.read()
            responsed="sample"
            print(data.decode("utf-8"))

    form=SendapiForm()
    return render(request,'form.html',{'form':form})

# Create your views here.
