# IED
import textwrap
import MySQLdb
import math 
import sqlite3
conn = sqlite3.connect('usernames.db')
c = conn.cursor()

from operator import itemgetter
text=open('info.txt','r')
text.readline()

for line in text:
    fields=line.strip().split(' ')
    acceleration=sqrt(field[1]**field[2]**filed[3])
    if (acceleration >30):
        ang_acc=sqrt(field[4]**field[5]**filed[6])
        if (field[7]=="h"):
            newton=middle;
        from time import gmtime, strftime
        strftime("%Y.%m.%d %H:%M:%S", gmtime())
         
        delta t=.015
        j=float(acceleration)/float(delta_t)
        inverse=1/float(delta_t)
        h=(inverse*delta_a)**(5/2)
        hic=h*delta_t
        
       
        if hic <150 and acceleration <40 and  delta_a < 3187:
            percent= "<25%"
        if hic <=500 and hic >= 150 and acceleration <90 and acceleration >= 40 and ang_ac >=3187 and ang_ac < 106222:
            percent="25%-50%"
        if hic <= 1800 and  hic >= 500 and acceleration<171 and acceleration >= 90 and ang_acc >= and ang_acc < 10622:
            percent=">50%"
        #c.execute("INSERT INTO data VALUES (0,"Ben Wyatt","6 ft-2 in. 200 lb." ,"Quaterback", acceleration, ang_acc,%Y %m %d, %H:%M:%S, newton, percent, 3))
        conn.commit()
conn.close()
