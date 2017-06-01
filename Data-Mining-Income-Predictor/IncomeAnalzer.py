
#Importing the file from the server

import string, httplib2
data_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

#Creating a class used for reading data elements into the class.

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

    data = data.decode().split("\n")
    
    countlines = 0
    for line in data:
        countlines += 1
        
    print('Number of lines is: {0}'.format(countlines))

    
#testing each line of data from the start against the training loop
    
    test_loop = 0
    countlines = 0
    while test_loop < 32560:
        
#setting variabes to 0 these are pretty much all counters
        over = 0
        under = 0
        probability = 0
        probability_above = 0
        probability_below = 0
        probability_above_counter = 0
        probability_below_counter = 0
        
        total_age = 0
        total_age_above = 0
        total_age_below = 0
        
        total_work_class = 0
        total_work_class_above = 0
        total_work_class_below = 0
            

        total_education_number = 0
        total_education_number_above = 0
        total_education_number_below = 0

        total_marital_status = 0
        total_marital_status_above = 0
        total_marital_status_below = 0

        total_occupation = 0
        total_occupation_above = 0
        total_occupation_below = 0

        total_relationship = 0
        total_relationship_above = 0
        total_relationship_below = 0

        total_race = 0
        total_race_above = 0
        total_race_below = 0

        total_sex = 0
        total_sex_above = 0
        total_sex_below = 0

        total_capital_gain = 0
        total_capital_gain_above = 0
        total_capital_gain_below = 0

        total_capital_loss = 0
        total_capital_loss_above = 0
        total_capital_loss_below = 0

        total_hours_per_week = 0
        total_hours_per_week_above = 0
        total_hours_per_week_below = 0



        

        countlines += 1
        print(countlines)
        test_loop += 1

       #reading an element in the list data into one variable and stripping that variable into a load of words divided by ,
        
        a = data[test_loop]
        b = a.split(",")

        #making the split variable into various variables
        
        age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income = b
        test_line = testing(age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income)

        i = 1
        if test_line.income == ' <=50K':
            #running through the trainig data to recognise patterns in the data file
            
            train_loop = 0
            while train_loop < 32560:
                
                train_loop += 1
                c = data[train_loop]
                d = c.split(",")
                
                age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income = d
                train_line = testing(age,work_class,fnlwgt,education,education_number,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,income)

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


            
                
            age_result = total_age_above/total_age
            age_result=round(age_result,3)
                #print('Age',age_result)
            work_class_result = total_work_class_above/total_work_class
            work_class_result=round(work_class_result,3)
                #print('Work Class',work_class_result)
            education_number_result = total_education_number_above/total_education_number
            education_number_result=round(education_number_result,3)
                #print('Education',education_number_result)
            marital_status_result = total_marital_status_above/total_marital_status
            marital_status_result=round(marital_status_result,3)
                #print('married',marital_status_result)
            occupation_result = total_occupation_above/total_occupation
            occupation_result=round(occupation_result,3)
                #print('occupation',occupation_result)
            relationship_result = total_relationship_above/total_relationship
            relationship_result=round(relationship_result,3)
                #print('relationship',relationship_result)
            race_result = total_race_above/total_race
            race_result=round(race_result,3)
                #print('race',race_result)
            sex_result = total_sex_above/total_sex
            sex_result=round(sex_result,3)
                #print('sex',sex_result)
            capital_gain_result = total_capital_gain_above/total_capital_gain
            capital_gain_result=round(capital_gain_result,3)
                #print('Cap gain',capital_gain_result)
            capital_loss_result = total_capital_loss_above/total_capital_loss
            capital_loss_result=round(capital_loss_result,3)
                #print('Cap loss',capital_loss_result)
            hours_per_week_result = total_hours_per_week_above/total_hours_per_week
            hours_per_week_result=round(hours_per_week_result,3)
                #print('hours',hours_per_week_result)
                
            probability = age_result + work_class_result + education_number_result + marital_status_result + occupation_result + relationship_result + race_result + sex_result + capital_gain_result + capital_loss_result + hours_per_week_result
            probability = probability/11
            print(probability)
            total_probability_of_above_50 = total_probability_of_above_50+probability
            total_probability_of_above_50=round(total_probability_of_above_50,4)

            #if probability > 0.56405:
             #   if train_line.income == ' <=50K':
              #      right +=1
               # else:
                #    wrong +=1
            #if probability < 0.56405:
             #   if train_line.income == ' >50K':
              #      right +=1
              #  else:
               #     wrong +=1
            #accuracy = right/countlines
            #print('Correct {0} Incorrect {1} Accuracy {2}%'.format(right,wrong,accuracy))
            
            
        #print('Prob: {0} Income: {1}'.format(probability,test_line.income))
            
     
    print(total_probability_of_above_50)
    
           
            
     #   if test_line.income == ' >50K':
      #      probability_above = probability_above+probability
       #     probability_above_counter += 1
                
       # else:
        #    probability_below = probability_below+probability
         #   probability_below_counter += 1
       

        
        
                
        
        #print('above {0} counter {1}'.format(probability_above,probability_above_counter))        
        #probability_above = probability_above/probability_above_counter
        #probability_below = 1 - probability_above
        

        #distance =  probability_below - probability_above
       # midpoint = distance/2
        
        #midpoint = probability_above+midpoint
       # print(midpoint)
        
        #print ('midpoint{0}above{1}below{2}'.format(midpoint,probability_above,probability_below))
        
       # error_check_true = 0
       # error_check_false =0
       # percentage_correct = 0
        #total_corrected = 0

        #if test_line.income == ' >50K':
          #  print('Should Be Greater')
         #   error_check_true += 1
        #else:
          #  print('Should be Less Than')
         #   error_check_false +=1
        

        #if probability < midpoint:
          #  print('Greater')
          #  error_check_true +=1
         #   print('Midpoint: {0} Probability {1}'.format(midpoint,probability))
        #else:
         #   print('Less')
         #   error_check_false +=1

        #if error_check_true == 2:
          #  percentage_correct +=1
         #   total_corrected +=1
        #if error_check_false == 2:
        #    percentage_correct +=1
       #     total_corrected +=1
      #  else:
     #       total_corrected += 1

    #percentage_correct = percentage_correct/total_corrected
            

        


        
    #print('over {0}'.format(over))
    #print('under {0}'.format(under))


    

    
    ##there is a lot of shit to be done weigh in the probability of each factor and the probability of the entire thing



        

  
        
        
except httplib2.HttpLib2Error as e:
        print(e)
