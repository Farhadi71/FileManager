import getpass
import os
from subprocess import PIPE, Popen


#########################################################################################
def mkdir(command):
    first_path = os.getcwd()
    path = str(command.split()[1])
    #print(path)
    path_split = path.split('/')
    #print(path_split)
    counter = 0 # for count the path_split size
    for dir in path_split:
        counter += 1
        if not os.path.exists(dir):
            os.makedirs(dir)
            os.chdir(dir)
            #print(os.getcwd())
        else :
            if counter == len(path_split) : print("%s be in directory !" %path)
            os.chdir(dir)
            #print(os.getcwd())

    os.chdir(first_path)
    print(os.getcwd())


#########################################################################################
def rootf():
    mkdir("mkdir Localhost")
    os.chdir("Localhost")
    path = os.getcwd()
    return path

root = rootf()

#########################################################################################
def cd(command):
    if(len(command.split(' ')) != 1):
        path = str(command.split(' ')[1])
        path_split = path.split('/')
        # print(path_split)
        for dir in path_split:
            if not os.path.exists(dir):
                print("Couldn,t find directory !")
                break;
            else:
                os.chdir(dir)
    else:
        os.chdir(root)

    return os.getcwd()


#########################################################################################
def ls(command) :
    first_path = os.getcwd()
    if (len(command.split(' ')) != 1):
        path = str(command.split(' ')[1])
        path_split = path.split('/')
        # print(path_split)
        for dir in path_split:
            if not os.path.exists(dir):
                print("Couldn,t find directory !")
                os.chdir(first_path)
                break;
            else:
                os.chdir(dir)

    path = os.getcwd()
    for it in os.scandir(path):
        if it.is_dir():
            print(it.path +"\t \t \t \tDir")
        else :
            print(it.path + "\t \t \t \tFile")

#########################################################################################
def login_accept() :
    directory = root
    while True :
        command = input("Project@%s:~$ " %directory)
        command_split = command.split(' ')
        for c in command_split:
            if command == "exit"  :
                break
            elif c == "mkdir" :
                mkdir(command)
            elif c == "cd" :
                directory = cd(command)
            elif c == "ls" :
                ls(command)


#########################################################################################
def authentication_user() :
    usr = input("Username :")
    pwd = getpass.getpass("Enter password : ")
    if usr == "a" and pwd == "123" :
        print("Welcome %s to Project" %usr )
        login_accept()


while True :
    UsrInput = input("Press s : sign in  or a : create User account \nProject~$ ")
    if UsrInput == 'a':
        '''Create Acount'''
    elif UsrInput == 's':
        authentication_user()
