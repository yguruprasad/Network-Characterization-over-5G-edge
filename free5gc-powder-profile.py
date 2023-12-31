#!/usr/bin/env python
"""
This profile is the base for an end-to-end 5G network with 5 nodes.

One node for the 5G core, one for the simulated Radio Access Network (RAN),
one for the UPF branching function, one for the UPF anchor point 1, and one
for the UPF anchor point 2.
"""


#
# Standard geni-lib/portal libraries
#
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.emulab as elab
import geni.rspec.igext as IG

#
# Globals
#
class GLOBALS(object):
    SITE_URN = "urn:publicid:IDN+emulab.net+authority+cm"
    # Use kernel version required by free5gc: Ubuntu 18, kernel 5.0.0-23-generic
    UBUNTU18_IMG = "urn:publicid:IDN+emulab.net+image+reu2020:ubuntu1864std50023generic"
    HWTYPE = "d430"

#
# This geni-lib script is designed to run in the PhantomNet Portal.
#
pc = portal.Context()

#
# Create our in-memory model of the RSpec -- the resources we're going
# to request in our experiment, and their configuration.
#
request = pc.makeRequestRSpec()

# Create the link between the `sim-gnb` and `5GC` nodes.
gNBCoreLink = request.Link("gNBCoreLink")

# Add node which will run gNodeB and UE components with a simulated RAN.
sim_ran = request.RawPC("sim-ran")
sim_ran.component_manager_id = GLOBALS.SITE_URN
sim_ran.disk_image = GLOBALS.UBUNTU18_IMG
sim_ran.hardware_type = GLOBALS.HWTYPE
gNBCoreLink.addNode(sim_ran)

# Add node that will host the 5G Core Virtual Network Functions (AMF, SMF, UPF, etc).
free5gc = request.RawPC("free5gc")
free5gc.component_manager_id = GLOBALS.SITE_URN
free5gc.disk_image = GLOBALS.UBUNTU18_IMG
free5gc.hardware_type = GLOBALS.HWTYPE
gNBCoreLink.addNode(free5gc)

# Add node that will host the 5G Core branching UPF Virtual Network Function.
upf = request.RawPC("upfb")
upf.component_manager_id = GLOBALS.SITE_URN
upf.disk_image = GLOBALS.UBUNTU18_IMG
upf.hardware_type = GLOBALS.HWTYPE
gNBCoreLink.addNode(upf)

# Add node that will host the UPF anchor point 1.
upf1 = request.RawPC("upf1")
upf1.component_manager_id = GLOBALS.SITE_URN
upf1.disk_image = GLOBALS.UBUNTU18_IMG
upf1.hardware_type = GLOBALS.HWTYPE
gNBCoreLink.addNode(upf1)

# Add node that will host the UPF anchor point 2.
upf2 = request.RawPC("upf2")
upf2.component_manager_id = GLOBALS.SITE_URN
upf2.disk_image = GLOBALS.UBUNTU18_IMG
upf2.hardware_type = GLOBALS.HWTYPE
gNBCoreLink.addNode(upf2)

#
# Print and go!
#
pc.printRequestRSpec(request)