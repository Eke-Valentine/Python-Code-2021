
from urllib import request
from os import name, path
import json
import requests
from requests.models import Response 
import pyttsx3
#using requests library to get an API
#
jokeUrls="http://v2.jokeapi.dev/joke/Any?amount=4"
response= requests.get(jokeUrls) 
print(response.status_code)
datas=response.text
print(datas)

engine=pyttsx3.init()
engine.speak("hello")


file1=open("./data5.doc","r+")
for i in file1:
    print(i)

r=request.urlopen("http://www.google.com")
#print(f"this is google's website {r.getcode()}")


#r2=request.urlopen("http://www.amazon.com")
#print(f"this is amazon's website /n {r2.read()}")

#Api calls using urllib
jokeUrl=" http://v2.jokeapi.dev/joke/Any?amount=10"
jokeRequest= request.urlopen(jokeUrl)
data=jokeRequest.read()
jsonData=json.loads(data)
#print(jsonData)


class Jokes:

    def __init__(self,category,joke) -> None:
        self.category=category
        self.joke=joke

    def __str__(self) -> str:
        return f"the joke is {self.joke} and the type is {self.category} "


names= {"boysi": "tola" , "Kill": [{"boy": "tola" , "Kill":"low", "girl": "sade"}]}
print(names["Kill"][0])
nameslist=list(names)
print(nameslist[0])

if nameslist[0]=="boys":
    print("exist")
else:
    print("doewsn exist")
n=-1
category= jsonData["jokes"]
print(f" length of {len(category)} ")

for i in category: 
    n+=1
    jokese=category[n]
    list_jokes=list(jokese)
    print(f"this is joke number {n+1} ")
   

    if list_jokes[2]=="setup" :
        setup=jokese['setup']
        delivery=jokese['delivery']
        print(f"val { setup} ")
        print(f" it is {delivery}  \n")
       
        
    else:
        delivery=jokese['joke']
        print(f"full joke: {delivery} \n")

 

