import compute
class ClassListDetails():
    def __init__(self,stu_id,first_name,last_name):
        self.stu_id=stu_id
        self.first_name=first_name
        self.last_name=last_name
    def __repr__(self):
        return repr((self.stu_id,self.first_name,self.last_name))

class a1ScoreDetails():
    maxscore=0
    def __init__(self,stu_id,score):
        self.stu_id=stu_id
        self.score=score
    def __repr__(self):
        return repr((self.stu_id,self.score,a1ScoreDetails.maxscore))
    

class a2ScoreDetails():
    maxscore=0
    def __init__(self,stu_id,score):
        self.stu_id=stu_id
        self.score=score
    def __repr__(self):
        return repr((self.stu_id,self.score,a1ScoreDetails.maxscore))

class t1ScoreDetails():
    maxscore=0
    def __init__(self,stu_id,score):
        self.stu_id=stu_id
        self.score=score
    def __repr__(self):
        return repr((self.stu_id,self.score,t1ScoreDetails.maxscore))

class t2ScoreDetails():
    maxscore=0
    def __init__(self,stu_id,score):
        self.stu_id=stu_id
        self.score=score
    def __repr__(self):
        return repr((self.stu_id,self.score,t2ScoreDetails.maxscore))

class projectScoreDetails():
    maxscore=0
    def __init__(self,stu_id,score):
        self.stu_id=stu_id
        self.score=score
    def __repr__(self):
        return repr((self.stu_id,self.score,projectScoreDetails.maxscore))
#-----------------------------------Building datastructure - reading files----------------------------

#-----------------------------------class.txt -----------------------------
with open("class.txt",mode='r') as myclassfile:
    for i in myclassfile.readlines():
        studobj=ClassListDetails(int(i.split("|")[0].rstrip()),i.split("|")[1].rstrip(),i.split("|")[2].rstrip())
        compute.studentrecord.append(studobj)
	
#-------------------------------------a1.txt------------------------------
with open("a1.txt",mode='r') as mya1record:
    a=mya1record.seek(0)
    a1ScoreDetails.maxscore=int(mya1record.readline().rstrip())
    for i in mya1record.readlines():
        try:
            if (len(i.split("|")[1].rstrip())!=0):
                a1obj=a1ScoreDetails(int(i.split("|")[0].rstrip()),int(i.split("|")[1].rstrip()))
            else:
                #for any entry which has no score again against the student_id
                a1obj=a1ScoreDetails(int(i.split("|")[0].rstrip()),0)
            
        except IndexError:
            a1obj=a1ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except ValueError:
            a1obj=a1ScoreDetails(int(i.split("|")[0].rstrip()),0)
        compute.a1record.append(a1obj)

#-------------------------------------a2.txt------------------------------
with open("a2.txt",mode='r') as mya2record:
    a=mya2record.seek(0)
    a2ScoreDetails.maxscore=int(mya2record.readline().rstrip())
    for i in mya2record.readlines():
        try:
            if (len(i.split("|")[1].rstrip())!=0):
                a2obj=a2ScoreDetails(int(i.split("|")[0].rstrip()),int(i.split("|")[1].rstrip()))
            else:
                a2obj=a2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except IndexError:
            a2obj=a2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except ValueError:
            a2obj=a2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        compute.a2record.append(a2obj)
    
#-------------------------------------t1.txt------------------------------
with open("t1.txt",mode='r') as myt1record:
    a=myt1record.seek(0)
    t1ScoreDetails.maxscore=int(myt1record.readline().rstrip())
    for i in myt1record.readlines():
        try:
            if (len(i.split("|")[1].rstrip())!=0):
                t1obj=t1ScoreDetails(int(i.split("|")[0].rstrip()),int(i.split("|")[1].rstrip()))
            else:
                t1obj=t1ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except IndexError:
            t1obj=t1ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except ValueError:
            t1obj=t1ScoreDetails(int(i.split("|")[0].rstrip()),0)
        compute.t1record.append(t1obj)

#-------------------------------------t2.txt------------------------------
with open("t2.txt",mode='r') as myt2record:
    a=myt2record.seek(0)
    t2ScoreDetails.maxscore=int(myt2record.readline().rstrip())
    for i in myt2record.readlines():
        try:
            if (len(i.split("|")[1].rstrip())!=0):
                t2obj=t2ScoreDetails(int(i.split("|")[0].rstrip()),int(i.split("|")[1].rstrip()))
            else:
                t2obj=t2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except IndexError:
            t2obj=t2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        except ValueError:
            t2obj=t2ScoreDetails(int(i.split("|")[0].rstrip()),0)
        compute.t2record.append(t2obj)
#-----------------------------project.txt--------------------------------
with open("project.txt",mode='r') as myprecord:
    a=myprecord.seek(0)
    projectScoreDetails.maxscore=int(myprecord.readline().rstrip())
    for i in myprecord.readlines():
        try:
            if (len(i.split("|")[1].rstrip())!=0):
                pobj=projectScoreDetails(int(i.split("|")[0].rstrip()),int(i.split("|")[1].rstrip()))
            else:
                pobj=projectScoreDetails(int(i.split("|")[0].rstrip()),0)
        except IndexError:
            pobj=projectScoreDetails(int(i.split("|")[0].rstrip()),0)
        except ValueError:
            pobj=projectScoreDetails(int(i.split("|")[0].rstrip()),0)
        compute.projectrecord.append(pobj)
#------- Sorting the file data on the basis of the student_id----------------------------------------------
#print("\n\n Sorting datastructure........")
compute.studentrecord.sort(key=lambda stu:stu.stu_id)
compute.a1record.sort(key=lambda stu:stu.stu_id)
compute.a2record.sort(key=lambda stu:stu.stu_id)
compute.t1record.sort(key=lambda stu:stu.stu_id)
compute.t2record.sort(key=lambda stu:stu.stu_id)
compute.projectrecord.sort(key=lambda stu:stu.stu_id)


#------------------------------- Menu ---------------------------------------------------------------------
def MainMenu():
    
    while(True):
        try:
            print("\n Welcome to grade calculator Main Menu, choose from the below option - to exit press 6")
            print("\n 1 Display individual components")
            print("\n 2 Display component average")
            print("\n 3 Display standard report")
            print("\n 4 Sort by alternate component")
            print("\n 5 Change the pass/fail point")
            print("\n 6 Exit")
            choice=int(input("Enter your choice (1/2/3/4/5/6):"))
            if (choice==1):
                compute.disp_ind_component()            
            elif (choice==2):
                compute.component_avg()
            elif (choice==3):
                compute.standard_report()
            elif (choice==4):
                compute.sort_report()
            elif (choice==5):
                compute.change_pass_fail()
            elif (choice==6):
                print("Good Bye!")
                break
            else:
                print ("Invalid choice - enter 1/2/3/4/5/6")
        except ValueError: # to catch hold of any value that is not an digit
            print ("Invalid choice - enter 1/2/3/4/5/6") 

    exit # out of the while means - 6 was pressed!

#-- calling the MainMenu----
MainMenu()
