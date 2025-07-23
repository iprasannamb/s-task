import os

tasks=[]

def save():
    with open("task.txt","a",encoding="utf-8") as f:
        for i in range(len(tasks)):
            f.write(f"{tasks[i]["task"]}-{tasks[i]["status"]}\n")         
            
    
def display():
    print("TASK(S)".center(50,"-")) 
    print()
    try:   
        with open("task.txt","r",encoding="utf-8") as f:
            c=f.readlines()
            for i,it in enumerate(c):
                na=it.replace('\n','').rsplit('-')
                st='Done' if na[1]=='True' else "Not Done"
                print(f"{i+1}.{na[0]} - {st}")
    except:
        print("No Task")
        

    

def intake():
    
    print("Add New Task".center(50,"-")) 
    print()   
    
    
    while(True):        
        a=input("Enter the task :")    
        if(a.strip()=='exit' or a.strip()==''):
            break
        elif(a.strip()!=''):       
            tasks.append({"task":a,"status":False})
    save()        

            
def status():
    print("UPDATE".center(50,"-")) 
    print()   
       
    display()
    print('\n')
    id=int(input('Select the task : '))
    with open("task.txt","r",encoding="utf-8") as f:
        c=f.readlines()
        v=c[id-1].replace("\n",'').rsplit('-')
        v[1]='False' if v[1]=='True' else 'True'
        c[id-1]=f"{v[0]}-{v[1]}\n"        
    with open("task.txt","w",encoding="utf-8") as f:  
        for i in range(len(c)):            
            f.write(f"{c[i]}")
    print("\nDone")    
        

            
def edit():
    print("EDIT TASK(S)".center(50,"-"))
    print()        
    
    display()
    print('\n')
    id=int(input('Select the task : '))
    with open("task.txt","r",encoding="utf-8") as f:
        c=f.readlines()
        if((id-1)<len(c)):
            nt=input("Enter New Task : ")
            v=c[id-1].replace("\n",'').rsplit('-')
            v[0]=f'{nt}'
            c[id-1]=f"{v[0]}-{v[1]}\n"
        else:
            print("Invalid Input")
            exit()
    with open("task.txt","w",encoding="utf-8") as f:  
        for i in range(len(c)):            
            f.write(f"{c[i]}")
    print("\nDone") 
    
def rmv():
    print("REMOVE TASK".center(50,"-"))
    print()        
    
    display()
    print('\n')
    id=int(input('Select the task : '))
    with open("task.txt","r",encoding="utf-8") as f:
        c=f.readlines()
        if((id-1)<len(c)):
            c.remove(c[id-1])
        else:
            print("Invalid Input")
            exit()
    with open("task.txt","w",encoding="utf-8") as f:  
        for i in range(len(c)):            
            f.write(f"{c[i]}")
    print("\nDone")    
            

def main():
    while(True):
        print()
        print("TASK MANAGER".center(50,"-"))
        print()
        print('1.Add Task\n2.Display Task(s)\n3.Edit Task\n4.Update Status\n5.Remove')     
        print()
        ask=input("Select your choice :")
        print()
        match(ask):
            case "1":            
                intake()            
            case "2":
                display()
            case "3":
                edit()
            case "4":
                status()
            case "5":
                rmv()
            case _:
                break
main()
