import requests

response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')

loads = response.json()

#get login fron the dict
for load in loads:
    if load["user"]["login"] == "HirazawaUi":
        for i in load["requested_reviewers"]:
            print(i["login"])