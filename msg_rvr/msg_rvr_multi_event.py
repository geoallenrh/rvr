import os
import sys
import time
import requests
import polling
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import DriveFlagsBitmask

rvr = SpheroRvrObserver()




hostname ='http://kafka-bridge-route-rvr.apps.cluster-orielly-6809.orielly-6809.sandbox661.opentlc.com'
url = hostname + '/consumers/rvr-group/instances/rvr-consumer/records'
headers = {'accept': 'application/vnd.kafka.json.v2+json'}
process_messages = True


def get_messages():
    # get messages through Kafka Bridge
    
    while(process_messages):
        resp = requests.get(url,headers=headers)
        print(resp.status_code)
        if (resp.status_code == 200 and resp.text != "[]"):
            # This means we should have some data, if we don't will wait and try again.
            records = resp.json()
            print(records)
            for i in records: 
                print(i)
                #command = records[i]['value']['Body'].lower().strip()
                command = i['value']['Body'].lower().strip()
                print("Command: " + command)
                process_command(command)
        else:
            time.sleep(5)
            continue
        
        
def process_command(cmd):
    rvr_cmd = cmd
    rvr.wake()
        
    if (rvr_cmd == "drive"):
        time.sleep(2)

        rvr.reset_yaw()

        rvr.drive_with_heading(
            speed=128,  # Valid speed values are 0-255
            heading=0,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_heading(
            speed=128,  # Valid speed values are 0-255
            heading=0,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.drive_reverse.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)

    else:
        colorValue = (Colors[rvr_cmd])
        print(colorValue)

        #rvr.led_control.set_all_leds_color(color=Colors.blue)
        rvr.led_control.set_all_leds_color(Colors[rvr_cmd])
        # Delay to show LEDs change
        time.sleep(1)
        rvr.led_control.turn_leds_off()
        time.sleep(1)
        rvr.led_control.set_all_leds_color(Colors[rvr_cmd])


def main():
    """ This program will get commands Twilio message and process. """
    try:
        get_messages()
        
    
    except KeyboardInterrupt:
        print('\nProgram termintated with keyboard interrupt.')
    
    finally:
        rvr.close()
        
if __name__ == '__main__':
    main()