source modal.tcl
source nspa.tcl

# Perform modal analysis
set results [do_modal 3]
# Perform nonlinear static pushover analysis in X direction
lassign [do_nspa_x] dx vx
# Perform nonlinear static pushover analysis in Y direction
lassign [do_nspa_y] dy vy
