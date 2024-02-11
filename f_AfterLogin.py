'''
The functions support After Log-in
'''

'''
Functions
'''

#This function to gives additional options after login is successful
def addOptions():
    print("Welcome! What would you like to do?")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Job search/internship option is currently under construction.")

    elif choice == "2":
        print("Find someone you know option is currently under construction.")

    elif choice == "3":
        print("Here are 5 skills you can learn:")
        print("1. Programming")
        print("2. Prompt Engineering")
        print("3. 3D Modeling & Simulation")
        print("4. Data Analysis")
        print("5. Language Learning")
        print("6. Return to the previous level. . .")

        #Presents the user with the option to choose a skill
        choiceSkill = input("Enter your skill choice: ")

        if choiceSkill == "1":
            print("The Programming option is currently under construction.")

        elif choiceSkill == "2":
            print("The Prompt Engineering option is currently under construction.")

        elif choiceSkill == "3":
            print("The 3D Modeling & Simulation option is currently under construction.")

        elif choiceSkill == "4":
            print("The Data Analysis option is currently under construction.")

        elif choiceSkill == "5":
            print("The Language Learning option is currently under construction.")
        
        else:
            print("6. Returning to the previous level. . .")
            addOptions()

    else:
        print("Invalid choice.")

    return 1