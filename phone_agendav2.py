import os
import sys
from pathlib import Path
from tracemalloc import start

file_name = "phone_agendav2.txt"
file1 = open(file_name, "a+")

next_id = 1

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner(title):
    """Prints program banner."""

    cls()
    print("+", "-" * (len(title) + 2), "+", sep="")
    print("|", title, "|")
    print("+", "-" * (len(title) + 2), "+", sep="")

def print_message(*msg):
    print("-" * 50)
    print(*msg)
    print("-" * 50)

def print_contact(name, phone):
    print("+" + "-" * 30 + "+")
    print("Full Name: ", name)
    print("Phone number: ", phone)
    print("+" + "-" * 30 + "+")
    print()

def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print_banner("PHONE AGENDA MENU")
    print("[Enter 1,2,3,4 or 0]\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To search and delete your contacts\n"+
          "Enter 0 To Quit\n" + "-" * 42)
    choice = input("Enter your choice: ")
    if choice == "1":
        print_banner("AGENDA")
        file1 = open(file_name, "r+")
        file_contents = file1.readlines()
        if len(file_contents) == 0:
            print_message("Agenda is empty")
        else:
            count = 0
            file_contents.sort()
            for file in file_contents:
                print ("+" + "-" * 30 + "+\n",
                count, ".",
                file, "\n" + "+" + "-" * 30 + "+"
                )
                count += 1
        file1.close
        ret_to_main_menu_prompt()
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ret_to_main_menu_prompt()
        enter_contact_record_again()
        ret_to_main_menu_prompt()
    elif choice == "3":
        search_contact_record()
        ret_to_main_menu_prompt()
        show_main_menu()
    elif choice == "4":
        search_contact_to_delete()
        show_main_menu
    elif choice== "0":
        cls()
        print_message("Thanks for using Phone Agenda")
        sys.exit()
    else:
        cls()
        print_message("Wrong choice, Please Enter [0 to 4]")
        ret_to_main_menu_prompt()
        show_main_menu()
        
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    print_banner("SEARCH CONTACT")
    search_name = input("Enter first and last name for Searching contact record: ")
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in your Agenda with name = " + search_name )

def input_firstname():
    ''' First name '''
    first_name = input("Enter First name ")
    return first_name

def input_lastname():
    ''' Last name '''
    last_name = input("Enter Last name ")
    return last_name


def enter_contact_record():
    ''' It  collects contact info first name, last name, email and phone '''
    print_banner("ADD NEW CONTACT")
    first = input_firstname()
    last = input_lastname()
    phone = input('Enter Phone number ')
    contact = (first + " " + last + ", " + phone + "\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print_message( "This contact " + contact + "has been added successfully!")
    
def enter_contact_record_again():
    '''Ask if you want to add another contact or not'''
    print_banner("DO YOU WANT TO ADD ANOTHER CONTACT?")
    print ("[Enter 1 or 2]\n"+
    "Enter 1 to add another contact\n"+
    "Enter 2 if you dont't want to add another contact"
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_contact_record()
        ret_to_main_menu_prompt() 
        enter_contact_record_again()
    elif choice == "2":
        show_main_menu()

def ret_to_main_menu_prompt():
    input("Press Enter to continue ...") 

def search_contact_to_delete():
    ''' This function is used to searches and delete a specific contact record '''
    print_banner("DELETE CONTACT")
    search_name = input("Enter first and last name for Searching contact record: ")
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
    
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            print_message ("[Enter 1 or 2]\n"+
            "Enter 1 to delete the contact\n"+
            "Enter 2 if you want to keep it")
            choice = input("Enter your choice: ")
            if choice == "1":
                del file_contents[get_line_number(line, file_name)]
                new_file = open(file_name, "w+")
                for line in file_contents:
                    new_file.write(line)
                new_file.close()
                print_message("Contact was successfully deleted.")
                ret_to_main_menu_prompt()
                show_main_menu()
                
            elif choice == "2":
                show_main_menu()
                
            else:
                cls()
                print_message("[Sorry, wrong number.]")
                ret_to_main_menu_prompt()
                show_main_menu()
    if found == False:
        print_message("There's no contact Record in your Agenda with name = " + search_name )
        ret_to_main_menu_prompt
        show_main_menu()

def get_line_number(phrase, f_name):
    with open(f_name) as f:
        for i, line in enumerate(f, 0):
            if phrase in line:
                return i

show_main_menu()

file1.close()