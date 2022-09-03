from .QPclasses import Engrave
from .QPclasses import Create
from .models import Details,Questions

# def req():

#         partb6a=["Write the charcteristics CIT Logo Simple -   an algoritm. logo1.png   "]
#         Engrave.PartB6a(partb6a,cout_code,BTlvl,cout_code,cout_code)
#         partb6b=["Write the charcteristics CIT Logo Simple -   an algoritm. logo1.png   ","Write the charcteristics CIT Logo Simple -   an algoritm. logo1.png   "]
#         Engrave.PartB6b(partb6b,cout_code,BTlvl,cout_code,["10","2"])
#         partb7a=["Explain Asymptomatic Notations"]
#         Engrave.PartB7a(partb7a,cout_code,BTlvl,cout_code,["12"])
#         partb7b=["Illustrate mathematical Analysis on recursive Algorithms"]
#         Engrave.PartB7b(partb7b,cout_code,BTlvl,cout_code,["12"])

#         Engrave.PartB8a(CourseObjectives,cout_code,BTlvl,cout_code,cout_code)
#         Engrave.PartB8b(CourseObjectives,cout_code,BTlvl,cout_code,cout_code)

#         partca=["Write the Asymptomatic notationsused for worst-case,best-case and the average case analysis of algorithms. Write an algorithm for sequential search. Give worst-case, best-case and average case complexities."]

#         Engrave.partCa(partca,cout_code,BTlvl,cout_code,["16"])
#         partcb=["Write the charcteristics of an algoritm."]
#         Engrave.partCb(partcb,cout_code,BTlvl,cout_code,["16"])

#         Create()

def Exec(s):
                from random import sample 
                
                # IAexam(1,2,3),fdate,subcode,branch,Set,studYear,semester
                IAexam=0
                fdate="1/4/2022"
                subc="CS8967"
                branch="CSE/IT/CSBS"
                studYear=1
                studSem=2
                units=["1"]
                partc=1
           # if IA= 0 - 1 unit selected, = 1 - 2 unit selected, = 3 - all 5 unit

                if IAexam==0:
                        subdet=Details.objects.filter(subcode=subc).values()
                        CourseObjectives=[]
                        for i in range(1,8):
                           if  str(subdet[0]["cobj"+str(i)])!="NA":
                              CourseObjectives.append(str(subdet[0]["cobj"+str(i)]))
                        cout_code=[]
                        for i in range(1,6):
                           if  str(subdet[0]["cno"+str(i)])!="NA":
                              cout_code.append(str(subdet[0]["cno"+str(i)]))
                        cout=[]
                        for i in range(1,6):
                           if  str(subdet[0]["co"+str(i)])!="NA":
                              cout.append(str(subdet[0]["co"+str(i)]))
                        Engrave.header(IAexam,fdate,subc,branch,s,studYear,studSem)
                        Engrave.courseObjectives(CourseObjectives)
                        Engrave.courseOutcomes(cout_code,cout)
                        Engrave.partc_is_available(partc)

                        marks2=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="2").values()
                        partA=[]
                        CO2=[]
                        BT_Level2=[]
                        Univ_QP_Reference2=[]
                        selctd2=sample(list(marks2),5)
                        for k in selctd2:
                                if k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]!="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~"+" "+"~~$"+k["Qnimg3"]+"~~")
                                elif k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~")
                                elif  k["Qnimg1"]!="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~")
                                elif  k["Qnimg1"]=="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"])
                                else : partA.append(k["Qn"])
                                CO2.append(k["CO"])
                                BT_Level2.append(k["BT_Level"])
                                Univ_QP_Reference2.append(k["Univ_QP_Reference"])
                        Engrave.partA(partA,CO2,BT_Level2,Univ_QP_Reference2)
                        
                        if partc==1:
                                splitup13=[["7","6"],["8","5"],["9","4"],["10","3"],["13"]]
                                qn6aSpltUp=sample(splitup13,1)
                                qn6bSpltUp=sample(splitup13,1)
                                qn7aSpltUp=sample(splitup13,1)
                                qn7bSpltUp=sample(splitup13,1)
                                splitup15=[["8","7"],["10","5"],["9","6"],["15"]]
                                qn8aSpltUp=sample(splitup15,1)
                                qn8bSpltUp=sample(splitup15,1)
                                m3=0
                                m4=0
                                m5=0
                                m6=0
                                m7=0
                                m8=0
                                m9=0
                                m10=0
                                m13=0
                                m15=0
                                partb6a=[]
                                partb6b=[]
                                partb7a=[]
                                partb7b=[]
                                partc8a=[]
                                partc8b=[]
                                
