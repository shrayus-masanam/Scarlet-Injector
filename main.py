import requests
import json
from datetime import datetime

ipa_url = input("Enter IPA URL: ")
tweaks = []
while True:
    tweak = input("Enter tweak URL (leave blank to stop): ")
    if tweak == "":
        break
    tweaks.append(tweak.strip())

repo_json = {
	"META": {
		"repoName": f"Custom App {datetime.today().strftime('%Y-%m-%d')}",
		"repoIcon": "https://usescarlet.com/favicon.png"
	},
	"Other": [{
		"name": f"Custom App {datetime.today().strftime('%Y-%m-%d')}",
        "version": "1.0",
        "icon":	"https://usescarlet.com/icon.png",
		"down": ipa_url.strip(),
        "description": f"This is your IPA with the tweaks you specified injected into it.",
        "bundleID": "user.you.app",
		"category": "Tweaked Apps",
		"debs": tweaks,
        "changelog": f"Uploaded on {datetime.today().strftime('%Y-%m-%d')}."
	}]
}

print("Creating repo...")

response = requests.post("https://paste.bingner.com/paste/new", data={
    "text": json.dumps(repo_json),
    "lang": "json",
    "expire": "14d",
    "password": "",
    "title": "A Custom Repo",
})
print("Done. Add this repo to Scarlet and install the app inside. Repo will expire in 14 days.")
print("https://paste.bingner.com/paste/" + response.text.split("<title>")[1].split(" -")[0] + "/raw")