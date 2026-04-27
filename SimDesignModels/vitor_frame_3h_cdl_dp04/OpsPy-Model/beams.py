import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.14727227, 0.00964285, 37.91832309, 0.07239148, 3.79183231, 0.31667313, -54.05857638, -0.01046539, -65.81027536, -0.08188651, -6.58102754, -0.32616817, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 46.05881574, 0.01000049, 56.0714608, 0.07468802, 5.60714608, 0.31531201, -79.80090685, -0.01107104, -97.14868584, -0.08469903, -9.71486858, -0.32532302, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29971743.92441675, 0.07, 0.00071458, 0.00023333, 12488226.63517365, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32718044557000003, 1001992, 0.32718044557000003, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 45.81991561, 0.01009334, 55.82823255, 0.09108637, 5.58282326, 0.39474693, -79.38184131, -0.01117516, -96.7209965, -0.10336225, -9.67209965, -0.40702281, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 45.81991561, 0.01009334, 55.82823255, 0.09084295, 5.58282326, 0.39234307, -79.38184131, -0.01117516, -96.7209965, -0.10308518, -9.67209965, -0.40458531, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29678247.85646028, 0.07, 0.00071458, 0.00023333, 12365936.60685845, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25933047187, 1101992, 0.25933047187, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 45.53329511, 0.00990316, 55.19424655, 0.07113672, 5.51942465, 0.30881338, -78.90716195, -0.01093389, -95.64915828, -0.08063055, -9.56491583, -0.31830722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.80218677, 0.00955112, 37.3375897, 0.0689854, 3.73375897, 0.31062283, -53.45793967, -0.01034381, -64.80028943, -0.07799251, -6.48002894, -0.31962994, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 31355769.99304084, 0.07, 0.00071458, 0.00023333, 13064904.16376702, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32596236567, 1201992, 0.32596236567, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.92400632, 0.00795147, 44.70454931, 0.08529115, 4.47045493, 0.36584111, -150.30942434, -0.00989618, -181.98228584, -0.117504, -18.19822858, -0.39805395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 72.58098916, 0.00843971, 87.87509083, 0.08708835, 8.78750908, 0.36646959, -150.35434759, -0.00980119, -182.03667522, -0.10342814, -18.20366752, -0.38280938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 31718665.1057253, 0.1, 0.00133333, 0.00052083, 13216110.46071888, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32802824845, 1011992, 0.32802824845, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 71.40717989, 0.00818417, 86.47292021, 0.10992996, 8.64729202, 0.46932343, -147.86814307, -0.00951065, -179.06588886, -0.13063351, -17.90658889, -0.49002699, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 71.40717989, 0.00818417, 86.47292021, 0.10877196, 8.64729202, 0.45853835, -147.86814307, -0.00951065, -179.06588886, -0.12925498, -17.90658889, -0.47902137, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 31653085.16020977, 0.1, 0.00133333, 0.00052083, 13188785.48342074, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25709159847, 1111992, 0.25709159847, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 72.64423482, 0.00851511, 88.24136585, 0.08868995, 8.82413659, 0.36843996, -150.44279595, -0.00991166, -182.74372123, -0.10535547, -18.27437212, -0.38510548, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 36.96473267, 0.00801614, 44.90127134, 0.08650464, 4.49012713, 0.36445905, -150.39817775, -0.01001113, -182.68952325, -0.11921737, -18.26895233, -0.39717177, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 30701117.80321854, 0.1, 0.00133333, 0.00052083, 12792132.41800773, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.3285267047, 1211992, 0.3285267047, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 61.6281503, 0.00871022, 74.64854391, 0.08658352, 7.46485439, 0.35769022, -143.90235189, -0.01035685, -174.30510216, -0.10555042, -17.43051022, -0.37665711, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 91.30899786, 0.00915453, 110.60016735, 0.08816845, 11.06001674, 0.35927515, -143.85540936, -0.01025498, -174.24824192, -0.09842117, -17.42482419, -0.36952787, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 31581209.57762219, 0.08, 0.00106667, 0.00026667, 13158837.32400925, 0.00073242)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.36885846935, 1021992, 0.36885846935, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 91.00893364, 0.00898753, 110.17888987, 0.10704723, 11.01788899, 0.44134338, -143.3582147, -0.01006854, -173.55492825, -0.11948661, -17.35549282, -0.45378276, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 91.00893364, 0.00898753, 110.17888987, 0.10725198, 11.01788899, 0.44154813, -143.3582147, -0.01006854, -173.55492825, -0.11971507, -17.35549282, -0.45401122, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 31738233.6330231, 0.08, 0.00106667, 0.00026667, 13224264.01375962, 0.00073242)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.29913596039, 1121992, 0.29913596039, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 95.9721002, 0.00915381, 116.9908668, 0.08979706, 11.69908668, 0.35795639, -150.93325709, -0.01030977, -183.98901909, -0.10029403, -18.39890191, -0.36845335, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 64.66952807, 0.00869352, 78.83274544, 0.08741843, 7.88327454, 0.35557775, -150.7630012, -0.01043292, -183.78147561, -0.1066675, -18.37814756, -0.37482682, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29510975.30678367, 0.08, 0.00106667, 0.00026667, 12296239.71115986, 0.00073242)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.37291263354, 1221992, 0.37291263354, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 30.39550872, 0.00945423, 36.92995353, 0.0716489, 3.69299535, 0.31566085, -52.74837411, -0.010249, -64.08825142, -0.08103961, -6.40882514, -0.32505155, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 30.3312188, 0.00941217, 36.85184253, 0.07321687, 3.68518425, 0.3183955, -77.89019532, -0.0109068, -94.63507653, -0.09046695, -9.46350765, -0.33564558, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 30628147.39201961, 0.07, 0.00071458, 0.00023333, 12761728.08000817, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32441825602, 1031992, 0.32441825602, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 30.84024896, 0.00955017, 37.56930556, 0.089522, 3.75693056, 0.39321483, -79.19910373, -0.01109659, -96.47961443, -0.11081606, -9.64796144, -0.4145089, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 30.84024896, 0.00955017, 37.56930556, 0.09030336, 3.75693056, 0.40108198, -79.19910373, -0.01109659, -96.47961443, -0.11179037, -9.64796144, -0.42256899, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29745625.3449407, 0.07, 0.00071458, 0.00023333, 12394010.56039196, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25834982493, 1131992, 0.25834982493, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 31.04018094, 0.00955672, 37.73708592, 0.07302671, 3.77370859, 0.31656799, -79.72965765, -0.0110857, -96.93129517, -0.09022849, -9.69312952, -0.33376977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 31.10565642, 0.00960285, 37.8166877, 0.07103331, 3.78166877, 0.30936556, -53.99014415, -0.01041558, -65.63849329, -0.08033635, -6.56384933, -0.3186686, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 30421946.96565408, 0.07, 0.00071458, 0.00023333, 12675811.2356892, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32688585632, 1231992, 0.32688585632, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.87224801, 0.00963083, 38.68275325, 0.06882709, 3.86827533, 0.30657068, -55.34252179, -0.01044356, -67.16818701, -0.07782133, -6.7168187, -0.31556493, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 31.8094962, 0.00957965, 38.60659255, 0.07063512, 3.86065925, 0.31257611, -81.74903273, -0.01110828, -99.21727708, -0.08724034, -9.92172771, -0.32918132, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 30969655.52404045, 0.07, 0.00071458, 0.00023333, 12904023.13501685, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32880755755, 1002992, 0.32880755755, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 30.46330777, 0.00960876, 37.18868309, 0.08975806, 3.71886831, 0.39053329, -78.18149319, -0.01117877, -95.44159801, -0.11111953, -9.5441598, -0.41189477, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 30.46330777, 0.00960876, 37.18868309, 0.09033761, 3.71886831, 0.39629749, -78.18149319, -0.01117877, -95.44159801, -0.1118422, -9.5441598, -0.41780208, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28991440.63727233, 0.07, 0.00071458, 0.00023333, 12079766.93219681, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25775832358, 1102992, 0.25775832358, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 31.27143383, 0.0096999, 38.06139524, 0.07120253, 3.80613952, 0.30804737, -80.30398939, -0.01125955, -97.74038172, -0.08794918, -9.77403817, -0.32479402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 31.33859238, 0.00974582, 38.14313592, 0.07064015, 3.81431359, 0.31525429, -54.38530193, -0.01057461, -66.19397381, -0.07988515, -6.61939738, -0.32449929, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 30043745.35783928, 0.07, 0.00071458, 0.00023333, 12518227.23243303, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32822403214, 1202992, 0.32822403214, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.12686327, 0.00873097, 75.4211107, 0.08846959, 7.54211107, 0.35894207, -145.03875716, -0.0104072, -176.07494705, -0.10788096, -17.6074947, -0.37835344, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 62.12686327, 0.00873097, 75.4211107, 0.08838295, 7.54211107, 0.35885543, -145.03875716, -0.0104072, -176.07494705, -0.10777505, -17.6074947, -0.37824753, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 30890468.59992172, 0.08, 0.00106667, 0.00026667, 12871028.58330072, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36972338201000005, 1012992, 0.36972338201000005, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 61.33717843, 0.00828661, 74.42965946, 0.10443807, 7.44296595, 0.44162599, -143.123112, -0.00989216, -173.67288094, -0.12742924, -17.36728809, -0.46461716, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 61.33717843, 0.00828661, 74.42965946, 0.10502335, 7.44296595, 0.44221127, -143.123112, -0.00989216, -173.67288094, -0.1281447, -17.36728809, -0.46533262, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 31029338.04291329, 0.08, 0.00106667, 0.00026667, 12928890.85121387, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.29657053029999997, 1112992, 0.29657053029999997, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 63.34559546, 0.00831151, 76.76309291, 0.08701805, 7.67630929, 0.35899116, -147.71405772, -0.00992241, -179.0019946, -0.10613454, -17.90019946, -0.37810765, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 63.34559546, 0.00831151, 76.76309291, 0.08626304, 7.67630929, 0.35823614, -147.71405772, -0.00992241, -179.0019946, -0.1052116, -17.90019946, -0.37718471, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 31446173.68989042, 0.08, 0.00106667, 0.00026667, 13102572.37078768, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36768341507, 1212992, 0.36768341507, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 62.05228248, 0.00869977, 74.97337589, 0.08349583, 7.49733759, 0.3541492, -144.92062616, -0.0103253, -175.09732351, -0.1017572, -17.50973235, -0.37241057, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 62.05228248, 0.00869977, 74.97337589, 0.08391059, 7.49733759, 0.35456396, -144.92062616, -0.0103253, -175.09732351, -0.10226421, -17.50973235, -0.37291758, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 32318505.91864565, 0.08, 0.00106667, 0.00026667, 13466044.13276902, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36947627586, 1022992, 0.36947627586, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 62.01478824, 0.00857942, 75.21463473, 0.10517108, 7.52146347, 0.4382357, -144.77330768, -0.01022491, -175.58830342, -0.1283001, -17.55883034, -0.46136471, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 62.01478824, 0.00857942, 75.21463473, 0.10417801, 7.52146347, 0.43724262, -144.77330768, -0.01022491, -175.58830342, -0.12708615, -17.55883034, -0.46015076, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 31183842.29657276, 0.08, 0.00106667, 0.00026667, 12993267.62357198, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.3002420424, 1122992, 0.3002420424, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 62.18741507, 0.00863384, 75.48998169, 0.08712809, 7.54899817, 0.35816413, -145.16781794, -0.01029698, -176.22079815, -0.10624961, -17.62207982, -0.37728565, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.18741507, 0.00863384, 75.48998169, 0.08752389, 7.54899817, 0.35855993, -145.16781794, -0.01029698, -176.22079815, -0.10673344, -17.62207982, -0.37776948, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 30909929.19547109, 0.08, 0.00106667, 0.00026667, 12879137.16477962, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36895462451, 1222992, 0.36895462451, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 30.67136882, 0.00962529, 37.27435641, 0.07094873, 3.72743564, 0.3126048, -53.2140649, -0.01043304, -64.67008476, -0.08023201, -6.46700848, -0.32188807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 30.60630778, 0.00958519, 37.19528892, 0.07188972, 3.71952889, 0.30918616, -78.56851163, -0.01110412, -95.4828825, -0.08879366, -9.54828825, -0.32609011, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 30547748.61781078, 0.07, 0.00071458, 0.00023333, 12728228.59075449, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32603478019, 1032992, 0.32603478019, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 31.58592121, 0.00959959, 38.24322487, 0.08675158, 3.82432249, 0.3922428, -81.16881121, -0.01110334, -98.2766049, -0.10730667, -9.82766049, -0.41279789, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 31.58592121, 0.00959959, 38.24322487, 0.08593911, 3.82432249, 0.38385429, -81.16881121, -0.01110334, -98.2766049, -0.10629359, -9.82766049, -0.40420876, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 31706270.04486708, 0.07, 0.00071458, 0.00023333, 13210945.85202795, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.26045746172, 1132992, 0.26045746172, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 31.06398477, 0.00935518, 37.59717637, 0.0712715, 3.75971764, 0.31527241, -79.84449355, -0.01082269, -96.63691017, -0.08802817, -9.66369102, -0.33202908, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 31.12513386, 0.00940195, 37.67118597, 0.06986056, 3.7671186, 0.31370051, -54.04897896, -0.0101829, -65.41623715, -0.0789975, -6.54162371, -0.32283745, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 31817692.48333952, 0.07, 0.00071458, 0.00023333, 13257371.86805813, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32583593812, 1232992, 0.32583593812, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 31.05427131, 0.00971735, 37.68523555, 0.05595417, 3.76852355, 0.29637337, -31.05427131, -0.00971735, -37.68523555, -0.05595417, -3.76852355, -0.29637337, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 31.01142269, 0.00969041, 37.63323754, 0.05675575, 3.76332375, 0.29976388, -45.97124024, -0.01016921, -55.78739877, -0.06173025, -5.57873988, -0.30473839, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 31009349.11593829, 0.07, 0.00071458, 0.00023333, 12920562.13164096, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.327093593, 1003992, 0.327093593, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 31.18290814, 0.00945536, 37.82521197, 0.07008768, 3.7825212, 0.37863032, -46.25089401, -0.00992781, -56.10284525, -0.07635176, -5.61028453, -0.3848944, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 31.18290814, 0.00945536, 37.82521197, 0.06985355, 3.7825212, 0.37557743, -46.25089401, -0.00992781, -56.10284525, -0.07609526, -5.61028453, -0.38181915, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 31142604.1800382, 0.07, 0.00071458, 0.00023333, 12976085.07501592, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25808578790000003, 1103992, 0.25808578790000003, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 31.28295128, 0.0092967, 37.95291986, 0.05718164, 3.79529199, 0.30063285, -46.40827408, -0.00976591, -56.30317585, -0.06222485, -5.63031759, -0.30567606, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 31.31834031, 0.00933322, 37.99585434, 0.05669761, 3.79958543, 0.30148912, -31.31834031, -0.00933322, -37.99585434, -0.05669761, -3.79958543, -0.30148912, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 31090421.43459528, 0.07, 0.00071458, 0.00023333, 12954342.2644147, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32531822687, 1203992, 0.32531822687, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 35.68501678, 0.00822142, 43.35172924, 0.09430302, 4.33517292, 0.40000005, -144.62451547, -0.01052274, -175.69622778, -0.13029377, -17.56962278, -0.4359908, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 35.68501678, 0.00822142, 43.35172924, 0.09446437, 4.33517292, 0.4001614, -144.62451547, -0.01052274, -175.69622778, -0.13051827, -17.56962278, -0.4362153, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 30664450.2372281, 0.08, 0.00106667, 0.00026667, 12776854.26551171, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32712126831, 1013992, 0.32712126831, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 35.72110959, 0.00802432, 43.49144505, 0.11954733, 4.3491445, 0.50729654, -144.85065172, -0.01032578, -176.35969969, -0.16549512, -17.63596997, -0.55324433, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 35.72110959, 0.00802432, 43.49144505, 0.12091194, 4.3491445, 0.50866115, -144.85065172, -0.01032578, -176.35969969, -0.1673938, -17.63596997, -0.55514301, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 29932687.66769718, 0.08, 0.00106667, 0.00026667, 12471953.19487382, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25789865858, 1113992, 0.25789865858, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 36.32214274, 0.00816557, 44.0592704, 0.09519689, 4.40592704, 0.39999317, -147.34974943, -0.01044937, -178.73732008, -0.13154181, -17.87373201, -0.43633808, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 36.32214274, 0.00816557, 44.0592704, 0.09400583, 4.40592704, 0.3988021, -147.34974943, -0.01044937, -178.73732008, -0.1298846, -17.87373201, -0.43468087, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 31141826.93863978, 0.08, 0.00106667, 0.00026667, 12975761.22443324, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32808800299, 1213992, 0.32808800299, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 52.47531714, 0.01001813, 63.46408473, 0.08820292, 6.34640847, 0.36108515, -122.14090223, -0.01206637, -147.71822241, -0.1076407, -14.77182224, -0.38052294, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 52.47531714, 0.01001813, 63.46408473, 0.08854324, 6.34640847, 0.36142548, -122.14090223, -0.01206637, -147.71822241, -0.10805672, -14.77182224, -0.38093896, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 32037394.66070402, 0.07, 0.00071458, 0.00023333, 13348914.44196001, 0.00060032)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36645844202, 1023992, 0.36645844202, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 54.77420466, 0.00984049, 66.38530118, 0.10866753, 6.63853012, 0.440984, -127.35343139, -0.01191316, -154.34995271, -0.1327209, -15.43499527, -0.46503738, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 54.77420466, 0.00984049, 66.38530118, 0.10850364, 6.63853012, 0.44082012, -127.35343139, -0.01191316, -154.34995271, -0.13252057, -15.43499527, -0.46483705, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 31404233.76935945, 0.07, 0.00071458, 0.00023333, 13085097.40389977, 0.00060032)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30091797123999997, 1123992, 0.30091797123999997, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 52.43031462, 0.01051002, 63.81707961, 0.09213022, 6.38170796, 0.36259759, -121.93197033, -0.01271367, -148.41303766, -0.11248751, -14.84130377, -0.38295488, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 52.43031462, 0.01051002, 63.81707961, 0.09188255, 6.38170796, 0.36234992, -121.93197033, -0.01271367, -148.41303766, -0.11218474, -14.84130377, -0.38265211, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 30030068.21217262, 0.07, 0.00071458, 0.00023333, 12512528.42173859, 0.00060032)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36973036581999996, 1223992, 0.36973036581999996, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 31.45922555, 0.00957135, 38.23244188, 0.0576212, 3.82324419, 0.30247148, -31.45922555, -0.00957135, -38.23244188, -0.0576212, -3.82324419, -0.30247148, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 31.41869332, 0.00953697, 38.18318299, 0.05817398, 3.8183183, 0.30238666, -46.59952162, -0.01001926, -56.63246537, -0.06330211, -5.66324654, -0.30751479, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 30542492.59308296, 0.07, 0.00071458, 0.00023333, 12726038.58045123, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32704670125, 1033992, 0.32704670125, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 30.70898477, 0.00938018, 37.28030814, 0.07188362, 3.72803081, 0.38495093, -45.54317389, -0.00984976, -55.28882081, -0.07832357, -5.52888208, -0.39139087, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 30.70898477, 0.00938018, 37.28030814, 0.0711435, 3.72803081, 0.37548844, -45.54317389, -0.00984976, -55.28882081, -0.07751275, -5.52888208, -0.38185769, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 30890076.32629398, 0.07, 0.00071458, 0.00023333, 12870865.13595582, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25656326026, 1133992, 0.25656326026, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 31.28536044, 0.00953695, 37.92684775, 0.05541938, 3.79268477, 0.29362656, -46.3993517, -0.01001051, -56.24934867, -0.06027566, -5.62493487, -0.29848284, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 31.32649646, 0.00956817, 37.97671643, 0.05500471, 3.79767164, 0.29518596, -31.32649646, -0.00956817, -37.97671643, -0.05500471, -3.79767164, -0.29518596, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 31326940.58911995, 0.07, 0.00071458, 0.00023333, 13052891.91213331, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32682257889, 1233992, 0.32682257889, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 47.40849397, 0.00976999, 57.76646017, 0.12275362, 5.77664602, 0.50637923, -128.84707985, -0.01229598, -156.99802045, -0.15579088, -15.69980205, -0.53941648, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 47.40849397, 0.00976999, 57.76646017, 0.12337493, 5.77664602, 0.50700053, -128.84707985, -0.01229598, -156.99802045, -0.15657997, -15.69980205, -0.54020557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29662208.63092605, 0.07, 0.00071458, 0.00023333, 12359253.59621919, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.26067081787, 6200992, 0.26067081787, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 45.54407832, 0.00992042, 55.26131581, 0.12237808, 5.52613158, 0.5086703, -123.98799395, -0.01237757, -150.44194423, -0.15520445, -15.04419442, -0.54149667, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 45.54407832, 0.00992042, 55.26131581, 0.12294826, 5.52613158, 0.50924048, -123.98799395, -0.01237757, -150.44194423, -0.15592861, -15.04419442, -0.54222083, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 31053104.855289, 0.07, 0.00071458, 0.00023333, 12938793.68970375, 0.00060032)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.2588713801, 6201992, 0.2588713801, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 31.38533616, 0.00935853, 38.14991569, 0.08770737, 3.81499157, 0.39001042, -80.65722144, -0.01087274, -98.04152428, -0.10856847, -9.80415243, -0.41087152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 31.38533616, 0.00935853, 38.14991569, 0.08754482, 3.81499157, 0.38836222, -80.65722144, -0.01087274, -98.04152428, -0.10836578, -9.80415243, -0.40918318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 30480299.68295911, 0.07, 0.00071458, 0.00023333, 12700124.86789963, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25849740314, 6202992, 0.25849740314, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 63.10646668, 0.00857848, 76.79092689, 0.07900425, 7.67909269, 0.32287511, -147.56951642, -0.01005262, -179.56955195, -0.09614222, -17.95695519, -0.34001307, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 93.34804496, 0.0088744, 113.59030656, 0.08366565, 11.35903066, 0.32952177, -217.44353296, -0.01080339, -264.5955529, -0.1022294, -26.45955529, -0.34808553, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 30122060.45803193, 0.1, 0.00133333, 0.00052083, 12550858.52417997, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.37043385026, 2001992, 0.37043385026, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 123.03415873, 0.00664284, 149.28745879, 0.06888067, 14.92874588, 0.28869783, -188.24822335, -0.00718582, -228.4170443, -0.07599778, -22.84170443, -0.29581494, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 122.94122325, 0.00656951, 149.17469253, 0.07076817, 14.91746925, 0.28997435, -277.8961621, -0.00771219, -337.19425788, -0.08547215, -33.71942579, -0.30467833, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 31047106.54278379, 0.125, 0.00260417, 0.00065104, 12936294.39282658, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.40751218776000003, 2101992, 0.40751218776000003, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 127.6513512, 0.0067321, 155.28630328, 0.06928354, 15.52863033, 0.28793195, -195.17008204, -0.00729497, -237.42201132, -0.07645367, -23.74220113, -0.29510208, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 127.66245665, 0.00664926, 155.29981292, 0.07198564, 15.52998129, 0.29660987, -288.10754119, -0.00783512, -350.47929065, -0.08697313, -35.04792906, -0.31159735, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 30221003.14469056, 0.125, 0.00260417, 0.00065104, 12592084.64362107, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41267515979, 2201992, 0.41267515979, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.84355024, 0.00870448, 76.42675476, 0.07784728, 7.64267548, 0.31869728, -146.92635624, -0.0101853, -178.68348547, -0.09470657, -17.86834855, -0.33555657, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 92.84933976, 0.00901031, 112.91809091, 0.08221674, 11.29180909, 0.3232872, -216.3851111, -0.01094944, -263.15527618, -0.10043815, -26.31552762, -0.34150861, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 30315168.29389792, 0.1, 0.00133333, 0.00052083, 12631320.12245747, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.37115707253, 2301992, 0.37115707253, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 91.57608833, 0.00889708, 111.17961524, 0.08302889, 11.11796152, 0.32856941, -213.46313123, -0.0107897, -259.15879607, -0.1014096, -25.91587961, -0.34695012, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 61.81013696, 0.00853284, 75.04172072, 0.08206124, 7.50417207, 0.33248969, -213.42153478, -0.01088858, -259.10829514, -0.10935648, -25.91082951, -0.35978493, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 30868859.72900023, 0.1, 0.00133333, 0.00052083, 12862024.88708343, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36895997808, 2011992, 0.36895997808, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 123.77957842, 0.00667352, 149.86784503, 0.07005281, 14.9867845, 0.29045617, -279.96926254, -0.00781566, -338.976676, -0.08458316, -33.8976676, -0.30498652, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 123.64390973, 0.00661416, 149.70358227, 0.07176698, 14.97035823, 0.28978145, -368.48310433, -0.00829276, -446.14604023, -0.09248547, -44.61460402, -0.31049994, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 31707297.52076837, 0.125, 0.00260417, 0.00065104, 13211373.96698682, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.40992607864, 2111992, 0.40992607864, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 121.73972924, 0.00679313, 148.01517495, 0.07304996, 14.80151749, 0.29692952, -275.44916363, -0.00797368, -334.90017103, -0.08822656, -33.4900171, -0.31210613, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 121.54903854, 0.00673531, 147.7833269, 0.07547914, 14.77833269, 0.30184496, -362.46813161, -0.00847177, -440.70070015, -0.0973049, -44.07007002, -0.32367072, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30399390.76208419, 0.125, 0.00260417, 0.00065104, 12666412.81753508, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40963315096999997, 2211992, 0.40963315096999997, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 93.37190083, 0.0084984, 112.95672379, 0.08177872, 11.29567238, 0.32943889, -217.41586245, -0.01030151, -263.01899505, -0.09988054, -26.30189951, -0.34754071, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 62.86555699, 0.00815102, 76.05165252, 0.08025365, 7.60516525, 0.32807905, -217.15670003, -0.01040023, -262.70547313, -0.10695876, -26.27054731, -0.35478416, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 31954731.25136387, 0.1, 0.00133333, 0.00052083, 13314471.35473495, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36725610555, 2311992, 0.36725610555, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 62.86981674, 0.00827857, 76.32266477, 0.08286337, 7.63226648, 0.3335534, -217.11552254, -0.01060095, -263.57377998, -0.11048356, -26.357378, -0.36117359, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 63.02619319, 0.00835452, 76.51250257, 0.07899309, 7.65125026, 0.32142578, -147.4147812, -0.00977977, -178.95851319, -0.09612948, -17.89585132, -0.33856217, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 30892049.50679598, 0.1, 0.00133333, 0.00052083, 12871687.29449832, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.36836472679000004, 2021992, 0.36836472679000004, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 124.94619037, 0.00664692, 151.67975027, 0.0725921, 15.16797503, 0.29137735, -372.06306073, -0.00836554, -451.66989059, -0.09358217, -45.16698906, -0.31236742, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 125.16590919, 0.00678446, 151.94648026, 0.06907486, 15.19464803, 0.291718, -191.5144448, -0.00733997, -232.4909873, -0.07621005, -23.24909873, -0.29885318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 30896970.98727249, 0.125, 0.00260417, 0.00065104, 12873737.91136354, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.41147489316, 2121992, 0.41147489316, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 123.12223378, 0.00660215, 149.74436051, 0.07427665, 14.97443605, 0.29529861, -366.6281232, -0.0083268, -445.90235387, -0.09577812, -44.59023539, -0.31680008, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 123.36260393, 0.00673972, 150.03670475, 0.07023851, 15.00367047, 0.29162597, -188.74800685, -0.00729674, -229.56007796, -0.07750285, -22.9560078, -0.29889032, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 30292817.71253268, 0.125, 0.00260417, 0.00065104, 12622007.38022195, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.4090944823, 2221992, 0.4090944823, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 62.05930442, 0.00839971, 75.14658306, 0.07975153, 7.51465831, 0.32402162, -214.39550755, -0.01069631, -259.60796638, -0.10624937, -25.96079664, -0.35051946, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 62.23557902, 0.00846399, 75.36003105, 0.07724353, 7.53600311, 0.32356428, -145.57835427, -0.00987437, -176.27841615, -0.09395159, -17.62784162, -0.34027233, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 31677822.95376528, 0.1, 0.00133333, 0.00052083, 13199092.8974022, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.36825344781, 2321992, 0.36825344781, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 35.74446588, 0.00790679, 43.70881331, 0.08943188, 4.37088133, 0.36540041, -145.24016219, -0.00995831, -177.60162243, -0.12338956, -17.76016224, -0.39935809, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 70.04863747, 0.00831718, 85.65641539, 0.09573654, 8.56564154, 0.37901556, -213.93846597, -0.01070945, -261.60683163, -0.12471811, -26.16068316, -0.40799713, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 28360738.55069158, 0.1, 0.00133333, 0.00052083, 11816974.39612149, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32527512853, 2002992, 0.32527512853, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 80.40769556, 0.00636787, 98.1102989, 0.0781741, 9.81102989, 0.32645988, -188.82011285, -0.00734959, -230.39085476, -0.09512668, -23.03908548, -0.34341246, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 80.2809531, 0.00631003, 97.95565275, 0.08003539, 9.79556527, 0.32491868, -278.37299883, -0.007915, -339.65975433, -0.10664666, -33.96597543, -0.35152995, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29173557.93220596, 0.125, 0.00260417, 0.00065104, 12155649.13841915, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36697600785, 2102992, 0.36697600785, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 81.31464474, 0.00641524, 99.06343842, 0.07726866, 9.90634384, 0.32536128, -190.98219907, -0.00739445, -232.66846184, -0.09400679, -23.26684618, -0.34209941, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 81.18857287, 0.00635789, 98.90984845, 0.07886572, 9.89098485, 0.32165392, -281.58695013, -0.00795802, -343.04978621, -0.10505919, -34.30497862, -0.34784739, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29722218.62672523, 0.125, 0.00260417, 0.00065104, 12384257.76113551, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36862097021, 2202992, 0.36862097021, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.87990649, 0.00802728, 43.55541482, 0.08694599, 4.35554148, 0.36740279, -145.74522466, -0.00999332, -176.92336295, -0.11979815, -17.69233629, -0.40025496, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 70.12999388, 0.00843944, 85.13235607, 0.09164459, 8.51323561, 0.36820826, -214.57339172, -0.01073131, -260.47540254, -0.11924398, -26.04754025, -0.39580765, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 30906986.8083689, 0.1, 0.00133333, 0.00052083, 12877911.17015371, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32635708449, 2302992, 0.32635708449, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 70.39703805, 0.00822278, 85.6958135, 0.0923906, 8.56958135, 0.36889657, -215.11612666, -0.01051792, -261.86544179, -0.12028605, -26.18654418, -0.39679202, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 70.39703805, 0.00822278, 85.6958135, 0.09327979, 8.56958135, 0.37676532, -215.11612666, -0.01051792, -261.86544179, -0.1214457, -26.18654418, -0.40493123, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29990435.84428697, 0.1, 0.00133333, 0.00052083, 12496014.93511957, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32506283072000003, 2012992, 0.32506283072000003, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 82.36880099, 0.0064727, 100.07240955, 0.07710506, 10.00724096, 0.32213842, -285.88559992, -0.00806863, -347.33127711, -0.1026582, -34.73312771, -0.34769156, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 122.36068838, 0.00666591, 148.6597932, 0.08036375, 14.86597932, 0.32372097, -376.74709664, -0.00850024, -457.72172596, -0.10461387, -45.7721726, -0.34797109, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 30641343.43715141, 0.125, 0.00260417, 0.00065104, 12767226.43214642, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.37142331288, 2112992, 0.37142331288, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 83.05267465, 0.00628876, 100.66289132, 0.07652338, 10.06628913, 0.32333604, -287.95201572, -0.00783527, -349.00841649, -0.10189221, -34.90084165, -0.34870487, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 123.5695804, 0.00647134, 149.77086885, 0.0801662, 14.97708688, 0.32857223, -379.72302773, -0.00824578, -460.23825283, -0.10435552, -46.02382528, -0.35276155, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 31390230.6458872, 0.125, 0.00260417, 0.00065104, 13079262.76911967, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36992541151, 2212992, 0.36992541151, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 71.2885143, 0.00832408, 86.45167377, 0.09217955, 8.64516738, 0.37506346, -218.00826985, -0.01059055, -264.37891164, -0.11995134, -26.43789116, -0.40283525, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 71.2885143, 0.00832408, 86.45167377, 0.09146292, 8.64516738, 0.3686458, -218.00826985, -0.01059055, -264.37891164, -0.11901674, -26.43789116, -0.39619962, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 31221802.85480453, 0.1, 0.00133333, 0.00052083, 13009084.52283522, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32671125001, 2312992, 0.32671125001, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 70.9857519, 0.0083301, 86.31962601, 0.09402609, 8.6319626, 0.37778867, -216.99993797, -0.01063499, -263.87483384, -0.1223961, -26.38748338, -0.40615868, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 36.21618724, 0.00792662, 44.03936923, 0.0885661, 4.40393692, 0.37096292, -147.28965456, -0.00990654, -179.10619462, -0.12210558, -17.91061946, -0.4045024, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 30350463.45556976, 0.1, 0.00133333, 0.00052083, 12646026.43982073, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32640522434, 2022992, 0.32640522434, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 122.3492933, 0.00663718, 148.14668266, 0.07779789, 14.81466827, 0.31917838, -376.91813482, -0.00842733, -456.39144946, -0.10123215, -45.63914495, -0.34261264, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 82.50312433, 0.00649842, 99.89893565, 0.07282378, 9.98989357, 0.31836401, -193.92634491, -0.00745346, -234.81577952, -0.08853064, -23.48157795, -0.33407087, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 31685989.07868898, 0.125, 0.00260417, 0.00065104, 13202495.44945374, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.37117336974, 2122992, 0.37117336974, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 121.03212092, 0.00641921, 147.10165676, 0.08133322, 14.71016568, 0.32753283, -371.98148888, -0.00820439, -452.10389511, -0.10590411, -45.21038951, -0.35210372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 81.47032632, 0.00629471, 99.01850755, 0.07561837, 9.90185076, 0.32182778, -191.31741139, -0.00724675, -232.5259441, -0.09198911, -23.25259441, -0.33819852, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 30517804.57585022, 0.125, 0.00260417, 0.00065104, 12715751.90660426, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36736782088000003, 2222992, 0.36736782088000003, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 69.79025138, 0.00847962, 84.88116901, 0.09241445, 8.4881169, 0.37032122, -213.49775127, -0.01080476, -259.66289491, -0.12026905, -25.96628949, -0.39817582, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 35.73162555, 0.00806195, 43.45796279, 0.08707731, 4.34579628, 0.3639218, -145.04860512, -0.01005469, -176.41282161, -0.119994, -17.64128216, -0.39683849, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 30290831.12459688, 0.1, 0.00133333, 0.00052083, 12621179.6352487, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32625305613, 2322992, 0.32625305613, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 36.26010656, 0.00810308, 44.05933222, 0.09525766, 4.40593322, 0.40057246, -147.08500231, -0.01039941, -178.72167499, -0.13166335, -17.8721675, -0.43697815, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 36.26010656, 0.00810308, 44.05933222, 0.09456195, 4.40593322, 0.39987675, -147.08500231, -0.01039941, -178.72167499, -0.13069535, -17.8721675, -0.43601016, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 30598711.77179522, 0.08, 0.00106667, 0.00026667, 12749463.23824801, 0.00073242)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32753079594, 2003992, 0.32753079594, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 73.34625951, 0.00755567, 89.3437984, 0.07587495, 8.93437984, 0.31515365, -171.9591647, -0.00877404, -209.46514582, -0.09228861, -20.94651458, -0.33156731, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 73.34625951, 0.00755567, 89.3437984, 0.07636941, 8.93437984, 0.31977646, -171.9591647, -0.00877404, -209.46514582, -0.09289305, -20.94651458, -0.3363001, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 29768602.56592741, 0.1125, 0.00189844, 0.00058594, 12403584.40246976, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.37310561717, 2103992, 0.37310561717, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 70.54687122, 0.0073163, 85.35831088, 0.0749994, 8.53583109, 0.32007418, -165.48352802, -0.00844499, -200.2270857, -0.09118189, -20.02270857, -0.33625667, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 70.54687122, 0.0073163, 85.35831088, 0.0757873, 8.53583109, 0.32768359, -165.48352802, -0.00844499, -200.2270857, -0.09214503, -20.02270857, -0.34404132, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 31905972.6126097, 0.1125, 0.00189844, 0.00058594, 13294155.25525404, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36720446134999996, 2203992, 0.36720446134999996, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 36.34575933, 0.00809882, 44.1296428, 0.09357815, 4.41296428, 0.39875373, -147.45194533, -0.01038478, -179.03056088, -0.12931783, -17.90305609, -0.4344934, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 36.34575933, 0.00809882, 44.1296428, 0.09436826, 4.41296428, 0.39954384, -147.45194533, -0.01038478, -179.03056088, -0.13041716, -17.90305609, -0.43559274, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 30844281.3588285, 0.08, 0.00106667, 0.00026667, 12851783.89951188, 0.00073242)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32768021831, 2303992, 0.32768021831, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 35.03125371, 0.00798793, 42.66528779, 0.10001935, 4.26652878, 0.40842331, -142.00456747, -0.01027217, -172.95029714, -0.13832157, -17.29502971, -0.44672554, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 35.03125371, 0.00798793, 42.66528779, 0.09883063, 4.26652878, 0.4072346, -142.00456747, -0.01027217, -172.95029714, -0.13666764, -17.29502971, -0.44507161, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 29822153.94144927, 0.08, 0.00106667, 0.00026667, 12425897.47560386, 0.00073242)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32425004643, 2013992, 0.32425004643, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 72.2218682, 0.00750886, 88.01369301, 0.07833705, 8.8013693, 0.32439291, -169.31716507, -0.00871986, -206.33956668, -0.09530137, -20.63395667, -0.34135724, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 106.94023178, 0.00775888, 130.32347356, 0.08161921, 13.03234736, 0.32276239, -249.68052323, -0.00934168, -304.27494431, -0.09962972, -30.42749443, -0.3407729, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29612420.51678712, 0.1125, 0.00189844, 0.00058594, 12338508.5486613, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.37115367939, 2113992, 0.37115367939, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 71.5525697, 0.00719576, 86.86777982, 0.07659809, 8.68677798, 0.32233785, -167.78584217, -0.00833965, -203.69895387, -0.09317816, -20.36989539, -0.33891793, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 106.10729077, 0.00742723, 128.81864076, 0.08029579, 12.88186408, 0.32505582, -247.61129826, -0.00891925, -300.61036003, -0.09799494, -30.061036, -0.34275496, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 30875870.15686821, 0.1125, 0.00189844, 0.00058594, 12864945.89869509, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36712699587, 2213992, 0.36712699587, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 35.99833843, 0.00812174, 43.60868685, 0.09496185, 4.36086868, 0.40063646, -146.03960501, -0.010372, -176.91359323, -0.13119839, -17.69135932, -0.436873, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 35.99833843, 0.00812174, 43.60868685, 0.09470262, 4.36086868, 0.40037723, -146.03960501, -0.010372, -176.91359323, -0.13083771, -17.69135932, -0.43651231, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 31547655.14694951, 0.08, 0.00106667, 0.00026667, 13144856.31122896, 0.00073242)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32714526219, 2313992, 0.32714526219, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 36.29355522, 0.00806011, 44.18662137, 0.09515734, 4.41866214, 0.40070161, -147.18467154, -0.01038036, -179.19416586, -0.13156449, -17.91941659, -0.43710876, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 36.29355522, 0.00806011, 44.18662137, 0.0964576, 4.41866214, 0.40200187, -147.18467154, -0.01038036, -179.19416586, -0.13337363, -17.91941659, -0.4389179, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 29946517.14969706, 0.08, 0.00106667, 0.00026667, 12477715.47904044, 0.00073242)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32728481448999996, 2023992, 0.32728481448999996, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 103.68133055, 0.0076783, 126.0001842, 0.08113042, 12.60001842, 0.32697517, -242.27733877, -0.00920504, -294.43091781, -0.09899408, -29.44309178, -0.34483883, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 70.1140606, 0.00742684, 85.20709085, 0.07741471, 8.52070908, 0.32449253, -164.38057999, -0.00859465, -199.76579437, -0.09414894, -19.97657944, -0.34122676, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 30552525.07900832, 0.1125, 0.00189844, 0.00058594, 12730218.78292014, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36763503297, 2123992, 0.36763503297, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 108.51416657, 0.00747695, 131.93052736, 0.0825886, 13.19305274, 0.33362822, -252.98871401, -0.00899983, -307.5813556, -0.10081751, -30.75813556, -0.35185713, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 73.11238967, 0.00724686, 88.88937206, 0.07809795, 8.88893721, 0.32443345, -171.36697058, -0.00841479, -208.34638937, -0.09502429, -20.83463894, -0.34135979, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 30410790.82074495, 0.1125, 0.00189844, 0.00058594, 12671162.84197706, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36956480007, 2223992, 0.36956480007, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 35.13731491, 0.00816518, 42.78635064, 0.09855528, 4.27863506, 0.40567898, -142.33019382, -0.01048085, -173.31402797, -0.13624659, -17.3314028, -0.44337029, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 35.13731491, 0.00816518, 42.78635064, 0.09855785, 4.27863506, 0.40568156, -142.33019382, -0.01048085, -173.31402797, -0.13625017, -17.3314028, -0.44337387, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 29887219.23383907, 0.08, 0.00106667, 0.00026667, 12453008.01409961, 0.00073242)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32560170113, 2323992, 0.32560170113, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
