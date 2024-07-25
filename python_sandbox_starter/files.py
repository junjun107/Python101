# Python has functions for creating, reading, updating, and deleting files.


#open a file 
myFile = open('myfile.txt','w')

#get info of file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)


#write to file
myFile.write("I love Python")
myFile.write(' and JavaScript')
myFile.close()