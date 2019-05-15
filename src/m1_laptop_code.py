"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jonah Egertson.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Jonah Egertson")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    forward_button = ttk.Button(frame, text="Go Forward")
    backward_button = ttk.Button(frame, text="Go Backward")
    go_until_button = ttk.Button(frame, text="Go Until (Distance)")
    speed_entry = ttk.Entry(frame)
    speed_entry.insert(0,"Speed")
    dist_entry = ttk.Entry(frame)
    dist_entry.insert(0,"Distance")
    delta_entry = ttk.Entry(frame)
    delta_entry.insert(0,"Delta (for Go Until)")

    forward_button.grid()
    backward_button.grid()
    go_until_button.grid()
    speed_entry.grid()
    dist_entry.grid()
    delta_entry.grid()

    forward_button["command"] = lambda: send_forward(
        int(speed_entry.get()), int(speed_entry.get()), int(dist_entry.get()), mqtt_sender)
    backward_button["command"] = lambda: send_backward(
        int(speed_entry.get()), int(speed_entry.get()), int(dist_entry.get()), mqtt_sender)
    go_until_button["command"] = lambda: send_go_until(int(speed_entry.get()),int(dist_entry.get()),int(delta_entry.get()),mqtt_sender)
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.

def send_forward(left,right,dist,mqtt):
    print('Sending Message: Forward', left, dist)
    mqtt.send_message("forward",[left,right,dist])

def send_backward(left,right,dist,mqtt):
    print('Sending Message: Backward', left, dist)
    mqtt.send_message("backward",[left,right,dist])

def send_go_until(speed,dist,delta,mqtt):
    i=0
    print('Sending Message: Go Until',dist,delta,speed)
    mqtt.send_message("go_until",[dist,delta,speed])