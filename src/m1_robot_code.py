"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jonah Egertson.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
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

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # TODO: Add methods here as needed.

    def forward(self, left, right, dist):
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.right_motor.reset_position()

        init_pos = self.robot.sensor_system.ir_proximity_sensor.get_distance()

        #Determine inches/degree (inches from dist, degrees from sensor)
        degrees = 360
        dist_per_spin = self.robot.drive_system.wheel_circumference
        deg_ratio = degrees/dist_per_spin
        dist_deg = deg_ratio * dist

        position = (self.robot.drive_system.left_motor.get_position()+self.robot.drive_system.right_motor.get_position())/2

        while abs(position) < dist_deg: #insert condition
            self.robot.drive_system.left_motor.turn_on(left)
            self.robot.drive_system.right_motor.turn_on(right)
            position = (self.robot.drive_system.left_motor.get_position()+self.robot.drive_system.right_motor.get_position())/2

        self.robot.drive_system.left_motor.turn_off()
        self.robot.drive_system.right_motor.turn_off()

        print('Movement has concluded')

        #Check distance

        final_pos = self.robot.sensor_system.ir_proximity_sensor.get_distance()

        if abs(final_pos-init_pos) < (dist - (dist/5)) or abs(final_pos-init_pos) > (dist + (dist/5)):
            print('Unfortunately it was wildly off. Perhaps the code is wrong or a sensor is malfunctioning. Or maybe it is just on the wooden board or something stupid like that.')
        else:
            print('It arrived within 20% of its target distance. Nice work!')


        # Placeholder

    def backward(self, left, right, dist):
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.right_motor.reset_position()

        init_pos = self.robot.sensor_system.ir_proximity_sensor.get_distance()

        # Determine inches/degree (inches from dist, degrees from sensor)
        degrees = 360
        dist_per_spin = self.robot.drive_system.wheel_circumference
        deg_ratio = degrees / dist_per_spin
        dist_deg = deg_ratio * dist

        position = (self.robot.drive_system.left_motor.get_position() + self.robot.drive_system.right_motor.get_position()) / 2

        while abs(position) < dist_deg:  # insert condition
            self.robot.drive_system.left_motor.turn_on(-1*left)
            self.robot.drive_system.right_motor.turn_on(-1*right)
            position = (self.robot.drive_system.left_motor.get_position() + self.robot.drive_system.right_motor.get_position()) / 2

        self.robot.drive_system.left_motor.turn_off()
        self.robot.drive_system.right_motor.turn_off()

        print('Movement has concluded')

        # Check distance

        final_pos = self.robot.sensor_system.ir_proximity_sensor.get_distance()

        if abs(final_pos - init_pos) < (dist - (dist / 5)) or abs(final_pos - init_pos) > (dist + (dist / 5)):
            print(
                'Unfortunately it was wildly off. Perhaps the code is wrong or a sensor is malfunctioning. Or maybe it is just on the wooden board or something stupid like that.')
        else:
            print('It arrived within 20% of its target distance. Nice work!')


def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.


