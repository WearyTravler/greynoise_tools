import os
from greynoise import GreyNoise


#api key via env variable
greynoise_key = os.getenv(str("REDACTED"))

api_client = GreyNoise(api_key=str(greynoise_key), timeout=10)


print(api_client.quick('8.8.8.8'))