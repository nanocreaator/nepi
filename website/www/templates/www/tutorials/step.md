
#Introduction to NEPI: A Step by Step Tutorial

###Requirements
For this tutorial you will need a computer with Linux or Mac.

###Installing the IPython Console
The IPython console can be used as an interactive interpreter to execute Python instructions. We can take advantage of this feature, to interactively run NEPI experiments. We will use the IPython console in this tutorial. You can easily install IPython on Debian, Ubuntu, Fedora or Mac as follows:

#####**Debian/Ubuntu**
<pre><code class="bash">$ sudo apt-get install ipython</code></pre>

#####**Fedora**
<pre><code class="bash">$ sudo yum install ipython</code></pre>

#####**Mac**
<pre><code class="bash">$ pip install ipython</code></pre>

Make sure to add Python and IPython source folder path to the PYTHONPATH environment variable

<pre><code class="bash">$ export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python:/usr/local/share/python/ipython</code></pre>

If an "pkg_resources.DistributionNotFound" error occurs you will also need to install gnureadline as follows:

<pre><code class="bash">$ sudo easy_install gnureadline</code></pre>

###Starting the IPython Console
If NEPI is not installed in the system, you will need to add NEPI's path to the PYTHONPATH environment variable.

<pre><code class="bash">$ export PYTHONPATH=$PYTHONPATH:"path-to-nepi-directory"/src</code></pre>

Then you can start IPython as follows:

<pre><code class="python">$ ipython

Python 2.7.3 (default, Jan  2 2013, 13:56:14)
Type "copyright", "credits" or "license" for more information.
IPython 0.13.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
</code></pre>

###The NEPI ExperimentController
The first thing we need to do in order to design a NEPI experiment is to import the NEPI Python library. In particular we need to import the ExperimentController class. To do this type the following in the Python console:
<pre><code class="python">from nepi.execution.ec import ExperimentController
</code></pre>

After importing the ExperimentController class, we need to instantiate a new ExperimentController (EC) to hold the description of the experiment. The **exp-id** argument is the name you want to give to the experiment.

<pre><code class="python">ec = ExperimentController(exp_id="exp-id")
</code></pre>

###Designing an Experiment
In order to design our experiment, we need to tell the EC which resources are going to be involved and how they will interact. Resources can be added to the EC using the register_resource invokation, and they can be associated to other resources with the register_connection invokation.

We can start by defining a very simple experiment which consists on sending ICMP requests to a remote host from the local computer, using the Ping command. For this, we use two different NEPI resource abstractions, the linux::Node and the linux::Application. Adding these resources to the EC is very easy, just go ahead and copy & paste the instructions below in the IPython console:

<pre><code class="python">node = ec.register_resource("linux::Node")
ec.set(node, "hostname", "localhost")

app = ec.register_resource("linux::Application")
ec.set(app, "command", "ping -c 3 nepi.inria.fr")
ec.register_connection(app, node)
</code></pre>

Note that the application was "connected" to the node. This is equivalent to instructing the EC to "run the application in the node". Note as well that the application and node are configured in the same way by setting attributes. On the node we configured the "hostname" to be "localhost", in the application we set the "command" to ping the nepi.inria.fr host.

So far we have describe the experiment, so let's go ahead and tell NEPI to execute it.

###Deploying an Experiment
Deploying an experiment is very easy, in fact the ExperimentController (EC) will do everything for you. You just need to gently tell it to the EC:

<pre><code class="python">ec.deploy()
</code></pre>

After some seconds, you should see output messages from NEPI informing about the progress in the experiment deployment.

<pre><code class="python">In [9]: 2014-07-03 12:21:07,638 linux::Node INFO  guid 1 - host localhost - Deploying node
2014-07-03 12:21:08,641 linux::Application INFO  guid 2 - host localhost - Deploying command 'ping -c 3 nepi.inria.fr'  
2014-07-03 12:21:08,664 linux::Application INFO  guid 2 - host localhost - Uploading command 'ping -c 3 nepi.inria.fr'
2014-07-03 12:21:08,702 linux::Application INFO  guid 2 - host localhost - Provisioning finished
2014-07-03 12:21:09,637 linux::Application INFO  guid 2 - host localhost - Starting command 'ping -c 3 nepi.inria.fr'
</code></pre>

###Monitoring the State of Resources
So far, so good. But now we might what to know what is going on with the experiment . For this NEPI provides the "state" primitive, which can be used to query the state of resources.

<pre><code class="python">ec.state(node, hr=True)
</code></pre>

The "hr" argument stands for human readable and provides state information as a string instead of as a numeric code.

<pre><code class="python">In [9]: ec.state(app, hr=True)
'STARTED'

