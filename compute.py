
#--------------------------------Initialising the datastructure - list--------------
studentrecord=list() # will hold the instances of class - ClassListDetails as the element of list
a1record=list() # will hold the instances of class -a1ScoreDetails as the element of list
a2record=list() # will hold the instances of class - a2ScoreDetails as the element of list
t1record=list() # will hold the instances of class - t1ScoreDetails as the element of list
t2record=list() # will hold the instances of class - t2ScoreDetails as the element of list
projectrecord=list() #will hold the instances of class - projectScoreDetails as the element of list
grade_pointer=dict()
#----------------------------------------------------------------------------
# 1. Display individual component
def disp_ind_component():
    print("\n**** Displaying Score for individual component,Select from below listed components.To be able to return to main menu,please select a valid option****")
    print("a1/A1 - Assignment1")
    print("a2/A2 - Assignment2")
    print("t1/T1 - Test1")
    print("t2/T2 - Test2")
    print("pr/PR - Project")
    while True:
        try:
            compchoice=input("Enter your choice:")
            if compchoice.lower()=='a1':
                print(f"A1 grades ({a1record[0].maxscore})")
                for studrec in studentrecord:
                    for a1rec in a1record:
                        if (studrec.stu_id==a1rec.stu_id):
                            print(f"{studrec.stu_id}\t{studrec.last_name},{studrec.first_name}\t{a1rec.score if a1rec.score!=0 else ''}")
                break
            elif compchoice.lower()=='a2':
                print(f"A2 grades ({a2record[0].maxscore})")
                for studrec in studentrecord:
                    for a2rec in a2record:
                        if (studrec.stu_id==a2rec.stu_id):
                           print(f"{studrec.stu_id}\t{studrec.last_name},{studrec.first_name}\t{a2rec.score if a2rec.score!=0 else ''}") 
                break
            elif compchoice.lower()=='t1':
                 print(f"T1 grades ({t1record[0].maxscore})")
                 for studrec in studentrecord:
                     for t1rec in t1record:
                         if (studrec.stu_id==t1rec.stu_id):
                             print(f"{studrec.stu_id}\t{studrec.last_name},{studrec.first_name}\t{t1rec.score if t1rec.score!=0 else ''}")
                 break
            elif compchoice.lower() == 't2':
                print(f"T2 grades ({t2record[0].maxscore})")
                for studrec in studentrecord:
                    for t2rec in t2record:
                        if (studrec.stu_id==t2rec.stu_id):
                            print(f"{studrec.stu_id}\t{studrec.last_name},{studrec.first_name}\t{t2rec.score if t2rec.score!=0 else ''}")
                break
            elif compchoice.lower() =='pr':
                print(f"PR grades ({t2record[0].maxscore})")
                for studrec in studentrecord:
                    for pr_rec in projectrecord:
                        if (studrec.stu_id==pr_rec.stu_id):
                            print(f"{studrec.stu_id}\t{studrec.last_name},{studrec.first_name}\t{pr_rec.score if pr_rec.score!=0 else ''}")
                break
            else:
                print("Invalid choice - enter a1/A1/a2/A2/t1/T1/t2/T2/pr/PR")
            
        except ValueError: 
             print("Invalid choice - enter a1/A1/a2/A2/t1/T1/t2/T2/pr/PR")  
            

# 2. Display component average
def component_avg():
    print("\n****Computing average , Select from below listed components. To be able to return to main menu,please select a valid option****")
    print("a1/A1 - Assignment1")
    print("a2/A2 - Assignment2")
    print("t1/T1 - Test1")
    print("t2/T2 - Test2")
    print("pr/PR - Project")
    while True:
        try:
            compchoice=input("Enter your choice:")
            if compchoice.lower()=='a1':
                sum=0
                for item in a1record:
                    sum+=item.score
                print(f"A1 average:{round(sum/len(a1record),1)}/{a1record[0].maxscore}")
                break
            elif compchoice.lower()=='a2':
                sum=0
                for item in a2record:
                    sum+=item.score
                print(f"A2 average:{round(sum/len(a2record),1)}/{a2record[0].maxscore}")
                break
            elif compchoice.lower()=='t1':
                sum=0
                for item in t1record:
                    sum+=item.score
                print(f"T1 average:{round(sum/len(t1record),1)}/{t1record[0].maxscore}")
                break
            elif compchoice.lower() == 't2':
                sum=0
                for item in t2record:
                    sum+=item.score
                print(f"T2 average:{round(sum/len(t2record),1)}/{t2record[0].maxscore}")
                break
            elif compchoice.lower() =='pr':
                sum=0
                for item in projectrecord:
                    sum+=item.score
                print(f"PR average:{round(sum/len(projectrecord),1)}/{projectrecord[0].maxscore}")
                break
            else:
                print("Invalid choice - enter a1/A1/a2/A2/t1/T1/t2/T2/pr/PR")
                
        except ValueError:
            print("Invalid choice - enter a1/A1/a2/A2/t1/T1/t2/T2/pr/PR")

