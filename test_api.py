import requests
import json

# Predefined func
def get(url,params,headers): 
  
  r = requests.get(url, params=params, headers=headers)
  
  return r.text

def post(url,headers,data,params=''):
  
  r = requests.post(url,data=json.dumps(data),headers=headers)

  return r.text

def delete(url,headers):
  r = requests.delete(url,headers=headers)
  return r.text

def put(url,data,headers):
  r = requests.put(url,data = json.dumps(data), headers=headers)

  return r.text

# For managing apps
url = 'http://127.0.0.1:8090/v2/users/domain/manage_my_apps'

params = {'limit':5,'where':"name='projectsly' and is_active=1"}

headers = {'Content-Type': 'application/json',
  'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
  }


print(get(url,params,headers))

#Add projects

url = 'http://127.0.0.1:8090/v2/projects/projects'
params ={}
data = {
    "name": "test2907",
    "icon": "fe fe-activity",
    "color": "#1CA085",
    "is_public": "0"
  }

print(post(url,headers,data))

# Update projects
data ={
  "id": "2291",
  "name": "test2907",
  "icon": "fe fe-activity",
  "color": "#1CA085",
  "description": None,
  "member_id": [
    1,2,3
  ],
  "is_public": "0"
}
print(post('http://127.0.0.1:8090/v2/projects/projects',data=json.dumps(data),headers=headers))



# Delete Project
id='2218'
url = 'http://127.0.0.1:8090/v2/projects/projects/'+id
print(delete(url,headers))


# Get Added Projects
params ={'limit':5,'order_by':5}

print(get('http://127.0.0.1:8090/v2/projects/domain/add_project',params=params,headers=headers))



# Project Groups

data = {'name':'test2907','project_id':'2840'}
print(post('http://127.0.0.1:8090//v2/projects/groups',data=json.dumps(data),headers=headers))

# Delete Groups
id = '2643'
print(delete('http://127.0.0.1:8090/v2/projects/groups/'+id,headers=headers))



# Add Tasks
data = {
  "name": "<task name>",
  "description": None,
  "group_id": None,
  "due_date": None,
  "assignee_id": None,
  "project_id": None,
  "priority_id": "2",
  "status_id": "1",
  "actual_hours": "0",
  "estimated_hours": "0"
}

print(post('http://127.0.0.1:8090/v2/projects/tasks',data = json.dumps(data), headers = headers))



# Update Task
# Task Id
id = '27874'
data = {
  "name": "task_name",
  "description": None,
  "due_date": None,
  "assignee_id": "None",
  "priority_id": "2",
  "status_id": "1",
  "actual_hours": "0",
  "estimated_hours": "0"
}
url = 'http://127.0.0.1:8090/v2/projects/tasks/'+id
print(put(url,data,headers))

# Delete Task
id = '27874'

print(delete('http://127.0.0.1:8090/v2/projects/tasks/'+id, headers = headers))

