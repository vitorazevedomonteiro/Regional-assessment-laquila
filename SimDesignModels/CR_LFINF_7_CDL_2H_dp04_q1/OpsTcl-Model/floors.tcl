# Add floors to ops domain (nodes & diaphrams)

# Floor no. 1
# Retained floor node
node 91000 6.65 5.27410808 3.0
# Rigid floor diaphragm - multi-point constraints
rigidDiaphragm 3 91000 10001 10101 10201 10301 10011 10111 10211 10311 10021 10121 10221 10321
# Fix the floating dofs of the retained node
fix 91000 0 0 1 1 1 0

# Floor no. 2
# Retained floor node
node 92000 6.65 5.26476082 6.0
# Rigid floor diaphragm - multi-point constraints
rigidDiaphragm 3 92000 10002 10102 10202 10302 10012 10112 10212 10312 10022 10122 10222 10322
# Fix the floating dofs of the retained node
fix 92000 0 0 1 1 1 0
