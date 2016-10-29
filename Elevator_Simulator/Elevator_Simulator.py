

#Fionn Mcguire
#C13316356
#DT211/2
#OOP assignment (Elevator simulator)

import random

#check if this is a letter or a stupid ass decimal

"""
floors = int(input("How many floors would you like?"))
customers = int(input("How many people are going to use the elevator today?"))
Matrix =  [[0 for x in range(5)] for x in range(int(customers))]

def getting_variables():
    
    floors = int(input("How many floors would you like?"))
    customers = int(input("How many people are going to use the elevator today?"))
    Matrix =  [[0 for x in range(5)] for x in range(int(customers))]
    return(floors,customers,Matrix)"""




class building(object):
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

    def __init__(self):
        self.floors = 0
        self.customers = 0
        self.Matrix =  [0][0]
        
        def getting_variables():
    
            floors =int(input("How many floors would you like?"))
            customers = int(input("How many people are going to use the elevator today?"))
            Matrix = [[0 for x in range(5)] for x in range(int(customers))]
            return(floors,customers,Matrix)
        floors,customers,Matrix = getting_variables()

        self.floors = floors
        self.customers = customers
        self.Matrix = Matrix

        print(self.floors)
        
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
    print(building.customers)
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

    while i < building.customers:
                
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



building1 = building()
#print(building1)


