string="abcdefghi"
alist=list(string)
print(string)
print(alist)

alist.reverse() #reverse order of alist
newstring="".join(alist)
print(newstring)
newstring2="-".join(alist) #join with linking character
print(newstring2)
