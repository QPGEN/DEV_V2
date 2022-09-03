from django.db import models

# class Subj(models.Model): #
    
#     subjCode=models.CharField(max_length=20)
#     subjName=models.CharField(max_length=100)
#     def __str__(self):
#         return  self.id +" - "+self.subjCode+" - "+self.subjName

# class CourseObjective(models.Model):
#     subjCode=models.ForeignKey(Subj,on_delete=models.CASCADE)
#     CObjec=models.CharField(max_length=200)

#     def __str__(self):
#         return  self.id +" - "+self.subjCode+" - "+self.CObjec

# class CourseOutcome(models.Model):
#     subjCode=models.ForeignKey(Subj,on_delete=models.CASCADE)
#     COno=models.CharField(max_length=20)
#     CourseOutcome=models.CharField(max_length=200)

#     def __str__(self):
#         return self.id +" - "+self.subjCode+" - "+self.COno + " - "+ self.CourseOutcome

class Questions(models.Model):
    subjCode=models.CharField(max_length=10)#Qns,CO,BT_Level,Univ_QP_Reference,mark_alloted
    unit=models.CharField(max_length=10)
    Qn=models.CharField(max_length=500)
    Qnimg1=models.ImageField(max_length=10,default="NA")
    Qnimg2=models.ImageField(max_length=10, default="NA")
    Qnimg3=models.ImageField(max_length=10, default="NA")
    Ans=models.CharField(max_length=500)
    ansimg1=models.ImageField(max_length=10, default="NA")
    ansimg2=models.ImageField(max_length=10, default="NA")
    ansimg3=models.ImageField(max_length=10, default="NA")
    mark_alloted=models.CharField(max_length=10)
    CO= models.CharField(max_length=10,default="NA")
    BT_Level=models.CharField(max_length=20,default="NA")
    Univ_QP_Reference= models.CharField(max_length=100, default="NA")

class Details(models.Model):
	subcode = models.CharField(max_length=100)
	subname = models.CharField(max_length=100)
	cno1 = models.CharField(max_length=100)
	cno2 = models.CharField(max_length=100)
	cno3 = models.CharField(max_length=100)
	cno4 = models.CharField(max_length=100)
	cno5 = models.CharField(max_length=100)
	co1 = models.CharField(max_length=100)
	co2 = models.CharField(max_length=100)
	co3 = models.CharField(max_length=100)
	co4 = models.CharField(max_length=100)
	co5 = models.CharField(max_length=100)
	cobj1 = models.CharField(max_length=100, default="NA")
	cobj2  = models.CharField(max_length=100, default="NA")
	cobj3  = models.CharField(max_length=100, default="NA")
	cobj4  = models.CharField(max_length=100, default="NA")
	cobj5 = models.CharField(max_length=100, default="NA")
	cobj6 = models.CharField(max_length=100, default="NA")
	cobj7 = models.CharField(max_length=100, default="NA")

