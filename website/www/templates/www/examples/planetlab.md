
#PlanetLab experiments with NEPI
This section presents a step-by-step tutorial explaining how to use PlanetLab resources in a NEPI script.
How to use PlanetLab
PlanetLab is a world wide distributed testbed of hosts (nodes) connected through the Internet. PlanetLab is an ideal testbed to conduct experiments that require realistic Internet conditions, since you get direct access to the Internet itself.
Two main PlanetLab deployments are available to the public:
PlanetLab Central
PlanetLab Europe
Other deployments exist, but access is private:
PlanetLab Japan
PlanetLab Korea (PPK)
In order to use PlanetLab testbeds, the first thing that is required is to get an account.
Create an account
Visit the PlanetLab Central or the PlanetLab Europe website and click on the button "Create an account" on the right side.
Fill the form with your personal information and the site you belongs to.
Wait for the PI (Principal Investigator) of your site to validate your registration.
Log in to your account and upload your public key
How To Access PlanetLab nodes
To run experiments using PlanetLab resources you will need a slice. If you don't have a slice, ask you PI to assign one to you. A slice is a "virtual container" that contains the resources (hosts) used in your experiments.
In the slice page of the PlanetLab site you can browse and add hosts to your slice. When you add a host to your slice, a virtual machine (sliver) will be created in that host for the exclusive use of your slice.
You need to wait around 30 min for the VM to be created with your credentials.
Then you should be able to access through ssh the node : ssh slice_name@node_name
How to use PlanetLab in a NEPI script
In order to use PlanetLab hosts in a NEPI script, you will need to register resources of type planetlab::Node with the ExperimentController (EC). Otherwise, PlanetLab hosts use Linux, so you can connect linux::Application resources to a planetlab::Node.
Register PlanetLab resources
Four attributes must be set in a PlanetlabNode resource to add your credentials to access the hosts:
username : the name of your slice
identity : the path to the public SSH file on your local machine (usually ~/.ssh/id_rsa.pub)
pluser : the user used to authenticate on the website ( usually, a mail address )
plpassword : the password used to authenticate on the website
An example to show how to register a planetlab::Node:
