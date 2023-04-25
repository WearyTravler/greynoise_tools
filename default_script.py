import requests 

#check status of greynoise 

api_key = "REDACTED"

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

	print(response.text)

greynoise_status()
