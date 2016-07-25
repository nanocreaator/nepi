
#Plotting and serializing experiments tutorial

This tutorial explains how to show graphically the description of a NEPI experiment (plot) and how to persist the experiment to XML format (serialize).

###Plotting
The example experiment description below is composed of one linux::Node and one linux::Application:

<pre><code class="python">from nepi.execution.ec import ExperimentController

ec = ExperimentController(exp_id="my_exp")

node = ec.register_resource("linux::Node")
ec.set(node, "hostname", "localhost")

app = ec.register_resource("linux::Application")
ec.set(app, "command", " ping -c3 nepi.inria.fr")
ec.register_connection(node, app)
</code></pre>

Once the experiment is defined, can use the plot method of the ExperimentController to generate a .PNG file with a graph representation of the experiment description graph:

<pre><code class="python">filename = ec.plot() # plot as .png
print filename
>> /tmp/tmpMJSTPv/my_exp_20140916160354087614.png
</code></pre>

Passing the argument show=True produces a window to pop-up, showing the experiment diagram.

<pre><code class="python">ec.plot(show=True) # show experiment from png plot
</code></pre>

Alternatively, is it possible to generate a .DOT file with the experiment description graph, instead of a .PNG image. This is done by specifing the required format on the plot method.

<pre><code class="python">from nepi.util.plotter import PFormats
filepath = ec.plot(format=PFormats.DOT) # generate .dot plot
print filepath
>> /tmp/tmpP7fhmO/my_exp_20140916160354087614.dot
</code></pre>

To show a .DOT diagram the evince viewer needs to be installed (Linux only).

<pre><code class="python">ec.plot(format = PFormats.DOT, show=True) # show the .dot plot
</code></pre>

###Serializing
Experiments can be serialized to XML and loaded from a previously created XML files, using the save and load methods as shown below:

<pre><code class="python">filename = ec.save() # save to a XML file
print filename
>> /tmp/my_exp/20140916160354087614/my_exp_20140916161613.xml

ec2 = ExperimentController.load(filepath=filename) #copy of ec
</code></pre>
