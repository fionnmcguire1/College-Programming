
#Fionn Mcguire
#C13316356
#DT211/2
#OOP assignment (Income predictor)


#Importing the file from the server
import string, httplib2
data_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

#Creating a class used for reading data elements into the from both the line comparing and the line compared against.

class testing:
    def __init__(self,age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income):
            self.age = age
            self.work_class = work_class
            self.fnlwgt = fnlwgt
            self.education = education
            self.education_number = education_number
            self.marital_status = marital_status
            self.occupation = occupation
            self.relationship = relationship
            self.race = race
            self.sex = sex
            self.capital_gain = capital_gain
            self.capital_loss = capital_loss
            self.hours_per_week = hours_per_week
            self.native_country = native_country
            self.income = income

#These variables must be initialised as zero and cannot be reset
#for the rest of the program duration. This is why i have them here instead of inside the while loops

total_probability_of_above_50 = 0
total_probability_of_below_50 = 0
right = 0
wrong = 0
accuracy = 0       

#Storing the file in cache file
# Reading how many lines are in the file

try:
    h = httplib2.Http(".cache")
    data_headers, data = h.request(data_url)

    #making the file a list
    data = data.decode().split("\n")

    #This is not a requirement of the program but it helps me
    #acertain where in the list the program is processing it also tells me i have read
    # the file correctly
    countlines = 0
    for line in data:
        countlines += 1
        
    print('Number of lines is: {0}'.format(countlines))

    
#testing each line of data from the start against the training loop
    
    test_loop = 0
    countlines = 0

    #This will be the loop which takes a line from data and compares
    #it with the rest of the file
    #to do: take that nuumber out
    
    while test_loop < 32560:
        