#-----------------------------------------------------------6a-----------------                          
                                if  qn6aSpltUp[0][0]=="7":
                                        m7+=1
                                        m6+=1
                                elif qn6aSpltUp[0][0]=="8":
                                        m8+=1
                                        m5+=1
                                elif qn6aSpltUp[0][0]=="9":
                                        m9+=1
                                        m4+=1
                                elif qn6aSpltUp[0][0]=="10":
                                        m10+=1
                                        m3+=1
                                elif qn6aSpltUp[0][0]=="13":
                                        m13+=1
#-------------------------------------------------------------6b----------------
                                if  qn6bSpltUp[0][0]=="7":
                                        m7+=1
                                        m6+=1
                                elif qn6bSpltUp[0][0]=="8":
                                        m8+=1
                                        m5+=1
                                elif qn6bSpltUp[0][0]=="9":
                                        m9+=1
                                        m4+=1
                                elif qn6bSpltUp[0][0]=="10":
                                        m10+=1
                                        m3+=1
                                elif qn6bSpltUp[0][0]=="13":
                                        m13+=1
#--------------------------------------------------------------7a-----------------
                                if  qn7aSpltUp[0][0]=="7":
                                        m7+=1
                                        m6+=1
                                elif qn7aSpltUp[0][0]=="8":
                                        m8+=1
                                        m5+=1
                                elif qn7aSpltUp[0][0]=="9":
                                        m9+=1
                                        m4+=1
                                elif qn7aSpltUp[0][0]=="10":
                                        m10+=1
                                        m3+=1
                                elif qn7aSpltUp[0][0]=="13":
                                        m13+=1
#---------------------------------------------------------------7b----------------
                                if  qn7bSpltUp[0][0]=="7":
                                        m7+=1
                                        m6+=1
                                elif qn7bSpltUp[0][0]=="8":
                                        m8+=1
                                        m5+=1
                                elif qn7bSpltUp[0][0]=="9":
                                        m9+=1
                                        m4+=1
                                elif qn7bSpltUp[0][0]=="10":
                                        m10+=1
                                        m3+=1
                                elif qn7bSpltUp[0][0]=="13":
                                        m13+=1
#----------------------------------------------------------------8a---------------- partc-----------
                                if  qn8aSpltUp[0][0]=="8":
                                        m8+=1
                                        m7+=1
                                elif qn8aSpltUp[0][0]=="9":
                                        m9+=1
                                        m6+=1
                                elif qn8aSpltUp[0][0]=="10":
                                        m10+=1
                                        m5+=1
                                elif qn8aSpltUp[0][0]=="15":
                                        m15+=1
#----------------------------------------------------------------8b---------------- partc-----------
                                if  qn8bSpltUp[0][0]=="8":
                                        m8+=1
                                        m7+=1
                                elif qn8bSpltUp[0][0]=="9":
                                        m9+=1
                                        m6+=1
                                elif qn8bSpltUp[0][0]=="10":
                                        m10+=1
                                        m5+=1
                                elif qn8bSpltUp[0][0]=="15":
                                        m15+=1
                                
                                mark3=0
                                mark4=0
                                mark5=0
                                mark6=0
                                mark7=0
                                mark8=0
                                mark9=0
                                mark10=0
                                mark13=0
                                mark15=0

                                if m3!=0:
                                        mark3=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="3").values()
                                if m4!=0:        
                                        mark4=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="4").values()
                                if m5!=0:
                                        mark5=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="5").values()
                                if m6!=0:
                                        mark6=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="6").values()
                                if m7!=0:
                                        mark7=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="7").values()
                                if m8!=0:
                                        mark8=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="8").values()
                                if m9!=0:
                                        mark9=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="9").values()
                                if m10!=0:
                                        mark10=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="10").values()
                                if m13!=0:
                                        mark13=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="13").values()
                                if m15!=0:
                                        mark15=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="15").values()
                                
                                smark3=0
                                smark4=0
                                smark5=0
                                smark6=0
                                smark7=0
                                smark8=0
                                smark9=0
                                smark10=0
                                smark13=0
                                smark15=0

                                if m3!=0:
                                        smark3=sample(list(mark3),m3)
                                if m4!=0:        
                                        smark4=sample(list(mark4),m4)
                                if m5!=0:
                                        smark5=sample(list(mark5),m5)
                                if m6!=0:
                                        smark6=sample(list(mark6),m6)
                                if m7!=0:
                                        smark7=sample(list(mark7),m7)
                                if m8!=0:
                                        smark8=sample(list(mark8),m8)
                                if m9!=0:
                                        smark9=sample(list(mark9),m9)
                                if m10!=0:
                                        smark10=sample(list(mark10),m10)
                                if m13!=0:
                                        smark13=sample(list(mark13),m13)
                                if m15!=0:
                                        smark15=sample(list(mark15),m15)                                
                                
