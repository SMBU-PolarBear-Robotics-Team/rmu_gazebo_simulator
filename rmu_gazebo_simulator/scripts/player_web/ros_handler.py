# Copyright 2021 Zhenpeng Ge
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rmoss_interfaces.msg import ChassisCmd, GimbalCmd, ShootCmd
from std_msgs.msg import Int32


def publish_chassis_cmd_msg(pub, x, y, w):
    # print('pub chassis')
    msg = ChassisCmd()
    msg.type = msg.FOLLOW_GIMBAL
    msg.twist.linear.x = x
    msg.twist.linear.y = y
    msg.twist.angular.z = w
    # print(msg)
    pub.publish(msg)


def publish_gimbal_cmd_msg(pub, pitch, yaw):
    # print('pub gimbal')
    msg = GimbalCmd()
    msg.pitch_type = msg.ABSOLUTE_ANGLE
    msg.yaw_type = msg.ABSOLUTE_ANGLE
    msg.position.yaw = yaw
    msg.position.pitch = pitch
    # print(msg)
    pub.publish(msg)


def publish_shoot_cmd_msg(pub, num, vel):
    # print('pub shoot')
    msg = ShootCmd()
    msg.projectile_num = num
    msg.projectile_velocity = vel
    # print(msg)
    pub.publish(msg)


def publish_reset_cmd_msg(pub):
    msg = Int32()
    msg.data = 500
    pub.publish(msg)
