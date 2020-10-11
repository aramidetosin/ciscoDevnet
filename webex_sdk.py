from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='NWVlY2NlMGItOWE0Zi00YWFlLTg1MTMtNzk5NDI5ZGY2MjliYmRlYTM2YWEtYWQy_PF84_consumer')

teams = api.teams.list()

# for team in teams:
#     print(team)
#     if getattr(team, 'name') != 'CBT Team':
#         create_team = api.teams.create('CBT Team')
#         teamId = getattr(create_team, 'id')
#     else:
#         teamId = team.id

# roles = api.roles.list()
# for role in roles:
#     print(role)



print(api.people.me())
print(api.people.list())
api.people.create(emails=['funtoakande@gmail.com'], displayName="Funto Akande", firstName='Funto', lastName='Akande', roles=[])