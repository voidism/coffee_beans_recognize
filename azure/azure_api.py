import http.client, urllib.request, urllib.parse, urllib.error, base64, json

class API:
    def __init__(self):
        self.headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Prediction-key': '###############',
        }

        self.params = urllib.parse.urlencode({
            # Request parameters
            'iterationId': '###########################',
            'application': 'customvision',
        })
        self.body = None
        self.response = None
        self.conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')

    def quest(self,filename):
        self.body = open(filename, mode="rb")
        self.conn.request("POST", "/customvision/v1.1/Prediction/#################/image?%s" % self.params, self.body, self.headers)
        self.response = self.conn.getresponse()
        data = self.response.read()
        result = json.loads(data.decode('ascii'))
        ans = 0
        if result["Predictions"][0]["Probability"]>result["Predictions"][1]["Probability"]:
            ans = result["Predictions"][0]['Tag'] == "good_beans"
        print("result:",ans)
        return ans



    def __exit__(self):
        self.conn.close()