#setting variabes to 0 these are pretty much all counters
        over = 0
        under = 0
        probability = 0
        probability_above = 0
        probability_below = 0
        probability_above_counter = 0
        
        
        total_age = 0
        total_age_above = 0
        
        
        total_work_class = 0
        total_work_class_above = 0
        
            

        total_education_number = 0
        total_education_number_above = 0
        

        total_marital_status = 0
        total_marital_status_above = 0
        

        total_occupation = 0
        total_occupation_above = 0
        
        total_relationship = 0
        total_relationship_above = 0
        
        total_race = 0
        total_race_above = 0
        
        total_sex = 0
        total_sex_above = 0
        
        total_capital_gain = 0
        total_capital_gain_above = 0
        
        total_capital_loss = 0
        total_capital_loss_above = 0
        
        total_hours_per_week = 0
        total_hours_per_week_above = 0
        
        countlines += 1
        print(countlines)
        test_loop += 1

       #reading an element in the list data into one variable and stripping that variable into a load of words divided by ,
        
        a = data[test_loop]
        #splitting the line into a set of variable
        b = a.split(",")

        #making the split variable into various variables

        #making that line into the 15 variables
        age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income = b
        test_line = testing(age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income)


        ''' instead of the if i = 1 statement i origionally had the if statement below which is commented out
        The reason for this was i went through the entire file and checked all the lines below 50K
        From here i got the total probability and divided that by the variable 'under' (The variable
        under counted how many lines in the file were under 50K) This gave me an average value
        for the lines which were under 50K. I then did the same for >50K. I took these two results and subtracted them.
        The distance between the two values divided by 2 gave me a figure which i added onto the lower figure
        This gave me the midpoint'''
        #if test_line.income == ' <=50K':
        i = 1
        if i == 1:
            #running through the trainig data to recognise patterns in the data file
            
            train_loop = 0
            while train_loop < 32560:
                
                train_loop += 1
                c = data[train_loop]
                d = c.split(",")
                
                age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income = d
                train_line = testing(age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income)

                '''The following if statements increment 2 counters
                total_age is a counter which increments the amount
                of times that exact age turns up in the file. total_age_above
                is incremented if the line which that age is on is above 50K
                This gives the probability of the line being over 50K.'''
                if test_line.age == train_line.age:
                    total_age += 1

                    if train_line.income == ' >50K':
                        total_age_above += 1

                                
                if test_line.work_class == train_line.work_class:
                    total_work_class+= 1

                    if train_line.income == ' >50K':
                            total_work_class_above += 1
                                
                    if test_line.education_number == train_line.education_number:
                        total_education_number += 1

                        if train_line.income == ' >50K':
                            total_education_number_above += 1
                                

                    if test_line.marital_status == train_line.marital_status:
                        total_marital_status += 1

                        if train_line.income == ' >50K':
                            total_marital_status_above += 1

                    if test_line.occupation == train_line.occupation:
                        total_occupation += 1 

                        if train_line.income == ' >50K':
                            total_occupation_above += 1

                    if test_line.relationship == train_line.relationship:
                        total_relationship += 1

                        if train_line.income == ' >50K':
                            total_relationship_above += 1

                    if test_line.race == train_line.race:
                        total_race += 1

                        if train_line.income == ' >50K':
                            total_race_above += 1

                    if test_line.sex == train_line.sex:
                        total_sex += 1

                        if train_line.income == ' >50K':
                            total_sex_above += 1

                    if test_line.capital_gain == train_line.capital_gain:
                        total_capital_gain += 1

                        if train_line.income == ' >50K':
                            total_capital_gain_above += 1

                    if test_line.capital_loss == train_line.capital_loss:
                        total_capital_loss += 1

                        if train_line.income == ' >50K':
                            total_capital_loss_above += 1

                        if test_line.hours_per_week == train_line.hours_per_week:
                            total_hours_per_week += 1

                            if train_line.income == ' >50K':
                                total_hours_per_week_above += 1


            
            '''The following set of equations give a decimal value of the probability that element in the line
             will be above 50K. The round figure gets that value and rounds it off to 3 decimal points'''   
            age_result = total_age_above/total_age
            age_result=round(age_result,3)
                
            work_class_result = total_work_class_above/total_work_class
            work_class_result=round(work_class_result,3)
                
            education_number_result = total_education_number_above/total_education_number
            education_number_result=round(education_number_result,3)
                
            marital_status_result = total_marital_status_above/total_marital_status
            marital_status_result=round(marital_status_result,3)
                
            occupation_result = total_occupation_above/total_occupation
            occupation_result=round(occupation_result,3)
                
            relationship_result = total_relationship_above/total_relationship
            relationship_result=round(relationship_result,3)
                
            race_result = total_race_above/total_race
            race_result=round(race_result,3)
                
            sex_result = total_sex_above/total_sex
            sex_result=round(sex_result,3)
                
            capital_gain_result = total_capital_gain_above/total_capital_gain
            capital_gain_result=round(capital_gain_result,3)
                
            capital_loss_result = total_capital_loss_above/total_capital_loss
            capital_loss_result=round(capital_loss_result,3)
                
            hours_per_week_result = total_hours_per_week_above/total_hours_per_week
            hours_per_week_result=round(hours_per_week_result,3)
                

            #This equation gets the probability of that combination of elements (line) being over 50K  
            probability = age_result + work_class_result + education_number_result + marital_status_result + occupation_result + relationship_result + race_result + sex_result + capital_gain_result + capital_loss_result + hours_per_week_result
            probability = probability/11

            #The variables below were used for making the average probability value for the entirity of the above or below 50K
            #total_probability_of_above_50 = total_probability_of_above_50+probability
            #total_probability_of_above_50=round(total_probability_of_above_50,4)

            #The figure inside these if statements is the midpoint as i have calculated
            
            
            if probability > 0.2702:
                if train_line.income == ' <=50K':
                    right +=1
                else:
                    wrong +=1
            if probability < 0.2702:
                if train_line.income == ' >50K':
                    right +=1
                else:
                    wrong +=1
                    
            #This equation calculates the accuracy of the income predictor (Not a requirement)
            #The program proves to be 67.7% accurate 
                    
            accuracy = right/countlines
            print('Correct {0} Incorrect {1} Accuracy {2}%'.format(right,wrong,accuracy))
            
            

        


    '''The two statements below are used as i said before to count how many lines are over and how many lines are under '''

        
    #print('over {0}'.format(over))
    #print('under {0}'.format(under))


    




        

  
        
        
except httplib2.HttpLib2Error as e:
        print(e)
