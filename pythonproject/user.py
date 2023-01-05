#!/usr/bin/python3
import re
from project import project
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return "number"
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return "float"
        except ValueError:
            return "string"

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      return True

    print("Invalid email")
    return False


class user():

    def register():


            first_name=input("please enter your first name : ")
            while check_user_input(first_name)!="string" or not first_name:
                print("please enter a valid name \nNOTE : don't use numbers or empty value")
                first_name=input("please enter your first name : ")

            last_name=input("please enter your last name : ")
            while check_user_input(last_name)!="string" or not last_name:
                print("please enter a valid name \nNOTE : don't use numbers or empty value")
                last_name=input("please enter your last name : ")


            email=input("please enter your email : ")
            while(not isValid(email)):
                email=input("please enter your email : ")

            password=input("please enter your password : ")
            confirm_password=input("please confirm your password : ")
            while password != confirm_password:
                print("password not match")
                confirm_password=input("please confirm your password : ")

            phone=input("please enter your phone number : ")
            while check_user_input(phone)!="number" or not phone:
                print("please enter a valid phone number  \nNOTE : don't use letters or empty value")
                phone=input("please enter your phone number : ")
                

            while True:
                done=input("please enter done to create account : ")
                if done=="done":
                    fileobj = open("usersinfo.txt" , "a")
                    usersinfo = f"{first_name}:{last_name}:{email}:{password}:{phone} \n "
                    fileobj.write(usersinfo)
                    fileobj.close()
                    print(" account created successfully <3 ")
                    break



    def login():

            email=input("please enter your email : ")
            while not isValid(email):
                email=input("please enter your email : ")

            password=input("please enter your password : ")

            try:
                fileobj = open("usersinfo.txt" , "r")
                users = fileobj.readlines()
                for u in users:
                    userinfo = u.strip("\n")
                    userinfo=userinfo.split(":")
                    if userinfo[2] == email and userinfo[3]==password:
                        print( f"welcome back {userinfo[0]}  <3 ")
                        if userinfo[0]:
                            print("user mwgod")
                            while True:
                                choice = input("press 1 if you want to add project \n press 2 if you want to view all projects \n press 3 if you want to edit your projects\n press 4 if you want to delete project  \n press 5 if you want to search for project\n ")
                                if choice=="1":
                                    project.add_project(userinfo[0])
                                elif choice=="2":
                                    project.view_all_projects()
                                elif choice=="3":
                                    project.edit_user_projects(userinfo[0])
                                elif choice=="4":
                                    project.delete_projects(userinfo[0])
                                elif choice=="5":
                                    project.search_for_project()
                                else:
                                    continue 
                                   
                        break
            except(Exception):
                print(" wrong email or password please try again \n if tou don't have account please register first ")

    while True:
        login_or_rigister = input("press 1 if you want to login \n press 2 if you want to register")
        if login_or_rigister=="1":
            login()
        if login_or_rigister=="2":
            register()
        else:
            continue

        