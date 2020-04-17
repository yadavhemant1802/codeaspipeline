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

lisst=[]
with open("employee_data1", 'r') as readFilecsv: 
    data = csv.reader(readFilecsv)    
    next(data)  
    for d in data:  
		name=d[0] 
		dept=d[1]
		dob=d[2] 
		address=d[3]
		
		lisst.append(name)
		lisst.append(dept)
		lisst.append(dob)
		lisst.append(address)
columns=["Name","Department","Date Of Birth","Address"]
 
with open("Writing_File",'w') as filewritess:
	writer=csv.writer(filewritess)
	writer.writerow(columns)
	writer.writerows(list)