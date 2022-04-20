# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:26:54 2021

@author: peiyi
"""

"""

IMPORTANT: READ FIRST

Welcome to the Virus Simulator!
when asked for input, input the following on their respective lines:
- Number of cells able to be killed by one virus
- How many new viruses produced by one virus
- The increment that viruses are produced
- The amount of nutrients needed to reproduce
- Name of the virus
- Number of starting cells
- Number of repetitions

Currently the Simulator includes:
- Growth
- Nutrients
- Random mutations
- Cell count
- Cell/Virus graph
- Overall stats

Statistics are displayed to the right -->

Warnings:
Mutations happen completely randomly. Some may result in strange results.
I am not responsible for any crashes of computers due to large repetition amounts/excessive input.
NOT FOR PROFESSIONAL USE

"""

import random
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import datetime as dt

class virus:
    def __init__(self,death,mult,inc,nutr,name):
        self.d=death #0
        self.m=mult #1
        self.i=inc #2
        self.n=nutr #3
        self.name=name #4
        self.count=500 #5
        self.time=1 #6
        self.mutations=0
    def stat(self,nutr):
        return self.d,self.m,self.i,self.n,self.name,self.count,self.time
    def tick(self,nutr):
        self.n+=100
        if self.n>=nutr and self.time>=self.i:
            self.count+=round(self.n/nutr)*self.m
            self.time=0
        if self.count>10000:
            self.count-=random.randint(500-50*self.mutations,1000-50*self.mutations)
        self.time+=1
    def change(self,death,mult,inc,nutr):
        self.d=death
        self.m=mult
        self.i=inc
        self.n=nutr
    def mutate(self):
        self.mutations+=1
        death=self.d+random.randint(-1,2)
        mult=self.m+random.randint(-1,2)
        inc=self.i+random.randint(-1,1)
        nutr=self.n+random.randint(round(-self.n/8),round(self.n/8))
        self.change(death,mult,inc,nutr)    

def vrun(p):
    death=int(input("Number of cells able to be killed by one virus: "))
    mult=int(input("Number of new viruses able to be produced by one virus: "))
    inc=int(input("Increment of reproduction: "))
    nutr=int(input("Nutrients needed for one reproduction: "))
    name=input("Name of virus: ")
    c=int(input("Starting cells (recommended <1M): "))
    cells=c
    x=virus(death,mult,inc,nutr,name)
    r=int(input("Rounds: "))
    n=1000
    clist=[]
    cellist=[]
    nutrlist=[]
    mutation_dates=[]
    day=0
    for i in range(r):
        day+=1
        x.tick(n)
        rint=random.randint(1,100)
        if rint==33:
            print("MUTATION IMMINENT")
            mutation_dates.append(day-2)
            x.mutate()
        tup=x.stat(n)
        cells-=(abs(tup[0]*tup[5]))
        if cells<=0:
            nutrlist.append(n)
            clist.append(abs(tup[5]))
            cellist.append(cells)
            data={
              "nutrients":nutrlist,
              "cells":cellist,
              "count":clist
            }
            df=pd.DataFrame(data)
            plt.plot(nutrlist,label="nutrient count")
            plt.plot(clist, label="virus count")
            plt.plot(cellist, label="cell count")
            plt.legend()
            plt.draw()
            plt.xlabel("days after outbreak")
            plt.ylabel("organism count")
            plt.title("Virus Visualization")
            print("__________________________")
            print("OVERALL STATS:")
            print(df.describe())
            print("Mutation Dates: "+str(mutation_dates))
            break
        cells+=random.randint(cells//101,cells//100)
        #population killer
		#if cells>=2500000:
           #cells-=random.randint(cells-50000,cells-20000)-random.randint(-500,500)
        n-=(tup[3]-random.randint(0,30))        
        if n<0:
            n=100
        print("------------------")
        print(name)
        print("count: "+str(abs(tup[5])))
        #print("timer: "+str(tup[6]))
        print("cells: "+str(cells))
        print("nutrients: "+str(n))
        nutrlist.append(n)
        clist.append(abs(tup[5])*10)
        cellist.append(cells)
    data={
      "nutrients":nutrlist,
      "cells":cellist,
      "count":clist
    }
    df=pd.DataFrame(data)
    plt.plot(nutrlist,label="nutrient count")
    plt.plot(clist, label="virus count")
    plt.plot(cellist, label="cell count")
    plt.legend()
    plt.draw()
    plt.xlabel("days after outbreak")
    plt.ylabel("organism count")
    plt.title("Virus Visualization")
    print("__________________________")
    print("OVERALL STATS:")
    print(df.describe())
    print("NOTE: Vertical scale exaggerated by 10x for virus count")
    plt.pause(p)
    plt.close()
    return

def menu():
	return (
    '''
		[--- Virus Simulator Beta 1.0 ---]
----------------------------------------------------------
	- 1 to simulate a new virus
	- 2 to access saved parameter sets
	- 3 to store a new parameter set 
	- 4 to write to personal notepad
	- 5 to read from personal notepad
	- g to access user guide
	- q to quit/logout
----------------------------------------------------------
    ''')


def interface(acc,p):
	if input("Press [enter] to continue")!="":
		return
	print(menu())
	opt=input("User Selection: ")
	if opt=="1":
		vrun(p)
	elif opt=="2":
		with open("VirusParameters.txt","r") as params:
			lines=params.readlines()
			for i in range(0,len(lines)):
				lines[i].strip("\n")
		ind=input("Index of desired parameter: ")
		param=-1
		for i in range(len(lines)):
			if lines[i]=="{a}\n".format(a=acc):
				param=lines[i+int(ind)+1]
				break
		if param==-1:
			print("No such parameter exists.")
		print("Saved parameters: "+param)
	elif opt=="3":
		text=input("Parameters to save: ")
		with open("VirusParameters.txt","r") as params:
			lines=params.readlines()
			for i in range(len(lines)):
				if lines[i]=="{a}\n".format(a=acc):
					loc=i
		lines[loc]=lines[loc]+text+"\n"
		with open("VirusParameters.txt","w") as params:
			params.writelines(lines)
	elif opt=="4":
		text=input("Notes to record: ")
		with open("VirusNotes.txt","r") as notes:
			lines=notes.readlines()
			for i in range(len(lines)):
				if lines[i]=="{a}\n".format(a=acc):
					loc=i
		lines[loc]=lines[loc]+text+"\n"
		with open("VirusNotes.txt","w") as notes:
			notes.writelines(lines)
	elif opt=="5":
		with open("VirusNotes.txt","r") as params:
			lines=params.readlines()
			for i in range(0,len(lines)):
				lines[i].strip("\n")
		ind=input("Index of desired note: ")
		param=-1
		for i in range(len(lines)):
			if lines[i]=="{a}\n".format(a=acc):
				param=lines[i+int(ind)+1]
				break
		if param==-1:
			print("No such note exists.")
		print("Saved parameters: "+param)
	elif opt=="g":
		print("Virus Simulator User Guide")
		if input("Press [enter] to continue")!="":
			return
		print("WIP, download latest version for update.")
	elif opt=="q":
		return
	else:
		print("Invalid selection.")
	return interface(acc,p)
		
def startup(username,password):
	with open("Saved Logins.txt","r") as logs:
		if "{x}, {y}".format(x=username, y=password) in logs.read():
			print("Login Success. User "+username+" was successfully logged in at "+str(dt.datetime.now()))
		else:
			print("Login failure, incorrect username or password")
			return 
	p=int(input("Pause time after simulation display (seconds): "))
	interface(username,p)
	
	