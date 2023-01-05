from datetime import date
import traceback
import re

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




    def add_project():


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
            while(not startDate):
                year, month, day = map(int, startDate.split('-'))
                if project.isDate(year, month, day):
                    inputdate = date(year, month, day)
                    if project.isInvalidDate(inputdate):
                        break
                startDate=input("please enter the start date  : ")

            endDate=input("please enter the end date in YYYY-MM-DD format : ")
            while(not endDate):
                year, month, day = map(int, endDate.split('-'))
                if project.isDate(year, month, day):
                    inputdate = date(year, month, day)
                    if project.isInvalidDate(inputdate):
                        break
                endDate=input("please enter the end date  : ")

            while True:
                done=input("please enter done to confirm : ")
                if done=="done":
                    fileobj = open("projects.txt" , "a")
                    projectinfo = f"{title}:{details}:{totalTarget}EGP:{startDate}\n"
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
            projectname=input("please enter the name of the campaign : ")
            try:
                fileobj = open("projects.txt" , "r")
                projectinfos = fileobj.readlines()
                for p in projectinfos:
                    projectinfo = p.strip("\n")
                    projectinfo=projectinfo.split(":")
                    if projectinfo[0] == username:
                        if projectinfo[1]==projectname:
                            edit=input("what do you want to edit: ")
                            print(edit)
                        else:
                            print( f" user {projectinfo[0]} don't have any projects with name {projectname} please try again")
                        break
            except(Exception):
                print(" no project found ")
    def delete_projects():
        print("delete_projects")
    def search_for_project():
        print("search_for_project")
        
    # # print(today)
    # # date dayzero=0:00:00
    # # print(today-today)
    # date_entry = input('Enter a date in YYYY-MM-DD format')
    # year, month, day = map(int, date_entry.split('-'))
    # date1 = date(year, month, day)
    # print (date1)
    # isDate(date1)

# startDate=input("please enter the start date in YYYY-MM-DD format : ")
# while(True):
#     year, month, day = map(int, startDate.split('-'))
#     if project.isDate(year, month, day):
#             inputdate = date(year, month, day)
#             if project.isInvalidDate(inputdate):
#                 break
#     startDate=input("please enter the start date  : ")

    edit_user_projects("haidy")