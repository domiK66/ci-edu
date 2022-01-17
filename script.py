import json

f = open('swenga-springboot-employee-manager/swenga-springboot-employee-manager_result.csv','r')

arr=[]
headers = []

for header in f.readline().split(','):
  headers.append(header)

for line in f.readlines():
  lineItems = {}
  for i,item in enumerate(line.split(',')):  
    lineItems[headers[i]] = item
  arr.append(lineItems)

f.close()

jsonText = json.dumps(arr)

print(jsonText)

#curl --location --request PUT 'https://gitlab.fh-joanneum.at/api/v4/projects/25/repository/files/exercise1_result%2Ecsv' --header 'PRIVATE-TOKEN: b5sACgy_eTYJyiSQcexV' --header 'Content-Type: application/json' --data-raw '{"branch": "main","author_email": "me@me","author_name": "raffling nico","content": "'"$text"'","commit_message": "test benotung"}'