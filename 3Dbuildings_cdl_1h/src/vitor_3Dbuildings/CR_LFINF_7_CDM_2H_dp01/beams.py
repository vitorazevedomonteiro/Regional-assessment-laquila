import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 62.6090907, 0.00735312, 76.40298807, 0.05162407, 7.64029881, 0.25246985, -62.6090907, -0.00735312, -76.40298807, -0.05162407, -7.64029881, -0.25246985, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 62.6090907, 0.00735312, 76.40298807, 0.05177029, 7.64029881, 0.25419314, -62.6090907, -0.00735312, -76.40298807, -0.05177029, -7.64029881, -0.25419314, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29126791.55574284, 0.1125, 0.00189844, 0.00058594, 12136163.14822619, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32850610301, 1001992, 0.32850610301, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 61.36752691, 0.00710111, 75.01193621, 0.06588494, 7.50119362, 0.32482273, -61.36752691, -0.00710111, -75.01193621, -0.06588494, -7.50119362, -0.32482273, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 61.36752691, 0.00710111, 75.01193621, 0.06581418, 7.50119362, 0.32401321, -61.36752691, -0.00710111, -75.01193621, -0.06581418, -7.50119362, -0.32401321, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 28509898.27365128, 0.1125, 0.00189844, 0.00058594, 11879124.28068803, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25699069659999996, 1101992, 0.25699069659999996, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 64.31370404, 0.00729789, 78.44569207, 0.04998562, 7.84456921, 0.24713399, -64.31370404, -0.00729789, -78.44569207, -0.04998562, -7.84456921, -0.24713399, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 64.31370404, 0.00729789, 78.44569207, 0.05000221, 7.84456921, 0.2473324, -64.31370404, -0.00729789, -78.44569207, -0.05000221, -7.84456921, -0.2473324, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29299211.54487082, 0.1125, 0.00189844, 0.00058594, 12208004.81036284, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32986511107, 1201992, 0.32986511107, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 62.42861284, 0.00733538, 76.28294715, 0.05092979, 7.62829472, 0.24788006, -82.60124627, -0.00759172, -100.93234844, -0.05410125, -10.09323484, -0.25105152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 62.42861284, 0.00733538, 76.28294715, 0.05107253, 7.62829472, 0.24955592, -82.60124627, -0.00759172, -100.93234844, -0.05425354, -10.09323484, -0.25273693, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28639442.33782098, 0.1125, 0.00189844, 0.00058594, 11933100.97409208, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.3283290559, 1011992, 0.3283290559, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 62.20500671, 0.00725574, 75.86873427, 0.06177573, 7.58687343, 0.31056225, -82.31003499, -0.00750633, -100.38996059, -0.06567204, -10.03899606, -0.31445855, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 62.20500671, 0.00725574, 75.86873427, 0.06193577, 7.58687343, 0.31245813, -82.31003499, -0.00750633, -100.38996059, -0.06584278, -10.03899606, -0.31636514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29322376.41958214, 0.1125, 0.00189844, 0.00058594, 12217656.84149256, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25950344179, 1111992, 0.25950344179, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 60.6618796, 0.00722277, 74.20883828, 0.05234447, 7.42088383, 0.25186104, -80.25956182, -0.00747621, -98.18305801, -0.05561517, -9.8183058, -0.25513175, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 60.6618796, 0.00722277, 74.20883828, 0.05262108, 7.42088383, 0.25505118, -80.25956182, -0.00747621, -98.18305801, -0.05591028, -9.8183058, -0.25834038, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 28199692.93836344, 0.1125, 0.00189844, 0.00058594, 11749872.05765143, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32542907872, 1211992, 0.32542907872, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 61.64335854, 0.00714356, 75.14102863, 0.05116412, 7.51410286, 0.25063718, -81.56792262, -0.0073899, -99.42835293, -0.05435408, -9.94283529, -0.25382714, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 61.6738063, 0.0071655, 75.17814335, 0.0508108, 7.51781434, 0.25013246, -61.6738063, -0.0071655, -75.17814335, -0.0508108, -7.51781434, -0.25013246, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29524055.18761269, 0.1125, 0.00189844, 0.00058594, 12301689.66150529, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32598414171, 1021992, 0.32598414171, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 62.54456873, 0.00705056, 76.48548361, 0.06446438, 7.64854836, 0.31937255, -62.54456873, -0.00705056, -76.48548361, -0.06446438, -7.64854836, -0.31937255, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 62.54456873, 0.00705056, 76.48548361, 0.06464124, 7.64854836, 0.32141604, -62.54456873, -0.00705056, -76.48548361, -0.06464124, -7.64854836, -0.32141604, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28334685.50048579, 0.1125, 0.00189844, 0.00058594, 11806118.95853575, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25776463381000003, 1121992, 0.25776463381000003, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 63.98959439, 0.00726814, 77.97662056, 0.05066245, 7.79766206, 0.25038552, -63.98959439, -0.00726814, -77.97662056, -0.05066245, -7.79766206, -0.25038552, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 63.97417902, 0.00724359, 77.95783566, 0.05074218, 7.79578357, 0.24771699, -84.64617779, -0.00749521, -103.14837827, -0.05390252, -10.31483783, -0.25087733, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29633727.98790215, 0.1125, 0.00189844, 0.00058594, 12347386.6616259, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32931383236, 1221992, 0.32931383236, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 62.29314269, 0.00733077, 76.22819587, 0.05181474, 7.62281959, 0.25090601, -62.29314269, -0.00733077, -76.22819587, -0.05181474, -7.62281959, -0.25090601, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 62.29314269, 0.00733077, 76.22819587, 0.05178952, 7.62281959, 0.2506131, -62.29314269, -0.00733077, -76.22819587, -0.05178952, -7.62281959, -0.2506131, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28076614.58566951, 0.1125, 0.00189844, 0.00058594, 11698589.41069563, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32784775875000005, 1002992, 0.32784775875000005, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 62.093442, 0.00723873, 75.92577429, 0.0637031, 7.59257743, 0.31638225, -62.093442, -0.00723873, -75.92577429, -0.0637031, -7.59257743, -0.31638225, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 62.093442, 0.00723873, 75.92577429, 0.06408479, 7.59257743, 0.32083448, -62.093442, -0.00723873, -75.92577429, -0.06408479, -7.59257743, -0.32083448, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28375615.69128516, 0.1125, 0.00189844, 0.00058594, 11823173.20470215, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.2589037123, 1102992, 0.2589037123, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 62.75371349, 0.00712935, 76.24257804, 0.05136864, 7.6242578, 0.25534635, -62.75371349, -0.00712935, -76.24257804, -0.05136864, -7.6242578, -0.25534635, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 62.75371349, 0.00712935, 76.24257804, 0.05130676, 7.6242578, 0.25460832, -62.75371349, -0.00712935, -76.24257804, -0.05130676, -7.6242578, -0.25460832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 30636485.64106415, 0.1125, 0.00189844, 0.00058594, 12765202.35044339, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32695084830000004, 1202992, 0.32695084830000004, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 61.76590595, 0.00711245, 75.46179237, 0.05274075, 7.54617924, 0.25569326, -61.76590595, -0.00711245, -75.46179237, -0.05274075, -7.54617924, -0.25569326, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 61.74499321, 0.00708841, 75.43624246, 0.05263603, 7.54362425, 0.25082587, -81.69325029, -0.00733822, -99.80779843, -0.05593158, -9.98077984, -0.25412142, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 28696330.56614274, 0.1125, 0.00189844, 0.00058594, 11956804.40255947, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32553131409999997, 1012992, 0.32553131409999997, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 61.66739627, 0.00724013, 75.19536027, 0.0642662, 7.51953603, 0.31999717, -81.59884319, -0.00748904, -99.49916459, -0.06832841, -9.94991646, -0.32405937, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 61.66739627, 0.00724013, 75.19536027, 0.06396047, 7.51953603, 0.31645112, -81.59884319, -0.00748904, -99.49916459, -0.06800223, -9.94991646, -0.32049288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29406222.36186353, 0.1125, 0.00189844, 0.00058594, 12252592.65077647, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25880191297, 1112992, 0.25880191297, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 63.7049004, 0.00738746, 77.64529705, 0.05134986, 7.76452971, 0.2516941, -84.29616031, -0.00764192, -102.74249494, -0.05454406, -10.27424949, -0.2548883, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 63.73693308, 0.00741001, 77.68433937, 0.05101888, 7.76843394, 0.25144256, -63.73693308, -0.00741001, -77.68433937, -0.05101888, -7.76843394, -0.25144256, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29563358.74450763, 0.1125, 0.00189844, 0.00058594, 12318066.14354485, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.33024383455, 1212992, 0.33024383455, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 61.5072183, 0.00709607, 75.13508205, 0.05202202, 7.51350821, 0.25307805, -61.5072183, -0.00709607, -75.13508205, -0.05202202, -7.51350821, -0.25307805, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 61.5072183, 0.00709607, 75.13508205, 0.05179409, 7.51350821, 0.25043897, -61.5072183, -0.00709607, -75.13508205, -0.05179409, -7.51350821, -0.25043897, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 28749629.27142729, 0.1125, 0.00189844, 0.00058594, 11979012.19642804, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.3251260673, 1022992, 0.3251260673, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 61.75512834, 0.00721139, 75.52727822, 0.06402174, 7.55272782, 0.31731291, -61.75512834, -0.00721139, -75.52727822, -0.06402174, -7.55272782, -0.31731291, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 61.75512834, 0.00721139, 75.52727822, 0.0637257, 7.55272782, 0.31389707, -61.75512834, -0.00721139, -75.52727822, -0.0637257, -7.55272782, -0.31389707, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 28297673.53422755, 0.1125, 0.00189844, 0.00058594, 11790697.30592815, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.25830384037, 1122992, 0.25830384037, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 61.53285774, 0.00715918, 75.33065523, 0.05170025, 7.53306552, 0.25010259, -61.53285774, -0.00715918, -75.33065523, -0.05170025, -7.53306552, -0.25010259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 61.53285774, 0.00715918, 75.33065523, 0.05226282, 7.53306552, 0.25666094, -61.53285774, -0.00715918, -75.33065523, -0.05226282, -7.53306552, -0.25666094, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 27902735.73430981, 0.1125, 0.00189844, 0.00058594, 11626139.88929575, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.32557742565000003, 1222992, 0.32557742565000003, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 67.02042162, 0.01292695, 81.62095063, 0.08944228, 8.16209506, 0.3038453, -90.31078157, -0.01391465, -109.98516074, -0.09611365, -10.99851607, -0.31051667, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 67.02042162, 0.01292695, 81.62095063, 0.08999089, 8.16209506, 0.30805842, -90.31078157, -0.01391465, -109.98516074, -0.09670302, -10.99851607, -0.31477054, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29841557.06655677, 0.075, 0.0005625, 0.00039062, 12433982.11106532, 0.00077515)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30226337767, 6200992, 0.30226337767, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 38.38488015, 0.01203337, 46.69598819, 0.08492284, 4.66959882, 0.33774328, -57.00127039, -0.0129088, -69.34320594, -0.09298147, -6.93432059, -0.34580191, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 38.38488015, 0.01203337, 46.69598819, 0.08470526, 4.66959882, 0.33573923, -57.00127039, -0.0129088, -69.34320594, -0.09274246, -6.93432059, -0.34377642, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 30212053.4747712, 0.075, 0.0005625, 0.00039062, 12588355.614488, 0.00077515)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25897687782, 6201992, 0.25897687782, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 61.52057614, 0.00708076, 74.93222898, 0.06333341, 7.4932229, 0.26275311, -91.85249084, -0.00749573, -111.87658355, -0.06929203, -11.18765835, -0.26871173, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 61.49272374, 0.00706075, 74.89830469, 0.06400114, 7.48983047, 0.26527923, -111.28947969, -0.00769173, -135.5508888, -0.07309988, -13.55508888, -0.27437797, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29798949.37089154, 0.1125, 0.00189844, 0.00058594, 12416228.90453814, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32546906213, 2001992, 0.32546906213, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 108.08774774, 0.00772388, 132.04422403, 0.06811275, 13.2044224, 0.24283136, -146.19248676, -0.00819847, -178.59446494, -0.07307311, -17.85944649, -0.24779172, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 108.08774774, 0.00772388, 132.04422403, 0.06815494, 13.2044224, 0.24316324, -146.19248676, -0.00819847, -178.59446494, -0.07311844, -17.85944649, -0.24812674, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28726942.12712905, 0.1125, 0.00189844, 0.00058594, 11969559.2196371, 0.00152995)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.37009925242999997, 2101992, 0.37009925242999997, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 107.1869, 0.00768825, 130.69016433, 0.06945164, 13.06901643, 0.24935867, -145.00340614, -0.00815359, -176.79883434, -0.07450486, -17.67988343, -0.25441188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 107.1869, 0.00768825, 130.69016433, 0.06953279, 13.06901643, 0.25000104, -145.00340614, -0.00815359, -176.79883434, -0.07459204, -17.67988343, -0.25506028, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29434225.07981342, 0.1125, 0.00189844, 0.00058594, 12264260.44992226, 0.00152995)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36912500969, 2201992, 0.36912500969, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 61.84580988, 0.007271, 75.568928, 0.06493564, 7.5568928, 0.26544077, -92.32724753, -0.00770386, -112.81396646, -0.07105131, -11.28139665, -0.27155643, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 61.81004631, 0.00725096, 75.52522876, 0.06548472, 7.55252288, 0.2667427, -111.84912554, -0.00790945, -136.66760176, -0.07480332, -13.66676018, -0.27606129, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 28648841.90421559, 0.1125, 0.00189844, 0.00058594, 11937017.46008983, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32728458887, 2301992, 0.32728458887, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 61.50025725, 0.00700123, 75.21195558, 0.06585786, 7.52119556, 0.26666011, -111.23961845, -0.0076482, -136.04088204, -0.07525757, -13.6040882, -0.27605981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 61.51834786, 0.00702386, 75.23407956, 0.06560373, 7.52340796, 0.26809341, -91.81586884, -0.00744876, -112.28653925, -0.07180163, -11.22865392, -0.2742913, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 28316338.24579484, 0.1125, 0.00189844, 0.00058594, 11798474.26908118, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32481909423000005, 2011992, 0.32481909423000005, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 106.06490997, 0.00766377, 129.46164954, 0.08183484, 12.94616495, 0.29384692, -143.48569296, -0.00813026, -175.13704109, -0.08781087, -17.51370411, -0.29982294, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 106.06490997, 0.00766377, 129.46164954, 0.07687795, 12.94616495, 0.25680817, -143.48569296, -0.00813026, -175.13704109, -0.08248577, -17.51370411, -0.26241599, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29045770.53911196, 0.1125, 0.00189844, 0.00058594, 12102404.39129665, 0.00152995)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36787119030000004, 2111992, 0.36787119030000004, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 109.42108826, 0.00761511, 133.2580874, 0.08177539, 13.32580874, 0.29769705, -147.97826418, -0.00807611, -180.21480845, -0.08774514, -18.02148085, -0.3036668, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 109.42108826, 0.00761511, 133.2580874, 0.07616411, 13.32580874, 0.25532415, -147.97826418, -0.00807611, -180.21480845, -0.08171704, -18.02148085, -0.26087709, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29843097.47066679, 0.1125, 0.00189844, 0.00058594, 12434623.94611116, 0.00152995)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.37022332279000003, 2211992, 0.37022332279000003, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 63.33838732, 0.00737166, 77.63513499, 0.06589579, 7.7635135, 0.26501656, -114.56833529, -0.00806115, -140.42871237, -0.07528856, -14.04287124, -0.27440933, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 63.36728627, 0.00739471, 77.67055702, 0.0657115, 7.7670557, 0.26706093, -94.57463453, -0.00784739, -115.92203131, -0.07191126, -11.59220313, -0.27326069, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 27405084.98089834, 0.1125, 0.00189844, 0.00058594, 11418785.40870764, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32981188686, 2311992, 0.32981188686, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 62.32990983, 0.00710656, 75.89429587, 0.05020581, 7.58942959, 0.24904751, -62.32990983, -0.00710656, -75.89429587, -0.05020581, -7.58942959, -0.24904751, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 62.31069881, 0.00708336, 75.8709041, 0.05103692, 7.58709041, 0.25532247, -82.44953733, -0.00732762, -100.39240547, -0.05422032, -10.03924055, -0.25850587, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29906155.23710596, 0.1125, 0.00189844, 0.00058594, 12460898.01546082, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32622410231, 2002992, 0.32622410231, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 61.16252043, 0.00712668, 74.42671641, 0.06475401, 7.44267164, 0.2687537, -91.32608963, -0.00754018, -111.13179977, -0.07084663, -11.11317998, -0.27484633, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 61.1279812, 0.00710814, 74.38468673, 0.06477075, 7.43846867, 0.26511178, -110.64769486, -0.00773654, -134.64364368, -0.0739743, -13.46436437, -0.27431534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 30116299.76226709, 0.1125, 0.00189844, 0.00058594, 12548458.23427796, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.32550079425, 2102992, 0.32550079425, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 62.74643782, 0.00729706, 76.69749539, 0.06612768, 7.66974954, 0.26963425, -93.66611147, -0.00773422, -114.49185646, -0.07236255, -11.44918565, -0.27586912, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 62.71616057, 0.00727565, 76.6604863, 0.06591583, 7.66604863, 0.26395364, -113.4754446, -0.00794093, -138.70560132, -0.07530164, -13.87056013, -0.27333945, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 28509587.94727152, 0.1125, 0.00189844, 0.00058594, 11878994.9780298, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.3284589195, 2202992, 0.3284589195, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 61.3421658, 0.00727032, 74.84381456, 0.05231528, 7.48438146, 0.25497275, -61.3421658, -0.00727032, -74.84381456, -0.05231528, -7.48438146, -0.25497275, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 61.30155714, 0.00724976, 74.79426778, 0.05271503, 7.47942678, 0.25587613, -81.11238692, -0.00749937, -98.96553808, -0.05600488, -9.89655381, -0.25916598, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29190373.92369734, 0.1125, 0.00189844, 0.00058594, 12162655.80154056, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32645944941, 2302992, 0.32645944941, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 60.86855484, 0.0072499, 74.52275036, 0.05394448, 7.45227504, 0.25710171, -80.53118367, -0.00750614, -98.59615218, -0.05732316, -9.85961522, -0.26048039, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 60.90910449, 0.00727183, 74.57239622, 0.05374181, 7.45723962, 0.2585538, -60.90910449, -0.00727183, -74.57239622, -0.05374181, -7.45723962, -0.2585538, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 27873804.93228042, 0.1125, 0.00189844, 0.00058594, 11614085.38845017, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32583976203, 2012992, 0.32583976203, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 62.08830398, 0.00708553, 75.79725076, 0.06614382, 7.57972508, 0.2696164, -112.33220798, -0.00773071, -137.13488677, -0.0755717, -13.71348868, -0.27904429, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 62.11047074, 0.00710728, 75.82431188, 0.06547391, 7.58243119, 0.26724553, -92.71499877, -0.00753124, -113.1862454, -0.07164986, -11.31862454, -0.27342148, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28983045.76457106, 0.1125, 0.00189844, 0.00058594, 12076269.06857128, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.32623215058, 2112992, 0.32623215058, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 61.69366544, 0.00712513, 75.47427292, 0.06544665, 7.54742729, 0.26490176, -111.60918497, -0.00778219, -136.53949764, -0.07477685, -13.65394976, -0.27423196, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 61.71999732, 0.007147, 75.5064866, 0.06504095, 7.55064866, 0.26491437, -92.125692, -0.00757859, -112.70394735, -0.07117795, -11.27039473, -0.27105137, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 28182893.87392755, 0.1125, 0.00189844, 0.00058594, 11742872.44746981, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.32606269078000005, 2212992, 0.32606269078000005, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 62.2939323, 0.00722256, 76.05564088, 0.05326693, 7.60556409, 0.25728956, -82.42438827, -0.00747468, -100.63323093, -0.056598, -10.06332309, -0.26062063, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 62.32294289, 0.00724559, 76.09106036, 0.05294815, 7.60910604, 0.25735346, -62.32294289, -0.00724559, -76.09106036, -0.05294815, -7.60910604, -0.25735346, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 28947400.7463202, 0.1125, 0.00189844, 0.00058594, 12061416.97763342, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32727839355, 2312992, 0.32727839355, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
