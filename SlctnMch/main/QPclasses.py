
from .QPTemplate import *

class Header:
    # exam=["Internal Assessment","Internal Assessment","Model Exam"]
    MONTH=[0,"January","February","March","April","May","June","July","August","September","October","November","December"]
    #branch=["CSE","EEE","ECE","IT","MECH","MCT","CSBS","AIDS","BME","CVL","S&H"]
    #Set=["A","B"]
    #marks=["50 Marks","100 Marks"]
    time=["1.30 hours","3 hours"]
    Year=[0,"I","II","III","IV"]
    Sem=[0,"I","II","III","IV","V","VI","VII","VIII"]
    H=[]
 

    def __init__(self,exam,date,subjcode,branch,Set,Year,Sem):
        self.H.append("Internal Assessment")#int 0,1,2 #self.exam[exam]
        self.H.append(exam+1) 
        tdData=date.split("/")
        self.H.append(tdData[0])
        self.H.append(self.MONTH[int(tdData[1])])
        self.H.append(date)
        self.H.append(subjcode)
      #  self.H.append(subjname)#str
        self.H.append(branch)
        self.H.append(Set) 
        if exam==0 or exam==1: 
           self.H.append("50 Marks") 
        elif exam==2:
           self.H.append("100 Marks")
        self.H.append(self.Year[Year]) 
        self.H.append(self.Sem[Sem]) 
   # 0 - "Internal Assessment",1 - IA- "1, 2 or 3", 2="date" , 3- "month", 4-"full date", 5- subjcode hc,
   # 6 - "branch" , 7 - Set, 8 - 50m or 100m, 9 - stud year, 10 - sem
class CourseObjectives:
    #only cobj column
    CObj=[]
    def __init__(self,C):
         for i in C:
             self.CObj.append(i)
    
class CourseOutcomes:
    #cout no and cout column list
    COut=[]
    def __init__(self,cout_code,cout):
        self.COut.append(cout_code)
        self.COut.append(cout)
    

class PartA:
    partA=[]
    def __init__(self,Qns,CO=[],BT_Level=[],Univ_QP_Reference=[]):
        self.partA.append(Qns)
        self.partA.append(CO)
        self.partA.append(BT_Level)
        self.partA.append(Univ_QP_Reference)

class PartB: 
    partB=[] 

    partB6a=[]
    partB6b=[]
    partB7a=[]
    partB7b=[]
    partB8a=[]
    partB8b=[]

    partB11a=[]
    partB11b=[]
    partB12a=[]
    partB12b=[]
    partB13a=[]
    partB13b=[]
    partB14a=[]
    partB14b=[]
    partB15a=[]
    partB15b=[]

    def PartB6a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB6a.append(Qns)
        PartB.partB6a.append(CO)
        PartB.partB6a.append(BT_Level)
        PartB.partB6a.append(Univ_QP_Reference)
        PartB.partB6a.append(mark_alloted)
        PartB.partB.append(PartB.partB6a)
    def PartB6b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB6b.append(Qns)
        PartB.partB6b.append(CO)
        PartB.partB6b.append(BT_Level)
        PartB.partB6b.append(Univ_QP_Reference)
        PartB.partB6b.append(mark_alloted)
        PartB.partB.append(PartB.partB6b)
    def PartB7a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB7a.append(Qns)
        PartB.partB7a.append(CO)
        PartB.partB7a.append(BT_Level)
        PartB.partB7a.append(Univ_QP_Reference)
        PartB.partB7a.append(mark_alloted)
        PartB.partB.append(PartB.partB7a)
    def PartB7b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB7b.append(Qns)
        PartB.partB7b.append(CO)
        PartB.partB7b.append(BT_Level)
        PartB.partB7b.append(Univ_QP_Reference)
        PartB.partB7b.append(mark_alloted)
        PartB.partB.append(PartB.partB7b)
    def PartB8a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB8a.append(Qns)
        PartB.partB8a.append(CO)
        PartB.partB8a.append(BT_Level)
        PartB.partB8a.append(Univ_QP_Reference)
        PartB.partB8a.append(mark_alloted)
        PartB.partB.append(PartB.partB8a)
    def PartB8b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB8b.append(Qns)
        PartB.partB8b.append(CO)
        PartB.partB8b.append(BT_Level)
        PartB.partB8b.append(Univ_QP_Reference)
        PartB.partB8b.append(mark_alloted)
        PartB.partB.append(PartB.partB8b)


    def PartB11a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB11a.append(Qns)
        PartB.partB11a.append(CO)
        PartB.partB11a.append(BT_Level)
        PartB.partB11a.append(Univ_QP_Reference)
        PartB.partB11a.append(mark_alloted)
        PartB.partB.append(PartB.partB11a)
    def PartB11b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB11b.append(Qns)
        PartB.partB11b.append(CO)
        PartB.partB11b.append(BT_Level)
        PartB.partB11b.append(Univ_QP_Reference)
        PartB.partB11b.append(mark_alloted)
        PartB.partB.append(PartB.partB11b)
    def PartB12a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB12a.append(Qns)
        PartB.partB12a.append(CO)
        PartB.partB12a.append(BT_Level)
        PartB.partB12a.append(Univ_QP_Reference)
        PartB.partB12a.append(mark_alloted)
        PartB.partB.append(PartB.partB12a)
    def PartB12b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB12b.append(Qns)
        PartB.partB12b.append(CO)
        PartB.partB12b.append(BT_Level)
        PartB.partB12b.append(Univ_QP_Reference)
        PartB.partB12b.append(mark_alloted)
        PartB.partB.append(PartB.partB12b)
    def PartB13a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB13a.append(Qns)
        PartB.partB13a.append(CO)
        PartB.partB13a.append(BT_Level)
        PartB.partB13a.append(Univ_QP_Reference)
        PartB.partB13a.append(mark_alloted)
        PartB.partB.append(PartB.partB13a)
    def PartB13b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB13b.append(Qns)
        PartB.partB13b.append(CO)
        PartB.partB13b.append(BT_Level)
        PartB.partB13b.append(Univ_QP_Reference)
        PartB.partB13b.append(mark_alloted)
        PartB.partB.append(PartB.partB13b)
    def PartB14a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB14a.append(Qns)
        PartB.partB14a.append(CO)
        PartB.partB14a.append(BT_Level)
        PartB.partB14a.append(Univ_QP_Reference)
        PartB.partB14a.append(mark_alloted)
        PartB.partB.append(PartB.partB14a)
    def PartB14b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB14b.append(Qns)
        PartB.partB14b.append(CO)
        PartB.partB14b.append(BT_Level)
        PartB.partB14b.append(Univ_QP_Reference)
        PartB.partB14b.append(mark_alloted)
        PartB.partB.append(PartB.partB14b)
    def PartB15a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB15a.append(Qns)
        PartB.partB15a.append(CO)
        PartB.partB15a.append(BT_Level)
        PartB.partB15a.append(Univ_QP_Reference)
        PartB.partB15a.append(mark_alloted)
        PartB.partB.append(PartB.partB15a)
    def PartB15b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        PartB.partB15b.append(Qns)
        PartB.partB15b.append(CO)
        PartB.partB15b.append(BT_Level)
        PartB.partB15b.append(Univ_QP_Reference)
        PartB.partB15b.append(mark_alloted)
        PartB.partB.append(PartB.partB15b)
  
    #if 50m, part c available - 2 qns with coice , 2 set of 2 8m(2-16m) and 1 8m all choice
    #if part c is available then 5 qns total 13 mark, choice is available for each qn, subdivision on each choice question is variable

