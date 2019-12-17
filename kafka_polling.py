import requests
import polling

# url = 'http://localhost:8080/dynarest/Kafka/1.0/record'
url = 'http://rvr-kafka-bridge-route-rvr.apps.cluster-sgf-633d.sgf-633d.example.opentlc.com:80/consumers/rvr-group/instances/rvr-consumer/records'

def is_correct_response(resp):
     print(resp.status_code)
     if (resp.status_code == 200 and resp.text != "[]"):
        # This means we should have some data.
        records = resp.json()
        print(records)
        command = records[0]['value']['Body'].lower()
        print("Command: " + command)
        return resp == 'success'

polling.poll(
    lambda: requests.get(url, headers={'Accept': 'application/vnd.kafka.json.v2+json'},),
    check_success=is_correct_response,
    step=10,
    #timeout=5
    poll_forever=True
    )