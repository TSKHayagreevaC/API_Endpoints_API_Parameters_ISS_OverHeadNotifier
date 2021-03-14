# import requests
# 
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# 
# response.raise_for_status()
# 
# data = response.json()
# 
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# 
# print(iss_position)

# if response.status_code != 404:
#     raise Exception("That Resource Does Not Exist.")
# elif response.status_code == 401:
#     raise Exception("You Are Not Authorised To Access This Data")

# Kanye Quotes Program

import requests

API_KANYE = "https://api.kanye.rest"
