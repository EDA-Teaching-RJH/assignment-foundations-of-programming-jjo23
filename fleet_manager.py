# note i havent actually watched star trek so i dont have a clue if these characters and their divisions are factual

n = ["Airiam", "Jonathan Archer", "Ascencia", "Soji Asha", "Ayala"]
r = ["Lt, Commander", "Captain", "Civilian", "Civilian", "Lieutenant"]
d = ["Command", "Operations", "None", "None", "Security"]
id = ["100","101", "102", "103", "104"]


def display_roster():
    print("NAME -- RANK -- ID")
    for i in range(len(n)):
        print(f"{n[i]} -- {r[i]} -- {id[i]}")
    
    display_menu()


def add_member():
    new_n = str(input("enter name to add: ")).title().strip()
    new_r = str(input("enter rank: ")).title().strip()
    new_d = str(input("enter division: ")).title().strip()
    new_id = str(input("enter ID: ")).strip()

    n.append(new_n)
    r.append(new_r)
    d.append(new_d)
    id.append(new_id)
    
    print("New member added.")
    display_menu()


# function to remove the members from the system
def remove_member():
    #prompt the user to enter the name they would like to remove 
    query = str(input("enter ID: ")).title().strip()
    
    # while loop to make sure a valid name is entered
    while query not in id:
        print("ID is not in list.")
        query = str(input("enter ID: ")).title().strip()
    else:
       # pops the data from their respective lists
       idx = n.index(query)
       n.pop(idx)
       r.pop(idx)
       d.pop(idx)
       id.pop(idx)

    print("Member removed.")

    display_menu()

def update_rank():
    num = str(input("enter ID to update: ")).strip()
    while num not in id:
        num = str(input("enter ID to update: ")).strip()            
    else:
        new_rank = str(input("enter updated rank: ")).title().strip()
        idx = id.index(num)
        r[idx] = new_rank

    print("Rank updated.")

    display_menu()

def search_crew():
    search_condition = input("how would you like to search through the crew?(name, rank, id): ").lower()
    value = str(input("what are you searching for?: ")).title()
    found = False

    for i in range(len(n)):
        if search_condition == "name" and n[i] == value:
            print(f"{n[i]} -- {r[i]} -- {id[i]}")
            found = True
        elif search_condition  == "rank" and  r[i] == value:
            print(f"{n[i]} -- {r[i]} -- {id[i]}")
            found = True
        elif search_condition == "id" and id[i] == value:
            print(f"{n[i]} -- {r[i]} -- {id[i]}")
            found = True
    display_menu()

    if not found:
        print("No matches found")

# created the display_menu function
def display_menu():

    print("===Menu===")
    print("1 - View members")
    print("2 - add members")
    print("3 - remove member")
    print("4 - Update rank")
    print("5 - Search crew")
    print("6 - Filter By Division")
    print("7 - Calculate Payroll")
    print("8 - Count Officers")
    print("9 - Exit")

    userinput = int(input("Enter option: "))
    
    #if statements to determine what the outcome is
    if userinput == 1:
        display_roster()
    elif userinput == 2:
        add_member()
    elif userinput == 3:
        remove_member()
    elif userinput == 4:
        update_rank()
    elif userinput == 5:
        search_crew()
    elif userinput == 6:
        filter_by_div()
    elif userinput == 7:
        calculate_payroll()
    elif userinput == 8:
        count_officers()
    else:
        exit

#asks the user for their full name as their login and prints it our when done
login = str(input("Enter full name: \n")).title().strip()
print(f"Welcome {login}.")

display_menu()