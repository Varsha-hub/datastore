
import json
data={}

def create(title,name,rollno):
    data[title]={
        'stdname':name,
        'stdrollno':rollno
        }
    with open('data.txt','w') as outfile:
        json.dump(data,outfile)
        
def read(title):
    with open('data.txt') as json_file:
        data=json.load(json_file)
        print(data[title])

def delete(title):
    del data[title]
    with open('data.txt','w') as outfile:
        json.dump(data,outfile)

print("choose an option")
print("create-1")
print("read-2")
print("delete-3")
print("exit-4")

while(True):
    n=int(input("enter choice: "))
    try:
        if(n==1):
            title=input("enter distinct key: ")
            try:
                if(title in data):
                    raise Exception("key already exists")
                else:
                    name=input("enter student name: ")
                    rollno=int(input("enter roll number: "))
                    create(title,name,rollno)
            except Exception:
                print("key already exists")
        elif(n==2):
            title=input("enter key to read: ")
            read(title)
    
        elif(n==3):
            title=input("enter key to delete: ")
            delete(title)
        elif(n==4):
            break
        else:
            raise Exception("invalid option")
    except Exception:
        print("invalid option")