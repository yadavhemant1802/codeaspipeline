from os import *
from sys import *
import pandas as pd
import numpy as np
import csv
import orionsdk
import requests
import xlxswriter
import stmp
import time
list=[]
with open("employee_data1", 'r') as readFile: 
    data = csv.reader(readFile)    
    next(data)  
    for d in data:  
		name=d[0] 
		dept=d[1]
		dob=d[2] 
		address=d[3]
		
		list.append(name)
		list.append(ept)
		list.append(dob)
		list.append(address)
columns=["Name","Department","Date Of Birth","Address"]
 
with open("Writing_File",'w') as file:
	writer=csv.writer(file)
	writer.writerow(columns)
	writer.writerows(list)