#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    # Launch arguments:
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true',description='Use simulation (Gazebo) clock')
    use_sim_time = LaunchConfiguration('use_sim_time')
    launch_gui_arg = DeclareLaunchArgument('launch_gui', default_value='true',description='Launch the lerobotArm GUI interface')
    launch_gui = LaunchConfiguration('launch_gui')
    gui_delay_arg = DeclareLaunchArgument('gui_delay', default_value='8.0',description='Delay before launching GUI (seconds)')

    # Find your packages:
    fiar_pkg   = FindPackageShare("fiar_pkg")
  

    # Launch files:
    gazebo_launch     = PathJoinSubstitution([fiar_pkg,"launch", "gz_launch.launch.py"])
    spawn_controllers   = PathJoinSubstitution([fiar_pkg, "launch", "position_launcher_gz.launch.py"])

    return LaunchDescription([
        use_sim_time_arg,
        launch_gui_arg,
        gui_delay_arg,

        # 1. Start Gazebo:
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch),
            launch_arguments={'use_sim_time': use_sim_time}.items()
        ),

        # # 2. Publish URDF:
        # TimerAction(
        #     period=1.0,
        #     actions=[ IncludeLaunchDescription(
        #         PythonLaunchDescriptionSource(gazebo_launch),
        #         launch_arguments={
        #             'use_sim_time': use_sim_time,
        #             'launch_state_publisher': 'true',
        #             'joint_states_topic': '/joint_states'
        #         }.items()
        #     ) ]
        # ),
        
   
        # 4. Spawn the robot in Gazebo:
        # TimerAction(
        #     period=2.0,
        #     actions=[ IncludeLaunchDescription(
        #         PythonLaunchDescriptionSource(gazebo_launch),
        #         launch_arguments={'use_sim_time': use_sim_time}.items()
        #     ) ]
        # ),  

        # #6. Spawn gazebo and ROS2 bridge:
        # TimerAction(
        #     period = 8.0,
        #     actions=[ IncludeLaunchDescription(
        #         PythonLaunchDescriptionSource(gazebo_launch),
        #         launch_arguments={'use_sim_time': use_sim_time}.items()
        #     )]
        # ),

        # 7. Spawn controllers automatically:
        TimerAction(
            period = 6.0,
            actions=[ IncludeLaunchDescription(
                PythonLaunchDescriptionSource(spawn_controllers),
                launch_arguments={'use_sim_time': use_sim_time}.items()
            )]
        )
    ])