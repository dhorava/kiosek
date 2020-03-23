import json
import requests

class DatabricksAPI():

    def __init__(self):
        self.token = 'dapi76a91a2c9fc7bc4c99f2d4e24d7bd18e'
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.api_url = 'https://westeurope.azuredatabricks.net/api/'

    def runNow(self, job_id, email):

        endpoint = '2.0/jobs/run-now'
        url = self.api_url + endpoint
        headers = self.headers

        data = {
            "job_id": job_id,
            "notebook_params": {
                "email": email
            }
        }

        print(url)
        print(headers)
        print(data)

        response = requests.post(url, data=data, headers=headers)
        r = response.json()

        print(r)

        return r
