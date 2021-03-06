
#Automated topology generation tutorial
The NEPI ExperimentController is responsible of executing an experiment defined by the user and collecting the results. Experiments can be described using the design methods of the NEPI API (e.g. register_resource and register_connection primitives), as shown in the example below. Alternatively, experiment descriptions can be automatically generated by the ExperimentController based on an abstract topology given by user.

<pre><code class="python">from nepi.execution.ec import ExperimentController

ec = ExperimentController(exp_id="example")

node = ec.register_resource("linux::Node")
ec.set(node, "hostname", "localhost")

app = ec.register_resource("linux::Application")
ec.set(app, "command", "ping -c 5 nepi.inria.fr")
ec.register_connection(app, node)
</code></pre>

###Abstract topologies and executable experiments
An abstract topology is a high level representation of the "shape" of a network experiment. An executable experiment, on the other hand, is a detailed representation that includes all necessary information to allow instantiation of the experiment (i.e. what concrete resources will be used, how to configure them, etc).

- An **abstract topology** can be thought of an undirected graph where nodes are abstract experiment resources, or groups of resources. These abstract resources can be mapped to different possible concrete NEPI resources, giving place to different possible executable experiments with a same "shape".
- An **executable experiment** description is the representation of an experiment that can be executed by NEPI. Instead of a graph made of abstract nodes, the executable experiment description is a graph where nodes are concrete NEPI resources.

The ExperimentController can generate an executable experiment description from an abstract topology. The diagram below gives an example of a mapping between an abtract two-node linear topology and an executable NEPI experiment, using linux::Node and linux::Application resources.

