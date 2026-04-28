# Add components of joints to ops domain

# -------------------------------------------------
# Add stairs joints to ops domain
# -------------------------------------------------

# -------------------------------------------------
# Add floor joints to ops domain
# -------------------------------------------------

# Joint grid ids (x, y, z): (0, 0, 1)
node 1 0.0 0.0 3.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10001 0.0 0.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300001 42301.8123
uniaxialMaterial Elastic 400001 36597.115
section Aggregator 10001 99999 P 99999 Vy 99999 Vz 400001 My 300001 Mz 99999 T
element zeroLengthSection 10001 1 10001 10001 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 0, 1)
node 101 5.0 0.0 3.0 -mass 10.773272171253824 10.773272171253824 10.773272171253824 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10101 5.0 0.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300101 65575.64675
uniaxialMaterial Elastic 400101 44660.3611
section Aggregator 10101 99999 P 99999 Vy 99999 Vz 400101 My 300101 Mz 99999 T
element zeroLengthSection 10101 101 10101 10101 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 0, 1)
node 201 8.3 0.0 3.0 -mass 10.773272171253824 10.773272171253824 10.773272171253824 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10201 8.3 0.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300201 65575.64675
uniaxialMaterial Elastic 400201 44660.3611
section Aggregator 10201 99999 P 99999 Vy 99999 Vz 400201 My 300201 Mz 99999 T
element zeroLengthSection 10201 201 10201 10201 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 0, 1)
node 301 13.3 0.0 3.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10301 13.3 0.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300301 42301.8123
uniaxialMaterial Elastic 400301 36597.115
section Aggregator 10301 99999 P 99999 Vy 99999 Vz 400301 My 300301 Mz 99999 T
element zeroLengthSection 10301 301 10301 10301 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 1, 1)
node 11 0.0 5.0 3.0 -mass 13.256880733944953 13.256880733944953 13.256880733944953 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10011 0.0 5.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300011 56652.2333
uniaxialMaterial Elastic 400011 49162.55725
section Aggregator 10011 99999 P 99999 Vy 99999 Vz 400011 My 300011 Mz 99999 T
element zeroLengthSection 10011 11 10011 10011 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 1, 1)
node 111 5.0 5.0 3.0 -mass 20.606483180428132 20.606483180428132 20.606483180428132 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10111 5.0 5.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300111 82552.9297
uniaxialMaterial Elastic 400111 56564.23705
section Aggregator 10111 99999 P 99999 Vy 99999 Vz 400111 My 300111 Mz 99999 T
element zeroLengthSection 10111 111 10111 10111 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 1, 1)
node 211 8.3 5.0 3.0 -mass 20.606483180428132 20.606483180428132 20.606483180428132 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10211 8.3 5.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300211 82552.9297
uniaxialMaterial Elastic 400211 56564.23705
section Aggregator 10211 99999 P 99999 Vy 99999 Vz 400211 My 300211 Mz 99999 T
element zeroLengthSection 10211 211 10211 10211 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 1, 1)
node 311 13.3 5.0 3.0 -mass 13.256880733944953 13.256880733944953 13.256880733944953 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10311 13.3 5.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300311 56652.2333
uniaxialMaterial Elastic 400311 49162.55725
section Aggregator 10311 99999 P 99999 Vy 99999 Vz 400311 My 300311 Mz 99999 T
element zeroLengthSection 10311 311 10311 10311 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 2, 1)
node 21 0.0 10.0 3.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10021 0.0 10.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300021 42301.8123
uniaxialMaterial Elastic 400021 36597.115
section Aggregator 10021 99999 P 99999 Vy 99999 Vz 400021 My 300021 Mz 99999 T
element zeroLengthSection 10021 21 10021 10021 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 2, 1)
node 121 5.0 10.0 3.0 -mass 10.773272171253824 10.773272171253824 10.773272171253824 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10121 5.0 10.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300121 65575.64675
uniaxialMaterial Elastic 400121 44660.3611
section Aggregator 10121 99999 P 99999 Vy 99999 Vz 400121 My 300121 Mz 99999 T
element zeroLengthSection 10121 121 10121 10121 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 2, 1)
node 221 8.3 10.0 3.0 -mass 10.773272171253824 10.773272171253824 10.773272171253824 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10221 8.3 10.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300221 65575.64675
uniaxialMaterial Elastic 400221 44660.3611
section Aggregator 10221 99999 P 99999 Vy 99999 Vz 400221 My 300221 Mz 99999 T
element zeroLengthSection 10221 221 10221 10221 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 2, 1)
node 321 13.3 10.0 3.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10321 13.3 10.0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300321 42301.8123
uniaxialMaterial Elastic 400321 36597.115
section Aggregator 10321 99999 P 99999 Vy 99999 Vz 400321 My 300321 Mz 99999 T
element zeroLengthSection 10321 321 10321 10321 -orient 0 0 1 0 1 0 -doRayleigh 0 
