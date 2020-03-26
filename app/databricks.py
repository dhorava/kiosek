import json
import requests

class DatabricksAPI():

    def __init__(self):
        self.token = 'dapi76a91a2c9fc7bc4c99f2d4e24d7bd18e'
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.api_url = 'https://westeurope.azuredatabricks.net/api/2.0/'

    def runNow(self, job_id, email):

        endpoint = 'jobs/run-now'
        url = self.api_url + endpoint
        headers = self.headers

        data = '{"job_id":' + str(job_id) + ',"notebook_params":{"email":"' + str(email) + '"}}'

        print(url)
        print(headers)
        print(data)

        response = requests.post(url, data=data, headers=headers)
        r = response.json()

        print(r)

        return r


    def getJobRuns(self, job_id):

        endpoint = 'jobs/runs/list?job_id='
        url = self.api_url + endpoint + str(job_id)
        headers = self.headers

        #print(url)
        #print(headers)

        response = requests.get(url, headers=headers)
        r = response.json()

        #print(r)

        return r
