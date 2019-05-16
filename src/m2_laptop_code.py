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
    frame = ttk.Frame(window, padding=12, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Zach Witonsky")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # DONE: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    spin_right_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")
    dist_label = ttk.Label(frame, text="Degrees")

    spin_left_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    spin_left_entry.insert(0, "100")
    spin_right_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    spin_right_entry.insert(0, "100")
    dist_entry = ttk.Entry(frame, width=15, justify=tkinter.CENTER)
    dist_entry.insert(0, "3")

    left_button = ttk.Button(frame, text="Spin Left", width=10)
    right_button = ttk.Button(frame, text="Spin Right", width=10)
    dist_button = ttk.Button(frame, text="Rotations", width=15)
    stop_button = ttk.Button(frame, text="Stop", width=15)

    frame_label.grid(row=0, column=1)
    spin_left_label.grid(row=1, column=0)
    spin_right_label.grid(row=1, column=2)
    dist_label.grid(row=1, column=1)

    spin_left_entry.grid(row=2, column=0)
    spin_right_entry.grid(row=2, column=2)
    dist_entry.grid(row=2, column=1)

    left_button.grid(row=3, column=0)
    right_button.grid(row=3, column=2)
    stop_button.grid(row=3, column=1)

    left_button["command"] = lambda: handle_spin_left(
        spin_left_entry, spin_right_entry, dist_entry, mqtt_sender)
    right_button["command"] = lambda: handle_spin_right(
        spin_left_entry, spin_right_entry, dist_entry, mqtt_sender)
    # number_spins_button["command"] = lambda: handle_number_spins()

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

def go(mqtt_sender, direction, spin_left_speed, spin_right_speed, dist_value):
    print()
    print(direction)
    print("Left wheel motor speed:", spin_left_speed, "for", dist_value, "degrees")
    print("Right wheel motor speed:", spin_right_speed, "for", dist_value, "degrees")

    mqtt_sender.send_message("go", [spin_left_speed, spin_right_speed, dist_value])

def handle_spin_left(spin_left_box, spin_right_box, dist_box, mqtt_sender):
    left = -int(spin_left_box.get())
    right = int(spin_right_box.get())
    dist = int(dist_box.get())
    go(mqtt_sender, "SPIN LEFT", left, right, dist)

def handle_spin_right(spin_left_box, spin_right_box, dist_box, mqtt_sender):
    left = int(spin_left_box.get())
    right = -int(spin_right_box.get())
    dist = int(dist_box.get())
    go(mqtt_sender, "SPIN RIGHT", left, right, dist)

# def handle_number_spins():

def handle_stop(mqtt_sender):
    print()
    print("The movement has STOPPED.")
    mqtt_sender.send_message("stop", [])





