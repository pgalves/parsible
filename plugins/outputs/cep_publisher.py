import requests
import json

CEP_HOSTNAME = "10.0.1.100"
CEP_PORT = "8080"
CEP_INSTANTCE_NAME = "ProtonOnWebServer"
cep_url = "http://" + CEP_HOSTNAME + ":" + CEP_PORT + "/" + CEP_INSTANTCE_NAME + "/rest/events"


# Publish the events extracted from the log lines to the CEP instance
def output_cep_publish(data):
    payload = json.dumps(data)
    print "PAYLOAD:", payload
    headers = {'content-type': 'application/json'}
    r = requests.post(cep_url, data=payload, headers=headers)
