import json
"""data ='{"var1":"Harry","var2":"Nikhil"}'
parsed=json.loads(data)
print(parsed)
print(parsed["var2"])


data2={"Channel name ":"Code",
       "cars":["Mercedes","Audi","BMW"],"isbad":False}
jcomp=json.dumps(data2)
print(jcomp)"""

data={
    "100":{"Name":"Nikhil","class":"SIXTJ","Rollno":15},
    "104":{"Name":"Varun","class":"Eight","Rollno":18},
    "10":{"Name":"Suresh","class":"Seventh","Rollno":16}
    }
print(json.dumps(data,sort_keys=True))
print(type(json.dumps(data)))
