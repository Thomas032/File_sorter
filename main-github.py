import os
import time


def get_type():
    files = os.listdir()
    li=[] 
    na = [] 
    for fi in files:
        splitted = fi.split(".") 
        compar = len(splitted) % 2 
        if compar == 0:
            typ = splitted[1] 
            name = typ+"_files" 
            li.append(name) 
            na.append(fi) 
        else: 
            if os.path.isfile(fi): 
                typ = splitted[-1] 
                name = typ+"_files" 
                li.append(name) 
                na.append(fi) 
                
    return li, name, fi  
    
def make_folders(li):
    for name in li: 
        if not os.path.exists(name): 
            os.makedirs(name) 
        
            print("Done!") 
        
    #print(r'C:\Users\Tomáš\Desktop\unknown images- desk\%s\%s' %(name, fi)) #Only for Debugging! (not important)

def move_files():
    files = os.listdir()
    li=[] 
    na = [] 
    for fi in files:
        
        splitted = fi.split(".") 
        compar = len(splitted) % 2 
        if compar == 0:
            typ = splitted[1] 
            name = typ+"_files"
            
            li.append(name) 
            na.append(fi) 

        else: 
            if os.path.isfile(fi): 
                typ = splitted[-1] 
                name = typ+"_files" 
                li.append(name) 
                na.append(fi)
                
        
        if "." in fi: 
            src = "%s\%s" %(name,fi)
            
            if not os.path.exists(src):
                if typ != "py":
                    os.rename(fi,src) 
                else :
                    print(f"File {fi} can not be moved because it is dependent on the location!")
            else:
                print(f"Ditrectory: {src} already exists!")


        
  
 
        

    


types, jmeno, fi =get_type() 

make_folders(types) 
move_files()