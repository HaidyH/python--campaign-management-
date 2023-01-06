from datetime import date
import traceback
import fileinput


class project():

    def isDate(year, month, day):
        try:
            date(year, month, day)
            return True
        except ValueError:
            print(f"please enter a valid date {traceback.print_exc()}")
            return False

 

    def isInvalidDate(inputdate):
        if inputdate >= date.today():
            return True
        print("Invalid date please enter date is not in tha past")
        return False


    def check_user_input(input):
        try:
            # Convert it into integer
            val = int(input)
            return "number"
        except ValueError:
            try:
                # Convert it into float
                val = float(input)
                return "number"
            except ValueError:
                return "string"




    def add_project(username):


            title=input("please enter the title of the campaign : ")
            while project.check_user_input(title)!="string" or not title:
                print("please enter a valid title \nNOTE : don't use numbers or empty value")
                title=input("please enter the title of the campaign : ")

            details=input("please enter the campaign detals : ")
            while project.check_user_input(details)!="string" or not details:
                print("please enter a valid name \nNOTE : don't use numbers or empty value")
                details=input("please enter the campaign detals : ")


            totalTarget=input("please enter your total target : ")
            if not totalTarget:
                totalTarget=250000
            while project.check_user_input(totalTarget)!="number":
                print("please enter a valid number  \nNOTE : don't use letters ")
                totalTarget=input("please enter your total target : ")
            
            startDate=input("please enter the start date in YYYY-MM-DD format : ")
            while True:
                year, month, day = map(int, startDate.split('-'))
                if project.isDate(year, month, day):
                    inputdate = date(year, month, day)
                    if project.isInvalidDate(inputdate):
                        break
                startDate=input("please enter the start date  : ")

            endDate=input("please enter the end date in YYYY-MM-DD format : ")
            while True:
                year, month, day = map(int, endDate.split('-'))
                if project.isDate(year, month, day):
                    inputdate = date(year, month, day)
                    if project.isInvalidDate(inputdate) and endDate > startDate:
                        break
                endDate=input("please enter a valid end date that not before start date  : ")

            while True:
                done=input("please enter done to confirm : ")
                if done=="done":
                    fileobj = open("projects.txt" , "a")
                    projectinfo = f"{username}:{title}:{details}:{totalTarget}EGP:{startDate}:{endDate}\n"
                    fileobj.write(projectinfo)
                    fileobj.close()
                    print(" project created successfully <3 ")
                    break

    def view_all_projects():
        try:
            fileobj = open("projects.txt" , "r")
            projects = fileobj.readlines()
            print("All Projects \n")
            for p in projects:
                print(p)
        except(Exception):
            print("file not found please try again")
        


    def edit_user_projects(username):
        projectname=input("please enter the title of the campaign that you want to edit : ")

        try:
            fileobj = open("projects.txt" , "r")
            projectinfos = fileobj.readlines()
            newline=[]
            isfound=False
            #copy all except project that I want to delete 
            for p in projectinfos:
                projectinfo = p.strip("\n")
                projectinfo=projectinfo.split(":")   
                if projectinfo[1] != projectname:
                    newline.append(p)

            #get line that I want to delete
            def edit(editindex,editname):

                for p in projectinfos:
                    projectinfo = p.strip("\n")
                    projectinfo=projectinfo.split(":")
                    if projectinfo[1] == projectname:                            

                        oldelement=projectinfo[editindex]
                        newelement=input(f" please enter new campaign {editname}= ")
                        newline.append(p.replace(oldelement,newelement))
                        if projectinfo[0]==username:
                            with open("projects.txt","w") as f:
                                for line in newline:
                                    f.writelines(line)
                                print(" updated sucessfully <3 ")
                                return True
                return False

            while True:                
                inputedit=input("what do you want to edit: \n choose 1 if you want to edit title \n choose 3 if you want to edit details \n choose 3 if you want to edit budget \n choose 4 if you want to edit start date \n choose 5 if you want to edit end date\n choose 6 if you want to exit \n")           
                if inputedit=="1": 
                    edit(1,"title")
                    isfound=edit(1,"title")
                    break
                elif inputedit=="2":
                    edit(2,"details")
                    isfound=edit(2,"details")
                    break         
                elif inputedit=="3":
                    edit(3,"budget")
                    isfound=edit(3,"budget")
                    break          
                elif inputedit=="4":
                    edit(4,"start date")
                    isfound=edit(4,"start date")
                    break          
                elif inputedit=="5":
                    edit(5,"end date")
                    isfound=edit(5,"end date")
                    break          
                elif inputedit=="6":
                    break
                else:
                    print("invalid input")
                    inputedit=input("what do you want to edit: \n choose 1 if you want to edit title \n choose 3 if you want to edit details \n choose 3 if you want to edit budget \n choose 4 if you want to edit start date \n choose 5 if you want to edit end date\n choose 6 if you want to exit \n")           

            if not isfound:  
                print( f" user {projectinfo[0]} don't have any projects with name {projectname} please try again")
                
        except(Exception) as e:
            print(e)



    def delete_projects(username):
        projectname=input("please enter the title of the campaign you want to delete : ")
        try:
            fileobj = open("projects.txt" , "r")
            projectinfos = fileobj.readlines()
            newline=[]
            isfound=False
            #copy all except project that I want to delete 
            for p in projectinfos:
                projectinfo = p.strip("\n")
                projectinfo=projectinfo.split(":")   
                if projectinfo[1] != projectname:
                    newline.append(p)
            for p in projectinfos:
                projectinfo = p.strip("\n")
                projectinfo=projectinfo.split(":")
                if (projectinfo[1]==projectname and projectinfo[0]==username):
                    isfound=True
                    with open("projects.txt","w") as f:
                        for line in newline:
                            f.writelines(line)
                            fileobj.close()
                        
            if(isfound):
                print(" deleted sucessfully <3 ")
            else:
                print(" no project found ") 
        except(Exception) as e:
            print(e)  



    def search_for_project():
        projectname=input("please enter the title of the campaign : ")
        isfound= False
        try:
            fileobj = open("projects.txt" , "r")
            projectinfos = fileobj.readlines()
            for p in projectinfos:
                projectinfo = p.strip("\n")
                projectinfo=projectinfo.split(":")
                if projectinfo[1] == projectname:
                    newline=[]
                    newline.append(p)
                    isfound= True
                    for n in newline:
                        print(n)
            if(not isfound):
                print(" no project found ")           
        except(Exception):
            print(" no file found ")   
               
    edit_user_projects("haidy")


    