import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 62.43184387, 0.00715004, 76.04223532, 0.05235076, 7.60422353, 0.2559221, -82.6112861, -0.00739638, -100.62087661, -0.05561964, -10.06208766, -0.25919099, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 62.43184387, 0.00715004, 76.04223532, 0.05204844, 7.60422353, 0.25240487, -82.6112861, -0.00739638, -100.62087661, -0.05529711, -10.06208766, -0.25565354, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29798587.71270108, 0.1125, 0.00189844, 0.00058594, 12416078.21362545, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32690904355, 1001992, 0.32690904355, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 61.59553883, 0.00735534, 75.26081897, 0.0651289, 7.5260819, 0.32098303, -81.49628735, -0.00761047, -99.57664866, -0.06924731, -9.95766487, -0.32510145, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 61.59553883, 0.00735534, 75.26081897, 0.06460809, 7.5260819, 0.31502498, -81.49628735, -0.00761047, -99.57664866, -0.06869168, -9.95766487, -0.31910856, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28660409.0274231, 0.1125, 0.00189844, 0.00058594, 11941837.09475962, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25958591414, 1101992, 0.25958591414, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 61.81121538, 0.00722033, 75.51423347, 0.05124296, 7.55142335, 0.24914204, -81.78473066, -0.00747288, -99.91570634, -0.05443928, -9.99157063, -0.25233835, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 61.81121538, 0.00722033, 75.51423347, 0.05188408, 7.55142335, 0.25668816, -81.78473066, -0.00747288, -99.91570634, -0.05512327, -9.99157063, -0.25992735, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28710854.36836973, 0.1125, 0.00189844, 0.00058594, 11962855.98682072, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32671478274, 1201992, 0.32671478274, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 110.39563121, 0.00790319, 134.688566, 0.06718103, 13.4688566, 0.24113218, -149.33348889, -0.00838395, -182.19483194, -0.07206503, -18.21948319, -0.24601619, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 110.39563121, 0.00790319, 134.688566, 0.06696673, 13.4688566, 0.23942992, -149.33348889, -0.00838395, -182.19483194, -0.07183482, -18.21948319, -0.24429801, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29205330.34772355, 0.1125, 0.00189844, 0.00058594, 12168887.64488481, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.37398127831, 1011992, 0.37398127831, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 107.75783428, 0.00768478, 131.73949715, 0.08316325, 13.17394972, 0.29983955, -145.73250441, -0.00815994, -178.1654854, -0.08924505, -17.81654854, -0.30592135, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 107.75783428, 0.00768478, 131.73949715, 0.08293263, 13.17394972, 0.29804184, -145.73250441, -0.00815994, -178.1654854, -0.08899731, -17.81654854, -0.30410651, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 28443364.30553799, 0.1125, 0.00189844, 0.00058594, 11851401.79397416, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30135703291, 1111992, 0.30135703291, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 108.76760842, 0.00762556, 133.01956785, 0.07026972, 13.30195678, 0.24937338, -147.05437275, -0.00810047, -179.84314813, -0.07539793, -17.98431481, -0.25450159, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 108.76760842, 0.00762556, 133.01956785, 0.07024848, 13.30195678, 0.24920816, -147.05437275, -0.00810047, -179.84314813, -0.07537512, -17.98431481, -0.2543348, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 28310967.71106294, 0.1125, 0.00189844, 0.00058594, 11796236.54627622, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36950324933, 1211992, 0.36950324933, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 142.52836327, 0.00790795, 175.02074773, 0.07321137, 17.50207477, 0.24997167, -161.21199309, -0.00811073, -197.96371, -0.07531971, -19.796371, -0.25208001, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 142.52836327, 0.00790795, 175.02074773, 0.07385933, 17.50207477, 0.25480832, -161.21199309, -0.00811073, -197.96371, -0.07598658, -19.796371, -0.25693558, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 26609351.1834681, 0.1125, 0.00189844, 0.00058594, 11087229.65977838, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.36538781283, 1021992, 0.36538781283, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 146.84364196, 0.00814413, 179.93552814, 0.08637068, 17.99355281, 0.3025945, -166.10883457, -0.00834856, -203.54221999, -0.08885777, -20.354222, -0.30508159, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 146.84364196, 0.00814413, 179.93552814, 0.08662116, 17.99355281, 0.30449092, -166.10883457, -0.00834856, -203.54221999, -0.08911556, -20.354222, -0.30698532, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 27529441.68152311, 0.1125, 0.00189844, 0.00058594, 11470600.70063463, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.30261147586, 1121992, 0.30261147586, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 144.96751461, 0.00808949, 177.1932839, 0.07167477, 17.71932839, 0.24975021, -164.00859432, -0.00828763, -200.46712873, -0.07372834, -20.04671287, -0.25180377, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 144.96751461, 0.00808949, 177.1932839, 0.07196549, 17.71932839, 0.25197827, -164.00859432, -0.00828763, -200.46712873, -0.07402754, -20.04671287, -0.25404032, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 28523259.7467082, 0.1125, 0.00189844, 0.00058594, 11884691.56112842, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.36918636614, 1221992, 0.36918636614, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 60.61648356, 0.00717875, 74.23748569, 0.06678266, 7.42374857, 0.26939787, -90.48021734, -0.00761303, -110.81183608, -0.07309086, -11.08118361, -0.27570607, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 60.61648356, 0.00717875, 74.23748569, 0.06710921, 7.42374857, 0.27236753, -90.48021734, -0.00761303, -110.81183608, -0.07344959, -11.08118361, -0.27870791, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 27746377.38116262, 0.1125, 0.00189844, 0.00058594, 11560990.57548443, 0.00152995)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32508648262, 1031992, 0.32508648262, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 61.82704346, 0.0069988, 75.80818732, 0.08395569, 7.58081873, 0.3426528, -92.24219379, -0.0074326, -113.10121129, -0.09197354, -11.31012113, -0.35067065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 61.82704346, 0.0069988, 75.80818732, 0.08411263, 7.58081873, 0.34406291, -92.24219379, -0.0074326, -113.10121129, -0.09214594, -11.31012113, -0.35209623, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 27263010.1616258, 0.1125, 0.00189844, 0.00058594, 11359587.56734408, 0.00152995)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25679780597, 1131992, 0.25679780597, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 61.95425505, 0.00730545, 75.74135247, 0.06651362, 7.57413525, 0.27062269, -92.48666397, -0.0077417, -113.06834387, -0.07278479, -11.30683439, -0.27689386, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 61.95425505, 0.00730545, 75.74135247, 0.06615493, 7.57413525, 0.26734302, -92.48666397, -0.0077417, -113.06834387, -0.07239075, -11.30683439, -0.27357884, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 28447992.00917466, 0.1125, 0.00189844, 0.00058594, 11853330.00382278, 0.00152995)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32766467265, 1231992, 0.32766467265, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 62.0779302, 0.00721575, 75.87001746, 0.05304879, 7.58700175, 0.25557403, -82.13588354, -0.0074695, -100.38432174, -0.05636736, -10.03843217, -0.2588926, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 62.0779302, 0.00721575, 75.87001746, 0.05294876, 7.58700175, 0.25442708, -82.13588354, -0.0074695, -100.38432174, -0.05626064, -10.03843217, -0.25773897, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28561536.88053666, 0.1125, 0.00189844, 0.00058594, 11900640.36689028, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32694520496, 1002992, 0.32694520496, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 62.78006542, 0.00725262, 76.74091956, 0.06531897, 7.67409196, 0.32161739, -83.06291182, -0.00750867, -101.53420822, -0.06945788, -10.15342082, -0.3257563, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 62.78006542, 0.00725262, 76.74091956, 0.06477077, 7.67409196, 0.31536661, -83.06291182, -0.00750867, -101.53420822, -0.06887303, -10.15342082, -0.31946887, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28498027.89789847, 0.1125, 0.00189844, 0.00058594, 11874178.29079103, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25999659284, 1102992, 0.25999659284, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 61.98590196, 0.00711516, 75.48866395, 0.052824, 7.5488664, 0.25774207, -82.0221594, -0.00735982, -99.88953991, -0.05612519, -9.98895399, -0.26104325, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 61.98590196, 0.00711516, 75.48866395, 0.05264996, 7.5488664, 0.25572205, -82.0221594, -0.00735982, -99.88953991, -0.05593951, -9.98895399, -0.2590116, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29846049.34721395, 0.1125, 0.00189844, 0.00058594, 12435853.89467248, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32614533874, 1202992, 0.32614533874, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.68936046, 0.00706809, 76.70197398, 0.06512304, 7.6701974, 0.26509211, -93.54479299, -0.00749892, -114.45435439, -0.07127513, -11.44543544, -0.2712442, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 62.68044685, 0.00704386, 76.69106797, 0.06580548, 7.6691068, 0.26761291, -113.33673862, -0.00770013, -138.67028653, -0.07520036, -13.86702865, -0.27700779, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 28133666.65072489, 0.1125, 0.00189844, 0.00058594, 11722361.1044687, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32640170268, 1012992, 0.32640170268, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 61.57200477, 0.00705885, 74.8749741, 0.07799289, 7.48749741, 0.33006841, -111.44700658, -0.00768327, -135.5257436, -0.08916609, -13.55257436, -0.34124161, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 61.57200477, 0.00705885, 74.8749741, 0.07872454, 7.48749741, 0.33701128, -111.44700658, -0.00768327, -135.5257436, -0.09000655, -13.55257436, -0.34829329, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 30339029.01089478, 0.1125, 0.00189844, 0.00058594, 12641262.08787283, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25758979168, 1112992, 0.25758979168, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 63.22119979, 0.00726252, 77.30332955, 0.06523066, 7.73033295, 0.26504198, -114.37143995, -0.00793064, -139.84696816, -0.07451938, -13.98469682, -0.27433069, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 63.24569011, 0.00728503, 77.33327494, 0.06482282, 7.73332749, 0.26500876, -94.40307076, -0.00772392, -115.4307687, -0.07093201, -11.54307687, -0.27111795, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 28382757.69863249, 0.1125, 0.00189844, 0.00058594, 11826149.04109687, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32887612382, 1212992, 0.32887612382, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 107.71140373, 0.00774464, 131.65257612, 0.07082482, 13.16525761, 0.25170797, -145.68849902, -0.00822159, -178.07089633, -0.07598746, -17.80708963, -0.25687061, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 107.71140373, 0.00774464, 131.65257612, 0.07081424, 13.16525761, 0.25162543, -145.68849902, -0.00822159, -178.07089633, -0.07597609, -17.80708963, -0.25678728, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 28531070.86043667, 0.1125, 0.00189844, 0.00058594, 11887946.19184862, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36997325379, 1022992, 0.36997325379, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 110.10266471, 0.00773589, 135.06061897, 0.08448228, 13.5060619, 0.30063267, -148.81301048, -0.00822996, -182.54578452, -0.09067719, -18.25457845, -0.30682758, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 110.10266471, 0.00773589, 135.06061897, 0.08490251, 13.5060619, 0.30387094, -148.81301048, -0.00822996, -182.54578452, -0.09112864, -18.25457845, -0.31009706, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 27072657.88938456, 0.1125, 0.00189844, 0.00058594, 11280274.1205769, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30349053838, 1122992, 0.30349053838, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 107.97842624, 0.00761415, 132.3433891, 0.07158102, 13.23433891, 0.25152744, -145.96640913, -0.00809632, -178.90323051, -0.07681475, -17.89032305, -0.25676118, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 107.97842624, 0.00761415, 132.3433891, 0.07148296, 13.23433891, 0.25077571, -145.96640913, -0.00809632, -178.90323051, -0.07670941, -17.89032305, -0.25600216, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 27430201.68613408, 0.1125, 0.00189844, 0.00058594, 11429250.70255587, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36855994019000005, 1222992, 0.36855994019000005, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 61.61995002, 0.00713279, 75.18396148, 0.05142555, 7.51839615, 0.25085809, -81.53422065, -0.00738067, -99.48183506, -0.05463525, -9.94818351, -0.2540678, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 61.61995002, 0.00713279, 75.18396148, 0.05132812, 7.51839615, 0.24972166, -81.53422065, -0.00738067, -99.48183506, -0.05453131, -9.94818351, -0.25292485, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 29184496.12337979, 0.1125, 0.00189844, 0.00058594, 12160206.71807491, 0.00152995)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32583053038000004, 1032992, 0.32583053038000004, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 62.08764822, 0.00727212, 75.88063904, 0.06393562, 7.5880639, 0.31649999, -82.14959383, -0.00752699, -100.39941688, -0.06797954, -10.03994169, -0.32054391, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 62.08764822, 0.00727212, 75.88063904, 0.06439296, 7.5880639, 0.32181956, -82.14959383, -0.00752699, -100.39941688, -0.06846746, -10.03994169, -0.32589406, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 28567832.79295926, 0.1125, 0.00189844, 0.00058594, 11903263.66373303, 0.00152995)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25942732877999997, 1132992, 0.25942732877999997, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 61.77753027, 0.00694844, 75.57235913, 0.0546011, 7.55723591, 0.26065609, -81.71947532, -0.00719803, -99.96731028, -0.0580372, -9.99673103, -0.26409219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 61.77753027, 0.00694844, 75.57235913, 0.05439174, 7.55723591, 0.25830576, -81.71947532, -0.00719803, -99.96731028, -0.05781384, -9.99673103, -0.26172785, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 28206311.35245373, 0.1125, 0.00189844, 0.00058594, 11752629.73018906, 0.00152995)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32430089033000004, 1232992, 0.32430089033000004, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 62.80012069, 0.0072145, 76.51531453, 0.05039891, 7.65153145, 0.24928858, -62.80012069, -0.0072145, -76.51531453, -0.05039891, -7.65153145, -0.24928858, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 62.80012069, 0.0072145, 76.51531453, 0.0503754, 7.65153145, 0.24900823, -62.80012069, -0.0072145, -76.51531453, -0.0503754, -7.65153145, -0.24900823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 29687623.92103944, 0.1125, 0.00189844, 0.00058594, 12369843.3004331, 0.00152995)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32761306946, 1003992, 0.32761306946, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 61.59379094, 0.00715942, 75.28511051, 0.06513589, 7.52851105, 0.32207915, -61.59379094, -0.00715942, -75.28511051, -0.06513589, -7.52851105, -0.32207915, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 61.59379094, 0.00715942, 75.28511051, 0.06515171, 7.52851105, 0.32226129, -61.59379094, -0.00715942, -75.28511051, -0.06515171, -7.52851105, -0.32226129, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 28527132.65991258, 0.1125, 0.00189844, 0.00058594, 11886305.27496357, 0.00152995)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25772481018000004, 1103992, 0.25772481018000004, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 61.87351982, 0.00719037, 75.43687095, 0.05266725, 7.54368709, 0.2571097, -61.87351982, -0.00719037, -75.43687095, -0.05266725, -7.54368709, -0.2571097, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 61.87351982, 0.00719037, 75.43687095, 0.05229213, 7.54368709, 0.252757, -61.87351982, -0.00719037, -75.43687095, -0.05229213, -7.54368709, -0.252757, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 29452470.69172717, 0.1125, 0.00189844, 0.00058594, 12271862.78821965, 0.00152995)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32639746105, 1203992, 0.32639746105, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 61.15937953, 0.0071921, 74.60270186, 0.05180299, 7.46027019, 0.25326506, -61.15937953, -0.0071921, -74.60270186, -0.05180299, -7.46027019, -0.25326506, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 61.12281876, 0.00717102, 74.55810474, 0.05221789, 7.45581047, 0.25439045, -80.87757728, -0.00741831, -98.65511768, -0.05547743, -9.86551177, -0.25764999, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29277798.14662357, 0.1125, 0.00189844, 0.00058594, 12199082.56109315, 0.00152995)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.3256253367, 1013992, 0.3256253367, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 61.60606954, 0.00720843, 75.36307972, 0.06311168, 7.53630797, 0.31249461, -81.50963918, -0.00746323, -99.71123757, -0.0671047, -9.97112376, -0.31648762, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 61.60606954, 0.00720843, 75.36307972, 0.06396795, 7.53630797, 0.32250714, -81.50963918, -0.00746323, -99.71123757, -0.06801822, -9.97112376, -0.32655741, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 28203876.24250717, 0.1125, 0.00189844, 0.00058594, 11751615.10104465, 0.00152995)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25833578714, 1113992, 0.25833578714, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 62.75508956, 0.00718848, 76.65457115, 0.05200322, 7.66545712, 0.25233534, -83.0295975, -0.00744163, -101.4196336, -0.0552531, -10.14196336, -0.25558522, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 62.77505539, 0.00721298, 76.67895917, 0.05135625, 7.66789592, 0.24845697, -62.77505539, -0.00721298, -76.67895917, -0.05135625, -7.66789592, -0.24845697, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 28773404.629815, 0.1125, 0.00189844, 0.00058594, 11988918.59575625, 0.00152995)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32745886546999997, 1213992, 0.32745886546999997, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 61.71787001, 0.00716041, 75.32671823, 0.05114699, 7.53267182, 0.25051672, -61.71787001, -0.00716041, -75.32671823, -0.05114699, -7.53267182, -0.25051672, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 61.69003283, 0.00713763, 75.29274292, 0.0516346, 7.52927429, 0.2525689, -81.62597625, -0.00738632, -99.62458057, -0.05485878, -9.96245806, -0.25579308, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 29072110.80776933, 0.1125, 0.00189844, 0.00058594, 12113379.50323722, 0.00152995)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.32593327086, 1023992, 0.32593327086, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 60.80531108, 0.00709099, 74.41150905, 0.06422379, 7.44115091, 0.31612963, -80.44852313, -0.00734283, -98.45021596, -0.06829606, -9.8450216, -0.3202019, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 60.80531108, 0.00709099, 74.41150905, 0.06464218, 7.44115091, 0.32094587, -80.44852313, -0.00734283, -98.45021596, -0.06874243, -9.8450216, -0.32504612, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 28055437.09766349, 0.1125, 0.00189844, 0.00058594, 11689765.45735979, 0.00152995)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.25647783781, 1123992, 0.25647783781, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 61.64531518, 0.00742001, 75.28543889, 0.05333945, 7.52854389, 0.25699368, -81.55952424, -0.00767548, -99.60602132, -0.05666552, -9.96060213, -0.26031974, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 61.69332917, 0.00743961, 75.34407683, 0.05287445, 7.53440768, 0.25538786, -61.69332917, -0.00743961, -75.34407683, -0.05287445, -7.53440768, -0.25538786, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 28840579.12187593, 0.1125, 0.00189844, 0.00058594, 12016907.9674483, 0.00152995)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.32818349853, 1223992, 0.32818349853, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 62.7696215, 0.00718983, 76.54123557, 0.05238243, 7.65412356, 0.25612691, -62.7696215, -0.00718983, -76.54123557, -0.05238243, -7.65412356, -0.25612691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 62.7696215, 0.00718983, 76.54123557, 0.0517864, 7.65412356, 0.24921444, -62.7696215, -0.00718983, -76.54123557, -0.0517864, -7.65412356, -0.24921444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 29397600.92293189, 0.1125, 0.00189844, 0.00058594, 12249000.38455495, 0.00152995)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32733507342, 1033992, 0.32733507342, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 61.09383746, 0.00719203, 74.78891031, 0.06489628, 7.47889103, 0.31945522, -61.09383746, -0.00719203, -74.78891031, -0.06489628, -7.47889103, -0.31945522, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 61.09383746, 0.00719203, 74.78891031, 0.06484235, 7.47889103, 0.3188374, -61.09383746, -0.00719203, -74.78891031, -0.06484235, -7.47889103, -0.3188374, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 27925719.14631663, 0.1125, 0.00189844, 0.00058594, 11635716.31096526, 0.00152995)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25738695472, 1133992, 0.25738695472, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 62.43224079, 0.00725483, 76.24472401, 0.05210187, 7.6244724, 0.25369262, -62.43224079, -0.00725483, -76.24472401, -0.05210187, -7.6244724, -0.25369262, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 62.43224079, 0.00725483, 76.24472401, 0.05210451, 7.6244724, 0.25372342, -62.43224079, -0.00725483, -76.24472401, -0.05210451, -7.6244724, -0.25372342, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 28849173.54200602, 0.1125, 0.00189844, 0.00058594, 12020488.97583584, 0.00152995)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32746002585, 1233992, 0.32746002585, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 79.03294178, 0.01097328, 96.53432585, 0.08934109, 9.65343259, 0.30900537, -106.67716302, -0.0117428, -130.30019867, -0.09593189, -13.03001987, -0.31559617, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 79.03294178, 0.01097328, 96.53432585, 0.08888337, 9.65343259, 0.30551652, -106.67716302, -0.0117428, -130.30019867, -0.09544017, -13.03001987, -0.31207333, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 28786735.54456096, 0.0875, 0.00089323, 0.00045573, 11994473.14356707, 0.0010204)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30312699834, 6200992, 0.30312699834, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 67.01269435, 0.01333161, 81.91560667, 0.09351844, 8.19156067, 0.3126198, -90.28681571, -0.01436966, -110.36564571, -0.10051289, -11.03656457, -0.31961426, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 67.01269435, 0.01333161, 81.91560667, 0.09282971, 8.19156067, 0.30749339, -90.28681571, -0.01436966, -110.36564571, -0.099773, -11.03656457, -0.31443668, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 28494206.42330625, 0.075, 0.0005625, 0.00039062, 11872586.00971094, 0.00077515)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30440673654, 6201992, 0.30440673654, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 38.16746228, 0.01175233, 46.70124989, 0.08911075, 4.67012499, 0.3454835, -56.69999225, -0.0126488, -69.37743167, -0.09763084, -6.93774317, -0.35400359, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 38.16746228, 0.01175233, 46.70124989, 0.08837217, 4.67012499, 0.33897669, -56.69999225, -0.0126488, -69.37743167, -0.09681947, -6.93774317, -0.34742399, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 28113208.22029576, 0.075, 0.0005625, 0.00039062, 11713836.75845657, 0.00077515)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.2570638798, 6202992, 0.2570638798, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 61.7792965, 0.00716915, 75.77496713, 0.06616325, 7.57749671, 0.26490944, -111.73381302, -0.00784462, -137.04633249, -0.07561188, -13.70463325, -0.27435806, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 61.7792965, 0.00716915, 75.77496713, 0.06641081, 7.57749671, 0.26714102, -111.73381302, -0.00784462, -137.04633249, -0.07589625, -13.70463325, -0.27662647, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 27120330.47484024, 0.1125, 0.00189844, 0.00058594, 11300137.6978501, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32640824129, 2001992, 0.32640824129, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 184.84701483, 0.00726368, 226.1173767, 0.07456974, 22.61173767, 0.29236939, -249.37562354, -0.00781186, -305.05313738, -0.08011752, -30.50531374, -0.29791717, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 184.84701483, 0.00726368, 226.1173767, 0.07534772, 22.61173767, 0.29916656, -249.37562354, -0.00781186, -305.05313738, -0.08095328, -30.50531374, -0.30477212, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28216179.58828906, 0.125, 0.00260417, 0.00065104, 11756741.49512044, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41270769082, 2101992, 0.41270769082, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 189.74376358, 0.00702247, 231.75104187, 0.07445901, 23.17510419, 0.29455382, -255.68620904, -0.00755359, -312.29245283, -0.07999942, -31.22924528, -0.30009422, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 189.74376358, 0.00702247, 231.75104187, 0.07440085, 23.17510419, 0.29404562, -255.68620904, -0.00755359, -312.29245283, -0.07993693, -31.22924528, -0.2995817, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 28803448.08086828, 0.125, 0.00260417, 0.00065104, 12001436.70036178, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41215364254000003, 2201992, 0.41215364254000003, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.58512031, 0.0073298, 76.70207797, 0.06631799, 7.6702078, 0.26642589, -113.21520207, -0.0080131, -138.75248962, -0.07577357, -13.87524896, -0.27588147, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 62.58512031, 0.0073298, 76.70207797, 0.06599489, 7.6702078, 0.26351261, -113.21520207, -0.0080131, -138.75248962, -0.07540242, -13.87524896, -0.27292014, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 27458308.77210532, 0.1125, 0.00189844, 0.00058594, 11440961.98837722, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32865559939000005, 2301992, 0.32865559939000005, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 60.75504867, 0.00720903, 73.98415046, 0.06558173, 7.39841505, 0.26967978, -109.96698288, -0.00784481, -133.9117322, -0.07489827, -13.39117322, -0.27899632, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 60.75504867, 0.00720903, 73.98415046, 0.0648825, 7.39841505, 0.26322884, -109.96698288, -0.00784481, -133.9117322, -0.07409506, -13.39117322, -0.2724414, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29871724.1591335, 0.1125, 0.00189844, 0.00058594, 12446551.73297229, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.3258923745, 2011992, 0.3258923745, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 184.7697502, 0.00701871, 226.30677744, 0.07794947, 22.63067774, 0.30401901, -249.04789045, -0.0075582, -305.03491753, -0.08375781, -30.50349175, -0.30982734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 184.7697502, 0.00701871, 226.30677744, 0.07746915, 22.63067774, 0.29992419, -249.04789045, -0.0075582, -305.03491753, -0.08324181, -30.50349175, -0.30569684, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 27714292.11768712, 0.125, 0.00260417, 0.00065104, 11547621.71570297, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.40894979345000004, 2111992, 0.40894979345000004, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 183.74822141, 0.00701697, 223.56681433, 0.073495, 22.35668143, 0.29507923, -247.8964519, -0.00753003, -301.61608972, -0.07894615, -30.16160897, -0.30053038, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 183.74822141, 0.00701697, 223.56681433, 0.07348743, 22.35668143, 0.29501182, -247.8964519, -0.00753003, -301.61608972, -0.07893802, -30.16160897, -0.30046241, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30162134.78865111, 0.125, 0.00260417, 0.00065104, 12567556.16193796, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.4090525883, 2211992, 0.4090525883, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 61.6119033, 0.00721193, 75.29743408, 0.06677059, 7.52974341, 0.27059447, -111.48732509, -0.00786838, -136.25142323, -0.07628416, -13.62514232, -0.28010805, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 61.6119033, 0.00721193, 75.29743408, 0.06618889, 7.52974341, 0.26532227, -111.48732509, -0.00786838, -136.25142323, -0.07561596, -13.62514232, -0.27474934, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28576779.88871286, 0.1125, 0.00189844, 0.00058594, 11906991.62029702, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32673916018, 2311992, 0.32673916018, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 61.26476599, 0.00716353, 74.82926043, 0.06612742, 7.48292604, 0.26878305, -110.8644822, -0.00781281, -135.41073858, -0.07554538, -13.54107386, -0.278201, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 61.26476599, 0.00716353, 74.82926043, 0.06590758, 7.48292604, 0.2667755, -110.8644822, -0.00781281, -135.41073858, -0.07529284, -13.54107386, -0.27616076, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 28797870.54408726, 0.1125, 0.00189844, 0.00058594, 11999112.72670302, 0.00152995)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.32598284435, 2021992, 0.32598284435, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 181.42165091, 0.00729556, 221.05648211, 0.07448373, 22.10564821, 0.29689341, -244.9437238, -0.00782732, -298.45609731, -0.08000634, -29.84560973, -0.30241602, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 181.42165091, 0.00729556, 221.05648211, 0.07460651, 22.10564821, 0.29798146, -244.9437238, -0.00782732, -298.45609731, -0.08013824, -29.84560973, -0.30351319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29666586.03302048, 0.125, 0.00260417, 0.00065104, 12361077.51375853, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.41151951134000003, 2121992, 0.41151951134000003, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 187.62000767, 0.00703002, 228.79891077, 0.07558487, 22.87989108, 0.30102459, -252.95124322, -0.00755427, -308.46906812, -0.08120148, -30.84690681, -0.3066412, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 187.62000767, 0.00703002, 228.79891077, 0.07443469, 22.87989108, 0.29100551, -252.95124322, -0.00755427, -308.46906812, -0.07996587, -30.84690681, -0.29653669, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 29373945.5844907, 0.125, 0.00260417, 0.00065104, 12239143.99353779, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.41124125111000004, 2221992, 0.41124125111000004, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 61.83531646, 0.00716196, 75.61600492, 0.06538714, 7.56160049, 0.26513168, -111.87462078, -0.00781948, -136.8071251, -0.07470348, -13.68071251, -0.27444802, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 61.83531646, 0.00716196, 75.61600492, 0.06596993, 7.56160049, 0.27048956, -111.87462078, -0.00781948, -136.8071251, -0.07537293, -13.68071251, -0.27989257, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 28345639.64394227, 0.1125, 0.00189844, 0.00058594, 11810683.18497595, 0.00152995)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32654128880000005, 2321992, 0.32654128880000005, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 61.60057771, 0.00704971, 75.55041613, 0.06779209, 7.55504161, 0.27185376, -91.9153696, -0.00748624, -112.73018339, -0.07421474, -11.27301834, -0.27827641, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 61.58581235, 0.00702546, 75.53230706, 0.06849041, 7.55323071, 0.27429437, -111.35207105, -0.00769077, -136.56844818, -0.07829634, -13.65684482, -0.2841003, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 27150673.10870431, 0.1125, 0.00189844, 0.00058594, 11312780.46196013, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32498611126, 2002992, 0.32498611126, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 163.77987268, 0.00811666, 200.01877595, 0.07694077, 20.0018776, 0.29770669, -220.70624859, -0.0087639, -269.54101848, -0.08270037, -26.95410185, -0.30346629, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 163.77987268, 0.00811666, 200.01877595, 0.07679304, 20.0018776, 0.29643654, -220.70624859, -0.0087639, -269.54101848, -0.08254167, -26.95410185, -0.30218517, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 28841155.76560595, 0.1125, 0.00189844, 0.00058594, 12017148.23566915, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.41089149427, 2102992, 0.41089149427, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 166.29988647, 0.00788849, 203.13717454, 0.0774186, 20.31371745, 0.29970087, -223.87884322, -0.00852466, -273.47051531, -0.08321958, -27.34705153, -0.30550185, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 166.29988647, 0.00788849, 203.13717454, 0.07726979, 20.31371745, 0.29842522, -223.87884322, -0.00852466, -273.47051531, -0.08305971, -27.34705153, -0.30421515, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 28766209.69932248, 0.1125, 0.00189844, 0.00058594, 11985920.70805104, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.40954672902, 2202992, 0.40954672902, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 63.13723239, 0.00746358, 77.61559297, 0.06622644, 7.7615593, 0.26438698, -94.21375005, -0.00793152, -115.81844498, -0.07248542, -11.5818445, -0.27064596, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 63.10554433, 0.00743947, 77.57663834, 0.06692826, 7.75766383, 0.26699528, -114.11804689, -0.00815281, -140.2871102, -0.07648834, -14.02871102, -0.27655536, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 26107118.73426745, 0.1125, 0.00189844, 0.00058594, 10877966.13927811, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32997370663, 2302992, 0.32997370663, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 60.99960835, 0.0070764, 74.57966646, 0.06609489, 7.45796665, 0.26760555, -110.3668248, -0.00772468, -134.93727589, -0.07551996, -13.49372759, -0.27703063, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 60.99960835, 0.0070764, 74.57966646, 0.06652637, 7.45796665, 0.27154923, -110.3668248, -0.00772468, -134.93727589, -0.07601561, -13.49372759, -0.28103847, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28420119.60538312, 0.1125, 0.00189844, 0.00058594, 11841716.50224297, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32493285335000005, 2012992, 0.32493285335000005, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 162.04043544, 0.00805954, 197.9163758, 0.07870826, 19.79163758, 0.30434018, -218.37476952, -0.00870223, -266.72319678, -0.08459884, -26.67231968, -0.31023076, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 162.04043544, 0.00805954, 197.9163758, 0.07885979, 19.79163758, 0.30564135, -218.37476952, -0.00870223, -266.72319678, -0.08476162, -26.67231968, -0.31154318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28799887.10991303, 0.1125, 0.00189844, 0.00058594, 11999952.96246376, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.4090077472, 2112992, 0.4090077472, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 165.6965757, 0.00819196, 203.53549695, 0.08080448, 20.35354969, 0.30519357, -223.10054239, -0.00887864, -274.04838978, -0.08688493, -27.40483898, -0.31127402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 165.6965757, 0.00819196, 203.53549695, 0.08074196, 20.35354969, 0.304673, -223.10054239, -0.00887864, -274.04838978, -0.08681776, -27.40483898, -0.3107488, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 26465374.74463375, 0.1125, 0.00189844, 0.00058594, 11027239.47693073, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.41235031047000004, 2212992, 0.41235031047000004, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 62.5403981, 0.00727416, 76.67623099, 0.06625592, 7.6676231, 0.26583857, -113.12031604, -0.00795627, -138.68858762, -0.07570935, -13.86885876, -0.27529201, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 62.5403981, 0.00727416, 76.67623099, 0.06595397, 7.6676231, 0.26312148, -113.12031604, -0.00795627, -138.68858762, -0.0753625, -13.86885876, -0.27253001, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 27299603.19306355, 0.1125, 0.00189844, 0.00058594, 11374834.66377648, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32812587042, 2312992, 0.32812587042, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 62.28212706, 0.00713092, 76.13965636, 0.06549861, 7.61396564, 0.26595961, -112.66987232, -0.0077866, -137.73847756, -0.0748343, -13.77384776, -0.2752953, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 62.30453499, 0.00715322, 76.16704996, 0.06541932, 7.616705, 0.26899467, -92.99721901, -0.00758394, -113.68873595, -0.07159211, -11.36887359, -0.27516746, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 28460758.73899802, 0.1125, 0.00189844, 0.00058594, 11858649.47458251, 0.00152995)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32676885202, 2022992, 0.32676885202, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 163.59216385, 0.00783336, 199.75005454, 0.0785653, 19.97500545, 0.30441239, -220.29502, -0.00846194, -268.98563613, -0.08444796, -26.89856361, -0.31029504, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 163.59216385, 0.00783336, 199.75005454, 0.07838845, 19.97500545, 0.30289832, -220.29502, -0.00846194, -268.98563613, -0.08425797, -26.89856361, -0.30876784, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 28914464.47462222, 0.1125, 0.00189844, 0.00058594, 12047693.53109259, 0.00152995)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.40714277037, 2122992, 0.40714277037, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 162.13741084, 0.00825566, 197.18823046, 0.07430674, 19.71882305, 0.29250063, -218.6786965, -0.00889141, -265.95259527, -0.07984886, -26.59525953, -0.29804275, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 162.13741084, 0.00825566, 197.18823046, 0.07446571, 19.71882305, 0.29390741, -218.6786965, -0.00889141, -265.95259527, -0.08001964, -26.59525953, -0.29946134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 30305212.91564894, 0.1125, 0.00189844, 0.00058594, 12627172.04818706, 0.00152995)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.41193722237999997, 2222992, 0.41193722237999997, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 62.68180621, 0.00703953, 76.65481997, 0.06566002, 7.665482, 0.26632374, -113.34590406, -0.00769286, -138.61294682, -0.07503097, -13.86129468, -0.27569468, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 62.69112071, 0.00706353, 76.66621086, 0.06526307, 7.66662109, 0.26641975, -93.55114399, -0.00749248, -114.4055434, -0.07142754, -11.44055434, -0.27258422, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 28327048.53684215, 0.1125, 0.00189844, 0.00058594, 11802936.8903509, 0.00152995)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32638740187000004, 2322992, 0.32638740187000004, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 61.11971943, 0.00713206, 75.0187624, 0.05385817, 7.50187624, 0.25582682, -61.11971943, -0.00713206, -75.0187624, -0.05385817, -7.50187624, -0.25582682, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 61.09836937, 0.00710612, 74.99255719, 0.0541476, 7.49925572, 0.25539193, -80.82391003, -0.00736608, -99.20382095, -0.0575532, -9.9203821, -0.25879752, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 26813953.68746607, 0.1125, 0.00189844, 0.00058594, 11172480.70311086, 0.00152995)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32476385129, 2003992, 0.32476385129, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 108.80950478, 0.0075318, 132.15440321, 0.06719974, 13.21544032, 0.24565263, -147.17044826, -0.00798071, -178.74562336, -0.07208088, -17.87456234, -0.25053377, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 108.80950478, 0.0075318, 132.15440321, 0.06667103, 13.21544032, 0.24139577, -147.17044826, -0.00798071, -178.74562336, -0.07151289, -17.87456234, -0.24623764, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 30742712.37653955, 0.1125, 0.00189844, 0.00058594, 12809463.49022481, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36899945195, 2103992, 0.36899945195, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 106.57447094, 0.00749887, 130.47420505, 0.07173694, 13.04742051, 0.25305333, -144.08184669, -0.00796943, -176.39275375, -0.0769792, -17.63927538, -0.25829559, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 106.57447094, 0.00749887, 130.47420505, 0.07136089, 13.04742051, 0.25016956, -144.08184669, -0.00796943, -176.39275375, -0.07657521, -17.63927538, -0.25538388, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 27896427.84514843, 0.1125, 0.00189844, 0.00058594, 11623511.60214518, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36629215585999997, 2203992, 0.36629215585999997, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 61.2970746, 0.00732422, 75.11317172, 0.05302693, 7.51131717, 0.25402724, -61.2970746, -0.00732422, -75.11317172, -0.05302693, -7.51131717, -0.25402724, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 61.25690688, 0.0073016, 75.06395038, 0.05362437, 7.50639504, 0.25713618, -81.04279998, -0.00756171, -99.30949872, -0.05698206, -9.93094987, -0.26049386, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 27515513.05668554, 0.1125, 0.00189844, 0.00058594, 11464797.10695231, 0.00152995)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.3266448936, 2303992, 0.3266448936, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 60.8311602, 0.00724433, 74.46493656, 0.05395541, 7.44649366, 0.25727027, -80.48209488, -0.00750001, -98.52013458, -0.05733463, -9.85201346, -0.26064949, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 60.8311602, 0.00724433, 74.46493656, 0.05386539, 7.44649366, 0.25625202, -80.48209488, -0.00750001, -98.52013458, -0.05723859, -9.85201346, -0.25962522, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 27938713.51456159, 0.1125, 0.00189844, 0.00058594, 11641130.63106733, 0.00152995)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32576078545000003, 2013992, 0.32576078545000003, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 107.13697836, 0.00766107, 130.86159942, 0.06862714, 13.08615994, 0.24465211, -144.90982858, -0.00813114, -176.99894312, -0.07362587, -17.69989431, -0.24965083, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 107.13697836, 0.00766107, 130.86159942, 0.0685193, 13.08615994, 0.24380656, -144.90982858, -0.00813114, -176.99894312, -0.07351001, -17.69989431, -0.24879727, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 28787415.25123795, 0.1125, 0.00189844, 0.00058594, 11994756.35468248, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36866964875999997, 2113992, 0.36866964875999997, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 108.37955755, 0.00752346, 131.96523024, 0.06831943, 13.19652302, 0.24699608, -146.56602059, -0.00797867, -178.46187131, -0.07329066, -17.84618713, -0.25196731, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 108.37955755, 0.00752346, 131.96523024, 0.06806332, 13.19652302, 0.24495965, -146.56602059, -0.00797867, -178.46187131, -0.07301552, -17.84618713, -0.24991186, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 29906541.9974296, 0.1125, 0.00189844, 0.00058594, 12461059.16559567, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.3684062296, 2213992, 0.3684062296, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 62.37473769, 0.00724922, 76.42987492, 0.05195511, 7.64298749, 0.24952893, -82.51941063, -0.00751009, -101.11382374, -0.05520544, -10.11138237, -0.25277925, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 62.37473769, 0.00724922, 76.42987492, 0.05256527, 7.64298749, 0.2565955, -82.51941063, -0.00751009, -101.11382374, -0.05585639, -10.11138237, -0.25988663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 27536467.42698623, 0.1125, 0.00189844, 0.00058594, 11473528.0945776, 0.00152995)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32741833337000004, 2313992, 0.32741833337000004, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 61.97366243, 0.00708715, 75.62190724, 0.0521381, 7.56219072, 0.25356239, -81.99874088, -0.00733485, -100.05703929, -0.05539833, -10.00570393, -0.25682262, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 61.99385772, 0.00711087, 75.64655007, 0.05167565, 7.56465501, 0.25185721, -61.99385772, -0.00711087, -75.64655007, -0.05167565, -7.56465501, -0.25185721, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 29153957.40433498, 0.1125, 0.00189844, 0.00058594, 12147482.25180624, 0.00152995)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32581555916000005, 2023992, 0.32581555916000005, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 106.63544766, 0.00765069, 130.12354739, 0.06816823, 13.01235474, 0.24394156, -144.24886597, -0.00811639, -176.02190041, -0.07312926, -17.60219004, -0.24890259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 106.63544766, 0.00765069, 130.12354739, 0.06883186, 13.01235474, 0.24921191, -144.24886597, -0.00811639, -176.02190041, -0.07384219, -17.60219004, -0.25422224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29142395.47452236, 0.1125, 0.00189844, 0.00058594, 12142664.78105098, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36821993638, 2123992, 0.36821993638, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 107.72308977, 0.00768332, 131.5613275, 0.0696314, 13.15613275, 0.24836975, -145.69920797, -0.00815465, -177.9412497, -0.07470433, -17.79412497, -0.25344267, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 107.72308977, 0.00768332, 131.5613275, 0.06993352, 13.15613275, 0.25074648, -145.69920797, -0.00815465, -177.9412497, -0.07502888, -17.79412497, -0.25584185, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 28833263.69832914, 0.1125, 0.00189844, 0.00058594, 12013859.87430381, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36939220563999997, 2223992, 0.36939220563999997, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 61.30794283, 0.0071191, 75.09279953, 0.05209356, 7.50927995, 0.25019737, -81.10936503, -0.00737443, -99.34649585, -0.05535629, -9.93464959, -0.25346011, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 61.33242652, 0.00714369, 75.12278828, 0.05206944, 7.51227883, 0.25356558, -61.33242652, -0.00714369, -75.12278828, -0.05206944, -7.51227883, -0.25356558, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 27700310.00297797, 0.1125, 0.00189844, 0.00058594, 11541795.83457416, 0.00152995)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.3252076734, 2323992, 0.3252076734, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
