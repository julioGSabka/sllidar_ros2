#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    #Lidar 01
    serial_port_01 = LaunchConfiguration('serial_port_01', default='/dev/ttyUSB0')
    serial_baudrate_01 = LaunchConfiguration('serial_baudrate_01', default='115200')
    frame_id_01 = LaunchConfiguration('frame_id_01', default='laser01')


    #Lidar 02
    serial_port_02 = LaunchConfiguration('serial_port_02', default='/dev/ttyUSB1')
    serial_baudrate_02 = LaunchConfiguration('serial_baudrate_02', default='115200')
    frame_id_02 = LaunchConfiguration('frame_id_02', default='laser02')

    channel_type =  LaunchConfiguration('channel_type', default='serial')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Sensitivity')

    rviz_config_dir = os.path.join(
            get_package_share_directory('sllidar_ros2'),
            'rviz',
            'sllidar_ros2.rviz')
    
    use_rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Launch RViz'
    )

    channel_type_arg = DeclareLaunchArgument(
            'channel_type',
            default_value=channel_type,
            description='Specifying channel type of lidar')
    
    serial_port_01_arg = DeclareLaunchArgument(
            'serial_port_01',
            default_value=serial_port_01,
            description='Specifying usb port to connected lidar 01')
    serial_baudrate_01_arg = DeclareLaunchArgument(
            'serial_baudrate_01',
            default_value=serial_baudrate_01,
            description='Specifying usb port baudrate to connected lidar 01')
    frame_id_01_arg = DeclareLaunchArgument(
            'frame_id_01',
            default_value=frame_id_01,
            description='Specifying frame_id of lidar 01')
    
    serial_port_02_arg = DeclareLaunchArgument(
            'serial_port_02',
            default_value=serial_port_02,
            description='Specifying usb port to connected lidar 02')
    serial_baudrate_02_arg = DeclareLaunchArgument(
            'serial_baudrate_02',
            default_value=serial_baudrate_02,
            description='Specifying usb port baudrate to connected lidar 02')
    frame_id_02_arg = DeclareLaunchArgument(
            'frame_id_02',
            default_value=frame_id_02,
            description='Specifying frame_id of lidar 02')
    
    inverted_arg = DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data')

    angle_compensate_arg = DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data')

    scan_mode_arg = DeclareLaunchArgument(
            'scan_mode',
            default_value=scan_mode,
            description='Specifying scan mode of lidar')
    
    sllidar_node_01 = Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node_01',
            parameters=[{'channel_type':channel_type,
                         'serial_port': serial_port_01, 
                         'serial_baudrate': serial_baudrate_01, 
                         'frame_id': frame_id_01,
                         'inverted': inverted, 
                         'angle_compensate': angle_compensate, 
                         'scan_mode': scan_mode}],
            remappings=[
                ('scan', 'scan_01')
            ],
            output='screen')
    
    sllidar_node_02 = Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node_02',
            parameters=[{'channel_type':channel_type,
                         'serial_port': serial_port_02, 
                         'serial_baudrate': serial_baudrate_02, 
                         'frame_id': frame_id_02,
                         'inverted': inverted, 
                         'angle_compensate': angle_compensate, 
                         'scan_mode': scan_mode}],
            remappings=[
                ('scan', 'scan_02')
            ],
            output='screen')
    
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_dir],
        condition=IfCondition(LaunchConfiguration('rviz'))
    )
    

    return LaunchDescription([

        use_rviz_arg,
        channel_type_arg,
        serial_port_01_arg,
        serial_baudrate_01_arg,
        frame_id_01_arg,
        serial_port_02_arg,
        serial_baudrate_02_arg,
        frame_id_02_arg,
        inverted_arg,
        angle_compensate_arg,
        scan_mode_arg,

        sllidar_node_01,
        sllidar_node_02,

        rviz
    ])

