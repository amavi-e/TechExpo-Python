Project_Details = {}
Project_ID_List = []
def APD():
    global Project_Details, Project_Name, Category, Description, Country
    get_project_id = 'yes'
    while get_project_id == 'yes':
        Project_ID = input('Please enter project ID: ')
        if Project_ID in Project_ID_List:
            print('This ID already exists. Please enter a new project ID')
        else:
            Project_ID_List.append(Project_ID)
            get_project_id = 'no'
    Project_Name = input('Please enter the name of your project: ')
    Category = input('Please enter your category: ')
    No_of_TeamMembers = int(input("How many team members are there in your group? "))
    Team_Members = []
    for x in range(No_of_TeamMembers):
        name = input(f"Please enter {x + 1} member's full name: ")
        Team_Members.append(name)
    Description = input('Please enter a brief description about your project: ')
    Country = input('Please enter your country: ')
    Project_Details[Project_ID] = {
        'Project_Name': Project_Name,
        'Category': Category,
        'Team_Members': Team_Members,
        'Description': Description,
        'Country': Country}
def DPD():
    global Project_Details, Project_Name, Category, Description, Country
    Del_Project_ID = input('Please enter the Project ID of the details that you want to delete: ')
    if Del_Project_ID in Project_Details:
        Del_Detail = input('Which detail do you want to delete? Project_Name, Category, Team_Members, Description or Country? ')
        if Del_Detail == 'Team_Members':
            name = input('Enter the full name that you want to delete. Please ensure the first letter of first name and surname are capital: ')
            if name in Project_Details[Del_Project_ID][Del_Detail]:
                Name_Position = Project_Details[Del_Project_ID][Del_Detail].index(name)
                del Project_Details[Del_Project_ID][Del_Detail][Name_Position]
        elif Del_Detail in Project_Details[Del_Project_ID]:
            del Project_Details[Del_Project_ID][Del_Detail]
        else:
            print('You have entered an invalid name')
    else:
        print('You have entered an invalid Project ID')

def UPD():
    global Project_Details, Project_Name, Category, Description, Country
    Update_Project_ID = input('Please enter the Project ID of the details that you want to update: ')
    if Update_Project_ID in Project_Details:
        Update_Detail = input('Which detail do you want to update? Project_Name, Category, Team_Members, Description or Country? ')
        if Update_Detail == 'Team_Members':
            Member_name = input('Please enter the incorrect name that was initially entered. Please ensure the first letter of first name and surname are capital: ')
            if Member_name in Project_Details[Update_Project_ID][Update_Detail]:
                Name_Position = Project_Details[Update_Project_ID][Update_Detail].index(Member_name)
                New_Name = input('Please enter the new name that you want to enter: ')
                Project_Details[Update_Project_ID][Update_Detail][Name_Position] = New_Name
        elif Update_Detail in Project_Details[Update_Project_ID]:
            New = input('Please enter the new detail that matched the detail that you have chosen to update: ')
            Project_Details[Update_Project_ID][Update_Detail] = New
        else:
            print('You have entered an invalid name')
    else:
        print('You have entered an invalid Project ID')

def VPD():
    global Project_Details
    Project_Details_Keys = list(Project_Details.keys())
    Project_Details_Keys.sort()
    for i in Project_Details_Keys:
        print(f'The details of Project_ID {i} are', Project_Details[i])

def SPD():
    global Project_Details, f
    f = open('Project Details.txt', 'w')
    Project_Details_Keys = list(Project_Details.keys())
    for j in Project_Details_Keys:
        f.write(j + ' - ' + str(Project_Details[j]) + '\n')
    f.close()

def RSS():
    global f, Project_Details, Random_Projects_Dict
    prev_category = []
    import random
    Random_Projects_Dict = {}
    f = open('Project Details.txt', 'r')
    Lines = f.readlines()
    for i in range(len(Project_Details)):
        Random_Line = random.choice(Lines)
        words = Random_Line.split()
        Project_ID_Line = words[0]
        Category = Project_Details[Project_ID_Line]['Category']
        if Project_ID_Line not in Random_Projects_Dict and Category not in prev_category:
            Random_Projects_Dict[Project_ID_Line] = Random_Line
            prev_category.append(Category)
    print('These are the randomly selcted details of projects from each category')
    print(Random_Projects_Dict)

