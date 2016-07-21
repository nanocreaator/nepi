
#W-ilab.t Robot Dancing
In a room of 200 square meters with some mobile robots ( based on roomba ), this use case aims at moving the robots in a synchronized way in order to perform a choregraphy. In the context of the FP7 european project Openlab, a demo has been recorded for this use case.

###Experiment Description
In a room of 200 square meter with some mobile robots ( based on roomba ), this use case aims at moving the robots in a synchronized way in order to perform a choregraphy.

Each mobile robot is listening to a port series and is waiting for information about localisation or eyes control ( each robot has two eyes, that can be open or close ). These informations come from an other machine running an OMF 5.4 RC. To control the eyes of the robot, we used a special type of message of the OMF 5.4 protocol "STDIN" that allow to run an application , waiting for input, on the remote machine. By sending, close or open, we were able to control during run time the eyes of the robot.

This experiment is in 2 steps :

- The first step is to describe the movement of each robot and save all the coordinates into a file. The description is done through a web interface provided by iMinds
- The second steps, done by NEPI, is to load this file into the remote machine and to send messages to the OMF 5.4 RC.

![picformat](http://nepi.inria.fr/pub/UseCases/RobotDancing/robot_dashboard.png)

[More information about how to use the robots in the W-ilab.t testbed](http://ilabt.iminds.be/wilabt/use/mobilitytoolkit).

###Role of NEPI
In this experiment, NEPI was used for :

- Orchestrate the whole experiment by sending message at the right time.
- Upload the coordinate file automatically after generation
- Retrieve some results during run time as the localisation of the robot

###Scripts
[Script to load the coordinate file, open the eyes and run the whole experiment](http://nepi.inria.fr/pub/UseCases/RobotDancing/nepi_omf5_iminds_stdin.py.txt)

###Results
[As a results, you can find the recorded demo of this use case](http://nepi.inria.fr/data/nepi/Robot.avi).

###Conclusion
To conclude, this use case is a success. NEPI alleviates the different issues that can happened and help the user to control the whole experiment. Some issues happened in the move of the robot. Indeed, sometimes the robots lose their position and get lost ( some error in the calibration appears ). This could happen because there are too long straight line in the description of the robot's way, or because the robot is passing really close to obstacle.

###Authors
- Julien Tribino
- Vincent Sercu
- Pieter Becue
