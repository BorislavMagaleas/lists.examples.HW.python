students_first_name = []                                                             ### Four lists created to store the specific parts of the data introduced by the user
students_last_name  = []
students_age        = []
student_mark        = []
 
Data = input("Introduce studnet's data (first name, last name, age, mark) ").split() ### User introduces the input data about the students -> Data is stored in form of a list

for i in range(len(Data)):
    if i % 4 == 0:                                                                   ### Finding of the specific information according to the index 
        students_first_name.append(Data[i])                                          ### The information found is added to the corresponding list 
    elif i % 4 == 1:
        students_last_name.append(Data[i])
    elif i % 4 == 2:
        if int(Data[i]) >= 18 and int(Data[i]) <= 30:                                ### In case if input data (age) is not relevant -> "IIDT" (Invalid Input Data) is added to the list instead of the input value
            students_age.append(Data[i])
        else:
            students_age.append("IIDT")
    elif i % 4 == 3:
        if int(Data[i]) >= 1 and int(Data[i]) <= 10:                                 ### In case if input data (mark) is not relevant -> "IIDT" (Invalid Input Data) is added to the list instead of the input value
            student_mark.append(Data[i])
        else:
            student_mark.append("IIDT")

for s in range(len(students_first_name)):                                            ### All information collected in the lists is printed in form of a "table"
    print("\t", students_first_name[s], students_last_name[s], students_age[s], student_mark[s])
