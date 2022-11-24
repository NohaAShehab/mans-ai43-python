"""
open file with append mode if file not exists 000> python interpreter
will try to create it
open the file for appending starting from the end of the file
"""

try:
    fileobj=open("mycv.txt", "a")
except Exception as e:
    print(e)
    exit()
else:
    fileobj.write("Added string\n")
    # fileobj.seek(10000)  # useless line
    fileobj.write("##########################")
    fileobj.writelines(["test", "abc", "done"])
    fileobj.close()