class PartC: 

   # 50m - 1 16m , 100m - 1 15m
    # 1 qn total 15 mark, choice is available, subdivision is a variable for each question
    partC=[]
    partCa=[]
    partCb=[]
    
    def __init__(self,yn):
        self.partC.append(yn)

    def a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
        
     if PartC.partC[0]==1:
        PartC.partCa.append(Qns)
        PartC.partCa.append(CO)
        PartC.partCa.append(BT_Level)
        PartC.partCa.append(Univ_QP_Reference)
        PartC.partCa.append(mark_alloted)
        PartC.partC.append(PartC.partCa)

    def b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):

     if PartC.partC[0]==1:
        PartC.partCb.append(Qns)
        PartC.partCb.append(CO)
        PartC.partCb.append(BT_Level)
        PartC.partCb.append(Univ_QP_Reference)
        PartC.partCb.append(mark_alloted)
        PartC.partC.append(PartC.partCb)

class saveAs: pass
#def createQP

class Engrave:

   def header(exam,date,subjcode,branch,Set,Year,Sem) :
    Header(exam,date,subjcode,branch,Set,Year,Sem)

#Course Objectives-----------------------------------------------------------------------------------------------
   def courseObjectives(c):
    CourseObjectives(c)

#Course outcomes-------------------------------------------------------------------------------------------------
   def courseOutcomes(cout_code,cout):
    CourseOutcomes(cout_code,cout)

#Part A----------------------------------------------------------------------------------------------------------
   def partA(Qns,CO,BT_Level,Univ_QP_Reference):
    PartA(Qns,CO,BT_Level,Univ_QP_Reference)

#Part B---------------------------------------------------------------------------------------------------------- 
   #50 marks with part c
   def PartB6a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB6a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB6b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB6b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB7a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB7a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB7b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB7b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)

   #50 marks and no Part C
   def PartB8a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB8a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB8b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB8b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   
   #100 marks
   def PartB11a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB11a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB11b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB11b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB12a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB12a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB12b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB12b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB13a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB13a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB13b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB13b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB14a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB14a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB14b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB14b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB15a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB15a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def PartB15b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartB.PartB15b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   
#Part C----------------------------------------------------------------------------------------------------------
   
   def partc_is_available(yn):
       PartC(yn)
   def partCa(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartC.a(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)
   def partCb(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted):
       PartC.b(Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted)

class Create: 
    docx=[]
    def __init__(self): #to create template
       Data(Header.H,CourseObjectives.CObj,CourseOutcomes.COut,PartA.partA,PartB.partB,PartC.partC)
      
       pass

