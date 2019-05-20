"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Zach Witonsky .
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import time
import m2_robot_code as m2
import m3_robot_code as m3

class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    def spin(self, left_motor_speed, right_motor_speed):
        """Spins"""
        print_message_received("spin", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    def deg(self, left_motor_speed, right_motor_speed, deg):

        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.right_motor.reset_position()

        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

        while abs(self.robot.drive_system.left_motor.get_position()/4.5) < deg:  # insert condition
            pass

        self.robot.drive_system.left_motor.turn_off()
        self.robot.drive_system.right_motor.turn_off()

    def spin_until_facing(self, x, speed):

        blob = self.robot.sensor_system.camera.get_biggest_blob()
        print(blob)

        # turn left
        if blob.center.x <= x:
            while True:
                self.robot.drive_system.go(-speed, speed)
                if blob.center.x >= x:
                    self.robot.drive_system.stop()
                    break

        # turn right
        if blob.center.x >= x:
            while True:
                self.robot.drive_system.go(speed, -speed)
                if blob.center.x <= x:
                    self.robot.drive_system.stop()
                    break

# take out signature and delta and big_enough
# stopping cond: center of object x cord is "close to" x
#
    #
    # TODO: Add methods here as needed.

def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

