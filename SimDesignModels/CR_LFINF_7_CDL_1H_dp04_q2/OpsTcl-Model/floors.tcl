# Add floors to ops domain (nodes & diaphrams)

# Floor no. 1
# Retained floor node
node 91000 6.65 5.0 3.0
# Rigid floor diaphragm - multi-point constraints
rigidDiaphragm 3 91000 10001 10101 10201 10301 10011 10111 10211 10311 10021 10121 10221 10321
# Fix the floating dofs of the retained node
fix 91000 0 0 1 1 1 0
