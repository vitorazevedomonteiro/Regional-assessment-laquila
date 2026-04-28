import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.30795789, 0.0104031, 38.08423007, 0.06035364, 3.80842301, 0.26639089, -80.04525239, -0.01202037, -97.37019001, -0.07430532, -9.737019, -0.28034257, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 46.19430352, 0.01083495, 56.19256579, 0.06142311, 5.61925658, 0.26718653, -79.94143636, -0.01195797, -97.24390411, -0.06953793, -9.72439041, -0.27530134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 30234282.79977469, 0.07, 0.00071458, 0.00023333, 12597617.83323945, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.33203357878000006, 1001992, 0.33203357878000006, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 41.76724464, 0.01020462, 50.55347058, 0.08131603, 5.05534706, 0.36400834, -72.10831796, -0.01121302, -87.27714174, -0.09215274, -8.72771417, -0.37484505, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 41.76724464, 0.01020462, 50.55347058, 0.08221658, 5.05534706, 0.37347489, -72.10831796, -0.01121302, -87.27714174, -0.09317776, -8.72771417, -0.38443607, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 31806048.85577076, 0.07, 0.00071458, 0.00023333, 13252520.35657115, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25349583584, 1101992, 0.25349583584, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 46.27940268, 0.00988187, 56.14806264, 0.06522925, 5.61480626, 0.28533955, -80.19687613, -0.01092218, -97.29812754, -0.07391913, -9.72981275, -0.29402943, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.21560365, 0.00948737, 37.87204605, 0.06381254, 3.7872046, 0.28112312, -80.21128156, -0.01099234, -97.31560481, -0.07873217, -9.73156048, -0.29604274, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 31083549.26304968, 0.07, 0.00071458, 0.00023333, 12951478.85960403, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32692100046, 1201992, 0.32692100046, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 71.78720749, 0.00732741, 88.0826813, 0.07043209, 8.80826813, 0.28365592, -168.09017101, -0.0085859, -206.24611935, -0.08572607, -20.62461193, -0.2989499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 106.4837569, 0.00756792, 130.65524, 0.07592604, 13.065524, 0.30462917, -248.02466789, -0.00921383, -304.32549951, -0.09277588, -30.43254995, -0.32147901, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 26960343.05070087, 0.1125, 0.00189844, 0.00058594, 11233476.27112536, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36837838514, 1011992, 0.36837838514, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 112.06106588, 0.00790547, 137.25668005, 0.09577308, 13.72566801, 0.38026055, -261.06496976, -0.00959963, -319.76236123, -0.11701039, -31.97623612, -0.40149787, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 112.06106588, 0.00790547, 137.25668005, 0.09300542, 13.72566801, 0.35669459, -261.06496976, -0.00959963, -319.76236123, -0.11362717, -31.97623612, -0.37731634, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27702955.42238175, 0.1125, 0.00189844, 0.00058594, 11542898.09265906, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30868897449000005, 1111992, 0.30868897449000005, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 99.65635919, 0.00710666, 120.42625316, 0.06989618, 12.04262532, 0.2885099, -232.86211844, -0.00848823, -281.39410925, -0.08524315, -28.13941093, -0.30385687, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 67.28640443, 0.00688222, 81.30990978, 0.06640725, 8.13099098, 0.28348597, -157.86357367, -0.00794154, -190.76473233, -0.08070589, -19.07647323, -0.29778461, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 32274524.65622501, 0.1125, 0.00189844, 0.00058594, 13447718.60676042, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.35851582234, 1211992, 0.35851582234, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 98.47450197, 0.00895165, 119.32216885, 0.0675934, 11.93221688, 0.27399323, -150.32271861, -0.00978097, -182.14697666, -0.074617, -18.21469767, -0.28101683, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 145.81810155, 0.00934455, 176.68870404, 0.07165789, 17.6688704, 0.27549537, -221.9890146, -0.01042975, -268.98547494, -0.07932519, -26.89854749, -0.28316268, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 31473239.85697389, 0.1, 0.00133333, 0.00052083, 13113849.94040579, 0.00127345)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.41376723815000005, 1021992, 0.41376723815000005, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 134.04464523, 0.01043129, 162.25423528, 0.07412418, 16.22542353, 0.29128484, -204.20721371, -0.01157171, -247.18246107, -0.08199242, -24.71824611, -0.29915309, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 134.04464523, 0.01043129, 162.25423528, 0.07464364, 16.22542353, 0.29602908, -204.20721371, -0.01157171, -247.18246107, -0.08256676, -24.71824611, -0.3039522, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 31784607.9461172, 0.1, 0.00133333, 0.00052083, 13243586.6442155, 0.00127345)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.34679308349000004, 1121992, 0.34679308349000004, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 136.60850018, 0.0096347, 167.78937718, 0.07939303, 16.77893772, 0.28817499, -208.04067594, -0.01084554, -255.52594018, -0.08797238, -25.55259402, -0.29675435, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 92.51984336, 0.00919897, 113.63748869, 0.07569278, 11.36374887, 0.29361692, -141.17829564, -0.01011936, -173.40222802, -0.08363686, -17.3402228, -0.301561, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 26507061.70082674, 0.1, 0.00133333, 0.00052083, 11044609.04201114, 0.00127345)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.40833622353, 1221992, 0.40833622353, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 53.18497453, 0.00982236, 64.61057124, 0.0709795, 6.46105712, 0.27145888, -81.28029504, -0.01069131, -98.74154005, -0.07830843, -9.874154, -0.27878782, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 53.18497453, 0.00982236, 64.61057124, 0.06984853, 6.46105712, 0.26164489, -81.28029504, -0.01069131, -98.74154005, -0.07705801, -9.874154, -0.26885436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 30668826.70278731, 0.07, 0.00071458, 0.00023333, 12778677.79282805, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.36490133176, 1031992, 0.36490133176, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 55.20444481, 0.01034532, 67.46969648, 0.07966894, 6.74696965, 0.30477626, -84.337989, -0.01129611, -103.07609358, -0.08794234, -10.30760936, -0.31304966, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 55.20444481, 0.01034532, 67.46969648, 0.07945534, 6.74696965, 0.3029208, -84.337989, -0.01129611, -103.07609358, -0.08770618, -10.30760936, -0.31117163, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 28559999.51748579, 0.07, 0.00071458, 0.00023333, 11899999.79895241, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.30397506912, 1131992, 0.30397506912, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 53.81259291, 0.01005315, 65.76949944, 0.07580871, 6.57694994, 0.28261094, -82.20878181, -0.01097802, -100.47518874, -0.0836793, -10.04751887, -0.29048153, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 53.81259291, 0.01005315, 65.76949944, 0.07243729, 6.57694994, 0.25496681, -82.20878181, -0.01097802, -100.47518874, -0.07995175, -10.04751887, -0.26248127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 28554820.07255786, 0.07, 0.00071458, 0.00023333, 11897841.69689911, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.3673922813, 1231992, 0.3673922813, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 30.04960055, 0.00967422, 36.5575233, 0.06210397, 3.65575233, 0.27299128, -77.02815801, -0.01120077, -93.71035321, -0.07657713, -9.37103532, -0.28746444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 44.43168449, 0.01007819, 54.05437382, 0.06528347, 5.40543738, 0.29624916, -76.95656253, -0.01113627, -93.62325211, -0.07397149, -9.36232521, -0.30493717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 30197685.4393489, 0.07, 0.00071458, 0.00023333, 12582368.93306204, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32515479775, 1002992, 0.32515479775, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 46.26484388, 0.00998967, 56.35625522, 0.07306348, 5.63562552, 0.32805573, -80.15360403, -0.01106553, -97.63692227, -0.08285678, -9.76369223, -0.33784903, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 46.26484388, 0.00998967, 56.35625522, 0.07834899, 5.63562552, 0.3869721, -80.15360403, -0.01106553, -97.63692227, -0.08887279, -9.76369223, -0.3974959, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29764953.98478334, 0.07, 0.00071458, 0.00023333, 12402064.16032639, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25940093309, 1102992, 0.25940093309, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 47.20913572, 0.00978617, 57.45532526, 0.06636065, 5.74553253, 0.28689846, -81.76150031, -0.01084723, -99.50687559, -0.07524088, -9.95068756, -0.29577869, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 31.80478528, 0.00938768, 38.70764112, 0.0648899, 3.87076411, 0.28236779, -81.72479409, -0.01092554, -99.46220272, -0.08013306, -9.94622027, -0.29761095, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 30069165.11163786, 0.07, 0.00071458, 0.00023333, 12528818.79651578, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32757073204, 1202992, 0.32757073204, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 60.67015402, 0.00803413, 72.89052952, 0.06257953, 7.28905295, 0.27081437, -142.01559517, -0.00933169, -170.62082828, -0.07600885, -17.06208283, -0.2842437, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 89.79163008, 0.0083031, 107.87774595, 0.06631587, 10.7877746, 0.27698838, -209.36407018, -0.00999588, -251.53484744, -0.08091162, -25.15348474, -0.29158413, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 33844157.31554893, 0.1, 0.00133333, 0.00052083, 14101732.21481205, 0.00127345)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36225728804, 1012992, 0.36225728804, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 94.54329733, 0.00950559, 114.91997518, 0.08759279, 11.49199752, 0.35160711, -220.3833039, -0.01152254, -267.88196019, -0.10697759, -26.78819602, -0.3709919, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 94.54329733, 0.00950559, 114.91997518, 0.08774452, 11.49199752, 0.35297735, -220.3833039, -0.01152254, -267.88196019, -0.10716306, -26.78819602, -0.37239589, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 30481820.08480467, 0.1, 0.00133333, 0.00052083, 12700758.36866861, 0.00127345)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30909053474000003, 1112992, 0.30909053474000003, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 90.63475926, 0.00839538, 109.60231001, 0.08218893, 10.960231, 0.33084437, -211.17335186, -0.01016391, -255.3665654, -0.10037033, -25.53665654, -0.34902578, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 61.21941496, 0.0081223, 74.03108203, 0.07676425, 7.4031082, 0.31636141, -143.23919109, -0.00947657, -173.21551197, -0.09338558, -17.3215512, -0.33298275, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 32069553.17874201, 0.1, 0.00133333, 0.00052083, 13362313.82447584, 0.00127345)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36371575118, 1212992, 0.36371575118, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 64.94613861, 0.00848083, 78.78515152, 0.08085628, 7.87851515, 0.35004555, -151.39260414, -0.01013712, -183.65201553, -0.09861003, -18.36520155, -0.36779929, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 96.42292162, 0.00892076, 116.96914787, 0.08368086, 11.69691479, 0.35287013, -151.61674558, -0.01002094, -183.92391803, -0.09344059, -18.3923918, -0.36262986, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 31123766.46490306, 0.08, 0.00106667, 0.00026667, 12968236.02704294, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.37148583755, 1022992, 0.37148583755, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 96.00215414, 0.00915665, 116.94207027, 0.10215024, 11.69420703, 0.42999837, -150.99754056, -0.01030737, -183.93300814, -0.11407251, -18.39330081, -0.44192063, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 96.00215414, 0.00915665, 116.94207027, 0.09636925, 11.69420703, 0.39140247, -150.99754056, -0.01030737, -183.93300814, -0.1076219, -18.39330081, -0.40265512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29765929.97205687, 0.08, 0.00106667, 0.00026667, 12402470.82169036, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30501928035, 1122992, 0.30501928035, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 97.35702505, 0.00891107, 117.13403525, 0.06754081, 11.71340353, 0.30877521, -153.18928381, -0.00996845, -184.30800409, -0.07538935, -18.43080041, -0.31662374, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 65.57364031, 0.00848483, 78.89420504, 0.06999538, 7.8894205, 0.33831834, -152.99856519, -0.01007448, -184.07854307, -0.08526597, -18.40785431, -0.35358892, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 33473879.04436895, 0.08, 0.00106667, 0.00026667, 13947449.6018204, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.37268522624, 1222992, 0.37268522624, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 30.35523477, 0.00947822, 37.25378972, 0.07618078, 3.72537897, 0.31666511, -77.91113535, -0.01111096, -95.61728234, -0.09428456, -9.56172823, -0.33476889, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 44.99163124, 0.00989865, 55.21646538, 0.07417391, 5.52164654, 0.28760336, -77.90390046, -0.01102681, -95.60840325, -0.08418555, -9.56084033, -0.297615, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 26866315.38256085, 0.07, 0.00071458, 0.00023333, 11194298.07606702, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32464892995000005, 1032992, 0.32464892995000005, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 46.83081525, 0.00939297, 56.40191238, 0.06849527, 5.64019124, 0.32440191, -81.13704143, -0.01036231, -97.71950963, -0.07763314, -9.77195096, -0.33353978, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 46.83081525, 0.00939297, 56.40191238, 0.06963622, 5.64019124, 0.33741695, -81.13704143, -0.01036231, -97.71950963, -0.07893178, -9.77195096, -0.34671251, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 33201213.26326399, 0.07, 0.00071458, 0.00023333, 13833838.85969333, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25691399436, 1132992, 0.25691399436, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 45.31051397, 0.01016642, 54.89368954, 0.06805308, 5.48936895, 0.29697263, -78.49531314, -0.01120984, -95.09707512, -0.07709702, -9.50970751, -0.30601657, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 30.63815162, 0.00976627, 37.11812195, 0.06481489, 3.7118122, 0.27448674, -78.5660456, -0.0112716, -95.18276749, -0.07991352, -9.51827675, -0.28958537, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 31524787.49949726, 0.07, 0.00071458, 0.00023333, 13135328.12479053, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32712851872, 1232992, 0.32712851872, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 30.02113541, 0.00899531, 36.47562493, 0.06022691, 3.64756249, 0.27116715, -52.130939, -0.00976172, -63.33899608, -0.06807404, -6.33389961, -0.27901427, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 29.96459446, 0.00894357, 36.40692777, 0.06122836, 3.64069278, 0.27057464, -77.00851673, -0.01038584, -93.56520777, -0.07558145, -9.35652078, -0.28492772, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 30623468.39332607, 0.07, 0.00071458, 0.00023333, 12759778.4972192, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32083263326000006, 1003992, 0.32083263326000006, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 31.54597062, 0.00942226, 38.70573332, 0.07383161, 3.87057333, 0.32661378, -80.97302872, -0.01106827, -99.35089631, -0.09138238, -9.93508963, -0.34416455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 31.54597062, 0.00942226, 38.70573332, 0.0784829, 3.87057333, 0.37673082, -80.97302872, -0.01106827, -99.35089631, -0.09718223, -9.93508963, -0.39543015, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 26972430.13084736, 0.07, 0.00071458, 0.00023333, 11238512.55451973, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25898282839000003, 1103992, 0.25898282839000003, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 30.92227426, 0.00935251, 37.62891605, 0.06254997, 3.7628916, 0.27534442, -79.45125738, -0.01086918, -96.68320862, -0.07720282, -9.66832086, -0.28999728, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 30.98428456, 0.00940455, 37.70437557, 0.0607697, 3.77043756, 0.26783579, -53.79351413, -0.01021022, -65.46063235, -0.06867455, -6.54606324, -0.27574064, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 30111036.44644431, 0.07, 0.00071458, 0.00023333, 12546265.18601846, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32540345381999997, 1203992, 0.32540345381999997, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 61.71985794, 0.00835782, 74.795459, 0.07302052, 7.4795459, 0.3266092, -144.04959298, -0.00996319, -174.56708077, -0.08900791, -17.45670808, -0.34259659, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 61.57375052, 0.0082573, 74.61839814, 0.07686833, 7.46183981, 0.33590925, -211.97814084, -0.01088656, -256.88656572, -0.10276922, -25.68865657, -0.36181013, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 31436177.37471448, 0.08, 0.00106667, 0.00026667, 13098407.23946437, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.36582411624000005, 1013992, 0.36582411624000005, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 64.72267953, 0.00829539, 78.15571413, 0.0854562, 7.81557141, 0.38461046, -222.50382855, -0.01091794, -268.68395659, -0.1142503, -26.86839566, -0.41340455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 64.72267953, 0.00829539, 78.15571413, 0.08918028, 7.81557141, 0.41948107, -222.50382855, -0.01091794, -268.68395659, -0.1192375, -26.86839566, -0.4495383, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 32478545.91129325, 0.08, 0.00106667, 0.00026667, 13532727.46303886, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.30275434210999996, 1113992, 0.30275434210999996, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 61.60056445, 0.00869402, 75.26717029, 0.07781581, 7.52671703, 0.32486401, -212.03529674, -0.01158717, -259.07711935, -0.10415382, -25.90771193, -0.35120201, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 61.79262085, 0.00879775, 75.50183603, 0.07674549, 7.5501836, 0.3440171, -144.16580756, -0.01055992, -176.1502104, -0.09362032, -17.61502104, -0.36089192, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 28659351.85532567, 0.08, 0.00106667, 0.00026667, 11941396.6063857, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.36956856093, 1213992, 0.36956856093, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 61.97260056, 0.00877174, 75.40418576, 0.07686635, 7.54041858, 0.33717153, -144.65083586, -0.01047734, -176.00162651, -0.09371728, -17.60016265, -0.35402246, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 61.97260056, 0.00877174, 75.40418576, 0.07944068, 7.54041858, 0.34987662, -144.65083586, -0.01047734, -176.00162651, -0.09686418, -17.60016265, -0.36730012, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 30153226.97971718, 0.08, 0.00106667, 0.00026667, 12563844.57488216, 0.00073242)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36977333662, 1023992, 0.36977333662, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 62.77932078, 0.00850379, 76.12880042, 0.10411242, 7.61288004, 0.43670197, -146.51050133, -0.01014343, -177.6646924, -0.12701694, -17.76646924, -0.4596065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 62.77932078, 0.00850379, 76.12880042, 0.09766756, 7.61288004, 0.40875528, -146.51050133, -0.01014343, -177.6646924, -0.11913864, -17.76646924, -0.43022636, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 31237078.43871237, 0.08, 0.00106667, 0.00026667, 13015449.34946349, 0.00073242)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30067089633, 1123992, 0.30067089633, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 65.45828054, 0.00841149, 79.24422829, 0.08111651, 7.92442283, 0.35022903, -152.54322326, -0.01004197, -184.66983715, -0.09891775, -18.46698372, -0.36803027, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 65.45828054, 0.00841149, 79.24422829, 0.08176091, 7.92442283, 0.35087343, -152.54322326, -0.01004197, -184.66983715, -0.09970547, -18.46698372, -0.36881799, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 31745987.4244872, 0.08, 0.00106667, 0.00026667, 13227494.760203, 0.00073242)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.37159178105, 1223992, 0.37159178105, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 30.92362284, 0.00942893, 37.3671173, 0.05791088, 3.73671173, 0.26743198, -53.69078551, -0.0102028, -64.87822886, -0.06538544, -6.48782289, -0.27490654, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 30.86177952, 0.00938682, 37.29238781, 0.05932446, 3.72923878, 0.27186755, -79.31038108, -0.01084001, -95.83612916, -0.07310888, -9.58361292, -0.28565197, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 32285675.97503908, 0.07, 0.00071458, 0.00023333, 13452364.98959962, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32558307506, 1033992, 0.32558307506, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 31.9260914, 0.0095659, 38.43721847, 0.06726221, 3.84372185, 0.32274998, -82.08539814, -0.01102697, -98.82620274, -0.08297037, -9.88262027, -0.33845815, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 31.9260914, 0.0095659, 38.43721847, 0.06849914, 3.84372185, 0.33717124, -82.08539814, -0.01102697, -98.82620274, -0.08451274, -9.88262027, -0.35318484, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 33297059.70794719, 0.07, 0.00071458, 0.00023333, 13873774.87831133, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.2611161325, 1133992, 0.2611161325, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 30.83972394, 0.00988874, 37.3942197, 0.07173187, 3.73942197, 0.31414581, -79.05576266, -0.01141719, -95.85781515, -0.0885314, -9.58578152, -0.33094534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 30.89910381, 0.0099189, 37.46621982, 0.06955092, 3.74662198, 0.30468073, -53.55968629, -0.01073277, -64.94295084, -0.07860654, -6.49429508, -0.31373635, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 31264344.52732321, 0.07, 0.00071458, 0.00023333, 13026810.219718, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32826480683, 1233992, 0.32826480683, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 30.66305107, 0.0096544, 37.45112853, 0.05815656, 3.74511285, 0.29898468, -30.66305107, -0.0096544, -37.45112853, -0.05815656, -3.74511285, -0.29898468, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 30.61812647, 0.00962234, 37.39625868, 0.05659186, 3.73962587, 0.27285554, -45.38807387, -0.01011976, -55.43592464, -0.06157584, -5.54359246, -0.27783952, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 28807436.34512423, 0.07, 0.00071458, 0.00023333, 12003098.47713509, 0.00060032)
    ops.section('Aggregator', 1004991, 1004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1004992, 1004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.32561624496, 1004992, 0.32561624496, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 30.38682058, 0.0101194, 36.75004406, 0.05654571, 3.67500441, 0.3235976, -44.92611194, -0.01059317, -54.33396984, -0.06145415, -5.43339698, -0.32850604, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 30.38682058, 0.0101194, 36.75004406, 0.05785343, 3.67500441, 0.34309477, -44.92611194, -0.01059317, -54.33396984, -0.06288679, -5.43339698, -0.34812812, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 32037627.04129776, 0.07, 0.00071458, 0.00023333, 13349011.2672074, 0.00060032)
    ops.section('Aggregator', 1104991, 1104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1104992, 1104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.26004854464, 1104992, 0.26004854464, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 31.20738941, 0.00912769, 37.76438802, 0.05050673, 3.7764388, 0.27520823, -46.30228904, -0.00958433, -56.03088379, -0.05491593, -5.60308838, -0.27961743, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 31.23852447, 0.00916476, 37.80206488, 0.04898937, 3.78020649, 0.26073067, -31.23852447, -0.00916476, -37.80206488, -0.04898937, -3.78020649, -0.26073067, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 31867368.21124681, 0.07, 0.00071458, 0.00023333, 13278070.08801951, 0.00060032)
    ops.section('Aggregator', 1204991, 1204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1204992, 1204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.32416188916, 1204992, 0.32416188916, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 33.29824374, 0.00782963, 40.6260862, 0.08347731, 4.06260862, 0.3695677, -134.78558231, -0.0100733, -164.44743237, -0.11532693, -16.44474324, -0.40141733, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 33.29824374, 0.00782963, 40.6260862, 0.0846562, 4.06260862, 0.38143573, -134.78558231, -0.0100733, -164.44743237, -0.1169672, -16.44474324, -0.41374673, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 29201323.31508433, 0.08, 0.00106667, 0.00026667, 12167218.0479518, 0.00073242)
    ops.section('Aggregator', 1014991, 1014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1014992, 1014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.31958988947, 1014992, 0.31958988947, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 38.25841783, 0.00847523, 46.41573837, 0.11305325, 4.64157384, 0.4888985, -155.23556702, -0.01086045, -188.33432937, -0.15636678, -18.83343294, -0.53221203, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 38.25841783, 0.00847523, 46.41573837, 0.11026291, 4.64157384, 0.48610816, -155.23556702, -0.01086045, -188.33432937, -0.15248439, -18.83343294, -0.52832964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 31089858.85193303, 0.08, 0.00106667, 0.00026667, 12954107.8549721, 0.00073242)
    ops.section('Aggregator', 1114991, 1114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1114992, 1114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.26606694783, 1114992, 0.26606694783, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 35.09698042, 0.00801828, 42.88832268, 0.08203149, 4.28883227, 0.36308703, -142.20943285, -0.01037018, -173.77916766, -0.11334966, -17.37791677, -0.39440519, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 35.09698042, 0.00801828, 42.88832268, 0.08493552, 4.28883227, 0.39285726, -142.20943285, -0.01037018, -173.77916766, -0.11739022, -17.37791677, -0.42531197, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 28617189.82136149, 0.08, 0.00106667, 0.00026667, 11923829.09223395, 0.00073242)
    ops.section('Aggregator', 1214991, 1214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1214992, 1214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.32455917967, 1214992, 0.32455917967, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 55.11443753, 0.01081553, 67.39192863, 0.07775761, 6.73919286, 0.32539711, -128.16289379, -0.01318004, -156.71292274, -0.09501111, -15.67129227, -0.34265061, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 55.11443753, 0.01081553, 67.39192863, 0.08235992, 6.73919286, 0.34788605, -128.16289379, -0.01318004, -156.71292274, -0.10063704, -15.67129227, -0.36616318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 28376496.02844168, 0.07, 0.00071458, 0.00023333, 11823540.0118507, 0.00060032)
    ops.section('Aggregator', 1024991, 1024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1024992, 1024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.37661076423, 1024992, 0.37661076423, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 51.35755185, 0.00999771, 62.20928487, 0.09926271, 6.22092849, 0.43678138, -119.51244863, -0.01204802, -144.76515518, -0.12116698, -14.47651552, -0.45868565, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 51.35755185, 0.00999771, 62.20928487, 0.09664753, 6.22092849, 0.41217609, -119.51244863, -0.01204802, -144.76515518, -0.11797014, -14.47651552, -0.43349871, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 31575185.87805902, 0.07, 0.00071458, 0.00023333, 13156327.44919126, 0.00060032)
    ops.section('Aggregator', 1124991, 1124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1124992, 1124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.29627990796000003, 1124992, 0.29627990796000003, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 53.49873779, 0.00977421, 65.37363539, 0.09336997, 6.53736354, 0.36664094, -124.26517178, -0.01194281, -151.8478074, -0.11413159, -15.18478074, -0.38740257, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 53.49873779, 0.00977421, 65.37363539, 0.08886426, 6.53736354, 0.35017416, -124.26517178, -0.01194281, -151.8478074, -0.10862375, -15.18478074, -0.36993365, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 28626091.79183463, 0.07, 0.00071458, 0.00023333, 11927538.24659777, 0.00060032)
    ops.section('Aggregator', 1224991, 1224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1224992, 1224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.36593714254000004, 1224992, 0.36593714254000004, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 31.08352586, 0.00988231, 37.7437915, 0.04567299, 3.77437915, 0.25277253, -31.08352586, -0.00988231, -37.7437915, -0.04567299, -3.77437915, -0.25277253, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 31.0409984, 0.00985823, 37.6921517, 0.04592011, 3.76921517, 0.25024025, -45.99595285, -0.0103435, -55.85150354, -0.04985003, -5.58515035, -0.25417017, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 30815990.92082305, 0.07, 0.00071458, 0.00023333, 12839996.21700961, 0.00060032)
    ops.section('Aggregator', 1034991, 1034990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1034992, 1034991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.32811460951, 1034992, 0.32811460951, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 28.43433185, 0.00953531, 34.50249438, 0.07065614, 3.45024944, 0.37843241, -42.03575126, -0.00998954, -51.00658878, -0.07694866, -5.10065888, -0.38472494, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 28.43433185, 0.00953531, 34.50249438, 0.06734548, 3.45024944, 0.33703625, -42.03575126, -0.00998954, -51.00658878, -0.07332177, -5.10065888, -0.34301254, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 31040003.26271809, 0.07, 0.00071458, 0.00023333, 12933334.6927992, 0.00060032)
    ops.section('Aggregator', 1134991, 1134990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1134992, 1134991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.25211656228, 1134992, 0.25211656228, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 31.23134533, 0.00930757, 38.15996341, 0.05782457, 3.81599634, 0.29615817, -46.32191693, -0.0098018, -56.59835132, -0.06295317, -5.65983513, -0.30128677, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 31.26398942, 0.00935079, 38.19984954, 0.05669262, 3.81998495, 0.28873645, -31.26398942, -0.00935079, -38.19984954, -0.05669262, -3.81998495, -0.28873645, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 28662516.11590623, 0.07, 0.00071458, 0.00023333, 11942715.04829426, 0.00060032)
    ops.section('Aggregator', 1234991, 1234990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1234992, 1234991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.32503270448, 1234992, 0.32503270448, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 48.68943763, 0.00961332, 58.94853024, 0.11971278, 5.89485302, 0.5068795, -130.35351525, -0.01160561, -157.8196116, -0.15143746, -15.78196116, -0.53860417, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 48.68943763, 0.00961332, 58.94853024, 0.11645802, 5.89485302, 0.50362474, -130.35351525, -0.01160561, -157.8196116, -0.14730374, -15.78196116, -0.53447046, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 31721877.05472576, 0.08, 0.00106667, 0.00026667, 13217448.7728024, 0.00073242)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25828666436, 6200992, 0.25828666436, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 61.98082109, 0.00870075, 75.10611908, 0.09850184, 7.51061191, 0.43040156, -144.72108325, -0.01035306, -175.36777864, -0.12012734, -17.53677786, -0.45202706, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 61.98082109, 0.00870075, 75.10611908, 0.0955422, 7.51061191, 0.41707207, -144.72108325, -0.01035306, -175.36777864, -0.11650944, -17.53677786, -0.4380393, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 31458802.48509797, 0.08, 0.00106667, 0.00026667, 13107834.36879082, 0.00073242)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30129582472, 6201992, 0.30129582472, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 45.93859747, 0.00971703, 55.63312778, 0.10533116, 5.56331278, 0.47666647, -125.07004935, -0.01211632, -151.46387613, -0.13355108, -15.14638761, -0.50488638, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 45.93859747, 0.00971703, 55.63312778, 0.10867068, 5.56331278, 0.49576254, -125.07004935, -0.01211632, -151.46387613, -0.13779244, -15.14638761, -0.52488429, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 31641011.99936633, 0.07, 0.00071458, 0.00023333, 13183754.99973597, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.258336616, 6202992, 0.258336616, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 6203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6203990, 37.23960962, 0.0125843, 45.20251548, 0.12215678, 4.52025155, 0.50729238, -100.4851769, -0.01597068, -121.97181472, -0.15513323, -12.19718147, -0.54026883, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6203991, 37.23960962, 0.0125843, 45.20251548, 0.11822639, 4.52025155, 0.48934259, -100.4851769, -0.01597068, -121.97181472, -0.15014143, -12.19718147, -0.52125764, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6203990, 30931289.18848925, 0.06, 0.00045, 0.0002, 12888037.16187052, 0.00046953)
    ops.section('Aggregator', 6203991, 6203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6203992, 6203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6203, 6203991, 0.25964880751999997, 6203992, 0.25964880751999997, 6203990)
    # Create element
    ops.element('forceBeamColumn', 6203, 1104, 1204, 6203, 6203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 36.1528001, 0.00835547, 43.69148051, 0.0798416, 4.36914805, 0.34415319, -146.28316517, -0.01032187, -176.78652946, -0.10978526, -17.67865295, -0.37409685, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 70.29532377, 0.00878932, 84.95349627, 0.08235563, 8.49534963, 0.32845321, -215.14107692, -0.01108597, -260.00288064, -0.10702805, -26.00028806, -0.35312564, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 32249023.98061714, 0.1, 0.00133333, 0.00052083, 13437093.32525714, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32885487238000005, 2001992, 0.32885487238000005, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 84.16467459, 0.00635983, 101.40343636, 0.05962347, 10.14034364, 0.26668326, -197.75570307, -0.00728276, -238.26038593, -0.07239309, -23.82603859, -0.27945287, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 125.12967667, 0.00654767, 150.75896468, 0.06476117, 15.07589647, 0.29431945, -292.31310214, -0.00774618, -352.1852035, -0.07890729, -35.21852035, -0.30846557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 33101735.06715987, 0.125, 0.00260417, 0.00065104, 13792389.61131661, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.3713649928, 2101992, 0.3713649928, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.34163583, 0.00635361, 98.11902046, 0.06059772, 9.81190205, 0.26869152, -191.2498249, -0.00727119, -230.69668186, -0.07358005, -23.06966819, -0.28167385, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 120.74647553, 0.00654748, 145.65143401, 0.06552313, 14.5651434, 0.29338175, -282.49262618, -0.00774069, -340.75906497, -0.07983347, -34.0759065, -0.30769209, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 32776591.37707816, 0.125, 0.00260417, 0.00065104, 13656913.07378257, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36821433133, 2201992, 0.36821433133, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 36.74238487, 0.00783201, 44.71141522, 0.07859323, 4.47114152, 0.32960069, -149.51186771, -0.00981688, -181.93939292, -0.10827165, -18.19393929, -0.35927911, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 72.21575275, 0.00822571, 87.87857724, 0.08725074, 8.78785772, 0.37098777, -220.45584373, -0.01053226, -268.27035865, -0.11359338, -26.82703587, -0.39733041, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 30110421.06759332, 0.1, 0.00133333, 0.00052083, 12546008.77816388, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.3267965749, 2301992, 0.3267965749, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 66.2564627, 0.00874698, 80.01075878, 0.08046379, 8.00107588, 0.33137413, -202.24906497, -0.01098092, -244.23430548, -0.10451098, -24.42343055, -0.35542131, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 66.2564627, 0.00874698, 80.01075878, 0.08075986, 8.00107588, 0.33413424, -202.24906497, -0.01098092, -244.23430548, -0.1048971, -24.42343055, -0.35827148, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 32468220.39476516, 0.1, 0.00133333, 0.00052083, 13528425.16448549, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32417122579, 2011992, 0.32417122579, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 129.08159105, 0.0067683, 156.65999409, 0.07508565, 15.66599941, 0.312968, -301.14986138, -0.00805746, -365.49081183, -0.09156969, -36.54908118, -0.32945204, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 129.08159105, 0.0067683, 156.65999409, 0.07419396, 15.66599941, 0.30477707, -301.14986138, -0.00805746, -365.49081183, -0.09047967, -36.54908118, -0.32106278, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 30977551.03262661, 0.125, 0.00260417, 0.00065104, 12907312.93026109, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.37664657577000005, 2111992, 0.37664657577000005, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 114.69755271, 0.00659038, 139.65008606, 0.07740673, 13.96500861, 0.31460421, -268.45384233, -0.00783855, -326.85616474, -0.09440559, -32.68561647, -0.33160307, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 114.69755271, 0.00659038, 139.65008606, 0.07555683, 13.96500861, 0.29831888, -268.45384233, -0.00783855, -326.85616474, -0.09214424, -32.68561647, -0.31490629, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29926276.63371131, 0.125, 0.00260417, 0.00065104, 12469281.93071305, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36389936540999995, 2211992, 0.36389936540999995, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 74.84359927, 0.00865708, 91.85026416, 0.09455002, 9.18502642, 0.36627174, -228.04502581, -0.01125032, -279.86355635, -0.12326828, -27.98635563, -0.39499001, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 74.84359927, 0.00865708, 91.85026416, 0.09112492, 9.18502642, 0.33784398, -228.04502581, -0.01125032, -279.86355635, -0.11880141, -27.98635563, -0.36552047, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 26877548.79574397, 0.1, 0.00133333, 0.00052083, 11198978.66489332, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.33208795962, 2311992, 0.33208795962, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 74.32529505, 0.00880014, 90.30131302, 0.08661309, 9.0301313, 0.35071726, -227.30564271, -0.01121466, -276.16436611, -0.11269505, -27.61643661, -0.37679921, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 37.95781547, 0.00837292, 46.11674362, 0.08107606, 4.61167436, 0.33951614, -154.32417247, -0.0104461, -187.49572935, -0.11160279, -18.74957293, -0.37004287, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 30637020.73495996, 0.1, 0.00133333, 0.00052083, 12765425.30623332, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.33291579329000004, 2021992, 0.33291579329000004, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 117.53210304, 0.00674994, 143.66652657, 0.07987539, 14.36665266, 0.31964636, -274.88647451, -0.00806779, -336.01019612, -0.09745751, -33.60101961, -0.33722848, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 79.32178733, 0.00653756, 96.9597699, 0.07390924, 9.69597699, 0.29375572, -186.31308444, -0.00754635, -227.74163827, -0.08990256, -22.77416383, -0.30974904, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 28503444.74098441, 0.125, 0.00260417, 0.00065104, 11876435.3087435, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.36772842582, 2121992, 0.36772842582, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 117.69770659, 0.00673087, 144.27099508, 0.07251274, 14.42709951, 0.28776506, -275.05634877, -0.00807975, -337.15740339, -0.08849256, -33.71574034, -0.30374487, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 79.39363536, 0.00651935, 97.31879328, 0.06856254, 9.73187933, 0.27721165, -186.40270751, -0.00755138, -228.4879194, -0.08339395, -22.84879194, -0.29204307, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 27386041.54029221, 0.125, 0.00260417, 0.00065104, 11410850.64178842, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.36747133255000003, 2221992, 0.36747133255000003, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 71.23904649, 0.00812362, 86.49541509, 0.08528662, 8.64954151, 0.34498127, -217.60496796, -0.01036723, -264.20668099, -0.11099998, -26.4206681, -0.37069463, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 36.25911262, 0.0077365, 44.02426971, 0.08199573, 4.40242697, 0.35458285, -147.58991215, -0.00966775, -179.19738323, -0.11298952, -17.91973832, -0.38557664, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 30845509.20132431, 0.1, 0.00133333, 0.00052083, 12852295.5005518, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32520430189, 2321992, 0.32520430189, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 35.80378143, 0.00801377, 43.88890469, 0.08862022, 4.38889047, 0.35816089, -145.37839671, -0.01013027, -178.20739433, -0.12228335, -17.82073943, -0.39182403, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 52.9614226, 0.008211, 64.92104285, 0.08940048, 6.49210429, 0.33320509, -213.92537043, -0.01097718, -262.23347973, -0.12394147, -26.22334797, -0.36774609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 27371708.09731049, 0.1, 0.00133333, 0.00052083, 11404878.37387937, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.3260809399, 2002992, 0.3260809399, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 76.4538001, 0.00598423, 93.22864879, 0.07177071, 9.32286488, 0.29929344, -179.50258552, -0.0069061, -218.8875305, -0.08732454, -21.88875305, -0.31484726, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 76.35187645, 0.0059279, 93.10436191, 0.07279375, 9.31043619, 0.29188536, -264.65376436, -0.00743473, -322.7218636, -0.09698027, -32.27218636, -0.31607187, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29394032.69269226, 0.125, 0.00260417, 0.00065104, 12247513.62195511, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.35791091593, 2102992, 0.35791091593, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 82.41985527, 0.00652334, 99.87453043, 0.06354147, 9.98745304, 0.27576659, -193.72717972, -0.00748471, -234.75424754, -0.07718458, -23.47542475, -0.28940971, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 82.2740365, 0.00647141, 99.69783052, 0.06433849, 9.96978305, 0.26797604, -285.70203348, -0.00804018, -346.20731066, -0.08553472, -34.62073107, -0.28917227, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 31455369.86876662, 0.125, 0.00260417, 0.00065104, 13106404.11198609, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.37136360905, 2202992, 0.37136360905, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 37.24779176, 0.00791774, 44.97960081, 0.06988166, 4.49796008, 0.30495623, -151.71540464, -0.00983577, -183.20813167, -0.09605026, -18.32081317, -0.33112483, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 55.21780753, 0.00810019, 66.67979021, 0.0766173, 6.66797902, 0.34193404, -223.5069659, -0.01059283, -269.90201644, -0.10592521, -26.99020164, -0.37124196, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 32471518.9714893, 0.1, 0.00133333, 0.00052083, 13529799.57145387, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32845584896, 2302992, 0.32845584896, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 54.09893508, 0.00802707, 65.93332465, 0.08124885, 6.59333247, 0.32678265, -218.62551408, -0.01063706, -266.4508456, -0.11251537, -26.64508456, -0.35804918, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 54.09893508, 0.00802707, 65.93332465, 0.08073523, 6.59333247, 0.32220321, -218.62551408, -0.01063706, -266.4508456, -0.11180074, -26.64508456, -0.35326872, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29584411.0553639, 0.1, 0.00133333, 0.00052083, 12326837.93973496, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32637881234000005, 2012992, 0.32637881234000005, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 80.47575117, 0.00614772, 98.31729562, 0.07564755, 9.83172956, 0.30740612, -278.5585377, -0.00774248, -340.31520926, -0.10081538, -34.03152093, -0.33257395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 119.742521, 0.00640122, 146.28954269, 0.07715109, 14.62895427, 0.31147481, -279.2053252, -0.00767159, -341.10539011, -0.09415736, -34.11053901, -0.32848108, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28707953.84263736, 0.125, 0.00260417, 0.00065104, 11961647.43443223, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.3651006913, 2112992, 0.3651006913, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 83.85111351, 0.00644572, 101.9623026, 0.07255943, 10.19623026, 0.30257792, -290.71947484, -0.0080565, -353.51262287, -0.09659477, -35.35126229, -0.32661326, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 124.73272296, 0.00670451, 151.6740221, 0.07116288, 15.16740221, 0.28108421, -291.27188694, -0.00798837, -354.18435169, -0.08678331, -35.41843517, -0.29670465, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 30356214.16668524, 0.125, 0.00260417, 0.00065104, 12648422.56945218, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.37269764329, 2212992, 0.37269764329, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 54.38870904, 0.0082136, 65.64026455, 0.07207597, 6.56402646, 0.30416161, -220.25723232, -0.01070903, -265.82250716, -0.09956498, -26.58225072, -0.33165061, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 54.38870904, 0.0082136, 65.64026455, 0.07434767, 6.56402646, 0.32649656, -220.25723232, -0.01070903, -265.82250716, -0.10272574, -26.58225072, -0.35487463, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 32635235.99891802, 0.1, 0.00133333, 0.00052083, 13598014.99954917, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32817355206000004, 2312992, 0.32817355206000004, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 51.68756583, 0.00840463, 62.77419871, 0.07775865, 6.27741987, 0.31671149, -208.74493663, -0.01098807, -253.51931206, -0.10748492, -25.35193121, -0.34643775, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 35.10392436, 0.00818824, 42.63347843, 0.0790915, 4.26334784, 0.36228172, -141.94935176, -0.01016558, -172.39652654, -0.10881798, -17.23965265, -0.3920082, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 30757249.73112223, 0.1, 0.00133333, 0.00052083, 12815520.72130093, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32556890911, 2022992, 0.32556890911, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 120.84231234, 0.00653629, 146.98010268, 0.07987298, 14.69801027, 0.32761677, -282.25967882, -0.00778779, -343.31150879, -0.09743572, -34.33115088, -0.34517952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 81.35573947, 0.00634185, 98.95271539, 0.07264828, 9.89527154, 0.28988595, -191.07281505, -0.00730294, -232.4012296, -0.08835697, -23.24012296, -0.30559465, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 30273299.55127613, 0.125, 0.00260417, 0.00065104, 12613874.81303172, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.36781250379, 2122992, 0.36781250379, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 119.12076409, 0.00652441, 144.46836361, 0.06613154, 14.44683636, 0.27613288, -278.55496657, -0.00774627, -337.82842565, -0.08061098, -33.78284256, -0.29061232, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 80.2587871, 0.00632869, 97.33698173, 0.06306859, 9.73369817, 0.27112679, -188.61872247, -0.00726711, -228.75472961, -0.07662686, -22.87547296, -0.28468506, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 31199399.71444428, 0.125, 0.00260417, 0.00065104, 12999749.88101845, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36655356847000004, 2222992, 0.36655356847000004, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 54.6429671, 0.00789644, 66.79327008, 0.08325561, 6.67932701, 0.33060968, -220.35753832, -0.01054641, -269.3558083, -0.11539863, -26.93558083, -0.3627527, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 36.79305991, 0.00772294, 44.97429254, 0.08011607, 4.49742925, 0.33302231, -149.57188118, -0.00975789, -182.8303913, -0.11048324, -18.28303913, -0.36338949, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 28504018.72032982, 0.1, 0.00133333, 0.00052083, 11876674.46680409, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.3260413133, 2322992, 0.3260413133, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 65.04633204, 0.00831396, 78.42675116, 0.06192363, 7.84267512, 0.26550512, -152.1877228, -0.00969504, -183.49364662, -0.07522837, -18.34936466, -0.27880985, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 64.91894006, 0.00823513, 78.27315388, 0.06802414, 7.82731539, 0.30772417, -224.2380443, -0.01048184, -270.36514972, -0.09055019, -27.03651497, -0.33025022, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 32902445.93162317, 0.1, 0.00133333, 0.00052083, 13709352.47150966, 0.00127345)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.37107281136000003, 2003992, 0.37107281136000003, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 82.58485618, 0.00654861, 100.93550209, 0.07706567, 10.09355021, 0.32022846, -193.88079267, -0.00757096, -236.96178764, -0.09377215, -23.69617876, -0.33693493, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 82.45799982, 0.00648722, 100.7804578, 0.07513535, 10.07804578, 0.28651385, -285.80556043, -0.00815948, -349.31256256, -0.1000918, -34.93125626, -0.3114703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 28552265.49166698, 0.125, 0.00260417, 0.00065104, 11896777.28819458, 0.00178813)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.37152346821, 2103992, 0.37152346821, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 79.85243922, 0.00631994, 97.05176609, 0.06908827, 9.70517661, 0.29396227, -187.62406397, -0.0072684, -228.03619961, -0.0839974, -22.80361996, -0.3088714, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 79.71724, 0.00626676, 96.88744646, 0.07043928, 9.68874465, 0.29000626, -276.66505424, -0.00781563, -336.25562839, -0.0937543, -33.62556284, -0.31332129, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 30519054.262317, 0.125, 0.00260417, 0.00065104, 12716272.60929875, 0.00178813)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36592526964, 2203992, 0.36592526964, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 66.23158039, 0.00861161, 80.24095704, 0.07202128, 8.0240957, 0.30114592, -154.918456, -0.01007176, -187.68697802, -0.08758476, -18.7686978, -0.3167094, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 66.08700581, 0.00852958, 80.06580189, 0.07538726, 8.00658019, 0.31152449, -228.2058938, -0.01090758, -276.47625518, -0.10044217, -27.64762552, -0.3365794, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 31519532.06650835, 0.1, 0.00133333, 0.00052083, 13133138.36104515, 0.00127345)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.37543140792, 2303992, 0.37543140792, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 62.49057688, 0.00790534, 76.52209443, 0.07079091, 7.65220944, 0.27575356, -215.02849254, -0.01030823, -263.31058907, -0.09452345, -26.33105891, -0.2994861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 62.49057688, 0.00790534, 76.52209443, 0.07619658, 7.65220944, 0.32544299, -215.02849254, -0.01030823, -263.31058907, -0.10176263, -26.33105891, -0.35100903, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 27802691.27258027, 0.1, 0.00133333, 0.00052083, 11584454.69690845, 0.00127345)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.36403571575, 2013992, 0.36403571575, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 78.1546009, 0.00589559, 95.28403615, 0.07194849, 9.52840362, 0.29472971, -270.49207138, -0.00740627, -329.77682711, -0.09586311, -32.97768271, -0.31864433, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 116.34196167, 0.00606792, 141.84106315, 0.07350701, 14.18410631, 0.2836553, -356.7719788, -0.00780175, -434.9670235, -0.09575298, -43.49670235, -0.30590127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29463273.26398423, 0.125, 0.00260417, 0.00065104, 12276363.85999343, 0.00178813)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.35944195841, 2113992, 0.35944195841, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 79.83254745, 0.00648514, 97.47727898, 0.07011479, 9.7477279, 0.28658457, -277.02626947, -0.00812513, -338.25510795, -0.09333681, -33.82551079, -0.3098066, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 118.43911044, 0.0066846, 144.61673315, 0.07525751, 14.46167332, 0.30738415, -364.87340602, -0.00857308, -445.51837477, -0.09800299, -44.55183748, -0.33012963, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 28915315.92042371, 0.125, 0.00260417, 0.00065104, 12048048.30017655, 0.00178813)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36855162108, 2213992, 0.36855162108, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 63.84857721, 0.00852688, 77.63847399, 0.07397964, 7.7638474, 0.29585862, -220.47731588, -0.01093429, -268.0955959, -0.09858744, -26.80955959, -0.32046642, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 63.84857721, 0.00852688, 77.63847399, 0.07572832, 7.7638474, 0.3119273, -220.47731588, -0.01093429, -268.0955959, -0.10092923, -26.80955959, -0.33712822, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 30360040.31521456, 0.1, 0.00133333, 0.00052083, 12650016.79800607, 0.00127345)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.37202802211, 2313992, 0.37202802211, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 61.74403806, 0.00851816, 74.41485006, 0.06559411, 7.44148501, 0.2727578, -213.25407995, -0.01076985, -257.01704786, -0.08720492, -25.70170479, -0.29436861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 61.92282994, 0.00857085, 74.63033274, 0.06338208, 7.46303327, 0.27042449, -144.80534866, -0.00995533, -174.52159994, -0.07695745, -17.45215999, -0.28399986, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 33013406.64807013, 0.1, 0.00133333, 0.00052083, 13755586.10336255, 0.00127345)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.3687937013, 2023992, 0.3687937013, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 123.71405552, 0.00656248, 150.29311014, 0.075397, 15.02931101, 0.30519637, -380.2765424, -0.00838187, -461.9761597, -0.09815297, -46.19761597, -0.32795234, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 83.28009693, 0.00643483, 101.17221303, 0.06759872, 10.1172213, 0.27631052, -195.58179631, -0.00740526, -237.60110628, -0.08217297, -23.76011063, -0.29088478, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 30664815.86864696, 0.125, 0.00260417, 0.00065104, 12777006.61193623, 0.00178813)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.37110700302, 2123992, 0.37110700302, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 128.52149889, 0.00676015, 155.95521572, 0.07377182, 15.59552157, 0.30132888, -394.94142191, -0.00862504, -479.24413565, -0.09601885, -47.92441357, -0.32357592, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 86.47910145, 0.00663068, 104.9386059, 0.06762255, 10.49386059, 0.28641673, -203.083561, -0.00762607, -246.43301578, -0.0821835, -24.64330158, -0.30097768, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 31027977.15306348, 0.125, 0.00260417, 0.00065104, 12928323.81377645, 0.00178813)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.37706913352, 2223992, 0.37706913352, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 64.40873727, 0.00862056, 78.47723784, 0.07881703, 7.84772378, 0.31242007, -222.34744596, -0.01108848, -270.91376325, -0.10509431, -27.09137633, -0.33869736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 64.58110608, 0.00870001, 78.68725637, 0.07643202, 7.86872564, 0.31254295, -151.00240878, -0.01021295, -183.98516181, -0.09300964, -18.39851618, -0.32912057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 29678784.79586918, 0.1, 0.00133333, 0.00052083, 12366160.33161216, 0.00127345)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.37366330801, 2323992, 0.37366330801, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 50.6414392, 0.01015713, 61.47856232, 0.08831507, 6.14785623, 0.36301079, -117.7745244, -0.01224925, -142.9779357, -0.10779075, -14.29779357, -0.38248648, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 50.6414392, 0.01015713, 61.47856232, 0.08682161, 6.14785623, 0.36151733, -117.7745244, -0.01224925, -142.9779357, -0.10596513, -14.29779357, -0.38066085, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 30887427.1082859, 0.07, 0.00071458, 0.00023333, 12869761.29511913, 0.00060032)
    ops.section('Aggregator', 2004991, 2004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2004992, 2004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.36403916021, 2004992, 0.36403916021, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 70.00665601, 0.00752526, 85.55342132, 0.08063748, 8.55534213, 0.32883839, -164.03842306, -0.0087513, -200.46734298, -0.09812484, -20.0467343, -0.34632576, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 70.00665601, 0.00752526, 85.55342132, 0.07506975, 8.55534213, 0.28075507, -164.03842306, -0.0087513, -200.46734298, -0.09131876, -20.0467343, -0.29700409, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 28592090.84869557, 0.1125, 0.00189844, 0.00058594, 11913371.18695649, 0.00152995)
    ops.section('Aggregator', 2104991, 2104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2104992, 2104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.36829860709, 2104992, 0.36829860709, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 71.41960381, 0.00763144, 87.14296306, 0.07366724, 8.71429631, 0.30301084, -167.38119231, -0.00886201, -204.23094332, -0.08958523, -20.42309433, -0.31892883, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 71.41960381, 0.00763144, 87.14296306, 0.07149434, 8.71429631, 0.2833393, -167.38119231, -0.00886201, -204.23094332, -0.08692904, -20.42309433, -0.298774, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 29175306.8839092, 0.1125, 0.00189844, 0.00058594, 12156377.8682955, 0.00152995)
    ops.section('Aggregator', 2204991, 2204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2204992, 2204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.37129614615000006, 2204992, 0.37129614615000006, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 52.90440539, 0.00963641, 64.84299056, 0.08103943, 6.48429906, 0.33498685, -122.78050253, -0.01183309, -150.48756161, -0.09911728, -15.04875616, -0.3530647, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 52.90440539, 0.00963641, 64.84299056, 0.08627981, 6.48429906, 0.36123874, -122.78050253, -0.01183309, -150.48756161, -0.10552321, -15.04875616, -0.38048214, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 27424479.63757662, 0.07, 0.00071458, 0.00023333, 11426866.51565692, 0.00060032)
    ops.section('Aggregator', 2304991, 2304990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2304992, 2304991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.36369068177999997, 2304992, 0.36369068177999997, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 55.35673469, 0.0107978, 67.54468267, 0.08531279, 6.75446827, 0.35056643, -128.7534565, -0.01312243, -157.10123457, -0.10421074, -15.71012346, -0.36946438, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 55.35673469, 0.0107978, 67.54468267, 0.08321476, 6.75446827, 0.3398626, -128.7534565, -0.01312243, -157.10123457, -0.10164608, -15.71012346, -0.35829391, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 29170456.52004532, 0.07, 0.00071458, 0.00023333, 12154356.88335222, 0.00060032)
    ops.section('Aggregator', 2014991, 2014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2014992, 2014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.37699765276, 2014992, 0.37699765276, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 71.95411534, 0.00729632, 86.63794944, 0.06446414, 8.66379494, 0.28217919, -168.86059064, -0.00840226, -203.32034165, -0.07828511, -20.33203416, -0.29600016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 106.59636885, 0.00753178, 128.34972358, 0.06807799, 12.83497236, 0.28943558, -249.12936267, -0.00897285, -299.96973799, -0.0829855, -29.9969738, -0.30434309, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 33268647.37268454, 0.1125, 0.00189844, 0.00058594, 13861936.40528523, 0.00152995)
    ops.section('Aggregator', 2114991, 2114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2114992, 2114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.36893674488, 2114992, 0.36893674488, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 73.29914828, 0.00706185, 88.95707996, 0.06307442, 8.895708, 0.26815896, -171.71549138, -0.00819715, -208.39681026, -0.07666781, -20.83968103, -0.28175235, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 108.93018788, 0.00727981, 132.19950928, 0.06740601, 13.21995093, 0.28268354, -253.66501413, -0.00875806, -307.85213026, -0.08225728, -30.78521303, -0.29753481, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 30986398.60199765, 0.1125, 0.00189844, 0.00058594, 12910999.41749902, 0.00152995)
    ops.section('Aggregator', 2214991, 2214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2214992, 2214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.36778226215000004, 2214992, 0.36778226215000004, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 54.07190992, 0.00977293, 65.48404661, 0.09047192, 6.54840466, 0.3627658, -125.75563612, -0.01181877, -152.29696805, -0.1104665, -15.2296968, -0.38276038, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 54.07190992, 0.00977293, 65.48404661, 0.08432839, 6.54840466, 0.33735322, -125.75563612, -0.01181877, -152.29696805, -0.10295655, -15.2296968, -0.35598138, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 31635452.81545035, 0.07, 0.00071458, 0.00023333, 13181438.67310431, 0.00060032)
    ops.section('Aggregator', 2314991, 2314990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2314992, 2314991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.36725026545, 2314992, 0.36725026545, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 53.53906025, 0.0103478, 65.11444668, 0.0883671, 6.51144467, 0.35819931, -124.56228934, -0.01252967, -151.49321841, -0.10790171, -15.14932184, -0.37773391, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 53.53906025, 0.0103478, 65.11444668, 0.08903503, 6.51144467, 0.35886724, -124.56228934, -0.01252967, -151.49321841, -0.10871819, -15.14932184, -0.3785504, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 30298453.44811296, 0.07, 0.00071458, 0.00023333, 12624355.6033804, 0.00060032)
    ops.section('Aggregator', 2024991, 2024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2024992, 2024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.37060068092000004, 2024992, 0.37060068092000004, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 108.27690748, 0.00745611, 132.43435539, 0.07559742, 13.24343554, 0.29748576, -252.05364888, -0.00904474, -308.28884283, -0.09234177, -30.82888428, -0.31423011, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 72.91247617, 0.00722592, 89.17983535, 0.0727143, 8.91798353, 0.30031182, -170.7130253, -0.00844292, -208.80047268, -0.08849695, -20.88004727, -0.31609447, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 28267174.13862593, 0.1125, 0.00189844, 0.00058594, 11777989.22442747, 0.00152995)
    ops.section('Aggregator', 2124991, 2124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2124992, 2124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.36882279103000004, 2124992, 0.36882279103000004, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 105.51420048, 0.00714078, 128.9234631, 0.08005776, 12.89234631, 0.31513381, -245.46246999, -0.00865651, -299.92049931, -0.09779139, -29.99204993, -0.33286744, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 71.00274671, 0.00692373, 86.75533676, 0.0738031, 8.67553368, 0.28963284, -166.18908038, -0.00808586, -203.05960407, -0.08984028, -20.30596041, -0.30567002, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 28659218.63517284, 0.1125, 0.00189844, 0.00058594, 11941341.09798869, 0.00152995)
    ops.section('Aggregator', 2224991, 2224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2224992, 2224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.36318302505000005, 2224992, 0.36318302505000005, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 52.74025932, 0.01005645, 64.12586923, 0.08042269, 6.41258692, 0.34366089, -122.7027231, -0.01218158, -149.19188637, -0.09819839, -14.91918864, -0.36143659, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 52.74025932, 0.01005645, 64.12586923, 0.07938675, 6.41258692, 0.33352477, -122.7027231, -0.01218158, -149.19188637, -0.09693204, -14.91918864, -0.35107006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 30386432.95166048, 0.07, 0.00071458, 0.00023333, 12661013.72985854, 0.00060032)
    ops.section('Aggregator', 2324991, 2324990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2324992, 2324991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.36704967182000003, 2324992, 0.36704967182000003, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)
