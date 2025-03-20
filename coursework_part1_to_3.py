# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W2006939
# Date: 23 NOV 2023

# Equating my variables to None/0 before they're actually given a value in the definition function
pass_credit_entered = None
defer_credit_entered = None
fail_credit_entered = None
total_credits = 0 
number_of_student_record = 0
progress_count = 0 
progress_module_trailer_count = 0
do_not_progress_count = 0
exclude_count = 0

#Creating a list to store the students records
student_data = []

def user_pass_credits():
    global pass_credit_entered # to call outside the statement
    while True: # Using loop until the condition is met which is until the user inputs a multiple of 20
        try:
            pass_credit_entered = int(input("Please enter number of credits for Pass: "))
            if pass_credit_entered in [0, 20, 40, 60, 80, 100, 120]:
                print(f"Credits for Pass: {pass_credit_entered}")
                return pass_credit_entered
            else: 
                print("Credit entered has to be a number from 0 to 120 (Multiples of 20).")
        except ValueError: 
            print("You have entered an alphabet.\nPlease enter a number from 0 to 120 (Multiples of 20).")

def user_defer_credits():
    global defer_credit_entered # to call outside the statement
    while True:
        try:
            defer_credit_entered = int(input("Please enter number of credits for Defer: "))
            if defer_credit_entered in [0, 20, 40, 60, 80, 100, 120]:
                print(f"Credits for Defer: {defer_credit_entered}")
                return defer_credit_entered
            else: 
                print("Credit entered has to be a number from 0 to 120 (Multiples of 20).")
        except ValueError:
            print("You have entered an alphabet.\nPlease enter a number from 0 to 120 (Multiples of 20).")

def user_fail_credits():
    global fail_credit_entered # to call outside the statement
    while True:
        try:
            fail_credit_entered = int(input("Please enter number of credits for Fail: "))
            if fail_credit_entered in [0, 20, 40, 60, 80, 100, 120]:
                print(f"Credits for Fail: {fail_credit_entered}")
                return fail_credit_entered
            else: 
                print("Credit entered has to be a number from 0 to 120 (Multiples of 20).")
        except ValueError:
            print("You have entered an alphabet.\nPlease enter a number from 0 to 120 (Multiples of 20).")

def progression_outcome(): # Creating a function which gives an ouput if certain criterias match withthe user's input
    global progress_count, progress_module_trailer_count, do_not_progress_count, exclude_count
    if pass_credit_entered == 120:
        print("Progression Outcome: Progress")
        progress_count += 1
    elif pass_credit_entered == 100:
        print("Progression Outcome: Progress (Module Trailer)")
        progress_module_trailer_count += 1
    elif pass_credit_entered <= 80 and fail_credit_entered <= 60:
        print("Progression Outcome: Do Not Progress (Module Retriever)")
        do_not_progress_count += 1
    else:
        print("Progression Outcome: Exclude")
        exclude_count += 1


def main(): 
    global number_of_student_record, total_credits, pass_credit_entered, defer_credit_entered, fail_credit_entered, data_of_credits
    while True:
        final_result = []
        user_pass_credits()
        final_result.append(pass_credit_entered)
        user_defer_credits()
        final_result.append(defer_credit_entered)
        user_fail_credits()
        final_result.append(fail_credit_entered)
        total_credits = sum(final_result)
        if total_credits == 120:
            data_of_credits = f"Credits for Pass: {pass_credit_entered}\nCredits for Defer: {defer_credit_entered}\nCredits for Fail: {fail_credit_entered}"
            student_data.append(data_of_credits)
            print(data_of_credits)
            number_of_student_record += 1
            break
        else:
            print("The total number of credits should be 120. Please try again. ")


def continue_or_quit():
    while True:
        answer = input("Would you like to add another students record (Y) or quit(Q): ")
        if answer.lower() == "y":
            main()
            progression_outcome()
        elif answer.lower() == "q":
            histogram() # call the histogram
            break
        else:
            print("Please enter Y/Q.")

# Creating the Histogram

from graphics import * 

def progress_bar(win, x, count, colour, label):
    global number_of_student_record
    porportion = count/number_of_student_record
    bar_height = porportion*300
    bar = Rectangle(Point(x, 400 - bar_height), Point(x + 150, 400)) #Setting the co-ordinates ffor the bottom left and top right corner
    bar.setFill(colour)
    bar.draw(win) 

    # Adding the total of each outcome on top of each bar
    count_label = Text(Point(x+ 75,400 - bar_height-20) ,str(count)) #setting the co-ordinates for the label
    count_label.setSize(18)
    count_label.draw(win)

    #Adding each outcome label below the bar
    outcome_label = Text(Point(x+75, 420),label)
    outcome_label.setSize(18)
    outcome_label.draw(win)


def histogram(): # reference from the textbook and the worksheet (grapgicsDocumentation)
    global number_of_student_record,progress_count,progress_module_trailer_count,do_not_progress_count,exclude_count
    # Creating the window 
    win = GraphWin("Histogram Results",900,500) #setting the window dimensions 
    win.setBackground("Light Blue")

    # Picking the colours for each progression outcome
    progress_colour = "Light Green"
    progress_module_trailer_colour = "Coral"
    do_not_progress_colour = "Red"
    exclude_colour = "Crimson"

    # Creating the bar for each progression outcome
    progress_bar(win, 150, progress_count, progress_colour, "Progress")
    progress_bar(win,275,progress_module_trailer_count,progress_module_trailer_colour, "Trailer")
    progress_bar(win,390,do_not_progress_count,do_not_progress_colour, "Retriever")
    progress_bar(win,515,exclude_count,exclude_colour, "Excluded ")
    
    # Creating where the title name 
    title = Text(Point(450,40), "Histogram Results") # Co-ordinates for where the title will be and the title name
    title.setSize(30)
    title.setStyle("bold")
    title.draw(win) #calling the function in the window

    # Creating the sentence that says how many outcomes are in the histogram
    number_of_outcomes = Text(Point(150,450),f"{number_of_student_record} outcomes in total")
    number_of_outcomes.setSize(20)
    number_of_outcomes.draw(win)
    win.getMouse() #open the window
    win.close()


# Creating the text file to store all the students records
def save_file():
    
    global number_of_student_record, total_credits, pass_credit_entered, defer_credit_entered, fail_credit_entered, data_of_credits
    
    student_data = []
    
    student_records = "student_records.txt"
    
    for records in student_records:
        print (student_data)
    
    with open(student_records, 'a') as file:
        for records in student_records:
            file.write(records + "\n")

main()
progression_outcome()
continue_or_quit()
save_file()
print(student_data)



