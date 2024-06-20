users=['Ram','Hari']
users[0]='Sofia'
print(users[0])
# Mutable Data Type
users.append('Deepak')
# append canonly one elemnet in the variable
# Used to call the functions
# dir command is usedfr fin or search the different property of any defined variables that shows the different methods.
print(users)
print(dir(users))
users.insert(0,'Hari')
print(users)
print(users.pop())
# Pop can used for single data can be removed with indexing value
print(users.remove('Sofia'))
# Remove the data based on the defined data
us=['Sita','Rita']
users.extend(us)
print(users)
namelist=['S','P','D']
namelist.index
namelist.sort()
print(namelist)
namelist.reverse()
print(namelist)
namelist.count
print(namelist)
# sorting takes same types of data types viz; number, variable etc.
namelist.sort(reverse=True)
# data set sorted from reverseorder
# if the data set is defined as capital and small letter than when we used sorting, capital letter srted first regardless of the rule as it is defined based on the ASCII table.
data=[]
name=input("enter your name")
email=input('enter your email address')
data.append(name)
data.append(email)
print(data)
