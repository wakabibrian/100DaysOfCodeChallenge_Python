# -------------HTTP Post Requests-----------------#
# GET request (from before) is a way of getting data from some body else - requests.get()
# POST request we give the external system some piece of data, we are not interest in the
# response we get back other than if it was successful or not - requests.post()
# PUT you simply update a piece of data in the external service - resquests.put()
# DELETE is where you want to delete a piece of data in the external service - requests.delete()

# -------------Day 37 project: Habbit tracker-----------------#
import requests

USERNAME = "wakabi"
TOKEN = "hehstdkkahasredadj"
GRAPH_ID = "graph1"

pixela_end_point = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hr",
    "type": "int",
    "color": "ajisai"

}

# HTTPHeader helps the key/token not visible to others in logs
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_end_point, json=graph_config, headers=headers)
# print(response.text)

pixel_end_point = f"{graph_end_point}/{GRAPH_ID}"

pixel_params = {
    "date": "20230512",
    "quantity": "4",
}

response = requests.post(
    url=pixel_end_point, json=pixel_params, headers=headers)
print(response.text)
