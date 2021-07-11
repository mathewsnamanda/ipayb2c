from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchapiForm
import http.client
import hashlib
import json

def contact(request):
    if request.method=="POST":
        form=SearchapiForm(request.POST)
        if form.is_valid():
            vid=form.cleaned_data['vid']
            reference=form.cleaned_data['reference']
            
            hash=""
            datatohash="vid="+str(vid)+"&reference="+str(reference)
            encoded=datatohash.encode()
            result = hashlib.sha256(encoded)
            result=result.hexdigest()
            hash=result
            
            dic={'vid':vid,'reference':reference,'hash':hash}
            jsonStr = json.dumps(dic)
            baseurl="apis.staging.ipayafrica.com/b2c/v3"
            conn = http.client.HTTPSConnection("apis.staging.ipayafrica.com")
            payload = jsonStr#"{\n\t\t\"vid\":\"demo\",\n\t\t\"reference\":\"demo\",\n        \"hash\":\"jnjdbfjdbfjd\"\n}"
            headers = {  'Content-Type': 'application/json','Cookie': 'PHPSESSID=f0d43802c3aad57106780cd732b2a18c'
}
            conn.request("POST", "/b2c/v3/transaction/status", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))

    form=SearchapiForm()
    return render(request,'form.html',{'form':form})
# Create your views here.
