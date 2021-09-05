import requests
url = 'http://creativai.herokuapp.com/webhooks/rest/webhook'
msg=input()
myobj = {
"message": msg,
"sender" : 1,
}
x= requests.post(url,json=myobj)
print(x.text)
