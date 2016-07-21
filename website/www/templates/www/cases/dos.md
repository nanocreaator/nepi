
#Deny Of Service and Information Disclosure on Openflow over PlanetLab
Some functional components are weak points for OpenFlow and thus allow us to imagine different possible attacks. For example for OpenFlow switches, components like ingress buffer or flows table allow us to get their respective sizes, such information may prove to be useful, when we want to make a DDoS attack. In this use case, t wo different types of attack, Deny of Service and Information Disclosure, are performed on an Openflow Controller over the experimental platform PlanetLab.

###Experiment Description
Some functional components are weak points for OpenFlow and thus allow us to imagine different possible attacks. For example for OpenFlow switches, components like ingress buffer or flows table allow us to get their respective sizes, such information may prove to be useful, when we want to make a DDoS attack. In this use case, we are more interested in the interaction between the controller and one switch of the network. This interaction is a weak point of OpenFlow because it allow us to determine the content of the flows table of the swicth. This asynchronous channel is used by the switch to request the controller in order that the latter take a decision concerning a data packet that the switch doesn't know how to forward it. In return the controller give a "rule" to the switch. In fact this rule is only a new entry of the flows table allowing the switch to forward this packet and the following (packets that belong to the same communication).

When an OpenFlow switch receive a packet, several cases are possible :

- The switch has an entry in the flows table that match this packet, thus it executes the corresponding action : in the simplest case it redirects to the corresponding interface.
- The switch has no entry that match this packet, thus it doesn't know how to forward the packet and so it request the controller through the asynchronous channel.

In this use case, we performed 2 different types of attack, Deny of Service and Information Disclosure, on an Openflow Controller over the experimental platform PlanetLab.

###Deny of Service
The aim of this first attack is to overload the controller with a lot of packets. However, as the experiment is running over PlanetLab, which use Internet, the experiment can not be ran without taking into considerations the impact on the real traffic. Therefore, instead of generate a huge number of packet we took the decision to reduce the maximal size of the flow table, using the following command :

<pre><code class="bash">$ sudo ovs-vsctl add bridge nepi_bridge_1 flow_tables 0=@inria_pres -- --id=@inria_pres create flow_table flow_limit=100</code></pre>

Once the flow table is configured, the experiment consists at sending more than 100 packets to the switch. This latter will ask the controller to know what he needs to do. After the 100 packets, the table of the controller will be full and when we try to process a ping between 2 nodes, an error occurred on the controller showing that the attack works successfully.

###Information disclosure
Information Disclosure is a passive attack, which allow us to get miscellaneous information about the targeted network. It is a passive attack to the extent that it doesn't damage the working of the network. As part of networks using OpenFlow, such an attack allow attacker to determine the topology of the network, the features of some nodes of the network as well as some details of communication between these nodes : in fact it is information that a normal user isn't supposed to have.

Among the information that can be stolen using this attack, we focus on the detection of the field in the flow table that create aggregated rules for one packet. Therefore, we use the following algorithms :

- One host sends a packet with a given pattern and measures its RTT.
- This node sends a second identical packet with the same pattern and measures also its RTT.
- Finally this node sends a third paquet by changing only one field (e.g. the destination port) and measures its RTT.

We suppose the entry that corresponds to the first packet isn't present. Thus, the RTT of this packet is long. Then we note that the second RTT is smaller than the first one. Finally two cases are possible for the third packet :

- The RTT is long (a new entry is created), so it means that the field we modified doesn't contain the aggregation character.
- The RTT is smalll ( no entry is created), so it means that the field we modified, is a part of the aggregated fields.

We can represent this attack with the following diagram :

![picformat](http://nepi.inria.fr/pub/UseCases/DosOpenflow/ddos_id_image.jpg)

###Role of NEPI
In this use case, NEPI was used to deploy the Openflow topology over the PlanetLab testbed. Different Resources Managers exist in NEPI for OpenVSwitch, allowing a user to deploy a topology. Each PlanetLab node can have the choice between 3 behaviours, depending on the type of RM running : Switch, Host or Controller.

The generation of the packet was done by the [library scapy](http://www.secdev.org/projects/scapy/)

###Scripts
The followings scripts have been implemented :

- [script to deploy the openflow topology on openlab for the DDOS Attack](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_ddos.py.txt)
- [script to deploy the openflow topology on openlab for the Information Disclosure Attack](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_info_disclosure.py.txt)
- [script use to generate the packet with scapy](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_scapy.py.txt)
- [code of the controller used in order to create aggregate rules](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_pox.py.txt)

###Results
Below are presented the results from the project. More results can ben found with more time of investigation using the script provided above.

#####**Denial of service**
![picformat](http://nepi.inria.fr/pub/UseCases/DosOpenflow/ddos_graph_1.png)

From the two curves (one representing 100 packets and the other 200 packets sent), we can noticed that with a little hard_timeout completion time, the ddos is much longer than with a big hard_timeout. Hard timeout is the time before a rule be removed from the flow table. This is explained by the fact that for a hard_timeout small when sending packets, flow installed quickly evicted from the table and the risk that the table is full are zero so the attack takes longer to be realized. Whereas with a "hard_timeout" tall, flow remain much longer and the risk that the table is full getting bigger and effective attack becomes faster.

![picformat](http://nepi.inria.fr/pub/UseCases/DosOpenflow/ddos_graph_2.png)

We note easily with this histogram (blue for 100 packets sent and red for 200 packets sent) that the more "hard_timeout" is great as the number of packet loss is important. This is normal because as the flows remain longer, it is easy to overload the table. Unlike a low hard_timeout where the attack will be very delicate in the sense that the flow rules are removed quickly (10-20 seconds) and so it will be more difficult to overload the flow_table.

#####**Information disclosure**
![picformat](http://nepi.inria.fr/pub/UseCases/DosOpenflow/graph_id_1_en.png)

We can note on this graph that for each pair of sent packets, the RTT of the first packet approximate the 700 ms while the duration of the second packet is around 300 ms. From this graph we can conclude that the hypothesis concerning the Information Disclosure is valid. Secondly we modified once again the program to obtain the difference between the RTT of the first and second packet and this for many pairs. Consequently we obtained the following results :

![picformat](http://nepi.inria.fr/pub/UseCases/DosOpenflow/graph_id_2_en.png)

We can note on this graph that the difference between two RTT for each pair of packets is quite the same. In reality this difference of time is the extra workload introduced when the switch request the controller. From this graph we can deduce that this supplementary workload is constant.

So another idea to perform the Information Disclosure is to realize a statistical step, in which we could obtain an average of the crossing time for “long” packets (it means packets that cross the network with a long time). This allow us to compare the crossing of a packet, that we send, with this average and then to make conclusions.

###Conclusion
This use case is not really finished as many others results can be retrieved from the expeirments, using the script provided below. However, it shows how Nepi can support the experiment in his study, simplifying all the work of deploying Openflow Topology over PlanetLab and let the user focus on the important part : The attack.

It is important to notice that this use case was done in the context of project school including some time constraints and can be improved by any interested user.

###Attachments
- [Script_ovs_ddos.py.txt](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_ddos.py.txt)
- [Script_ovs_info_disclosure.py.txt](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_info_disclosure.py.txt)
- [Script_ovs_pox.py.txt](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_pox.py.txt)
- [Script_ovs_scapy.py.txt](http://nepi.inria.fr/pub/UseCases/DosOpenflow/script_ovs_scapy.py.txt)

###Authors
- Rousseau Anthony
- Duong Michel
- Fernando Bruno
- Lazizi Ouardia
