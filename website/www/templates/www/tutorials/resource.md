
#Inspecting resources tutorial

This tutorial explains how to get information about available resources in NEPI, and their configuration attributes and traces.

###Printing available resources
The ResourceFactory class holds information about all the resources supported by NEPI to model experiments. The code below shows how to print the list of available resource type_ids and the resource description.

from nepi.execution.resource import ResourceFactory

<pre><code class="python">for type_id in ResourceFactory.resource_types():
    rm_type = ResourceFactory.get_resource_type(type_id)
    print type_id, ":", rm_type.get_help() or "No description available"
</code></pre>

###Printing resource attributes
The code below can be used to list the attributes associated to a resource type, in this case the linux::Application resource type.

from nepi.execution.resource import ResourceFactory

type_id = "linux::Application"

<pre><code class="python">rm_type = ResourceFactory.get_resource_type(type_id)
for attr in rm_type.get_attributes():
  print "", attr.name, ":", attr.help
</code></pre>

###Printing resource traces
The traces that area available for a resource type can be listen as shown below. In this case traces are listed for the linux::Application, and it is also indictaed whether the traces are enabled by default.

<pre><code class="python">from nepi.execution.resource import ResourceFactory

type_id = "linux::Application"

rm_type = ResourceFactory.get_resource_type(type_id)
for trace in rm_type.get_traces():
   print "", trace.name, ":", trace.enabled
</code></pre>
