"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Shane Saylor.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Shane Saylor")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_button = ttk.Button(frame, text='Arm Up')
    speed_entry_box = ttk.Entry(frame, width=8)
    speed_entry_box.insert(0, '100')
    arm_calibrate_button = ttk.Button(frame, text='Calibrate Arm')
    arm_to_button = ttk.Button(frame, text='Arm to')
    position_entry_box = ttk.Entry(frame, width=8)
    arm_down_button = ttk.Button(frame, text='Arm Down')
    arm_speed_label = ttk.Label(frame, text='Arm Speed')
    arm_position_label = ttk.Label(frame, text='Arm Position (0-360)')

    go_until_color_button = ttk.Button(frame, text='Go Until Color')
    color_entry_box = ttk.Entry(frame, width=8)
    color_label = ttk.Label(frame, text='Color:')
    color_speed_box = ttk.Entry(frame, width=8)
    color_speed_box.insert(0, '50')
    color_speed_label = ttk.Label(frame, text='Speed:')

    arm_up_button.grid(row=1, column=1)
    speed_entry_box.grid(row=2, column=0)
    arm_calibrate_button.grid(row=1, column=2)
    arm_to_button.grid(row=2, column=2)
    position_entry_box.grid(row=2, column=3)
    arm_down_button.grid(row=2, column=1)
    arm_speed_label.grid(row=1, column=0)
    arm_position_label.grid(row=1, column=3)

    go_until_color_button.grid(row=3, column=0)
    color_label.grid(row=3, column=1)
    color_entry_box.grid(row=3, column=2)
    color_speed_box.grid(row=4, column=2)
    color_speed_label.grid(row=4, column=1)

    arm_up_button['command'] = lambda: handle_arm_up(speed_entry_box, mqtt_sender)
    arm_calibrate_button['command'] = lambda: handle_arm_calibrate(speed_entry_box, mqtt_sender)
    arm_to_button['command'] = lambda: handle_arm_to(speed_entry_box, position_entry_box, mqtt_sender)
    arm_down_button['command'] = lambda: handle_arm_down(speed_entry_box, mqtt_sender)

    go_until_color_button['command'] = lambda: handle_go_until_color(color_entry_box, color_speed_box, mqtt_sender)

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
def handle_arm_up(speed_entry_box, mqtt_sender):
    print('handle_arm_up: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('arm_up', [speed])


def handle_arm_calibrate(speed_entry_box, mqtt_sender):
    print('handle_arm_calibrate: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('arm_calibrate', [speed])


def handle_arm_to(speed_entry_box, position_entry_box, mqtt_sender):
    print('handle_arm_to: ', speed_entry_box.get(), position_entry_box.get())
    speed = int(speed_entry_box.get())
    position = int(position_entry_box.get())
    mqtt_sender.send_message('arm_to', [speed, position])


def handle_arm_down(speed_entry_box, mqtt_sender):
    print('handle_arm_down: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('arm_down', [speed])


def handle_go_until_color(color_entry_box, color_speed_box, mqtt_sender):
    print('handle_go_until_color: ', color_entry_box.get(), color_speed_box.get())
    color = str(color_entry_box.get())
    speed = int(color_speed_box.get())
    mqtt_sender.send_message('go_until_color', [color, speed])

