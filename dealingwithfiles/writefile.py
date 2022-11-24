"""
open file with write mode if file not exists 000> python interpreter
will try to create it
open the file for writing starting from the beginning of the file
"""

try:
    fileobj=open("mycv.txt", "w")
except Exception as e:
    print(e)
    exit()
else:
    # print(fileobj)
    res=fileobj.write("11111")
    print(res)
    # print("Noha",file=fileobj)

    # "write content at certain position"
    # fileobj.seek(10)
    # fileobj.write("Hello itiains")

    "writelines "
    fileobj.writelines(["Ahmed\n", "Ali\n", "Omar\n", "Layla\n"])
    fileobj.close()