import rclpy
import math
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
from typing import List

#global variables

pub1 = None
pub2 = None
key = False
key2 = False
name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2","neck_to_body","head_to_neck"]
name_wheels = ["w1","w2","w3","w4"]
actual_position = None
#---------------------------------- Verify Pose ----------------------------------
def verificar_pose_alcanzada(pose_actual: List[float], pose_objetivo: List[float]) -> bool:
    # Margen de error tolerado en radianes (aprox 0.5 grados de diferencia)
    tolerancia = 0.008 
    
    # Comparamos joint por joint
    for i in range(len(pose_actual)):
        if not math.isclose(pose_actual[i], pose_objetivo[i], abs_tol=tolerancia):
            # Con un solo joint que esté fuera de rango, el robot aún no llega
            return False 
            
    return True
#---------------------------------- Callback Joint States ----------------------------------
def callback_joint_states(msg: JointState):
    global actual_position
    joint_states = msg

    actual_position = joint_states.position


#---------------------------------- Pose 1 ----------------------------------
def pose1():
    global pub1
    global pub2
    global key
    global name_joints
    global name_wheels
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    #           LF1     LF2     RF1     RF2     LB1    LB2     RB1     RB2    Neck   Head  
    position = [-0.785, 0.785, -0.785, -0.785, -0.785, -0.785, -0.785, 0.785, 0.0, 0.0]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [0.0, 0.0, 0.0, 0.0]
    
    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints

    #assigning parameters to message Float32MultiArray
    wheels.data = velocity_wheels

    for i in range(0, len(name_joints)):
        print(f"{name_joints[i]}: {position[i]}")
    for i in range(0, len(name_wheels)):
        print(f"{name_wheels[i]}: {velocity_wheels[i]}")

    if verificar_pose_alcanzada(position, position):
        key = True

    pub1.publish(joint)
    pub2.publish(wheels) 

#---------------------------------- Pose 2 ----------------------------------
def pose2():
    global pub1
    global pub2
    global key2
    global name_joints
    global name_wheels
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    #           LF1     LF2     RF1     RF2     LB1    LB2     RB1     RB2    Neck   Head  
    position = [-0.785, 0.785, -0.785, -0.785, -2.356, -0.785, -2.356, 0.785, 0.0, 0.0]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [0.0, 0.0, 0.0, 0.0]
    
    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints

    #assigning parameters to message Float32MultiArray
    wheels.data = velocity_wheels

    for i in range(0, len(name_joints)):
        print(f"{name_joints[i]}: {position[i]}")
    for i in range(0, len(name_wheels)):
        print(f"{name_wheels[i]}: {velocity_wheels[i]}")

    if verificar_pose_alcanzada(position, position):
        key2 = True

    pub1.publish(joint)
    pub2.publish(wheels) 

#---------------------------------- Main ----------------------------------
def main():
    global pub1
    global pub2
    global key
    global actual_position

    #init ros2
    rclpy.init()

    #create a node
    node = rclpy.create_node("nInit_robot")

    #create a publisher
    pub1 = node.create_publisher(JointTrajectory,"/fiar_controller/joint_trajectory",10)
    pub2 = node.create_publisher(Float64MultiArray,"/fiar_wheel_controller/commands",10)
    sub1 = node.create_subscription(JointState, "/joint_states", 10, callback_joint_states)

    key = verificar_pose_alcanzada(position, position)

    if not key:
        node.create_timer(2.0,pose1)
        print("xd")
        
    elif key==True:
        node.create_timer(2.0,pose2)
        print("xdd")

    
    

    #keep alive the node
    rclpy.spin(node)

    #shutdown
    rclpy.shutdown()
    node.destroy_node()

if __name__ == "__main__":
    main()
