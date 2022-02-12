from re import A

def vacuum_cleaner():

    cost = 0

    location_input = input("Enter Location of Vacuum:\n") 
    status_input = input(f"Enter status of {location_input}:\n") 
    status_input_complement = input("Enter status of 2nd room:\n")
    status_input_complement2 = input("Enter status of 3rd room:\n")

    goal_state = {'A': '0', 'B': '0', 'C': '0'}
    
    if location_input=='A':
        goal_state["A"]=status_input
        goal_state["B"]=status_input_complement
        goal_state["C"]=status_input_complement2
        print(f"INITIAL STATE : {goal_state}")

    elif location_input=='B':
        goal_state["A"]=status_input_complement
        goal_state["B"]=status_input
        goal_state["C"]=status_input_complement2
        print(f"INITIAL STATE : {goal_state}")
        
    elif location_input=='C':
        goal_state["A"]=status_input_complement2
        goal_state["B"]=status_input_complement
        goal_state["C"]=status_input
        print(f"INITIAL STATE : {goal_state}")

    if location_input == 'A':

        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1                 
            print("Cost for CLEANING A " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                      
                print("COST for moving RIGHT" + str(cost))
                goal_state['B'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location B is already clean.")

            if status_input_complement2 == '1':
                print("Location C is Dirty.")
                print("Moving RIGHT to the Location C. ")
                cost += 1                      
                print("COST for moving RIGHT" + str(cost))
                goal_state['C'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location C has been Cleaned. ")
                    
            else:
                print("No action" + str(cost))
                print("Location C is already clean.")

        if status_input == '0':
            print("Location A is already clean ")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                       
                print("COST for moving RIGHT " + str(cost))
                goal_state['B'] = '0'
                cost += 1                       
                print("Cost for SUCK" + str(cost))
                print("Location B has been Cleaned. ")

            else:
                print("No action " + str(cost))
                print(cost)
                print("Location B is already clean.")

            if status_input_complement2 == '1':
                print("Location C is Dirty.")
                print("Moving RIGHT to the Location C. ")
                cost += 1                      
                print("COST for moving RIGHT" + str(cost))
                goal_state['C'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location C has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location C is already clean.")



    elif location_input == 'B':
        print("Vacuum is placed in location B")
        
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1  
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1 
                print("COST for moving LEFT" + str(cost))
                goal_state['A'] = '0'
                cost += 1  
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned.")

            else:
                print("No action" + str(cost))
                print("Location A is already clean.")

            if status_input_complement2 == '1':
                print("Location C is Dirty.")
                print("Moving RIGHT to the Location C. ")
                cost += 1                      
                print("COST for moving RIGHT" + str(cost))
                goal_state['C'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location C has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location C is already clean.")

        if status_input == '0':
            print("Location B is already clean ")

            if status_input_complement == '1':  
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("COST for moving LEFT " + str(cost))                
                goal_state['A'] = '0'
                cost += 1  
                print("Cost for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print("Location A is already clean.")

            if status_input_complement2 == '1':    
                print("Location C is Dirty.")
                print("Moving RIGHT to the Location C. ")
                cost += 1                      
                print("COST for moving RIGHT" + str(cost))
                goal_state['C'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location C has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location C is already clean.")

    else:
        print("Vacuum is placed in Location C")

        if status_input == '1':
            print("Location C is Dirty.")
            goal_state['C'] = '0'
            cost += 1                 
            print("Cost for CLEANING C " + str(cost))
            print("Location C has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving LEFT to the Location B. ")
                cost += 1                      
                print("COST for moving LEFT" + str(cost))
                goal_state['B'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location B is already clean.")

            if status_input_complement2 == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1                      
                print("COST for moving LEFT" + str(cost))
                goal_state['A'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location A is already clean.")

        if status_input == '0':
            print("Location C is already clean ")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving LEFT to the Location B. ")
                cost += 1                       
                print("COST for moving LEFT " + str(cost))
                goal_state['B'] = '0'
                cost += 1                       
                print("Cost for SUCK" + str(cost))
                print("Location B has been Cleaned. ")

            else:
                print("No action " + str(cost))
                print(cost)
                print("Location B is already clean.")

            if status_input_complement2 == '1':
                
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1                      
                print("COST for moving LEFT" + str(cost))
                goal_state['A'] = '0'
                cost += 1                      
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location A is already clean.")


    print(f"GOAL STATE: {goal_state}")
    print("Performance Measurement: " + str(cost))


vacuum_cleaner()
