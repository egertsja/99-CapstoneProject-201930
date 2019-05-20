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
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    spin_left_label = ttk.Label(frame, text="Wheel speed (0 to 100)")
    deg_label = ttk.Label(frame, text="Degrees (0 to 360)")
    x_label = ttk.Label(frame, text="x value")
    delta_label = ttk.Label(frame, text="delta")
    big_enough_label = ttk.Label(frame, text="big enough")

    spin_left_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    spin_left_entry.insert(0, "100")
    # spin_right_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    # spin_right_entry.insert(0, "100")
    deg_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    deg_entry.insert(0, "360")
    signature_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    signature_entry.insert(0, "RED")
    x_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    x_entry.insert(0, "10")
    delta_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    delta_entry.insert(0, "2")
    big_enough_entry = ttk.Entry(frame, width=10, justify=tkinter.CENTER)
    big_enough_entry.insert(0, "5")

    left_button = ttk.Button(frame, text="Spin Left", width=10)
    right_button = ttk.Button(frame, text="Spin Right", width=10)
    stop_button = ttk.Button(frame, text="Stop", width=8)
    signature_button = ttk.Button(frame, text="Color", width=10)

    frame_label.grid(row=0, column=1)
    spin_left_label.grid(row=0, column=0)
    deg_label.grid(row=2, column=0)
    x_label.grid(row=3, column=1)
    delta_label.grid(row=5, column=1)
    big_enough_label.grid(row=3, column=2)

    spin_left_entry.grid(row=1, column=0)
    # spin_right_entry.grid(row=4, column=0)
    deg_entry.grid(row=3, column=0)
    signature_entry.grid(row=1, column=1)
    x_entry.grid(row=4, column=1)
    delta_entry.grid(row=6, column = 1)
    big_enough_entry.grid(row=4, column=2)

    left_button.grid(row=4, column=0)
    right_button.grid(row=5, column=0)
    stop_button.grid(row=0, column=2)
    signature_button.grid(row=2, column=1)

    left_button["command"] = lambda: handle_spin_left(
        spin_left_entry, spin_left_entry, deg_entry, mqtt_sender)
    right_button["command"] = lambda: handle_spin_right(
        spin_left_entry, spin_left_entry, deg_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    signature_button["command"] = lambda: handle_spin_until_facing(
        signature_entry, x_entry, delta_entry, spin_left_entry, big_enough_entry, mqtt_sender)

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

def go(mqtt_sender, direction, spin_left_speed, spin_right_speed, deg):
    print()
    print(direction)
    print("Left wheel motor speed:", spin_left_speed, "for", deg, "degrees")
    print("Right wheel motor speed:", spin_right_speed, "for", deg, "degrees")
    mqtt_sender.send_message("deg", [spin_left_speed, spin_right_speed, deg])

def go2(mqtt_sender, signature, x, delta, speed, big_enough):
    print()
    print("Left and right wheel motor speed:", speed)
    print("Spin until the color", signature, "is found")
    mqtt_sender.send_message("spin_until_facing", [signature, x, delta, speed, big_enough])

def handle_spin_left(spin_left_box, spin_right_box, deg_box, mqtt_sender):
    left = -int(spin_left_box.get())
    right = int(spin_right_box.get())
    deg = int(deg_box.get())
    go(mqtt_sender, "SPIN LEFT", left, right, deg)

def handle_spin_right(spin_left_box, spin_right_box, deg_box, mqtt_sender):
    left = int(spin_left_box.get())
    right = -int(spin_right_box.get())
    deg = int(deg_box.get())
    go(mqtt_sender, "SPIN RIGHT", left, right, deg)

def handle_stop(mqtt_sender):
    print()
    print("STOP.")
    mqtt_sender.send_message("stop", [])

def handle_spin_until_facing(sigature_box, x_box, delta_box, spin_left_box, big_enough_box, mqtt_sender):
    signature = str(sigature_box.get())
    x = int(x_box.get())
    delta = int(delta_box.get())
    speed = int(spin_left_box.get())
    big_enough = int(big_enough_box.get())
    go2(mqtt_sender, signature, x, delta, speed, big_enough)






