            #   PROJECT
# create a program to  read and write into a text file 

# the program should prompt the user to enter the name of the text file 
# if the file exist it should let the user know and allow the user name changes into the file by adding content or 
# changing word in the file 

# if the file doesn't exist it should create the file and allow the user to be able to write into the file by adding
# content or changing the words of the file. 

# before a user is able to make any changes to a file they should see the content of the file.


# read the file -> try the except error 
# if file exists -> open file in append -> allow user add text to the file 
# print the content and allow user to change the content (a word)
# if not exist-> create the file in except block-> allow user to write file
# print file content and allow for changes


filename= input('enter name of file')
try:
    file= open (filename)
except FileNotFoundError as e:
    print("file not found")
    cmd =input ("create file y\n: ")
    if cmd =="y":
        file = open(filename, "w")
        choice =input("write to file? y/n:")
        if choice =="y":
            while True:
                line =input ("type here:")
                if line == "done":
                    file.close()
                    break
                else:
                    file.write (line+ "\n")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

                
        
        
