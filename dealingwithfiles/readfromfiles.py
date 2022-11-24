try:
    fileobj = open("students.txt")  # default is read mode
except Exception as e:
    print(e)
    exit()
else:
    # "1- read all content in the file "
    # print(fileobj)  # IO, textIOWrapperobject
    # data =fileobj.read()
    # print(data)
    # "1- read first part from the file "
    # print(fileobj)  # IO, textIOWrapperobject
    # data = fileobj.read(10)
    # print(data)
    "2- read first part from the file "
    # print(fileobj)  # IO, textIOWrapperobject
    # fileobj.seek(10)
    # data = fileobj.read(10)
    # print(data)
    # print("-------------------")
    # fileobj.seek(1)
    # print(fileobj.read())
    # #
    # "3- read file content line by line"
    # data = fileobj.readlines()
    # print(data)
    # fileobj.close()
    # for l in fileobj:  # scan file line by line "\n"
    #     print(l)

    for i , l in enumerate(fileobj):
        if i in range(5,11):
            print(i, l )