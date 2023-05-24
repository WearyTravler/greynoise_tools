import requests 
import os
import greynoise
from greynoise import GreyNoise
#check status of greynoise 

api_key = os.getenv("GREYNOISE_API_KEY")

api_client = GreyNoise(api_key=os.getenv("GREYNOISE_API_KEY", timeout=10))

def greynoise_status():
	global api_key

	url = "https://api.greynoise.io/ping"

	headers = {
    	"accept": "*/*",
    	"key": str(api_key)
	}

	response = requests.get(url, headers=headers)

	print(response.text)



#basic search
def search():
	global api_key

	ip_choice = input("What ip would you like to search: ")

	url = "https://api.greynoise.io/v3/community/" + str(ip_choice)

	headers = {
    	"accept": "application/json",
    	"key": str(api_key)
	}

	response = requests.get(url, headers=headers)
	#print(response.text)
	#print(response.json())
	# for x in response.json():
	# 	print(x)
	response = response.json()
	print("Ip: " + response.get('ip'))
	#print("Response: " + response.get('response'))
	#print("Noise: " + response.get('noise')) bool problem or str problem
	print("Classification: " + response.get('classification'))
	#print("Riot          : " + response.get('riot')) bool problem or str problem
    


	
		
# {
#     "ip": "1.1.1.1", < green
#     "noise": false, < red
#     "riot": true, < blue
#     "classification": "benign", < purple
#     "name": "Cloudflare Public DNS", < orange
#     "link": "https://viz.greynoise.io/riot/1.1.1.1", < blue
#     "last_seen": "2023-04-25", < grey
#     "message": "Success" < green
# }

# b'{\n    "ip": "1.1.1.1",\n    "noise": false,\n    "riot": true,\n    "classification": "benign",\n    "name": "Cloudflare Public DNS"'
# b',\n    "link": "https://viz.greynoise.io/riot/1.1.1.1",\n    "last_seen": "2023-04-25",\n    "message": "Success"\n}'

# ip
# noise
# riot
# classification
# name
# link
# last_seen
# message


while True:
	print("1: Check Status of GreyNoise and API key")
	print("2: Run a basic IP query")
	choice = input("GreyNoise commandline tool: ")
	if choice == "1":
		greynoise_status()
	if choice == "2":
		search()
	else:
		exit()
