# @Work Sllidar ROS2 Fork Package

ROS2 node for SLAMTEC LIDAR

Visit following Website for more details about SLAMTEC LIDAR:

SLAMTEC LIDAR roswiki: <http://wiki.ros.org/rplidar>

SLAMTEC LIDAR HomePage: <http://www.slamtec.com/en/Lidar>

SLAMTEC LIDAR SDK: <https://github.com/Slamtec/rplidar_sdk>

SLAMTEC LIDAR Tutorial: <https://github.com/robopeak/rplidar_ros/wiki>

## Supported SLAMTEC LIDAR

| Lidar Model |
| ---------------------- |
|RPLIDAR A1              |
|RPLIDAR A2              |
|RPLIDAR A3              |
|RPLIDAR C1              |
|RPLIDAR S1              |
|RPLIDAR S2              |
|RPLIDAR S3              |
|RPLIDAR S2E             |
|RPLIDAR T1              |

## Use sllidar_ros2 package

   sllidar_ros2 running requires the read and write permissions of the serial device.
   You can manually modify it with the following command:

   ```bash
   sudo chmod 777 /dev/ttyUSB0
   ```

   But a better way is to create a udev rule:

   ```bash
   cd src/rpldiar_ros/
   source scripts/create_udev_rules.sh
   ```

## Work Specific Launches

### `double_a1.launch.py`

This launch is used to run two A1M8 LIDAR sensors simultaneously.

What it does:
* Starts two independent nodes of the sllidar_node.
* Automatically remaps topics to avoid conflicts: Lidar 01 publishes to /front_scan and Lidar 02 to /back_scan.
* Allows configuring distinct serial ports and frame_ids for each sensor.
* Optionally opens RViz for visualization.

```bash
ros2 launch sllidar_ros2 double_a1.launch.py ​​serial_port_01:=/dev/ttyUSB0 serial_port_02:=/dev/ttyUSB1
```

### `single_a1.launch.py`

This launch is used to operate a single A1M8 LIDAR with an integrated filter chain.

What it does:
* Starts a sllidar_node mapped to the topic `/front_scan`.
* Starts a laser_filters node.
* Filtering: It receives the data from `/front_scan`, applies the filters defined in `config/laser_filter.yaml` and publishes the clean result to the default topic `/scan`.

```bash
ros2 launch sllidar_ros2 single_a1.launch.py ​​serial_port_01:=/dev/ttyUSB0
```

**NOTE:** When using two lidars simultaneously when laser_scan_merger is applied, the reference frame of the result becomes the base_link. When using only one lidar, a filter is applied to use only a specific portion of the lidar, but the reference frame becomes the lidar link. Using a single lidar with SlamToolBox creates a map only in front of the lidar.


## Run sllidar_ros2

### Run sllidar node and view in the rviz

The command for RPLIDAR A1 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_a1_launch.py
```

The command for RPLIDAR A2M7 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_a2m7_launch.py
```

The command for RPLIDAR A2M8 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_a2m8_launch.py
```

The command for RPLIDAR A2M12 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_a2m12_launch.py
```

The command for RPLIDAR A3 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_a3_launch.py
```

The command for RPLIDAR C1 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_c1_launch.py
```

The command for RPLIDAR S1 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_s1_launch.py
```

The command for RPLIDAR S2 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_s2_launch.py
```

```bash
ros2 launch sllidar_ros2 view_sllidar_s2e_launch.py
```

The command for RPLIDAR S3 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_s3_launch.py
```


The command for RPLIDAR T1 is :

```bash
ros2 launch sllidar_ros2 view_sllidar_t1_launch.py
```

The command for RPLIDAR S1(TCP connection) is :

```bash
ros2 launch sllidar_ros2 view_sllidar_s1_tcp_launch.py
```

Notice: different lidar use different serial_baudrate.

## RPLIDAR frame

RPLIDAR frame must be broadcasted according to picture shown in rplidar-frame.png
