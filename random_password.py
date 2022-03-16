# take the input of the password and creates a generated password and a key for the password on the end
#random key generator and uses a list of generated numbers and stores the password


def encrypt_password(password,length): #made a bunch of lists iterate 2 by default unless passed
    model=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    iterate=0
    for i in password.lower(): #loop thru password find letters and check against model find distance
        #from each letter and then add or subtract that value to the iterate variable
        
        for k in range(len(model)):
            if model[k]==i and iterate<28: #if number too high 
                iterate+=k
            elif model[k]==i and iterate > 26:
                iterate-=k
    password_length=len(password)
    
    #setting value for jumping thru first list
    stored_pass1=[]
    for character in range(1,110000000,password_length):
        
        numb1=110000000%character # list of semi random characters
        stored_pass1.append(numb1)# appending numbers to list 1
    stored_list2=[]
    stored_pass_len=len(stored_pass1)
    
    for character in range(1,stored_pass_len,iterate):
        numb1=stored_pass_len%character # returning remainder of last list length over the number in the list
        stored_list2.append(numb1)# making new list
    stored_list3=[]
    for index in range(1,len(stored_list2),iterate):    
        stored_list3.append(stored_list2[index])
    final_pass=''#final pass intial value created
    
    for index in range(length): #minus 5 for room for the passlength,iterating number, and the length of encyrpted password on
        #the end
        i=stored_list3[index]
        final_pass+=str(i)

    
    
    return '$'+ final_pass
if __name__=='__main__': #if ran as main which it is
    
    while True:
        try:
            password=input("input your password(8-16 characters): ")
            if len(password)>7:
               break
        except:
            pass
    while True:
        try: 
            length=int(input("length of new encrypted password (100-320): "))
            break
             #try convert to int
        except:
            print('not a number retry')
            pass
    
    print('Your password inputted was',password,'and your encrypted password is:',encrypt_password(password,length))
    
