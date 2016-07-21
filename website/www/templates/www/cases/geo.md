
#GEO-Cloud
GEO-Cloud is a close to reality industry driven experiment that will go beyond conventional services and infrastructures in the EO sector to implement and test in cloud a complete EO system (from the acquisition of geo-data with a constellation of satellites to its distribution to end users with remote access). The main objective is to value if the use of future internet technologies provides socio-economical viable solutions applicable to industry to offer highly demanding services such as crisis management in the EO sector.

###Experiment Description

#####**The GEO-Cloud experiment**
GEO-Cloud is a close to reality industry driven experiment that will go beyond conventional services and infrastructures in the EO sector to implement and test in cloud a complete EO system (from the acquisition of geo-data with a constellation of satellites to its distribution to end users with remote access). The main objective is to value if the use of future internet technologies provides socio-economical viable solutions applicable to industry to offer highly demanding services such as crisis management in the EO sector.

The scenario is that of a constellation of 17 satellites in Low Earth Orbits that covers the Earth’s surface in a daily basis, the geo-data is downloaded in 12 ground stations distributed around the world and transferred to the cloud for its treatment and distribution. We will focus in two main use cases: i) to offer basic satellite imagery services ii) to offer high added value services with real time response to manage crisis events such as natural disasters.

GEO-Cloud will emulate the remote sensing mission with the satellites, the topology network and the communications in the Virtual Wall testbed. The data acquired from the emulated satellites will be transferred to the BonFIRE cloud for storage, processing and distribution of data. End users accessing and broadcasting will be emulated in another network implemented in Virtual Wall. In order to implement realistic impairments in Virtual Wall, real networks will be tested in PlanetLab Europe. The technologies for imagery distribution and EO service delivery using cloud technologies and Internet protocols will be tested. In 1 a scheme of the GEO-Cloud experiment is depicted.

![picformat](http://nepi.inria.fr/pub/UseCases/GeoCloud/GeoCloud_image1.png)

The GEO-Cloud objectives are summarized as follows :

- 1- To implement in Fed4FIRE a close to real world Earth Observation system.
- 2- To test and validate the following models :
  - A global remote sensing model
  - A cloud model for Earth Observation
  - A model of end-users demand
- 3- To compare the different types of services offered (basic and added value services) to cover different types of demand.
- 4- To validate if future internet cloud computing and networks provide viable solutions for conventional Earth Observation systems to establish the basis for the implementation of EO infrastructures in cloud.
- 5- To verify if the Fed4FIRE infrastructure and tools are appropriate for running this complex, close to reality experiments.

#####**The GEO-Cloud experiment**
We used PlanetLab Europe and PlanetLab Central to obtain realistic models of the network impairments to be implemented in the GEO-Cloud experiment deployed in Fed4FIRE, specifically, in the links between i) the ground station simulators and the BonFIRE cloud and ii) between the end users and the BonFIRE cloud.

Thus, the experiment carried out in PlanetLab consists of measuring the impairments in a network implemented in PlanetLab to obtain their models and implement them in networks connecting Virtual Wall and BonFIRE, i.e. between the ground stations and the cloud, respectively to realistically simulate the complete Earth Observation system. The experiment then consists of communicating 12 real nodes representing the ground stations (the nearest PlanetLab node to the real ground station was selected) and the end users distributed around the world (we selected 31 nodes from different 31 countries) with a node representing the cloud (located in INRIA) to measure the real impairments of the networks and to implement a realistic model of the communications, see 2.

We defined that the network depends of the effective bandwidth, the loss rate and the latency. Those impairments were measured between the nodes representing the ground stations and the end users with the node representing the cloud. To obtain a representative behavior of the network 21600 trials were done to measure the impairments between the links.

The deployment of the experiment was done with NEPI, in which Iperf and Ping were implemented to measure the impairments.

![picformat](http://nepi.inria.fr/pub/UseCases/GeoCloud/GeoCloud_image2.png)

###Role of NEPI
For this experiment, NEPI provides the following favourable points:

- The software (in this case PING and IPERF) were deployed and executed remotely and automatically.
- NEPI provided the reservation of PlanetLab nodes around the world automatically. Although it offers the possibility of provisioning a specific node if desired, as well.
- The traces were fetched by NEPI and pushed into our computers easily.
- We could compute some constraints about how the experiment and nodes had to be executed. For example we provided a scheduling for the execution and a constraint that consisted of making a node acting as a client until a condition was fulfilled and then make it acting as a server when the condition was not fulfilled.
- In the PlanetLab case, NEPI allowed us to automatically select and provision a node from a specific country or region. This was very useful for us when provisioning the nodes simulating end users accessing the web services.

###Scripts
The followings scripts have been implemented :

- [Script to measure the effective bandwidth in the ground stations nodes]()
- [Script to measure the effective bandwidth in the end users nodes]()
- [Script to measure the latency in the ground stations nodes]()
- [Script to measure the latency in the end users nodes]()
- [Script to measure the loss rate in the ground stations nodes]()
- [Script to measure the loss rate in the end users nodes]()

###Results
[Paper in the “Workshop on Federated Future Internet and Distributed Cloud Testbeds (FIDC2014)” with the experiment results](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6932980)

###Conclusion
The NEPI platform is very useful and user-friendly. It allows experimenters to deploy a large scale experiment around the world in few steps. The learning curve is high because NEPI does all low-level actions for you so you can focus in the high level aspects of the experiment.

It is also important to highlight that it is open-source, so anyone can use it, and it is programmed in Python, which is easy to use.

###Authors
- Rubén Pérez
- Manuel José Latorre
- Félix Pedrera
- Jonathan Becedas
- Gerardo González
