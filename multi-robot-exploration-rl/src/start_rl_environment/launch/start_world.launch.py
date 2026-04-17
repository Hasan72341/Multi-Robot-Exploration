import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PythonExpression, LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    
    map_name = PythonExpression(["'map", LaunchConfiguration('map_number'), ".world'"])

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                launch_arguments={
                    'world': LaunchConfiguration('world'),
                    'gui': LaunchConfiguration('gui'),
                    'verbose': 'true',
                }.items(),
    )    

    return LaunchDescription([
        # Keep Gazebo GUI stable on mixed desktop setups (Wayland/X11, weak GL drivers).
        SetEnvironmentVariable('QT_QPA_PLATFORM', 'xcb'),
        SetEnvironmentVariable('LIBGL_ALWAYS_SOFTWARE', '1'),
        SetEnvironmentVariable('MESA_GL_VERSION_OVERRIDE', '3.3'),
        # Avoid startup stalls when remote model DB is unreachable.
        SetEnvironmentVariable('GAZEBO_MODEL_DATABASE_URI', ''),
        DeclareLaunchArgument(
            'map_number',
            default_value='1',
            description='Number of the map to be launched'),
        DeclareLaunchArgument(
            'gui',
            default_value='false',
            description='Start Gazebo client GUI if true'),
        DeclareLaunchArgument(
            'world',
            default_value=PathJoinSubstitution([
                get_package_share_directory('start_rl_environment'), 'worlds', map_name]),
            description='SDF world file'),
        gazebo
    ])