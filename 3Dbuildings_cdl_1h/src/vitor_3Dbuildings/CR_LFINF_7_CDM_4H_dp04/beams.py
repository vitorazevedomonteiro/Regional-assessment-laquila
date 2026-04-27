import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 61.98569266, 0.00707538, 75.11678021, 0.06306571, 7.51167802, 0.26696072, -92.56867607, -0.00747865, -112.17848178, -0.06898678, -11.21784818, -0.27288179, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 61.98569266, 0.00707538, 75.11678021, 0.06247432, 7.51167802, 0.26129768, -92.56867607, -0.00747865, -112.17848178, -0.0683371, -11.21784818, -0.26716046, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 31439546.04969477, 0.1125, 0.00189844, 0.00058594, 13099810.85403949, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32608615756000003, 1001992, 0.32608615756000003, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 62.19661906, 0.00728648, 74.99130494, 0.07472516, 7.49913049, 0.33013912, -92.89727156, -0.00768773, -112.00749695, -0.08177244, -11.2007497, -0.3371864, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 82.24123093, 0.0074765, 99.15936461, 0.07612827, 9.91593646, 0.3323587, -112.52897782, -0.00785352, -135.67771074, -0.08177181, -13.56777107, -0.33800224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 32900732.03920376, 0.1125, 0.00189844, 0.00058594, 13708638.34966823, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.26020583742000003, 1101992, 0.26020583742000003, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 79.98208025, 0.00738179, 96.63382953, 0.06327152, 9.66338295, 0.26721991, -109.43220951, -0.00775604, -132.21528429, -0.06793327, -13.22152843, -0.27188166, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 60.50796962, 0.00719199, 73.10533564, 0.06223206, 7.31053356, 0.26674408, -90.36024523, -0.00759006, -109.172661, -0.06805429, -10.9172661, -0.2725663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 32326917.99739504, 0.1125, 0.00189844, 0.00058594, 13469549.16558127, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32551425277, 1201992, 0.32551425277, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 162.22378052, 0.0078103, 194.31915944, 0.068815, 19.43191594, 0.28997492, -218.82594093, -0.00837527, -262.11984931, -0.07391148, -26.21198493, -0.29507141, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 162.22378052, 0.0078103, 194.31915944, 0.06859687, 19.43191594, 0.28788558, -218.82594093, -0.00837527, -262.11984931, -0.07367715, -26.21198493, -0.29296586, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 34588630.27248659, 0.1125, 0.00189844, 0.00058594, 14411929.28020275, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.40743358781, 1011992, 0.40743358781, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 167.64936739, 0.00780092, 202.31349685, 0.08382311, 20.23134969, 0.34738824, -225.87733631, -0.00838862, -272.58100928, -0.09005787, -27.25810093, -0.35362299, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 167.64936739, 0.00780092, 202.31349685, 0.08419731, 20.23134969, 0.3508502, -225.87733631, -0.00838862, -272.58100928, -0.09045986, -27.25810093, -0.35711275, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 32660020.0736613, 0.1125, 0.00189844, 0.00058594, 13608341.69735887, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.34234643473, 1111992, 0.34234643473, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 167.52807941, 0.00792469, 201.67724758, 0.07166709, 20.16772476, 0.29629841, -225.83660184, -0.00851274, -271.8714643, -0.07699002, -27.18714643, -0.30162135, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 167.52807941, 0.00792469, 201.67724758, 0.07118978, 20.16772476, 0.29185161, -225.83660184, -0.00851274, -271.8714643, -0.07647726, -27.18714643, -0.29713909, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 33319652.11139033, 0.1125, 0.00189844, 0.00058594, 13883188.37974597, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.41207603295, 1211992, 0.41207603295, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 224.85530194, 0.00843013, 271.4368073, 0.07244794, 27.14368073, 0.2888607, -224.85530194, -0.00843013, -271.4368073, -0.07244794, -27.14368073, -0.2888607, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 224.85530194, 0.00843013, 271.4368073, 0.07334125, 27.14368073, 0.29698605, -224.85530194, -0.00843013, -271.4368073, -0.07334125, -27.14368073, -0.29698605, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 32568278.80224955, 0.1125, 0.00189844, 0.00058594, 13570116.16760398, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.41146114879, 1021992, 0.41146114879, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 218.70550796, 0.00853121, 261.57380373, 0.08359836, 26.15738037, 0.352165, -218.70550796, -0.00853121, -261.57380373, -0.08359836, -26.15738037, -0.352165, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 218.70550796, 0.00853121, 261.57380373, 0.08304446, 26.15738037, 0.34693409, -218.70550796, -0.00853121, -261.57380373, -0.08304446, -26.15738037, -0.34693409, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 34957715.03994396, 0.1125, 0.00189844, 0.00058594, 14565714.59997665, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.34238808949000005, 1121992, 0.34238808949000005, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 223.87531112, 0.00833763, 269.16455424, 0.07215467, 26.91645542, 0.29295994, -223.87531112, -0.00833763, -269.16455424, -0.07215467, -26.91645542, -0.29295994, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 223.87531112, 0.00833763, 269.16455424, 0.07210994, 26.91645542, 0.29254829, -223.87531112, -0.00833763, -269.16455424, -0.07210994, -26.91645542, -0.29254829, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 33656767.00348818, 0.1125, 0.00189844, 0.00058594, 14023652.91812008, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.41019405898000005, 1221992, 0.41019405898000005, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 107.80351664, 0.00764478, 130.45485268, 0.06491005, 13.04548527, 0.24085241, -145.88877171, -0.0080882, -176.54246183, -0.06960723, -17.65424618, -0.24554959, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 107.80351664, 0.00764478, 130.45485268, 0.06559041, 13.04548527, 0.24653173, -145.88877171, -0.0080882, -176.54246183, -0.07033813, -17.65424618, -0.25127945, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 31865807.34620448, 0.1125, 0.00189844, 0.00058594, 13277419.7275852, 0.00152995)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.36960777756, 1031992, 0.36960777756, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 110.28219016, 0.00751231, 132.8522734, 0.076475, 13.28522734, 0.29451906, -149.20541739, -0.00794312, -179.74143309, -0.08202846, -17.97414331, -0.30007253, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 110.28219016, 0.00751231, 132.8522734, 0.07634083, 13.28522734, 0.29337998, -149.20541739, -0.00794312, -179.74143309, -0.08188433, -17.97414331, -0.29892348, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 33138469.67882221, 0.1125, 0.00189844, 0.00058594, 13807695.69950926, 0.00152995)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.30238315055, 1131992, 0.30238315055, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 104.83552733, 0.00751854, 126.48527839, 0.06601899, 12.64852784, 0.24755556, -141.90511645, -0.00794671, -171.21016717, -0.07079267, -17.12101672, -0.25232924, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 104.83552733, 0.00751854, 126.48527839, 0.06607499, 12.64852784, 0.24802403, -141.90511645, -0.00794671, -171.21016717, -0.07085282, -17.12101672, -0.25280186, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 32718505.26519704, 0.1125, 0.00189844, 0.00058594, 13632710.52716543, 0.00152995)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.36596517285, 1231992, 0.36596517285, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 62.79449607, 0.00708707, 75.97938121, 0.06169555, 7.59793812, 0.2635944, -93.77782819, -0.00748912, -113.46824647, -0.06747922, -11.34682465, -0.26937807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 62.79449607, 0.00708707, 75.97938121, 0.06198074, 7.59793812, 0.26638973, -93.77782819, -0.00748912, -113.46824647, -0.06779252, -11.34682465, -0.27220151, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 31901831.31605276, 0.1125, 0.00189844, 0.00058594, 13292429.71502198, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32708897187999997, 1002992, 0.32708897187999997, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 62.12137485, 0.00699297, 74.52319447, 0.0726411, 7.45231945, 0.32849265, -92.80476595, -0.00737458, -111.33217248, -0.07949228, -11.13321725, -0.33534384, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 62.09395868, 0.00697621, 74.49030497, 0.07324243, 7.4490305, 0.32978063, -112.47468197, -0.00755478, -134.92896152, -0.08367563, -13.49289615, -0.34021382, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 34220055.49118836, 0.1125, 0.00189844, 0.00058594, 14258356.45466182, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25778382057, 1102992, 0.25778382057, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 63.05668585, 0.00735921, 76.20481995, 0.06084004, 7.62048199, 0.26030935, -114.18332115, -0.00798282, -137.9920196, -0.06941693, -13.79920196, -0.26888624, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 63.09705298, 0.00737542, 76.25360415, 0.06060117, 7.62536042, 0.26171447, -94.23800635, -0.00778651, -113.88784884, -0.06625762, -11.38878488, -0.26737091, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 32251348.43962946, 0.1125, 0.00189844, 0.00058594, 13438061.84984561, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32986908954, 1202992, 0.32986908954, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 108.25301083, 0.00745716, 129.99068707, 0.06390198, 12.99906871, 0.24517073, -146.50679719, -0.00787749, -175.92600041, -0.06851511, -17.59260004, -0.24978387, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 108.25301083, 0.00745716, 129.99068707, 0.06329233, 12.99906871, 0.23995128, -146.50679719, -0.00787749, -175.92600041, -0.06786018, -17.59260004, -0.24451913, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 33975536.14441723, 0.1125, 0.00189844, 0.00058594, 14156473.39350718, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36829791531, 1012992, 0.36829791531, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 109.31781924, 0.00751874, 131.66225453, 0.07534785, 13.16622545, 0.29041123, -147.92278747, -0.00794837, -178.15803343, -0.08081593, -17.81580334, -0.29587931, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 109.31781924, 0.00751874, 131.66225453, 0.07519187, 13.16622545, 0.28908401, -147.92278747, -0.00794837, -178.15803343, -0.08064837, -17.81580334, -0.2945405, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 33196144.11519616, 0.1125, 0.00189844, 0.00058594, 13831726.71466507, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30169679643, 1112992, 0.30169679643, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 106.60142115, 0.00736229, 128.04423877, 0.06364036, 12.80442388, 0.24364187, -144.27407318, -0.00777749, -173.29472418, -0.06823598, -17.32947242, -0.24823749, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 106.60142115, 0.00736229, 128.04423877, 0.06386903, 12.80442388, 0.24561029, -144.27407318, -0.00777749, -173.29472418, -0.06848164, -17.32947242, -0.2502229, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 33902409.08913881, 0.1125, 0.00189844, 0.00058594, 14126003.78714117, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36592484305, 1212992, 0.36592484305, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 168.3964545, 0.00807929, 202.6235368, 0.06958278, 20.26235368, 0.28809397, -227.07680949, -0.00867551, -273.2308492, -0.07474758, -27.32308492, -0.29325877, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 168.3964545, 0.00807929, 202.6235368, 0.07004067, 20.26235368, 0.29243044, -227.07680949, -0.00867551, -273.2308492, -0.07523948, -27.32308492, -0.29762925, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 33448962.30095913, 0.1125, 0.00189844, 0.00058594, 13937067.62539964, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.41468811429, 1022992, 0.41468811429, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 168.11056117, 0.00790165, 202.02344273, 0.08137617, 20.20234427, 0.34380763, -226.6200739, -0.0084843, -272.33605791, -0.08741661, -27.23360579, -0.34984807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 168.11056117, 0.00790165, 202.02344273, 0.08102699, 20.20234427, 0.34050966, -226.6200739, -0.0084843, -272.33605791, -0.08704149, -27.23360579, -0.34652416, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 33778679.36417547, 0.1125, 0.00189844, 0.00058594, 14074449.73507311, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.34426181494, 1122992, 0.34426181494, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 164.59788666, 0.00794028, 198.27311381, 0.07077114, 19.82731138, 0.29114305, -221.96007752, -0.00852847, -267.37108602, -0.0760265, -26.7371086, -0.29639842, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 164.59788666, 0.00794028, 198.27311381, 0.07090588, 19.82731138, 0.29240044, -221.96007752, -0.00852847, -267.37108602, -0.07617125, -26.7371086, -0.29766582, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 33153353.28654847, 0.1125, 0.00189844, 0.00058594, 13813897.20272853, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.41033222457, 1222992, 0.41033222457, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 106.39295684, 0.00757511, 127.57026227, 0.06140483, 12.75702623, 0.23677906, -144.03991599, -0.00799554, -172.7107734, -0.06582382, -17.27107734, -0.24119805, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 106.39295684, 0.00757511, 127.57026227, 0.06165422, 12.75702623, 0.23896192, -144.03991599, -0.00799554, -172.7107734, -0.06609174, -17.27107734, -0.24339944, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 34342459.65709812, 0.1125, 0.00189844, 0.00058594, 14309358.19045755, 0.00152995)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.36809953872, 1032992, 0.36809953872, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 107.8627472, 0.00737414, 130.31095588, 0.0793794, 13.03109559, 0.30126992, -145.91501917, -0.00780249, -176.28260097, -0.08515642, -17.6282601, -0.30704694, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 107.8627472, 0.00737414, 130.31095588, 0.07850701, 13.03109559, 0.29407344, -145.91501917, -0.00780249, -176.28260097, -0.08421922, -17.6282601, -0.29978566, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 32344658.34791895, 0.1125, 0.00189844, 0.00058594, 13476940.97829956, 0.00152995)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.29880432012, 1132992, 0.29880432012, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 107.72661373, 0.00749972, 129.52591703, 0.06279885, 12.9525917, 0.23955419, -145.80322548, -0.00792359, -175.30762207, -0.06733042, -17.53076221, -0.24408576, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 107.72661373, 0.00749972, 129.52591703, 0.06338498, 12.9525917, 0.24461671, -145.80322548, -0.00792359, -175.30762207, -0.06796009, -17.53076221, -0.24919182, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 33643614.61677397, 0.1125, 0.00189844, 0.00058594, 14018172.75698915, 0.00152995)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.36828286416, 1232992, 0.36828286416, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 63.12180774, 0.006966, 75.22404627, 0.05530328, 7.52240463, 0.25371929, -94.31159546, -0.00733907, -112.39379978, -0.06043995, -11.23937998, -0.25885596, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 63.12180774, 0.006966, 75.22404627, 0.0553281, 7.52240463, 0.25398587, -94.31159546, -0.00733907, -112.39379978, -0.06046722, -11.23937998, -0.25912499, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 35786251.02302928, 0.1125, 0.00189844, 0.00058594, 14910937.9262622, 0.00152995)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32673787608, 1003992, 0.32673787608, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 61.95087977, 0.00720183, 74.63474918, 0.07208699, 7.46347492, 0.32098326, -92.53611616, -0.00759796, -111.48202972, -0.07887749, -11.14820297, -0.32777377, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 61.95087977, 0.00720183, 74.63474918, 0.07261651, 7.46347492, 0.32635804, -92.53611616, -0.00759796, -111.48202972, -0.0794592, -11.14820297, -0.33320073, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 33119876.42520767, 0.1125, 0.00189844, 0.00058594, 13799948.5105032, 0.00152995)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25925967428, 1103992, 0.25925967428, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 61.88342249, 0.00710252, 73.58854967, 0.05593827, 7.35885497, 0.25795948, -92.46628689, -0.00747524, -109.95610248, -0.06112372, -10.99561025, -0.26314493, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 61.88342249, 0.00710252, 73.58854967, 0.05615742, 7.35885497, 0.26033572, -92.46628689, -0.00747524, -109.95610248, -0.06136447, -10.99561025, -0.26554277, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 36266146.39601858, 0.1125, 0.00189844, 0.00058594, 15110894.33167441, 0.00152995)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32661461892, 1203992, 0.32661461892, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 61.91550794, 0.00711618, 74.25470164, 0.04722304, 7.42547016, 0.24841852, -81.95480002, -0.00734034, -98.28764111, -0.05012912, -9.82876411, -0.2513246, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 61.91550794, 0.00711618, 74.25470164, 0.04701543, 7.42547016, 0.24574911, -81.95480002, -0.00734034, -98.28764111, -0.04990762, -9.82876411, -0.24864131, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 34292239.56907901, 0.1125, 0.00189844, 0.00058594, 14288433.15378292, 0.00152995)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32651391565, 1013992, 0.32651391565, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 61.75613544, 0.00703629, 74.48938124, 0.05927554, 7.44893812, 0.31216024, -81.73800206, -0.0072651, -98.59122749, -0.06299755, -9.85912275, -0.31588225, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 61.75613544, 0.00703629, 74.48938124, 0.0596238, 7.44893812, 0.31652588, -81.73800206, -0.0072651, -98.59122749, -0.0633691, -9.85912275, -0.32027118, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 32793137.2361488, 0.1125, 0.00189844, 0.00058594, 13663807.18172867, 0.00152995)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25753400807000004, 1113992, 0.25753400807000004, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 60.54486978, 0.00711167, 73.15285325, 0.04848235, 7.31528533, 0.24716806, -80.12526428, -0.00734197, -96.81070785, -0.05147908, -9.68107078, -0.25016479, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 60.54486978, 0.00711167, 73.15285325, 0.04875612, 7.31528533, 0.25057491, -80.12526428, -0.00734197, -96.81070785, -0.05177117, -9.68107078, -0.25358995, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 32315474.36894901, 0.1125, 0.00189844, 0.00058594, 13464780.98706209, 0.00152995)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32480731753, 1213992, 0.32480731753, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 109.05067177, 0.00755345, 131.27310787, 0.06412134, 13.12731079, 0.24350637, -147.57844136, -0.00798322, -177.65209822, -0.06875306, -17.76520982, -0.24813809, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 109.05067177, 0.00755345, 131.27310787, 0.06365429, 13.12731079, 0.2395459, -147.57844136, -0.00798322, -177.65209822, -0.06825131, -17.76520982, -0.24414293, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 33333026.53900156, 0.1125, 0.00189844, 0.00058594, 13888761.05791732, 0.00152995)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36988400798, 1023992, 0.36988400798, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 106.51759175, 0.00747655, 128.3868553, 0.07790771, 12.83868553, 0.29849551, -144.16262787, -0.00790289, -173.76084213, -0.08356578, -17.37608421, -0.30415358, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 106.51759175, 0.00747655, 128.3868553, 0.07763846, 12.83868553, 0.29623113, -144.16262787, -0.00790289, -173.76084213, -0.08327652, -17.37608421, -0.3018692, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 32991738.47555474, 0.1125, 0.00189844, 0.00058594, 13746557.69814781, 0.00152995)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.29894712469, 1123992, 0.29894712469, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 108.39201147, 0.00750217, 131.16209016, 0.06587038, 13.11620902, 0.24455801, -146.64281037, -0.00794015, -177.44829397, -0.07064404, -17.7448294, -0.24933167, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 108.39201147, 0.00750217, 131.16209016, 0.06600322, 13.11620902, 0.2456571, -146.64281037, -0.00794015, -177.44829397, -0.07078675, -17.7448294, -0.25044063, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 31876838.90865884, 0.1125, 0.00189844, 0.00058594, 13282016.21194118, 0.00152995)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36854896975, 1223992, 0.36854896975, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 62.61056696, 0.00701064, 75.49519788, 0.06011538, 7.54951979, 0.26100157, -93.51370671, -0.00740257, -112.75789592, -0.06574074, -11.27578959, -0.26662693, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 62.61056696, 0.00701064, 75.49519788, 0.06006854, 7.54951979, 0.2605347, -93.51370671, -0.00740257, -112.75789592, -0.06568929, -11.27578959, -0.26615545, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 32883358.57523099, 0.1125, 0.00189844, 0.00058594, 13701399.40634625, 0.00152995)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32633163028, 1033992, 0.32633163028, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 64.44834385, 0.00709712, 77.53459255, 0.0708492, 7.75345925, 0.31870433, -96.25457541, -0.00749187, -115.79908559, -0.07752667, -11.57990856, -0.3253818, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 64.44834385, 0.00709712, 77.53459255, 0.0708937, 7.75345925, 0.31915935, -96.25457541, -0.00749187, -115.79908559, -0.07757554, -11.57990856, -0.3258412, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 33493269.1926375, 0.1125, 0.00189844, 0.00058594, 13955528.83026562, 0.00152995)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.26105869514, 1133992, 0.26105869514, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 61.66963496, 0.0070532, 74.81066692, 0.06139519, 7.48106669, 0.25963691, -92.09279157, -0.00745726, -111.7166197, -0.06715461, -11.17166197, -0.26539633, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 61.66963496, 0.0070532, 74.81066692, 0.06213901, 7.48106669, 0.26687793, -92.09279157, -0.00745726, -111.7166197, -0.06797174, -11.17166197, -0.27271066, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 31122970.96286335, 0.1125, 0.00189844, 0.00058594, 12967904.56785973, 0.00152995)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32553000974, 1233992, 0.32553000974, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 61.82362195, 0.00694136, 74.63610163, 0.04815167, 7.46361016, 0.2479542, -61.82362195, -0.00694136, -74.63610163, -0.04815167, -7.46361016, -0.2479542, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 61.82362195, 0.00694136, 74.63610163, 0.04847687, 7.46361016, 0.25203969, -61.82362195, -0.00694136, -74.63610163, -0.04847687, -7.46361016, -0.25203969, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 32549623.50929525, 0.1125, 0.00189844, 0.00058594, 13562343.12887302, 0.00152995)
    ops.section('Aggregator', 1004991, 1004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1004992, 1004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.32457129289000003, 1004992, 0.32457129289000003, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 61.52775058, 0.00706983, 74.22734732, 0.06070547, 7.42273473, 0.31878241, -61.52775058, -0.00706983, -74.22734732, -0.06070547, -7.42273473, -0.31878241, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 61.52775058, 0.00706983, 74.22734732, 0.06068608, 7.42273473, 0.31854182, -61.52775058, -0.00706983, -74.22734732, -0.06068608, -7.42273473, -0.31854182, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 32743117.03558054, 0.1125, 0.00189844, 0.00058594, 13642965.43149189, 0.00152995)
    ops.section('Aggregator', 1104991, 1104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1104992, 1104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.257377428, 1104992, 0.257377428, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 62.12837083, 0.0072214, 74.98186001, 0.04823688, 7.498186, 0.24831455, -62.12837083, -0.0072214, -74.98186001, -0.04823688, -7.498186, -0.24831455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 62.12837083, 0.0072214, 74.98186001, 0.04798963, 7.498186, 0.24521808, -62.12837083, -0.0072214, -74.98186001, -0.04798963, -7.498186, -0.24521808, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 32632236.00617181, 0.1125, 0.00189844, 0.00058594, 13596765.00257159, 0.00152995)
    ops.section('Aggregator', 1204991, 1204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1204992, 1204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.32728302357, 1204992, 0.32728302357, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 62.6111577, 0.0072343, 75.33876697, 0.04743199, 7.5338767, 0.24759626, -62.6111577, -0.0072343, -75.33876697, -0.04743199, -7.5338767, -0.24759626, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 62.6111577, 0.0072343, 75.33876697, 0.04744513, 7.5338767, 0.2477646, -62.6111577, -0.0072343, -75.33876697, -0.04744513, -7.5338767, -0.2477646, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 33443004.63960964, 0.1125, 0.00189844, 0.00058594, 13934585.26650402, 0.00152995)
    ops.section('Aggregator', 1014991, 1014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1014992, 1014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.32799234398, 1014992, 0.32799234398, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 62.33332503, 0.0068473, 74.73478803, 0.05861971, 7.4734788, 0.31730851, -62.33332503, -0.0068473, -74.73478803, -0.05861971, -7.4734788, -0.31730851, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 62.33332503, 0.0068473, 74.73478803, 0.05866679, 7.4734788, 0.31791395, -62.33332503, -0.0068473, -74.73478803, -0.05866679, -7.4734788, -0.31791395, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 34361860.67068245, 0.1125, 0.00189844, 0.00058594, 14317441.94611769, 0.00152995)
    ops.section('Aggregator', 1114991, 1114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1114992, 1114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.25646304974, 1114992, 0.25646304974, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 61.67696992, 0.00718353, 74.57413345, 0.05044754, 7.45741335, 0.25546683, -61.67696992, -0.00718353, -74.57413345, -0.05044754, -7.45741335, -0.25546683, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 61.67696992, 0.00718353, 74.57413345, 0.04993265, 7.45741335, 0.24921135, -61.67696992, -0.00718353, -74.57413345, -0.04993265, -7.45741335, -0.24921135, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 32109447.136572, 0.1125, 0.00189844, 0.00058594, 13378936.306905, 0.00152995)
    ops.section('Aggregator', 1214991, 1214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1214992, 1214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.32642655312, 1214992, 0.32642655312, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 63.06792398, 0.00711823, 75.9457139, 0.0485841, 7.59457139, 0.25185136, -63.06792398, -0.00711823, -75.9457139, -0.0485841, -7.59457139, -0.25185136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 63.0429013, 0.00709848, 75.91558186, 0.04887629, 7.59155819, 0.25178389, -83.44308692, -0.00732851, -100.48126537, -0.05189998, -10.04812654, -0.25480758, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 33242712.8319213, 0.1125, 0.00189844, 0.00058594, 13851130.34663388, 0.00152995)
    ops.section('Aggregator', 1024991, 1024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1024992, 1024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.32747216651000005, 1024992, 0.32747216651000005, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 62.42205322, 0.00701673, 75.33119333, 0.06144988, 7.53311933, 0.32037797, -82.6166322, -0.00724684, -99.70209521, -0.0653199, -9.97020952, -0.32424799, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 62.42205322, 0.00701673, 75.33119333, 0.06076013, 7.53311933, 0.31197291, -82.6166322, -0.00724684, -99.70209521, -0.06458402, -9.97020952, -0.3157968, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 32651133.92543878, 0.1125, 0.00189844, 0.00058594, 13604639.13559949, 0.00152995)
    ops.section('Aggregator', 1124991, 1124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1124992, 1124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.25805754242, 1124992, 0.25805754242, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 61.46279007, 0.00699193, 73.85453416, 0.04740113, 7.38545342, 0.24760958, -81.35547964, -0.00721517, -97.75786362, -0.0503265, -9.77578636, -0.25053496, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 61.49443764, 0.00700972, 73.89256231, 0.04717849, 7.38925623, 0.24846975, -61.49443764, -0.00700972, -73.89256231, -0.04717849, -7.38925623, -0.24846975, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 33803470.51114417, 0.1125, 0.00189844, 0.00058594, 14084779.3796434, 0.00152995)
    ops.section('Aggregator', 1224991, 1224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1224992, 1224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.32493789067, 1224992, 0.32493789067, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 60.4162516, 0.00716255, 72.92286478, 0.04850038, 7.29228648, 0.2489131, -60.4162516, -0.00716255, -72.92286478, -0.04850038, -7.29228648, -0.2489131, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 60.4162516, 0.00716255, 72.92286478, 0.04890316, 7.29228648, 0.25397896, -60.4162516, -0.00716255, -72.92286478, -0.04890316, -7.29228648, -0.25397896, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 32604142.83439787, 0.1125, 0.00189844, 0.00058594, 13585059.51433245, 0.00152995)
    ops.section('Aggregator', 1034991, 1034990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1034992, 1034991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.3249293957, 1034992, 0.3249293957, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 62.69873915, 0.00701618, 75.04110608, 0.05781723, 7.50411061, 0.31573678, -62.69873915, -0.00701618, -75.04110608, -0.05781723, -7.50411061, -0.31573678, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 62.69873915, 0.00701618, 75.04110608, 0.05788795, 7.50411061, 0.31665995, -62.69873915, -0.00701618, -75.04110608, -0.05788795, -7.50411061, -0.31665995, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 34789476.18816111, 0.1125, 0.00189844, 0.00058594, 14495615.07840046, 0.00152995)
    ops.section('Aggregator', 1134991, 1134990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1134992, 1134991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.25835909575, 1134992, 0.25835909575, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 62.50991525, 0.0070801, 75.59734354, 0.04916393, 7.55973435, 0.25054913, -62.50991525, -0.0070801, -75.59734354, -0.04916393, -7.55973435, -0.25054913, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 62.50991525, 0.0070801, 75.59734354, 0.04917088, 7.55973435, 0.25063495, -62.50991525, -0.0070801, -75.59734354, -0.04917088, -7.55973435, -0.25063495, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 32047663.94733731, 0.1125, 0.00189844, 0.00058594, 13353193.31139055, 0.00152995)
    ops.section('Aggregator', 1234991, 1234990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1234992, 1234991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.32643170891, 1234992, 0.32643170891, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 79.22352536, 0.01045803, 95.3065204, 0.08126255, 9.53065204, 0.29796284, -121.04485898, -0.01141652, -145.61791173, -0.08970006, -14.56179117, -0.30640035, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 79.22352536, 0.01045803, 95.3065204, 0.08124358, 9.53065204, 0.29780619, -121.04485898, -0.01141652, -145.61791173, -0.08967909, -14.56179117, -0.30624169, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 33502511.16590116, 0.0875, 0.00089323, 0.00045573, 13959379.65245882, 0.0010204)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30067814807000004, 6200992, 0.30067814807000004, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 139.96591825, 0.00904072, 167.81544138, 0.08621382, 16.78154414, 0.35783424, -188.60114098, -0.0097441, -226.12778963, -0.09264974, -22.61277896, -0.36427016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 139.96591825, 0.00904072, 167.81544138, 0.0865199, 16.78154414, 0.36070271, -188.60114098, -0.0097441, -226.12778963, -0.09297856, -22.61277896, -0.36716136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 34357813.15469437, 0.1, 0.00133333, 0.00052083, 14315755.48112266, 0.00127345)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.33811379111, 6201992, 0.33811379111, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 95.49367241, 0.00853532, 115.16589382, 0.07962847, 11.51658938, 0.29739044, -145.99024335, -0.00928347, -176.06503592, -0.08788613, -17.60650359, -0.3056481, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 95.49367241, 0.00853532, 115.16589382, 0.07962667, 11.51658938, 0.29737558, -145.99024335, -0.00928347, -176.06503592, -0.08788414, -17.60650359, -0.30563305, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 32834324.09251722, 0.1, 0.00133333, 0.00052083, 13680968.37188218, 0.00127345)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.30048061208000004, 6202992, 0.30048061208000004, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 6203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6203990, 39.1105744, 0.01168859, 47.46017472, 0.0856165, 4.74601747, 0.34423066, -58.12814876, -0.01253867, -70.53775453, -0.09375212, -7.05377545, -0.35236627, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6203991, 39.06780265, 0.01165304, 47.40827175, 0.08587693, 4.74082718, 0.3394093, -70.34453571, -0.01293253, -85.36218162, -0.09819446, -8.53621816, -0.35172682, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6203990, 31020016.72794189, 0.075, 0.0005625, 0.00039062, 12925006.96997579, 0.00077515)
    ops.section('Aggregator', 6203991, 6203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6203992, 6203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6203, 6203991, 0.2587374952, 6203992, 0.2587374952, 6203990)
    # Create element
    ops.element('forceBeamColumn', 6203, 1104, 1204, 6203, 6203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 109.04684144, 0.00750198, 130.79056733, 0.06115916, 13.07905673, 0.23603419, -147.58677937, -0.00792291, -177.01529314, -0.06556583, -17.70152931, -0.24044086, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 109.04684144, 0.00750198, 130.79056733, 0.06122952, 13.07905673, 0.23664893, -147.58677937, -0.00792291, -177.01529314, -0.06564141, -17.70152931, -0.24106082, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 34270020.30468558, 0.1125, 0.00189844, 0.00058594, 14279175.12695232, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36947125973, 2001992, 0.36947125973, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 186.64101405, 0.00706313, 225.35974918, 0.06291009, 22.53597492, 0.24777885, -252.25478903, -0.00750965, -304.58512173, -0.067505, -30.45851217, -0.25237376, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 186.64101405, 0.00706313, 225.35974918, 0.06315929, 22.53597492, 0.24999082, -252.25478903, -0.00750965, -304.58512173, -0.06777271, -30.45851217, -0.25460424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 32501241.72994008, 0.15, 0.003125, 0.001125, 13542184.0541417, 0.00281737)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41340766998, 2101992, 0.41340766998, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 190.04294872, 0.00685549, 228.7257945, 0.06218747, 22.87257945, 0.24887725, -256.72149707, -0.0072876, -308.97662227, -0.06672971, -30.89766223, -0.2534195, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 190.04294872, 0.00685549, 228.7257945, 0.06276834, 22.87257945, 0.25414061, -256.72149707, -0.0072876, -308.97662227, -0.06735373, -30.89766223, -0.25872601, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 33384293.53146822, 0.15, 0.003125, 0.001125, 13910122.30477842, 0.00281737)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.4125045587, 2201992, 0.4125045587, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 108.90668238, 0.00742212, 131.62704619, 0.06641358, 13.16270462, 0.24792516, -147.31594521, -0.00785453, -178.0493382, -0.07122797, -17.80493382, -0.25273956, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 108.90668238, 0.00742212, 131.62704619, 0.06637901, 13.16270462, 0.24763841, -147.31594521, -0.00785453, -178.0493382, -0.07119084, -17.80493382, -0.25245024, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 32225379.62888618, 0.1125, 0.00189844, 0.00058594, 13427241.51203591, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36813905977, 2301992, 0.36813905977, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 109.26007509, 0.00738067, 131.55384344, 0.06273903, 13.15538434, 0.23824655, -147.80746571, -0.00780389, -177.96656452, -0.06727435, -17.79665645, -0.24278188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 109.26007509, 0.00738067, 131.55384344, 0.06281659, 13.15538434, 0.23890798, -147.80746571, -0.00780389, -177.96656452, -0.06735767, -17.79665645, -0.24344907, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 33275080.03540253, 0.1125, 0.00189844, 0.00058594, 13864616.68141772, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36813830666, 2011992, 0.36813830666, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 191.7815721, 0.00703564, 231.16472956, 0.06324561, 23.11647296, 0.25160299, -259.11931929, -0.00748026, -312.33056813, -0.0678656, -31.23305681, -0.25622298, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 191.78065665, 0.00699086, 231.16362612, 0.06401016, 23.11636261, 0.25108787, -319.34630593, -0.00775688, -384.92542135, -0.07207757, -38.49254214, -0.25915528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 32982048.08320669, 0.15, 0.003125, 0.001125, 13742520.03466946, 0.00281737)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41612619268, 2111992, 0.41612619268, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 186.71124343, 0.00672961, 223.38119873, 0.06213191, 22.33811987, 0.25512788, -252.30286911, -0.00714345, -301.85497301, -0.06666112, -30.1854973, -0.25965709, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 186.72564591, 0.00668843, 223.39842984, 0.0627603, 22.33984298, 0.25341009, -310.98488431, -0.00740058, -372.06209421, -0.07065252, -37.20620942, -0.26130231, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 34880060.91738372, 0.15, 0.003125, 0.001125, 14533358.71557655, 0.00281737)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40901433089, 2211992, 0.40901433089, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 108.21701685, 0.00742251, 130.24057642, 0.0632704, 13.02405764, 0.24047696, -146.43349409, -0.00784554, -176.23459999, -0.06784189, -17.62346, -0.24504845, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 108.21701685, 0.00742251, 130.24057642, 0.06345383, 13.02405764, 0.24204412, -146.43349409, -0.00784554, -176.23459999, -0.06803895, -17.62346, -0.24662924, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 33391984.224696, 0.1125, 0.00189844, 0.00058594, 13913326.76029, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36779530651, 2311992, 0.36779530651, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 108.75812715, 0.00779531, 131.7993396, 0.06559386, 13.17993396, 0.24196497, -147.18395177, -0.00824966, -178.36595895, -0.07034158, -17.83659589, -0.24671268, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 108.75812715, 0.00779531, 131.7993396, 0.06525438, 13.17993396, 0.23917802, -147.18395177, -0.00824966, -178.36595895, -0.06997687, -17.83659589, -0.24390052, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 31435336.56331982, 0.1125, 0.00189844, 0.00058594, 13098056.90138326, 0.00152995)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.37191211544999997, 2021992, 0.37191211544999997, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 188.67998453, 0.00685963, 228.94272195, 0.06799076, 22.8942722, 0.25962194, -313.91911519, -0.0076399, -380.90684014, -0.07659895, -38.09068401, -0.26823013, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 188.63356563, 0.00690796, 228.88639765, 0.06629927, 22.88863976, 0.25268339, -254.73783458, -0.00736005, -309.09676709, -0.07116303, -30.90967671, -0.25754716, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 31044662.02172714, 0.15, 0.003125, 0.001125, 12935275.84238631, 0.00281737)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.41193575153, 2121992, 0.41193575153, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 188.84945295, 0.00689282, 227.98812394, 0.06495054, 22.79881239, 0.25355149, -314.42647386, -0.00765389, -379.59073097, -0.07314598, -37.9590731, -0.26174693, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 188.84574857, 0.00693771, 227.98365183, 0.06359076, 22.79836518, 0.24894401, -255.13313721, -0.00737931, -308.00896903, -0.06824063, -30.8008969, -0.25359388, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 32548337.18360622, 0.15, 0.003125, 0.001125, 13561807.15983593, 0.00281737)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.41286469507, 2221992, 0.41286469507, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 106.11339221, 0.00742049, 127.33116627, 0.06382829, 12.73311663, 0.2452841, -143.63855646, -0.00783576, -172.35962903, -0.06843362, -17.2359629, -0.24988943, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 106.11339221, 0.00742049, 127.33116627, 0.06365141, 12.73311663, 0.24376045, -143.63855646, -0.00783576, -172.35962903, -0.0682436, -17.2359629, -0.24835264, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 34154313.08660298, 0.1125, 0.00189844, 0.00058594, 14230963.78608458, 0.00152995)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.36619781176, 2321992, 0.36619781176, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 106.83606585, 0.00763265, 128.0527869, 0.06172806, 12.80527869, 0.23841283, -144.64405546, -0.0080552, -173.36911708, -0.0661689, -17.33691171, -0.24285367, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 106.83606585, 0.00763265, 128.0527869, 0.06146795, 12.80527869, 0.23614413, -144.64405546, -0.0080552, -173.36911708, -0.06588947, -17.33691171, -0.24056565, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 34436457.63434199, 0.1125, 0.00189844, 0.00058594, 14348524.01430916, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.36908639321, 2002992, 0.36908639321, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 183.42348939, 0.00690188, 221.11782215, 0.06910484, 22.11178222, 0.28917065, -247.57525005, -0.00738324, -298.45305141, -0.07420672, -29.84530514, -0.29427254, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 183.42348939, 0.00690188, 221.11782215, 0.06956244, 22.11178222, 0.29348794, -247.57525005, -0.00738324, -298.45305141, -0.07469832, -29.84530514, -0.29862383, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 32948117.60617994, 0.125, 0.00260417, 0.00065104, 13728382.33590831, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.40788612964, 2102992, 0.40788612964, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 189.03808459, 0.00703124, 227.76121804, 0.06847364, 22.7761218, 0.28797138, -255.10461516, -0.00752174, -307.36101671, -0.07352817, -30.73610167, -0.29302591, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 189.03808459, 0.00703124, 227.76121804, 0.06821159, 22.7761218, 0.28549517, -255.10461516, -0.00752174, -307.36101671, -0.07324666, -30.73610167, -0.29053023, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 33096985.82814714, 0.125, 0.00260417, 0.00065104, 13790410.76172798, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.41307100311, 2202992, 0.41307100311, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 104.4867735, 0.00721865, 125.85486611, 0.06479249, 12.58548661, 0.24478888, -141.39326798, -0.00763079, -170.30893208, -0.06948131, -17.03089321, -0.2494777, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 104.4867735, 0.00721865, 125.85486611, 0.06541161, 12.58548661, 0.25003326, -141.39326798, -0.00763079, -170.30893208, -0.07014642, -17.03089321, -0.25476807, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 33172451.41343711, 0.1125, 0.00189844, 0.00058594, 13821854.7555988, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.3625453102, 2302992, 0.3625453102, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 108.66853846, 0.0075424, 130.80844352, 0.06416332, 13.08084435, 0.24364433, -147.06511495, -0.00797123, -177.02785972, -0.06879804, -17.70278597, -0.24827905, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 108.66853846, 0.0075424, 130.80844352, 0.06400309, 13.08084435, 0.24228163, -147.06511495, -0.00797123, -177.02785972, -0.06862591, -17.70278597, -0.24690445, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 33342477.8015832, 0.1125, 0.00189844, 0.00058594, 13892699.083993, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.36945764055, 2012992, 0.36945764055, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 186.31980569, 0.00696985, 223.83189377, 0.06828401, 22.38318938, 0.29073659, -251.51447272, -0.00744905, -302.15231564, -0.07331772, -30.21523156, -0.2957703, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 186.31980569, 0.00696985, 223.83189377, 0.06820935, 22.38318938, 0.29001988, -251.51447272, -0.00744905, -302.15231564, -0.07323751, -30.21523156, -0.29504805, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 33863644.51834634, 0.125, 0.00260417, 0.00065104, 14109851.88264431, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.41078115299, 2112992, 0.41078115299, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 189.62828624, 0.00723238, 229.28772365, 0.0687623, 22.92877236, 0.28456693, -255.95934779, -0.0077427, -309.49146545, -0.07384317, -30.94914655, -0.28964779, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 189.62828624, 0.00723238, 229.28772365, 0.06907441, 22.92877236, 0.28748468, -255.95934779, -0.0077427, -309.49146545, -0.07417845, -30.94914655, -0.29258872, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 32101111.10872073, 0.125, 0.00260417, 0.00065104, 13375462.96196697, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.41612902789, 2212992, 0.41612902789, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 109.55718056, 0.0076063, 130.98657517, 0.06008542, 13.09865752, 0.23505759, -148.31133703, -0.00802665, -177.32104823, -0.06440401, -17.73210482, -0.23937618, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 109.55718056, 0.0076063, 130.98657517, 0.06072206, 13.09865752, 0.24077126, -148.31133703, -0.00802665, -177.32104823, -0.06508793, -17.73210482, -0.24513713, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 35038759.90709465, 0.1125, 0.00189844, 0.00058594, 14599483.29462277, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.37113547148, 2312992, 0.37113547148, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 109.26041527, 0.00756548, 130.91953187, 0.06234948, 13.09195319, 0.24154177, -147.89283604, -0.00798754, -177.21020749, -0.06684097, -17.72102075, -0.24603327, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 109.26041527, 0.00756548, 130.91953187, 0.06172042, 13.09195319, 0.23607034, -147.89283604, -0.00798754, -177.21020749, -0.06616518, -17.72102075, -0.24051511, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 34509656.62308068, 0.1125, 0.00189844, 0.00058594, 14379023.59295028, 0.00152995)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.37037206775, 2022992, 0.37037206775, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 188.90796082, 0.00699946, 227.00111112, 0.06837645, 22.70011111, 0.29113823, -254.9558432, -0.00748238, -306.36750003, -0.07341854, -30.63675, -0.29618032, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 188.90796082, 0.00699946, 227.00111112, 0.0680162, 22.70011111, 0.28768892, -254.9558432, -0.00748238, -306.36750003, -0.07303153, -30.63675, -0.29270425, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 33795879.33703577, 0.125, 0.00260417, 0.00065104, 14081616.39043157, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.41269240819999997, 2122992, 0.41269240819999997, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 186.88049514, 0.00697154, 225.0618376, 0.06754167, 22.50618376, 0.28427469, -252.2160903, -0.00745652, -303.74607426, -0.07252589, -30.37460743, -0.28925892, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 186.88049514, 0.00697154, 225.0618376, 0.06787822, 22.50618376, 0.28747874, -252.2160903, -0.00745652, -303.74607426, -0.07288744, -30.37460743, -0.29248797, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 33216149.08969472, 0.125, 0.00260417, 0.00065104, 13840062.12070614, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.4109743348, 2222992, 0.4109743348, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 110.20282385, 0.00763165, 133.2957261, 0.06469201, 13.32957261, 0.2409101, -149.09778267, -0.00807612, -180.34108844, -0.06937501, -18.03410884, -0.2455931, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 110.20282385, 0.00763165, 133.2957261, 0.06438247, 13.32957261, 0.23834136, -149.09778267, -0.00807612, -180.34108844, -0.06904247, -18.03410884, -0.24300136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 32003463.56696683, 0.1125, 0.00189844, 0.00058594, 13334776.48623618, 0.00152995)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.37143267659, 2322992, 0.37143267659, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 63.32807411, 0.00713967, 76.59141973, 0.06130476, 7.65914197, 0.26268744, -94.57608771, -0.00754392, -114.38397475, -0.06704694, -11.43839747, -0.26842961, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 63.30465547, 0.00712031, 76.56309631, 0.06165126, 7.65630963, 0.26231411, -114.60981032, -0.00773421, -138.61353293, -0.0703746, -13.86135329, -0.27103745, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 32030092.38572825, 0.1125, 0.00189844, 0.00058594, 13345871.82738677, 0.00152995)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32811615111, 2003992, 0.32811615111, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 162.94846155, 0.00820669, 196.88188036, 0.07094138, 19.68818804, 0.28749078, -219.83859047, -0.00881728, -265.61916974, -0.076212, -26.56191697, -0.2927614, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 162.94846155, 0.00820669, 196.88188036, 0.07132477, 19.68818804, 0.29102651, -219.83859047, -0.00881728, -265.61916974, -0.07662386, -26.56191697, -0.29632561, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 32314447.15343896, 0.1125, 0.00189844, 0.00058594, 13464352.98059957, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.41239201554, 2103992, 0.41239201554, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 164.60684337, 0.00822412, 198.06363618, 0.06973099, 19.80636362, 0.28809904, -222.10523021, -0.00882513, -267.24872798, -0.07490083, -26.7248728, -0.29326887, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 164.60684337, 0.00822412, 198.06363618, 0.06942079, 19.80636362, 0.28518545, -222.10523021, -0.00882513, -267.24872798, -0.07456759, -26.7248728, -0.29033224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 33449015.10584269, 0.1125, 0.00189844, 0.00058594, 13937089.62743445, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.41400379132000004, 2203992, 0.41400379132000004, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 61.80165753, 0.00707839, 74.7713378, 0.06264298, 7.47713378, 0.2669756, -92.30175092, -0.00747787, -111.6721731, -0.0685183, -11.16721731, -0.27285092, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 61.77088513, 0.00706055, 74.73410751, 0.06232363, 7.47341075, 0.26013095, -111.84661084, -0.007667, -135.3187124, -0.07114841, -13.53187124, -0.26895572, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 31928308.26832617, 0.1125, 0.00189844, 0.00058594, 13303461.77846924, 0.00152995)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32596170372, 2303992, 0.32596170372, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 62.10343079, 0.00707316, 74.81495167, 0.05929258, 7.48149517, 0.25741433, -112.47513626, -0.00766821, -135.49689247, -0.06765332, -13.54968925, -0.26577507, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 62.10343079, 0.00707316, 74.81495167, 0.05987758, 7.48149517, 0.2633047, -112.47513626, -0.00766821, -135.49689247, -0.06832532, -13.54968925, -0.27175244, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 33132769.33155583, 0.1125, 0.00189844, 0.00058594, 13805320.55481493, 0.00152995)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.3265279409, 2013992, 0.3265279409, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 161.91532515, 0.00791112, 195.80368984, 0.07190932, 19.58036898, 0.29028951, -218.33193036, -0.00850668, -264.02811182, -0.07725877, -26.40281118, -0.29563896, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 161.91532515, 0.00791112, 195.80368984, 0.07277987, 19.58036898, 0.2982724, -218.33193036, -0.00850668, -264.02811182, -0.07819399, -26.40281118, -0.30368651, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 32064206.17467862, 0.1125, 0.00189844, 0.00058594, 13360085.90611609, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.40792309124000004, 2113992, 0.40792309124000004, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 162.92284412, 0.0079859, 197.26027388, 0.07425671, 19.72602739, 0.29855768, -219.6828076, -0.0085905, -265.98290146, -0.07978401, -26.59829015, -0.30408498, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 162.92284412, 0.0079859, 197.26027388, 0.07423027, 19.72602739, 0.298319, -219.6828076, -0.0085905, -265.98290146, -0.0797556, -26.59829015, -0.30384433, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 31708543.60623112, 0.1125, 0.00189844, 0.00058594, 13211893.16926297, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.40945236548999997, 2213992, 0.40945236548999997, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 62.60056909, 0.00716513, 75.50794459, 0.06151149, 7.55079446, 0.26474244, -113.36981174, -0.00777056, -136.74510612, -0.07019891, -13.67451061, -0.27342985, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 62.60056909, 0.00716513, 75.50794459, 0.06078875, 7.55079446, 0.25766697, -113.36981174, -0.00777056, -136.74510612, -0.06936868, -13.67451061, -0.2662469, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 32793066.51694505, 0.1125, 0.00189844, 0.00058594, 13663777.71539377, 0.00152995)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32780942482000003, 2313992, 0.32780942482000003, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 61.19253733, 0.00708798, 74.09959231, 0.06293875, 7.40995923, 0.26578534, -110.79839158, -0.00769687, -134.1685768, -0.07185336, -13.41685768, -0.27469995, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 61.22824161, 0.00710496, 74.14282752, 0.0624862, 7.41428275, 0.2652361, -91.44297023, -0.00750609, -110.73060718, -0.06834511, -11.07306072, -0.27109501, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 31667479.38082051, 0.1125, 0.00189844, 0.00058594, 13194783.07534188, 0.00152995)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32554066721999997, 2023992, 0.32554066721999997, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 163.39459979, 0.00793835, 196.95416678, 0.07178509, 19.69541668, 0.29436741, -220.35503071, -0.00852724, -265.61368323, -0.07711661, -26.56136832, -0.29969893, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 163.39459979, 0.00793835, 196.95416678, 0.07164587, 19.69541668, 0.29307863, -220.35503071, -0.00852724, -265.61368323, -0.07696705, -26.56136832, -0.29839981, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 32974041.82871037, 0.1125, 0.00189844, 0.00058594, 13739184.09529599, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.40947218282000003, 2123992, 0.40947218282000003, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 161.53730094, 0.00800255, 194.01774736, 0.06968105, 19.40177474, 0.28992794, -217.96055301, -0.00858391, -261.78607209, -0.07484397, -26.17860721, -0.29509087, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 161.53730094, 0.00800255, 194.01774736, 0.06964724, 19.40177474, 0.2896079, -217.96055301, -0.00858391, -261.78607209, -0.07480766, -26.17860721, -0.29476831, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 33919090.69314121, 0.1125, 0.00189844, 0.00058594, 14132954.45547551, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.40926794227, 2223992, 0.40926794227, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 62.2700705, 0.00712576, 75.08839933, 0.05972956, 7.50883993, 0.25815839, -112.77288018, -0.00772707, -135.98724062, -0.06815372, -13.59872406, -0.26658255, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 62.30335752, 0.00714262, 75.1285385, 0.05944677, 7.51285385, 0.25906949, -93.06295588, -0.007539, -112.22001738, -0.06499769, -11.22200174, -0.26462041, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 32869601.31606242, 0.1125, 0.00189844, 0.00058594, 13695667.21502601, 0.00152995)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32712807005000005, 2323992, 0.32712807005000005, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 62.21983889, 0.0071754, 75.02535689, 0.04909003, 7.50253569, 0.25249915, -62.21983889, -0.0071754, -75.02535689, -0.04909003, -7.50253569, -0.25249915, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 62.18388578, 0.00715729, 74.98200424, 0.04926475, 7.49820042, 0.25091976, -82.30364909, -0.00738864, -99.24263318, -0.05231179, -9.92426332, -0.2539668, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 32878628.80437917, 0.1125, 0.00189844, 0.00058594, 13699428.66849132, 0.00152995)
    ops.section('Aggregator', 2004991, 2004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2004992, 2004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.32702110245, 2004992, 0.32702110245, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 109.64922112, 0.00781982, 132.18493925, 0.06320612, 13.21849393, 0.23854774, -148.42027135, -0.00826411, -178.9244315, -0.06776459, -17.89244315, -0.24310621, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 109.64922112, 0.00781982, 132.18493925, 0.06305255, 13.21849393, 0.23724314, -148.42027135, -0.00826411, -178.9244315, -0.06759962, -17.89244315, -0.2417902, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 32943327.19052678, 0.1125, 0.00189844, 0.00058594, 13726386.32938616, 0.00152995)
    ops.section('Aggregator', 2104991, 2104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2104992, 2104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.37316031337, 2104992, 0.37316031337, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 106.03990737, 0.00752596, 127.6315624, 0.06456501, 12.76315624, 0.24482484, -143.53899303, -0.007951, -172.76614437, -0.069227, -17.27661444, -0.24948682, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 106.03990737, 0.00752596, 127.6315624, 0.06453515, 12.76315624, 0.24457121, -143.53899303, -0.007951, -172.76614437, -0.06919492, -17.27661444, -0.24923098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 33368841.11680923, 0.1125, 0.00189844, 0.00058594, 13903683.79867052, 0.00152995)
    ops.section('Aggregator', 2204991, 2204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2204992, 2204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.36714169699000004, 2204992, 0.36714169699000004, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 60.37697071, 0.00700271, 72.99887441, 0.04986615, 7.29988744, 0.25304687, -60.37697071, -0.00700271, -72.99887441, -0.04986615, -7.29988744, -0.25304687, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 60.34091152, 0.00698468, 72.95527699, 0.05009589, 7.2955277, 0.25208594, -79.85976478, -0.0072132, -96.5545782, -0.05320722, -9.65545782, -0.25519727, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 32123005.8306136, 0.1125, 0.00189844, 0.00058594, 13384585.76275567, 0.00152995)
    ops.section('Aggregator', 2304991, 2304990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2304992, 2304991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.32351745477, 2304992, 0.32351745477, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 61.90421276, 0.00698566, 74.31600316, 0.04892025, 7.43160032, 0.25460941, -81.94129781, -0.00720851, -98.37052238, -0.05194723, -9.83705224, -0.25763639, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 61.90421276, 0.00698566, 74.31600316, 0.04830562, 7.43160032, 0.24691525, -81.94129781, -0.00720851, -98.37052238, -0.0512915, -9.83705224, -0.24990113, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 34039758.76693671, 0.1125, 0.00189844, 0.00058594, 14183232.81955696, 0.00152995)
    ops.section('Aggregator', 2014991, 2014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2014992, 2014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.32537545562000003, 2014992, 0.32537545562000003, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 107.3195673, 0.00758079, 129.74828869, 0.06422837, 12.97482887, 0.23925775, -145.23529526, -0.00801884, -175.58802642, -0.06887429, -17.55880264, -0.24390367, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 107.3195673, 0.00758079, 129.74828869, 0.06471644, 12.97482887, 0.24334418, -145.23529526, -0.00801884, -175.58802642, -0.06939861, -17.55880264, -0.24802635, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 32137733.80498045, 0.1125, 0.00189844, 0.00058594, 13390722.41874185, 0.00152995)
    ops.section('Aggregator', 2114991, 2114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2114992, 2114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.36857610205999997, 2114992, 0.36857610205999997, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 106.57502497, 0.00748862, 128.43480503, 0.06340161, 12.8434805, 0.2393384, -144.24303041, -0.00791518, -173.82895752, -0.06798148, -17.38289575, -0.24391826, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 106.57502497, 0.00748862, 128.43480503, 0.06409758, 12.8434805, 0.24527354, -144.24303041, -0.00791518, -173.82895752, -0.06872914, -17.38289575, -0.2499051, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 33036697.95449883, 0.1125, 0.00189844, 0.00058594, 13765290.81437452, 0.00152995)
    ops.section('Aggregator', 2214991, 2214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2214992, 2214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.36713052568, 2214992, 0.36713052568, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 61.96231525, 0.00695257, 74.99364539, 0.05089342, 7.49936454, 0.25565254, -82.00079509, -0.00718446, -99.24642944, -0.05406359, -9.92464294, -0.25882272, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 61.96231525, 0.00695257, 74.99364539, 0.05083442, 7.49936454, 0.254942, -82.00079509, -0.00718446, -99.24642944, -0.05400065, -9.92464294, -0.25810823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 31818535.2573746, 0.1125, 0.00189844, 0.00058594, 13257723.02390608, 0.00152995)
    ops.section('Aggregator', 2314991, 2314990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2314992, 2314991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.32493790581000004, 2314992, 0.32493790581000004, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 62.13237835, 0.00690294, 74.21259044, 0.04651353, 7.42125904, 0.24909911, -82.24938836, -0.00711977, -98.2408904, -0.0493791, -9.82408904, -0.25196468, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 62.15455868, 0.00692119, 74.23908323, 0.04608347, 7.42390832, 0.24716528, -62.15455868, -0.00692119, -74.23908323, -0.04608347, -7.42390832, -0.24716528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 35268898.33656744, 0.1125, 0.00189844, 0.00058594, 14695374.3069031, 0.00152995)
    ops.section('Aggregator', 2024991, 2024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2024992, 2024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.32501206242, 2024992, 0.32501206242, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 111.05648916, 0.00756318, 134.33036978, 0.06415719, 13.43303698, 0.23911169, -150.21435422, -0.00800568, -181.6944683, -0.06880357, -18.16944683, -0.24375808, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 111.05648916, 0.00756318, 134.33036978, 0.06444671, 13.43303698, 0.24153177, -150.21435422, -0.00800568, -181.6944683, -0.0691146, -18.16944683, -0.24619967, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 31998914.05441536, 0.1125, 0.00189844, 0.00058594, 13332880.8560064, 0.00152995)
    ops.section('Aggregator', 2124991, 2124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2124992, 2124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.37135667496999997, 2124992, 0.37135667496999997, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 108.36071292, 0.00759056, 130.3427864, 0.06245065, 13.03427864, 0.23787959, -146.66791437, -0.00801962, -176.42099354, -0.06695479, -17.64209935, -0.24238373, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 108.36071292, 0.00759056, 130.3427864, 0.06316887, 13.03427864, 0.24409484, -146.66791437, -0.00801962, -176.42099354, -0.06772637, -17.64209935, -0.24865234, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 33534667.52893616, 0.1125, 0.00189844, 0.00058594, 13972778.13705673, 0.00152995)
    ops.section('Aggregator', 2224991, 2224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2224992, 2224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.36975884271000004, 2224992, 0.36975884271000004, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 63.56400725, 0.00731105, 76.65544381, 0.04739183, 7.66554438, 0.24487505, -84.13028108, -0.00754759, -101.45748063, -0.05030854, -10.14574806, -0.24779176, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 63.60034055, 0.00732967, 76.6992602, 0.04745268, 7.66992602, 0.24933823, -63.60034055, -0.00732967, -76.6992602, -0.04745268, -7.66992602, -0.24933823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 32845431.31210937, 0.1125, 0.00189844, 0.00058594, 13685596.38004557, 0.00152995)
    ops.section('Aggregator', 2324991, 2324990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2324992, 2324991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.32979436941, 2324992, 0.32979436941, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)