![medpicformat](http://nepi.inria.fr/pub/Nepi/TopologyGenerationTutorial/abstract_topology_mapping.png)

###The NetGraph object
Internally, the ExperimentController holds a reference to a NetGraph object that represents the abstract topology of the experiment. NetGraph objects use a [networkx](http://networkx.github.io/) undirected graph to represent the experiment topology. A NetGraph object is only instantiated if the arguments for automatic topology generation are given to the constructor of th e!ExperimentController.

<pre><code class="python"># the EC's NetGraph
netgraph = ec.netgraph

#####**Annotations**
The user can add extra information to the nodes and edges of the NetGraph object as annotations. This information is useful when mapping the abstract topology to an executable experiment.

# The networkx undirected graph with the abstract topology
topology = netgraph.topology
</code></pre>

<pre><code class="python"># Add annotation to node
ec.netgraph.annotate_node('node-id', 'annotation-id', 'annotation-value')

# retrieve node annotation
ec.netgraph.node_annotation('node-id', 'annotation-id')

# Add annotation to edge
ec.netgraph.annotate_edge('node-id1', 'node-id2', 'annotation-id', 'annotation-value')

# retrieve edge annotation
ec.netgraph.edge_annotation('node-id1', 'node-id2', 'annotation-id')
</code></pre>

###Automated Topology Generation
The ExperimentController can automatically construct the executable experiment description from an abstract topology. For this, the user must provide extra arguments for the constructor of the EC, describing the abstract topology and providing the add_node_callback and add_edge_callbackfunctions. The arguments that can be given to the ExperimentController to automate topology generation are the following:

#####**Topology generation**

- -**topo_type**: the shape of the abstract topology to be generated automatically. One of, TopologyType.LINEAR, TopologyType.TREE, TopologyType.LADDER, TopologyType.STAR, TopologyType.MESH.
node_count: the number of nodes in the abstract topology, that will be generated automatically.
- -**topology**: an undirected networkx.Graph, representing the abstract topology.
- -**assign\_st**: automatically select source and target nodes on the topology graph.
- -**assign\_ips**: automatically assign IP addresses to each node.
- -**network**: base network segment for IP address assignment.
- -**version**: IP version for IP address assignment

#####**Mapping to an executable experiment**

- -**add\_node\_callback**: function that will be invoked per each node in the abstract topology graph, to register resources for the executable experiment description.
- -**add\_edge\_callback**: function that will be invoked per each edge in the abstract topology graph.

###Topology generation
There are two alternative ways to describe the topology graph: implicit (using the topo_type and node_count arguments) and explicit (using the topologyargument).

#####**Implicit topology graph**

In the example below, an executable experiment description is automatically generated, based on an implicit 2-node linear topology.

<pre><code class="python">from nepi.execution.ec import ExperimentController
from nepi.util.netgraph import TopologyType

ec = ExperimentController("linear_topo",
        topo_type = TopologyType.LINEAR,
        node_count = 2,
        add_node_callback = add_node,
        add_edge_callback = add_edge)
</code></pre>

#####**Explicit topology graph**
In the example below, an executable experiment description is automatically generated, based on an explicit 2-node linear topology. A networkx graph can be generated manually, using networkx generators, or by loading the graph from a file.

<pre><code class="python">import networkx

from nepi.execution.ec import ExperimentController
from nepi.util.netgraph import TopologyType

ad_hoc_topo = networkx.path_graph(2)

ec = ExperimentController("linear_topo",
        topology = ad_hoc_topo,
        add_node_callback = add_node,
        add_edge_callback = add_edge)
</code></pre>

###Mapping to an executable experiment
In order to map an abstract topology to a NEPI executable experiment, NEPI needs the add_node_callback and add_edge_callbackfunctions to be provided by the user. The example below shows how to generate a executable experiment, where 2 linux nodes ping each other, from an implicit 2 node abstract topology (Same example as in the diagram above).

**1**. Define variables for host configuration, including a dictionary with the hostnames of the linux hosts, the path to the local ssh key, and the username to log in to the linux hosts.

<pre><code class="python">username = 'username'

ssh_key = 'path-to-ssh-key'

HOSTS = dict({
 0: 'hostname1',
 1: 'hostname2',
})
</code></pre>

**2**. Define the add_node function to add resources to the experiment. This function is invoked once per node in the topology graph, passing an automatically generated id (nid) from each node in the graph. In the example below, the add_node function registers a linux::Node resource for each node in the graph and adds an annotation to the netgraph to keep track of the linux::Node guid that corresponds to the nid.

<pre><code class="python">def add_node(ec, nid):
   node_guid = ec.register_resource("linux::Node")
   ec.set(node_guid, "hostname", HOSTS[nid])
   ec.set(node_guid, "username", username)
   ec.set(node_guid, "identity", ssh_key)

   ec.netgraph.annotate_node(nid, "node_guid", node_guid)
</code></pre>

**3**. Define the add_edge function to connect resources registered with the add_node function. The add_edge function is invoked once per edge in the topology graph. The add_edge function receives an object and an automatically generated identifier for two nodes in the graph. In the example below, the add_edge function is used to add a linux::Application resource to each node in order to execute a peerwise pings. The guid corresponding to the linux::Node resources is retrieved using the node annotations.

<pre><code class="python">def add_edge(ec, nid1, nid2):
   node1_guid = ec.netgraph.node_annotation(nid1, "node_guid")
   node2_guid = ec.netgraph.node_annotation(nid2, "node_guid")

   command = "ping -c3 %s"

   app1 = ec.register_resource("linux::Application")
   ec.set(app1, "command", command % HOSTS[nid2])
   ec.register_connection(app1, node1_guid)   

   app2 = ec.register_resource("linux::Application")
   ec.set(app2, "command", command % HOSTS[nid1])
   ec.register_connection(app2, node2_guid)
</code></pre>

**4**. Construct the ExperimentController giving the arguments for automatic topology generation:

<pre><code class="python">from nepi.execution.ec import ExperimentController
from nepi.util.netgraph import TopologyType

ec = ExperimentController("linear_topo",
       topo_type = TopologyType.LINEAR,
       node_count = 2,
       add_node_callback = add_node,
       add_edge_callback = add_edge)
</code></pre>

**5**. Deploy the experiment as usual, then use the wait_finished method of the ExperimentController to wait until the linux::Application resources are finished. The filter_resources method returns the list of guids for all resources of a given type. It can be used to retrieve the linux::Application resources.

<pre><code class="python">ec.deploy()

apps = ec.filter_resources("linux::Application")

ec.wait_finished(apps)
</code></pre>

**6**. Once the linux::Applications are finished, retrieve the output from the ping commands:

<pre><code class="python">for app in apps:
   print ec.trace(app, "stdout")
</code></pre>

**7**. Finally, release the ExperimentController

<pre><code class="python">ec.shutdown()
</code></pre>

Using automatic topology generation in NEPI allows to easily change the size or shape of an experiment with just one argument (i.e. node_count and topo_type). By changing the add_node and add_edge function definitions it is possible to map a same experiment scenario to multiple platforms.
