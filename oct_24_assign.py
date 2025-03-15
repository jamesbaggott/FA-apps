#James Baggott

#FA Computing ASsignment 10/10/24



#Initialising varibles

firstname = []

surname = []

grade = []



#Defining a function to read the csv file

def readFile(filename):

    with open(filename, 'r') as csv_file:

        for row in csv_file.readlines():



            #Setting length of "row"

            row = row[0:-1]

            #Initialising colums + splitting

            colums = row.split(",")

            #Setting firstname to append to the first colum

            firstname.append(colums[0])

            #Setting surname to append to the second colum

            surname.append(colums[1])

            #Setting grade to append to the third colum

            grade.append(colums[2])

            #displaying first colum

            print(colums[0])

            #displaying second colum

            print(colums[1])

            #displaying third colum

            print(colums[2])





#activate function

readFile("csv.csv")





#defining function to find the max in the "grade" colum, aswell as finding the position in the list the max is

def FindMaxSort():

    max = int(grade[0])

    #loop for the length of (grade)

    for i in range(0, len(grade)):

        #if a value in grade is greater than the max variable

        if int(grade[i]) > max:

            #set the max to that value

          max = int(grade[i])

    #display the max      

    print(max)



    #initialising variables

    i = 0

    global index

    index = -1

    #conditional loop finding position of (max)

    while i < len(grade):

        if int(grade[i]) == max:

            index = i

        #counter    

        i = i + 1

    print (index)





#activating function

FindMaxSort()





#defining function to create a textfile and write inside of it

def TextWrite(filename, text, firstname, surname, grade):

    with open(filename, "w") as text_file:

        #writing the text

        text_file.write(text)

        text_file.write(' ')

        #writing the firstname

        text_file.write(firstname)

        text_file.write(' ')

        #writing the surname

        text_file.write(surname)

        text_file.write(' ')

        #writing the grade

        text_file.write(grade)

       

#activating function

TextWrite("test.txt", "The person with the highest score is", firstname[index], surname[index], grade[index])
