from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Float64MultiArray
import rclpy
import time

#global variables
pub1 = None
pub2 = None
#===================== set to cero position ======================
def set_to_cero():
    #declare variables
    global pub1
    global pub2
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    #declare parameters
    name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2","neck_to_body","head_to_neck"]
    name_wheels = ["w1","w2","w3","w4"]
    position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [0.0, 0.0, 0.0, 0.0]
    

    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints
    
    #assigning parameters to message Float64MultiArray
    wheels.data = velocity_wheels
        
    pub1.publish(joint)
    pub2.publish(wheels)

#===================== set to max position =====================
def set_to_max():
    global pub1
    global pub2

    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2","neck_to_body","head_to_neck"]
    name_wheels = ["w1","w2","w3","w4"]
    position = [3.1415,3.1415,3.1415,3.1415,3.1415,3.1415,3.1415,3.1415,3.1415,3.1415]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [1.0, 1.0, 1.0, 1.0]
    

    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)
   

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints
    
    #assigning parameters to message Float64MultiArray
    wheels.data = velocity_wheels

    pub1.publish(joint) 
    pub2.publish(wheels)

#===================== set to min position ======================
def set_to_min():
    #declare variables
    global pub1
    global pub2
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    #declare parameters
    name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2","neck_to_body","head_to_neck"]
    name_wheels = ["w1","w2","w3","w4"]
    position = [-3.1415,-3.1415,-3.1415,-3.1415,-3.1415,-3.1415,-3.1415,-3.1415,-3.1415,-3.1415]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [1.0, 1.0, 1.0, 1.0]
    

    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints
    
    #assigning parameters to message Float64MultiArray
    wheels.data = velocity_wheels
        
    pub1.publish(joint)
    pub2.publish(wheels)

#===================== set to half position ======================
def set_to_half():
    #declare variables
    global pub1
    global pub2
    point= JointTrajectoryPoint()
    joint = JointTrajectory()
    wheels = Float64MultiArray()

    #declare parameters
    name_joints = ["LF1","LF2","RF1","RF2","LB1","LB2","RB1","RB2","neck_to_body","head_to_neck"]
    name_wheels = ["w1","w2","w3","w4"]
    position = [-1.5708,-1.5708,1.5708,1.5708,-1.5708,-1.5708,1.5708,1.5708,1.5708,1.5708]
    velocity_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    velocity_wheels = [1.0, 1.0, 1.0, 1.0]
    

    #assigning parameters to message JointTrajectoryPoint
    point.positions = position
    point.velocities = velocity_joints
    point.time_from_start = Duration(sec=0,nanosec=500000000)

    #assigning parameters to message JointTrajectory
    joint.points.append(point)
    joint.joint_names = name_joints
    
    #assigning parameters to message Float64MultiArray
    wheels.data = velocity_wheels
        
    pub1.publish(joint)
    pub2.publish(wheels)

#===================== main function =====================
def main():
    global pub1
    global pub2

    #init ros2
    rclpy.init()

    #create a node
    node = rclpy.create_node("nInit_robot")

    #create a publisher
    pub1 = node.create_publisher(JointTrajectory,"/fiar_controller/joint_trajectory",10)
    pub2 = node.create_publisher(Float64MultiArray,"/fiar_wheel_controller/commands",10)


    #create a timer
    #time_max = node.create_timer(2.0,set_to_max)
    #time_min = node.create_timer(2.0,set_to_min)
    #time_half = node.create_timer(2.0,set_to_half)
    time_min = node.create_timer(2.0,set_to_cero)

    

    #keep alive the node
    rclpy.spin(node)

    #shutdown
    rclpy.shutdown()
    node.destroy_node()

if __name__ == "__main__":
    main()
