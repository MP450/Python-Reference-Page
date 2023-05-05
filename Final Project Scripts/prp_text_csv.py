# Writing to text files

TheFile=open("test.txt","w") 
TheFile.write("Row 1\n") 
TheFile.write("Row 2\n") 
TheFile.write("Row 3\n") 
TheFile.close()

# Writing to csv files

TheFile=open("test_csv.csv","w") # open the file for writing
TheFile.write("1,2,3,4\n") # write a string to the file
TheFile.write("5,6,7,8\n")
TheFile.close() # close the file

##########

TheFile=open("test2.csv","w") 
Index=0
while (Index<10): # go through the code below for each value from 0 to 9     
    TheFile.write(format(Index)+"\n")  # Convert the Index to a string and write a line to the file
    Index+=1
TheFile.close()

##########

TheFile=open("test3.csv","w") 
Row=0 # start the row counter at 0
while (Row<10): # write out 10 rows (0 to 9)
    Column=0 # start the column counter at 0
    while (Column<4): # write out 4 columns (0 to 3)
        TheValue=Row*Column # creating an interesting value
        if (Column>0): # don't write out the comma on the first column, just the subsequent ones
            TheFile.write(",") 
        TheFile.write(format(TheValue)) # convert the value to a string and write it to the file
        Column+=1 # move to the next column
    TheFile.write("\n") # move to the next line
    Row+=1 # move to the next line
TheFile.close()

##########

TheFile=open("Test.csv","w") # open the file for writing

TheFile.write("Latitude,Longitude\n") # write the header line

Count=0 # setup a counter
while (Count<5): # loop until the counter is 5
    TheFile.write(format(Count+40)+","+format(Count-120)+"\n") # write two columns of data
    Count+=1 # add one to the counter

TheFile.close() # close the file

##########

# Using csv library to write files
import csv

TheFile=open('Test12.csv', 'w') # open the file for writing

# Create a CSV writer object
writer = csv.writer(TheFile,quoting=csv.QUOTE_NONNUMERIC, lineterminator = '\n') # just quote non-numbers and use "newline" for the end of line character

# write out each row of the CSV file.
writer.writerow(['SN', 'Person', 'DOB']) # write the header line
writer.writerow([1, 'John', '18/1/1997']) # specify the rows as lists
writer.writerow([2, 'Marie','19/2/1998'])

# close the file
TheFile.close()

##########

# Split comma delimited strings

TheString="Rock,Sand,Shale" # create a string delimited with commas
TheElements=TheString.split(",") # split the string at each comma
print(TheElements) # print the elements in the string
print(TheElements[1]) # print the second element in the string

##########

TheFile=open("test.txt","r") # open the file for reading (thus the "r")
TheOutputFile=open("output.csv","w") # open the output file for writing

TheOutputFile.write("Column1","Column2") # output the header line

NumLines=0
TheLine=TheFile.readline() # read the first line in the file
while ((TheLine!="") and (NumLines<100)): # while the line is not blank, go through this loop
    print(TheLine) 
    TheLine=TheFile.readline() # read the next line in the file

    TheCells=TheLine.split("\t") # split up the line

    # do conversions on the cells here.

    TheOutputFile.write(TheCells[0]+","+TheCells[1]) # output the line to the output file

    NumLines+=1 # add one to count the number of lines read

TheFile.close()
TheOutputFile.close() # close the file

print("Read "+format(NumLines)+" lines from the file")

