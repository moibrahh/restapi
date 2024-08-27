import requests

BASE = "http://127.0.0.1:5000/"

'''data = [{"likes": 433, "name": "Hana" , "views": 789767},
        {"likes": 111, "name": "Pat" , "views": 786767},
        {"likes": 31231, "name": "Jon" , "views": 34254324}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i) ,data[i])
    print(response.json())'''
    
#input()
response = requests.patch(BASE + "video/2", {"views" : 99, "likes": 2000000})
print(response.json())
