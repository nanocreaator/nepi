
#How To Extend NEPI

###Clone the code
In order to be able to work on the NEPI code, you will have to follow the steps described below :

<pre><code class="python">git clone http://git.onelab.eu/nepi.git
</code></pre>

###Structure of the Code
The direcotry of nepi is structured as followed :

- **Doc**: The documentation of NEPI, including the user manual.
- **Test**: The tests of the code
- **Examples**: The public examples that were used or will be used
- **Src**: The source code

Inside these directories, the same structure is used to separate the different files :
- **Design**: Contains the code of the graphical part ( not implemented yet )
- **Execution**: Contains the core of NEPI. This part should not be touched when adding a new testbed to NEPI
- **Util**: Contains some classes and methods used in different part of the code, that is not related to a specific platform. We can find, in this folder, all the methods enabling ssh call or SFA call. All the classes and methods from this directory can be used in several RMs
- **Resources**: This last directory gather all the RM that can be used depending on the platform they are running or the technology they use. To add a new testbed, you will have to create a new directory inside this directory only if your testbed and/or the technology used to control your testbed is not already created.

##Process to extend
In the previous section, the structure of the folders was explained. This new section describes the minimum amount of code you will have to write to use your testbed using NEPI.

**It is important to remember that the EC should never be modified to fit the specifity of a particular testbed.**

###The RMs
To enable NEPI to use your testbed, you will have to create some RMs. The creation of RM is in two phases :

- The design, where, depending on the characteristics of your testbed, you think about the number of RMs you will need and how they will be connected.
- The conception, where you implement the minimum amount of method for each RMs

#####**Design/Connections**
This part is the main important, because it will define the number of RMs you need to configure and control your testbed . As you should now, an RM is an abstraction of a resource, and a resource can be anything ( a node, an application, a wireless interface, an openVSwitch, ... )

There is no perfect method to know which element of your testbed need to be described with an RM. First, imagine what is configurable in your testbed and associate one RM for each of them. Then, in order to keep the minimum number of RM ( in order to avoid useless RM ), check what will be the connection between the RM. Usually, an RM is necessary when the relation with an other RM is " 1 - N ". For example, many applications can run on one node, many wireless interface can be configure on one node, many openVswitchs can be launched on the same node.

#####**Implementation**
After identifying the number of RM and the role of each of them, you can start to implement them. Under doc/template/ the file template_rm.py contains all the basic method you have to fill in order to create your RM.

During an experiment, each RM passes through different states and some actions can be proceed during each one of these steps. However, 4 actions are mandatory to implement (but can be just passed if nothing need to be done) :

- **Deploy**: The deploy contains the discover and provision, usually used for the reservation and the provisionning of the resource. At the end of this method, the RM is in state READY, that means the resource is accessible
- **Start**: To start the resources ( in some cases, it does not mean anything )
- **Stop**: To stop the resources ( in some cases, it does not mean anything )
- **Release**: The release is use to clean everything before the end of the experiment. For example, delete some folders, unsubscribe from a reservation, disconnect from a server, ...

###The APIs
Each RM need to communicate with its testbed and use consequently a specific API.

#####**Structure**
In NEPI, the communication between an RM and its resource is done through an API. Different API already exist as SSH or XMPP, but new one can be added easily. There are two element that composed the API :

- **The Client**: It knows how to communicate and has all the required method to send the messages
- **The Factory**: It contains all the different client, and save them depending on the credentials used to create them.

A same client can be used by different RMs.

#####**Implementation**
Regarding the implementation, you will have to implement these two elements :

- **The client**: You can use any library that already exists and improve it to fit your requirement. For example, for XMPP, sleekXmpp has been used and modified to be used in the context of OMF
- **The Factory**: You can fin a template ( template_api.py ) for the API under doc/template in the NEPI Repository. with the 4 basics methods that composed it :
  - Get\_api : Retrieve the API depending on the parameters
  - Create\_api : Create the API with the parameters
  - Release\_api : Release the API when no more RM use it ( the counter is at 0 )
  - Make_key : Hash the parameters to create an unique key that identify the instance of the API. This one doesn't need to be modified.
