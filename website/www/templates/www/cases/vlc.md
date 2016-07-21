

#VLC/CCN Streaming Experiment using PlanetLab and OMF 6
The goal of this use case is to compare the performance of CCN and classic VOD Streaming deployments, to stream video from a content provider to a wireless home setting, across the Internet.

###Experiment Description
You are living in an house with 3 chambers. You want to see a movie in your living room. As you didn't buy this movie, you will use a VOD website as NetFlix to provide this video. This video will have to be transferred from the VOD Content Provider until the Internet box from your house.

Moreover, your kids decide to see this movie. However, they want to watch it from their bedroom because they want to play at the same time. You decide to share the stream content through wireless to their laptop.

###Modelisation
The Netflix servers will be modeled by PlanetLab Node. Indeed, PlanetLab is a plateform containing nodes spread all around the world connected through Internet. It represents similar conditions as the Netflix Architecture. Using PlanetLab, the video can be streamed though Internet until reaching the entrance of the wireless testbed.

OMF ( cOntrol and Management Framework ) is a well known components used in Wireless Testbed. OMF Testbed are composed by a Gateway, that orchestrate the nodes and usually host the XMPP Server (used for the communication), and the nodes themselves. For this use case, the OMF nodes will represent the video streaming client (in each bedroom), and an other OMF node will be as the Home Media Center. The traffic to the Home Media Center Node will be done though the gateway using wired connection.

We will use NEPI to evaluate several alternatives to deliver content to the house, using VLC in different modes: Broadcast and Video On Demand.
You can find below a representation of the experiment scenario:

The picture shows how we are going to simulate a VOD website delivering a content to several wireless devices in a house using:

- content server : PL node
- media server: one w-iLab.t node
- wireless devices : 5 w-iLab.t nodes
- NEPI for global orchestration

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/demo_scenarioT.png)

###Experiment Stages
All stages taken care of by NEPI

- Provisioning the resources for the experiment: through SFA, one PlanetLab node and 6 w-iLab.t nodes (media center + 5 devices)
- Resources configuration and control
- ssh access into the Planetlab node, FRCP for the w-iLab.t nodes
- Data collection

Below you can find a graphical representation of the experiment deployment lifecycle (the experiment stages numerated above):

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/exp_deploymentT.png)

###Scripts
The following script has been implemented:

- [Script to deploy the VOD experiment](http://nepi.inria.fr/code/nepi/file/8b8b246fafc8/examples/omf/vod_exp/vod_experiment.py)

###Results
We plot the results using matplotlib, is possible to see the number of frames growing for the video transfer in vod mode, and not for broadcast mode as expected. And more packet loss for more clients.

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/graph1T.png)

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/graph2T.png)

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/graph3T.png)

![picformat](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/graph4T.png)

###Video
Take a look at the [video with audio](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/nepi-video-v7-mp3-audio.mkv)
explaning the experiment, presented in the final review of the Openlab project in September 2014.

###Conclusion
Is possible to deploy the experiment using NEPI from end to end. But this use case is not finished because we didn't perform the CCN part yet. The video proved that the experiment works but some modifications in the iMinds gateway was necessary in order to forward the UDP stream of the video. Consequently, this use case is quite hard to redo because it depends on the testbed configuration.

###Attachments
- [nepi_omf6_iminds_vlc.py.txt](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/nepi_omf6_iminds_vlc.py.txt)
- [nepi_omf6_iminds_vlc_vod.py.txt](http://nepi.inria.fr/pub/UseCases/VLCCCNStreamingExperiment/nepi_omf6_iminds_vlc_vod.py.txt)

###Authors
- Lucia Guevgeozian Odizzio
- Julien Tribino
- Alina Quereilhac