In [10]: ec.state(node, hr=True)
'STARTED'
</code></pre>

It is worth noticing that even if all resources in NEPI share a same life cycle and thus go through the same state changes (i.e. NEW, DISCOVERED, PROVISIONED, READY, STARTED, STOPPED and RELEASED), a same state might have a differente meaning depending on the type of the resource. In the example above, we see that the application is STARTED which means that it is 'running'. When the application finished running its state will pass to STOPPED. For a node, however, the state STARTED means the same thing as the state READY, this is that the node can be accessed by the user and is currently taking part in the experiment.

###Retrieving Experiment Results
One useful feature of NEPI is that it allows to retrieve results while the experiment is running. NEPI uses the concept of "traces", which are measurement points exposed by resources. Traces are associated to a name identifier (a type), different resource types will provide different traces. For instance, a linux::Application will natively provide "stdout" and a "stderr" traces, associated to the standard output and standard error pipes of the application Linux process. Traces can be retrieved using the "trace", after a resource has STARTED and before it is RELEASED.

<pre><code class="python">ec.trace(app, "stdout")
</code></pre>

In the experiment we previously ran, the "stdout" trace of the linux::Application will retrieve the output of the ping command.

<pre><code class="python">In [11]: ec.trace(app, "stdout")
2014-07-03 12:52:59,651 LinuxApplication INFO  guid 2 - host localhost - Retrieving 'stdout' trace all  
'PING nepi.pl.sophia.inria.fr (138.96.116.79) 56(84) bytes of data.\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_seq=1 ttl=63 time=3.38 ms\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_seq=2 ttl=63 time=1.99 ms\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_seq=3 ttl=63 time=2.77 ms\n\n--- nepi.pl.sophia.inria.fr ping statistics ---\n3 packets transmitted, 3 received, 0% packet loss, time 2002ms\nrtt min/avg/max/mdev = 1.993/2.718/3.384/0.572 ms\n'
</code></pre>

###Incremental Experiment Deployment
Another interesting feature of NEPI is that we can continue to register and deploy resources after the first invokation to "deploy". This means that we can incrementally describe and deploy our experiment as we go, which is very useful when we are first conceiving a new experiment. The incremental deployment allows us to test small parts of an experiment behavior, making it easier to detect when something goes wrong and debug it.

To specify a specific group of resources to be deployed at one time, the deploy invokation can receive a list of Global Unique Identifiers (guids). The value returned by the register_resource invokation is in fact the "guid" of the resource just registered.

<pre><code class="python">app2 = ec.register_resource("linux::Application")
ec.set(app2, "command", "ping -c 3 nepi.inria.fr")
ec.register_connection(app2, node)

ec.deploy(guids=[app2])
</code></pre>

###Using a Remote Linux Host
The linux::Node resource has other attributes apart from the "hostname" that can be configured to use a remote host intead of the local host. In this case, a SSH account on the remote host is required. To login into a host using SSH we need three parameters: the hostname, the username and optionally the identity (which is the absolute path to the ssh private key) if the private key is not the default id_rsa key. With this three parameters we would log in as follow:

<pre><code class="python">$ ssh -i identity username@hostname
</code></pre>

The linux::Node should be configured with the same three paremeters to describe a remote host.

<pre><code class="python">node = ec.register_resource("linux::Node")
ec.set(node, "hostname", hostname)
ec.set(node, "username", username)
ec.set(node, "identity", identity)
ec.set(node, "cleanHome", True)
ec.set(node, "cleanProcesses", True)
</code></pre>

Additional attributes such as "cleanHome" and "cleanProcesses" can be used to ensure that the node is clean before starting the experiment and thus experiment results will not be compromised.

###Putting Everything Together
Lets now try to deploy an application on a remote host. For simplicity, we will first define two Python functions, one to add a node to the EC and another to add an application. Copy & paste the code below into your IPython console:

<pre><code class="python">def add_node(ec, hostname, username, identity):
    node = ec.register_resource("linux::Node")
    ec.set(node, "hostname", hostname)
    ec.set(node, "username", username)
    ec.set(node, "identity", identity)
    ec.set(node, "cleanHome", True)
    ec.set(node, "cleanProcesses", True)
    return node

def add_app(ec, command, node):
    app = ec.register_resource("linux::Application")
    ec.set(app, "command", command)
    ec.register_connection(app, node)
    return app
</code></pre>    

Note: You can paste many lines at once in IPython if you type "%cpaste" and finish the paste block with "--"

In the IPython console now define some variables with the hostname, username and identity.

<pre><code class="python">hostname = "<remote-hostname>"
username = "<your-username>"
identity = "<absolute-path-to-ssh-key>"
</code></pre>

And now, we can describe the remote ping experiment in few lines:

