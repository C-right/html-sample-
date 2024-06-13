##HOW TO CREATE AND EXTRACT PAGES IN PDF CONTNUATION OF FILE HADDNLING

# from PyPDF2 import PdfReader
# # print(PdfReader)
# note = []
# reader = PdfReader ("params.pdf")
# content_pages = reader.pages[1].extract_text() ##THIS COMMAND WILL HELP U ACCESS THE PAGES
# note.append(content_pages) ##THIS WILL
# print(content_pages)

# from PyPDF2 import PdfReader
# # print(PdfReader)
# notes = []
# reader = PdfReader ("params.pdf")
# page1 = reader.pages[0].extract_text() ##THIS COMMAND WILL HELP U ACCESS THE PAGES
# page2= reader.pages [1].extract_text()
# notes.append(page1) ##THIS WILL
# notes.append(page2)
# print(note[1])
##ITERATE THROUGH THE WORK TO HAVE A SINGLE PAGE
# for note in notes:
#     print(note) ##THIS COMMAND WILL PRINT ALL THE PAGES
#     with open ("extracted.pdf", "w") as file: ##THIS WILL ENABLE YOU EXTRACT THE NEW PAGES
#         file.write(note)
#         file.close()
## TO ADD TO THE PDF ALREADY EXISTING, DO THIS
# for note in notes:
#     print(note) ##THIS COMMAND WILL PRINT ALL THE PAGES
#     with open ("extracted.pdf", "w") as file: ##THIS WILL ENABLE YOU EXTRACT THE NEW PAGES
#         file.write("""
#                     my extracted content can also be added here

# """)
#         file.write(note)
#         file.close()

# # FILE HANDLING CLASS WITH DR 
# fileobject = open("users.txt", "w") ##this approach requres you to close the file 

# fileobject.write ("This is the first statement")

# fileobject.close() 

with open ("users.txt", "w") as fileobject: ##THIS IS THE BEST APPROACH TO CREATE FILE AND IT DOES NOT REQUIRE YOU TO CLOSE
    fileobject.write("This is the first statement")

    print("..........welcome to the jounalist app😃 .............")
    print("This app let you create and manage a simple note")
    username = input ("Please enter your name: ")
    print("Welcome to the jounalist app " + username + "!")

    print("""
    .............................Menu Options😂........................
          1. create note
          2. Edit note
          3. Delete note
    """)

    option = input("Please select an option: ")

    option = int(option) ##you typecast integial to string

    if option != 1 and option !=2 and option != 3:
        print("Invalid menu option")
        print("Please try again")
    else:
        if option == 1:
        ##create note
            note_name = input("Enter the note name: ")

            print("You are creating note " + note_name)

            with open(note_name, "w") as fileobject:
                content = input("Enter file content: ")
                fileobject.write(content)
                pass
            print("Note created successfully🤣")

        elif option == 3:
             import os
             note_to_be_deleted = input("Enter note to be deleted: ")
             os.remove(note_to_be_deleted)
             print("Note" + note_to_be_deleted + "deleted successfully😆")

        elif option ==2:
            new_data = input("edit file")
            print("about to edit note " + new_data)
            with open(new_data, "a") as fileobject:
             new_content = input("Enter new file content: ")
             fileobject.write(new_content)
             pass
            print("Successful")

            




# # TO CHECK IF A FILE EXIST DO THIS
# if os.path.isfile(note_to_be_deleted):
#     os.remove(note_to_be_deleted)
#     print("Note" + note_to_be_deleted + " deleted successfully")
# else:
#     print("Invalid input. Note does not exist")