#3. Display standard report
def computed_grade(tot):
    if(len(grade_pointer)==0):
        range=round((100-50)/7,0)
        grade_pointer['C']=[50.0,50+range]
        grade_pointer['B-']=[round(grade_pointer['C'][1]+0.1,1),round(grade_pointer['C'][1]+0.1+range,1)]
        grade_pointer['B']=[round(grade_pointer['B-'][1]+0.1,1),round(grade_pointer['B-'][1]+0.1+range,1)]
        grade_pointer['B+']=[round(grade_pointer['B'][1]+0.1,1),round(grade_pointer['B'][1]+0.1+range,1)]
        grade_pointer['A-']=[round(grade_pointer['B+'][1]+0.1,1),round(grade_pointer['B+'][1]+0.1+range,1)]
        grade_pointer['A']=[round(grade_pointer['A-'][1]+0.1,1),round(grade_pointer['A-'][1]+0.1+range,1)]
        grade_pointer['A+']=[round(grade_pointer['A'][1]+0.1,1),round(grade_pointer['A'][1]+0.1+range,1)]
        grade_pointer['F']=[0.0,round(50.0-0.1,1)]
    
    if grade_pointer['A+'][1]<tot and tot<=100:
         return ("A+")
    else: # this means the grade will perfectly fall in some range
        for item in grade_pointer:
            if (grade_pointer[item][0]<=tot and grade_pointer[item][1]>=tot):
                return (f"{item}")

def stud_score(student_id): #fetching all the score and computing GR and calling funct - computed_grade for fetching the default grade
    student_grade_report=dict()
    sum=0
    for item in studentrecord: 
        if item.stu_id==student_id:
            student_grade_report['stu_rec']=[item.last_name,item.first_name,item.stu_id]
    for item in a1record:
        if item.stu_id==student_id:
            student_grade_report['A1']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.075
    for item in a2record:
        if item.stu_id==student_id:
            student_grade_report['A2']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.075
    for item in t1record:
        if item.stu_id==student_id:
            student_grade_report['T1']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.3
    for item in t2record:
        if item.stu_id==student_id:
            student_grade_report['T2']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.3
    for item in projectrecord:
        if item.stu_id==student_id:
            student_grade_report['PR']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.25
    student_grade_report['GR']=[round(sum,1)]
    student_grade_report['FL']=[computed_grade(sum)]
    return(student_grade_report)
            
    
def standard_report():
    
    print("{id:<6}{ln:<9}{fn:<9}{a1:<6}{a2:<6}{t1:<6}{t2:<6}{pr:<6}{gr:<6}{fl:<6}".format(id='ID',ln='LN',fn='FN',a1='A1',a2='A2',t1='T1',t2='T2',pr='PR',gr='GR',fl='FL'))
    
    for item in studentrecord:
        a=stud_score(item.stu_id)
        for item in a.keys():
            #print(item)
            if item=='stu_rec':
                print(f"{a[item][2]:<6}{a[item][0]:<9}{a[item][1]:<9}",end='')
            elif item=='A1':#if a1rec.score!=0 else ''
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='A2':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='T1':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='T2':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='PR':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='GR':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
            elif item=='FL':
                print(f"{a[item][0] if a[item][0]!=0 else '':<6}")
         
       
#4 . Sort by alternate component
def sort_report():
    print("Sorting by alternate component - please enter your choice(1/2)from below option. To be able to go back to main menu please enter a valid choice.")
    print("1 Sort by Last Name")
    print("2 Sort by Numeric Grade")
    while True:
        try:
            sortcompchoice=int(input("Enter your choice (1/2):"))
            if sortcompchoice==1:
                print("**Sorting by Last Name**")
                student_record_keeper=list() # list of dictionaries
                for item in studentrecord:
                    a=stud_score(item.stu_id)
                    student_record_keeper.append(a)
                
                print("{id:<6}{ln:<9}{fn:<9}{a1:<6}{a2:<6}{t1:<6}{t2:<6}{pr:<6}{gr:<6}{fl:<6}".format(id='ID',ln='LN',fn='FN',a1='A1',a2='A2',t1='T1',t2='T2',pr='PR',gr='GR',fl='FL'))
                new_ln_list=sorted(student_record_keeper,key=lambda k:k['stu_rec'][0])
                for item in new_ln_list:
                    for item2_key,item2_val in item.items():
                        if item2_key=='stu_rec':
                            print(f"{item2_val[2]:<6}{item2_val[0]:<9}{item2_val[1]:<9}",end='')
                        elif item2_key=='A1':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}" ,end='')
                        elif item2_key=='A2':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='T1':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='T2':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='PR':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='GR':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='FL':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}")

                break
            elif sortcompchoice==2:
                print("**Sorting by Numeric Grade**")
                student_record_keeper=list() # list of dictionaries
                for item in studentrecord:
                    a=stud_score(item.stu_id)
                    student_record_keeper.append(a)
                print("{id:<6}{ln:<9}{fn:<9}{a1:<6}{a2:<6}{t1:<6}{t2:<6}{pr:<6}{gr:<6}{fl:<6}".format(id='ID',ln='LN',fn='FN',a1='A1',a2='A2',t1='T1',t2='T2',pr='PR',gr='GR',fl='FL'))
                new_gr_list=sorted(student_record_keeper,key=lambda k:k['GR'],reverse=True)
                
                for item in new_gr_list:
                    for item2_key,item2_val in item.items():
                        if item2_key=='stu_rec':
                            print(f"{item2_val[2]:<6}{item2_val[0]:<9}{item2_val[1]:<9}",end='')
                        elif item2_key=='A1':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}" ,end='')
                        elif item2_key=='A2':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='T1':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='T2':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='PR':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='GR':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}",end='')
                        elif item2_key=='FL':
                            print(f"{item2_val[0] if item2_val[0]!=0 else '':<6}")

                break
            else:
                print("Invalid choice - enter from either (1/2)")
        except ValueError:
            print("Invalid choice - enter (1/2)")
   
