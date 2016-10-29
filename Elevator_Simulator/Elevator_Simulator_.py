

#Fionn Mcguire
#C13316356
#DT211/2
#OOP assignment (Elevator simulator)

import random

#check if this is a letter or a stupid ass decimal
nope = 0
while nope == 0:
    floors = int(input("How many floors would you like?"))
    
    if floors > 163:
        print("The tallest building in the world is 163 stories. Pick a lower number")
    elif floors < 0:
        print("There are no negative floors in this building")
    else:
        nope = 1
        
nope = 0
while nope == 0:
    customers = int(input("How many people are going to use the elevator today?"))
    if customers > 1630:
        print("Be realistic. Try again")
    elif customers < 0:
        print("There can't be a negative amount of people in the building")
    else:
        nope = 1
Matrix =  [[0 for x in range(5)] for x in range(int(customers))]

def getting_variables():
    
    floors = int(input("How many floors would you like?"))
    customers = int(input("How many people are going to use the elevator today?"))
    Matrix =  [[0 for x in range(5)] for x in range(int(customers))]
    return(floors,customers,Matrix)




class building:
    """
    This class building is used to represent the building and the list of people inside it
    This class accepts floors, and customers and from those two the matrix is created which
    contains 5 values
    person id was used by myself to fix bugs ect it is not used in the program otherwise
    Crucially the matrix has two other variable floor_on and floor_to these obviously represent
    the floor the customer is currently on and the destination floor for that user. These are
    randomly assigned variables between 1 - (the number of floors the user has specified)
    next is the on_elevator variable which tells the program if that customers is on the
    elevator or not.
    """
    
    def __init__(self, floors, customers,Matrix):
        self.floors = floors
        self.customers = customers
        self.Matrix =  Matrix



class people(building):
    def __init__(self, floors, customers, Matrix):
        building.__init__(self, floors, customers, Matrix)
    """
    The people class takes care of populating the matrix of customers as specified in the
    building docstring. This class inherits the 3 variables from the building string and
    develops the matrix. This class also prints how many customers are on each floor.

    """
        
    """
    The method below is the method which populates the list
    """
    def array_of_customers(i,customers, person_id, floor_on, floor_to, finished, on_elevator, Matrix):


                    
        Matrix[i][0] = person_id
        Matrix[i][1] = floor_on
        Matrix[i][2] = floor_to
        Matrix[i][3] = finished
        Matrix[i][4] = on_elevator

    person_id =0
    floor_on =0
    floor_to = 0
    finished = 0
    on_elevator = 0
    i = 0

    """
    This while loop populates each line of the list over and over until the list is complete
    """

    while i < int(customers):
                
        person_id =i+1
        floor_on = random.randint(1, int(floors))
        floor_to = random.randint(1, int(floors))
                
                
            
        array_of_customers(i,int(customers),person_id,floor_on,floor_to,finished, on_elevator, Matrix)
                
        i = i+1
    
    i = 0
    j = 0
    count =0

    while i < floors:
        
        while j < customers:
            if Matrix[j][1] == i+1:
                count+=1
            j+=1
        if count == 0:
            print("Floor {0} has no one on it".format(i+1))  
        elif count == 1:
            print("Floor {0} has 1 person".format(i+1))
        else:
            print("Floor {0} has {1} people".format(i+1, count))

        i+=1
        j = 0
        count = 0
        
    print("")
    print("")
    print("")


