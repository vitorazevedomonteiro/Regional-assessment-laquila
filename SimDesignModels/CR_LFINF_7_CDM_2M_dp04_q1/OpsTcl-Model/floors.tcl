# Add floors to ops domain (nodes & diaphrams)

# Floor no. 1
# Retained floor node
node 91000 6.65 5.25667273 3.0
# Rigid floor diaphragm - multi-point constraints
rigidDiaphragm 3 91000 1 101 201 301 11 111 211 311 21 121 221 321
# Fix the floating dofs of the retained node
fix 91000 0 0 1 1 1 0

# Floor no. 2
# Retained floor node
node 92000 6.65 5.24672224 6.0
# Rigid floor diaphragm - multi-point constraints
rigidDiaphragm 3 92000 2 102 202 302 12 112 212 312 22 122 222 322
# Fix the floating dofs of the retained node
fix 92000 0 0 1 1 1 0
