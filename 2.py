'''
 minimizing the string
condition all the characters are lowercase if not convert it
and the z doesnt come in the string

the problem states that
if two successive elements come one after other replace them with the next 
succesive element i.e if ab comes replace it with the c 
do this in a loop until the string cannot be minimized further

'''
userInput=input('enter the string')
userInputLower=userInput.lower()
print(userInputLower)

charlist=[]
charlist1=[]
charlist2=[]
charlist3=[]
characterstring=''

for elm in userInputLower:
    charlist.append(ord(elm))
print(charlist)


while(charlist!=charlist2):
    charlist2=charlist
    charlist1=[]
    i=0
    for i in range(0,len(charlist),2):
        if len(charlist)%2==0:
            if charlist[i]+1==charlist[i+1]:
                charlist1.append(charlist[i]+2)

            else:
                charlist1.append(charlist[i])
                charlist1.append(charlist[i+1])
        
        else:
            if i==len(charlist)-1:
                charlist1.append(charlist[i])

            else:
                if charlist[i]+1==charlist[i+1]:
                    charlist1.append(charlist[i]+2)

                else:
                    charlist1.append(charlist[i])
                    charlist1.append(charlist[i+1])
    charlist=charlist1
    

for i in range(len(charlist)):
    charlist3.append(chr(charlist[i]))

for i in range(len(charlist3)):
    characterstring=characterstring+str(charlist3[i])


print(characterstring)
    
'''
print(charlist2)

print(charlist)           
                
print(charlist1)

'''


