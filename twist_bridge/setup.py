from setuptools import find_packages, setup

package_name = 'twist_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AshimThapa',
    maintainer_email='yammagar1239@gmail.com',
    description='TODO: Bridge from Twist to TwistStamped',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twist_to_twiststamped = twist_bridge.twist_to_twiststamped:main',
        ],
    },
)
