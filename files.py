file = open("test.txt", "r+")
#print(file.readlines())
file.close()

with open("test.txt", "r") as file:
    #print(file.readlines())
    pass


##Writing Files
try:
    with open("newFile.txt", "a") as file:
        #file.write("This is a new file created!!") ##Write one line
        file.writelines(["Python is good for ML\n", "Java is good for FinTech\n", "Go is good for K8s"])
except FileNotFoundError as e:
    print("ERROR", e)