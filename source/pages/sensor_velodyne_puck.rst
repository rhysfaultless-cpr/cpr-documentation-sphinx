Velodyne Puck
=============

.. image:: ../images/sensor_velodyne_puck_1.jpg
   :width: 400
   :align: center


Safety
------

..  caution::

    ======================== ==================== ====================================================================================================================
    |safety_laser_radiation| Laser Radiation Risk This sensor is a Class 1 laser product. 
                                                  Class 1 lasers provide no hazard during normal use, however it is not recommended to stare directly into the beam(s)
    ======================== ==================== ====================================================================================================================
        
.. |safety_laser_radiation| image:: ../images/safety_laser_radiation.png
   :align: middle
   :width: 40


|

Item Numbers
------------

.. list-table::
   :widths: 80 40 60
   :header-rows: 1
   
   * - Description
     - CPR item
     - Manufacturer item

   * - Velodyne Puck sensor
     - 011703
     - 80-VLP-16

   * - Velodyne Puck sensor, with M12 connector
     - 020972
     - 80-VLP-16 M12-0.3M-A

   * - Velodyne Puck sensor, PACS kit
     - 027206
     - 


|

Specifications
--------------

Overview
^^^^^^^^

.. list-table::
   :widths: 100 100
   :header-rows: 1
   
   * - Description
     - Value

   * - Mass
     - 830 g

   * - Voltage, Minimum
     - 9 V

   * - Voltage, Maximum
     - 18 V

   * - Voltage, Sensor
     - 12 V

   * - Power, Average
     - 8 W

   * - Data
     - Ethernet, 100 Mbit/s

   * - Range, Minimum
     - 

   * - Range, Maximum
     - 100 m

   * - Range, Accuracy
     - ±3 cm

   * - View, Horizontal
     - 360°

   * - View, Vertical
     - ±15°

   * - Resolution, Horizontal
     - 0.4°

   * - Resolution, Vertical
     - 2°


|

IP addresses
^^^^^^^^^^^^

.. list-table::
   :widths: 100 100
   :header-rows: 1
   
   * - Description
     - IP address

   * - Primary / Front
     - 192.168.131.20

   * - Secondary / Rear
     - 192.168.131.21

   * - Additional LiDAR
     - 192.168.131.22  -  29

   * - Default from Manufacturer
     - 192.168.1.201


|

Pinout
^^^^^^

.. list-table::
   :widths: 100 100 100
   :header-rows: 1
   
   * - Pin
     - Description
     - Wire colour

   * - 1
     - ethernet rx-
     - Blue

   * - 2
     - ethernet rx+
     - Light blue

   * - 3
     - ethernet tx-
     - Orange

   * - 4
     - ethernet tx+
     - Light orange	

   * - 5
     - GPS receive
     - White

   * - 6
     - GPS pulse
     - Yellow

   * - 7
     - +12 V
     - Red

   * - 8
     - Ground
     - Black


|

Hardware Build
--------------

Parts List
^^^^^^^^^^

The PACS kit for this sensor includes:

.. list-table::
   :widths: 1 8 2 2
   :header-rows: 1
   
   * - ID
     - Description
     - CPR item
     - Quantity

   * - 1
     - Plate—80 X 80, Attachment Interface
     - :download:`026914 <../assets/clearpath_robotics_026914.pdf>`
     - 1

   * - 2
     - Sensor, 3D LiDAR—Velodyne Puck, M12 connector
     - 020972
     - 1

   * - 3
     - Cable—Velodyne, Bulkhead, M12
     - 021194
     - 1

   * - 4 
     - Cable—M12 8-position Female 90°, M12 8-position Male, 500
     - 026861
     - 1

   * - 5
     - Screw, Cap, Hex Head—#0.25-20 UNC X 9.5, Stainless Steel
     - 019974
     - 1

   * - 6
     - Spacer, Round—Ø5.3 X Ø8 X 7, Aluminum Alloy
     - 026612
     - 4

   * - 7
     - Screw, Cap, Round Head—M5×0.8 X 16, Stainless Steel
     - 023257
     - 4

..


|

Instructions
^^^^^^^^^^^^

#.  Mount the sensor (ID 2) to the attachment-plate (ID 1) using a #1/4-20 screw (ID 5).
    Use the centre hole in the attachment-plate for mounting the sensor.

    .. image:: ../images/027206_isometric_1.png
      :width: 300
      :align: left

    .. image:: ../images/026914_drawing.png
      :width: 300
      :align: right

#.  Mount this assembly onto your robot, using the included spacers (ID 6) and screws (ID 7).

    .. image:: ../images/027206_isometric_2.png
      :width: 300
      :align: center

#.  Connect the wye-cable (ID 3) to a robot's User Power connector, and to an Ethernet port. 
    You can optionally mount this cables M12 connetor to a cutout on the robot.
#.  Make sure the robot is off.
    Connect the sensor's cable to the wye-cable from the last step. 
    You may add the extension cable (ID 4) between the sensor and wye-cable.
#.  There is white painted lettering on the robot's top plate.
    This lettering designates sensor locations on the robot.
    Take note of the location that you have mounted this sensor.
    You will need this sensor location during software installation, to make sure your robot's URDF is confured correctly.
    

|

Software Bringup
----------------

.. include:: components/pacs_sensor_software_supported.rst


|

Troubleshooting
---------------

==============================================  =======================================================================================================================
Issue                                           Troubleshooting steps
==============================================  =======================================================================================================================
Sensor is not turning on                        
                                                #. Turn the robot off
                                                #. Check that connectors are fully seated 
                                                #. Turn on the robot and see if the sensor is turning on
                                                #. If it does not turn on, unplug the rectangular power connector
                                                #. With a multimeter, measure the voltage across positions 2 and 6 on the robot's connector
                                                #. If the measurement is 12 V, then there is likely an issue with the sensor, and you should contact Clearpath Robotics
                                                #. If the measurement is 0 V, then the 12 V fuse on your robot has likely failed. 
                                                   Shut off the robot, replace the fuse, and then replace the sensor's rectangular connector.
Cannot ping the sensor on the robot's computer  
                                                #. Turn the robot on
                                                #. Connect your laptop to a spare RJ45 Ethernet port on the robot
                                                #. Configure your laptop's Ethernet port to a static address of 192.168.131.250, and a subnet of 255.255.255.0
                                                #. In a new terminal session, enter :code: `ping 192.168.131.20`. 
                                                   This address may be different if you have more sensors on your robot.
                                                #. The sensor if working properly if you revceive Reply messages
                                                #. If you do not get Reply messages, then the issue is likely:

                                                  #. Your Ethernet cable has an issue
                                                  #. Your laptop's Ethernet port is not configured properly
                                                  #. The sensor's IP address is not the same as what you entered into the terminal
                                                  #. The sensor is not on
Sensor's rostopics are not listed               
                                                #. 
Sensors rostopics don't have any data           
                                                #. 
==============================================  =======================================================================================================================

|

If the issue persists
^^^^^^^^^^^^^^^^^^^^^

.. include:: contact_support.rst


|

Further Reading
---------------

#. `Clearpath Robotics Store <https://store.clearpathrobotics.com/collections/3d-lidar/products/puck>`_
#. `Velodyne website <https://velodynelidar.com/products/puck/>`_
#. `ROS webpage <http://wiki.ros.org/velodyne>`_
#. `ROS tutorial <http://wiki.ros.org/velodyne/Tutorials/Getting%20Started%20with%20the%20Velodyne%20VLP16>`_