def AWP():
    global Project_Details, Random_Projects_Dict, reward, First_Place, First_Place_Name, First_Place_Country, Second_Place, Second_Place_Name, Second_Place_Country, Third_Place, Third_Place_Name, Third_Place_Country
    marks = {}
    for project_id, project_details in Random_Projects_Dict.items():
        print(f'Project details: {project_details}')
        total_mark = 0
        for judge in range(4):
            judge_mark = input(f'Judge number {judge+1}, please enter the number of asterisks for project {project_id}. Please note that the maximum number of asterisks is 5: ')
            while len(judge_mark) > 5:
                judge_mark = input(f'You have entered an invalid number of asterisks. Please enter the number of asterisks for project {project_id} again: ')
            total_mark += int(len(judge_mark))
        marks[project_id] = total_mark
    print("Total marks for each project:", marks)
    sorted_marks = sorted(marks.values(), reverse=True)
    First_Place = sorted_marks[0]
    First_Place_ID = None
    for key, value in marks.items():
        if value == First_Place:
            First_Place_ID = key
            break
    First_Place_Name = Project_Details[First_Place_ID]['Project_Name']
    First_Place_Country = Project_Details[First_Place_ID]['Country']
    Second_Place = sorted_marks[1]
    Second_Place_ID = None
    for key, value in marks.items():
        if value == Second_Place:
            Second_Place_ID = key
            break
    Second_Place_Name = Project_Details[Second_Place_ID]['Project_Name']
    Second_Place_Country = Project_Details[Second_Place_ID]['Country']
    Third_Place = sorted_marks[2]
    Third_Place_ID = None
    for key, value in marks.items():
        if value == Third_Place:
            Third_Place_ID = key
            break
    Third_Place_Name = Project_Details[Third_Place_ID]['Project_Name']
    Third_Place_Country = Project_Details[Third_Place_ID]['Country']
    
def VAP():
    global First_Place, First_Place_Name, First_Place_Country, Second_Place, Second_Place_Name, Second_Place_Country, Third_Place, Third_Place_Name, Third_Place_Country
    for stars in range(First_Place):
        print('       *       ')
    print(f' Project Name - {First_Place_Name}')
    print(f' Country - {First_Place_Country}')
    print(' 1st Place')
    print(" ")
    for stars in range(Second_Place):
        print('       *       ')
    print(f' Project Name - {Second_Place_Name}')
    print(f' Country - {Second_Place_Country}')
    print(' 2nd Place')
    print(" ")
    for stars in range(Third_Place):
        print('       *       ')
    print(f' Project Name - {Third_Place_Name}')
    print(f' Country - {Third_Place_Country}')
    print(' 3rd Place')

response = input("Do you want to enter details of a new project? Enter 'y' if yes or 'n' if no: ").lower()
while response == 'y':
    APD()
    VPD()
    SPD()
    response = input("Do you want to enter details of a new project? Enter 'y' if yes or 'n' if no: ").lower()
response2 = input("Do you want to update or delete details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()
while response2 == 'y':
    response3 = input("Do you want to delete details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()
    while response3 == 'y':
        DPD()
        VPD()
        SPD()
        response3 = input("Do you want to delete more details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()
    response4 = input("Do you want to update details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()
    while response4 == 'y':
        UPD()
        VPD()
        SPD()
        response4 = input("Do you want to update more details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()
    response2 = input("Do you want to update or delete more details from an already entered project? Enter 'y' if yes or 'n' if no: ").lower()

print('Random Spotlight Selection will be implemented now')
RSS()

print('The points will be given by the judges now and the winning teams are being selected')
AWP()

print('The award winning projects will be displayed now')
VAP()



