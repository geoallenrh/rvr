#  Twilio, Red Hat AMQ Streams and Sphero RVR

I was exploring opportunities to learn about AMQ Streams and had obtained a RVR to play around with.  I thought it would be fun to explore the world of asynchronous messaging with all the capabilities in the RVR.

## Bill of Materials

Sphero RVR - https://www.sphero.com/rvr

Supported Raspberry Pi (I'm using the Pi 3 B+)
https://sdk.sphero.com/docs/getting_started/raspberry_pi/raspberry_pi_setup/

Twilio Account - https://www.twilio.com/

Red Hat Openshift - Tested with v4.2 and 4.3 and AMQ Streams Operator 1.4.0


## Deployment Steps

### Openshift Resources

Create New Project
```shell
oc new-project rvr
```
Kafka Resources

Install AMQ Streams Operator/Subscription in rvr project
```shell
oc apply -f <filename>
```
*I have been installaing the Operator manually. Need to figure out the correct YAML for the Operator deployment *
    
### Create Kafka Cluster
```shell
oc apply -f kafka-rvr-cluster.yaml 
```
    Should configuration allow dynamic topics?

### Create Topic(s)
```shell
oc apply -f kafkatopic-twilio-in.yaml
oc apply -f kafkatopic-rvr-telemetry.yaml
```
    What is guidance/best practice? Should this be dynamic?

### Create Kafka Bridge
```shell
oc apply -f kafkabridge-rvr-kafka-bridge.yaml
```
### Create Bridge Route
```shell
oc apply -f route-kafka-bridge-route.yaml
```

### Get the route Host as you will use this for integration 
```shell
    oc get route kafka-bridge-route
```
    

### Deploy Kafdrop - https://hub.docker.com/r/obsidiandynamics/kafdrop
kafdrop_dc.yaml
kafdrop_service.yaml
kafdrop_route.yaml

## Deploy Twilio Message Handler

Deploying the application as Java application in OpenShift
In this section, we are going to leverage the S2I build mechanism of OpenShift. 
We use a Java S2I Builder, and therefore do not need a Dockerfile in this approach. 
You do not need to locally clone the Git repository, as it will be directly built inside OpenShift. We are going to create an OpenShift build executing it:

# Build and Deploy to Openshift
```shell
oc new-app registry.access.redhat.com/redhat-openjdk-18/openjdk18-openshift~https://github.com/geoallenrh/rvr --context-dir=quarkus/twilio-handler/ --name=rvr-twilio-handler
oc logs -f bc/rvr-twilio-handler
```
# To create the route
```shell
oc expose svc/rvr-twilio-handler
```
# Get the route URL
```shell
export URL="http://$(oc get route | grep rvr-twilio-handler | awk '{print $2}')"
```

## Update Twilio

Update The WebHook In Twilio Messaging service.

## Install python on the RVR

Follow the instructions to install the python SDK
https://github.com/sphero-inc/sphero-sdk-raspberrypi-python

I created a sphero-dev directory and placed the sdk there.

Within the sdk directory, I created /projects/msg_rvr directory 

'''
/sphero-dev/sphero-sdk-raspberrypi-python-master/projects/msg_rvr
'''

Upload the /msg_rvr files to this location.

** the use of the external config.ini is WIP *** The initial versions of the files will require you to update the Bridge URL.

Of course, as long as they reference the sdk, they can be placed in another location.

create a shell
```
$ pipenv shell
```

Pulls messages from twilio-in topic and can change color or simple movement
```shell
$ python msg_rvr_local_event.py
```

Sends simple sensor data and battery info to telemetry topic
```shell
$ python msg_rvr_local_event.py
```

## Testing and Execution

A key objective of this project was to use the HTTP Bridge in order to simplify the integration with Kafka.

I've been performing the testing and consumer initialization via Postman but have started to build this in the init_messaging.py.

Ensure you are using the correct Content-Type
```
Content-Type - application/vnd.kafka.v2+json
```

Check Cluster Health
```
{{hostname}}/healthy
```

Create Consumer
```
{{hostname}}/consumers/rvr-group
```
{
    "name": "rvr-consumer",
    "format": "json",
    "enable.auto.commit": false
  }

Subscribe to Topic
```
{{hostname}}/consumers/rvr-group/instances/rvr-consumer/subscription
```
{
    "topics": [
        "twilio.in"
    ]
}

Test Send Message directly to Topic
```
{{hostname}}/topics/twilio.in
```
Example Kafka Record of Twilio Message (Add in your numbers)
```
{
    "records": [
        {
            "key":"SM9502d827b23cd1e6128cc2ca60576ffb",
            "value": {"ApiVersion":"2010-04-01", "SmsSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "SmsStatus":"received", "SmsMessageSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "NumSegments":"1", "From":"<your phone number>", "ToState":"NJ", "MessageSid":"SM9502d827b23cd1e6128cc2ca60576ffb", "AccountSid":"<AccountSid>", "ToZip":"07930", "FromCountry":"US", "ToCity":"HACKENSACK", "FromCity":"SPRINGFIELD", "To":"<from twilio number>", "FromZip":"65806", "Body":"blue", "ToCountry":"US", "FromState":"MO", "NumMedia":"0"}
        }
    ]
}
```

Test message to Twilio Handler - Emulate Twilio
The Content-Type from Twilio is application/x-www-form-urlencoded


Get Messages
```
{{hostname}}/consumers/rvr-group/instances/rvr-consumer/records
```

Get Existing Subscriptions - If the subscription is removed from the broker, then you will have to redefine.
```
{{hostname}}/consumers/rvr-group/instances/rvr-consumer/subscription
```


## Once it's all configured, send a text to your Twilio number.  Good luck!
The only commands that are currently supported is to change the color and to do a simple movement.

Send the color you want to see or ‘Drive’ to move the RVR

(These are the predefined colors)
```
red
green
blue 
white 
yellow 
purple
orange 
pink
```
Send the color or the command 'Drive' as the body of the message.
