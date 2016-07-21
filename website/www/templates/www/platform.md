
#Linux Testbeds
If your testbed consists of Linux hosts then NEPI can work on it "out of the box", given the following reuquirements:

- Users are given a SSH account with SSH key authentication
- Users have sudo with no password enabled in the suddoers file
- Users have sudo with requiretty disabled in the suddoers file
- Hosts have an IPv4 address
- Hosts use Ubuntu/Debian or Fedora (other Linux distributions might work as well but are un tested)

#Planetlab
Worldwide distributed network, composed of thousands of hosts interconnected through the Internet

- Host are virtualized and resources are shared by multiple experiments (Many VMs per host)
- Restricted privileges to manipulate network configuration
- Access resources through SSH key authentication
- [PlanetLab Central](http://www.planet-lab.org)
- [PlanetLab Europe](http://www.planet-lab.eu)

#OMF 6.0
A Control and Management Framework for Networking Testbed Wireless LAN testbeds

- Hosts are not virtualized and resources can not be shared by many users (Only one user per host at the same time)
- Full privileges to manipulate network configuration
- Access resource through XMPP service
- Many Wireless deployments open to researchers (NICTA, NITOS, w-Ilab.t,..)
- [More info](http://omf.mytestbed.net)

#NS-3 Network Simulator
Discrete-event network simulator for Internet systems

- Real-time mode
- Real-world traffic (Ethernet, IP, etc..)
- Good wireless models
- Easy interconnection with the outside world thanks to a device abstraction layer
- [More info](www.nsnam.org)

#Direct Code Execution
Application layer emulation using ns-3 network models

- Execution of unmodified application binaries
- Support for linux network stacks
- [More info](http://www.nsnam.org/overview/projects/direct-code-execution/)
