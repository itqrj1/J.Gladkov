import os

print(os.getcwd())

#должен лежать в этойже папке
file = os.open("names","r+",encoding ='utf-8' )
#r+  режимы

#
#если лежит не в тойже деректории
file = os.open("c://dir/names/","r+",encoding ='utf-8' )
#создаем
file = os.open("c://dir/names/","x",encoding ='utf-8' )
f.seek(15)
print(file.readlines(3))
print("Names of the file:",f.name)
print("closed of not",f.closed)
print("Opened mode", f.mode)
print("Place", f.fileno())
f.writelines("asdasda\n\rsdfsdfsdfw\n\rsdfsdfs")
f.writelines("asdasda\n")
f.writelines("asdasda\n")
f.writelines("asdasda\n")
file.close ()
