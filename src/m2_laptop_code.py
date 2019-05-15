"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zach Witonsky.
  Spring term, 2018-2019.
"""
#DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Zach Witonsky")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    spin_right_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    spin_left_entry = ttk.Entry(frame, width=10)
    spin_left_entry.insert(0, "100")
    spin_right_entry = ttk.Entry(frame, width=10, justify=tkinter.RIGHT)
    spin_right_entry.insert(0, "100")

    left_button = ttk.Button(frame, text="Spin Left", width=10)
    right_button = ttk.Button(frame, text="Spin Right", width=10)
    stop_button = ttk.Button(frame, text="Stop")

    frame_label.grid(row=0, column=1)
    spin_left_label.grid(row=1, column=0)
    spin_right_label.grid(row=1, column=2)
    spin_left_entry.grid(row=2, column=0)
    spin_right_entry.grid(row=2, column=2)

    left_button.grid(row=4, column=0)
    right_button.grid(row=4, column=2)
    stop_button.grid(row=4, column=1)

    left_button["command"] = lambda: handle_spin_left(
        spin_left_entry, spin_right_entry, mqtt_sender)
    right_button["command"] = lambda: handle_spin_right(
        spin_left_entry, spin_right_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

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

def go(mqtt_sender, direction, spin_left_speed, spin_right_speed):
    print()
    print(direction)
    print("  using wheel motor speeds:", spin_left_speed, spin_right_speed)
    mqtt_sender.send_message("go", [spin_left_speed, spin_right_speed])

def handle_spin_left(spin_left_box, spin_right_box, mqtt_sender):
    left = -int(spin_left_box.get())
    right = int(spin_right_box.get())
    go(mqtt_sender, "SPIN LEFT", left, right)

def handle_spin_right(spin_left_box, spin_right_box, mqtt_sender):
    left = int(spin_left_box.get())
    right = -int(spin_right_box.get())
    go(mqtt_sender, "SPIN RIGHT", left, right)

def handle_stop(mqtt_sender):
    print()
    print("STOP.")
    mqtt_sender.send_message("stop", [])

def send_forward(left, right, dist, mqtt):
    i = 0
    print('Sending Message: Forward', left, dist)
    mqtt.send_message("forward", [left, right, dist])

def send_backward(left, right, dist, mqtt):
    i = 0
    print('Sending Mesage: Backward', left, dist)
    mqtt.send_message("backward", [left, right, dist])


