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
oc new-project rvr

Kafka Resources

Install AMQ Streams Operator/Subscription in rvr project

oc apply -f <filename>

** I have been installating the Operator manually. Need to figure out the correct YAML for the Operator
    
Define Kafka Cluster
    kafka-rvr-cluster.yaml 
    ** Should configuration allow dynamic topics?

Topic(s)
    kafkatopic-twilio-in.yaml
    kafkatopic-rvr-telemetry.yaml
    ** What is guidance/best practice? Sould this be dynamic?

Kafka Bridge
    kafkabridge-rvr-kafka-bridge.yaml
    
Bridge Route
    route-kafka-bridge-route.yaml

    Get the route Host as you will use this for integration 
    oc get route kafka-bridge-route
    

Deploy Kafdrop - https://hub.docker.com/r/obsidiandynamics/kafdrop
kafdrop_dc.yaml
kafdrop_service.yaml
kafdrop_route.yaml

## Deploy Node.red image and flow

https://hub.docker.com/r/nodered/node-red

** Currently through the Developer UI

Docuement the route as you will need it for the integration with Twilio

Import the /node-red/twilio-kafka.json into the Node.red.

Update the 'Post Kafka Message' with the Bridge URL

Click Deploy

## Update Twilio

Update Messaging in Twilio


## Install python on the RVR

Follow the instructions to install the python SDK
https://github.com/sphero-inc/sphero-sdk-raspberrypi-python

I created a sphero-dev directory placed the sdk there.

Within the sdk directory, I created /projects/msg_rvr directory 

'''
/sphero-dev/sphero-sdk-raspberrypi-python-master/projects/msg_rvr
'''

Upload the /msg_rvr files to this location.

** the use of the external config.ini is WIP *** The initial versions of the files will require you to update the Bridge URL.

Of course, as long as they reference the sdk, they can be placed in another location.

create a shell - ''' $ pipenv shell'''

Pulls messages from twilio-in topic and can change color or simple movement
$ python msg_rvr_local_event.py

Sends simple sensor data and battery info to telemetry topic
$ python msg_rvr_local_event.py


## Running

A key objective of this project was to use the HTTP Bridge in order to simplify the integration with Kafka.

Initially I've been performing the initialization via Postman but have started to build this in the init_messaging.py.

Content-Type - application/vnd.kafka.v2+json

Check Cluster Health
{{hostname}}/healthy

Create Consumer
{{hostname}}/consumers/rvr-group
{
    "name": "rvr-consumer",
    "format": "json",
    "enable.auto.commit": false
  }

Subscribe to Topic
{{hostname}}/consumers/rvr-group/instances/rvr-consumer/subscription
{
    "topics": [
        "twilio-in"
    ]
}

Test Send Message directly to Topic

Test message to Node.Red - Emulate Twilio

Get Messages


## Once it's all configured, send a text to your Twilio number.  