#---------------------------------------------------------------------PART B 6A --------------------------------------------------------------------------------------------------------------------------                  
                                if  qn6aSpltUp[0][0]=="7":
                                       m7=m7-1
                                       m=m7
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark7[m]["Qn"])
                                       else : partb6a.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark6[m]["Qn"])
                                       else : partb6a.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.PartB6a(partb6a,CO,BT_Level,Univ_QP_Reference,qn6aSpltUp[0])
                                elif qn6aSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark8[m]["Qn"])
                                       else : partb6a.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark5[m]["Qn"])
                                       else : partb6a.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.PartB6a(partb6a,CO,BT_Level,Univ_QP_Reference,qn6aSpltUp[0])
                                elif qn6aSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark9[m]["Qn"])
                                       else : partb6a.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m4=m4-1
                                       m=m4
                                       if smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~"+" "+"~~$"+smark4[m]["Qnimg3"]+"~~")
                                       elif smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~")
                                       elif  smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~")
                                       elif  smark4[m]["Qnimg1"]=="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark4[m]["Qn"])
                                       else : partb6a.append(smark4[m]["Qn"])
                                       CO.append(smark4[m]["CO"])
                                       BT_Level.append(smark4[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark4[m]["Univ_QP_Reference"])
                                       Engrave.PartB6a(partb6a,CO,BT_Level,Univ_QP_Reference,qn6aSpltUp[0])
                                elif qn6aSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark10[m]["Qn"])
                                       else : partb6a.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m3=m3-1
                                       m=m3
                                       if smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~"+" "+"~~$"+smark3[m]["Qnimg3"]+"~~")
                                       elif smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~")
                                       elif  smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~")
                                       elif  smark3[m]["Qnimg1"]=="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark3[m]["Qn"])
                                       else : partb6a.append(smark3[m]["Qn"])
                                       CO.append(smark3[m]["CO"])
                                       BT_Level.append(smark3[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark3[m]["Univ_QP_Reference"])
                                       Engrave.PartB6a(partb6a,CO,BT_Level,Univ_QP_Reference,qn6aSpltUp[0])
                                elif qn6aSpltUp[0][0]=="13":
                                       m13=m13-1
                                       m=m13
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]!="NA":
                                        partb6a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~"+" "+"~~$"+smark13[m]["Qnimg3"]+"~~")
                                       elif smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~")
                                       elif  smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~")
                                       elif  smark13[m]["Qnimg1"]=="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6a.append(smark13[m]["Qn"])
                                       else : partb6a.append(smark13[m]["Qn"])
                                       CO.append(smark13[m]["CO"])
                                       BT_Level.append(smark13[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark13[m]["Univ_QP_Reference"])
                                       Engrave.PartB6a(partb6a,CO,BT_Level,Univ_QP_Reference,qn6aSpltUp[0])
                                

#--------------------------------------------------------------------------------------------------PART B 6B---------------------------------------------------------------

                                if  qn6bSpltUp[0][0]=="7":
                                       m7=m7-1
                                       m=m7
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark7[m]["Qn"])
                                       else : partb6b.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark6[m]["Qn"])
                                       else : partb6b.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.PartB6b(partb6b,CO,BT_Level,Univ_QP_Reference,qn6bSpltUp[0])
                                elif qn6bSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark8[m]["Qn"])
                                       else : partb6b.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark5[m]["Qn"])
                                       else : partb6b.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.PartB6b(partb6b,CO,BT_Level,Univ_QP_Reference,qn6bSpltUp[0])
                                elif qn6bSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark9[m]["Qn"])
                                       else : partb6b.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m4=m4-1
                                       m=m4
                                       if smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~"+" "+"~~$"+smark4[m]["Qnimg3"]+"~~")
                                       elif smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~")
                                       elif  smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~")
                                       elif  smark4[m]["Qnimg1"]=="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark4[m]["Qn"])
                                       else : partb6b.append(smark4[m]["Qn"])
                                       CO.append(smark4[m]["CO"])
                                       BT_Level.append(smark4[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark4[m]["Univ_QP_Reference"])
                                       Engrave.PartB6b(partb6b,CO,BT_Level,Univ_QP_Reference,qn6bSpltUp[0])
                                elif qn6bSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark10[m]["Qn"])
                                       else : partb6b.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m3=m3-1
                                       m=m3
                                       if smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~"+" "+"~~$"+smark3[m]["Qnimg3"]+"~~")
                                       elif smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~")
                                       elif  smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~")
                                       elif  smark3[m]["Qnimg1"]=="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark3[m]["Qn"])
                                       else : partb6b.append(smark3[m]["Qn"])
                                       CO.append(smark3[m]["CO"])
                                       BT_Level.append(smark3[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark3[m]["Univ_QP_Reference"])
                                       Engrave.PartB6b(partb6b,CO,BT_Level,Univ_QP_Reference,qn6bSpltUp[0])
                                elif qn6bSpltUp[0][0]=="13":
                                       m13=m13-1
                                       m=m13
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]!="NA":
                                        partb6b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~"+" "+"~~$"+smark13[m]["Qnimg3"]+"~~")
                                       elif smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~")
                                       elif  smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~")
                                       elif  smark13[m]["Qnimg1"]=="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb6b.append(smark13[m]["Qn"])
                                       else : partb6b.append(smark13[m]["Qn"])
                                       CO.append(smark13[m]["CO"])
                                       BT_Level.append(smark13[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark13[m]["Univ_QP_Reference"])
                                       Engrave.PartB6b(partb6b,CO,BT_Level,Univ_QP_Reference,qn6bSpltUp[0])     

#----------------------------------------------------------------------------------------------PART B 7a--------------------------------------------------------------
                                
                                if  qn7aSpltUp[0][0]=="7":
                                       m7=m7-1
                                       m=m7
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark7[m]["Qn"])
                                       else : partb7a.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark6[m]["Qn"])
                                       else : partb7a.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.PartB7a(partb7a,CO,BT_Level,Univ_QP_Reference,qn7aSpltUp[0])
                                elif qn7aSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark8[m]["Qn"])
                                       else : partb7a.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark5[m]["Qn"])
                                       else : partb7a.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.PartB7a(partb7a,CO,BT_Level,Univ_QP_Reference,qn7aSpltUp[0])
                                elif qn7aSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark9[m]["Qn"])
                                       else : partb7a.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m4=m4-1
                                       m=m4
                                       if smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~"+" "+"~~$"+smark4[m]["Qnimg3"]+"~~")
                                       elif smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~")
                                       elif  smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~")
                                       elif  smark4[m]["Qnimg1"]=="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark4[m]["Qn"])
                                       else : partb7a.append(smark4[m]["Qn"])
                                       CO.append(smark4[m]["CO"])
                                       BT_Level.append(smark4[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark4[m]["Univ_QP_Reference"])
                                       Engrave.PartB7a(partb7a,CO,BT_Level,Univ_QP_Reference,qn7aSpltUp[0])
                                elif qn7aSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark10[m]["Qn"])
                                       else : partb7a.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m3=m3-1
                                       m=m3
                                       if smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~"+" "+"~~$"+smark3[m]["Qnimg3"]+"~~")
                                       elif smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~")
                                       elif  smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~")
                                       elif  smark3[m]["Qnimg1"]=="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark3[m]["Qn"])
                                       else : partb7a.append(smark3[m]["Qn"])
                                       CO.append(smark3[m]["CO"])
                                       BT_Level.append(smark3[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark3[m]["Univ_QP_Reference"])
                                       Engrave.PartB7a(partb7a,CO,BT_Level,Univ_QP_Reference,qn7aSpltUp[0])
                                elif qn7aSpltUp[0][0]=="13":
                                       m13=m13-1
                                       m=m13
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]!="NA":
                                        partb7a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~"+" "+"~~$"+smark13[m]["Qnimg3"]+"~~")
                                       elif smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~")
                                       elif  smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~")
                                       elif  smark13[m]["Qnimg1"]=="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7a.append(smark13[m]["Qn"])
                                       else : partb7a.append(smark13[m]["Qn"])
                                       CO.append(smark13[m]["CO"])
                                       BT_Level.append(smark13[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark13[m]["Univ_QP_Reference"])
                                       Engrave.PartB7a(partb7a,CO,BT_Level,Univ_QP_Reference,qn7aSpltUp[0])

#--------------------------------------------------------------------------------------------PART B 7b-------------------------------------------------------------------

                                if  qn7bSpltUp[0][0]=="7":
                                       m7=m7-1
                                       m=m7
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark7[m]["Qn"])
                                       else : partb7b.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark6[m]["Qn"])
                                       else : partb7b.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.PartB7b(partb7b,CO,BT_Level,Univ_QP_Reference,qn7bSpltUp[0])
                                elif qn7bSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark8[m]["Qn"])
                                       else : partb7b.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark5[m]["Qn"])
                                       else : partb7b.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.PartB7b(partb7b,CO,BT_Level,Univ_QP_Reference,qn7bSpltUp[0])
                                elif qn7bSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark9[m]["Qn"])
                                       else : partb7b.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m4=m4-1
                                       m=m4
                                       if smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~"+" "+"~~$"+smark4[m]["Qnimg3"]+"~~")
                                       elif smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]!="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~"+" "+"~~$"+smark4[m]["Qnimg2"]+"~~")
                                       elif  smark4[m]["Qnimg1"]!="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark4[m]["Qn"]+" "+"~~$"+smark4[m]["Qnimg1"]+"~~")
                                       elif  smark4[m]["Qnimg1"]=="NA" and smark4[m]["Qnimg2"]=="NA" and smark4[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark4[m]["Qn"])
                                       else : partb7b.append(smark4[m]["Qn"])
                                       CO.append(smark4[m]["CO"])
                                       BT_Level.append(smark4[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark4[m]["Univ_QP_Reference"])
                                       Engrave.PartB7b(partb7b,CO,BT_Level,Univ_QP_Reference,qn7bSpltUp[0])
                                elif qn7bSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark10[m]["Qn"])
                                       else : partb7b.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m3=m3-1
                                       m=m3
                                       if smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~"+" "+"~~$"+smark3[m]["Qnimg3"]+"~~")
                                       elif smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]!="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~"+" "+"~~$"+smark3[m]["Qnimg2"]+"~~")
                                       elif  smark3[m]["Qnimg1"]!="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark3[m]["Qn"]+" "+"~~$"+smark3[m]["Qnimg1"]+"~~")
                                       elif  smark3[m]["Qnimg1"]=="NA" and smark3[m]["Qnimg2"]=="NA" and smark3[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark3[m]["Qn"])
                                       else : partb7b.append(smark3[m]["Qn"])
                                       CO.append(smark3[m]["CO"])
                                       BT_Level.append(smark3[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark3[m]["Univ_QP_Reference"])
                                       Engrave.PartB7b(partb7b,CO,BT_Level,Univ_QP_Reference,qn7bSpltUp[0])
                                elif qn7bSpltUp[0][0]=="13":
                                       m13=m13-1
                                       m=m13
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]!="NA":
                                        partb7b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~"+" "+"~~$"+smark13[m]["Qnimg3"]+"~~")
                                       elif smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]!="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~"+" "+"~~$"+smark13[m]["Qnimg2"]+"~~")
                                       elif  smark13[m]["Qnimg1"]!="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark13[m]["Qn"]+" "+"~~$"+smark13[m]["Qnimg1"]+"~~")
                                       elif  smark13[m]["Qnimg1"]=="NA" and smark13[m]["Qnimg2"]=="NA" and smark13[m]["Qnimg3"]=="NA":
                                        partb7b.append(smark13[m]["Qn"])
                                       else : partb7b.append(smark13[m]["Qn"])
                                       CO.append(smark13[m]["CO"])
                                       BT_Level.append(smark13[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark13[m]["Univ_QP_Reference"])
                                       Engrave.PartB7b(partb7b,CO,BT_Level,Univ_QP_Reference,qn7bSpltUp[0])


#----------------------------------------------------------------------------------------------PART C 8a--------------------------------------------------------
                                
                                if  qn8aSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark8[m]["Qn"])
                                       else : partc8a.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m7=m7-1
                                       m=m7
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark7[m]["Qn"])
                                       else : partc8a.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       Engrave.partCa(partc8a,CO,BT_Level,Univ_QP_Reference,qn8aSpltUp[0])
                               
                                elif qn8aSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark9[m]["Qn"])
                                       else : partc8a.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark6[m]["Qn"])
                                       else : partc8a.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.partCa(partc8a,CO,BT_Level,Univ_QP_Reference,qn8aSpltUp[0])
                                elif qn8aSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark10[m]["Qn"])
                                       else : partc8a.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark5[m]["Qn"])
                                       else : partc8a.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.partCa(partc8a,CO,BT_Level,Univ_QP_Reference,qn8aSpltUp[0])
                                elif qn8aSpltUp[0][0]=="15":
                                       m15=m15-1
                                       m=m15
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]!="NA" and smark15[m]["Qnimg3"]!="NA":
                                        partc8a.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~"+" "+"~~$"+smark15[m]["Qnimg2"]+"~~"+" "+"~~$"+smark15[m]["Qnimg3"]+"~~")
                                       elif smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]!="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~"+" "+"~~$"+smark15[m]["Qnimg2"]+"~~")
                                       elif  smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]=="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~")
                                       elif  smark15[m]["Qnimg1"]=="NA" and smark15[m]["Qnimg2"]=="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8a.append(smark15[m]["Qn"])
                                       else : partc8a.append(smark15[m]["Qn"])
                                       CO.append(smark15[m]["CO"])
                                       BT_Level.append(smark15[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark15[m]["Univ_QP_Reference"])
                                       Engrave.partCa(partc8a,CO,BT_Level,Univ_QP_Reference,qn8aSpltUp[0])

#----------------------------------------------------------------------------------------------------------PART C 8b-----------------------------------------------

                                if  qn8bSpltUp[0][0]=="8":
                                       m8=m8-1
                                       m=m8
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~"+" "+"~~$"+smark8[m]["Qnimg3"]+"~~")
                                       elif smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]!="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~"+" "+"~~$"+smark8[m]["Qnimg2"]+"~~")
                                       elif  smark8[m]["Qnimg1"]!="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark8[m]["Qn"]+" "+"~~$"+smark8[m]["Qnimg1"]+"~~")
                                       elif  smark8[m]["Qnimg1"]=="NA" and smark8[m]["Qnimg2"]=="NA" and smark8[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark8[m]["Qn"])
                                       else : partc8b.append(smark8[m]["Qn"])
                                       CO.append(smark8[m]["CO"])
                                       BT_Level.append(smark8[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark8[m]["Univ_QP_Reference"])
                                       m7=m7-1
                                       m=m7
                                       if smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~"+" "+"~~$"+smark7[m]["Qnimg3"]+"~~")
                                       elif smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]!="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~"+" "+"~~$"+smark7[m]["Qnimg2"]+"~~")
                                       elif  smark7[m]["Qnimg1"]!="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark7[m]["Qn"]+" "+"~~$"+smark7[m]["Qnimg1"]+"~~")
                                       elif  smark7[m]["Qnimg1"]=="NA" and smark7[m]["Qnimg2"]=="NA" and smark7[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark7[m]["Qn"])
                                       else : partc8b.append(smark7[m]["Qn"])
                                       CO.append(smark7[m]["CO"])
                                       BT_Level.append(smark7[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark7[m]["Univ_QP_Reference"])
                                       Engrave.partCb(partc8b,CO,BT_Level,Univ_QP_Reference,qn8bSpltUp[0])
                               
                                elif qn8bSpltUp[0][0]=="9":
                                       m9=m9-1
                                       m=m9
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~"+" "+"~~$"+smark9[m]["Qnimg3"]+"~~")
                                       elif smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]!="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~"+" "+"~~$"+smark9[m]["Qnimg2"]+"~~")
                                       elif  smark9[m]["Qnimg1"]!="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark9[m]["Qn"]+" "+"~~$"+smark9[m]["Qnimg1"]+"~~")
                                       elif  smark9[m]["Qnimg1"]=="NA" and smark9[m]["Qnimg2"]=="NA" and smark9[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark9[m]["Qn"])
                                       else : partc8b.append(smark9[m]["Qn"])
                                       CO.append(smark9[m]["CO"])
                                       BT_Level.append(smark9[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark9[m]["Univ_QP_Reference"])
                                       m6=m6-1
                                       m=m6
                                       if smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~"+" "+"~~$"+smark6[m]["Qnimg3"]+"~~")
                                       elif smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]!="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~"+" "+"~~$"+smark6[m]["Qnimg2"]+"~~")
                                       elif  smark6[m]["Qnimg1"]!="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark6[m]["Qn"]+" "+"~~$"+smark6[m]["Qnimg1"]+"~~")
                                       elif  smark6[m]["Qnimg1"]=="NA" and smark6[m]["Qnimg2"]=="NA" and smark6[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark6[m]["Qn"])
                                       else : partc8b.append(smark6[m]["Qn"])
                                       CO.append(smark6[m]["CO"])
                                       BT_Level.append(smark6[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark6[m]["Univ_QP_Reference"])
                                       Engrave.partCb(partc8b,CO,BT_Level,Univ_QP_Reference,qn8bSpltUp[0])
                                elif qn8bSpltUp[0][0]=="10":
                                       m10=m10-1
                                       m=m10
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~"+" "+"~~$"+smark10[m]["Qnimg3"]+"~~")
                                       elif smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]!="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~"+" "+"~~$"+smark10[m]["Qnimg2"]+"~~")
                                       elif  smark10[m]["Qnimg1"]!="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark10[m]["Qn"]+" "+"~~$"+smark10[m]["Qnimg1"]+"~~")
                                       elif  smark10[m]["Qnimg1"]=="NA" and smark10[m]["Qnimg2"]=="NA" and smark10[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark10[m]["Qn"])
                                       else : partc8b.append(smark10[m]["Qn"])
                                       CO.append(smark10[m]["CO"])
                                       BT_Level.append(smark10[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark10[m]["Univ_QP_Reference"])
                                       m5=m5-1
                                       m=m5
                                       if smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~"+" "+"~~$"+smark5[m]["Qnimg3"]+"~~")
                                       elif smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]!="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~"+" "+"~~$"+smark5[m]["Qnimg2"]+"~~")
                                       elif  smark5[m]["Qnimg1"]!="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark5[m]["Qn"]+" "+"~~$"+smark5[m]["Qnimg1"]+"~~")
                                       elif  smark5[m]["Qnimg1"]=="NA" and smark5[m]["Qnimg2"]=="NA" and smark5[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark5[m]["Qn"])
                                       else : partc8b.append(smark5[m]["Qn"])
                                       CO.append(smark5[m]["CO"])
                                       BT_Level.append(smark5[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark5[m]["Univ_QP_Reference"])
                                       Engrave.partCb(partc8b,CO,BT_Level,Univ_QP_Reference,qn8bSpltUp[0])
                                elif qn8bSpltUp[0][0]=="15":
                                       m15=m15-1
                                       m=m15
                                       CO=[]
                                       BT_Level=[]
                                       Univ_QP_Reference=[]
                                       if smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]!="NA" and smark15[m]["Qnimg3"]!="NA":
                                        partc8b.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~"+" "+"~~$"+smark15[m]["Qnimg2"]+"~~"+" "+"~~$"+smark15[m]["Qnimg3"]+"~~")
                                       elif smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]!="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~"+" "+"~~$"+smark15[m]["Qnimg2"]+"~~")
                                       elif  smark15[m]["Qnimg1"]!="NA" and smark15[m]["Qnimg2"]=="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark15[m]["Qn"]+" "+"~~$"+smark15[m]["Qnimg1"]+"~~")
                                       elif  smark15[m]["Qnimg1"]=="NA" and smark15[m]["Qnimg2"]=="NA" and smark15[m]["Qnimg3"]=="NA":
                                        partc8b.append(smark15[m]["Qn"])
                                       else : partc8b.append(smark15[m]["Qn"])
                                       CO.append(smark15[m]["CO"])
                                       BT_Level.append(smark15[m]["BT_Level"])
                                       Univ_QP_Reference.append(smark15[m]["Univ_QP_Reference"])
                                       Engrave.partCb(partc8b,CO,BT_Level,Univ_QP_Reference,qn8bSpltUp[0])
                                
                                Create()
                        elif partc==0:
                                splitup13=[["7","6"],["8","5"],["9","4"],["10","3"],["13"]]
                                qn6aSpltUp=sample(splitup13,1)
                                qn6bSpltUp=sample(splitup13,1)
                                qn7aSpltUp=sample(splitup13,1)
                                qn7bSpltUp=sample(splitup13,1)
                                splitup15=[["8","7"],["10","5"],["9","6"],["15"]]
                                qn8aSpltUp=sample(splitup15,1)
                                qn8bSpltUp=sample(splitup15,1)
                                m3=0
                                m4=0
                                m5=0
                                m6=0
                                m7=0
                                m8=0
                                m9=0
                                m10=0
                                m13=0
                                m15=0
                                partb6a=[]
                                partb6b=[]
                                partb7a=[]
                                partb7b=[]
                                partc8a=[]
                                partc8b=[]

                   


                elif IAexam == 1:

                        marks2UnitNo1=Questions.objects.filter(subjCode=subc,unit=units[0],mark_alloted="2").values()
                        marks2UnitNo2=Questions.objects.filter(subjCode=subc,unit=units[1],mark_alloted="2").values()
                        partA=[]
                        CO2=[]
                        BT_Level2=[]
                        Univ_QP_Reference2=[]
                        splitup2M=[["2","3"],["3","2"]]
                        spltsclt2=sample(splitup2M,1)
                        selctd2UnitNo1=sample(list(marks2UnitNo1),int(spltsclt2[0][0]))
                        selctd2UnitNo2=sample(list(marks2UnitNo2),int(spltsclt2[0][1]))
                        for k in selctd2UnitNo1:
                                if k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]!="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~"+" "+"~~$"+k["Qnimg3"]+"~~")
                                elif k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~")
                                elif  k["Qnimg1"]!="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~")
                                elif  k["Qnimg1"]=="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"])
                                else : partA.append(k["Qn"])
                                CO2.append(k["CO"])
                                BT_Level2.append(k["BT_Level"])
                                Univ_QP_Reference2.append(k["Univ_QP_Reference"])
                        for k in selctd2UnitNo2:
                                if k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]!="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~"+" "+"~~$"+k["Qnimg3"]+"~~")
                                elif k["Qnimg1"]!="NA" and k["Qnimg2"]!="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~"+" "+"~~$"+k["Qnimg2"]+"~~")
                                elif  k["Qnimg1"]!="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"]+" "+"~~$"+k["Qnimg1"]+"~~")
                                elif  k["Qnimg1"]=="NA" and k["Qnimg2"]=="NA" and k["Qnimg3"]=="NA":
                                        partA.append(k["Qn"])
                                else : partA.append(k["Qn"])
                                CO2.append(k["CO"])
                                BT_Level2.append(k["BT_Level"])
                                Univ_QP_Reference2.append(k["Univ_QP_Reference"])
                        Engrave.partA(partA,CO2,BT_Level2,Univ_QP_Reference2)
                                                                                                       

                elif IAexam == 2:

                        marks2=[]
                        for i in range(0,5):
                                marks2.append(Questions.objects.filter(subjCode=subc,unit=units[i],mark_alloted="2").values())
                        partA=[]
                        CO2=[]
                        BT_Level2=[]
                        Univ_QP_Reference2=[]
                        slctd2=[]
                        for i in range(0,5):
                               slctd2.append(list(marks2[i]),2)
                        for k in selctd2:
                            for j in range(0,2):
                                if k[j]["Qnimg1"]!="NA" and k[j]["Qnimg2"]!="NA" and k[j]["Qnimg3"]!="NA":
                                        partA.append(k[j]["Qn"]+" "+"~~$"+k[j]["Qnimg1"]+"~~"+" "+"~~$"+k[j]["Qnimg2"]+"~~"+" "+"~~$"+k[j]["Qnimg3"]+"~~")
                                elif k[j]["Qnimg1"]!="NA" and k[j]["Qnimg2"]!="NA" and k[j]["Qnimg3"]=="NA":
                                        partA.append(k[j]["Qn"]+" "+"~~$"+k[j]["Qnimg1"]+"~~"+" "+"~~$"+k[j]["Qnimg2"]+"~~")
                                elif  k[j]["Qnimg1"]!="NA" and k[j]["Qnimg2"]=="NA" and k[j]["Qnimg3"]=="NA":
                                        partA.append(k[j]["Qn"]+" "+"~~$"+k[j]["Qnimg1"]+"~~")
                                elif  k[j]["Qnimg1"]=="NA" and k[j]["Qnimg2"]=="NA" and k[j]["Qnimg3"]=="NA":
                                        partA.append(k[j]["Qn"])
                                else : partA.append(k[j]["Qn"])
                                CO2.append(k[j]["CO"])
                                BT_Level2.append(k[j]["BT_Level"])
                                Univ_QP_Reference2.append(k[j]["Univ_QP_Reference"])
                        Engrave.partA(partA,CO2,BT_Level2,Univ_QP_Reference2)
                
                