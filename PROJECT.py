from datetime import datetime
from reading_from_user import *

def get_login_details():
    name = read_nonempty_alphabetical_string('Please enter your First Name >> ')
    number = read_nonempty_string('Please enter your password >> ')
    return name, number

#This only works for one user, i think thats what they wanted in the spec sheet
def read_login_details(typed_name, typed_number):
    with open("Login.txt") as login_file:
        line = login_file.readline()
        data = line.split(',')
        name = data[0]
        password = data[1].strip()
        if name == typed_name and password == typed_number:
            print(f'\nWelcome, {name}\n\n')
            return True
        else:
            print(f'Module record system - login failed.')
            return False

#this function reads modules and returns name and code lists
def read_modules_from_file(name_of_file):
    connection = open(name_of_file, 'r')
    module_code = []
    module_name = []
    line=[]
    while True:
        line = connection.readline().split(',')
        if len(line) < 2:
            break
        module_code.append(line[0].rstrip())
        module_name.append(line[1].rstrip())
    connection.close()
    return module_code, module_name

#makes a menu of modules and prompts for user choice
#then returns code of the module chosen
def display_modules(name_of_file):
    #reads all codes in to code list
    #_ just a holder that will not be used
    code , _= read_modules_from_file(name_of_file)
    #prints all module codes and adds number to it
    for num, module in enumerate(code):
        print(f'{num + 1}. {module}')
    #saves users choice
    choice = read_range_integer("> ",1, len(code))
    #retuns chosen code
    #choice -1 because list is 0 ...n and menu is 1... n
    return code[ choice -1 ]

#this function loads attendance to four paralel lists
#meaning student_names[0] and present[0], absent[0], excused[0]
#is one student data
def load_attendance(name_of_file):
    #This script capable to execute properly if files are
    #not created yet for selected module
    #there for try loop
    try:
        connection = open( name_of_file)
    except:
        #if file was not there exit function
        print("No data found for selected module.")
        return
    #otherwise initialiazing 4 lists
    student_names, present, absent, excused = [], [], [], []
    #infitinte loop
    while True:
        #read line from the file and split it and save it lo list line
        line = connection.readline().split(',')
        #if list didn't het 4 values, that means something is wrong with the file
        if len(line) < 4:
            #there for exit prematuraly
            break
        #otherwise save data to the lists
        student_names.append( line[0].rstrip())
        present.append( int(line[1].rstrip()))
        absent.append( int(line[2].rstrip()))
        excused.append( int(line[3].rstrip()))
    #close file
    connection.close()
    #return 4 lists
    return student_names, present, absent, excused
    
#this function tries to open argument file
#if file not found it will create one
#and ask for user to input student names
#then enter attendance
def take_class_attendance( name_of_file ):
    print("Module Record System(Attendance) - Choose a Module")
    print("---------------------------------------------------")
    #gets user input of module of intresed and saves its name
    module_code= display_modules( name_of_file )
    print(f"Module Record System(Attendance) {module_code}")
    print("-----------------------------------------------")
    #defining 4 lists 
    student_names, present, absent, excused = [],[],[],[]
    #just incase no file was created
    try:
        #if file was there loads the data to it
        student_names, present, absent, excused = load_attendance( module_code + ".txt" )
    except:
        #infinite loop
        while True:
            #Asking to enter student name or exit to stop doing it
            name = read_nonempty_string("Please enter student name, or type 'Exit' if you done entering students>>> ")
            #if user finished entering studends names exiting infinit loop
            if name.lower() == "exit":
                break
            #saving student name to student_names list
            student_names.append( name )
        #if there was no names entered exiting the function
        if not student_names:
            print("No data entered, exiting current procedure...")
            return
        #otherwise defining other 3 lists to same size as student_names
        present = [ 0 for i in range(len(student_names)) ]
        absent = [ 0 for i in range(len(student_names)) ]
        excused = [ 0 for i in range(len(student_names)) ]
    #string that will display the menu
    menu = '''
1. Present
2. Absent
3. Excused
''' #cycles throug the student_names   
    for student in range(len(student_names)):
        #temporary list for present absent and excused values
        data = [0, 0, 0]
        #Showing user what studend is being processed at the moment
        print(f'Student #{student+1}: {student_names[student]}')
        #printing menu
        print(menu)
        #getting user input
        choice = read_range_integer("> ",1, 3)
        #setting value in data to users choice
        data[ choice -1 ] = 1 
        #modifing data in the lists accordingly to users input
        present[ student ] += data[0]
        absent[ student ] += data[1]
        excused[ student ]+= data[2]
    #opening file that will be owerwirtten with updated data
    connection = open( module_code + ".txt", 'w')
    #cycling through the student_names list and storing each studens data
    for student in range(len(student_names)):
        print(f'{student_names[ student ]},{present[ student ]},{absent[ student ]},{excused[ student ]}', file = connection)
    #closing file
    connection.close() 
    print(f'{module_code}.txt updated with latest attendance records')

