import os
import sys
import time
import requests
import polling
import json



hostname ='http://kafka-bridge-route-rvr.apps.cluster-avaya-fb13.avaya-fb13.example.opentlc.com'
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
    rvr.wake()
        
        if (cmd == "drive"):
            time.sleep(2)

            rvr.drive_control.reset_heading()

            rvr.drive_control.roll_start(
                speed=25,
                heading=90
            )

            rvr.drive_control.roll_stop(heading=270)

        else:
            colorValue = (Colors[cmd])
            print(colorValue)

            #rvr.led_control.set_all_leds_color(color=Colors.blue)
            rvr.led_control.set_all_leds_color(Colors[cmd])
            # Delay to show LEDs change
            time.sleep(1)
            rvr.led_control.turn_leds_off()
            time.sleep(1)
            rvr.led_control.set_all_leds_color(Colors[cmd])





def main():
    """ This program will get commands Twilio message and process. """
    try:
        get_messages()
        
    
    except KeyboardInterrupt:
        print('\nProgram termintated with keyboard interrupt.')
    
    #finally:
        #rvr.close()
        
if __name__ == '__main__':
    main()