class elevator(people):
    """
    This class inherits the customers matrix as it has been changed
    It also inherits the number of customers and no of floors from the people class
    which were all inherited from the building class. This class carries out all functions
    of an actual elevator. I put in an elevator max as a real elevator would have one. I briefly thought about
    assigning a random weight to each customer and having an elevator weight max instead but no one
    pays attention to those anyway so i didn't bother.
    """
    def __init__(self, floors, customers, Matrix,):
        people.__init__(self, floors, customers, Matrix)
    current_floor = 1
    finished = 0
    elevator_max = 20
    pop_of_elevator = 0
    count_finished = 0
    count_pop = 0
    
    """
    On each floor the elevator is on people must get on and off. This method
    does this while changing their finished variable (Matrix[][3]) to 1 which
    identifies to the elevator that they rode the elevator already and are done
    for the day. This method also keeps track of population of the elevator
    and increments/decrements accordingly.
    
    When reading this function
    Matrix[][1] = starting floor of that customer
    Matrix[][2] = destination floor of that customer
    Matrix[][3] = if theyre finished for the day
    Matrix[][4] = if they're on the elevator

    This function also provides feedback so you can track whats going on in the elevator
    within the program.
    """


    
    def enter_exit(current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop):

        count_on = 0
        count_off = 0        
        j = 0
        i = 0
        
        while j < customers:                
            if Matrix[j][1] == current_floor and Matrix[j][3] == 0 and Matrix[j][4] == 0:
                if pop_of_elevator < elevator_max:
                    Matrix[j][4] = 1
                    count_on+=1
                    pop_of_elevator +=1                                    
            j+=1

        j = 0
        while j < customers:
            if Matrix[j][2] == current_floor and Matrix[j][4] == 1:
                Matrix[j][3] = 1
                Matrix[j][4] = 0 
                pop_of_elevator -=1
                count_off+=1    
            j+=1

        j = 0
        while j < customers:
            if Matrix[j][3] == 1:
                count_finished +=1
            j+=1
        
        if count_pop == 1:
            print("{0} people got on at floor {1}".format(count_on, current_floor))
            print("{0} people got off at floor {1}".format(count_off, current_floor))
            print("Population of elevator: {0}".format(pop_of_elevator))
            print("{0} are done for the day".format(count_finished))
        print("")
        """ I have to return the population counter so that the counter keeps track"""        
        return (pop_of_elevator)

    """
    As the elevator starts at floor 1 the only way to go is up therfore the up algorithm is run
    first and there are alot of things here which you will not find in the down algorithm.
    The algorithm i designed to run the elevator is people get on on the first floor. Out of these people
    The up method figures out what the maximum floor is i.e. the highest destination floor. Then the
    elevator goes up 1 floor at a time and records how many get on and off by running the enter_exit method
    if no one is getting on or off at a floor a message is displayed and the elevator skipps that floor.
    Once the current floor = max floor the elevator runs down algorithm which gets the lowest floor
    and runs the exact same way of the up algorithm. These two algorithms run until every Matrix[][3] = 1
    i.e. until everyone is finished. The a message is displayed signifying the program has finished running successfuly
    
    """


    def up(enter_exit,current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop):
        j = 0
        max_floor_in_elevator = 1
        count_pop = 1 
        count_noone_on = 0

        while j < customers:
            if Matrix[j][4] == 0 and Matrix [j][3] == 0:
                count_noone_on +=1
                if count_noone_on == customers:
                    print("Current floor is: {0}".format((current_floor)))
                    pop_of_elevator = enter_exit(current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop)
                    current_floor +=1
                    
            j+=1
        j = 0
                    
               
        
        while j < customers:
            if Matrix[j][4] == 1 :
                if Matrix[j][2] > max_floor_in_elevator:
                    max_floor_in_elevator = Matrix[j][2]
                    
            j+=1
        print("Max floor is: {0}".format(max_floor_in_elevator))
        j = 0
        
        
        while current_floor < (max_floor_in_elevator + 1):
            
            noone = 1
            
            
            j = 0
            while j < customers:
                
                if Matrix[j][4] == 1:    
                    if Matrix[j][1] == current_floor or Matrix[j][2] == current_floor:
                        print("Current floor is: {0}".format((current_floor)))
                        pop_of_elevator = enter_exit(current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop)
                        j = customers
                        noone = 0
                j+=1 
            if noone ==1:
                print("")
                print("No one getting on or off floor {0}".format(current_floor))
                print("")
                        
            current_floor +=1
        current_floor -=1

        print("")
        print("")
        print("")

        """I have to retrun the current floor and pop counter so that the program can keep track of these in real time"""        
        return (current_floor, pop_of_elevator)

    """
    This algorithm was explained in the up method docstring
    """

    def down(enter_exit,current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop):
        j = 0
        min_floor_in_elevator = floors
        count_pop = 1
        
        
         
        while j < customers:
            if Matrix[j][4] == 1 :
                if Matrix[j][2] < min_floor_in_elevator:
                    min_floor_in_elevator = Matrix[j][2]
                    
            j+=1
            
        print("Min floor is: {0}".format(min_floor_in_elevator))
        j = 0
        
        while current_floor > (min_floor_in_elevator - 1):
            j = 0
            noone = 1
            while j < customers:
                if Matrix[j][4] == 1 :  
                    if Matrix[j][1] == current_floor or Matrix[j][2] == current_floor:
                        print("Current floor is: {0}".format((current_floor)))
                        pop_of_elevator = enter_exit(current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop)
                        j = customers
                        noone = 0
                j+=1  
            if noone ==1:
                print("")
                print("No one getting on or off floor {0}".format(current_floor))
                print("")
                         
            current_floor -=1
            
        current_floor +=1

        print("")
        print("")
        print("")
        
        

        return (current_floor, pop_of_elevator)


    done = 0
    while done < customers:
        j = 0
        done = 0
        while j < customers:
            if Matrix[j][3] == 1:
                done+=1
            j+=1

        if done < customers:
            current_floor, pop_of_elevator = up(enter_exit,current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop)
        j = 0
        done = 0
        while j < customers:
            if Matrix[j][3] == 1:
                done+=1
            j+=1
        if done < customers:
            current_floor, pop_of_elevator = down(enter_exit,current_floor, Matrix, elevator_max, pop_of_elevator, count_finished,count_pop)



    print("The day is over everyone has gone home.")





def create_object():
    floors, customers, Matrix = getting_variables()
    building_1 = elevator(floors,customers, Matrix)

    print(building_1)
    



def run_loop():
    
    invalid = 0

    while invalid == 0:
        print("If you would you like to run this program again please enter Y")
        print("If you would you like to close this program please enter N")
        answer = input()
        
        if answer == 'Y' or answer == 'y':
            create_object()
            invalid = 1
        elif answer == 'N' or answer == 'n':
            exit()
            invalid = 1
        else:
            print("You must enter either Y or N")
            invalid = 0

run_loop()

            
"""
Run the program a few times. Sometimes it loop infinitly because the people on the first floor wernt counted
i have no idea why. I think its something to do with them coming back down.
"""
