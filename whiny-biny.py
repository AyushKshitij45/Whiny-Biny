# -*- coding: utf-8 -*-
"""
Project on binary file writing.

@authors: Ayush Kshitij
          Medhansh Jain
          Vatsal Kapoor
"""

import pickle


example_list=[]
example_dict=dict()
 
# Binary write list/dictionary(1st approach).
        
# Opening the file.
with open('file.bin','wb') as file:
           
    opt='y'
    # while loop continues till opt = y to add multiple elements.
    while opt=='y':
        
        try:
            dicty= input('What do you want to write? ')  # Input to add elements.  
            
            example_list.append(dicty)  # Adding to a list.
            # Converts example_list dictionary with keys(0,1,2...).
            example_dict= dict(enumerate(example_list))  
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
            
            # Check for valid responses to opt.
            acceptedResponses=['y','n'] 
            while opt not in acceptedResponses: 
                print("Please enter {}/{}".format('y','n'))
                opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))
        
        # Handling all general exceptions.
        except Exception as e:
            print(e)
        
    pickle.dump(example_dict,file) # Adding example_dict to file
                  
    file.close()
    
    
# Opening the file
with open('file.bin','rb') as file:
    
    try:         
        while True:
            # Loading the file.
            example_dict=pickle.load(file)
            print(example_dict)
                
    # Handling End of file error after reading is complete.
    except EOFError:
        file.close()
    
    # Handling all other exceptions.    
    except Exception as e:
        print(e)
    

# Binary write dictionary(2nd approach).
    
# Opening the file.
with open('file.bin','wb') as file:
       
    opt='y'
    while opt=='y':
        
        try:
            Name= input('Name of student: ')  # 1st element of dictionary.
            rollNo= input("Student's Roll No.: ")  # 2nd element of dictionary.

            # Adding to dictionary.
            example_dict['Name:']=Name            
            example_dict['Roll No.:']=rollNo
        
            opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))        
            
            pickle.dump(example_dict,file)
            
            acceptedResponses=['y','n']
            while opt not in acceptedResponses: 
                print("Please enter {}/{}".format('y','n'))
                opt=str(input('''Do you want to add more items?, ({} for {}, {} for {}): '''.format('y','yes','n','no')))
        
        except Exception as e:
            print(e)
                         
    file.close()
    
           
# Binary read/searching.

# Opening the file
with open('file.bin','rb') as file:
    
    i=0  
    try:
        # Asking viewer's intention and a name to search.
        searchedName=input('Enter name of the student (Press {} to view the full file) : '.format("the 'Enter' key"))
                
        while True:
            # Loading the file.
            example_dict=pickle.load(file)
            
            # Check if name exist or view entire file.
            if searchedName == '':
                i+=1  # Increment i 
                # Condition to print "Records:" only once.
                if i==1:
                    print('Records: ' )
                print(example_dict)  # View details of searched individual.
            
            elif example_dict['Name:'] == searchedName:
                i+=1 # Increment i if name is found.
                print('Records: ' )
                print(example_dict)
    
    # Handling End of file error after reading is complete.
    except EOFError:
        file.close()
    
    # Handling all other exceptions.    
    except Exception as e:
        print(e)
    
    # If the requested name is not present in the file.
    if i==0:
        print('No one by that name.')
        

'''---------------------------------------------------------------------------------------------------------'''


'''        
# ONE MORE EXAMPLE.
THE_IMAGE=open('THE IMAGE WITH TEXT.PNG','rb')

with open('AN IMAGE.PNG','wb') as thing:
    
    for i in THE_IMAGE:
        thing.write(i)

    thing.close()
'''        