import json
from django.http.response import Http404, JsonResponse
from rest_framework import generics, views
from .models import Document, Item
from .serializers import  DocumentSerializer, ItemSerializer
import cv2
import numpy as np
import face_recognition
import functools
from django.core import serializers


from pathlib import Path
BASE_ = Path(__file__).resolve().parent.parent

import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen  

from django.shortcuts import render, redirect
from .models import Item 
from PIL import Image
    
    
class data(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class doc(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class  = DocumentSerializer

class docEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class  = DocumentSerializer
    
class docProceed(views.APIView):
    def get(self, request, pk, format=None):
        if True:
            item = Document.objects.get(pk=pk)
            image = np.asarray(bytearray(item.docfile.read()), dtype="uint8")
            image_encode = cv2.imdecode(image, cv2.IMREAD_COLOR)
            imgS = cv2.cvtColor(image_encode, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
            encodeFace  = encodesCurFrame[0]
            data = Item.objects.get(pk=pk)
            data.encodings = encodeFace.tolist()
            data.save()
            
            curritem = Item.objects.get(pk=pk)
            encodeFace = np.array(curritem.encodings)
            encodeListKnown = getEncodings(pk)      
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            indexes = np.argwhere(faceDis <= 0.44)

            encodeListKnown = np.array(encodeListKnown)
            result = {}
            print(faceDis)
            print(indexes,'here')
            if len(indexes)==0:
                result['head'] = {'found':0}
            else:
                result['head'] = {'found':len(indexes)}
                l = []
                for i in indexes:
                    matchedEncodings = encodeListKnown[i][0]
                    items = Item.objects.exclude(id=pk)
                    for it in items:
                        t = it.encodings
                        if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,t,matchedEncodings), True): 
                            g = {'name':it.name,'phone':str(it.phone),'location':it.location}
                            l.append(g)
                    result['body'] = l
                    # break
            print(result)           
        # except Exception as e:
        #     print('ERROR:::: ',e)
            # raise Http404
        return JsonResponse(result,safe=False)

def getEncodings(pk):
    encodings = []
    items = Item.objects.exclude(id=pk)
    for item in items:
        t = item.encodings
        t = np.array(t)
        encodings.append(t)
    return encodings