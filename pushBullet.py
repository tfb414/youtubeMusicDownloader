from pushbullet.pushbullet import PushBullet

apiKey = "o.4Om3sn1YmS2wAXKDQG7wakv3Z7yDE5B4"
p = PushBullet(apiKey)

devices = p.getDevices()

# print(devices)

# p.pushNote(devices[3]["iden"], 'Hello mcfly', 'Test body')
p.pushLink(devices[3]["iden"], "Google", "http://www.google.com")