def generate_statistics(name_of_file):
    print("Module Record System(Statistics) - Choose a Module")
    print("--------------------------------------------------")
    #gets users input for module of interesed and saves its code
    module_code = display_modules(name_of_file)
    try:
        #trying to open file, module_code.txt
        student_names, present, absent, excused = load_attendance( module_code + ".txt" )
    except:
        #if file not found exiting prematuraly
        return
    #total amount of classes
    total = 0
    #if data was present in the file
    if student_names:
        #if data was correctly entered then sum of any studends
        #data should be equal, but it is not in example
        #i doubt we needed to check that
        total = present[0] + absent[0] + excused[0]
    #strings to store studends that are of that group
    low_attenders = ""
    non_attenders = ""
    best_attenders = ""
    #highest is the studend that was present the most 
    #average will store the total present days for all studends and then average
    highest, average = 0, 0
    #cylces through all the studends
    for student in range(len(present)):
        #current student that is being iterated
        #if his present days are more then seen so far
        if present[ student ] > highest :
            #set new highest
            highest = present[ student ]
            #and overwrite string with his name
            best_attenders = "\t"+student_names[ student ] + "\n"
        #incase there is second person with same amount of days
        elif present[ student ] == highest :
            #we add hime to that string
            best_attenders += "\t"+student_names[ student ] + "\n"

        #if student had 0 in present we add him to non attenders
        if present[ student ] == 0:
            non_attenders += "\t"+student_names[ student ] + "\n"
        #if student present days is less then 70 % of total
        #we add him to low attenders
        elif present[ student ] < total*0.7:
            low_attenders += "\t"+student_names[ student ] + "\n"
        #using average to store total present of whole class
        average += present[ student ]
    #if average has a value
    if average:
        #dividing it by total amount of students
        average /= len(student_names)
    #creating output string
    output = f'Module: {module_code}\n'
    output += f'Number of students: {len(student_names)}\n'
    output += f'Number of classes: {total}\n'
    output += f'Average Attendance: {average:.2f} days\n'
    output += 'Low Attender(s): under 70.0%\n'
    output += low_attenders 
    output += 'Non Attender(s):\n'
    output +=  non_attenders 
    output += 'Best Attender(s):\n'
    output += f'\tAtended { highest }/{total} days\n'
    output +=  best_attenders 
    #printing it on the screen
    print( output )
    #opening file for outputing the statistics
    output_file = open( module_code +"_"+ str(datetime.date(datetime.now())) + ".txt", "w")
    #writing output string to the file
    output_file.write( output )
    #closing file
    output_file.close()
    
def main():
    #menu string
    MENU='''
Module Record System - Options
------------------------------
1. Record Attendance
2. Generate Statistics
3. Exit
'''
    #amount of times to tolerate wrong input
    count = 3
    filename =  "Modules.txt"
    #while count is more then 0
    while True:
        #get log in input from user
        name, password = get_login_details()
        #if input was good exit loop
        if read_login_details(name, password ):
            break
        else:
            #display error and exit main function and quit program
            return
    #main loop
    while True:
        #display menu
        print(MENU) 
        #read user input and perform action accordingly
        choice = read_range_integer(">", 1, 3)
        if choice == 1:
            take_class_attendance( filename )
        elif choice == 2:
            generate_statistics( filename )
        elif choice == 3:
            break
        input("Press Enter to Continue...")


#excute main
main()
