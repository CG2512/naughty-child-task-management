# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:36:41 2022

@author: Admin
"""

import math
import sys
#List for works
# work_OG=[]
work_OG=[["a","b","c"],["d","e","f"]]
#maximum number of child
maxinum_childs=6

def list_flatten(data_list):
    #If list empty, nothing to do
    if data_list == []:
        return data_list
    #if first element is a list, flatten it and the rest of the list
    if isinstance(data_list[0], list):
        return list_flatten(data_list[0]) + list_flatten(data_list[1:])
    #After it's done,return the whole list with 2 half of it
    #
    return data_list[:1] + list_flatten(data_list[1:])

def allocate_tasks(task_list,max_child):
    try:
        #Check if task list is a list,exit if not
        if type(task_list)!=list:
            print("Invalid input")
            sys.exit()
        #Flatten lists to deal with nested list
        task_list=list_flatten(task_list)
        #if list has nothing, stop program
        if len(task_list)==0:
            print("No tasks")
            sys.exit()
        #Actual list for keeping check for which kids do which tasks
        child_works=[[] for child_number in range(maxinum_childs)]
        # print(child_works)
        # #Temp list for keeping track of what child(lists already used)
        recruited_child=[]
        # #Number of children available, change through time(minus)
        #Start with max child minus 1 cause child 1 can not be used
        available_child=max_child-1
        #Variable for which list to split
        split_list_1=1
        split_list_2=2
        current_list_index=0
        
        child_works[0]=task_list
        while available_child !=0:
           
            # print(task_list)
            # print("placeholder")
            # #First child uses the Original work list so check the number of items in that list
            # #Put that list into first child list
            
            
            
        #Current list about to be splitted
            list_to_split=child_works[current_list_index]
        #Check if the current list only have 1 or not
        #If it does,move index to next kid then reset loop
            if len(list_to_split)==1:
                current_list_index+=1
                continue
            if available_child>1:
        #First list to split to
                child_works[split_list_1]=list_to_split[:math.ceil(len(list_to_split)/2)]
                # print(child_works[split_list_1])
        #Second list to split to
                child_works[split_list_2]=list_to_split[math.ceil(len(list_to_split)/2):]
                # print(child_works[split_list_2])
        #Empty the original list because that kid have split all their tasks
                list_to_split.clear()
        #Minus the recruited kids
                available_child-=2
        #Put the recruited kids to the used list
                
                recruited_child.append(split_list_1)
                recruited_child.append(split_list_2)
             
            elif available_child==1:
        #First list to split to
                child_works[split_list_1]=list_to_split[:math.ceil(len(list_to_split)/2)]
        #Second list to split which is also the original list
        #because works can't be split if there's only one recruit:
                child_works[current_list_index]=list_to_split[math.ceil(len(list_to_split)/2):]
        #Minus child available for recruit
        #At this point there's no one left so might as well stop
                available_child-=1
        #Add recruited child to used kids list
                recruited_child.append(split_list_1)
                
        #Move the available child number for recruit to the next one
            while True:
        #if next childs are in the already recruited lists,move the child index until childs are recruitable
        #If the next two childs(the lists's index number) is already used 
        #Add 1 to both num until the next 2 list index numbers are unused 
                if split_list_1 in recruited_child or split_list_2 in recruited_child:
                    split_list_1+=1
                    split_list_2+=1
                    continue
                else:
                    break
            current_list_index+=1
            # print("l1: "+str(split_list_1))
            # print("L2: "+str(split_list_2))
            # print(str(available_child))
            # print(child_works)
            #Add 1 to the recruited child list because we start from child 2
        print_recruited_chill=[i+1 for i in recruited_child]
        #Tuple contains both recruited child list and task lists
        recruited_child_and_tasks=(child_works,print_recruited_chill)   
        print(recruited_child_and_tasks)                  
        return(recruited_child_and_tasks)
    #in case of index or TypeError(Happen with invalid child input)
    #Print messege then quit
    except TypeError:
        print("Invalid input")
        sys.exit
    except IndexError:
        print("Invalid input")
        sys.exit()
        
def print_all(data_tuple):
    #First index in tuple is the allocated task lists
    #Load data to a var
    child_tasks=data_tuple[0]
    #Counter for which child being printed
    child_num_allocate=1
    print("Allocation")
    for child_tasks in child_tasks:
        
        print("Child {}:{}".format(str(child_num_allocate),str(child_tasks)))
        child_num_allocate+=1
    #Second index is child recruited lists
    #load data to a var
    recruited_child=data_tuple[1]

    print (type(recruited_child))
    #Counter for which child being printed
    try:
        child_num_recruited=1
        child_num_1=0
        child_num_2=1
        last=len(recruited_child)-1
        print("Recruitment")
        for child in recruited_child:
            if child_num_1< last:
                print("{} : {} {}".format(str(child_num_recruited),str(recruited_child[child_num_1]),str(recruited_child[child_num_2])))
                child_num_1+=2 
                child_num_2+=2
                child_num_recruited+=1
            elif child_num_1==last:
                print("{} : {} ".format(str(child_num_recruited),str(recruited_child[child_num_1])))
                child_num_recruited+=1
                child_num_1+=1
            else:
                print("{} :".format(str(child_num_recruited)))
                child_num_recruited+=1
                
    except:
        print()
       
    
    
    
    
    
    
    
    
    
    
    
    
    



           
            
            
            
result=allocate_tasks(work_OG, maxinum_childs)
print_all(result)