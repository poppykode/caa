"""
Definition of Paynow views.
"""
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http.response import JsonResponse
import json
from .models import *
from django.core import serializers
import sys
import pprint
import hashlib
import requests
import urllib 
# from urllib import urlencode
import urllib.parse
from urllib.parse import urlencode
# from urlparse import urlparse
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import time

decorators = [never_cache, csrf_exempt]

@method_decorator(decorators, name='dispatch')
class ResultView(generic.View):

    def post(self, request):
        """
        This is the return function. The paynow system sends a request to this function
        through a result url. The url pointing to this action is defined in the request to
        https://www.paynow.co.zw/Interface/Initiatetransaction. This can be seen in the paynow docs.
        The paynow docs indicate that the data for a result for a transaction comes to this url.
        """
        integration_key = "5a56dc44-f36d-43c5-9f72-5e60ad5141f9"
        integration_id = 2891
        amount = float(request.POST["amount"])
        reference = request.POST["reference"]
        status = request.POST["status"]
        pollurl = request.POST["pollurl"]
        paynowreference = request.POST["paynowreference"]

        #skipping hash check for now
        print ("user has returned")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(request.POST)

        try:
            ut = Transaction.objects.get(reference=reference)
        except:
            resp = {"Couldn't find matching transaction"}
        else:
            if status == "Paid":
                ut.status = True
            else:
                ut.status = False

            print (status)

            ut.pollurl = pollurl
            ut.paynowreference = paynowreference
            ut.save()

            resp = {"Update successfull"}

        return JsonResponse(resp, status=200, safe=False)


@method_decorator(decorators, name='dispatch')
class PayNowView(generic.View):
    """ API implementation for paynow link """
    host = "localhost"
    port = "8000"

    def get(self, request):
        #if get variables not set do not proceed
        try:
            amount = request.GET["amount"]
            reference = request.GET["reference"]
            returnurl = request.GET["returnurl"]
            phone = request.GET["phone"]
            email = request.GET["email"]
            student_number = request.GET["student_number"]
        except:
            resp = {"error": "Problem with transaction details"}
            return

        integration_key = "5a56dc44-f36d-43c5-9f72-5e60ad5141f9"
        integration_id = 2891
        url = "https://www.paynow.co.zw/Interface/Initiatetransaction"

        def CreateMsg(values, merchantkey):
            values["hash"] = CreateHash(values, merchantkey)

            return values

        def CreateHash(values, merchantkey):
            string = ""
            for value in values:
                string += str(values[value])
            string += merchantkey
            #print string
            string = str(string).encode('utf-8')
            print ("string hashed")
            hash_object = hashlib.sha512(string)
            hash = hash_object.hexdigest()
            return hash.upper()

        def ParseMsg(msg):
            parts = msg.split("&")
            result = {}
            for part in parts:
                bits = part.split("=")
                result[ bits[0] ] = urllib.parse.unquote(bits[1])
            return result

        data = {
            "id": integration_id,
            "reference": reference,
            "amount": amount,
            "returnurl": returnurl,
            "resulturl": "http://%s:%s/paynow/result/" % (self.host, self.port),
            "status": "Message",
        }

        fulldata = CreateMsg(data, integration_key)
        print (fulldata)

        r = requests.post(url, data = fulldata)
        print ("request successfull")
        print (r.text)

        result = ParseMsg(r.text)
        print (result)
        print (CreateHash(result, integration_key))

        #skipped a hash check here for now
        if result["status"] == "Ok":
            try:
                pass
            except:
                resp = {"error": "Problem with the product details"}
                return
            else:
                resp = {"success": True, "url": result["browserurl"]}
                Transaction.objects.create(
                    reference=reference,
                    amount=amount,
                    requesting_number=phone,
                    email=email,
                    student_number = student_number,
                    status=True,
                )
        else:
            resp = {"error": "Status error"}
        print(resp) 
        return JsonResponse(resp, status=200, safe=False)