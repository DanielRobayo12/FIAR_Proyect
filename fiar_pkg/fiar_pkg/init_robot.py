from ament_index_python import packages
import rclpy
import math
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
from typing import List
import time

#global variables

pub1 = None
pub2 = None
key = False 
actual_position = [0.0]*8
name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2"]
name_wheels = ["w1","w2","w3","w4"]
velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
velocity_wheels = [0.0, 0.0, 0.0, 0.0]

#---------------------------------- Main ----------------------------------
def main():
    global pub1
    global pub2
    rclpy.init()

    #create a node
    node = rclpy.create_node("nInit_robot")

    #create a publisher
    pub1 = node.create_publisher(JointTrajectory,"/fiar_controller/joint_trajectory",10)
    pub2 = node.create_publisher(Float64MultiArray,"/fiar_wheel_controller/commands",10)
    sub1 = node.create_subscription(JointState, "/joint_states", callback_joint_states,10)

    #Create a timer
    node.create_timer(0.1,loop)
      
    #keep alive the node
    rclpy.spin(node)

    #shutdown
    rclpy.shutdown()
    node.destroy_node()

#---------------------------------- Loop ----------------------------------
def loop():
    global pub1, pub2, key
    global name_joints, name_wheels, actual_position
     
    #           LF1     LF2     RF1     RF2     LB1    LB2     RB1     RB2    
    position1 = [-0.785, 0.785, 0.785, -0.785, -0.785, 0.785, 0.785, -0.785]
    position2 = [-0.785, 0.785, -0.785, -0.785, -2.356, -0.785, -2.356, 0.785]

    if key == False:
        key = verify_pose(actual_position, position1)

    print(f"KEY: {key}")
    print(f"Actual: {actual_position}")
    print(f"Goal: {position1}")
    match key:
        case False:
            pose(position1)
        case True:
            #pose(position2)
            pass
            
    
    
#---------------------------------- pose1 ----------------------------------
def pose(position_a):
    global pub1, pub2, velocity_wheels
    global name_joints, name_wheels, velocity_joints
    
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()
    
    #assigning parameters to message JointTrajectoryPoint
    point.positions = position_a
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=2000000000)

    #assigning parameters to message 
    joint.points.append(point)
    joint.joint_names = name_joints
    wheels.data = velocity_wheels

    #publish
    pub1.publish(joint)
    pub2.publish(wheels) 
#---------------------------------- Verify Pose ----------------------------------
def verify_pose(lista1, lista2, tolerancia=0.1):
    # Verificar que tengan el mismo tamaño
    if len(lista1) != len(lista2):
        print("The lists do not have the same size")
        return False

    # Comparar elemento por elemento
    for a, b in zip(lista1, lista2):
        if abs(a - b) > tolerancia:
            return False

    return True
#---------------------------------- Callback Joint States --------------------------------
def callback_joint_states(msg: JointState):
    global actual_position, name_joints
    joint_states = msg
    names = joint_states.name

    #Organize the order of positions like the position1 array order
    for i in range(len(name_joints)):
        for j in range(len(actual_position)):

            if name_joints[i] == names[j]:
                actual_position[i] = joint_states.position[j]

#---------------------------------- print pose ------------------------------------------
def print_pose(position, velocity_wheels):
    for i in range(0, len(name_joints)):
        print(f"{name_joints[i]}: {position[i]}")
    for i in range(0, len(name_wheels)):
        print(f"{name_wheels[i]}: {velocity_wheels[i]}")

#------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()