from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('fiar_pkg')
    rviz_file = os.path.join(pkg_share, 'rviz2', 'rviz.rviz')
    
    xacro_file = PathJoinSubstitution([
        FindPackageShare('fiar_pkg'),
        'urdf',
        'fiarURDF.urdf.xacro'
    ])
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': ParameterValue(
                Command([
                    'xacro ', xacro_file
                ]),
                value_type=str
            )}]
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="screen"
        ),
        Node(
            package='rviz2',
            executable='rviz2', 
            arguments=['-d', rviz_file],
            output='screen'
        )
        
    ])