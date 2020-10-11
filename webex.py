import requests
import json


token = "NWVlY2NlMGItOWE0Zi00YWFlLTg1MTMtNzk5NDI5ZGY2MjliYmRlYTM2YWEtYWQy_PF84_consumer"


url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'}

# body = {
#     "name": "CBT Team"
# }
#
#
# post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
# print(post_response)

get_response = requests.get(url, headers=headers).json()
# print(json.dumps(get_response, indent=2, sort_keys=True))

teams = get_response['items']
for team in teams:
    if team['name'] =='CBT Team':
        teamId = team['id']
    # print(f"Name: {team['name']}")
    # print(f"      {team['id']}")


room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    'title': "CBT Room",
    'teamId': teamId
}

# room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()



get_rooms = requests.get(room_url, headers=headers).json()
# print(json.dumps(get_rooms, indent=2, sort_keys=True))


rooms = get_rooms['items']
for room in rooms:
    if room['title'] == 'CBT Room':
        roomId = room['id']
        # print(roomId)


msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
    "roomId": roomId,
    'text': 'ALERT: Interface on device XYZ is down'
}

msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()

read_msg = f'https://api.ciscospark.com/v1/messages?roomId={roomId}'
headers = {'Authorization': f'Bearer {token}'}
read_response = requests.get(read_msg,headers=headers, data=json.dumps(read_msg)).json()
# print(read_response)
msgs = read_response['items']
for msg in msgs:
    print(f"{msg['text']}")