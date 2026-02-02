import requests
import time

DISCORD_AUTH_TOKEN = "MTIxNzY3MTE3MTA4MDcxNjM1OQ.GdjCo3.tqza2u7Leyn4umJ7JTNkfLhQXigOD_nAdOjcm8"

CHANNEL_ID = input("Id Of Channel You Wish To Send Messages Too: ")
MESSAGE = input("Enter The Message You Wish to Send: ")
TIMES = input("How Many Times You Wish To Send The Message: ")

payload = {
    'content': MESSAGE
}

header = {
    'Authorization': DISCORD_AUTH_TOKEN
}

url = 'https://discord.com/api/v9/channels/{}/messages'.format(CHANNEL_ID)

i = 0
for i in range(int(TIMES)):
    req = requests.post(url=url, headers=header, data=payload)
    if req.status_code == 200:
        print(f"Succeeded {i} Times... ")
        time.sleep(0.1)
    elif req.status_code == 429:
        print("Sending to fast cooling down... ")
        time.sleep(1)

print("Finished With No Errors... ")