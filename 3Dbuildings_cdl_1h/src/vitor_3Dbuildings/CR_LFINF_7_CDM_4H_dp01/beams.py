import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 61.54238361, 0.00753218, 74.6763321, 0.06096432, 7.46763321, 0.25748973, -91.8633558, -0.00795458, -111.4681958, -0.06665241, -11.14681958, -0.26317782, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 61.54238361, 0.00753218, 74.6763321, 0.06155433, 7.46763321, 0.26326646, -91.8633558, -0.00795458, -111.4681958, -0.06730057, -11.14681958, -0.26901269, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 31039137.69219986, 0.1125, 0.00189844, 0.00058594, 12932974.03841661, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32926513797, 1001992, 0.32926513797, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 61.75083842, 0.00711228, 75.64453368, 0.08310044, 7.56445337, 0.34080104, -92.15711868, -0.00754724, -112.89210716, -0.09102397, -11.28921072, -0.34872457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 81.7131582, 0.00730706, 100.09829674, 0.08450372, 10.00982967, 0.34177437, -111.68914953, -0.00771556, -136.81876798, -0.09083425, -13.6818768, -0.3481049, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 27650184.77801726, 0.1125, 0.00189844, 0.00058594, 11520910.32417386, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25773925112, 1101992, 0.25773925112, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 82.04242588, 0.00746881, 99.79630567, 0.06284803, 9.97963057, 0.25943264, -112.21709346, -0.00786362, -136.5007341, -0.06749118, -13.65007341, -0.26407579, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 62.03679936, 0.00727379, 75.46148623, 0.06256136, 7.54614862, 0.26618271, -92.633089, -0.00769393, -112.67877522, -0.06843004, -11.26787752, -0.27205139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 30245380.70536662, 0.1125, 0.00189844, 0.00058594, 12602241.96056943, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32768187382999997, 1201992, 0.32768187382999997, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 162.87850093, 0.00804395, 198.45209288, 0.07599025, 19.84520929, 0.29696603, -219.53178828, -0.00867536, -267.47878075, -0.08166881, -26.74787807, -0.3026446, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 162.87850093, 0.00804395, 198.45209288, 0.07566742, 19.84520929, 0.29416084, -219.53178828, -0.00867536, -267.47878075, -0.081322, -26.74787807, -0.29981542, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29684396.16529671, 0.1125, 0.00189844, 0.00058594, 12368498.40220696, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.4096177923, 1011992, 0.4096177923, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 161.98024666, 0.00842563, 197.92509887, 0.08913723, 19.79250989, 0.34831303, -218.44388372, -0.00909256, -266.91851738, -0.09579954, -26.69185174, -0.35497534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 161.98024666, 0.00842563, 197.92509887, 0.08944484, 19.79250989, 0.35096987, -218.44388372, -0.00909256, -266.91851738, -0.09613, -26.69185174, -0.35765503, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 28643764.17872168, 0.1125, 0.00189844, 0.00058594, 11934901.74113403, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.34544944211, 1111992, 0.34544944211, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 160.70599131, 0.00800006, 194.94466286, 0.07482082, 19.49446629, 0.29791013, -216.71812029, -0.00860991, -262.89026656, -0.08039422, -26.28902666, -0.30348353, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 160.70599131, 0.00800006, 194.94466286, 0.07445419, 19.49446629, 0.29465093, -216.71812029, -0.00860991, -262.89026656, -0.08000036, -26.28902666, -0.3001971, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 31132196.51428558, 0.1125, 0.00189844, 0.00058594, 12971748.54761899, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.40800896242, 1211992, 0.40800896242, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 221.22709834, 0.00887522, 267.5660422, 0.07452385, 26.75660422, 0.29424841, -221.22709834, -0.00887522, -267.5660422, -0.07452385, -26.75660422, -0.29424841, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 221.22709834, 0.00887522, 267.5660422, 0.07475214, 26.75660422, 0.29629352, -221.22709834, -0.00887522, -267.5660422, -0.07475214, -26.75660422, -0.29629352, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 32024166.85178192, 0.1125, 0.00189844, 0.00058594, 13343402.85490914, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.41482172757, 1021992, 0.41482172757, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 221.36357475, 0.00873507, 268.83288668, 0.08865047, 26.88328867, 0.34871436, -221.36357475, -0.00873507, -268.83288668, -0.08865047, -26.88328867, -0.34871436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 221.36357475, 0.00873507, 268.83288668, 0.0895415, 26.88328867, 0.35653623, -221.36357475, -0.00873507, -268.83288668, -0.0895415, -26.88328867, -0.35653623, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 30771149.13984829, 0.1125, 0.00189844, 0.00058594, 12821312.14160345, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.34483975027999997, 1121992, 0.34483975027999997, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 215.93075639, 0.0085587, 264.25105843, 0.08145142, 26.42510584, 0.30509444, -215.93075639, -0.0085587, -264.25105843, -0.08145142, -26.42510584, -0.30509444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 215.93075639, 0.0085587, 264.25105843, 0.08195815, 26.42510584, 0.30930666, -215.93075639, -0.0085587, -264.25105843, -0.08195815, -26.42510584, -0.30930666, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 28052117.94016461, 0.1125, 0.00189844, 0.00058594, 11688382.47506859, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.40710027267, 1221992, 0.40710027267, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 106.40378755, 0.00757497, 129.04410741, 0.06596102, 12.90441074, 0.24227058, -143.98266789, -0.00801921, -174.61892371, -0.07074227, -17.46189237, -0.24705183, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 106.40378755, 0.00757497, 129.04410741, 0.0662489, 12.90441074, 0.24462752, -143.98266789, -0.00801921, -174.61892371, -0.07105153, -17.46189237, -0.24943015, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 31202389.20331807, 0.1125, 0.00189844, 0.00058594, 13000995.50138253, 0.00152995)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.36760515980999997, 1031992, 0.36760515980999997, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 108.89620322, 0.00742631, 132.15626557, 0.08070352, 13.21562656, 0.30053964, -147.26012272, -0.00786865, -178.71465956, -0.086589, -17.87146596, -0.30642512, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 108.89620322, 0.00742631, 132.15626557, 0.08078824, 13.21562656, 0.30122779, -147.26012272, -0.00786865, -178.71465956, -0.08668002, -17.87146596, -0.30711956, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 30991158.79088999, 0.1125, 0.00189844, 0.00058594, 12912982.8295375, 0.00152995)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.29995235166, 1131992, 0.29995235166, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 107.6039963, 0.00763058, 130.95747185, 0.06816589, 13.09574718, 0.2467818, -145.56739064, -0.00808819, -177.16012525, -0.07312015, -17.71601252, -0.25173606, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 107.6039963, 0.00763058, 130.95747185, 0.06771476, 13.09574718, 0.24318926, -145.56739064, -0.00808819, -177.16012525, -0.07263551, -17.71601252, -0.24811002, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 30070996.58728266, 0.1125, 0.00189844, 0.00058594, 12529581.91136778, 0.00152995)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.36897248246, 1231992, 0.36897248246, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 61.52367119, 0.00706963, 74.8452984, 0.06259802, 7.48452984, 0.26126225, -91.86289329, -0.00748094, -111.75382625, -0.06848161, -11.17538263, -0.26714583, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 61.52367119, 0.00706963, 74.8452984, 0.06277248, 7.48452984, 0.26292044, -91.86289329, -0.00748094, -111.75382625, -0.06867326, -11.17538263, -0.26882122, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 30209823.80767791, 0.1125, 0.00189844, 0.00058594, 12587426.58653246, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32542116263000004, 1002992, 0.32542116263000004, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 61.57554323, 0.00710941, 75.09468565, 0.0794807, 7.50946856, 0.33338881, -91.9288067, -0.00752925, -112.11212243, -0.08703267, -11.21121224, -0.34094078, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 61.54724808, 0.00708903, 75.06017819, 0.07959345, 7.50601782, 0.32967396, -111.37827277, -0.0077276, -135.83179202, -0.09101434, -13.5831792, -0.34109486, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29352462.8371346, 0.1125, 0.00189844, 0.00058594, 12230192.84880608, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25772191369, 1102992, 0.25772191369, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 61.49528223, 0.00703855, 75.16545997, 0.06704875, 7.516546, 0.27144327, -111.24812228, -0.00768495, -135.97817554, -0.07661943, -13.59781755, -0.28101395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 61.51742906, 0.00706051, 75.19252997, 0.06662207, 7.519253, 0.27137429, -91.82331312, -0.00748515, -112.2353019, -0.07291645, -11.22353019, -0.27766867, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 28523297.78031143, 0.1125, 0.00189844, 0.00058594, 11884707.4084631, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32515452496, 1202992, 0.32515452496, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 107.61871112, 0.00752253, 131.06390229, 0.06703822, 13.10639023, 0.24216085, -145.55062299, -0.00797742, -177.25944151, -0.07191403, -17.72594415, -0.24703665, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 107.61871112, 0.00752253, 131.06390229, 0.06756298, 13.10639023, 0.24637044, -145.55062299, -0.00797742, -177.25944151, -0.07247776, -17.72594415, -0.25128523, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29840912.30044897, 0.1125, 0.00189844, 0.00058594, 12433713.4585204, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36777651063000005, 1012992, 0.36777651063000005, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 108.40405772, 0.00772043, 131.8207902, 0.0811292, 13.18207902, 0.29945318, -146.66575892, -0.00818042, -178.34753277, -0.08704211, -17.83475328, -0.30536609, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 108.40405772, 0.00772043, 131.8207902, 0.08149426, 13.18207902, 0.30240249, -146.66575892, -0.00818042, -178.34753277, -0.08743429, -17.83475328, -0.30834252, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 30350456.77849919, 0.1125, 0.00189844, 0.00058594, 12646023.65770799, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.3026341811, 1112992, 0.3026341811, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 109.55450729, 0.00752576, 133.36807156, 0.06889179, 13.33680716, 0.24944639, -148.13120643, -0.00798175, -180.33008253, -0.07390615, -18.03300825, -0.25446075, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 109.55450729, 0.00752576, 133.36807156, 0.06856785, 13.33680716, 0.24686977, -148.13120643, -0.00798175, -180.33008253, -0.07355814, -18.03300825, -0.25186006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29977602.25262892, 0.1125, 0.00189844, 0.00058594, 12490667.60526205, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36937527006, 1212992, 0.36937527006, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 166.79546468, 0.0079431, 202.52391607, 0.07521979, 20.25239161, 0.29920435, -224.72036412, -0.00855827, -272.85662862, -0.08083237, -27.28566286, -0.30481693, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 166.79546468, 0.0079431, 202.52391607, 0.0752427, 20.25239161, 0.29940827, -224.72036412, -0.00855827, -272.85662862, -0.08085698, -27.28566286, -0.30502255, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 30832987.17640789, 0.1125, 0.00189844, 0.00058594, 12847077.99016996, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.41118878443, 1022992, 0.41118878443, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 161.80595683, 0.00791501, 197.19820288, 0.09209212, 19.71982029, 0.36416642, -218.03930895, -0.00853879, -265.73162523, -0.09896871, -26.57316252, -0.371043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 161.80595683, 0.00791501, 197.19820288, 0.09180331, 19.71982029, 0.36166847, -218.03930895, -0.00853879, -265.73162523, -0.09865844, -26.57316252, -0.36852361, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29590716.44473122, 0.1125, 0.00189844, 0.00058594, 12329465.18530468, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.33924203558, 1122992, 0.33924203558, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 165.03346058, 0.00798936, 201.25078054, 0.07546138, 20.12507805, 0.29401483, -222.32540178, -0.00862306, -271.11569062, -0.08110701, -27.11156906, -0.29966045, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 165.03346058, 0.00798936, 201.25078054, 0.07556584, 20.12507805, 0.29492279, -222.32540178, -0.00862306, -271.11569062, -0.08121923, -27.11156906, -0.30057618, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29381525.062903, 0.1125, 0.00189844, 0.00058594, 12242302.10954292, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.41023913706000004, 1222992, 0.41023913706000004, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 108.47849191, 0.00760378, 131.99118877, 0.06689038, 13.19911888, 0.242639, -146.73007976, -0.00806054, -178.53380256, -0.07175103, -17.85338026, -0.24749966, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 108.47849191, 0.00760378, 131.99118877, 0.06693228, 13.19911888, 0.24297575, -146.73007976, -0.00806054, -178.53380256, -0.07179606, -17.85338026, -0.24783952, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 30148926.83198217, 0.1125, 0.00189844, 0.00058594, 12562052.84665924, 0.00152995)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.36940543883, 1032992, 0.36940543883, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 106.15247768, 0.00762183, 129.03206197, 0.08243448, 12.9032062, 0.30421962, -143.63537978, -0.00807382, -174.59384492, -0.08844367, -17.45938449, -0.31022881, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 106.15247768, 0.00762183, 129.03206197, 0.08261612, 12.9032062, 0.30568068, -143.63537978, -0.00807382, -174.59384492, -0.0886388, -17.45938449, -0.31170336, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 30479769.31012485, 0.1125, 0.00189844, 0.00058594, 12699903.87921869, 0.00152995)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.29976715234, 1132992, 0.29976715234, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 109.55168711, 0.00749048, 133.48511959, 0.06937003, 13.34851196, 0.25021595, -148.10243772, -0.00794761, -180.45793845, -0.07442366, -18.04579384, -0.25526958, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 109.55168711, 0.00749048, 133.48511959, 0.0689236, 13.34851196, 0.24668991, -148.10243772, -0.00794761, -180.45793845, -0.07394407, -18.04579384, -0.25171039, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 29666870.76812652, 0.1125, 0.00189844, 0.00058594, 12361196.15338605, 0.00152995)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.36892031664, 1232992, 0.36892031664, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 62.93008507, 0.00721299, 76.56207444, 0.06171829, 7.65620744, 0.25833049, -93.96117545, -0.00763318, -114.31515627, -0.06750993, -11.43151563, -0.26412213, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 62.93008507, 0.00721299, 76.56207444, 0.06212092, 7.65620744, 0.26219577, -93.96117545, -0.00763318, -114.31515627, -0.06795224, -11.43151563, -0.26802709, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 30184356.5983137, 0.1125, 0.00189844, 0.00058594, 12576815.24929737, 0.00152995)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32813124409, 1003992, 0.32813124409, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 61.44826731, 0.00722889, 75.01651801, 0.07931128, 7.5016518, 0.33144368, -91.73841458, -0.00765633, -111.9949631, -0.08684238, -11.19949631, -0.33897477, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 61.44826731, 0.00722889, 75.01651801, 0.07927565, 7.5016518, 0.33111255, -91.73841458, -0.00765633, -111.9949631, -0.08680324, -11.19949631, -0.33864013, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 28979993.30370909, 0.1125, 0.00189844, 0.00058594, 12074997.20987879, 0.00152995)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25854002304, 1103992, 0.25854002304, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 62.36997842, 0.00724575, 76.14682616, 0.06422617, 7.61468262, 0.26385942, -93.111116, -0.00767614, -113.67834563, -0.07027193, -11.36783456, -0.26990518, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 62.36997842, 0.00724575, 76.14682616, 0.0639044, 7.61468262, 0.26087384, -93.111116, -0.00767614, -113.67834563, -0.06991845, -11.36783456, -0.26688789, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 28955442.5912298, 0.1125, 0.00189844, 0.00058594, 12064767.74634575, 0.00152995)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32767499493, 1203992, 0.32767499493, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 60.19329663, 0.00724573, 73.30255726, 0.05303175, 7.33025573, 0.25798731, -79.64068572, -0.00748973, -96.9853165, -0.05633743, -9.69853165, -0.26129299, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 60.19329663, 0.00724573, 73.30255726, 0.05298025, 7.33025573, 0.25738937, -79.64068572, -0.00748973, -96.9853165, -0.05628248, -9.69853165, -0.2606916, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29860133.11424931, 0.1125, 0.00189844, 0.00058594, 12441722.13093721, 0.00152995)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32527207533, 1013992, 0.32527207533, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 61.9300328, 0.0069661, 75.20020487, 0.06186232, 7.52002049, 0.31552733, -81.94999048, -0.00720289, -99.50997592, -0.06576998, -9.95099759, -0.31943499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 61.9300328, 0.0069661, 75.20020487, 0.06169557, 7.52002049, 0.31353666, -81.94999048, -0.00720289, -99.50997592, -0.06559208, -9.95099759, -0.31743317, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 30814181.50526599, 0.1125, 0.00189844, 0.00058594, 12839242.29386083, 0.00152995)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25691561028000004, 1113992, 0.25691561028000004, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 62.43918718, 0.00732064, 76.07661606, 0.05063186, 7.60766161, 0.24903452, -82.62184939, -0.00757098, -100.66740133, -0.05377839, -10.06674013, -0.25218105, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 62.43918718, 0.00732064, 76.07661606, 0.05049631, 7.60766161, 0.24742924, -82.62184939, -0.00757098, -100.66740133, -0.05363378, -10.06674013, -0.25056671, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 29682773.26743531, 0.1125, 0.00189844, 0.00058594, 12367822.19476471, 0.00152995)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32833562759, 1213992, 0.32833562759, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 108.01785995, 0.00779477, 131.62240254, 0.06812455, 13.16224025, 0.24538148, -146.14348391, -0.00826378, -178.07940721, -0.07307495, -17.80794072, -0.25033188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 108.01785995, 0.00779477, 131.62240254, 0.06853228, 13.16224025, 0.24864405, -146.14348391, -0.00826378, -178.07940721, -0.07351296, -17.80794072, -0.25362474, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 29650449.37222469, 0.1125, 0.00189844, 0.00058594, 12354353.90509362, 0.00152995)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.37097212201, 1023992, 0.37097212201, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 107.90998957, 0.00764073, 131.05812399, 0.08180447, 13.1058124, 0.30336961, -145.99938088, -0.00809327, -177.31819862, -0.087766, -17.73181986, -0.30933114, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 107.90998957, 0.00764073, 131.05812399, 0.0808776, 13.1058124, 0.29593061, -145.99938088, -0.00809327, -177.31819862, -0.08677029, -17.73181986, -0.3018233, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 30751941.09576503, 0.1125, 0.00189844, 0.00058594, 12813308.7899021, 0.00152995)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.3014554177, 1123992, 0.3014554177, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 107.13527829, 0.00748635, 130.41192812, 0.0686594, 13.04119281, 0.24831572, -144.90180442, -0.00793766, -176.38376457, -0.07365473, -17.63837646, -0.25331105, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 107.13527829, 0.00748635, 130.41192812, 0.06824856, 13.04119281, 0.24505597, -144.90180442, -0.00793766, -176.38376457, -0.07321338, -17.63837646, -0.25002078, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 30006383.55945006, 0.1125, 0.00189844, 0.00058594, 12502659.81643752, 0.00152995)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36702859645, 1223992, 0.36702859645, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 62.47890443, 0.0072165, 75.99444694, 0.0644368, 7.59944469, 0.2684202, -93.29203056, -0.0076352, -113.47312075, -0.07049453, -11.34731207, -0.27447793, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 62.47890443, 0.0072165, 75.99444694, 0.06395033, 7.59944469, 0.26384401, -93.29203056, -0.0076352, -113.47312075, -0.06996012, -11.34731207, -0.2698538, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 30266462.69134067, 0.1125, 0.00189844, 0.00058594, 12611026.12139195, 0.00152995)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32768664949, 1033992, 0.32768664949, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 63.24955326, 0.00717445, 77.35132921, 0.07892186, 7.73513292, 0.3284603, -94.39258514, -0.00760934, -115.43784188, -0.0864274, -11.54378419, -0.33596584, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 63.24955326, 0.00717445, 77.35132921, 0.07963727, 7.73513292, 0.33511839, -94.39258514, -0.00760934, -115.43784188, -0.08721331, -11.54378419, -0.34269443, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 28316007.2499059, 0.1125, 0.00189844, 0.00058594, 11798336.35412746, 0.00152995)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25992730389, 1133992, 0.25992730389, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 61.87859527, 0.00729156, 75.23107736, 0.06410591, 7.52310774, 0.26743065, -92.39769033, -0.00771071, -112.33574, -0.07012406, -11.233574, -0.27344881, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 61.87859527, 0.00729156, 75.23107736, 0.06371174, 7.52310774, 0.26370621, -92.39769033, -0.00771071, -112.33574, -0.06969105, -11.233574, -0.26968552, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 30412322.98398764, 0.1125, 0.00189844, 0.00058594, 12671801.24332818, 0.00152995)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32767069799000004, 1233992, 0.32767069799000004, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 62.11534122, 0.00725224, 75.68880079, 0.05003288, 7.56888008, 0.2476362, -62.11534122, -0.00725224, -75.68880079, -0.05003288, -7.56888008, -0.2476362, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 62.11534122, 0.00725224, 75.68880079, 0.0501031, 7.56888008, 0.2484767, -62.11534122, -0.00725224, -75.68880079, -0.0501031, -7.56888008, -0.2484767, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 29651650.76382769, 0.1125, 0.00189844, 0.00058594, 12354854.4849282, 0.00152995)
    ops.section('Aggregator', 1004991, 1004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1004992, 1004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.32719837638000004, 1004992, 0.32719837638000004, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 61.94999259, 0.00716175, 75.32817426, 0.06247259, 7.53281743, 0.31748762, -61.94999259, -0.00716175, -75.32817426, -0.06247259, -7.53281743, -0.31748762, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 61.94999259, 0.00716175, 75.32817426, 0.06258412, 7.53281743, 0.31882059, -61.94999259, -0.00716175, -75.32817426, -0.06258412, -7.53281743, -0.31882059, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 30367322.05472877, 0.1125, 0.00189844, 0.00058594, 12653050.85613699, 0.00152995)
    ops.section('Aggregator', 1104991, 1104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1104992, 1104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.25834608302, 1104992, 0.25834608302, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 62.04438534, 0.0073175, 75.50025717, 0.05125993, 7.55002572, 0.25328171, -62.04438534, -0.0073175, -75.50025717, -0.05125993, -7.55002572, -0.25328171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 62.04438534, 0.0073175, 75.50025717, 0.05103619, 7.55002572, 0.25062646, -62.04438534, -0.0073175, -75.50025717, -0.05103619, -7.55002572, -0.25062646, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 30114395.13817129, 0.1125, 0.00189844, 0.00058594, 12547664.6409047, 0.00152995)
    ops.section('Aggregator', 1204991, 1204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1204992, 1204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.3277182183, 1204992, 0.3277182183, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 63.81019199, 0.00727657, 77.31122781, 0.04936442, 7.73112278, 0.24997052, -63.81019199, -0.00727657, -77.31122781, -0.04936442, -7.73112278, -0.24997052, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 63.81019199, 0.00727657, 77.31122781, 0.04905656, 7.73112278, 0.2461994, -63.81019199, -0.00727657, -77.31122781, -0.04905656, -7.73112278, -0.2461994, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 31504525.99561806, 0.1125, 0.00189844, 0.00058594, 13126885.83150753, 0.00152995)
    ops.section('Aggregator', 1014991, 1014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1014992, 1014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.32942179498, 1014992, 0.32942179498, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 61.27704232, 0.00717699, 74.33459456, 0.06044387, 7.43345946, 0.31193477, -61.27704232, -0.00717699, -74.33459456, -0.06044387, -7.43345946, -0.31193477, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 61.27704232, 0.00717699, 74.33459456, 0.06052441, 7.43345946, 0.31291819, -61.27704232, -0.00717699, -74.33459456, -0.06052441, -7.43345946, -0.31291819, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 31122229.68954979, 0.1125, 0.00189844, 0.00058594, 12967595.70397908, 0.00152995)
    ops.section('Aggregator', 1114991, 1114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1114992, 1114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.25783583997, 1114992, 0.25783583997, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 61.29917015, 0.00731448, 74.80522338, 0.05240886, 7.48052234, 0.25512376, -61.29917015, -0.00731448, -74.80522338, -0.05240886, -7.48052234, -0.25512376, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 61.29917015, 0.00731448, 74.80522338, 0.05246213, 7.48052234, 0.25574552, -61.29917015, -0.00731448, -74.80522338, -0.05246213, -7.48052234, -0.25574552, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 29123122.87390164, 0.1125, 0.00189844, 0.00058594, 12134634.53079235, 0.00152995)
    ops.section('Aggregator', 1214991, 1214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1214992, 1214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.32676693826000003, 1214992, 0.32676693826000003, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 62.41810472, 0.00712364, 76.17723555, 0.05119193, 7.61772356, 0.25092408, -62.41810472, -0.00712364, -76.17723555, -0.05119193, -7.61772356, -0.25092408, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 62.40195103, 0.00709924, 76.15752103, 0.05133066, 7.6157521, 0.24892046, -82.56263004, -0.00734822, -100.762318, -0.05453737, -10.0762318, -0.25212717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 29091844.98056277, 0.1125, 0.00189844, 0.00058594, 12121602.07523449, 0.00152995)
    ops.section('Aggregator', 1024991, 1024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1024992, 1024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.32636208004000006, 1024992, 0.32636208004000006, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 62.38532824, 0.00722192, 75.83336806, 0.06232539, 7.58333681, 0.31605101, -82.5562361, -0.00746616, -100.35240039, -0.06625437, -10.03524004, -0.31997998, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 62.38532824, 0.00722192, 75.83336806, 0.06262655, 7.58333681, 0.31965386, -82.5562361, -0.00746616, -100.35240039, -0.06657566, -10.03524004, -0.32360297, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 30471951.39320091, 0.1125, 0.00189844, 0.00058594, 12696646.41383371, 0.00152995)
    ops.section('Aggregator', 1124991, 1124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1124992, 1124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.25953997569000004, 1124992, 0.25953997569000004, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 61.17456012, 0.0071313, 74.71390083, 0.0523594, 7.47139008, 0.25342612, -80.9430162, -0.00738033, -98.85757206, -0.0556328, -9.88575721, -0.25669952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 61.20601162, 0.00715365, 74.75231327, 0.05220353, 7.47523133, 0.25532822, -61.20601162, -0.00715365, -74.75231327, -0.05220353, -7.47523133, -0.25532822, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 28823735.29902097, 0.1125, 0.00189844, 0.00058594, 12009889.70792541, 0.00152995)
    ops.section('Aggregator', 1224991, 1224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1224992, 1224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.32530007493, 1224992, 0.32530007493, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 62.25272838, 0.0072967, 75.79359781, 0.05083109, 7.57935978, 0.25129442, -62.25272838, -0.0072967, -75.79359781, -0.05083109, -7.57935978, -0.25129442, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 62.25272838, 0.0072967, 75.79359781, 0.05064457, 7.57935978, 0.24907663, -62.25272838, -0.0072967, -75.79359781, -0.05064457, -7.57935978, -0.24907663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 29936429.84238296, 0.1125, 0.00189844, 0.00058594, 12473512.43432623, 0.00152995)
    ops.section('Aggregator', 1034991, 1034990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1034992, 1034991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.32775033693, 1034992, 0.32775033693, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 61.38797935, 0.00718308, 74.73600622, 0.06280588, 7.47360062, 0.31735497, -61.38797935, -0.00718308, -74.73600622, -0.06280588, -7.47360062, -0.31735497, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 61.38797935, 0.00718308, 74.73600622, 0.06275018, 7.47360062, 0.31669506, -61.38797935, -0.00718308, -74.73600622, -0.06275018, -7.47360062, -0.31669506, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 29958074.8589291, 0.1125, 0.00189844, 0.00058594, 12482531.19122046, 0.00152995)
    ops.section('Aggregator', 1134991, 1134990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1134992, 1134991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.25787622734000004, 1134992, 0.25787622734000004, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 63.41851937, 0.00703333, 77.45027099, 0.05196047, 7.7450271, 0.25355789, -63.41851937, -0.00703333, -77.45027099, -0.05196047, -7.7450271, -0.25355789, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 63.41851937, 0.00703333, 77.45027099, 0.05177257, 7.7450271, 0.25137572, -63.41851937, -0.00703333, -77.45027099, -0.05177257, -7.7450271, -0.25137572, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 28844061.95312088, 0.1125, 0.00189844, 0.00058594, 12018359.1471337, 0.00152995)
    ops.section('Aggregator', 1234991, 1234990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1234992, 1234991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.32657809042999997, 1234992, 0.32657809042999997, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 79.86376149, 0.01064175, 97.14249947, 0.08680117, 9.71424995, 0.3040166, -121.97524158, -0.01167609, -148.36491069, -0.09588016, -14.83649107, -0.3130956, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 79.86376149, 0.01064175, 97.14249947, 0.08681247, 9.71424995, 0.3041044, -121.97524158, -0.01167609, -148.36491069, -0.09589266, -14.83649107, -0.31318459, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 30257994.02979482, 0.0875, 0.00089323, 0.00045573, 12607497.51241451, 0.0010204)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30228521014, 6200992, 0.30228521014, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 142.65799476, 0.00930863, 174.25027579, 0.09287964, 17.42502758, 0.35509938, -191.9885213, -0.01010811, -234.50527845, -0.0998869, -23.45052785, -0.36210664, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 142.65799476, 0.00930863, 174.25027579, 0.09321157, 17.42502758, 0.35790856, -191.9885213, -0.01010811, -234.50527845, -0.10024349, -23.45052785, -0.36494047, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 28783518.17491947, 0.1, 0.00133333, 0.00052083, 11993132.57288311, 0.00127345)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.34164340892, 6201992, 0.34164340892, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 94.75291289, 0.00866502, 115.43078056, 0.08650666, 11.54307806, 0.30903363, -144.78884389, -0.00946551, -176.38602082, -0.0955295, -17.63860208, -0.31805647, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 94.75291289, 0.00866502, 115.43078056, 0.0863714, 11.54307806, 0.30798225, -144.78884389, -0.00946551, -176.38602082, -0.09537995, -17.63860208, -0.3169908, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 29734643.96180458, 0.1, 0.00133333, 0.00052083, 12389434.98408524, 0.00127345)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.30048354489, 6202992, 0.30048354489, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 6203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6203990, 38.23493244, 0.01190148, 46.71652819, 0.08845939, 4.67165282, 0.34491295, -56.79137937, -0.01279609, -69.38932295, -0.09689873, -6.9389323, -0.35335229, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6203991, 38.1873199, 0.01186619, 46.65835384, 0.0893036, 4.66583538, 0.34518627, -68.70236403, -0.01321428, -83.94250286, -0.10216761, -8.39425029, -0.35805028, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6203990, 28668620.11695839, 0.075, 0.0005625, 0.00039062, 11945258.382066, 0.00077515)
    ops.section('Aggregator', 6203991, 6203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6203992, 6203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6203, 6203991, 0.25794833643, 6203992, 0.25794833643, 6203990)
    # Create element
    ops.element('forceBeamColumn', 6203, 1104, 1204, 6203, 6203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 104.88753172, 0.00744135, 127.88348338, 0.06965712, 12.78834834, 0.24979529, -141.87374709, -0.00789301, -172.97870092, -0.07473027, -17.29787009, -0.25486844, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 104.88753172, 0.00744135, 127.88348338, 0.06944364, 12.78834834, 0.24811901, -141.87374709, -0.00789301, -172.97870092, -0.07450092, -17.29787009, -0.2531763, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29442882.91714124, 0.1125, 0.00189844, 0.00058594, 12267867.88214218, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36462616774000006, 2001992, 0.36462616774000006, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 187.6689108, 0.00692989, 228.14760807, 0.06731772, 22.81476081, 0.25757123, -253.43273444, -0.00738761, -308.09616746, -0.07226114, -30.80961675, -0.26251465, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 187.6689108, 0.00692989, 228.14760807, 0.06711884, 22.81476081, 0.25588942, -253.43273444, -0.00738761, -308.09616746, -0.07204748, -30.80961675, -0.26081806, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 30437466.4637251, 0.15, 0.003125, 0.001125, 12682277.69321879, 0.00281737)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41155742312000004, 2101992, 0.41155742312000004, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 189.70143443, 0.00691895, 231.60936121, 0.06868491, 23.16093612, 0.25810627, -256.00476746, -0.00739067, -312.56010708, -0.0737447, -31.25601071, -0.26316606, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 189.70143443, 0.00691895, 231.60936121, 0.06822759, 23.16093612, 0.25433899, -256.00476746, -0.00739067, -312.56010708, -0.07325341, -31.25601071, -0.25936481, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 28947561.95073008, 0.15, 0.003125, 0.001125, 12061484.14613753, 0.00281737)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41215472307, 2201992, 0.41215472307, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 107.21914547, 0.00772914, 130.39044345, 0.06705256, 13.03904435, 0.24347926, -145.0799586, -0.00818834, -176.43341639, -0.0719184, -17.64334164, -0.2483451, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 107.21914547, 0.00772914, 130.39044345, 0.06749277, 13.03904435, 0.24704079, -145.0799586, -0.00818834, -176.43341639, -0.07239131, -17.64334164, -0.25193932, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 30323772.72118226, 0.1125, 0.00189844, 0.00058594, 12634905.30049261, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36974790006, 2301992, 0.36974790006, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 107.13674635, 0.00767711, 130.69891416, 0.06882158, 13.06989142, 0.24657796, -144.9279855, -0.00814365, -176.8014335, -0.07383002, -17.68014335, -0.2515864, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 107.13674635, 0.00767711, 130.69891416, 0.06934859, 13.06989142, 0.2507608, -144.9279855, -0.00814365, -176.8014335, -0.07439618, -17.68014335, -0.25580839, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29242974.95964629, 0.1125, 0.00189844, 0.00058594, 12184572.89985262, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36892917478, 2011992, 0.36892917478, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 188.41408045, 0.00704848, 229.56276417, 0.0685095, 22.95627642, 0.25968831, -254.44646499, -0.0075192, -310.01628804, -0.07354563, -31.0016288, -0.26472445, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 188.42631961, 0.0069984, 229.5776763, 0.06959107, 22.95776763, 0.26125829, -313.52548447, -0.0078114, -381.99786704, -0.07841914, -38.1997867, -0.27008636, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29687463.05855842, 0.15, 0.003125, 0.001125, 12369776.27439934, 0.00281737)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41355593173, 2111992, 0.41355593173, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 187.99736838, 0.00667436, 228.82490381, 0.06740193, 22.88249038, 0.25652737, -253.63685159, -0.00712286, -308.71936489, -0.07236136, -30.87193649, -0.2614868, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 188.17309735, 0.00662202, 229.03879598, 0.06915331, 22.9038796, 0.26378567, -312.55404992, -0.00739738, -380.43165725, -0.07793587, -38.04316572, -0.27256823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30032363.13437114, 0.15, 0.003125, 0.001125, 12513484.63932131, 0.00281737)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40774813089000006, 2211992, 0.40774813089000006, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 107.50316963, 0.00732987, 131.30703588, 0.0704749, 13.13070359, 0.25126557, -145.28901734, -0.00778525, -177.4596068, -0.07562078, -17.74596068, -0.25641146, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 107.50316963, 0.00732987, 131.30703588, 0.07073779, 13.13070359, 0.25331904, -145.28901734, -0.00778525, -177.4596068, -0.07590321, -17.74596068, -0.25848445, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28792664.39687918, 0.1125, 0.00189844, 0.00058594, 11996943.49869966, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36535520624, 2311992, 0.36535520624, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 109.83184323, 0.00762142, 133.41995469, 0.06798, 13.34199547, 0.2484183, -148.55689022, -0.00807586, -180.46181307, -0.07291797, -18.04618131, -0.25335626, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 109.83184323, 0.00762142, 133.41995469, 0.06750248, 13.34199547, 0.24457295, -148.55689022, -0.00807586, -180.46181307, -0.07240498, -18.04618131, -0.24947545, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 30685226.7643508, 0.1125, 0.00189844, 0.00058594, 12785511.15181283, 0.00152995)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.37078244238, 2021992, 0.37078244238, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 184.60933905, 0.00687346, 225.32193922, 0.07073683, 22.53219392, 0.26281148, -307.11444804, -0.00768177, -374.84356615, -0.07972293, -37.48435662, -0.27179758, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 184.59050258, 0.0069239, 225.29894867, 0.06906212, 22.52989487, 0.25653837, -249.25241188, -0.00739166, -304.22099493, -0.0741456, -30.42209949, -0.26162185, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29062272.36129192, 0.15, 0.003125, 0.001125, 12109280.1505383, 0.00281737)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.40933116925, 2121992, 0.40933116925, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 185.42205787, 0.0066807, 226.80754052, 0.07202641, 22.68075405, 0.2651212, -307.98819513, -0.00748736, -376.72996325, -0.08120069, -37.67299633, -0.27429547, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 185.27958846, 0.00673537, 226.6332725, 0.07048829, 22.66332725, 0.26017479, -249.96192668, -0.00720148, -305.7524572, -0.07569006, -30.57524572, -0.26537657, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 28239063.10018378, 0.15, 0.003125, 0.001125, 11766276.29174324, 0.00281737)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.40667261153, 2221992, 0.40667261153, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 108.09016868, 0.00767881, 131.50702195, 0.06717499, 13.15070219, 0.2436411, -146.23163495, -0.00813814, -177.91152575, -0.07205379, -17.79115257, -0.2485199, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 108.09016868, 0.00767881, 131.50702195, 0.06773965, 13.15070219, 0.2482044, -146.23163495, -0.00813814, -177.91152575, -0.0726604, -17.79115257, -0.25312514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 30178673.73857291, 0.1125, 0.00189844, 0.00058594, 12574447.39107205, 0.00152995)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.36990300738000004, 2321992, 0.36990300738000004, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 110.67052122, 0.0075674, 134.57555535, 0.06659348, 13.45755553, 0.24255184, -149.64240968, -0.00802321, -181.96544268, -0.07143384, -18.19654427, -0.24739219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 110.67052122, 0.0075674, 134.57555535, 0.0664807, 13.45755553, 0.24164259, -149.64240968, -0.00802321, -181.96544268, -0.07131268, -18.19654427, -0.24647457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 30353610.12037832, 0.1125, 0.00189844, 0.00058594, 12647337.55015763, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.37078800271, 2002992, 0.37078800271, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 185.14698781, 0.00710909, 224.89828883, 0.07321579, 22.48982888, 0.29642106, -249.84892654, -0.00762292, -303.49181863, -0.07864013, -30.34918186, -0.3018454, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 185.14698781, 0.00710909, 224.89828883, 0.07339154, 22.48982888, 0.298007, -249.84892654, -0.00762292, -303.49181863, -0.07882894, -30.34918186, -0.30344439, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 30702278.71408698, 0.125, 0.00260417, 0.00065104, 12792616.13086958, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.41135460566000004, 2102992, 0.41135460566000004, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 185.02524453, 0.00714114, 225.61744567, 0.07484747, 22.56174457, 0.29780079, -249.61678876, -0.00766969, -304.3795587, -0.08040534, -30.43795587, -0.30335867, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 185.02524453, 0.00714114, 225.61744567, 0.07466972, 22.56174457, 0.29623711, -249.61678876, -0.00766969, -304.3795587, -0.08021439, -30.43795587, -0.30178178, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29401096.86954869, 0.125, 0.00260417, 0.00065104, 12250457.02897862, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.41139160308, 2202992, 0.41139160308, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 106.46345119, 0.00759803, 129.94302132, 0.06890036, 12.99430213, 0.24626129, -144.00411645, -0.00806195, -175.76294743, -0.07391791, -17.57629474, -0.25127884, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 106.46345119, 0.00759803, 129.94302132, 0.06916916, 12.99430213, 0.24838044, -144.00411645, -0.00806195, -175.76294743, -0.07420668, -17.57629474, -0.25341796, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29060078.19639111, 0.1125, 0.00189844, 0.00058594, 12108365.91516296, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.36750459459, 2302992, 0.36750459459, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 106.61970906, 0.00761192, 130.05463578, 0.06878258, 13.00546358, 0.24648667, -144.22322744, -0.00807462, -175.92337739, -0.07378913, -17.59233774, -0.25149322, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 106.61970906, 0.00761192, 130.05463578, 0.06933576, 13.00546358, 0.25087551, -144.22322744, -0.00807462, -175.92337739, -0.0743834, -17.59233774, -0.25592315, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29280396.52626333, 0.1125, 0.00189844, 0.00058594, 12200165.21927639, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.36782235025, 2012992, 0.36782235025, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 187.68020882, 0.00703741, 228.15290644, 0.07184256, 22.81529064, 0.2900069, -253.12378219, -0.00755139, -307.70919832, -0.07717037, -30.77091983, -0.29533471, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 187.68020882, 0.00703741, 228.15290644, 0.07177367, 22.81529064, 0.28938824, -253.12378219, -0.00755139, -307.70919832, -0.07709636, -30.77091983, -0.29471093, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 30449593.21904457, 0.125, 0.00260417, 0.00065104, 12687330.50793524, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.41169259156, 2112992, 0.41169259156, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 189.73273767, 0.00724548, 230.16288565, 0.07041597, 23.01628856, 0.28721484, -256.03993248, -0.00776578, -310.59948021, -0.07562866, -31.05994802, -0.29242753, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 189.73273767, 0.00724548, 230.16288565, 0.07012582, 23.01628856, 0.28457002, -256.03993248, -0.00776578, -310.59948021, -0.07531696, -31.05994802, -0.28976116, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 31122345.57374586, 0.125, 0.00260417, 0.00065104, 12967643.98906077, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.41612485357000006, 2212992, 0.41612485357000006, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 106.53418869, 0.00766942, 129.9910725, 0.06923745, 12.99910725, 0.24772893, -144.11832899, -0.0081356, -175.85055446, -0.07427699, -17.58505545, -0.25276847, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 106.53418869, 0.00766942, 129.9910725, 0.06924749, 12.99910725, 0.24780805, -144.11832899, -0.0081356, -175.85055446, -0.07428778, -17.58505545, -0.25284834, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29167266.60968836, 0.1125, 0.00189844, 0.00058594, 12153027.75403682, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.36833978305, 2312992, 0.36833978305, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 108.90424571, 0.00753501, 132.44533789, 0.06663042, 13.24453379, 0.24229382, -147.28229096, -0.00798783, -179.11930489, -0.07147294, -17.91193049, -0.24713634, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 108.90424571, 0.00753501, 132.44533789, 0.06728224, 13.24453379, 0.24757648, -147.28229096, -0.00798783, -179.11930489, -0.07217317, -17.91193049, -0.25246742, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 30309708.94134992, 0.1125, 0.00189844, 0.00058594, 12629045.39222913, 0.00152995)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.36902766669, 2022992, 0.36902766669, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 185.7489221, 0.0071827, 225.60717585, 0.07222707, 22.56071759, 0.2925499, -250.6962485, -0.00770065, -304.49098698, -0.07757661, -30.4490987, -0.29789945, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 185.7489221, 0.0071827, 225.60717585, 0.07167485, 22.56071759, 0.28758645, -250.6962485, -0.00770065, -304.49098698, -0.07698337, -30.4490987, -0.29289498, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 30733997.79106634, 0.125, 0.00260417, 0.00065104, 12805832.41294431, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.41278196258000005, 2122992, 0.41278196258000005, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 181.55220908, 0.00705343, 220.87889034, 0.074752, 22.08788903, 0.3000642, -245.01685243, -0.00756678, -298.09083984, -0.0802941, -29.80908398, -0.3056063, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 181.55220908, 0.00705343, 220.87889034, 0.07435695, 22.08788903, 0.29656275, -245.01685243, -0.00756678, -298.09083984, -0.0798697, -29.80908398, -0.3020755, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 30186435.68110373, 0.125, 0.00260417, 0.00065104, 12577681.53379322, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.4083067274, 2222992, 0.4083067274, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 104.77318734, 0.0076306, 127.37183158, 0.06863423, 12.73718316, 0.24911681, -141.78500529, -0.00808166, -172.36676933, -0.07361673, -17.23667693, -0.25409931, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 104.77318734, 0.0076306, 127.37183158, 0.06806952, 12.73718316, 0.24461417, -141.78500529, -0.00808166, -172.36676933, -0.07301008, -17.23667693, -0.24955473, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 30437729.75124968, 0.1125, 0.00189844, 0.00058594, 12682387.39635403, 0.00152995)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.36670735179, 2322992, 0.36670735179, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 63.07833271, 0.00715963, 76.66314719, 0.06380794, 7.66631472, 0.26708664, -94.18217523, -0.00757534, -114.46564378, -0.06980629, -11.44656438, -0.273085, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 63.05556759, 0.00713902, 76.63547928, 0.06357838, 7.66354793, 0.26118205, -114.12169652, -0.00777096, -138.69942406, -0.07260357, -13.86994241, -0.27020724, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 30525672.62234239, 0.1125, 0.00189844, 0.00058594, 12719030.25930933, 0.00152995)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.3278701387, 2003992, 0.3278701387, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 168.04400058, 0.00804732, 204.06963561, 0.07450834, 20.40696356, 0.29625988, -226.42683012, -0.00867031, -274.96870198, -0.08006815, -27.4968702, -0.30181969, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 168.04400058, 0.00804732, 204.06963561, 0.07481876, 20.40696356, 0.29903505, -226.42683012, -0.00867031, -274.96870198, -0.08040163, -27.4968702, -0.30461792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 30786503.25585634, 0.1125, 0.00189844, 0.00058594, 12827709.68994014, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.41334166277000006, 2103992, 0.41334166277000006, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 164.14965414, 0.00793893, 199.35160854, 0.07446812, 19.93516085, 0.29542838, -221.22400828, -0.00855234, -268.66557917, -0.08002342, -26.86655792, -0.30098368, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 164.14965414, 0.00793893, 199.35160854, 0.0750132, 19.93516085, 0.30029193, -221.22400828, -0.00855234, -268.66557917, -0.08060899, -26.86655792, -0.30588773, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 30768544.30249073, 0.1125, 0.00189844, 0.00058594, 12820226.79270447, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.40940634393, 2203992, 0.40940634393, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 61.85029443, 0.00707731, 75.50601063, 0.06577885, 7.55060106, 0.26944479, -92.32666334, -0.00749946, -112.71115341, -0.07198599, -11.27111534, -0.27565193, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 61.82822571, 0.00705566, 75.47906943, 0.06589161, 7.54790694, 0.26670113, -111.86173514, -0.00769807, -136.55930728, -0.07528367, -13.65593073, -0.27609319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 28986351.25434102, 0.1125, 0.00189844, 0.00058594, 12077646.35597543, 0.00152995)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32570208304, 2303992, 0.32570208304, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 62.37913687, 0.0071809, 76.11498331, 0.06442103, 7.61149833, 0.26397141, -112.87710689, -0.0078304, -137.73257436, -0.07358286, -13.77325744, -0.27313324, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 62.37913687, 0.0071809, 76.11498331, 0.06495632, 7.61149833, 0.2689617, -112.87710689, -0.0078304, -137.73257436, -0.07419775, -13.77325744, -0.27820313, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 29162032.11399967, 0.1125, 0.00189844, 0.00058594, 12150846.71416653, 0.00152995)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32736875268, 2013992, 0.32736875268, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 165.17743639, 0.00805019, 200.92691715, 0.07400215, 20.09269171, 0.29149506, -222.60888312, -0.00867735, -270.78829646, -0.07952832, -27.07882965, -0.29702122, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 165.17743639, 0.00805019, 200.92691715, 0.07398299, 20.09269171, 0.29132603, -222.60888312, -0.00867735, -270.78829646, -0.07950774, -27.07882965, -0.29685078, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 30236615.27189552, 0.1125, 0.00189844, 0.00058594, 12598589.69662313, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.41136270738, 2113992, 0.41136270738, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 162.61458473, 0.00783216, 198.27035967, 0.07775849, 19.82703597, 0.30304977, -219.04604367, -0.00845344, -267.075293, -0.08357401, -26.7075293, -0.30886528, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 162.61458473, 0.00783216, 198.27035967, 0.07773798, 19.82703597, 0.30287248, -219.04604367, -0.00845344, -267.075293, -0.08355197, -26.7075293, -0.30868647, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 29436588.57925995, 0.1125, 0.00189844, 0.00058594, 12265245.24135832, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.40665352799, 2213992, 0.40665352799, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 60.60236564, 0.00735544, 73.91660261, 0.06551263, 7.39166026, 0.26770378, -109.66099233, -0.00800614, -133.7533264, -0.07481203, -13.37533264, -0.27700318, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 60.60236564, 0.00735544, 73.91660261, 0.06562104, 7.39166026, 0.26870738, -109.66099233, -0.00800614, -133.7533264, -0.07493656, -13.37533264, -0.2780229, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 29310070.57350913, 0.1125, 0.00189844, 0.00058594, 12212529.40562881, 0.00152995)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.3268352608, 2313992, 0.3268352608, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 61.8580631, 0.00718572, 74.80599058, 0.06242074, 7.48059906, 0.26534477, -112.01107242, -0.00779785, -135.4568638, -0.07124702, -13.54568638, -0.27417104, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 61.89582203, 0.00720221, 74.85165309, 0.06161173, 7.48516531, 0.26128092, -92.44366956, -0.00760563, -111.79367616, -0.06737716, -11.17936762, -0.26704635, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 32059424.40148891, 0.1125, 0.00189844, 0.00058594, 13358093.50062038, 0.00152995)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32710936006999997, 2023992, 0.32710936006999997, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 164.6602727, 0.00811593, 200.82331123, 0.07663308, 20.08233112, 0.2984595, -221.90186962, -0.00875766, -270.63642914, -0.08236437, -27.06364291, -0.30419079, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 164.6602727, 0.00811593, 200.82331123, 0.07685051, 20.08233112, 0.30035039, -221.90186962, -0.00875766, -270.63642914, -0.08259795, -27.06364291, -0.30609783, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29332431.5720995, 0.1125, 0.00189844, 0.00058594, 12221846.48837479, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.4116059475, 2123992, 0.4116059475, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 162.75877901, 0.00802617, 198.23499925, 0.07695784, 19.82349993, 0.30135533, -219.37215997, -0.00865488, -267.18829075, -0.08270691, -26.71882907, -0.30710439, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 162.75877901, 0.00802617, 198.23499925, 0.07657353, 19.82349993, 0.29801467, -219.37215997, -0.00865488, -267.18829075, -0.08229405, -26.71882907, -0.30373519, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 29808747.02307557, 0.1125, 0.00189844, 0.00058594, 12420311.25961482, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.40934780933000003, 2223992, 0.40934780933000003, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 61.62442128, 0.00699024, 75.16134832, 0.06446289, 7.51613483, 0.26437743, -111.49416898, -0.00762367, -135.98589482, -0.07364323, -13.59858948, -0.27355778, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 61.64392733, 0.00701179, 75.18513922, 0.06458077, 7.51851392, 0.26925336, -92.01999568, -0.0074281, -112.2338645, -0.07067045, -11.22338645, -0.27534305, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 29318905.00251465, 0.1125, 0.00189844, 0.00058594, 12216210.41771444, 0.00152995)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32496156625, 2323992, 0.32496156625, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 62.66551556, 0.00724302, 76.284489, 0.0502784, 7.6284489, 0.24946905, -62.66551556, -0.00724302, -76.284489, -0.0502784, -7.6284489, -0.24946905, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 62.63625891, 0.00722099, 76.24887406, 0.05050311, 7.62488741, 0.24850459, -82.88463718, -0.0074681, -100.89779262, -0.05364447, -10.08977926, -0.25164595, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 29988554.7919445, 0.1125, 0.00189844, 0.00058594, 12495231.16331021, 0.00152995)
    ops.section('Aggregator', 2004991, 2004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2004992, 2004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.32774842087, 2004992, 0.32774842087, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 106.24716844, 0.00758222, 129.48799208, 0.0700914, 12.94879921, 0.25196683, -143.72818222, -0.0080404, -175.16771501, -0.07519286, -17.5167715, -0.25706828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 106.24716844, 0.00758222, 129.48799208, 0.06921418, 12.94879921, 0.24509335, -143.72818222, -0.0080404, -175.16771501, -0.07425047, -17.5167715, -0.25012964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 29587742.6032657, 0.1125, 0.00189844, 0.00058594, 12328226.08469404, 0.00152995)
    ops.section('Aggregator', 2104991, 2104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2104992, 2104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.36726152795, 2104992, 0.36726152795, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 109.0891381, 0.00754599, 132.91773404, 0.06811904, 13.2917734, 0.24571115, -147.50836109, -0.00800502, -179.72895789, -0.07307753, -17.97289579, -0.25066964, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 109.0891381, 0.00754599, 132.91773404, 0.06787974, 13.2917734, 0.24381209, -147.50836109, -0.00800502, -179.72895789, -0.07282045, -17.97289579, -0.2487528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 29676785.68418574, 0.1125, 0.00189844, 0.00058594, 12365327.36841073, 0.00152995)
    ops.section('Aggregator', 2204991, 2204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2204992, 2204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.3691706846, 2204992, 0.3691706846, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 60.98252166, 0.00712401, 74.33011147, 0.05171849, 7.43301115, 0.25358079, -60.98252166, -0.00712401, -74.33011147, -0.05171849, -7.43301115, -0.25358079, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 60.94901357, 0.00710283, 74.28926928, 0.05226221, 7.42892693, 0.25621664, -80.64958774, -0.00734705, -98.30181967, -0.0555262, -9.83018197, -0.25948063, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 29549530.84400771, 0.1125, 0.00189844, 0.00058594, 12312304.51833655, 0.00152995)
    ops.section('Aggregator', 2304991, 2304990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2304992, 2304991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.32490037544, 2304992, 0.32490037544, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 61.38600387, 0.00722171, 74.99109734, 0.05273069, 7.49910973, 0.2545794, -81.22225952, -0.00747345, -99.22369898, -0.05602558, -9.9223699, -0.25787429, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 61.38600387, 0.00722171, 74.99109734, 0.05264229, 7.49910973, 0.25356218, -81.22225952, -0.00747345, -99.22369898, -0.05593127, -9.9223699, -0.25685115, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 28729185.79900866, 0.1125, 0.00189844, 0.00058594, 11970494.08292028, 0.00152995)
    ops.section('Aggregator', 2014991, 2014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2014992, 2014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.32626917655, 2014992, 0.32626917655, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 109.80413059, 0.00774462, 133.75986348, 0.0674002, 13.37598635, 0.24342214, -148.52267292, -0.00821261, -180.92554757, -0.0722995, -18.09255476, -0.24832143, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 109.80413059, 0.00774462, 133.75986348, 0.06703679, 13.37598635, 0.24052576, -148.52267292, -0.00821261, -180.92554757, -0.07190909, -18.09255476, -0.24539806, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 29752122.84054099, 0.1125, 0.00189844, 0.00058594, 12396717.85022541, 0.00152995)
    ops.section('Aggregator', 2114991, 2114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2114992, 2114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.37191532047, 2114992, 0.37191532047, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 110.79517688, 0.00747887, 134.74938569, 0.06815917, 13.47493857, 0.2480322, -149.77200978, -0.00793132, -182.15311243, -0.07311905, -18.21531124, -0.25299208, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 110.79517688, 0.00747887, 134.74938569, 0.06807955, 13.47493857, 0.24739324, -149.77200978, -0.00793132, -182.15311243, -0.07303351, -18.21531124, -0.25234721, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 30298966.37861319, 0.1125, 0.00189844, 0.00058594, 12624569.32442216, 0.00152995)
    ops.section('Aggregator', 2214991, 2214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2214992, 2214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.36988701371000005, 2214992, 0.36988701371000005, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 61.2699417, 0.00705959, 74.6776401, 0.0515269, 7.46776401, 0.2520564, -81.07327399, -0.00730342, -98.81453463, -0.05474422, -9.88145346, -0.25527373, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 61.2699417, 0.00705959, 74.6776401, 0.05139344, 7.46776401, 0.25049829, -81.07327399, -0.00730342, -98.81453463, -0.05460184, -9.88145346, -0.25370669, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 29562709.04211731, 0.1125, 0.00189844, 0.00058594, 12317795.43421555, 0.00152995)
    ops.section('Aggregator', 2314991, 2314990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2314992, 2314991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.32488236836, 2314992, 0.32488236836, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 60.9275026, 0.00717235, 74.48747761, 0.05267755, 7.44874776, 0.25369023, -80.61373396, -0.0074239, -98.55506047, -0.055972, -9.85550605, -0.25698467, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 60.96335009, 0.00719439, 74.53130328, 0.05219477, 7.45313033, 0.2518226, -60.96335009, -0.00719439, -74.53130328, -0.05219477, -7.45313033, -0.2518226, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 28440935.9988303, 0.1125, 0.00189844, 0.00058594, 11850389.99951263, 0.00152995)
    ops.section('Aggregator', 2024991, 2024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2024992, 2024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.32533135875, 2024992, 0.32533135875, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 106.91079918, 0.00771004, 129.9994923, 0.06851184, 12.99994923, 0.24878288, -144.66434369, -0.0081677, -175.90637595, -0.07348596, -17.59063759, -0.253757, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 106.91079918, 0.00771004, 129.9994923, 0.06788954, 12.99994923, 0.24381457, -144.66434369, -0.0081677, -175.90637595, -0.07281742, -17.59063759, -0.24874246, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 30364361.2689888, 0.1125, 0.00189844, 0.00058594, 12651817.195412, 0.00152995)
    ops.section('Aggregator', 2124991, 2124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2124992, 2124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.36929992097000003, 2124992, 0.36929992097000003, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 108.0623002, 0.00752439, 131.77487608, 0.06922775, 13.17748761, 0.24862739, -146.12524083, -0.00798389, -178.19013168, -0.07427067, -17.81901317, -0.25367031, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 108.0623002, 0.00752439, 131.77487608, 0.06864599, 13.17748761, 0.24405932, -146.12524083, -0.00798389, -178.19013168, -0.0736457, -17.81901317, -0.24905902, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 29387396.01335094, 0.1125, 0.00189844, 0.00058594, 12244748.33889623, 0.00152995)
    ops.section('Aggregator', 2224991, 2224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2224992, 2224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.36806168871, 2224992, 0.36806168871, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 61.2740365, 0.00736972, 74.30877025, 0.0495471, 7.43087702, 0.24826927, -81.07266803, -0.00761108, -98.31913493, -0.05260883, -9.83191349, -0.251331, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 61.32347795, 0.00738574, 74.3687293, 0.04932183, 7.43687293, 0.24922791, -61.32347795, -0.00738574, -74.3687293, -0.04932183, -7.43687293, -0.24922791, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 31214865.90830042, 0.1125, 0.00189844, 0.00058594, 13006194.12845851, 0.00152995)
    ops.section('Aggregator', 2324991, 2324990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2324992, 2324991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.3276029552, 2324992, 0.3276029552, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)
