#the programe is find the value of a-z and then convert it into binary and then 
#convert it into 8 character bit length
#and then concatenate it all and then convert into 
#6 bit length and the convert it back into the characters


#algorithm
#first check weather the character set qualify for the condition character set
#if not then return the -1 in else part

#in if part of the function 

#first way try is divide the string in to an list
#in list the iterate over the list and then convert it into an binary list or string of 8 digits
#then convert the list or string to string and then concatanate all of it
#and then divide based on 6th element
#and then convert it into the number
#and then convert it into the character set
import re



def convert(string_agrs):
    obj=re.compile(r'[a-zA-Z+!0-9 ]+')
    mo=obj.findall(string_agrs)
    lvalue_string=[]
    bin_list=[]
    bin_string=''
    bin_divlist=[]
    final_list=[]
    string_copy=''
    print(string_agrs)
    
    
    if len(mo)==1 and str(mo[0])==string_agrs:
        lvalue=list(string_agrs)
        #print(lvalue[0:])
        i=0
        for elm in lvalue:
            j=lvalue[i]
            i=i+1
            lvalue_string.append(j)

        i=0
        for elm in lvalue_string:
            k=ord(lvalue_string[i])
            l=bin(k)                    #binary value
            m=list(l)                   #list of binary value
            n=l[2:]                     #only the meaning ful part of the binary number
            
            if(len(n)==7):
                o='0'+str(n)                #the string conversion with the 0 addded at the first
            elif(len(n)==6):
                o='00'+str(n)


            bin_list.append(o)

            

          
            i=i+1

        #print(bin_list[0:])
        i=0
        for elm in bin_list:
            k=bin_list[i]
            i=i+1

            bin_string=bin_string+str(k)

        #print(bin_string)    

        bin_divlist=list(bin_string) 
        #print(bin_divlist)

        length=len(bin_divlist)
        #print(length)
        mod=length%6
        #print(mod)
        length_mod=length
        req=6-mod

        if req>0:
            i=1
            for i in range(req):
                bin_divlist.append(0)
        
        #print(bin_divlist)

        
        j=0
        i=0
        
        for j in range(0,len(bin_divlist),6):
            #print(len(bin_divlist))
            final_list.append(str(bin_divlist[j])+str(bin_divlist[j+1])+str(bin_divlist[j+2])+str(bin_divlist[j+3])+str(bin_divlist[j+4])+str(bin_divlist[j+5]))
            
            i=i+1
            #print(j)
        

        #print(final_list)
        final_list1=[]
        i=0
        for i in range(len(final_list)):
            #final_list1[i]=int(str(final_list[i]),2)
            k=int(final_list[i],2)
            final_list1.append(k)
            #print(chr(k))

            
           

       # print(final_list1)  

        i=0
        final_listchar=''
        for i in range(len(final_list1)):
            final_list1[i]=chr(final_list1[i])
            final_listchar=final_listchar+str(final_list1[i])
        
        return(final_listchar)
        
      #  print("final list")
       # print(final_list1)

       # print("final list char")
       # print(final_listchar)

        
              
    else:
        return -1

print(convert('11'))
    