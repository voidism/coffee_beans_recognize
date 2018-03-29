import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Prediction-key': '82d2bd2e2c4444c590bc80e242800c58',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': '4e83b1ba-87e3-4eb4-9349-1044f2f645f1',
    'application': 'customvision',
})
#body = "http://thisisreno.com/wp-content/uploads/2017/05/Poison_Hemlock-768x512.jpeg"
# body = {"Url": "https://i.imgur.com/0lxAyCX.jpg"}
body = open("m.jpg", mode="rb")
conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
conn.request("POST", "/customvision/v1.1/Prediction/91c2afcb-d86e-470b-a884-4a8e0238590c/image?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()
result = json.loads(data.decode('ascii'))
print(result["Predictions"][0]["Probability"]>result["Predictions"][1]["Probability"])
conn.close()
