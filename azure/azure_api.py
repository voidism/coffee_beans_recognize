import http.client, urllib.request, urllib.parse, urllib.error, base64, json

class API:
    def __init__(self):
        self.headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Prediction-key': '82d2bd2e2c4444c590bc80e242800c58',
        }

        self.params = urllib.parse.urlencode({
            # Request parameters
            'iterationId': '4e83b1ba-87e3-4eb4-9349-1044f2f645f1',
            'application': 'customvision',
        })
        self.body = None
        self.response = None
        self.conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')

    def quest(self,filename):
        self.body = open(filename, mode="rb")
        self.conn.request("POST", "/customvision/v1.1/Prediction/91c2afcb-d86e-470b-a884-4a8e0238590c/image?%s" % self.params, self.body, self.headers)
        self.response = self.conn.getresponse()
        data = self.response.read()
        result = json.loads(data.decode('ascii'))
        ans = result["Predictions"][0]["Probability"]>result["Predictions"][1]["Probability"]
        print("result:",ans)
        return ans

    def __exit__(self):
        self.conn.close()
