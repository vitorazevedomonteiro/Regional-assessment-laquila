import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.54465683, 0.00949924, 38.53009701, 0.07165695, 3.8530097, 0.31009383, -54.76057868, -0.01033728, -66.88709344, -0.08108581, -6.68870934, -0.31952269, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 46.72013068, 0.00984615, 57.06611986, 0.07439867, 5.70661199, 0.31340906, -80.90308093, -0.01093668, -98.81874998, -0.08441102, -9.881875, -0.3234214, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 28786154.73619708, 0.07, 0.00071458, 0.00023333, 11994231.14008212, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32708952436, 1001992, 0.32708952436, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 45.3561869, 0.00991099, 55.15155951, 0.09285055, 5.51515595, 0.40466341, -78.58815322, -0.01096135, -95.56048479, -0.105364, -9.55604848, -0.41717686, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 45.3561869, 0.00991099, 55.15155951, 0.0925702, 5.51515595, 0.40188871, -78.58815322, -0.01096135, -95.56048479, -0.1050449, -9.55604848, -0.41436341, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 30363464.05095609, 0.07, 0.00071458, 0.00023333, 12651443.35456504, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25764665921, 1101992, 0.25764665921, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 45.77874117, 0.00995432, 56.00016433, 0.07744641, 5.60001643, 0.32226559, -79.28691829, -0.0110595, -96.99000759, -0.08787967, -9.69900076, -0.33269886, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.94882834, 0.00959466, 37.85904611, 0.07414101, 3.78590461, 0.31445213, -53.70818241, -0.01044271, -65.70008182, -0.08391002, -6.57000818, -0.32422113, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28212610.26488823, 0.07, 0.00071458, 0.00023333, 11755254.27703676, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32630087334, 1201992, 0.32630087334, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.12091245, 0.00783878, 44.13313024, 0.09063623, 4.41331302, 0.37216828, -146.85962159, -0.00987303, -179.4355227, -0.1250746, -17.94355227, -0.40660665, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 71.02799537, 0.00834265, 86.78318341, 0.09293657, 8.67831834, 0.37642686, -146.95727013, -0.00976463, -179.5548313, -0.11046912, -17.95548313, -0.39395941, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28672280.18903435, 0.1, 0.00133333, 0.00052083, 11946783.41209765, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32558012615000004, 1011992, 0.32558012615000004, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 70.18883241, 0.00853706, 86.03021094, 0.11795511, 8.60302109, 0.47585789, -145.23934907, -0.01001746, -178.01937157, -0.14027374, -17.80193716, -0.49817652, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 70.18883241, 0.00853706, 86.03021094, 0.11686732, 8.60302109, 0.46638738, -145.23934907, -0.01001746, -178.01937157, -0.13897878, -17.80193716, -0.48849885, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27413132.48621549, 0.1, 0.00133333, 0.00052083, 11422138.53592312, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25801727393, 1111992, 0.25801727393, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 71.38173498, 0.00858532, 87.50698108, 0.09439199, 8.75069811, 0.37569016, -147.67068019, -0.01008042, -181.02971889, -0.11222862, -18.10297189, -0.3935268, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 36.34288902, 0.00805858, 44.55280476, 0.09157242, 4.45528048, 0.3672286, -147.61584656, -0.01019565, -180.96249826, -0.12639399, -18.09624983, -0.40205017, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 27342872.43759632, 0.1, 0.00133333, 0.00052083, 11392863.51566513, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32747962385, 1211992, 0.32747962385, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 62.31587378, 0.00879395, 76.28623473, 0.09082683, 7.62862347, 0.36093221, -145.3290169, -0.01058894, -177.90978161, -0.11086724, -17.79097816, -0.38097262, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 92.38969446, 0.00926851, 113.10219194, 0.09257295, 11.31021919, 0.36267833, -145.37917492, -0.01046353, -177.97118437, -0.10341721, -17.79711844, -0.37352259, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 27918613.70357693, 0.08, 0.00106667, 0.00026667, 11632755.70982372, 0.00073242)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.37022587305000004, 1021992, 0.37022587305000004, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 92.67869147, 0.00923853, 113.04655524, 0.1081886, 11.30465552, 0.43875054, -145.89200671, -0.0103992, -177.95448484, -0.12081077, -17.79544848, -0.45137271, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 92.67869147, 0.00923853, 113.04655524, 0.10968837, 11.30465552, 0.44025031, -145.89200671, -0.0103992, -177.95448484, -0.12248426, -17.79544848, -0.45304621, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29289411.18736686, 0.08, 0.00106667, 0.00026667, 12203921.32806952, 0.00073242)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.30251516107, 1121992, 0.30251516107, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 92.55671797, 0.0091346, 112.98897015, 0.09058793, 11.29889702, 0.36127988, -145.65377412, -0.01029131, -177.80740607, -0.10117947, -17.78074061, -0.37187142, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 62.41267377, 0.00867361, 76.19051203, 0.08941651, 7.6190512, 0.36010847, -145.58512929, -0.01041099, -177.72360763, -0.1091124, -17.77236076, -0.37980436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 28996211.07687022, 0.08, 0.00106667, 0.00026667, 12081754.61536259, 0.00073242)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.369423619, 1221992, 0.369423619, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 31.117598, 0.00967488, 38.07649352, 0.07420846, 3.80764935, 0.31745587, -53.99827704, -0.0105312, -66.07402815, -0.08398398, -6.60740282, -0.3272314, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 31.04940708, 0.00962028, 37.99305293, 0.07512514, 3.79930529, 0.31345601, -79.71981098, -0.01123541, -97.54772419, -0.09291556, -9.75477242, -0.33124642, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 28098957.2328474, 0.07, 0.00071458, 0.00023333, 11707898.84701975, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32714481993, 1031992, 0.32714481993, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 30.81448429, 0.00969425, 37.69921108, 0.09115416, 3.76992111, 0.39289399, -79.08826812, -0.0113096, -96.75856607, -0.11288461, -9.67585661, -0.41462444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 30.81448429, 0.00969425, 37.69921108, 0.09166876, 3.76992111, 0.39794976, -79.08826812, -0.0113096, -96.75856607, -0.11352628, -9.67585661, -0.41980728, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 28165708.86232103, 0.07, 0.00071458, 0.00023333, 11735712.0259671, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25902559591, 1131992, 0.25902559591, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 31.57927627, 0.00955538, 38.63559261, 0.07539292, 3.86355926, 0.318459, -81.0998531, -0.011172, -99.22142793, -0.09326698, -9.92214279, -0.33633306, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 31.64154314, 0.00961706, 38.71177285, 0.07358541, 3.87117729, 0.31364026, -54.92096131, -0.01047395, -67.19292324, -0.08328337, -6.71929232, -0.32333823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 28158420.92461554, 0.07, 0.00071458, 0.00023333, 11732675.38525648, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32796330274, 1231992, 0.32796330274, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 30.61690875, 0.00982857, 37.37535498, 0.07258159, 3.7375355, 0.31341102, -53.08596054, -0.01067227, -64.80427647, -0.08209838, -6.48042765, -0.32292782, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 30.54941353, 0.00978886, 37.29296071, 0.07442635, 3.72929607, 0.3187319, -78.34714213, -0.01137763, -95.64166887, -0.09197622, -9.56416689, -0.33628177, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28999694.3120252, 0.07, 0.00071458, 0.00023333, 12083205.96334383, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32695122076, 1002992, 0.32695122076, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 30.71099356, 0.00952585, 37.57596118, 0.09360219, 3.75759612, 0.40216232, -78.84971855, -0.0111233, -96.47535361, -0.11596083, -9.64753536, -0.42452097, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 30.71099356, 0.00952585, 37.57596118, 0.09363948, 3.75759612, 0.4025243, -78.84971855, -0.0111233, -96.47535361, -0.11600733, -9.64753536, -0.42489215, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28130461.76960126, 0.07, 0.00071458, 0.00023333, 11721025.73733386, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25782129379999996, 1102992, 0.25782129379999996, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 30.86646322, 0.00960657, 37.65809851, 0.07332459, 3.76580985, 0.31323574, -79.25196736, -0.01117708, -96.6900021, -0.09062916, -9.66900021, -0.33054031, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 30.93414052, 0.00965451, 37.74066703, 0.07208027, 3.7740667, 0.31373757, -53.678582, -0.01048831, -65.48963236, -0.08154194, -6.54896324, -0.32319924, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29211422.5775739, 0.07, 0.00071458, 0.00023333, 12171426.07398912, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32670527233, 1202992, 0.32670527233, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 64.96920159, 0.00883234, 79.34110688, 0.0881772, 7.93411069, 0.35516757, -151.45903985, -0.01061815, -184.96345307, -0.10761059, -18.49634531, -0.37460095, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 64.96920159, 0.00883234, 79.34110688, 0.08761588, 7.93411069, 0.35460625, -151.45903985, -0.01061815, -184.96345307, -0.10692442, -18.49634531, -0.37391478, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 28857859.12334376, 0.08, 0.00106667, 0.00026667, 12024107.9680599, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.37454534826999997, 1012992, 0.37454534826999997, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 64.05978425, 0.00852573, 78.19472713, 0.10581969, 7.81947271, 0.43650367, -149.2484022, -0.0102538, -182.18041509, -0.12918749, -18.21804151, -0.45987147, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 64.05978425, 0.00852573, 78.19472713, 0.10714898, 7.81947271, 0.43783296, -149.2484022, -0.0102538, -182.18041509, -0.13081244, -18.21804151, -0.46149642, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29026721.54085275, 0.08, 0.00106667, 0.00026667, 12094467.30868865, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30240352198, 1112992, 0.30240352198, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 62.92947389, 0.00875289, 77.02355647, 0.09121288, 7.70235565, 0.36092496, -146.72424352, -0.01054429, -179.58553216, -0.11134469, -17.95855322, -0.38105677, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 62.92947389, 0.00875289, 77.02355647, 0.09098316, 7.70235565, 0.36069524, -146.72424352, -0.01054429, -179.58553216, -0.11106388, -17.95855322, -0.38077596, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 27990507.22631983, 0.08, 0.00106667, 0.00026667, 11662711.34429993, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.37076574661, 1212992, 0.37076574661, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 62.66073569, 0.00847851, 76.72514003, 0.09073649, 7.672514, 0.36260238, -145.96927892, -0.01023368, -178.73255463, -0.11078714, -17.87325546, -0.38265304, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 62.66073569, 0.00847851, 76.72514003, 0.09081282, 7.672514, 0.36267871, -145.96927892, -0.01023368, -178.73255463, -0.11088045, -17.87325546, -0.38274634, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 27830761.2785826, 0.08, 0.00106667, 0.00026667, 11596150.53274275, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36782840974, 1022992, 0.36782840974, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 61.78450969, 0.00865435, 75.38941645, 0.10911995, 7.53894164, 0.44206672, -144.14828515, -0.01037772, -175.88963891, -0.13318847, -17.58896389, -0.46613525, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 61.78450969, 0.00865435, 75.38941645, 0.10879827, 7.53894164, 0.44174504, -144.14828515, -0.01037772, -175.88963891, -0.13279524, -17.58896389, -0.46574202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29162047.31121989, 0.08, 0.00106667, 0.00026667, 12150853.04634162, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30034830834000004, 1122992, 0.30034830834000004, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 61.57254553, 0.00863252, 75.16696113, 0.09139642, 7.51669611, 0.36326827, -143.64545077, -0.0103575, -175.36049424, -0.11152941, -17.53604942, -0.38340127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 61.57254553, 0.00863252, 75.16696113, 0.09123129, 7.51669611, 0.36310314, -143.64545077, -0.0103575, -175.36049424, -0.11132756, -17.53604942, -0.38319941, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 28986240.47679629, 0.08, 0.00106667, 0.00026667, 12077600.19866512, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36782035332, 1222992, 0.36782035332, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 30.57772848, 0.00946218, 37.37315195, 0.07301534, 3.73731519, 0.31389209, -53.06690051, -0.01029328, -64.86019187, -0.08263013, -6.48601919, -0.32350688, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 30.51185813, 0.00940928, 37.29264293, 0.07411447, 3.72926429, 0.31182282, -78.35176413, -0.01097614, -95.76422224, -0.09165914, -9.57642222, -0.32936749, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 28542635.45297733, 0.07, 0.00071458, 0.00023333, 11892764.77207389, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32471177681, 1032992, 0.32471177681, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 30.09536165, 0.00956326, 36.72926839, 0.09095191, 3.67292684, 0.39524663, -77.21316041, -0.01111757, -94.23322189, -0.11260374, -9.42332219, -0.41689845, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 30.09536165, 0.00956326, 36.72926839, 0.09166861, 3.67292684, 0.40235798, -77.21316041, -0.01111757, -94.23322189, -0.11349741, -9.42332219, -0.42418678, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 29093456.40455056, 0.07, 0.00071458, 0.00023333, 12122273.50189606, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25663308168, 1132992, 0.25663308168, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 31.4657653, 0.00963191, 38.66093214, 0.07747399, 3.86609321, 0.32097921, -80.76213402, -0.01132436, -99.22972962, -0.09591886, -9.92297296, -0.33942408, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 31.53006048, 0.00969939, 38.73992948, 0.07557865, 3.87399295, 0.31574959, -54.70840065, -0.01059475, -67.21837988, -0.08557918, -6.72183799, -0.32575012, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 26352374.67108082, 0.07, 0.00071458, 0.00023333, 10980156.11295034, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32803475862, 1232992, 0.32803475862, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 31.48512261, 0.00944345, 38.39319536, 0.05890759, 3.83931954, 0.30457358, -31.48512261, -0.00944345, -38.39319536, -0.05890759, -3.83931954, -0.30457358, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 31.44977812, 0.00940283, 38.35009603, 0.05906304, 3.8350096, 0.29937522, -46.64862654, -0.00989344, -56.88368613, -0.06429723, -5.68836861, -0.3046094, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 29395215.39498419, 0.07, 0.00071458, 0.00023333, 12248006.41457675, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32617385804000004, 1003992, 0.32617385804000004, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 30.85073812, 0.00977209, 37.69859987, 0.07101805, 3.76985999, 0.37253046, -45.72589807, -0.01027748, -55.87556213, -0.07737368, -5.58755621, -0.3788861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 30.85073812, 0.00977209, 37.69859987, 0.07138752, 3.76985999, 0.37723245, -45.72589807, -0.01027748, -55.87556213, -0.07777845, -5.58755621, -0.38362338, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 28625603.02650338, 0.07, 0.00071458, 0.00023333, 11927334.59437641, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25900078967, 1103992, 0.25900078967, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 30.79536919, 0.00964766, 37.64381596, 0.05966736, 3.7643816, 0.30251518, -45.65395197, -0.01015066, -55.80673365, -0.06494827, -5.58067336, -0.30779609, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 30.84040731, 0.00968157, 37.69886991, 0.05897414, 3.76988699, 0.30101769, -30.84040731, -0.00968157, -37.69886991, -0.05897414, -3.76988699, -0.30101769, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 28495392.21011891, 0.07, 0.00071458, 0.00023333, 11873080.08754955, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32613592633000005, 1203992, 0.32613592633000005, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 35.47192828, 0.00814603, 43.25490991, 0.09988574, 4.32549099, 0.40646603, -143.74327076, -0.01049091, -175.28232965, -0.13813444, -17.52823297, -0.44471473, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 35.47192828, 0.00814603, 43.25490991, 0.09848982, 4.32549099, 0.40507011, -143.74327076, -0.01049091, -175.28232965, -0.1361922, -17.52823297, -0.44277249, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29393786.01699719, 0.08, 0.00106667, 0.00026667, 12247410.8404155, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32617883223, 1013992, 0.32617883223, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 35.85139748, 0.00800337, 43.90849221, 0.12621147, 4.39084922, 0.51389466, -145.22131973, -0.01041672, -177.85775826, -0.17488748, -17.78577583, -0.56257067, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 35.85139748, 0.00800337, 43.90849221, 0.1257958, 4.39084922, 0.51347899, -145.22131973, -0.01041672, -177.85775826, -0.17430913, -17.78577583, -0.56199232, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 27737073.11571349, 0.08, 0.00106667, 0.00026667, 11557113.79821396, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25794257562, 1113992, 0.25794257562, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 36.12186866, 0.00794734, 44.03853463, 0.09588004, 4.40385346, 0.4024915, -146.4443787, -0.01026579, -178.53992838, -0.13261237, -17.85399284, -0.43922384, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 36.12186866, 0.00794734, 44.03853463, 0.09737553, 4.40385346, 0.40398699, -146.4443787, -0.01026579, -178.53992838, -0.13469315, -17.85399284, -0.44130461, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 29465673.55481861, 0.08, 0.00106667, 0.00026667, 12277363.98117442, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32614566702000003, 1213992, 0.32614566702000003, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 52.37916425, 0.01016625, 63.95167314, 0.0937343, 6.39516731, 0.36615306, -121.81891232, -0.0123689, -148.7332487, -0.11452383, -14.87332487, -0.38694259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 52.37916425, 0.01016625, 63.95167314, 0.09378402, 6.39516731, 0.36620278, -121.81891232, -0.0123689, -148.7332487, -0.11458461, -14.87332487, -0.38700336, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 28940890.45805052, 0.07, 0.00071458, 0.00023333, 12058704.35752105, 0.00060032)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36708191611, 1023992, 0.36708191611, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 53.68543823, 0.01030737, 65.28972182, 0.11012676, 6.52897218, 0.44063758, -124.90257343, -0.01248439, -151.90067444, -0.13450521, -15.19006744, -0.46501603, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 53.68543823, 0.01030737, 65.28972182, 0.10880397, 6.52897218, 0.43931479, -124.90257343, -0.01248439, -151.90067444, -0.13288821, -15.19006744, -0.46339903, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 30312416.03368935, 0.07, 0.00071458, 0.00023333, 12630173.34737056, 0.00060032)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30256195756, 1123992, 0.30256195756, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 51.91325528, 0.01036369, 63.64831998, 0.09702264, 6.364832, 0.3691232, -120.68360371, -0.01267345, -147.96430284, -0.11860673, -14.79643028, -0.39070729, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 51.91325528, 0.01036369, 63.64831998, 0.09708849, 6.364832, 0.36918906, -120.68360371, -0.01267345, -147.96430284, -0.11868723, -14.79643028, -0.39078779, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 27291257.80602365, 0.07, 0.00071458, 0.00023333, 11371357.41917652, 0.00060032)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36751118064000005, 1223992, 0.36751118064000005, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 30.82064408, 0.00993775, 37.58256504, 0.05763878, 3.7582565, 0.29819051, -30.82064408, -0.00993775, -37.58256504, -0.05763878, -3.7582565, -0.29819051, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 30.77655387, 0.00991269, 37.52880162, 0.05859334, 3.75288016, 0.30322118, -45.59254914, -0.01041247, -55.59536455, -0.06374313, -5.55953646, -0.30837097, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 29398626.00686525, 0.07, 0.00071458, 0.00023333, 12249427.50286052, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32769780249, 1033992, 0.32769780249, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 30.6862926, 0.00966466, 37.34940583, 0.07006496, 3.73494058, 0.3735859, -45.48374903, -0.01015031, -55.3599297, -0.07632009, -5.53599297, -0.37984102, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 30.6862926, 0.00966466, 37.34940583, 0.0706146, 3.73494058, 0.38072818, -45.48374903, -0.01015031, -55.3599297, -0.07692222, -5.53599297, -0.38703581, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 30041902.91628745, 0.07, 0.00071458, 0.00023333, 12517459.54845311, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25812447521000004, 1133992, 0.25812447521000004, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 31.37237108, 0.00987321, 38.13859522, 0.05586703, 3.81385952, 0.29237017, -46.50013877, -0.01036526, -56.52903842, -0.06075243, -5.65290384, -0.29725557, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 31.41652741, 0.00990062, 38.19227494, 0.0555511, 3.81922749, 0.2953034, -31.41652741, -0.00990062, -38.19227494, -0.0555511, -3.81922749, -0.2953034, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 30442177.96217564, 0.07, 0.00071458, 0.00023333, 12684240.81757318, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32893391207, 1233992, 0.32893391207, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 44.65761577, 0.009919, 54.55183067, 0.12652101, 5.45518307, 0.51510457, -121.47682329, -0.01247987, -148.39088428, -0.16057028, -14.83908843, -0.54915384, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 44.65761577, 0.009919, 54.55183067, 0.12731579, 5.45518307, 0.51589935, -121.47682329, -0.01247987, -148.39088428, -0.16157969, -14.83908843, -0.55016325, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 28752116.5593915, 0.07, 0.00071458, 0.00023333, 11980048.56641313, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25734490619, 6200992, 0.25734490619, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 45.68634699, 0.00991863, 55.94482801, 0.1275402, 5.5944828, 0.51384174, -124.19983567, -0.01254924, -152.08785345, -0.16193455, -15.20878535, -0.5482361, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 45.68634699, 0.00991863, 55.94482801, 0.12798609, 5.5944828, 0.51428764, -124.19983567, -0.01254924, -152.08785345, -0.16250085, -15.20878535, -0.5488024, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 27801576.25830773, 0.07, 0.00071458, 0.00023333, 11583990.10762822, 0.00060032)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25886512891, 6201992, 0.25886512891, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 31.37903545, 0.00933556, 38.29266588, 0.09163445, 3.82926659, 0.3993632, -80.60832168, -0.01089141, -98.36846434, -0.11351257, -9.83684643, -0.42124132, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 31.37903545, 0.00933556, 38.29266588, 0.09174366, 3.82926659, 0.40044197, -80.60832168, -0.01089141, -98.36846434, -0.11364875, -9.83684643, -0.42234706, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 29124225.17028561, 0.07, 0.00071458, 0.00023333, 12135093.82095234, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25825055957000004, 6202992, 0.25825055957000004, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 63.25249279, 0.00852311, 77.36397283, 0.08205171, 7.73639728, 0.32795322, -147.8253407, -0.01004966, -180.80482108, -0.0999322, -18.08048211, -0.34583371, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 93.66430717, 0.00881492, 114.56059035, 0.08669484, 11.45605904, 0.333046, -217.89990391, -0.01081353, -266.51285194, -0.10601519, -26.65128519, -0.35236635, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28270496.31149949, 0.1, 0.00133333, 0.00052083, 11779373.46312479, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.3699558441, 2001992, 0.3699558441, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 128.0095485, 0.00673769, 155.99195811, 0.06986895, 15.59919581, 0.28815415, -195.66797305, -0.00730793, -238.44026177, -0.07710769, -23.84402618, -0.2953929, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 128.04511202, 0.00665193, 156.03529568, 0.07162296, 15.60352957, 0.28812025, -288.82199876, -0.007854, -351.95740987, -0.08654948, -35.19574099, -0.30304678, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29629873.91718344, 0.125, 0.00260417, 0.00065104, 12345780.79882644, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41292825405000005, 2101992, 0.41292825405000005, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 127.7326167, 0.00674777, 155.90836626, 0.07243676, 15.59083663, 0.29666317, -195.22141642, -0.00732497, -238.28410378, -0.07995265, -23.82841038, -0.30417905, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 127.77012758, 0.00666022, 155.95415143, 0.07371453, 15.59541514, 0.29184422, -288.13952728, -0.00787762, -351.69844723, -0.08909645, -35.16984472, -0.30722614, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29047284.80459386, 0.125, 0.00260417, 0.00065104, 12103035.33524744, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41270996589, 2201992, 0.41270996589, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 63.70909553, 0.00834232, 78.00560595, 0.08141455, 7.80056059, 0.32398546, -148.79280306, -0.0098634, -182.18235037, -0.09918806, -18.21823504, -0.34175896, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 94.50047881, 0.00862017, 115.70666716, 0.08664483, 11.57066672, 0.33436367, -219.49728869, -0.01060953, -268.75313275, -0.10598812, -26.87531327, -0.35370696, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 27847345.08408022, 0.1, 0.00133333, 0.00052083, 11603060.45170009, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36887228726000004, 2301992, 0.36887228726000004, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 88.70659674, 0.00939122, 108.48808719, 0.08753095, 10.84880872, 0.33441978, -206.59148873, -0.01144599, -252.66120293, -0.10696525, -25.26612029, -0.35385407, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 60.12439199, 0.00899876, 73.53207675, 0.08527051, 7.35320768, 0.32768313, -206.76625627, -0.01155016, -252.87494348, -0.11369191, -25.28749435, -0.35610453, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 28301856.40325732, 0.1, 0.00133333, 0.00052083, 11792440.16802388, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36973308067, 2011992, 0.36973308067, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 126.61016277, 0.00663085, 154.47790444, 0.07304329, 15.44779044, 0.2930562, -285.62015233, -0.00783744, -348.48705375, -0.08827881, -34.84870538, -0.30829173, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 126.58437728, 0.00655896, 154.44644339, 0.07495661, 15.44464434, 0.29354495, -375.83481063, -0.00833302, -458.55856033, -0.09671881, -45.85585603, -0.31530715, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29189546.13987458, 0.125, 0.00260417, 0.00065104, 12162310.89161441, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41129301987000005, 2111992, 0.41129301987000005, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 125.91416335, 0.00678377, 154.18220094, 0.07526303, 15.41822009, 0.29709128, -284.17623831, -0.00804527, -347.97449876, -0.09099005, -34.79744988, -0.3128183, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 125.83529755, 0.00671072, 154.08562958, 0.07706055, 15.40856296, 0.29614693, -373.87892817, -0.0085669, -457.81566186, -0.09947536, -45.78156619, -0.31856174, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 27814497.68515523, 0.125, 0.00260417, 0.00065104, 11589374.03548135, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.41277211377, 2211992, 0.41277211377, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 94.2329251, 0.00886355, 114.88634142, 0.08384442, 11.48863414, 0.32646846, -219.36724558, -0.01082268, -267.44686368, -0.1024805, -26.74468637, -0.34510454, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 63.48817818, 0.00849093, 77.40314234, 0.08277538, 7.74031423, 0.32955025, -219.1451443, -0.01093383, -267.17608355, -0.11041421, -26.71760836, -0.35718908, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29463165.98648141, 0.1, 0.00133333, 0.00052083, 12276319.16103392, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.37111013634, 2311992, 0.37111013634, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 61.83301234, 0.00856659, 75.52069626, 0.08333916, 7.55206963, 0.32579039, -213.38445851, -0.0110372, -260.62037524, -0.11117128, -26.06203752, -0.3536225, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 62.0227216, 0.00863799, 75.75240057, 0.08117657, 7.57524006, 0.32939373, -144.96111876, -0.01015128, -177.05048169, -0.09882361, -17.70504817, -0.34704076, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 28810839.40998701, 0.1, 0.00133333, 0.00052083, 12004516.42082792, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.36919838773999997, 2021992, 0.36919838773999997, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 123.29638207, 0.00655791, 150.4017632, 0.07670441, 15.04017632, 0.30099888, -366.70876737, -0.00831427, -447.32573873, -0.09895998, -44.73257387, -0.32325445, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 123.4612436, 0.00670481, 150.60286775, 0.07221135, 15.06028678, 0.29436102, -188.82344039, -0.00727132, -230.33423925, -0.07969727, -23.03342393, -0.30184694, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29268605.87198143, 0.125, 0.00260417, 0.00065104, 12195252.44665893, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.40843547619, 2121992, 0.40843547619, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 124.41062274, 0.00678148, 152.17778825, 0.07768732, 15.21777883, 0.30149607, -370.2292191, -0.00862604, -452.86055536, -0.10025299, -45.28605554, -0.32406174, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 124.67641999, 0.00693136, 152.50290869, 0.07267945, 15.25029087, 0.29065318, -190.70019866, -0.00752549, -233.26251257, -0.0802185, -23.32625126, -0.29819223, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 28241122.51289357, 0.125, 0.00260417, 0.00065104, 11767134.38037232, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.41263743905, 2221992, 0.41263743905, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 62.37762328, 0.00847707, 76.28822062, 0.08589288, 7.62882206, 0.33426737, -215.22831516, -0.01096693, -263.22556594, -0.11464078, -26.32255659, -0.36301527, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 62.55462202, 0.00855713, 76.50469118, 0.08199941, 7.65046912, 0.32314579, -146.20477226, -0.01008159, -178.80934436, -0.0998586, -17.88093444, -0.34100498, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 28299593.09188689, 0.1, 0.00133333, 0.00052083, 11791497.12161954, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.36923900933, 2321992, 0.36923900933, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 36.05463882, 0.00786344, 44.04145025, 0.08799577, 4.40414503, 0.36152939, -146.58076109, -0.00989643, -179.05128184, -0.12138985, -17.90512818, -0.39492347, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 70.74689719, 0.00826732, 86.41872599, 0.09341089, 8.6418726, 0.36816421, -216.00250058, -0.01063512, -263.85130164, -0.12167579, -26.38513016, -0.39642911, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 28763617.34318017, 0.1, 0.00133333, 0.00052083, 11984840.5596584, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32561972937, 2002992, 0.32561972937, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 81.34909173, 0.0064474, 99.26700292, 0.07693723, 9.92670029, 0.32153439, -191.03139598, -0.00744175, -233.10787789, -0.09360963, -23.31078779, -0.3382068, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 81.21974185, 0.00638893, 99.10916249, 0.07974865, 9.91091625, 0.32886273, -281.631131, -0.00801457, -343.66306627, -0.10625657, -34.36630663, -0.35537066, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29144148.35585026, 0.125, 0.00260417, 0.00065104, 12143395.14827094, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36898906190999997, 2102992, 0.36898906190999997, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 79.69139277, 0.00647025, 97.11892811, 0.07775439, 9.71189281, 0.32634707, -187.23717061, -0.00745092, -228.18365549, -0.09458979, -22.81836555, -0.34318247, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 79.5249159, 0.0064192, 96.91604479, 0.08000631, 9.69160448, 0.32836516, -276.03062515, -0.00802188, -336.39515523, -0.10656839, -33.63951552, -0.35492725, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29603606.92684602, 0.125, 0.00260417, 0.00065104, 12334836.21951918, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36746964375, 2202992, 0.36746964375, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 36.63871039, 0.00801377, 44.63711628, 0.0864047, 4.46371163, 0.35984263, -148.98790269, -0.01004234, -181.51267515, -0.11911284, -18.15126752, -0.39255077, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 71.8401469, 0.0084233, 87.52319491, 0.09213967, 8.75231949, 0.37011779, -219.51505518, -0.01078542, -267.43624269, -0.11996479, -26.74362427, -0.39794291, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29713173.77898292, 0.1, 0.00133333, 0.00052083, 12380489.07457622, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32783207785, 2302992, 0.32783207785, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 68.63747478, 0.00867911, 83.84186604, 0.09605769, 8.3841866, 0.37708357, -209.86084847, -0.01110755, -256.34866669, -0.12506303, -25.63486667, -0.40608891, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 68.63747478, 0.00867911, 83.84186604, 0.09646778, 8.3841866, 0.38063233, -209.86084847, -0.01110755, -256.34866669, -0.12559785, -25.63486667, -0.4097624, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28764327.32138525, 0.1, 0.00133333, 0.00052083, 11985136.38391052, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32628967314, 2012992, 0.32628967314, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 80.69609853, 0.0063176, 98.96863038, 0.0814917, 9.89686304, 0.32535765, -279.32787699, -0.00800159, -342.57786828, -0.10867338, -34.25778683, -0.35253933, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 119.9929526, 0.00650874, 147.16372155, 0.08607154, 14.71637216, 0.33659892, -368.23123882, -0.00844546, -451.61218489, -0.11220793, -45.16121849, -0.36273531, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 27157628.31941515, 0.125, 0.00260417, 0.00065104, 11315678.46642298, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36734053042, 2112992, 0.36734053042, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 80.28688511, 0.00648991, 97.92860308, 0.07985089, 9.79286031, 0.32691317, -278.63704275, -0.00812014, -339.86293434, -0.10636383, -33.98629343, -0.35342612, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 119.13278514, 0.00668852, 145.31024854, 0.08339556, 14.53102485, 0.33000265, -367.0216873, -0.00856518, -447.66864586, -0.10860329, -44.76686459, -0.35521037, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29299728.04238404, 0.125, 0.00260417, 0.00065104, 12208220.01766002, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36916098191999996, 2212992, 0.36916098191999996, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 72.20866939, 0.00833447, 87.79403798, 0.09285534, 8.7794038, 0.37382469, -220.61213027, -0.01064925, -268.22859232, -0.12087783, -26.82285923, -0.40184718, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 72.20866939, 0.00833447, 87.79403798, 0.09235254, 8.7794038, 0.36937324, -220.61213027, -0.01064925, -268.22859232, -0.1202221, -26.82285923, -0.39724279, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 30398048.92395538, 0.1, 0.00133333, 0.00052083, 12665853.71831474, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32759949554, 2312992, 0.32759949554, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 71.69524014, 0.00842449, 87.53611373, 0.09509114, 8.75361137, 0.37547152, -218.97316644, -0.01082454, -267.3547081, -0.12385155, -26.73547081, -0.40423194, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 36.55918278, 0.00801237, 44.63683747, 0.08973112, 4.46368375, 0.3701103, -148.62131919, -0.0100725, -181.45880638, -0.1237732, -18.14588064, -0.40415238, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 28937838.1162796, 0.1, 0.00133333, 0.00052083, 12057432.54844983, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.3276450965, 2022992, 0.3276450965, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 121.20667004, 0.00645353, 148.02281038, 0.08331575, 14.80228104, 0.32833698, -372.06024516, -0.00831136, -454.37601, -0.10855184, -45.437601, -0.35357307, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 81.56551527, 0.00633098, 99.61132334, 0.07731705, 9.96113233, 0.32120216, -191.40016381, -0.00731991, -233.74613083, -0.09409442, -23.37461308, -0.33797953, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 28848101.88136485, 0.125, 0.00260417, 0.00065104, 12020042.45056869, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.36772555895, 2122992, 0.36772555895, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 118.63503809, 0.00632446, 145.22673783, 0.08658645, 14.52267378, 0.33679885, -363.87757304, -0.00818218, -445.43967577, -0.1128565, -44.54396758, -0.3630689, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 79.81680796, 0.00620625, 97.70751399, 0.07990461, 9.7707514, 0.32556258, -187.20925579, -0.00719415, -229.17166756, -0.0972842, -22.91716676, -0.34294217, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 27931437.32241324, 0.125, 0.00260417, 0.00065104, 11638098.88433885, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36415116941000003, 2222992, 0.36415116941000003, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 71.21033982, 0.00805775, 86.82263172, 0.09624416, 8.68226317, 0.38208129, -217.19618139, -0.01035277, -264.81469005, -0.12536179, -26.481469, -0.41119891, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 36.20212666, 0.00767148, 44.13915056, 0.08967405, 4.41391506, 0.36622811, -147.26717348, -0.00964663, -179.55431191, -0.12374224, -17.95543119, -0.4002963, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 29443457.98846724, 0.1, 0.00133333, 0.00052083, 12268107.49519468, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32458508731, 2322992, 0.32458508731, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 36.85761179, 0.00810494, 45.04000092, 0.09605411, 4.50400009, 0.40032934, -149.34876998, -0.01051355, -182.50419415, -0.13288305, -18.25041941, -0.43715828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 36.85761179, 0.00810494, 45.04000092, 0.09609232, 4.50400009, 0.40036755, -149.34876998, -0.01051355, -182.50419415, -0.13293621, -18.25041941, -0.43721144, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 28615540.04389865, 0.08, 0.00106667, 0.00026667, 11923141.68495777, 0.00073242)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32864982278000004, 2003992, 0.32864982278000004, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 73.37441216, 0.00736277, 89.74712827, 0.07851772, 8.97471283, 0.32012738, -171.85248433, -0.00859836, -210.19953007, -0.0955793, -21.01995301, -0.33718896, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 73.37441216, 0.00736277, 89.74712827, 0.07862326, 8.97471283, 0.32108386, -171.85248433, -0.00859836, -210.19953007, -0.09570831, -21.01995301, -0.33816891, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 28257197.57350907, 0.1125, 0.00189844, 0.00058594, 11773832.32229545, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.37089655111000003, 2103992, 0.37089655111000003, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 72.19181031, 0.00736626, 88.33350471, 0.07982142, 8.83335047, 0.32447427, -169.12896955, -0.00859986, -206.94528319, -0.0971702, -20.69452832, -0.34182304, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 72.19181031, 0.00736626, 88.33350471, 0.08061936, 8.83335047, 0.33171181, -169.12896955, -0.00859986, -206.94528319, -0.09814562, -20.69452832, -0.34923806, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 28111107.03979897, 0.1125, 0.00189844, 0.00058594, 11712961.2665829, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36944716018999996, 2203992, 0.36944716018999996, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 36.22774819, 0.00799683, 44.19873086, 0.09768009, 4.41987309, 0.40378081, -146.85723844, -0.0103397, -179.16939036, -0.13512195, -17.91693904, -0.44122267, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 36.22774819, 0.00799683, 44.19873086, 0.09762193, 4.41987309, 0.40372265, -146.85723844, -0.0103397, -179.16939036, -0.13504103, -17.91693904, -0.44114175, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 29213966.09581314, 0.08, 0.00106667, 0.00026667, 12172485.87325547, 0.00073242)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32668985808, 2303992, 0.32668985808, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 35.67258932, 0.00824587, 43.57080208, 0.09921925, 4.35708021, 0.4048165, -144.50335332, -0.01064487, -176.49761704, -0.13722214, -17.6497617, -0.4428194, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 35.67258932, 0.00824587, 43.57080208, 0.09906734, 4.35708021, 0.40466459, -144.50335332, -0.01064487, -176.49761704, -0.13701078, -17.6497617, -0.44260804, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 28797658.29210876, 0.08, 0.00106667, 0.00026667, 11999024.28837865, 0.00073242)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32722806973, 2013992, 0.32722806973, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 70.942938, 0.00727181, 86.64032809, 0.07863251, 8.66403281, 0.32184208, -166.26396377, -0.00846908, -203.0528306, -0.09570153, -20.30528306, -0.33891111, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 105.15109956, 0.0075109, 128.41765541, 0.08356807, 12.84176554, 0.33458317, -245.27456312, -0.00907547, -299.54593399, -0.10204897, -29.9545934, -0.35306407, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 28840571.4882955, 0.1125, 0.00189844, 0.00058594, 12016904.78678979, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36695177379, 2113992, 0.36695177379, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 72.76888056, 0.00749708, 88.99191678, 0.08032096, 8.89919168, 0.3276412, -170.51801176, -0.00874309, -208.53316139, -0.09776417, -20.85331614, -0.34508441, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 107.84333554, 0.00774497, 131.88584281, 0.0839079, 13.18858428, 0.32797029, -251.52572656, -0.00937405, -307.60067155, -0.10247683, -30.76006716, -0.34653922, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 28320881.1624359, 0.1125, 0.00189844, 0.00058594, 11800367.15101496, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.37159164557, 2213992, 0.37159164557, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 35.93586894, 0.00823153, 43.89445099, 0.09846493, 4.3894451, 0.40363948, -145.6080671, -0.01063508, -177.85533936, -0.1361828, -17.78553394, -0.44135734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 35.93586894, 0.00823153, 43.89445099, 0.09843044, 4.3894451, 0.40360498, -145.6080671, -0.01063508, -177.85533936, -0.13613481, -17.78553394, -0.44130935, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 28779978.64005725, 0.08, 0.00106667, 0.00026667, 11991657.76669052, 0.00073242)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32768133178, 2313992, 0.32768133178, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 36.02645243, 0.00798486, 44.01096017, 0.09774212, 4.40109602, 0.40430753, -146.00605956, -0.01034562, -178.36524107, -0.13523085, -17.83652411, -0.44179625, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 36.02645243, 0.00798486, 44.01096017, 0.0985811, 4.40109602, 0.4051465, -146.00605956, -0.01034562, -178.36524107, -0.13639817, -17.83652411, -0.44296357, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 28730051.47925355, 0.08, 0.00106667, 0.00026667, 11970854.78302231, 0.00073242)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32619466826000004, 2023992, 0.32619466826000004, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 105.03376695, 0.00758148, 128.08422163, 0.08270367, 12.80842216, 0.32855345, -245.16298932, -0.00913799, -298.96586186, -0.10096856, -29.89658619, -0.34681834, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 70.91130358, 0.00733816, 86.47332556, 0.07847887, 8.64733256, 0.32198653, -166.23236677, -0.00852914, -202.71331712, -0.09549267, -20.27133171, -0.33900033, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29380602.02451143, 0.1125, 0.00189844, 0.00058594, 12241917.5102131, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36766701121, 2123992, 0.36766701121, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 107.94356226, 0.0074435, 131.6052614, 0.08197904, 13.16052614, 0.32666424, -251.50845306, -0.00898928, -306.64020177, -0.10010271, -30.66402018, -0.34478791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 72.71417017, 0.00721389, 88.65343308, 0.07867836, 8.86534331, 0.32825559, -170.3599547, -0.00839873, -207.70359902, -0.09575805, -20.7703599, -0.34533528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 29454377.32804001, 0.1125, 0.00189844, 0.00058594, 12272657.22001667, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.3685992375, 2223992, 0.3685992375, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 35.39307555, 0.00792731, 43.23194452, 0.09863866, 4.32319445, 0.40675724, -143.44871049, -0.0102604, -175.21977382, -0.13647311, -17.52197738, -0.4445917, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 35.39307555, 0.00792731, 43.23194452, 0.09960659, 4.32319445, 0.40772517, -143.44871049, -0.0102604, -175.21977382, -0.13781985, -17.52197738, -0.44593844, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 28775676.59388151, 0.08, 0.00106667, 0.00026667, 11989865.24745063, 0.00073242)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32455036643, 2323992, 0.32455036643, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
