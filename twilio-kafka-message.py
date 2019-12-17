import requests
import json

test_records = """
    { 
        "records": [
            {
            "key":"SM9502d827b23cd1e6128cc2ca60576ffb",
            "value": {"ApiVersion":"2010-04-01", "SmsSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "SmsStatus":"received", "SmsMessageSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "NumSegments":"1", "From":"+14173802843", "ToState":"NJ", "MessageSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "AccountSid":"ACf5945ec5d9e7cfe500893a264097d8e2", "ToZip":"07930", "FromCountry":"US", "ToCity":"HACKENSACK", "FromCity":"SPRINGFIELD", "To":"+12015844158", "FromZip":"65806", "Body":"Red", "ToCountry":"US", "FromState":"MO", "NumMedia":"0"}
         }
                     ]
    }
    """

response = requests.get(
    'http://rvr-kafka-bridge-route-rvr.apps.cluster-sgf-633d.sgf-633d.example.opentlc.com:80/consumers/rvr-group/instances/rvr-consumer/records',
    headers={'Accept': 'application/vnd.kafka.json.v2+json'},
    )

# View the new `text-matches` array which provides information
# about your search term within the results
status_code = response.status_code
print(status_code)
print(response.text == "[]")

if (response.status_code == 200 and response.text != "[]" ):
    #returns a dict (it's a function!)
    records = response.json()
    command = records[0]['value']['Body']
    print(command.lower())
else:
    print("nothing there")
    

