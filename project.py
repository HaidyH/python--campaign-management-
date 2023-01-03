from datetime import date
import re


today = date.today()
def isDate(date):
    if date-today > 0:
      return True

    print("Invalid date")
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




def register():


        title=input("please enter the title of the campaign : ")
        while check_user_input(title)!="string" or not title:
            print("please enter a valid title \nNOTE : don't use numbers or empty value")
            title=input("please enter the title of the campaign : ")

        details=input("please enter the campaign detals : ")
        while check_user_input(details)!="string" or not details:
            print("please enter a valid name \nNOTE : don't use numbers or empty value")
            details=input("please enter the campaign detals : ")


        totalTarget=input("please enter your total target : ")
        if not totalTarget:
            totalTarget=250000
        while check_user_input(totalTarget)!="number":
            print("please enter a valid number  \nNOTE : don't use letters ")
            totalTarget=input("please enter your total target : ")
        
        startDate=input("please enter the start date in YYYY-MM-DD format : ")
        while(not startDate):
            year, month, day = map(int, startDate.split('-'))
            startDate1 = date(year, month, day)
            if isDate(startDate1):
                break
            startDate=input("please enter the start date  : ")

        # endDate=input("please enter the end date  : ")
        # while(not isDate(endDate)):
        #     endDate=input("please enter the end date  : ")

        while True:
            done=input("please enter done to confirm : ")
            if done=="done":
                fileobj = open("projects.txt" , "a")
                projectinfo = f"{title}:{details}:{totalTarget}EGP:{startDate}\n"
                fileobj.write(projectinfo)
                fileobj.close()
                print(" project created successfully <3 ")
                break

print(today)
print(today-today)

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = date(year, month, day)

print (date1)
