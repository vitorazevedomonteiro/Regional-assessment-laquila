# Adds the numerical model to the OpenSees domain

wipe
model BasicBuilder -ndm 3 -ndf 6

# Rigid-like material
uniaxialMaterial Elastic 99999 1000000000.0

# Define components of foundations
source foundations.tcl
# Define components of joints
source joints.tcl
# Define components of floors
source floors.tcl
# Define components of beams
source beams.tcl
# Define components of columns
source columns.tcl
# Define components of infills
source infills.tcl
# Perform static analysis under gravity loads
source gravity.tcl
