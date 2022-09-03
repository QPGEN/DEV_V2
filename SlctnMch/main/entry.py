from .models import Questions,Details

def gg():
        subcode={"GS8451":"Environmental Science","CS8967":"Python Programming","CH4575":"Chemistry","MA3498":"Math-1","PY7690":"Physics"}
        # cOut=[{"GS213.1":"Cout1","GS213.2":"Cout2","GS213.3":"Cout3","GS213.4":"Cout4","GS213.5":"Cout5"},
        # {"cS213.1":"Cout1","cS213.2":"Cout2","cS213.3":"Cout3","cS213.4":"Cout4","cS213.5":"Cout5"},
        # {"ch213.1":"Cout1","ch213.2":"Cout2","ch213.3":"Cout3","ch213.4":"Cout4","ch213.5":"Cout5"},
        # {"ma213.1":"Cout1","ma213.2":"Cout2","ma213.3":"Cout3","ma213.4":"Cout4","ma213.5":"Cout5"},
        # {"py213.1":"Cout1","py213.2":"Cout2","py213.3":"Cout3","py213.4":"Cout4","py213.5":"Cout5"}]

        # cobj=["cobj1","cobj2","cobj3","cobj4","cobj5"]
        a=[]
        j=0
        for i in subcode:
            
            a.append(Details(subcode = str(i),
            subname = str(subcode[i]),
            cno1 = str(i[0:2]+" 01"),
            cno2 = str(i[0:2]+" 02"),
            cno3 = str(i[0:2]+" 03"),
            cno4 = str(i[0:2]+" 04"),
            cno5 = str(i[0:2]+" 05"),
            co1 = str("course outcome 1 of sub-"+str(i)),
            co2 =str("course outcome 2 of sub-"+str(i)),
            co3 =str("course outcome 3 of sub-"+str(i)),
            co4 = str("course outcome 4 of sub-"+str(i)),
            co5 = str("course outcome 5 of sub-"+str(i)),
            cobj1 = str("course objective 1 of sub-"+str(i)),
            cobj2  =str("course objective 2 of sub-"+str(i)),
            cobj3  = str("course objective 3 of sub-"+str(i)),
            cobj4  = str("course objective 4 of sub-"+str(i)),
            cobj5 = str("course objective 5 of sub-"+str(i)),
            cobj6 =str("course objective 6 of sub-"+str(i)), 
            cobj7 =str("course objective 7 of sub-"+str(i))))
            a[j].save()
            j+=1

            # subjCode=models.CharField(max_length=10)#Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted
            # unit=models.CharField(max_length=10)
            # Qn=models.CharField(max_length=500)
            # Ans=models.CharField(max_length=500)
            # mark_alloted=models.CharField(max_length=10)

        units=['1','2','3','4','5']

        mkall=['2','3','4','5','6','7','8','9','10','13','15','16']


        c=0
        b=[]
        for i in subcode:
          for j in units:
            for k in mkall:
                for _ in range(0,20):
                    b.append(Questions(subjCode=str(i),unit=str(j),Qn="Question"+str(c+1),Ans="Answer"+str(c+1),mark_alloted=str(k)))
                    b[c].save()
                    c+=1
      