<pre><code class="python">rnode = add_node(ec, hostname, username, identity)
rapp = add_app(ec,"ping -c5 'nepi.inria.fr'", rnode)
ec.deploy()
</code></pre>

What we just did is to register a remote node and an application that will ping ww.google.com 5 times. We should again see information messages about the deployment status of this application being output to the console. We can also query the state of the application and retrieve the ping result..

<pre><code class="python">In [12]: ec.state(rapp, hr=True)
'STOPPED'

In [13]: ec.trace(rapp, "stdout")
2014-07-03 19:35:31,884 linux::Application INFO  guid 2 - host aguila1.lsi.upc.edu - Retrieving 'stdout' trace all  
'PING nepi.pl.sophia.inria.fr (138.96.116.79) 56(84) bytes of data.\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_req=2 ttl=51 time=41.4 ms\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_req=3 ttl=51 time=41.3 ms\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_req=4 ttl=51 time=41.7 ms\n64 bytes from nepi.pl.sophia.inria.fr (138.96.116.79): icmp_req=5 ttl=51 time=41.3 ms\n\n--- nepi.pl.sophia.inria.fr ping statistics ---\n5 packets transmitted, 4 received, 20% packet loss, time 4005ms\nrtt min/avg/max/mdev = 41.300/41.438/41.725/0.302 ms\n'
</code></pre>

###Behind the Scenes
When you use NEPI, most things happen in your machine, this machine is called the "controller". NEPI is a user-side application which is able to interpret instructions given by the experimenter and connect to a set of remote machines to deploy the experiment. However, in order to keep track of results and monitor running applications, NEPI will create and maintain an experiment directory structure in the remote (or local) hosts, when the linux::Node and the linux::Application resource abstractions are used.

If you now open another terminal and login to the host you used on the previous experiment (as indicated below), you will see a directory named "~/.nepi".

<pre><code class="python">$ ssh -i identity username@hostname
$ ls -a
.  ..  .nepi
</code></pre>

In the ~/.nepi directory you will find other two directories: nepi-usr and nepi-exp. The first one is used by NEPI to store files that might be re used in future experiments (e.g. source code, input files) . The second directory nepi-exp, is where experiment specific files (e.g. results, deployment scripts) are stored.

Inside the nepi-exp directory, you will find a directory with the exp-id you assigned to your EC, and inside that directory you should see a directory named node-1 which will contain the files (e.g. result traces) associated to the linux::Node resource. In fact for every resource deployed associated to this host (e.g. each linux::Application), NEPI will create a sub-directory to place specific result files. The name of the directory identifies the type of resources (e.g. 'node', 'app', etc) and it is followed by the global unique identifier (guid).

Each time you run a same experiment, NEPI will add a new sub directory to the resource directory. This sub directory is named with the "run-id" of the EC, this is the creation timestamp of the EC. If you take a look at the "run-id" directoroty of the ping application resource, you will find a file with the ping "stdout".

<pre><code class="python">cat .nepi/nepi-exp/'exp-id'/app-2/'run-id'/stdout
</code></pre>

###Registering Conditions to Define Workflows
Now that you have been introduced to the basics of NEPI, we can register two more applications and define a workflow between them. A workflow is used to define the order od . where one application will start after the other one has finished executing. For this we will use the EC register_condition method described below:

<pre><code class="python">register_condition(self, guids1, action, guids2, state, time=None):
    Registers an action START, STOP or DEPLOY for all RM on list
    guids1 to occur at time 'time' after all elements in list guids2
    have reached state 'state'.
</code></pre>  

To use the register_condition method we will need to import the ResourceState and the ResourceAction classes

<pre><code class="python">from nepi.execution.resource import ResourceState, ResourceAction
</code></pre>  

Then we will register the two applications. The first application will wait for 5 seconds and the create a file in the host called "greetings" with the content "HELLO WORLD". The second application will read the content of the file and output it to standard output. If the file doesn't exist il will instead output the string "FAILED".

<pre><code class="python">app1 = add_app(ec, "sleep 5; echo 'HELLO WORLD!' > ~/greetings", node)
app2 = add_app(ec, "cat ~/greetings || echo 'FAILED'", node)
</code></pre>

In order to guarantee that the second application is successful, we need to make sure that the first application is executed first. For this we register a condition:

<pre><code class="python">ec.register_condition(app2, ResourceAction.START, app1, ResourceState.STOPPED)
</code></pre>

We then deploy the two application:

<pre><code class="python">ec.deploy(guids=[app1,app2])
</code></pre>
And finally, we retrieve the standard output of the second application which should return the string "HELLO WORLD!".

<pre><code class="python">ec.trace(app2, "stdout")
</code></pre>
