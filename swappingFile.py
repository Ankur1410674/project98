def swappingFile():    
    filename = input("enter the file name")

    with open(sample1, "r") as a:
        data_a = a.read
    with open(sample1, "w") as a:
        a.write(data_b)   

swappingFile()        