# Add components of joints to ops domain

# -------------------------------------------------
# Add stairs joints to ops domain
# -------------------------------------------------

# Joint grid ids (x, y, z): (1, 0, 0.5)
node 1101 5.0 0.0 1.5 -mass 3.3837675840978605 3.3837675840978605 3.3837675840978605 0.0 0.0 0.0

# Joint grid ids (x, y, z): (2, 0, 0.5)
node 1201 8.3 0.0 1.5 -mass 3.3837675840978605 3.3837675840978605 3.3837675840978605 0.0 0.0 0.0

# Joint grid ids (x, y, z): (1, 0, 1.5)
node 1102 5.0 0.0 4.5 -mass 3.3434006116207966 3.3434006116207966 3.3434006116207966 0.0 0.0 0.0

# Joint grid ids (x, y, z): (2, 0, 1.5)
node 1202 8.3 0.0 4.5 -mass 3.3434006116207966 3.3434006116207966 3.3434006116207966 0.0 0.0 0.0

# -------------------------------------------------
# Add floor joints to ops domain
# -------------------------------------------------

# Joint grid ids (x, y, z): (0, 0, 1)
node 1 0 0 3.0 -mass 8.72262996941896 8.72262996941896 8.72262996941896 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10001 0 0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300001 33019.1508
uniaxialMaterial Elastic 400001 28236.1776
section Aggregator 10001 99999 P 99999 Vy 99999 Vz 400001 My 300001 Mz 99999 T
element zeroLengthSection 10001 1 10001 10001 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 0, 1)
node 101 5 0 3.0 -mass 8.647223241590213 8.647223241590213 8.647223241590213 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10101 5 0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300101 56704.87985
uniaxialMaterial Elastic 400101 49470.71035
section Aggregator 10101 99999 P 99999 Vy 99999 Vz 400101 My 300101 Mz 99999 T
element zeroLengthSection 10101 101 10101 10101 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 0, 1)
node 201 8.3 0 3.0 -mass 8.647223241590213 8.647223241590213 8.647223241590213 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10201 8.3 0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300201 56704.87985
uniaxialMaterial Elastic 400201 49470.71035
section Aggregator 10201 99999 P 99999 Vy 99999 Vz 400201 My 300201 Mz 99999 T
element zeroLengthSection 10201 201 10201 10201 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 0, 1)
node 301 13.3 0 3.0 -mass 8.72262996941896 8.72262996941896 8.72262996941896 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10301 13.3 0 3.0 # Constrained floor node
uniaxialMaterial Elastic 300301 33019.1508
uniaxialMaterial Elastic 400301 28236.1776
section Aggregator 10301 99999 P 99999 Vy 99999 Vz 400301 My 300301 Mz 99999 T
element zeroLengthSection 10301 301 10301 10301 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 1, 1)
node 11 0 5 3.0 -mass 15.901529051987769 15.901529051987769 15.901529051987769 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10011 0 5 3.0 # Constrained floor node
uniaxialMaterial Elastic 300011 62803.51325
uniaxialMaterial Elastic 400011 44301.04495
section Aggregator 10011 99999 P 99999 Vy 99999 Vz 400011 My 300011 Mz 99999 T
element zeroLengthSection 10011 11 10011 10011 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 1, 1)
node 111 5 5 3.0 -mass 22.623807339449538 22.623807339449538 22.623807339449538 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10111 5 5 3.0 # Constrained floor node
uniaxialMaterial Elastic 300111 127786.06275
uniaxialMaterial Elastic 400111 99134.4792
section Aggregator 10111 99999 P 99999 Vy 99999 Vz 400111 My 300111 Mz 99999 T
element zeroLengthSection 10111 111 10111 10111 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 1, 1)
node 211 8.3 5 3.0 -mass 22.623807339449538 22.623807339449538 22.623807339449538 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10211 8.3 5 3.0 # Constrained floor node
uniaxialMaterial Elastic 300211 127786.06275
uniaxialMaterial Elastic 400211 99134.4792
section Aggregator 10211 99999 P 99999 Vy 99999 Vz 400211 My 300211 Mz 99999 T
element zeroLengthSection 10211 211 10211 10211 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 1, 1)
node 311 13.3 5 3.0 -mass 15.901529051987769 15.901529051987769 15.901529051987769 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10311 13.3 5 3.0 # Constrained floor node
uniaxialMaterial Elastic 300311 62803.51325
uniaxialMaterial Elastic 400311 44301.04495
section Aggregator 10311 99999 P 99999 Vy 99999 Vz 400311 My 300311 Mz 99999 T
element zeroLengthSection 10311 311 10311 10311 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 2, 1)
node 21 0 10 3.0 -mass 8.72262996941896 8.72262996941896 8.72262996941896 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10021 0 10 3.0 # Constrained floor node
uniaxialMaterial Elastic 300021 33019.1508
uniaxialMaterial Elastic 400021 28236.1776
section Aggregator 10021 99999 P 99999 Vy 99999 Vz 400021 My 300021 Mz 99999 T
element zeroLengthSection 10021 21 10021 10021 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 2, 1)
node 121 5 10 3.0 -mass 12.896694189602448 12.896694189602448 12.896694189602448 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10121 5 10 3.0 # Constrained floor node
uniaxialMaterial Elastic 300121 62895.78755
uniaxialMaterial Elastic 400121 58652.3389
section Aggregator 10121 99999 P 99999 Vy 99999 Vz 400121 My 300121 Mz 99999 T
element zeroLengthSection 10121 121 10121 10121 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 2, 1)
node 221 8.3 10 3.0 -mass 12.896694189602448 12.896694189602448 12.896694189602448 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10221 8.3 10 3.0 # Constrained floor node
uniaxialMaterial Elastic 300221 62895.78755
uniaxialMaterial Elastic 400221 58652.3389
section Aggregator 10221 99999 P 99999 Vy 99999 Vz 400221 My 300221 Mz 99999 T
element zeroLengthSection 10221 221 10221 10221 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 2, 1)
node 321 13.3 10 3.0 -mass 8.72262996941896 8.72262996941896 8.72262996941896 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10321 13.3 10 3.0 # Constrained floor node
uniaxialMaterial Elastic 300321 33019.1508
uniaxialMaterial Elastic 400321 28236.1776
section Aggregator 10321 99999 P 99999 Vy 99999 Vz 400321 My 300321 Mz 99999 T
element zeroLengthSection 10321 321 10321 10321 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 0, 2)
node 2 0 0 6.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10002 0 0 6.0 # Constrained floor node
uniaxialMaterial Elastic 300002 42301.8123
uniaxialMaterial Elastic 400002 36597.115
section Aggregator 10002 99999 P 99999 Vy 99999 Vz 400002 My 300002 Mz 99999 T
element zeroLengthSection 10002 2 10002 10002 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 0, 2)
node 102 5 0 6.0 -mass 7.323853211009173 7.323853211009173 7.323853211009173 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10102 5 0 6.0 # Constrained floor node
uniaxialMaterial Elastic 300102 49116.39325
uniaxialMaterial Elastic 400102 37364.9203
section Aggregator 10102 99999 P 99999 Vy 99999 Vz 400102 My 300102 Mz 99999 T
element zeroLengthSection 10102 102 10102 10102 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 0, 2)
node 202 8.3 0 6.0 -mass 7.323853211009173 7.323853211009173 7.323853211009173 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10202 8.3 0 6.0 # Constrained floor node
uniaxialMaterial Elastic 300202 49116.39325
uniaxialMaterial Elastic 400202 37364.9203
section Aggregator 10202 99999 P 99999 Vy 99999 Vz 400202 My 300202 Mz 99999 T
element zeroLengthSection 10202 202 10202 10202 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 0, 2)
node 302 13.3 0 6.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10302 13.3 0 6.0 # Constrained floor node
uniaxialMaterial Elastic 300302 42301.8123
uniaxialMaterial Elastic 400302 36597.115
section Aggregator 10302 99999 P 99999 Vy 99999 Vz 400302 My 300302 Mz 99999 T
element zeroLengthSection 10302 302 10302 10302 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 1, 2)
node 12 0 5 6.0 -mass 13.318042813455659 13.318042813455659 13.318042813455659 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10012 0 5 6.0 # Constrained floor node
uniaxialMaterial Elastic 300012 56772.60865
uniaxialMaterial Elastic 400012 56772.60865
section Aggregator 10012 99999 P 99999 Vy 99999 Vz 400012 My 300012 Mz 99999 T
element zeroLengthSection 10012 12 10012 10012 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 1, 2)
node 112 5 5 6.0 -mass 20.25018348623853 20.25018348623853 20.25018348623853 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10112 5 5 6.0 # Constrained floor node
uniaxialMaterial Elastic 300112 102962.85915
uniaxialMaterial Elastic 400112 90870.2508
section Aggregator 10112 99999 P 99999 Vy 99999 Vz 400112 My 300112 Mz 99999 T
element zeroLengthSection 10112 112 10112 10112 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 1, 2)
node 212 8.3 5 6.0 -mass 20.25018348623853 20.25018348623853 20.25018348623853 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10212 8.3 5 6.0 # Constrained floor node
uniaxialMaterial Elastic 300212 102962.85915
uniaxialMaterial Elastic 400212 90870.2508
section Aggregator 10212 99999 P 99999 Vy 99999 Vz 400212 My 300212 Mz 99999 T
element zeroLengthSection 10212 212 10212 10212 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 1, 2)
node 312 13.3 5 6.0 -mass 13.318042813455659 13.318042813455659 13.318042813455659 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10312 13.3 5 6.0 # Constrained floor node
uniaxialMaterial Elastic 300312 56772.60865
uniaxialMaterial Elastic 400312 56772.60865
section Aggregator 10312 99999 P 99999 Vy 99999 Vz 400312 My 300312 Mz 99999 T
element zeroLengthSection 10312 312 10312 10312 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (0, 2, 2)
node 22 0 10 6.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10022 0 10 6.0 # Constrained floor node
uniaxialMaterial Elastic 300022 42301.8123
uniaxialMaterial Elastic 400022 36597.115
section Aggregator 10022 99999 P 99999 Vy 99999 Vz 400022 My 300022 Mz 99999 T
element zeroLengthSection 10022 22 10022 10022 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (1, 2, 2)
node 122 5 10 6.0 -mass 10.797737003058105 10.797737003058105 10.797737003058105 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10122 5 10 6.0 # Constrained floor node
uniaxialMaterial Elastic 300122 70466.89935
uniaxialMaterial Elastic 400122 53818.0074
section Aggregator 10122 99999 P 99999 Vy 99999 Vz 400122 My 300122 Mz 99999 T
element zeroLengthSection 10122 122 10122 10122 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (2, 2, 2)
node 222 8.3 10 6.0 -mass 10.797737003058105 10.797737003058105 10.797737003058105 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10222 8.3 10 6.0 # Constrained floor node
uniaxialMaterial Elastic 300222 70466.89935
uniaxialMaterial Elastic 400222 53818.0074
section Aggregator 10222 99999 P 99999 Vy 99999 Vz 400222 My 300222 Mz 99999 T
element zeroLengthSection 10222 222 10222 10222 -orient 0 0 1 0 1 0 -doRayleigh 0 

# Joint grid ids (x, y, z): (3, 2, 2)
node 322 13.3 10 6.0 -mass 6.957186544342508 6.957186544342508 6.957186544342508 0.0 0.0 0.0
# Joint flexibility model: elastic
node 10322 13.3 10 6.0 # Constrained floor node
uniaxialMaterial Elastic 300322 42301.8123
uniaxialMaterial Elastic 400322 36597.115
section Aggregator 10322 99999 P 99999 Vy 99999 Vz 400322 My 300322 Mz 99999 T
element zeroLengthSection 10322 322 10322 10322 -orient 0 0 1 0 1 0 -doRayleigh 0 
