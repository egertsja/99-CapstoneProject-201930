"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Shane Saylor.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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

    # TODO: Add methods here as needed.
    def arm_up(self, speed):
        """Moves the arm all the way up to its touch sensor"""
        self.robot.arm_and_claw.motor.turn_on(speed)
        while True:
            if self.robot.arm_and_claw.touch_sensor.is_pressed():
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_calibrate(self, speed):
        """
        Moves the arm all the way up to its touch sensor
        Then down 14.2 revolutions
        Then sets that position as 0
        """
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.reset_position()
        self.robot.arm_and_claw.motor.turn_on(-1 * speed)
        while True:
            if self.robot.arm_and_claw.motor.get_position() == -14.2*360:
                self.robot.arm_and_claw.motor.turn_off()
                break
        self.robot.arm_and_claw.motor.reset_position()

    def arm_to(self, speed, position):
        """Moves arm up or down to the given position"""
        print('Arm_to')
        while True:
            current = self.robot.arm_and_claw.motor.get_position()
            print(current)
            if current < position:
                self.robot.arm_and_claw.motor.turn_on(speed)
            elif current > position:
                self.robot.arm_and_claw.motor.turn_on(-1*speed)
            else:
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_down(self, speed):
        """Moves arm down to position 0"""
        self.robot.arm_and_claw.motor.turn_on(-1*speed)
        while True:
            current = self.robot.arm_and_claw.motor.get_position()
            if current == 0:
                self.robot.arm_and_claw.motor.turn_off()
                break

    def go_until_color(self, color, speed):
        """Goes forward until the ColorSensor sees the given color"""
        goal = self.robot.sensor_system.color_sensor.get_color_number_from_color_name(color)
        self.robot.drive_system.go(speed, speed)
        while True:
            current = self.robot.sensor_system.color_sensor.get_color()
            if current == goal:
                self.robot.drive_system.stop()
                break


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

