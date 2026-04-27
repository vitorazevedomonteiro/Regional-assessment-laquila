import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 61.83116677, 0.00712746, 74.94965025, 0.04871238, 7.49496502, 0.24674943, -61.83116677, -0.00712746, -74.94965025, -0.04871238, -7.49496502, -0.24674943, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 61.83116677, 0.00712746, 74.94965025, 0.04883926, 7.49496502, 0.2483126, -61.83116677, -0.00712746, -74.94965025, -0.04883926, -7.49496502, -0.2483126, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 31357574.65456474, 0.1125, 0.00189844, 0.00058594, 13065656.10606864, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32604149896, 1001992, 0.32604149896, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 63.08621551, 0.00707508, 76.94593851, 0.06193435, 7.69459385, 0.31268333, -63.08621551, -0.00707508, -76.94593851, -0.06193435, -7.69459385, -0.31268333, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 63.08621551, 0.00707508, 76.94593851, 0.06222861, 7.69459385, 0.31617972, -63.08621551, -0.00707508, -76.94593851, -0.06222861, -7.69459385, -0.31617972, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29311055.81244071, 0.1125, 0.00189844, 0.00058594, 12212939.9218503, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25866456221, 1101992, 0.25866456221, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 61.90946512, 0.00705494, 75.33050479, 0.05108657, 7.53305048, 0.2528756, -61.90946512, -0.00705494, -75.33050479, -0.05108657, -7.53305048, -0.2528756, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 61.90946512, 0.00705494, 75.33050479, 0.05139027, 7.53305048, 0.25649638, -61.90946512, -0.00705494, -75.33050479, -0.05139027, -7.53305048, -0.25649638, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 30139248.42676035, 0.1125, 0.00189844, 0.00058594, 12558020.17781681, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32536900835, 1201992, 0.32536900835, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 61.63438515, 0.0071602, 74.90269264, 0.05224619, 7.49026926, 0.25718786, -81.56282799, -0.00740161, -99.12121976, -0.05550246, -9.91212198, -0.26044413, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 61.63438515, 0.0071602, 74.90269264, 0.05187209, 7.49026926, 0.25280298, -81.56282799, -0.00740161, -99.12121976, -0.05510335, -9.91212198, -0.25603424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 30549720.87951912, 0.1125, 0.00189844, 0.00058594, 12729050.3664663, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32622380058, 1011992, 0.32622380058, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 63.58680328, 0.00734156, 77.00695035, 0.06008491, 7.70069504, 0.31130955, -84.15345865, -0.00758435, -101.91424758, -0.06385461, -10.19142476, -0.31507924, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 63.58680328, 0.00734156, 77.00695035, 0.06039588, 7.70069504, 0.31514826, -84.15345865, -0.00758435, -101.91424758, -0.06418637, -10.19142476, -0.31893875, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 31636051.02136238, 0.1125, 0.00189844, 0.00058594, 13181687.92556766, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.26195546697, 1111992, 0.26195546697, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 62.08767336, 0.00730769, 75.48255672, 0.04945973, 7.54825567, 0.24626439, -82.15957247, -0.00755332, -99.88479603, -0.05252403, -9.9884796, -0.24932869, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 62.08767336, 0.00730769, 75.48255672, 0.04970994, 7.54825567, 0.24929705, -82.15957247, -0.00755332, -99.88479603, -0.05279097, -9.9884796, -0.25237808, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 30424140.31534261, 0.1125, 0.00189844, 0.00058594, 12676725.13139276, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32792465542000004, 1211992, 0.32792465542000004, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 62.22193742, 0.00708667, 75.65437263, 0.05026399, 7.56543726, 0.24945343, -82.3370158, -0.00732842, -100.11188227, -0.05339297, -10.01118823, -0.25258241, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 62.24441852, 0.00710898, 75.68170694, 0.05047306, 7.56817069, 0.25568518, -62.24441852, -0.00710898, -75.68170694, -0.05047306, -7.56817069, -0.25568518, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 30386811.97515897, 0.1125, 0.00189844, 0.00058594, 12661171.65631624, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32621224459000003, 1021992, 0.32621224459000003, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 62.60422015, 0.0073065, 76.07299043, 0.06110215, 7.60729904, 0.31290734, -62.60422015, -0.0073065, -76.07299043, -0.06110215, -7.60729904, -0.31290734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 62.60422015, 0.0073065, 76.07299043, 0.06086981, 7.60729904, 0.31010292, -62.60422015, -0.0073065, -76.07299043, -0.06086981, -7.60729904, -0.31010292, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 30585239.47675258, 0.1125, 0.00189844, 0.00058594, 12743849.78198024, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.26028522722999997, 1121992, 0.26028522722999997, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 62.28347466, 0.00722255, 75.54958411, 0.04949623, 7.55495841, 0.24924229, -62.28347466, -0.00722255, -75.54958411, -0.04949623, -7.55495841, -0.24924229, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 62.24875757, 0.00720261, 75.50747243, 0.04981821, 7.55074724, 0.24947631, -82.37965651, -0.00744293, -99.92616537, -0.0529082, -9.99261654, -0.2525663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 31146549.81779546, 0.1125, 0.00189844, 0.00058594, 12977729.09074811, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32730165023, 1221992, 0.32730165023, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 62.88847227, 0.00706794, 76.42657496, 0.0497849, 7.6426575, 0.24914485, -62.88847227, -0.00706794, -76.42657496, -0.0497849, -7.6426575, -0.24914485, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 62.88847227, 0.00706794, 76.42657496, 0.05002196, 7.6426575, 0.25201633, -62.88847227, -0.00706794, -76.42657496, -0.05002196, -7.6426575, -0.25201633, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 30550477.18129831, 0.1125, 0.00189844, 0.00058594, 12729365.49220763, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32655145285, 1002992, 0.32655145285, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 62.51756511, 0.00715597, 75.72086063, 0.0590579, 7.57208606, 0.30842681, -62.51756511, -0.00715597, -75.72086063, -0.0590579, -7.57208606, -0.30842681, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 62.51756511, 0.00715597, 75.72086063, 0.05913078, 7.57208606, 0.30933112, -62.51756511, -0.00715597, -75.72086063, -0.05913078, -7.57208606, -0.30933112, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 31601104.29841587, 0.1125, 0.00189844, 0.00058594, 13167126.79100661, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25903891109, 1102992, 0.25903891109, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 60.6657584, 0.00711413, 73.66846456, 0.05100537, 7.36684646, 0.25385402, -60.6657584, -0.00711413, -73.66846456, -0.05100537, -7.36684646, -0.25385402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 60.6657584, 0.00711413, 73.66846456, 0.05101028, 7.36684646, 0.2539128, -60.6657584, -0.00711413, -73.66846456, -0.05101028, -7.36684646, -0.2539128, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 30799290.13042987, 0.1125, 0.00189844, 0.00058594, 12833037.55434578, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32461826714, 1202992, 0.32461826714, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 61.73528326, 0.00736118, 75.09529213, 0.05161709, 7.50952921, 0.25484429, -61.73528326, -0.00736118, -75.09529213, -0.05161709, -7.50952921, -0.25484429, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 61.68958002, 0.00734267, 75.03969835, 0.05143777, 7.50396983, 0.24901703, -81.62771457, -0.00758918, -99.29260462, -0.05463289, -9.92926046, -0.25221215, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 30242854.20837243, 0.1125, 0.00189844, 0.00058594, 12601189.25348851, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32775429446, 1012992, 0.32775429446, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 61.794832, 0.00726891, 74.98574906, 0.06262265, 7.49857491, 0.31877864, -81.77468059, -0.00751029, -99.23055829, -0.06656549, -9.92305583, -0.32272148, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 61.794832, 0.00726891, 74.98574906, 0.06215573, 7.49857491, 0.31321598, -81.77468059, -0.00751029, -99.23055829, -0.06606735, -9.92305583, -0.3171276, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 31026202.54772894, 0.1125, 0.00189844, 0.00058594, 12927584.39488706, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25934642469, 1112992, 0.25934642469, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 61.9671452, 0.00718238, 75.48742928, 0.05291021, 7.54874293, 0.25777177, -81.99799251, -0.00742886, -99.88870135, -0.05621449, -9.98887014, -0.26107605, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 61.99861038, 0.00720408, 75.52575967, 0.0518332, 7.55257597, 0.24902815, -61.99861038, -0.00720408, -75.52575967, -0.0518332, -7.55257597, -0.24902815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29747335.46254149, 0.1125, 0.00189844, 0.00058594, 12394723.10939229, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32668142269, 1212992, 0.32668142269, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 63.35405482, 0.00712814, 76.84123272, 0.04915868, 7.68412327, 0.24835449, -63.35405482, -0.00712814, -76.84123272, -0.04915868, -7.68412327, -0.24835449, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 63.35405482, 0.00712814, 76.84123272, 0.04936466, 7.68412327, 0.25088394, -63.35405482, -0.00712814, -76.84123272, -0.04936466, -7.68412327, -0.25088394, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 31174684.82105042, 0.1125, 0.00189844, 0.00058594, 12989452.00877101, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.32763022867, 1022992, 0.32763022867, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 60.68562542, 0.00705669, 73.60431592, 0.06197646, 7.36043159, 0.3180025, -60.68562542, -0.00705669, -73.60431592, -0.06197646, -7.36043159, -0.3180025, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 60.68562542, 0.00705669, 73.60431592, 0.0622137, 7.36043159, 0.32087092, -60.68562542, -0.00705669, -73.60431592, -0.0622137, -7.36043159, -0.32087092, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 31176441.34298767, 0.1125, 0.00189844, 0.00058594, 12990183.89291153, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.25620183496, 1122992, 0.25620183496, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 62.35242424, 0.00728041, 75.84170408, 0.05121275, 7.58417041, 0.25357202, -62.35242424, -0.00728041, -75.84170408, -0.05121275, -7.58417041, -0.25357202, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.35242424, 0.00728041, 75.84170408, 0.05128566, 7.58417041, 0.25444255, -62.35242424, -0.00728041, -75.84170408, -0.05128566, -7.58417041, -0.25444255, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 30261649.82692012, 0.1125, 0.00189844, 0.00058594, 12609020.76121672, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.32775970919, 1222992, 0.32775970919, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 66.00734997, 0.01318877, 80.05366148, 0.08917042, 8.00536615, 0.30740073, -88.93958928, -0.01416212, -107.86586305, -0.0957878, -10.7865863, -0.31401811, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 66.00734997, 0.01318877, 80.05366148, 0.0895464, 8.00536615, 0.31034695, -88.93958928, -0.01416212, -107.86586305, -0.09619171, -10.7865863, -0.31699226, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 31196817.86182863, 0.075, 0.0005625, 0.00039062, 12998674.10909526, 0.00077515)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30260058492, 6200992, 0.30260058492, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 39.32984378, 0.01197247, 47.60453253, 0.08103445, 4.76045325, 0.33041836, -58.43820886, -0.01282604, -70.73314683, -0.08869403, -7.07331468, -0.33807793, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 39.32984378, 0.01197247, 47.60453253, 0.08136865, 4.76045325, 0.33362467, -58.43820886, -0.01282604, -70.73314683, -0.08906115, -7.07331468, -0.34131717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 31798592.24531501, 0.075, 0.0005625, 0.00039062, 13249413.43554792, 0.00077515)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.26057206163, 6201992, 0.26057206163, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 63.71673861, 0.00718366, 77.11490563, 0.06118717, 7.71149056, 0.2616494, -95.15317088, -0.00759186, -115.16169776, -0.06691737, -11.51616978, -0.2673796, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 63.6937499, 0.00716394, 77.08708293, 0.06145828, 7.70870829, 0.26056025, -115.30802693, -0.00778394, -139.55465722, -0.07015254, -13.95546572, -0.26925451, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 31826730.41820456, 0.1125, 0.00189844, 0.00058594, 13261137.6742519, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32888354741000003, 2001992, 0.32888354741000003, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 107.88849832, 0.00771312, 130.95907461, 0.06726797, 13.09590746, 0.24627225, -145.99046245, -0.00816723, -177.20865672, -0.0721459, -17.72086567, -0.25115018, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 107.88849832, 0.00771312, 130.95907461, 0.06684832, 13.09590746, 0.24287501, -145.99046245, -0.00816723, -177.20865672, -0.07169508, -17.72086567, -0.24772177, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 30929131.31811226, 0.1125, 0.00189844, 0.00058594, 12887138.04921344, 0.00152995)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.37023932023, 2101992, 0.37023932023, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 107.3135745, 0.00758057, 130.22964946, 0.06716331, 13.02296495, 0.24610685, -145.1958481, -0.00802773, -176.20142176, -0.07203636, -17.62014218, -0.2509799, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 107.3135745, 0.00758057, 130.22964946, 0.06691135, 13.02296495, 0.24406513, -145.1958481, -0.00802773, -176.20142176, -0.07176569, -17.62014218, -0.24891946, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 31005500.56213451, 0.1125, 0.00189844, 0.00058594, 12918958.56755605, 0.00152995)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36837263712, 2201992, 0.36837263712, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 61.07268634, 0.00707376, 74.08820617, 0.06287459, 7.40882062, 0.2649054, -91.20420879, -0.00747739, -110.64121507, -0.06877736, -11.06412151, -0.27080816, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 61.03883887, 0.00705602, 74.04714529, 0.06353342, 7.40471453, 0.26739859, -110.50759197, -0.00766902, -134.05844327, -0.07254532, -13.40584433, -0.27641049, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 31115862.85594657, 0.1125, 0.00189844, 0.00058594, 12964942.8566444, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32506068336, 2301992, 0.32506068336, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 61.70510112, 0.00695057, 74.9916388, 0.06527809, 7.49916388, 0.2709739, -111.66951961, -0.00756678, -135.71455404, -0.07456834, -13.5714554, -0.28026414, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 61.72442955, 0.00697109, 75.0151291, 0.06404266, 7.50151291, 0.26324324, -92.15695605, -0.0073764, -112.00048353, -0.07007233, -11.20004835, -0.26927291, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 30536670.85113342, 0.1125, 0.00189844, 0.00058594, 12723612.85463893, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32482730718, 2011992, 0.32482730718, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 111.08038134, 0.00771627, 134.64912917, 0.07668764, 13.46491292, 0.28440582, -150.27066972, -0.00817058, -182.15471151, -0.08226525, -18.21547115, -0.28998342, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 111.08038134, 0.00771627, 134.64912917, 0.07222975, 13.46491292, 0.24950179, -150.27066972, -0.00817058, -182.15471151, -0.07747622, -18.21547115, -0.25474826, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 31354742.37811874, 0.1125, 0.00189844, 0.00058594, 13064475.99088281, 0.00152995)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.37293952912, 2111992, 0.37293952912, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 107.5114217, 0.0076182, 130.71759414, 0.07912589, 13.07175941, 0.28905692, -145.45075529, -0.00807236, -176.84607362, -0.08489174, -17.68460736, -0.29482277, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 107.5114217, 0.0076182, 130.71759414, 0.07390098, 13.07175941, 0.24925325, -145.45075529, -0.00807236, -176.84607362, -0.07927872, -17.68460736, -0.25463098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30395200.0712887, 0.1125, 0.00189844, 0.00058594, 12664666.69637029, 0.00152995)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36882526131, 2211992, 0.36882526131, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 61.876542, 0.00714445, 75.08299456, 0.06212814, 7.50829946, 0.26092553, -112.02178928, -0.00776637, -135.9308572, -0.07092682, -13.59308572, -0.26972421, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 61.91017781, 0.00716262, 75.12380934, 0.06176843, 7.51238093, 0.26120116, -92.45375607, -0.00757208, -112.18637369, -0.06755926, -11.21863737, -0.26699199, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 31034167.44691442, 0.1125, 0.00189844, 0.00058594, 12930903.10288101, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32669975972, 2311992, 0.32669975972, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 61.41740064, 0.00703335, 74.46270786, 0.05007072, 7.44627079, 0.25181553, -61.41740064, -0.00703335, -74.46270786, -0.05007072, -7.44627079, -0.25181553, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 61.3901069, 0.00701283, 74.42961682, 0.0504212, 7.44296168, 0.25232978, -81.24395841, -0.00724739, -98.50050764, -0.05355844, -9.85005076, -0.25546702, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 31297375.32201308, 0.1125, 0.00189844, 0.00058594, 13040573.05083879, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32479837770000003, 2002992, 0.32479837770000003, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 61.78391641, 0.00715018, 74.8487309, 0.0628693, 7.48487309, 0.26645238, -92.27144851, -0.00755519, -111.78315039, -0.06876538, -11.17831504, -0.27234846, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 61.74924394, 0.00713268, 74.8067266, 0.06292246, 7.48067266, 0.26316543, -111.80304041, -0.00774757, -135.44488878, -0.071834, -13.54448888, -0.27207697, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 31534825.82322795, 0.1125, 0.00189844, 0.00058594, 13139510.75967831, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.32650739397, 2102992, 0.32650739397, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 62.59596094, 0.00703601, 76.29625226, 0.06420951, 7.62962523, 0.26555922, -93.43375939, -0.00745342, -113.88347698, -0.07026132, -11.3883477, -0.27161103, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 62.58309259, 0.00701359, 76.28056744, 0.06421499, 7.62805674, 0.2618953, -113.21224179, -0.00764874, -137.99084844, -0.07335671, -13.79908484, -0.27103703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29551563.2053009, 0.1125, 0.00189844, 0.00058594, 12313151.33554204, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.32619258048, 2202992, 0.32619258048, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 62.51373136, 0.00715216, 75.89118892, 0.04986902, 7.58911889, 0.25014297, -62.51373136, -0.00715216, -75.89118892, -0.04986902, -7.58911889, -0.25014297, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 62.48800768, 0.00713062, 75.85996056, 0.05011291, 7.58599606, 0.2494167, -82.69367917, -0.0073712, -100.3894903, -0.05322767, -10.03894903, -0.25253147, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 30888689.29759804, 0.1125, 0.00189844, 0.00058594, 12870287.20733252, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32692252069, 2302992, 0.32692252069, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 62.01568913, 0.00714535, 75.24547139, 0.04914642, 7.52454714, 0.24675985, -82.07084497, -0.0073846, -99.57898562, -0.05219425, -9.95789856, -0.24980768, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 62.04767952, 0.00716568, 75.28428626, 0.04903363, 7.52842863, 0.24903645, -62.04767952, -0.00716568, -75.28428626, -0.04903363, -7.52842863, -0.24903645, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 31060681.02577576, 0.1125, 0.00189844, 0.00058594, 12941950.42740657, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.326561924, 2012992, 0.326561924, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 61.70504448, 0.00703632, 74.65635487, 0.06126044, 7.46563549, 0.26054639, -111.72552851, -0.00764129, -135.17566959, -0.06992922, -13.51756696, -0.26921517, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 61.7346518, 0.00705433, 74.69217649, 0.06094567, 7.46921765, 0.26121979, -92.20098721, -0.0074528, -111.55311009, -0.06665509, -11.15531101, -0.26692921, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 31920816.55499269, 0.1125, 0.00189844, 0.00058594, 13300340.23124696, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.32568602087, 2112992, 0.32568602087, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 61.64374946, 0.00701269, 75.05454812, 0.06331447, 7.50545481, 0.26194113, -111.55451029, -0.00763981, -135.8235577, -0.07231437, -13.58235577, -0.27094103, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 61.66693403, 0.00703326, 75.08277658, 0.06350873, 7.50827766, 0.26754197, -92.06772018, -0.00744564, -112.09735287, -0.06948673, -11.20973529, -0.27351997, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29925560.00175021, 0.1125, 0.00189844, 0.00058594, 12468983.33406259, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.3252351012, 2212992, 0.3252351012, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 62.26447211, 0.00718278, 75.3518123, 0.04948528, 7.53518123, 0.25013211, -82.40469029, -0.0074194, -99.7252935, -0.05255065, -9.97252935, -0.25319747, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 62.299338, 0.00720203, 75.39400664, 0.04930934, 7.53940066, 0.25168475, -62.299338, -0.00720203, -75.39400664, -0.04930934, -7.53940066, -0.25168475, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 31848091.25069907, 0.1125, 0.00189844, 0.00058594, 13270038.02112461, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32722271975, 2312992, 0.32722271975, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