#5 . Change Pass/Fail point
def new_computed_grade(pfchoice):
    new_point_system=dict()
    range=round((100-pfchoice)/7,0)
    new_point_system['C']=[float(pfchoice),float(pfchoice)+range]
    new_point_system['B-']=[round(new_point_system['C'][1]+0.1,1),round(new_point_system['C'][1]+0.1+range,1)]
    new_point_system['B']=[round(new_point_system['B-'][1]+0.1,1),round(new_point_system['B-'][1]+0.1+range,1)]
    new_point_system['B+']=[round(new_point_system['B'][1]+0.1,1),round(new_point_system['B'][1]+0.1+range,1)]
    new_point_system['A-']=[round(new_point_system['B+'][1]+0.1,1),round(new_point_system['B+'][1]+0.1+range,1)]
    new_point_system['A']=[round(new_point_system['A-'][1]+0.1,1),round(new_point_system['A-'][1]+0.1+range,1)]
    new_point_system['A+']=[round(new_point_system['A'][1]+0.1,1),round(new_point_system['A'][1]+0.1+range,1)]
    new_point_system['F']=[0.0,round(float(pfchoice)-0.1,1)]
    return new_point_system
 
def pf_stud_score(student_id,new_grade_pointer): #fetching all the score and computing GR and calling funct - computed_grade for fetching the default grade
    student_grade_report=dict()
    sum=0
    for item in studentrecord: 
        if item.stu_id==student_id:
            student_grade_report['stu_rec']=[item.last_name,item.first_name,item.stu_id]
    for item in a1record:
        if item.stu_id==student_id:
            student_grade_report['A1']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.075
    for item in a2record:
        if item.stu_id==student_id:
            student_grade_report['A2']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.075
    for item in t1record:
        if item.stu_id==student_id:
            student_grade_report['T1']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.3
    for item in t2record:
        if item.stu_id==student_id:
            student_grade_report['T2']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.3
    for item in projectrecord:
        if item.stu_id==student_id:
            student_grade_report['PR']=[item.score,item.maxscore]
            sum+=((item.score/item.maxscore)*100)*0.25
    student_grade_report['GR']=[round(sum,1)]
    if new_grade_pointer['A+'][1]<sum and sum<=100:
        student_grade_report['FL']=['A+']
    else:
        for item in new_grade_pointer:
           if (new_grade_pointer[item][0]<=sum and new_grade_pointer[item][1]>=sum):
                student_grade_report['FL']=[f"{item}"]
    return(student_grade_report)

            
def change_pass_fail():
    print("**Change the pass/fail point**")
    while True:
        try:            
            pfchoice=int(input("Enter the desire pass/fail point:"))
           
            if pfchoice>=0 and pfchoice<=100:
                new_grade_pointer=new_computed_grade(pfchoice)
                print("{id:<6}{ln:<9}{fn:<9}{a1:<6}{a2:<6}{t1:<6}{t2:<6}{pr:<6}{gr:<6}{fl:<6}".format(id='ID',ln='LN',fn='FN',a1='A1',a2='A2',t1='T1',t2='T2',pr='PR',gr='GR',fl='FL'))
                for item in studentrecord:
                    a=pf_stud_score(item.stu_id,new_grade_pointer) # sending the student id and new grade scheme
                    for item in a.keys():
                        #print(item)
                        if item=='stu_rec':
                            print(f"{a[item][2]:<6}{a[item][0]:<9}{a[item][1]:<9}",end='')
                        elif item=='A1':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='A2':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='T1':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='T2':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='PR':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='GR':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}",end='')
                        elif item=='FL':
                            print(f"{a[item][0] if a[item][0]!=0 else '':<6}")
               
                break
            else:
                print("Invalid choice- please enter a valid number(0-100)")
        except ValueError:
           print("Invalid choice- please enter a valid number(0-100)")
            
