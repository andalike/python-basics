with open("notes.txt","w") as file:
    file.write("Line 1 : Calss on 16-Feb\n")
    file.write("Class 2 of Python, First in Writing File\n")

with open("notes.txt","r") as file:
    content = file.read()
    print("File Content Iteration 1")
    print(content)

with open("notes.txt","a") as file:
    file.write("Line 4: I am the new content\n")

with open("notes.txt","r") as file:
    content = file.read()
    print("File Content Iteration 2")
    print(content)