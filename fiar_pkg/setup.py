from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'fiar_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share',package_name, 'urdf'), glob(os.path.join('urdf','*.urdf.xacro'))),
        (os.path.join('share',package_name, 'launch'), glob(os.path.join('launch','*launch.[pxy][yma]*'))),
        (os.path.join('share',package_name, 'rviz2'), glob(os.path.join('rviz2','*.rviz'))),
        ('share/fiar_pkg/config', [
        'config/bridge_config.yaml'
        ]),
        ('share/fiar_pkg/worlds', [
        'worlds/world.sdf'
        ]),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danirob',   
    maintainer_email='daniel6968.felipe@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
