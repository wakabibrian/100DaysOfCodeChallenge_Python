# -------------HTTP Post Requests-----------------#
# GET request (from before) is a way of getting data from some body else - requests.get()
# POST request we give the external system some piece of data, we are not interest in the
# response we get back other than if it was successful or not - requests.post()
# PUT you simply update a piece of data in the external service - resquests.put()
# DELETE is where you want to delete a piece of data in the external service - requests.delete()

# -------------Day 37 project: Habbit tracker-----------------#
import requests

pixela_end_point = "https://pixe.la/v1/users"
user_params = {
    "token": "hehstdkkahasredadj",
    "username": "wakabi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)
