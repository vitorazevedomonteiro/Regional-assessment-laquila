import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 30.09149384, 0.00982218, 36.79711573, 0.0746752, 3.67971157, 0.3148087, -77.09938386, -0.01142723, -94.28029616, -0.09229457, -9.42802962, -0.33242807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 44.48408406, 0.01024389, 54.39696674, 0.07627762, 5.43969667, 0.31915929, -77.02535453, -0.01135626, -94.18977005, -0.08651652, -9.418977, -0.32939819, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 28351980.16668099, 0.07, 0.00071458, 0.00023333, 11813325.06945041, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32598042945, 1001992, 0.32598042945, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 46.60962089, 0.01023957, 56.99027079, 0.09137746, 5.69902708, 0.39089316, -80.73260865, -0.01136827, -98.71295112, -0.10372023, -9.87129511, -0.40323594, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 46.60962089, 0.01023957, 56.99027079, 0.09202239, 5.69902708, 0.39721625, -80.73260865, -0.01136827, -98.71295112, -0.1044543, -9.87129511, -0.40964816, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28391928.83897668, 0.07, 0.00071458, 0.00023333, 11829970.34957362, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.26122593511000003, 1101992, 0.26122593511000003, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 45.71405756, 0.00982666, 55.77737002, 0.07449139, 5.577737, 0.31416176, -79.18710814, -0.01089937, -96.61904602, -0.08450142, -9.6619046, -0.32417178, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.83073055, 0.00942326, 37.61768606, 0.07344096, 3.76176861, 0.31493097, -79.19066408, -0.01097585, -96.62338475, -0.0908016, -9.66233847, -0.33229161, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29180830.00051164, 0.07, 0.00071458, 0.00023333, 12158679.16687985, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.3255594557, 1201992, 0.3255594557, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 72.18162034, 0.00725472, 88.29458509, 0.07907453, 8.82945851, 0.32179624, -169.06293418, -0.0084723, -206.80252893, -0.09626599, -20.68025289, -0.33898769, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 107.11622045, 0.00748897, 131.02756903, 0.08421973, 13.1027569, 0.33616408, -249.53314229, -0.00907931, -305.23594735, -0.10287622, -30.52359473, -0.35482057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28228844.11903281, 0.1125, 0.00189844, 0.00058594, 11762018.38293034, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36824211250000005, 1011992, 0.36824211250000005, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 108.05689817, 0.00747832, 132.31914082, 0.10184138, 13.23191408, 0.40292466, -251.5198894, -0.00908574, -307.99417924, -0.12443665, -30.79941792, -0.42551993, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 108.05689817, 0.00747832, 132.31914082, 0.10130066, 13.23191408, 0.39830753, -251.5198894, -0.00908574, -307.99417924, -0.12377566, -30.79941792, -0.42078253, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27804687.14489653, 0.1125, 0.00189844, 0.00058594, 11585286.31037355, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30081733008, 1111992, 0.30081733008, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 108.19783346, 0.00775671, 132.27213643, 0.08381755, 13.22721364, 0.33022342, -252.35721145, -0.00938418, -308.50735579, -0.10236216, -30.85073558, -0.34876804, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 73.00434482, 0.00750887, 89.24800386, 0.0801566, 8.92480039, 0.32921246, -171.07600404, -0.00875384, -209.14086561, -0.09755958, -20.91408656, -0.34661543, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 28458701.92460075, 0.1125, 0.00189844, 0.00058594, 11857792.46858365, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.37203135894, 1211992, 0.37203135894, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 97.35871897, 0.00897296, 118.59317105, 0.07306035, 11.8593171, 0.28947494, -148.58215536, -0.00982878, -180.98871012, -0.08068567, -18.09887101, -0.29710026, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 144.1426113, 0.00937246, 175.58087799, 0.07882007, 17.5580878, 0.30271757, -219.38431795, -0.01049355, -267.23319923, -0.08727686, -26.72331992, -0.31117436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29769884.12732735, 0.1, 0.00133333, 0.00052083, 12404118.3863864, 0.00127345)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.41235885181, 1021992, 0.41235885181, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 146.95546957, 0.00972304, 179.42870368, 0.09366775, 17.94287037, 0.35630791, -223.69147431, -0.01090106, -273.12131612, -0.10371279, -27.31213161, -0.36635295, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 146.95546957, 0.00972304, 179.42870368, 0.09350157, 17.94287037, 0.35491001, -223.69147431, -0.01090106, -273.12131612, -0.10352905, -27.31213161, -0.36493749, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28929992.6734251, 0.1, 0.00133333, 0.00052083, 12054163.61392713, 0.00127345)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.35009292398999997, 1121992, 0.35009292398999997, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 143.440459, 0.00918854, 174.53775199, 0.0778121, 17.4537752, 0.29554656, -218.26089461, -0.01028363, -265.57894584, -0.08615584, -26.55789458, -0.3038903, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 96.83068973, 0.00880096, 117.82317922, 0.07363286, 11.78231792, 0.29614848, -147.76213024, -0.00963752, -179.79634353, -0.08131756, -17.97963435, -0.30383318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 30136244.03734203, 0.1, 0.00133333, 0.00052083, 12556768.34889251, 0.00127345)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.40989718973, 1221992, 0.40989718973, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 53.12532309, 0.01019296, 64.81196298, 0.07896319, 6.4811963, 0.29641358, -81.18466791, -0.01111054, -99.04387183, -0.08714492, -9.90438718, -0.30459531, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 53.12532309, 0.01019296, 64.81196298, 0.0782957, 6.4811963, 0.29077289, -81.18466791, -0.01111054, -99.04387183, -0.08640693, -9.90438718, -0.29888411, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 29226320.90910134, 0.07, 0.00071458, 0.00023333, 12177633.71212556, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.36744154217, 1031992, 0.36744154217, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 53.4943992, 0.01010809, 65.18287506, 0.09248163, 6.51828751, 0.35546615, -81.74995936, -0.01101422, -99.6122485, -0.10208882, -9.96122485, -0.36507333, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 53.4943992, 0.01010809, 65.18287506, 0.09199055, 6.51828751, 0.35127127, -81.74995936, -0.01101422, -99.6122485, -0.10154587, -9.96122485, -0.36082658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29657713.22627781, 0.07, 0.00071458, 0.00023333, 12357380.51094909, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.29948274243, 1131992, 0.29948274243, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 54.26151405, 0.01026691, 66.46173659, 0.07975252, 6.64617366, 0.29476298, -82.88823064, -0.01122517, -101.52491776, -0.08805049, -10.15249178, -0.30306096, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 54.26151405, 0.01026691, 66.46173659, 0.0794602, 6.64617366, 0.29233122, -82.88823064, -0.01122517, -101.52491776, -0.08772729, -10.15249178, -0.30059832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 27701980.27194299, 0.07, 0.00071458, 0.00023333, 11542491.77997625, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.36964687103, 1231992, 0.36964687103, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.23580515, 0.00968229, 38.27944556, 0.07589224, 3.82794456, 0.31793495, -80.18916213, -0.01133084, -98.2717318, -0.0938902, -9.82717318, -0.3359329, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 46.30426382, 0.01010772, 56.74582543, 0.07709856, 5.67458254, 0.31827008, -80.18476103, -0.01124671, -98.26633826, -0.08749635, -9.82663383, -0.32866787, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 27480485.66134394, 0.07, 0.00071458, 0.00023333, 11450202.35889331, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32789376362, 1002992, 0.32789376362, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 46.53206478, 0.01005092, 57.13650436, 0.0951946, 5.71365044, 0.39889624, -80.55054923, -0.01120911, -98.90764207, -0.1081205, -9.89076421, -0.41182213, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 46.53206478, 0.01005092, 57.13650436, 0.09577068, 5.71365044, 0.40436924, -80.55054923, -0.01120911, -98.90764207, -0.1087762, -9.89076421, -0.41737476, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 26637120.98229906, 0.07, 0.00071458, 0.00023333, 11098800.40929127, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25978296384, 1102992, 0.25978296384, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 46.25357268, 0.00996613, 56.69581802, 0.07748961, 5.6695818, 0.32013237, -80.08479249, -0.01109601, -98.16480237, -0.08795192, -9.81648024, -0.33059468, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 31.18625626, 0.00954521, 38.22689161, 0.07578552, 3.82268916, 0.31503259, -80.07002284, -0.01118169, -98.14669831, -0.09377888, -9.81466983, -0.33302595, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 27391149.16462748, 0.07, 0.00071458, 0.00023333, 11412978.81859478, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32696805726000006, 1202992, 0.32696805726000006, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.1915078, 0.00858021, 75.73900058, 0.08007523, 7.57390006, 0.32570527, -145.40074996, -0.0100558, -177.07413561, -0.09745246, -17.70741356, -0.3430825, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 91.9212096, 0.0088806, 111.94487469, 0.08456924, 11.19448747, 0.33036062, -214.16710576, -0.010813, -260.82021681, -0.10333601, -26.08202168, -0.34912738, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29846310.41783171, 0.1, 0.00133333, 0.00052083, 12435962.67409655, 0.00127345)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36904724744, 1012992, 0.36904724744, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 91.87209038, 0.00884068, 112.0355795, 0.10255076, 11.20355795, 0.40387927, -213.99183834, -0.01078576, -260.95737582, -0.12533846, -26.09573758, -0.42666697, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 91.87209038, 0.00884068, 112.0355795, 0.10291642, 11.20355795, 0.40704149, -213.99183834, -0.01078576, -260.95737582, -0.12578545, -26.09573758, -0.42991051, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29375945.40200274, 0.1, 0.00133333, 0.00052083, 12239977.25083448, 0.00127345)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30059156632000006, 1112992, 0.30059156632000006, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 90.80638108, 0.00859523, 111.02743609, 0.08761963, 11.10274361, 0.33597531, -211.30868108, -0.01053536, -258.36357319, -0.10713605, -25.83635732, -0.35549173, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 61.3433238, 0.0083093, 75.00345109, 0.0835519, 7.50034511, 0.33647613, -143.37517644, -0.00979093, -175.30241872, -0.10176869, -17.53024187, -0.35469293, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 28401883.94514974, 0.1, 0.00133333, 0.00052083, 11834118.31047906, 0.00127345)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36523506347, 1212992, 0.36523506347, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 63.07388221, 0.00869147, 77.02303517, 0.08831017, 7.70230352, 0.35819284, -147.09343999, -0.01044131, -179.62400291, -0.10776847, -17.96240029, -0.37765114, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 93.55887348, 0.00915478, 114.24995815, 0.09166799, 11.42499581, 0.36155066, -147.1946473, -0.01031894, -179.7475928, -0.10238975, -17.97475928, -0.37227241, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 28874667.03854802, 0.08, 0.00106667, 0.00026667, 12031111.26606167, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.37053139476, 1022992, 0.37053139476, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 92.93506774, 0.00910031, 113.49027707, 0.11149717, 11.34902771, 0.44322517, -146.21532276, -0.01025752, -178.55496203, -0.12451513, -17.8554962, -0.45624313, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 92.93506774, 0.00910031, 113.49027707, 0.11129828, 11.34902771, 0.44302628, -146.21532276, -0.01025752, -178.55496203, -0.1242932, -17.8554962, -0.4560212, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 28867855.21496654, 0.08, 0.00106667, 0.00026667, 12028273.00623606, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30145179104, 1122992, 0.30145179104, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 93.36038956, 0.00921808, 113.78530259, 0.09016045, 11.37853026, 0.35966867, -146.95302751, -0.01037213, -179.10266635, -0.10069015, -17.91026664, -0.37019836, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.9611265, 0.00875689, 76.73544277, 0.08888925, 7.67354428, 0.35839746, -146.90287289, -0.01048916, -179.04153916, -0.10844424, -17.90415392, -0.37795246, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29578553.15644071, 0.08, 0.00106667, 0.00026667, 12324397.14851696, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.37104620476000005, 1222992, 0.37104620476000005, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 30.61559485, 0.00917983, 37.35639277, 0.07542307, 3.73563928, 0.32135671, -78.64936857, -0.01070379, -95.96601725, -0.09330463, -9.59660172, -0.33923828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 45.4265328, 0.00957412, 55.42833349, 0.07638785, 5.54283335, 0.31961234, -78.67235689, -0.01062603, -95.99406702, -0.0866741, -9.5994067, -0.32989859, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 29169180.09255874, 0.07, 0.00071458, 0.00023333, 12153825.03856614, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32361906799, 1032992, 0.32361906799, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 46.70797493, 0.00993381, 57.13311808, 0.09082111, 5.71331181, 0.3884137, -80.87884344, -0.01104383, -98.93086824, -0.10311056, -9.89308682, -0.40070315, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 46.70797493, 0.00993381, 57.13311808, 0.09188986, 5.71331181, 0.39889427, -80.87884344, -0.01104383, -98.93086824, -0.10432702, -9.89308682, -0.41133143, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 28238346.92802374, 0.07, 0.00071458, 0.00023333, 11765977.88667656, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25953798164, 1132992, 0.25953798164, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 45.7939608, 0.00994341, 55.85626981, 0.07426274, 5.58562698, 0.31364711, -79.33180632, -0.01102264, -96.7633876, -0.08423155, -9.67633876, -0.32361593, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 30.89761152, 0.0095366, 37.68674505, 0.07270252, 3.7686745, 0.30934847, -79.34950699, -0.01109778, -96.78497763, -0.08986142, -9.67849776, -0.32650737, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 29300743.06226883, 0.07, 0.00071458, 0.00023333, 12208642.94261201, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32638079726, 1232992, 0.32638079726, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 30.97479531, 0.00963587, 37.93263757, 0.07550938, 3.79326376, 0.32144975, -53.74877263, -0.01049455, -65.82231428, -0.08547245, -6.58223143, -0.33141281, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 30.90674454, 0.00958008, 37.8493006, 0.07631131, 3.78493006, 0.3161391, -79.34864508, -0.01120026, -97.17266458, -0.09440961, -9.71726646, -0.3342374, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 27772527.03835467, 0.07, 0.00071458, 0.00023333, 11571886.26598111, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32656373754, 1003992, 0.32656373754, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 30.64539755, 0.00985001, 37.57081526, 0.0915666, 3.75708153, 0.39106138, -78.59381043, -0.01150968, -96.35487766, -0.11340476, -9.63548777, -0.41289954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 30.64539755, 0.00985001, 37.57081526, 0.0926623, 3.75708153, 0.40177063, -78.59381043, -0.01150968, -96.35487766, -0.11477102, -9.63548777, -0.42387935, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 27313964.58072263, 0.07, 0.00071458, 0.00023333, 11380818.57530109, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25944448354000005, 1103992, 0.25944448354000005, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 30.77976527, 0.00976337, 37.66383791, 0.07330483, 3.76638379, 0.3094222, -78.97740489, -0.01138762, -96.64115859, -0.09061953, -9.66411586, -0.3267369, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 30.8504297, 0.00981077, 37.75030685, 0.07260884, 3.77503069, 0.31541625, -53.50940748, -0.01067222, -65.47709616, -0.08214962, -6.54770962, -0.32495703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 28091318.84761373, 0.07, 0.00071458, 0.00023333, 11704716.18650572, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.3273263087, 1203992, 0.3273263087, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 63.85654336, 0.00863195, 77.97652063, 0.08889022, 7.79765206, 0.35835804, -148.84197781, -0.01037907, -181.75395886, -0.10848806, -18.17539589, -0.37795587, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 63.72817848, 0.0085128, 77.81977168, 0.09311877, 7.78197717, 0.36258659, -218.9639464, -0.01137931, -267.38131736, -0.12468209, -26.73813174, -0.39414991, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 28885443.4747472, 0.08, 0.00106667, 0.00026667, 12035601.44781133, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.37110182915, 1013992, 0.37110182915, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 63.17102125, 0.00819918, 77.33555826, 0.11399614, 7.73355583, 0.44819774, -216.49163708, -0.01104584, -265.034525, -0.1527272, -26.5034525, -0.4869288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 63.17102125, 0.00819918, 77.33555826, 0.11458483, 7.73355583, 0.44878643, -216.49163708, -0.01104584, -265.034525, -0.15351557, -26.5034525, -0.48771717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 27905819.55806885, 0.08, 0.00106667, 0.00026667, 11627424.81586202, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.29922058964000003, 1113992, 0.29922058964000003, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 63.71355376, 0.00849382, 78.11028796, 0.09462603, 7.8110288, 0.36434985, -218.60263544, -0.01146039, -267.99815417, -0.12680707, -26.79981542, -0.3965309, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 63.82531675, 0.00862306, 78.24730495, 0.09047186, 7.82473049, 0.36019568, -148.6266315, -0.0104292, -182.21035086, -0.11048248, -18.22103509, -0.3802063, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 27322666.45106058, 0.08, 0.00106667, 0.00026667, 11384444.35460858, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.37074959857, 1213992, 0.37074959857, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 63.00516985, 0.00866779, 76.67816095, 0.08938498, 7.6678161, 0.35938955, -147.00892648, -0.01037048, -178.91189173, -0.10904045, -17.89118917, -0.37904502, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 63.00516985, 0.00866779, 76.67816095, 0.08856961, 7.6678161, 0.35857418, -147.00892648, -0.01037048, -178.91189173, -0.10804373, -17.89118917, -0.3780483, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 30075953.82206886, 0.08, 0.00106667, 0.00026667, 12531647.42586203, 0.00073242)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.37036409956, 1023992, 0.37036409956, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 61.9285874, 0.00876572, 75.7665296, 0.11042942, 7.57665296, 0.44217987, -144.44664265, -0.01054393, -176.72324341, -0.13481926, -17.67232434, -0.4665697, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 61.9285874, 0.00876572, 75.7665296, 0.11089527, 7.57665296, 0.44264572, -144.44664265, -0.01054393, -176.72324341, -0.13538871, -17.67232434, -0.46713916, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 28157681.44475979, 0.08, 0.00106667, 0.00026667, 11732367.26864991, 0.00073242)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30143139316000006, 1123992, 0.30143139316000006, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 62.14018685, 0.00857293, 76.0834615, 0.09259425, 7.60834615, 0.3643582, -144.84492071, -0.01033697, -177.34582895, -0.11304598, -17.7345829, -0.38480993, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 62.14018685, 0.00857293, 76.0834615, 0.09304507, 7.60834615, 0.36480902, -144.84492071, -0.01033697, -177.34582895, -0.11359707, -17.7345829, -0.38536102, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 27853542.00821352, 0.08, 0.00106667, 0.00026667, 11605642.5034223, 0.00073242)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36796639248999996, 1223992, 0.36796639248999996, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 30.9904937, 0.00944325, 37.75651267, 0.07113515, 3.77565127, 0.3107219, -53.79971795, -0.01025761, -65.54557511, -0.08047596, -6.55455751, -0.32006271, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 30.92751646, 0.00939055, 37.67978589, 0.07275382, 3.76797859, 0.31415757, -79.45446088, -0.01092418, -96.80140588, -0.08993391, -9.68014059, -0.33133766, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 29707235.64396871, 0.07, 0.00071458, 0.00023333, 12378014.85165363, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32561717205, 1033992, 0.32561717205, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 30.54636631, 0.00978962, 37.26090254, 0.09186929, 3.72609025, 0.3999113, -78.33574947, -0.0113687, -95.55508818, -0.11371652, -9.55550882, -0.42175853, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 30.54636631, 0.00978962, 37.26090254, 0.09132838, 3.72609025, 0.39457671, -78.33574947, -0.0113687, -95.55508818, -0.11304203, -9.55550882, -0.41629037, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 29275871.48011031, 0.07, 0.00071458, 0.00023333, 12198279.7833793, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25895799713, 1133992, 0.25895799713, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 30.40362269, 0.00953536, 37.05873352, 0.07405147, 3.70587335, 0.3168765, -78.04495392, -0.01107816, -95.12837268, -0.0915254, -9.51283727, -0.33435043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 30.47030111, 0.00957894, 37.14000732, 0.07268941, 3.71400073, 0.31639053, -52.86435944, -0.01039846, -64.43594664, -0.08223143, -6.44359466, -0.32593255, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 29544807.52152503, 0.07, 0.00071458, 0.00023333, 12310336.4673021, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32523274513, 1233992, 0.32523274513, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 30.41095273, 0.00986206, 37.09429804, 0.05914796, 3.7094298, 0.30398888, -30.41095273, -0.00986206, -37.09429804, -0.05914796, -3.7094298, -0.30398888, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 30.36785002, 0.00983828, 37.04172275, 0.05959441, 3.70417227, 0.30226731, -44.97943118, -0.01033411, -54.86445759, -0.06484297, -5.48644576, -0.30751587, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 29289666.32261735, 0.07, 0.00071458, 0.00023333, 12204027.63442389, 0.00060032)
    ops.section('Aggregator', 1004991, 1004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1004992, 1004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.32631411514, 1004992, 0.32631411514, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 31.36604272, 0.0097475, 38.36824002, 0.07225637, 3.836824, 0.37663519, -46.5059639, -0.01026075, -56.88801745, -0.0787405, -5.68880175, -0.38311931, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 31.36604272, 0.0097475, 38.36824002, 0.07257581, 3.836824, 0.38065731, -46.5059639, -0.01026075, -56.88801745, -0.07909045, -5.68880175, -0.38717195, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 28224605.25034807, 0.07, 0.00071458, 0.00023333, 11760252.18764503, 0.00060032)
    ops.section('Aggregator', 1104991, 1104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1104992, 1104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.25997837432, 1104992, 0.25997837432, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 30.82253276, 0.00986439, 37.58535023, 0.0594942, 3.75853502, 0.30403635, -45.66927916, -0.01036334, -55.68964319, -0.06473382, -5.56896432, -0.30927596, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 30.86721538, 0.00989092, 37.63983673, 0.05878921, 3.76398367, 0.30240249, -30.86721538, -0.00989092, -37.63983673, -0.05878921, -3.76398367, -0.30240249, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 29394060.99996212, 0.07, 0.00071458, 0.00023333, 12247525.41665088, 0.00060032)
    ops.section('Aggregator', 1204991, 1204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1204992, 1204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.32753153919, 1204992, 0.32753153919, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 35.16103605, 0.00829396, 43.05548859, 0.09916927, 4.30554886, 0.40550776, -142.28519129, -0.0107432, -174.23145385, -0.13718404, -17.42314539, -0.44352253, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 35.16103605, 0.00829396, 43.05548859, 0.10047022, 4.30554886, 0.40680871, -142.28519129, -0.0107432, -174.23145385, -0.13899414, -17.42314539, -0.44533263, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 27807781.72031025, 0.08, 0.00106667, 0.00026667, 11586575.71679594, 0.00073242)
    ops.section('Aggregator', 1014991, 1014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1014992, 1014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.3264362939, 1014992, 0.3264362939, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 35.02312484, 0.00807452, 42.76866902, 0.12520156, 4.2768669, 0.51464453, -141.88767568, -0.01042189, -173.2668649, -0.17338849, -17.32668649, -0.56283146, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 35.02312484, 0.00807452, 42.76866902, 0.12357489, 4.2768669, 0.51301786, -141.88767568, -0.01042189, -173.2668649, -0.1711252, -17.32668649, -0.56056817, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 28874857.40782839, 0.08, 0.00106667, 0.00026667, 12031190.58659516, 0.00073242)
    ops.section('Aggregator', 1114991, 1114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1114992, 1114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.25677700897, 1114992, 0.25677700897, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 35.07772846, 0.00802196, 42.59751752, 0.09659468, 4.25975175, 0.40468386, -142.21225253, -0.01026784, -172.69900831, -0.13350492, -17.26990083, -0.4415941, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 35.07772846, 0.00802196, 42.59751752, 0.0964324, 4.25975175, 0.40452158, -142.21225253, -0.01026784, -172.69900831, -0.13327913, -17.26990083, -0.44136831, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 30788377.97803133, 0.08, 0.00106667, 0.00026667, 12828490.82417972, 0.00073242)
    ops.section('Aggregator', 1214991, 1214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1214992, 1214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.32458134196, 1214992, 0.32458134196, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 53.17436396, 0.01054854, 64.9158378, 0.09449846, 6.49158378, 0.36384291, -123.66403679, -0.01281733, -150.97039166, -0.11543905, -15.09703917, -0.3847835, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 53.17436396, 0.01054854, 64.9158378, 0.09450829, 6.49158378, 0.36385273, -123.66403679, -0.01281733, -150.97039166, -0.11545106, -15.09703917, -0.3847955, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 28979059.72396731, 0.07, 0.00071458, 0.00023333, 12074608.21831971, 0.00060032)
    ops.section('Aggregator', 1024991, 1024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1024992, 1024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.37127180996, 1024992, 0.37127180996, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 53.46985736, 0.00998126, 65.20421388, 0.11185768, 6.52042139, 0.44561865, -124.31728906, -0.01214787, -151.5996396, -0.13668324, -15.15996396, -0.4704442, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 53.46985736, 0.00998126, 65.20421388, 0.1110501, 6.52042139, 0.44481107, -124.31728906, -0.01214787, -151.5996396, -0.13569604, -15.15996396, -0.469457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 29380646.54525716, 0.07, 0.00071458, 0.00023333, 12241936.06052382, 0.00060032)
    ops.section('Aggregator', 1124991, 1124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1124992, 1124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.29961562154, 1124992, 0.29961562154, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 54.96848828, 0.01016757, 66.90556305, 0.09216618, 6.69055631, 0.36122386, -127.81534233, -0.01235057, -155.57199613, -0.11258697, -15.55719961, -0.38164465, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 54.96848828, 0.01016757, 66.90556305, 0.09195543, 6.69055631, 0.3610131, -127.81534233, -0.01235057, -155.57199613, -0.11232934, -15.55719961, -0.38138702, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 30034765.2166404, 0.07, 0.00071458, 0.00023333, 12514485.5069335, 0.00060032)
    ops.section('Aggregator', 1224991, 1224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1224992, 1224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.37166752639, 1224992, 0.37166752639, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 30.46321605, 0.00952783, 37.23290599, 0.06037261, 3.7232906, 0.30742546, -30.46321605, -0.00952783, -37.23290599, -0.06037261, -3.7232906, -0.30742546, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 30.4192534, 0.00949374, 37.17917374, 0.0604051, 3.71791737, 0.30056098, -45.09918983, -0.00998902, -55.1213599, -0.06576346, -5.51213599, -0.30591933, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 28545552.16190946, 0.07, 0.00071458, 0.00023333, 11893980.06746227, 0.00060032)
    ops.section('Aggregator', 1034991, 1034990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1034992, 1034991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.32438679091, 1034992, 0.32438679091, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 31.23790382, 0.0097015, 38.05496292, 0.06968442, 3.80549629, 0.37120276, -46.31562047, -0.01019551, -56.42309516, -0.07590803, -5.64230952, -0.37742637, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 31.23790382, 0.0097015, 38.05496292, 0.06997597, 3.80549629, 0.37498223, -46.31562047, -0.01019551, -56.42309516, -0.07622742, -5.64230952, -0.38123368, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 29734358.90469993, 0.07, 0.00071458, 0.00023333, 12389316.21029164, 0.00060032)
    ops.section('Aggregator', 1134991, 1134990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1134992, 1134991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.25956208282, 1134992, 0.25956208282, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 31.54084164, 0.00985279, 38.6046474, 0.05955228, 3.86046474, 0.30100491, -46.76167565, -0.01037314, -57.23430024, -0.06481995, -5.72343002, -0.30627258, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 31.58666632, 0.00988986, 38.66073485, 0.05898927, 3.86607349, 0.30107134, -31.58666632, -0.00988986, -38.66073485, -0.05898927, -3.86607349, -0.30107134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 27993405.02541817, 0.07, 0.00071458, 0.00023333, 11663918.7605909, 0.00060032)
    ops.section('Aggregator', 1234991, 1234990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1234992, 1234991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.32897165488, 1234992, 0.32897165488, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 52.27490288, 0.00862346, 63.83863129, 0.12626747, 6.38386313, 0.51249822, -142.85199205, -0.01065111, -174.45227341, -0.16006491, -17.44522734, -0.54629566, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 52.27490288, 0.00862346, 63.83863129, 0.12545377, 6.38386313, 0.51168452, -142.85199205, -0.01065111, -174.45227341, -0.15903148, -17.44522734, -0.54526222, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 28858195.14204344, 0.08, 0.00106667, 0.00026667, 12024247.97585144, 0.00073242)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25891258446, 6200992, 0.25891258446, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 61.96073481, 0.00871734, 75.73990152, 0.1098555, 7.57399015, 0.44198143, -144.52934987, -0.01047591, -176.67057629, -0.13410882, -17.66705763, -0.46623474, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 61.96073481, 0.00871734, 75.73990152, 0.10909474, 7.57399015, 0.44122066, -144.52934987, -0.01047591, -176.67057629, -0.13317885, -17.66705763, -0.46530477, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 28495436.23909657, 0.08, 0.00106667, 0.00026667, 11873098.4329569, 0.00073242)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30109061819, 6201992, 0.30109061819, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 44.34219226, 0.01031687, 54.32754175, 0.13284669, 5.43275417, 0.51907077, -120.51326256, -0.01301275, -147.6514572, -0.16863178, -14.76514572, -0.55485586, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 44.34219226, 0.01031687, 54.32754175, 0.13202495, 5.43275417, 0.51824903, -120.51326256, -0.01301275, -147.6514572, -0.16758813, -14.76514572, -0.55381221, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 27585539.13301925, 0.07, 0.00071458, 0.00023333, 11493974.63875802, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25891704926000003, 6202992, 0.25891704926000003, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 6203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6203990, 37.50709411, 0.01207767, 45.73139337, 0.1309262, 4.57313934, 0.51848456, -101.42054791, -0.01547609, -123.65935253, -0.1664197, -12.36593525, -0.55397806, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6203991, 37.50709411, 0.01207767, 45.73139337, 0.13240711, 4.57313934, 0.51996547, -101.42054791, -0.01547609, -123.65935253, -0.16830052, -12.36593525, -0.55585888, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6203990, 29434370.13983575, 0.06, 0.00045, 0.0002, 12264320.89159823, 0.00046953)
    ops.section('Aggregator', 6203991, 6203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6203992, 6203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6203, 6203991, 0.25802565762, 6203992, 0.25802565762, 6203990)
    # Create element
    ops.element('forceBeamColumn', 6203, 1104, 1204, 6203, 6203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 36.29640485, 0.00824944, 44.5057727, 0.09242575, 4.45057727, 0.37375637, -147.26093934, -0.01042181, -180.56779782, -0.12754189, -18.05677978, -0.4088725, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 70.95669321, 0.00868749, 87.00537897, 0.09780252, 8.7005379, 0.3779548, -216.74617284, -0.01122707, -265.76890853, -0.12744715, -26.57689085, -0.40759944, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 27248247.71558273, 0.1, 0.00133333, 0.00052083, 11353436.54815947, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32861466278, 2001992, 0.32861466278, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 82.08529881, 0.00643325, 100.41363715, 0.08002903, 10.04136371, 0.33103815, -192.61177153, -0.00744866, -235.61890884, -0.09741331, -23.56189088, -0.34842244, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 121.952299, 0.00663248, 149.18230279, 0.08302854, 14.91823028, 0.32929855, -284.52051203, -0.00795653, -348.04940558, -0.10134429, -34.80494056, -0.3476143, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28210933.00999742, 0.125, 0.00260417, 0.00065104, 11754555.42083226, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36949546655, 2101992, 0.36949546655, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 80.02296941, 0.00635859, 98.04746003, 0.08122873, 9.804746, 0.33269749, -187.78170668, -0.00737186, -230.07793283, -0.09889432, -23.00779328, -0.35036308, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 118.82684681, 0.0065584, 145.59157952, 0.08448431, 14.55915795, 0.33276692, -277.30572706, -0.00788086, -339.76647445, -0.10313873, -33.97664744, -0.35142134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 27567665.46985047, 0.125, 0.00260417, 0.00065104, 11486527.27910436, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36624187574, 2201992, 0.36624187574, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 36.55179143, 0.00813385, 44.76634594, 0.0909981, 4.47663459, 0.3701158, -148.46319227, -0.01026898, -181.82842385, -0.12556349, -18.18284239, -0.4046812, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 71.60778839, 0.00855925, 87.70073645, 0.0968324, 8.77007365, 0.37891092, -218.65558182, -0.01105081, -267.79566841, -0.12617294, -26.77956684, -0.40825146, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 27736562.0358892, 0.1, 0.00133333, 0.00052083, 11556900.84828717, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32841205912, 2301992, 0.32841205912, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 70.77329285, 0.00829129, 86.61277037, 0.09458526, 8.66127704, 0.36896329, -215.98846524, -0.01070197, -264.32794899, -0.12324294, -26.4327949, -0.39762097, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 70.77329285, 0.00829129, 86.61277037, 0.09583301, 8.66127704, 0.37971542, -215.98846524, -0.01070197, -264.32794899, -0.12487021, -26.4327949, -0.40875261, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 28042701.99372125, 0.1, 0.00133333, 0.00052083, 11684459.16405052, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32575852113000003, 2011992, 0.32575852113000003, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 121.76958995, 0.00664162, 148.99794365, 0.08177213, 14.89979437, 0.3266354, -284.11526424, -0.00796941, -347.6450085, -0.09981015, -34.76450085, -0.34467342, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 121.76958995, 0.00664162, 148.99794365, 0.08193623, 14.89979437, 0.32807001, -284.11526424, -0.00796941, -347.6450085, -0.10001074, -34.76450085, -0.34614453, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 28107557.83003431, 0.125, 0.00260417, 0.00065104, 11711482.42918096, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36946324469, 2111992, 0.36946324469, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 120.54223309, 0.00654051, 146.9223423, 0.08099069, 14.69223423, 0.3289674, -281.46707155, -0.00781017, -343.06483606, -0.09881925, -34.30648361, -0.34679596, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 120.54223309, 0.00654051, 146.9223423, 0.08059841, 14.69223423, 0.32548701, -281.46707155, -0.00781017, -343.06483606, -0.09833973, -34.30648361, -0.34322832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29558266.45102076, 0.125, 0.00260417, 0.00065104, 12315944.35459198, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36754856524, 2211992, 0.36754856524, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 70.38743313, 0.00840833, 86.17261215, 0.09583339, 8.61726122, 0.37313371, -214.94835007, -0.01084774, -263.15295189, -0.12486384, -26.31529519, -0.40216416, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 70.38743313, 0.00840833, 86.17261215, 0.09648776, 8.61726122, 0.37873688, -214.94835007, -0.01084774, -263.15295189, -0.12571724, -26.31529519, -0.40796636, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 27893968.25295517, 0.1, 0.00133333, 0.00052083, 11622486.77206465, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.3262003415, 2311992, 0.3262003415, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 72.32755132, 0.00825432, 88.1168964, 0.09168003, 8.81168964, 0.36561767, -220.75026247, -0.01058667, -268.94077918, -0.11938697, -26.89407792, -0.39332461, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 36.79950521, 0.00785786, 44.83295962, 0.0870531, 4.48329596, 0.36540795, -149.7152328, -0.00986431, -182.39856621, -0.12005389, -18.23985662, -0.39840874, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 29713589.91350516, 0.1, 0.00133333, 0.00052083, 12380662.46396048, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.32707729084, 2021992, 0.32707729084, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 121.95007999, 0.00671743, 148.16632834, 0.07863995, 14.81663283, 0.32456826, -285.14214171, -0.00798764, -346.44064354, -0.09590687, -34.64406435, -0.34183518, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 82.17711616, 0.00651463, 99.84316185, 0.07566349, 9.98431619, 0.32514713, -193.09998607, -0.00748966, -234.61170292, -0.09201833, -23.46117029, -0.34150197, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 30629573.44071192, 0.125, 0.00260417, 0.00065104, 12762322.2669633, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.37089957103, 2121992, 0.37089957103, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 123.0653963, 0.00666784, 150.53684002, 0.08203861, 15.053684, 0.32850887, -287.06364174, -0.00799982, -351.14382118, -0.10013425, -35.11438212, -0.34660452, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 82.82080222, 0.0064682, 101.30859063, 0.07815632, 10.13085906, 0.32188497, -194.31794583, -0.00748985, -237.69483871, -0.09512255, -23.76948387, -0.3388512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 28229386.68410601, 0.125, 0.00260417, 0.00065104, 11762244.45171084, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.37073000544, 2221992, 0.37073000544, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 72.22588074, 0.00828887, 88.09913567, 0.09422199, 8.80991357, 0.37379471, -220.42694584, -0.01064827, -268.87070409, -0.12271863, -26.88707041, -0.40229136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 36.75873922, 0.00788862, 44.83729544, 0.0892365, 4.48372954, 0.37144067, -149.51421493, -0.00991723, -182.37331233, -0.12310193, -18.23733123, -0.40530609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 29288285.97822502, 0.1, 0.00133333, 0.00052083, 12203452.49092709, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32720050391, 2321992, 0.32720050391, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 36.42159727, 0.00809871, 44.43107314, 0.08693941, 4.44310731, 0.35970803, -147.98544092, -0.01015621, -180.52892904, -0.1198525, -18.0528929, -0.39262111, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 53.86796242, 0.00829708, 65.7140696, 0.09183757, 6.57140696, 0.37008894, -217.80470135, -0.01098195, -265.70214766, -0.12721736, -26.57021477, -0.40546873, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29247711.5371956, 0.1, 0.00133333, 0.00052083, 12186546.4738315, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32793801710000003, 2002992, 0.32793801710000003, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 80.32536868, 0.00642392, 97.82179915, 0.07732703, 9.78217991, 0.32581782, -188.71499394, -0.00739758, -229.82079681, -0.09407067, -22.98207968, -0.34256146, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 80.17754129, 0.00637027, 97.64177207, 0.07967248, 9.76417721, 0.32880287, -278.23655477, -0.00796116, -338.84189795, -0.10612614, -33.8841898, -0.35525654, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29850711.10519741, 0.125, 0.00260417, 0.00065104, 12437796.29383225, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36765008982, 2102992, 0.36765008982, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 80.37799518, 0.00636662, 98.02525397, 0.07801499, 9.8025254, 0.32653592, -188.76665752, -0.00734449, -230.21101114, -0.0949286, -23.02110111, -0.34344953, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 80.24948651, 0.00630944, 97.86853078, 0.08055087, 9.78685308, 0.33106003, -278.30155824, -0.00790787, -339.40360001, -0.10733064, -33.94036, -0.3578398, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29352582.2115225, 0.125, 0.00260417, 0.00065104, 12230242.58813438, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36694902919, 2202992, 0.36694902919, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.94576875, 0.00806027, 43.86573236, 0.08998421, 4.38657324, 0.37140068, -145.9807924, -0.0101069, -178.1448719, -0.12409311, -17.81448719, -0.40550958, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 53.13240741, 0.00826012, 64.8391186, 0.09354866, 6.48391186, 0.36884871, -214.81968671, -0.01093207, -262.15110181, -0.12959966, -26.21511018, -0.4048997, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29122888.71777092, 0.1, 0.00133333, 0.00052083, 12134536.96573788, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32669595808999996, 2302992, 0.32669595808999996, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 52.78849004, 0.00821508, 64.63758183, 0.09708711, 6.46375818, 0.38068821, -213.29056912, -0.01095014, -261.16652713, -0.13460368, -26.11665271, -0.41820478, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 52.78849004, 0.00821508, 64.63758183, 0.09571016, 6.46375818, 0.36899885, -213.29056912, -0.01095014, -261.16652713, -0.13268784, -26.11665271, -0.40597652, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 27827352.48630615, 0.1, 0.00133333, 0.00052083, 11594730.20262756, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32589253911, 2012992, 0.32589253911, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 81.90015398, 0.00655327, 100.19140829, 0.08101708, 10.01914083, 0.32791228, -283.97532597, -0.00824641, -347.39724464, -0.10796699, -34.73972446, -0.35486219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 121.73178618, 0.00682277, 148.91887864, 0.08198968, 14.89188786, 0.32667614, -284.40660283, -0.0081736, -347.92484116, -0.10005883, -34.79248412, -0.3447453, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28194281.26410378, 0.125, 0.00260417, 0.00065104, 11747617.19337657, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.37167315216999997, 2112992, 0.37167315216999997, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 80.35800951, 0.00632215, 98.25128826, 0.08071482, 9.82512883, 0.32670183, -278.497124, -0.00795716, -340.50994265, -0.10758247, -34.05099427, -0.35356948, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 119.49247163, 0.00658229, 146.09980195, 0.08263767, 14.6099802, 0.33388392, -278.99934341, -0.00788601, -341.12399101, -0.10085732, -34.1123991, -0.35210357, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 28406198.52697282, 0.125, 0.00260417, 0.00065104, 11835916.05290534, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36714385568, 2212992, 0.36714385568, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 53.43838805, 0.00804861, 65.08881676, 0.09108535, 6.50888168, 0.36587801, -216.07445725, -0.01064144, -263.18216674, -0.12617595, -26.31821667, -0.40096861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 53.43838805, 0.00804861, 65.08881676, 0.09143423, 6.50888168, 0.36897346, -216.07445725, -0.01064144, -263.18216674, -0.12666136, -26.31821667, -0.4042006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29795162.58792002, 0.1, 0.00133333, 0.00052083, 12414651.07830001, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32568964888, 2312992, 0.32568964888, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 53.17064336, 0.00836539, 64.84981471, 0.09302197, 6.48498147, 0.37139999, -214.96832168, -0.01104865, -262.18708199, -0.12883695, -26.2187082, -0.40721497, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 36.00417941, 0.00815972, 43.91265962, 0.08828124, 4.39126596, 0.36302106, -146.10970441, -0.01021427, -178.20335922, -0.12169265, -17.82033592, -0.39643247, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 29322931.23071958, 0.1, 0.00133333, 0.00052083, 12217888.01279982, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.3274396589, 2022992, 0.3274396589, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 119.86908472, 0.00663104, 147.16634268, 0.08283577, 14.71663427, 0.3253946, -279.58747152, -0.00799394, -343.25669326, -0.10114782, -34.32566933, -0.34370665, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 80.71539626, 0.00642825, 99.09635745, 0.08042192, 9.90963575, 0.33232465, -189.32796626, -0.00747191, -232.44278896, -0.09792295, -23.2442789, -0.34982568, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 26698867.0034551, 0.125, 0.00260417, 0.00065104, 11124527.91810629, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.36774596311, 2122992, 0.36774596311, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 123.26839592, 0.00663179, 151.45461799, 0.08332858, 15.1454618, 0.3269796, -286.98260266, -0.00801631, -352.60327783, -0.10177169, -35.26032778, -0.34542271, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 82.89336323, 0.00643363, 101.84753819, 0.07948539, 10.18475382, 0.32122921, -194.2148204, -0.00749475, -238.62346234, -0.09679439, -23.86234623, -0.33853821, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 26355807.44543726, 0.125, 0.00260417, 0.00065104, 10981586.43559886, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.37009803995, 2222992, 0.37009803995, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 53.4135956, 0.00810054, 65.20795373, 0.09273993, 6.52079537, 0.36873302, -215.89207817, -0.01075067, -263.56362058, -0.12851506, -26.35636206, -0.40450815, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 36.07459279, 0.00791083, 44.04029257, 0.0888951, 4.40402926, 0.36842461, -146.65050502, -0.00994264, -179.03268332, -0.1226214, -17.90326833, -0.40215092, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 28978724.75266698, 0.1, 0.00133333, 0.00052083, 12074468.64694457, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32598539770999996, 2322992, 0.32598539770999996, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 63.34047542, 0.00831273, 77.17415269, 0.08190107, 7.71741527, 0.33328676, -148.06740864, -0.00976992, -180.40560521, -0.09972549, -18.04056052, -0.35111118, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 63.20059454, 0.00822795, 77.00372156, 0.08433618, 7.70037216, 0.33183388, -218.05395062, -0.01060481, -265.67733772, -0.11252757, -26.56773377, -0.36002527, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 29685492.30020659, 0.1, 0.00133333, 0.00052083, 12368955.12508608, 0.00127345)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.36829740378000003, 2003992, 0.36829740378000003, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 81.96817473, 0.00642983, 100.26173894, 0.07969553, 10.02617389, 0.32971843, -192.34580606, -0.00744369, -235.27332475, -0.09700485, -23.52733248, -0.34702775, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 81.86647592, 0.0063658, 100.13734311, 0.08095536, 10.01373431, 0.32264826, -283.53662623, -0.00802455, -346.81600868, -0.10791354, -34.68160087, -0.34960644, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 28244572.95233643, 0.125, 0.00260417, 0.00065104, 11768572.06347351, 0.00178813)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36933063893, 2103992, 0.36933063893, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 82.15681122, 0.00643501, 100.43539301, 0.07956828, 10.0435393, 0.33014233, -192.80280755, -0.00744543, -235.69836101, -0.09684471, -23.5698361, -0.34741876, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 82.05552876, 0.00637135, 100.31157682, 0.08130055, 10.03115768, 0.32720379, -284.22126001, -0.00802419, -347.4559629, -0.10836801, -34.74559629, -0.35427125, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 28464528.9686808, 0.125, 0.00260417, 0.00065104, 11860220.403617, 0.00178813)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.3696279121, 2203992, 0.3696279121, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 62.00474758, 0.0085507, 75.92885251, 0.08281735, 7.59288525, 0.32866495, -144.89674894, -0.01008696, -177.43550791, -0.10087171, -17.74355079, -0.34671931, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 61.8235639, 0.00847075, 75.7069813, 0.08540715, 7.57069813, 0.32839997, -213.27945087, -0.01098112, -261.17458099, -0.11401294, -26.1174581, -0.35700576, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 27793749.24115026, 0.1, 0.00133333, 0.00052083, 11580728.85047928, 0.00127345)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.36830870716999997, 2303992, 0.36830870716999997, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 62.57851718, 0.00831071, 76.36793282, 0.08261623, 7.63679328, 0.32452735, -215.94211689, -0.01072574, -263.5257884, -0.11023435, -26.35257884, -0.35214547, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 62.57851718, 0.00831071, 76.36793282, 0.08320907, 7.63679328, 0.3297235, -215.94211689, -0.01072574, -263.5257884, -0.11102826, -26.35257884, -0.3575427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 29116054.45376544, 0.1, 0.00133333, 0.00052083, 12131689.3557356, 0.00127345)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.36810724018, 2013992, 0.36810724018, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 79.29840242, 0.00640484, 96.90049872, 0.08241392, 9.69004987, 0.33422385, -275.0975068, -0.00803838, -336.16169802, -0.10982836, -33.6161698, -0.36163829, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 117.69202515, 0.00660133, 143.81646521, 0.08565651, 14.38164652, 0.33385761, -362.38242282, -0.00848201, -442.82149993, -0.11158247, -44.28214999, -0.35978357, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 28623935.22367814, 0.125, 0.00260417, 0.00065104, 11926639.67653256, 0.00178813)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.3669678374, 2113992, 0.3669678374, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 81.86401135, 0.00645791, 100.39363609, 0.08317127, 10.03936361, 0.33281983, -283.48262831, -0.00817374, -347.64790236, -0.11090686, -34.76479024, -0.36055542, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 121.68642709, 0.00665423, 149.22971251, 0.08574381, 14.92297125, 0.32673805, -373.65015266, -0.0086282, -458.22452177, -0.11177351, -45.82245218, -0.35276775, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 27188991.75881515, 0.125, 0.00260417, 0.00065104, 11328746.56617298, 0.00178813)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.37037446234, 2213992, 0.37037446234, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 62.63601294, 0.00824992, 76.7659088, 0.08498927, 7.67659088, 0.32765412, -215.86608734, -0.01074665, -264.56275865, -0.11351459, -26.45627587, -0.35617944, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 62.63601294, 0.00824992, 76.7659088, 0.08545789, 7.67659088, 0.33165261, -215.86608734, -0.01074665, -264.56275865, -0.11414216, -26.45627587, -0.36033687, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 27450377.70166776, 0.1, 0.00133333, 0.00052083, 11437657.3756949, 0.00127345)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.36750412342, 2313992, 0.36750412342, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 62.97094461, 0.0084374, 77.17611125, 0.08640359, 7.71761113, 0.33339511, -217.12859862, -0.01097675, -266.10909184, -0.11538766, -26.61090918, -0.36237917, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 63.13265694, 0.00852654, 77.37430311, 0.08311945, 7.73743031, 0.32778494, -147.5011954, -0.0100802, -180.77493892, -0.10126377, -18.07749389, -0.34592926, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 27451922.6853386, 0.1, 0.00133333, 0.00052083, 11438301.11889108, 0.00127345)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.36971609206, 2023992, 0.36971609206, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 121.38648758, 0.00659096, 148.15035342, 0.08226716, 14.81503534, 0.32531554, -373.19394252, -0.00846811, -455.47750481, -0.10716183, -45.54775048, -0.35021021, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 81.79530578, 0.0064587, 99.82992095, 0.07734079, 9.98299209, 0.32748149, -192.05682528, -0.00745736, -234.40242082, -0.09410476, -23.44024208, -0.34424546, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29076962.27170318, 0.125, 0.00260417, 0.00065104, 12115400.94654299, 0.00178813)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36960935136, 2123992, 0.36960935136, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 121.12931578, 0.00651352, 148.33809676, 0.08480453, 14.83380968, 0.3300919, -371.70934375, -0.00842894, -455.2048878, -0.11053279, -45.52048878, -0.35582016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 81.53578664, 0.00638935, 99.85083569, 0.07937385, 9.98508357, 0.32899649, -191.27437026, -0.00740741, -234.23954689, -0.09662483, -23.42395469, -0.34624747, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 27773610.27611877, 0.125, 0.00260417, 0.00065104, 11572337.61504949, 0.00178813)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36829229927, 2223992, 0.36829229927, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 64.91890038, 0.00837243, 79.33577417, 0.08406771, 7.93357742, 0.32934087, -223.73951262, -0.01085733, -273.42649587, -0.11222707, -27.34264959, -0.35750023, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 65.04352864, 0.00846728, 79.48807927, 0.08069811, 7.94880793, 0.32215664, -151.94607813, -0.00998933, -185.68952447, -0.09828546, -18.56895245, -0.33974398, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 28592212.82394735, 0.1, 0.00133333, 0.00052083, 11913422.00997806, 0.00127345)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.37203351519, 2323992, 0.37203351519, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 53.24927363, 0.01021209, 64.78664905, 0.09264038, 6.4786649, 0.36358697, -123.88232118, -0.01237593, -150.72356708, -0.11313758, -15.07235671, -0.38408417, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 53.24927363, 0.01021209, 64.78664905, 0.09247984, 6.4786649, 0.36342642, -123.88232118, -0.01237593, -150.72356708, -0.11294133, -15.07235671, -0.38388792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 30171673.01941854, 0.07, 0.00071458, 0.00023333, 12571530.42475772, 0.00060032)
    ops.section('Aggregator', 2004991, 2004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2004992, 2004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.36907643362, 2004992, 0.36907643362, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 71.37341426, 0.007208, 86.98769047, 0.07907849, 8.69876905, 0.32693433, -167.289715, -0.00838227, -203.88748525, -0.09623791, -20.38874852, -0.34409374, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 71.37341426, 0.007208, 86.98769047, 0.07918406, 8.69876905, 0.32790432, -167.289715, -0.00838227, -203.88748525, -0.09636695, -20.38874852, -0.34508721, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 29580318.27012393, 0.1125, 0.00189844, 0.00058594, 12325132.61255164, 0.00152995)
    ops.section('Aggregator', 2104991, 2104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2104992, 2104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.3668938774, 2104992, 0.3668938774, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 70.91047711, 0.00726843, 86.7179657, 0.08089308, 8.67179657, 0.32916035, -166.15364784, -0.00847828, -203.192912, -0.09847822, -20.3192912, -0.34674549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 70.91047711, 0.00726843, 86.7179657, 0.08029658, 8.67179657, 0.32381903, -166.15364784, -0.00847828, -203.192912, -0.09774905, -20.3192912, -0.3412715, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 28326415.78837269, 0.1125, 0.00189844, 0.00058594, 11802673.24515529, 0.00152995)
    ops.section('Aggregator', 2204991, 2204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2204992, 2204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.36681626306, 2204992, 0.36681626306, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 52.82917545, 0.01027257, 64.36012513, 0.09050528, 6.43601251, 0.36170197, -122.89227559, -0.01246051, -149.7157994, -0.11053826, -14.97157994, -0.38173495, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 52.82917545, 0.01027257, 64.36012513, 0.09143581, 6.43601251, 0.3626325, -122.89227559, -0.01246051, -149.7157994, -0.11167575, -14.97157994, -0.38287244, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 29723481.60724743, 0.07, 0.00071458, 0.00023333, 12384784.00301976, 0.00060032)
    ops.section('Aggregator', 2304991, 2304990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2304992, 2304991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.36873606144000004, 2304992, 0.36873606144000004, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 54.08563251, 0.01051637, 66.3485331, 0.09353731, 6.63485331, 0.36203315, -125.70641786, -0.01289102, -154.20798537, -0.11437714, -15.42079854, -0.38287297, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 54.08563251, 0.01051637, 66.3485331, 0.09469294, 6.63485331, 0.36318878, -125.70641786, -0.01289102, -154.20798537, -0.1157898, -15.42079854, -0.38428563, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 27054266.28154824, 0.07, 0.00071458, 0.00023333, 11272610.9506451, 0.00060032)
    ops.section('Aggregator', 2014991, 2014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2014992, 2014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.37244525302, 2014992, 0.37244525302, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 71.19794464, 0.00738375, 86.68556866, 0.078701, 8.66855687, 0.32687527, -166.93220723, -0.00856781, -203.24481815, -0.09574716, -20.32448181, -0.34392143, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 105.42994021, 0.00762887, 128.36401903, 0.08185546, 12.8364019, 0.32396108, -246.17560234, -0.00917603, -299.72595678, -0.09991179, -29.97259568, -0.34201741, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 29932335.00792857, 0.1125, 0.00189844, 0.00058594, 12471806.25330357, 0.00152995)
    ops.section('Aggregator', 2114991, 2114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2114992, 2114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.36856598686, 2114992, 0.36856598686, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 71.60967247, 0.0073259, 87.85543165, 0.08171236, 8.78554316, 0.32795297, -167.68627701, -0.00858192, -205.72849644, -0.09951313, -20.57284964, -0.34575374, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 106.20621638, 0.00756687, 130.30073539, 0.08569535, 13.03007354, 0.33115437, -247.41383848, -0.00920967, -303.54348548, -0.10471518, -30.35434855, -0.35017419, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 27006910.74711233, 0.1125, 0.00189844, 0.00058594, 11252879.47796347, 0.00152995)
    ops.section('Aggregator', 2214991, 2214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2214992, 2214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.36814661557, 2214992, 0.36814661557, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 52.10343913, 0.01043035, 63.60478591, 0.09406213, 6.36047859, 0.36543988, -121.16225742, -0.0126665, -147.90769232, -0.11489932, -14.79076923, -0.38627707, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 52.10343913, 0.01043035, 63.60478591, 0.09369979, 6.36047859, 0.36507754, -121.16225742, -0.0126665, -147.90769232, -0.11445638, -14.79076923, -0.38583414, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 29000185.96944083, 0.07, 0.00071458, 0.00023333, 12083410.82060034, 0.00060032)
    ops.section('Aggregator', 2314991, 2314990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2314992, 2314991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.36849004082, 2314992, 0.36849004082, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 53.7854852, 0.01020953, 65.70049905, 0.09202333, 6.5700499, 0.36241821, -125.05463481, -0.01244441, -152.75779116, -0.11245491, -15.27577912, -0.38284979, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 53.7854852, 0.01020953, 65.70049905, 0.09183258, 6.5700499, 0.36222746, -125.05463481, -0.01244441, -152.75779116, -0.11222174, -15.27577912, -0.38261662, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 28760931.22148825, 0.07, 0.00071458, 0.00023333, 11983721.34228677, 0.00060032)
    ops.section('Aggregator', 2024991, 2024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2024992, 2024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.36982949468, 2024992, 0.36982949468, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 107.53317525, 0.00748572, 131.64877311, 0.08404629, 13.16487731, 0.32864165, -250.39186495, -0.00908901, -306.54522886, -0.10267787, -30.65452289, -0.34727324, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 72.44137556, 0.00725232, 88.68721855, 0.08065315, 8.86872186, 0.33009645, -169.62484026, -0.00847981, -207.665235, -0.09820614, -20.7665235, -0.34764945, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 27893768.20597184, 0.1125, 0.00189844, 0.00058594, 11622403.41915494, 0.00152995)
    ops.section('Aggregator', 2124991, 2124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2124992, 2124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.36849166116, 2124992, 0.36849166116, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 105.80238011, 0.00756409, 129.15954081, 0.08195883, 12.91595408, 0.32417975, -246.82415198, -0.00913419, -301.31358195, -0.10007551, -30.1313582, -0.34229642, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 71.38836121, 0.00732319, 87.14820918, 0.07918706, 8.71482092, 0.33066405, -167.31900165, -0.00852474, -204.25670385, -0.09637229, -20.42567039, -0.34784928, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 28993714.39007951, 0.1125, 0.00189844, 0.00058594, 12080714.3291998, 0.00152995)
    ops.section('Aggregator', 2224991, 2224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2224992, 2224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.36807767234, 2224992, 0.36807767234, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 54.89404288, 0.0103306, 67.04065322, 0.09197709, 6.70406532, 0.36032073, -127.61753028, -0.01259372, -155.8559389, -0.1123997, -15.58559389, -0.38074333, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 54.89404288, 0.0103306, 67.04065322, 0.09222687, 6.70406532, 0.36057051, -127.61753028, -0.01259372, -155.8559389, -0.11270503, -15.58559389, -0.38104867, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 28838770.51543461, 0.07, 0.00071458, 0.00023333, 12016154.38143109, 0.00060032)
    ops.section('Aggregator', 2324991, 2324990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2324992, 2324991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.37265650021, 2324992, 0.37265650021, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)
