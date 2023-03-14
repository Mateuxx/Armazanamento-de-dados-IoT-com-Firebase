# -*- coding: utf-8 -*-
"""alimentandoFirebase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DkFSKcWsT2YyVBKaFVkVMvUqln65N3cI
"""

#!pip install firebase
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from firebase import firebase
import datetime
import random
import time
import json
from testesprorasp import*
FB_URL="https://testemonit-b47a7-default-rtdb.firebaseio.com"

def feedFb(dtype, valor):
    global FB_URL
    firebaseApp = firebase.FirebaseApplication(FB_URL, None)
  
    data = {dtype: valor,
            'time_created': datetime.datetime.now()}
    result = firebaseApp.post('/PAI/Sensor/'+dtype+'/', data)
    print("Firebase post result: \n\t")
    print(result)

    time.sleep(5)

def feedFbLastRecord(device_name):
    global FB_URL
    lastRecord = consultaLastRecord(device_name)
    dataToSend = {}

    firebaseApp = firebase.FirebaseApplication(FB_URL, None)

    for v in lastRecord:
        dataToSend[v['DTYPE']] = v['VALUE']

    result = firebaseApp.put('/'+device_name+'/', name='LastRecord', data=dataToSend)
    print("Firebase post result: \n\t")
    print(result)



    
