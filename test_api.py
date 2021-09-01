import requests
import json

params={'limit':5,'where':"name='projectsly' and is_active=1"}

# For managing apps
r = requests.get('http://127.0.0.1:8090/v2/users/domain/manage_my_apps',params=params,headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
})
#r = requests.get('https://api.github.com/events')

print(r.text)

#Add projects
params ={}
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
data = {
  "name": "test2907",
  "icon": "fe fe-activity",
  "color": "#1CA085",
  
  "is_public": "0"
}
r= requests.post('http://127.0.0.1:8090/v2/projects/projects',data=json.dumps(data),headers=headers)
print(r.text)

# Update projects
params = {}
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
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
r= requests.post('http://127.0.0.1:8090/v2/projects/projects',data=json.dumps(data),headers=headers)
print(r.text)


# Delete Project
id='2218'
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
r = requests.delete('http://127.0.0.1:8090/v2/projects/projects/'+id,headers=headers)
print(r.text)


# Get Added Projects
params ={'limit':5,'order_by':5}
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
r = requests.get('http://127.0.0.1:8090/v2/projects/domain/add_project',params=params,headers=headers)
print(r.text)


# Project Groups
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
data = {'name':'test2907','project_id':'2840'}
r = requests.post('http://127.0.0.1:8090//v2/projects/groups',data=json.dumps(data),headers=headers)
print(r.text)

# Delete Groups
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}
id = '2643'
r = requests.delete('http://127.0.0.1:8090/v2/projects/groups/'+id,headers=headers)
print(r.text)


# Add Tasks
headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}

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

r = requests.post('http://127.0.0.1:8090/v2/projects/tasks',data = json.dumps(data), headers = headers)

print(r.text)


# Update Task
# Task Id
id = '27874'

headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}

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

r = requests.put('http://127.0.0.1:8090/v2/projects/tasks/'+id,data = json.dumps(data), headers=headers)

print(r.text)


# Delete Task
id = '27874'

headers={'Content-Type': 'application/json',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJha2VzaC55b2dndUA1MDBhcHBzLmNvbSIsInRlbmFudF9pZCI6Mjg0MCwidXNlcl9pZCI6NzgyMCwic3Vic2NyaWJlZCI6Im5vIiwiZXhwIjoiMTYzMzA2MjA1NCIsImVudiI6ImRldiJ9.o0qQJ864SiimPgYPDACLiOVrqzJ4uhQMmLWfWNiZ96o'
}

r = requests.delete('http://127.0.0.1:8090/v2/projects/tasks/'+id, headers = headers)

print(r.text)