import requests as rq
data = rq.get('http://universities.hipolabs.com/search?country=latvia')
universities = data.json()
sorted(universities["name"])
for value in universities:
    print(value["name"])