import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 62.51877112, 0.00721918, 76.23381385, 0.05139339, 7.62338138, 0.25137015, -82.72487187, -0.00746914, -100.87262384, -0.05459724, -10.08726238, -0.254574, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 62.51877112, 0.00721918, 76.23381385, 0.05125249, 7.62338138, 0.24971957, -82.72487187, -0.00746914, -100.87262384, -0.05444692, -10.08726238, -0.252914, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29404763.2611277, 0.1125, 0.00189844, 0.00058594, 12251984.69213654, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32754243923000004, 1001992, 0.32754243923000004, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 61.40895426, 0.00697546, 74.86604587, 0.06330178, 7.48660459, 0.31677715, -81.2519213, -0.00721827, -99.05737918, -0.06731109, -9.90573792, -0.32078646, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 61.40895426, 0.00697546, 74.86604587, 0.06332429, 7.48660459, 0.31704008, -81.2519213, -0.00721827, -99.05737918, -0.06733511, -9.90573792, -0.3210509, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29473377.20119143, 0.1125, 0.00189844, 0.00058594, 12280573.83382976, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25630243166000005, 1101992, 0.25630243166000005, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 62.10742856, 0.0070406, 75.89021257, 0.05382317, 7.58902126, 0.25875647, -82.16626911, -0.00729031, -100.40047983, -0.05720121, -10.04004798, -0.26213451, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 62.10742856, 0.0070406, 75.89021257, 0.05388463, 7.58902126, 0.2594571, -82.16626911, -0.00729031, -100.40047983, -0.05726677, -10.04004798, -0.26283924, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 28640798.65266505, 0.1125, 0.00189844, 0.00058594, 11933666.10527711, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32549552376999996, 1201992, 0.32549552376999996, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 105.34843655, 0.00753056, 127.84580244, 0.06715089, 12.78458024, 0.24574601, -142.55511962, -0.00797333, -172.99804588, -0.07202235, -17.29980459, -0.25061747, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 105.34843655, 0.00753056, 127.84580244, 0.06683437, 12.78458024, 0.24318856, -142.55511962, -0.00797333, -172.99804588, -0.07168231, -17.29980459, -0.2480365, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 31003207.95646978, 0.1125, 0.00189844, 0.00058594, 12918003.31519574, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36623393444, 1011992, 0.36623393444, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 108.2855645, 0.00745396, 132.04954562, 0.08136766, 13.20495456, 0.29681153, -146.39773839, -0.00791059, -178.52568737, -0.0873147, -17.85256874, -0.30275858, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 108.2855645, 0.00745396, 132.04954562, 0.0813712, 13.20495456, 0.29683962, -146.39773839, -0.00791059, -178.52568737, -0.08731852, -17.85256874, -0.30278693, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29380885.70705761, 0.1125, 0.00189844, 0.00058594, 12242035.71127401, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.29946440611, 1111992, 0.29946440611, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 106.18468977, 0.00761152, 129.60451745, 0.07007015, 12.96045175, 0.25030277, -143.63483394, -0.00807575, -175.31457108, -0.0751739, -17.53145711, -0.25540652, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 106.18468977, 0.00761152, 129.60451745, 0.07004763, 12.96045175, 0.25012617, -143.63483394, -0.00807575, -175.31457108, -0.07514971, -17.53145711, -0.25522825, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29055181.10774438, 0.1125, 0.00189844, 0.00058594, 12106325.46156016, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36741967713, 1211992, 0.36741967713, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 144.3492701, 0.00829022, 175.73397735, 0.06917913, 17.57339774, 0.2450142, -163.34699737, -0.00848499, -198.86222852, -0.07115065, -19.88622285, -0.24698573, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 144.3492701, 0.00829022, 175.73397735, 0.06925377, 17.57339774, 0.24560054, -163.34699737, -0.00848499, -198.86222852, -0.07122747, -19.88622285, -0.24757424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29962308.92722896, 0.1125, 0.00189844, 0.00058594, 12484295.3863454, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.37114808761, 1021992, 0.37114808761, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 145.37411213, 0.00804861, 177.66098078, 0.08495749, 17.76609808, 0.30090875, -164.46154372, -0.008246, -200.98763617, -0.08739909, -20.09876362, -0.30335035, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 145.37411213, 0.00804861, 177.66098078, 0.08507102, 17.76609808, 0.30177924, -164.46154372, -0.008246, -200.98763617, -0.08751594, -20.09876362, -0.30422416, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 28586029.87091195, 0.1125, 0.00189844, 0.00058594, 11910845.77954665, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.3010291606, 1121992, 0.3010291606, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 143.77362821, 0.00791749, 173.96509128, 0.06830128, 17.39650913, 0.24827592, -162.68910075, -0.00809895, -196.85268164, -0.07024475, -19.68526816, -0.25021939, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 143.77362821, 0.00791749, 173.96509128, 0.06802165, 17.39650913, 0.24602558, -162.68910075, -0.00809895, -196.85268164, -0.06995696, -19.68526816, -0.24796089, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 31895937.0559076, 0.1125, 0.00189844, 0.00058594, 13289973.77329483, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.36747516899, 1221992, 0.36747516899, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 61.90754688, 0.00732486, 75.52076766, 0.06546572, 7.55207677, 0.26900142, -92.42723046, -0.00775484, -112.75160703, -0.07162544, -11.2751607, -0.27516114, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 61.90754688, 0.00732486, 75.52076766, 0.06506622, 7.55207677, 0.26530005, -92.42723046, -0.00775484, -112.75160703, -0.07118657, -11.2751607, -0.2714204, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 29251868.45302419, 0.1125, 0.00189844, 0.00058594, 12188278.52209341, 0.00152995)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32785851982, 1031992, 0.32785851982, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 62.56683784, 0.00704707, 75.95345555, 0.07630434, 7.59534556, 0.32779739, -93.41902656, -0.00745442, -113.40668838, -0.08353694, -11.34066884, -0.33502999, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 62.56683784, 0.00704707, 75.95345555, 0.07697583, 7.59534556, 0.33429141, -93.41902656, -0.00745442, -113.40668838, -0.0842746, -11.34066884, -0.34159019, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 30897886.44567792, 0.1125, 0.00189844, 0.00058594, 12874119.3523658, 0.00152995)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25840369921, 1131992, 0.25840369921, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 62.25727972, 0.0073768, 76.09288714, 0.0643189, 7.60928871, 0.26303734, -92.9404769, -0.00781577, -113.59489606, -0.07036947, -11.35948961, -0.26908791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 62.25727972, 0.0073768, 76.09288714, 0.06417355, 7.60928871, 0.26169087, -92.9404769, -0.00781577, -113.59489606, -0.0702098, -11.35948961, -0.26772711, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 28543148.68284142, 0.1125, 0.00189844, 0.00058594, 11892978.61785059, 0.00152995)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32859178222999996, 1231992, 0.32859178222999996, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 63.49983368, 0.00709123, 77.4057974, 0.05130357, 7.74057974, 0.25162066, -84.00884575, -0.00733956, -102.40612168, -0.05450834, -10.24061217, -0.25482544, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 63.49983368, 0.00709123, 77.4057974, 0.05164084, 7.74057974, 0.25560175, -84.00884575, -0.00733956, -102.40612168, -0.05486817, -10.24061217, -0.25882908, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29515894.12542832, 0.1125, 0.00189844, 0.00058594, 12298289.21892847, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32748455102999996, 1002992, 0.32748455102999996, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 62.69696832, 0.00742551, 76.3825507, 0.06136201, 7.63825507, 0.3100186, -82.96083759, -0.00767813, -101.06964585, -0.06522132, -10.10696459, -0.31387791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 62.69696832, 0.00742551, 76.3825507, 0.06115358, 7.63825507, 0.30753689, -82.96083759, -0.00767813, -101.06964585, -0.06499895, -10.10696459, -0.31138226, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29719833.15542535, 0.1125, 0.00189844, 0.00058594, 12383263.81476056, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.26148367821, 1102992, 0.26148367821, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 61.91629223, 0.00717587, 75.64813913, 0.05296761, 7.56481391, 0.25552719, -81.92247415, -0.00742785, -100.09130876, -0.05628165, -10.00913088, -0.25884123, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 61.91629223, 0.00717587, 75.64813913, 0.0526631, 7.56481391, 0.25204198, -81.92247415, -0.00742785, -100.09130876, -0.05595677, -10.00913088, -0.25533565, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 28683315.10387636, 0.1125, 0.00189844, 0.00058594, 11951381.29328182, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32645173790000004, 1202992, 0.32645173790000004, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.87076629, 0.00699403, 76.60260551, 0.06464372, 7.66026055, 0.26760539, -93.83364894, -0.00740922, -114.32820717, -0.07074025, -11.43282072, -0.27370192, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 62.86466754, 0.00697096, 76.59517472, 0.06473437, 7.65951747, 0.26469933, -113.70030865, -0.00760283, -138.53401834, -0.07395639, -13.85340183, -0.27392135, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29682098.55924937, 0.1125, 0.00189844, 0.00058594, 12367541.0663539, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32612526099, 1012992, 0.32612526099, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 62.29163016, 0.0070089, 75.87074507, 0.07923967, 7.58707451, 0.33284928, -112.70305867, -0.00763959, -137.27149235, -0.090612, -13.72714924, -0.3442216, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 62.29163016, 0.0070089, 75.87074507, 0.07910722, 7.58707451, 0.33161503, -112.70305867, -0.00763959, -137.27149235, -0.09045985, -13.72714924, -0.34296766, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29801810.79270922, 0.1125, 0.00189844, 0.00058594, 12417421.16362884, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25787333784, 1112992, 0.25787333784, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 62.25267818, 0.00703049, 75.87179525, 0.06495595, 7.58717953, 0.26705923, -112.63188344, -0.00766517, -137.27253911, -0.07420487, -13.72725391, -0.27630815, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 62.27055926, 0.00705223, 75.89358821, 0.06481465, 7.58935882, 0.26953442, -92.95652399, -0.0074694, -113.29277009, -0.07092426, -11.32927701, -0.27564403, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29579516.87356948, 0.1125, 0.00189844, 0.00058594, 12324798.69732062, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32599600815, 1212992, 0.32599600815, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 108.0535473, 0.00749033, 131.58621424, 0.06967568, 13.15862142, 0.25165058, -146.12009199, -0.00794412, -177.94316067, -0.07474868, -17.79431607, -0.25672359, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 108.0535473, 0.00749033, 131.58621424, 0.06883744, 13.15862142, 0.24504744, -146.12009199, -0.00794412, -177.94316067, -0.07384818, -17.79431607, -0.25005818, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29859843.40506709, 0.1125, 0.00189844, 0.00058594, 12441601.41877795, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36777578627999996, 1022992, 0.36777578627999996, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 106.10336467, 0.00759397, 129.55195494, 0.08229033, 12.95519549, 0.29808297, -143.51785221, -0.00805855, -175.2349549, -0.08830347, -17.52349549, -0.30409611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 106.10336467, 0.00759397, 129.55195494, 0.08278119, 12.95519549, 0.30195277, -143.51785221, -0.00805855, -175.2349549, -0.08883079, -17.52349549, -0.30800237, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 28922633.07929346, 0.1125, 0.00189844, 0.00058594, 12051097.11637228, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.29914128198, 1122992, 0.29914128198, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 108.80734349, 0.0075443, 131.65936486, 0.06604802, 13.16593649, 0.24530011, -147.2087206, -0.00798444, -178.12590616, -0.0708339, -17.81259062, -0.250086, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 108.80734349, 0.0075443, 131.65936486, 0.06597727, 13.16593649, 0.24471562, -147.2087206, -0.00798444, -178.12590616, -0.0707579, -17.81259062, -0.24949625, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 31888706.83870954, 0.1125, 0.00189844, 0.00058594, 13286961.18279564, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36934287689, 1222992, 0.36934287689, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 62.24119768, 0.0071503, 75.76119271, 0.05005809, 7.57611927, 0.24776154, -82.36153915, -0.00739521, -100.25206249, -0.05317221, -10.02520625, -0.25087566, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 62.24119768, 0.0071503, 75.76119271, 0.05058432, 7.57611927, 0.25408786, -82.36153915, -0.00739521, -100.25206249, -0.05373363, -10.02520625, -0.25723716, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 30018836.87722385, 0.1125, 0.00189844, 0.00058594, 12507848.69884327, 0.00152995)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32673354653000003, 1032992, 0.32673354653000003, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 62.43628359, 0.00711506, 76.05889531, 0.06144197, 7.60588953, 0.31070119, -82.61514229, -0.00736098, -100.64046253, -0.06532069, -10.06404625, -0.31457991, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 62.43628359, 0.00711506, 76.05889531, 0.06178377, 7.60588953, 0.314779, -82.61514229, -0.00736098, -100.64046253, -0.06568534, -10.06404625, -0.31868057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 29747477.35405581, 0.1125, 0.00189844, 0.00058594, 12394782.23085659, 0.00152995)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25860971706999997, 1132992, 0.25860971706999997, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 62.41408046, 0.00717336, 76.39594574, 0.05252457, 7.63959457, 0.25252882, -82.57168209, -0.00743013, -101.06920904, -0.05581394, -10.1069209, -0.25581819, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 62.41408046, 0.00717336, 76.39594574, 0.05281289, 7.63959457, 0.25584649, -82.57168209, -0.00743013, -101.06920904, -0.05612154, -10.1069209, -0.25915514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 27973712.98670419, 0.1125, 0.00189844, 0.00058594, 11655713.74446008, 0.00152995)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32687261403999995, 1232992, 0.32687261403999995, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 63.44022298, 0.00721006, 77.45242901, 0.05013782, 7.7452429, 0.24686965, -63.44022298, -0.00721006, -77.45242901, -0.05013782, -7.7452429, -0.24686965, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 63.44022298, 0.00721006, 77.45242901, 0.05052627, 7.7452429, 0.25150722, -63.44022298, -0.00721006, -77.45242901, -0.05052627, -7.7452429, -0.25150722, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 28960425.0566116, 0.1125, 0.00189844, 0.00058594, 12066843.77358817, 0.00152995)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32815475679, 1003992, 0.32815475679, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 60.44972111, 0.0073339, 73.87064688, 0.06449423, 7.38706469, 0.31947894, -60.44972111, -0.0073339, -73.87064688, -0.06449423, -7.38706469, -0.31947894, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 60.44972111, 0.0073339, 73.87064688, 0.06435141, 7.38706469, 0.31782748, -60.44972111, -0.0073339, -73.87064688, -0.06435141, -7.38706469, -0.31782748, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 28609953.48184167, 0.1125, 0.00189844, 0.00058594, 11920813.95076736, 0.00152995)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25792936944, 1103992, 0.25792936944, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 62.08060765, 0.007201, 75.23932481, 0.05064945, 7.52393248, 0.25437666, -62.08060765, -0.007201, -75.23932481, -0.05064945, -7.52393248, -0.25437666, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 62.08060765, 0.007201, 75.23932481, 0.05056842, 7.52393248, 0.25339556, -62.08060765, -0.007201, -75.23932481, -0.05056842, -7.52393248, -0.25339556, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 31409092.63811379, 0.1125, 0.00189844, 0.00058594, 13087121.93254741, 0.00152995)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32693238371, 1203992, 0.32693238371, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 62.80029447, 0.0071956, 76.45089498, 0.04942796, 7.6450895, 0.24630611, -62.80029447, -0.0071956, -76.45089498, -0.04942796, -7.6450895, -0.24630611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 62.77699424, 0.00717275, 76.42253009, 0.05040853, 7.64225301, 0.25453435, -83.06890013, -0.0074192, -101.12519079, -0.05354612, -10.11251908, -0.25767193, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29978171.96272589, 0.1125, 0.00189844, 0.00058594, 12490904.98446912, 0.00152995)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32748778717, 1013992, 0.32748778717, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 60.41002516, 0.0070984, 73.53505453, 0.06418816, 7.35350545, 0.32133228, -79.93809264, -0.00733926, -97.30590222, -0.06824658, -9.73059022, -0.32539069, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 60.41002516, 0.0070984, 73.53505453, 0.06401251, 7.35350545, 0.31928385, -79.93809264, -0.00733926, -97.30590222, -0.06805918, -9.73059022, -0.32333052, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 30005924.03513545, 0.1125, 0.00189844, 0.00058594, 12502468.3479731, 0.00152995)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25632809372000004, 1113992, 0.25632809372000004, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 62.02007418, 0.00715172, 75.35303951, 0.04981092, 7.53530395, 0.24821784, -82.07383497, -0.00739322, -99.71792216, -0.052905, -9.97179222, -0.25131193, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 62.05126987, 0.00717259, 75.39094159, 0.0497841, 7.53909416, 0.25157182, -62.05126987, -0.00717259, -75.39094159, -0.0497841, -7.53909416, -0.25157182, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 30628780.99941221, 0.1125, 0.00189844, 0.00058594, 12761992.08308842, 0.00152995)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32657531497000003, 1213992, 0.32657531497000003, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 62.94170207, 0.0072795, 76.82456047, 0.05238232, 7.68245605, 0.25530208, -62.94170207, -0.0072795, -76.82456047, -0.05238232, -7.68245605, -0.25530208, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 62.91558442, 0.00725595, 76.79268213, 0.05240318, 7.67926821, 0.25185957, -83.24671564, -0.00750922, -101.60818867, -0.05567541, -10.16081887, -0.2551318, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 29052347.80762576, 0.1125, 0.00189844, 0.00058594, 12105144.91984406, 0.00152995)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.32823468760999996, 1023992, 0.32823468760999996, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 61.8442482, 0.00718453, 75.40457567, 0.06273637, 7.54045757, 0.31445654, -81.8333136, -0.00743249, -99.77655913, -0.06669903, -9.97765591, -0.31841921, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 61.8442482, 0.00718453, 75.40457567, 0.06308773, 7.54045757, 0.31860095, -81.8333136, -0.00743249, -99.77655913, -0.06707389, -9.97765591, -0.32258711, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 29436518.42678393, 0.1125, 0.00189844, 0.00058594, 12265216.01115997, 0.00152995)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.25853330741, 1123992, 0.25853330741, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 61.65729495, 0.00734647, 75.27828767, 0.05109409, 7.52782877, 0.24893898, -81.57993584, -0.00759994, -99.60212954, -0.05427292, -9.96021295, -0.25211782, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 61.70117516, 0.00736686, 75.33186166, 0.05122839, 7.53318617, 0.25422748, -61.70117516, -0.00736686, -75.33186166, -0.05122839, -7.53318617, -0.25422748, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 28947756.81237625, 0.1125, 0.00189844, 0.00058594, 12061565.33849011, 0.00152995)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.32761339949, 1223992, 0.32761339949, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 62.20291684, 0.00721027, 75.69063912, 0.04984135, 7.56906391, 0.24805663, -62.20291684, -0.00721027, -75.69063912, -0.04984135, -7.56906391, -0.24805663, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 62.20291684, 0.00721027, 75.69063912, 0.05019182, 7.56906391, 0.25229422, -62.20291684, -0.00721027, -75.69063912, -0.05019182, -7.56906391, -0.25229422, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 30125638.38310982, 0.1125, 0.00189844, 0.00058594, 12552349.32629576, 0.00152995)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32699612366999997, 1033992, 0.32699612366999997, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 63.29121541, 0.00710762, 76.81942152, 0.0596937, 7.68194215, 0.30902699, -63.29121541, -0.00710762, -76.81942152, -0.0596937, -7.68194215, -0.30902699, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 63.29121541, 0.00710762, 76.81942152, 0.05979945, 7.68194215, 0.31032376, -63.29121541, -0.00710762, -76.81942152, -0.05979945, -7.68194215, -0.31032376, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 30953018.86150462, 0.1125, 0.00189844, 0.00058594, 12897091.19229359, 0.00152995)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25936121128, 1133992, 0.25936121128, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 62.80615733, 0.00721761, 76.4657492, 0.04960606, 7.64657492, 0.24688007, -62.80615733, -0.00721761, -76.4657492, -0.04960606, -7.64657492, -0.24688007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 62.80615733, 0.00721761, 76.4657492, 0.0496034, 7.64657492, 0.24684807, -62.80615733, -0.00721761, -76.4657492, -0.0496034, -7.64657492, -0.24684807, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 29943815.65197096, 0.1125, 0.00189844, 0.00058594, 12476589.8549879, 0.00152995)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32767704432, 1233992, 0.32767704432, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 80.56691338, 0.01036291, 98.19721538, 0.08642874, 9.81972154, 0.30251635, -108.73011759, -0.011093, -132.52331916, -0.09280911, -13.25233192, -0.30889672, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 80.56691338, 0.01036291, 98.19721538, 0.08618521, 9.81972154, 0.30063538, -108.73011759, -0.011093, -132.52331916, -0.09254749, -13.25233192, -0.30699767, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29563251.87928787, 0.0875, 0.00089323, 0.00045573, 12318021.61636995, 0.0010204)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.30050315926000004, 6200992, 0.30050315926000004, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 66.9674291, 0.01259089, 81.56832942, 0.09026213, 8.15683294, 0.30678448, -90.23161653, -0.01355986, -109.90480477, -0.09700064, -10.99048048, -0.31352299, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 66.9674291, 0.01259089, 81.56832942, 0.09112244, 8.15683294, 0.31337697, -90.23161653, -0.01355986, -109.90480477, -0.09792485, -10.99048048, -0.32017938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29791260.15565159, 0.075, 0.0005625, 0.00039062, 12413025.06485483, 0.00077515)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30012491678, 6201992, 0.30012491678, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 39.91351636, 0.01200169, 48.66482595, 0.08688883, 4.86648259, 0.34282709, -59.31259037, -0.01289952, -72.31727871, -0.09516673, -7.23172787, -0.35110499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 39.91351636, 0.01200169, 48.66482595, 0.08582515, 4.86648259, 0.33322399, -59.31259037, -0.01289952, -72.31727871, -0.09399822, -7.23172787, -0.34139706, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 29439133.55981493, 0.075, 0.0005625, 0.00039062, 12266305.64992289, 0.00077515)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.26153553356, 6202992, 0.26153553356, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 62.10935068, 0.00699324, 75.6663634, 0.06394038, 7.56663634, 0.2637582, -112.37173553, -0.0076234, -136.89984655, -0.0730393, -13.68998466, -0.27285712, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 62.10935068, 0.00699324, 75.6663634, 0.06378885, 7.56663634, 0.26234771, -112.37173553, -0.0076234, -136.89984655, -0.07286523, -13.68998466, -0.27142409, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29721225.18518778, 0.1125, 0.00189844, 0.00058594, 12383843.82716158, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32553875087, 2001992, 0.32553875087, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 186.91043007, 0.00705841, 228.24919131, 0.07487478, 22.82491913, 0.29611971, -251.99868717, -0.00758907, -307.73294211, -0.08044294, -30.77329421, -0.30168787, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 186.91043007, 0.00705841, 228.24919131, 0.0745667, 22.82491913, 0.2934349, -251.99868717, -0.00758907, -307.73294211, -0.08011198, -30.77329421, -0.29898017, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28870697.85689057, 0.125, 0.00260417, 0.00065104, 12029457.44037107, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41111066106, 2101992, 0.41111066106, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 188.1858381, 0.00709569, 229.70348511, 0.07444141, 22.97034851, 0.29516909, -253.7231673, -0.00762759, -309.69969031, -0.07997585, -30.96996903, -0.30070353, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 188.1858381, 0.00709569, 229.70348511, 0.07387033, 22.97034851, 0.29018395, -253.7231673, -0.00762759, -309.69969031, -0.07936235, -30.96996903, -0.29567596, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29036296.76830189, 0.125, 0.00260417, 0.00065104, 12098456.98679245, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41243941726000005, 2201992, 0.41243941726000005, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.23483788, 0.00710803, 75.84893048, 0.06496161, 7.58489305, 0.26707225, -112.61894178, -0.00774716, -137.25473668, -0.0742043, -13.72547367, -0.27631495, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 62.23483788, 0.00710803, 75.84893048, 0.06447541, 7.58489305, 0.26258015, -112.61894178, -0.00774716, -137.25473668, -0.0736458, -13.72547367, -0.27175054, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29584701.98761018, 0.1125, 0.00189844, 0.00058594, 12326959.16150424, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32664091487, 2301992, 0.32664091487, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 61.91420012, 0.00717148, 75.52457833, 0.06347005, 7.55245783, 0.2607346, -112.04571073, -0.00781727, -136.67632044, -0.07248815, -13.66763204, -0.26975269, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 61.91420012, 0.00717148, 75.52457833, 0.06423214, 7.55245783, 0.26788971, -112.04571073, -0.00781727, -136.67632044, -0.07336356, -13.66763204, -0.27702114, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29272373.29453952, 0.1125, 0.00189844, 0.00058594, 12196822.20605813, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32680043337000003, 2011992, 0.32680043337000003, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 188.30305726, 0.00717569, 229.42346992, 0.07186463, 22.94234699, 0.28725292, -253.99450767, -0.00770538, -309.46019751, -0.07719951, -30.94601975, -0.2925878, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 188.30305726, 0.00717569, 229.42346992, 0.07205023, 22.94234699, 0.28890734, -253.99450767, -0.00770538, -309.46019751, -0.0773989, -30.94601975, -0.29425601, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29693561.61975994, 0.125, 0.00260417, 0.00065104, 12372317.34156664, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41387897804, 2111992, 0.41387897804, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 183.94704599, 0.00694514, 223.78436425, 0.07240881, 22.37843643, 0.29078973, -248.10765834, -0.00745397, -301.84020781, -0.07778039, -30.18402078, -0.2961613, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 183.94704599, 0.00694514, 223.78436425, 0.07313615, 22.37843643, 0.29731653, -248.10765834, -0.00745397, -301.84020781, -0.07856176, -30.18402078, -0.30274214, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 30198563.37557106, 0.125, 0.00260417, 0.00065104, 12582734.73982128, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40812061132000005, 2211992, 0.40812061132000005, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 61.82017484, 0.00722206, 75.41988219, 0.0661053, 7.54198822, 0.2700404, -111.88036521, -0.00787108, -136.49272242, -0.075511, -13.64927224, -0.2794461, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 61.82017484, 0.00722206, 75.41988219, 0.06570912, 7.54198822, 0.26640446, -111.88036521, -0.00787108, -136.49272242, -0.0750559, -13.64927224, -0.27575125, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29224634.95614932, 0.1125, 0.00189844, 0.00058594, 12176931.23172889, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32711388609000003, 2311992, 0.32711388609000003, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 61.75952367, 0.00717929, 75.33208619, 0.06341974, 7.53320862, 0.26055635, -111.7692487, -0.00782473, -136.3321829, -0.07242884, -13.63321829, -0.26956545, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 61.75952367, 0.00717929, 75.33208619, 0.0634351, 7.53320862, 0.2606994, -111.7692487, -0.00782473, -136.3321829, -0.07244648, -13.63321829, -0.26971078, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 29290553.93719115, 0.1125, 0.00189844, 0.00058594, 12204397.47382965, 0.00152995)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.32669986034, 2021992, 0.32669986034, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 183.24043681, 0.00688062, 222.49155731, 0.0731418, 22.24915573, 0.2963213, -247.17236615, -0.00737939, -300.11806142, -0.07856256, -30.01180614, -0.30174205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 183.24043681, 0.00688062, 222.49155731, 0.07266906, 22.24915573, 0.29208999, -247.17236615, -0.00737939, -300.11806142, -0.0780547, -30.01180614, -0.29747563, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 30832885.56886641, 0.125, 0.00260417, 0.00065104, 12847035.65369434, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.40693174351, 2121992, 0.40693174351, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 185.48703951, 0.00705583, 226.41187279, 0.07565489, 22.64118728, 0.29969296, -250.13440757, -0.00758369, -305.32267816, -0.0812784, -30.53226782, -0.30531647, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 185.48703951, 0.00705583, 226.41187279, 0.07587594, 22.64118728, 0.30163026, -250.13440757, -0.00758369, -305.32267816, -0.08151586, -30.53226782, -0.30727019, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 29032095.95406012, 0.125, 0.00260417, 0.00065104, 12096706.64752505, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.41030595849, 2221992, 0.41030595849, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 62.26859041, 0.00720861, 75.79631582, 0.06270148, 7.57963158, 0.26008201, -112.70712487, -0.00784823, -137.19251996, -0.0715936, -13.719252, -0.26897413, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 62.26859041, 0.00720861, 75.79631582, 0.06309827, 7.57963158, 0.26384307, -112.70712487, -0.00784823, -137.19251996, -0.0720494, -13.719252, -0.2727942, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 30010875.2660428, 0.1125, 0.00189844, 0.00058594, 12504531.36085116, 0.00152995)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32756530496, 2321992, 0.32756530496, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 63.02813482, 0.00706409, 76.87733503, 0.06307197, 7.6877335, 0.26087011, -94.06977714, -0.00748558, -114.73977129, -0.06901298, -11.47397713, -0.26681113, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 63.01825918, 0.00704097, 76.86528941, 0.0636006, 7.68652894, 0.2621329, -113.98208124, -0.0076825, -139.02741485, -0.07265326, -13.90274149, -0.27118557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29300624.64084446, 0.1125, 0.00189844, 0.00058594, 12208593.60035186, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32685680142, 2002992, 0.32685680142, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 163.75486018, 0.00799411, 199.64981892, 0.07535919, 19.96498189, 0.29369672, -220.6472692, -0.00862608, -269.01300696, -0.08099513, -26.9013007, -0.29933266, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 163.75486018, 0.00799411, 199.64981892, 0.07603295, 19.96498189, 0.29958614, -220.6472692, -0.00862608, -269.01300696, -0.08171895, -26.9013007, -0.30527213, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29455832.27163562, 0.1125, 0.00189844, 0.00058594, 12273263.44651484, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.40949116104, 2102992, 0.40949116104, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 168.81005008, 0.00801587, 205.72554224, 0.07641276, 20.57255422, 0.2992721, -227.32977763, -0.00865165, -277.04240209, -0.08212917, -27.70424021, -0.3049885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 168.81005008, 0.00801587, 205.72554224, 0.07612202, 20.57255422, 0.29674075, -227.32977763, -0.00865165, -277.04240209, -0.08181683, -27.70424021, -0.30243556, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29605659.42826357, 0.1125, 0.00189844, 0.00058594, 12335691.42844316, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.4130772172, 2202992, 0.4130772172, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 61.91357768, 0.00724035, 75.37164306, 0.06288326, 7.53716431, 0.26167996, -92.44594097, -0.00766106, -112.54078228, -0.06878753, -11.25407823, -0.26758423, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 61.87727867, 0.00722169, 75.3274538, 0.06381612, 7.53274538, 0.26676513, -112.00197983, -0.00786106, -136.34768921, -0.0728718, -13.63476892, -0.27582081, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29977241.52617158, 0.1125, 0.00189844, 0.00058594, 12490517.30257149, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32724457128, 2302992, 0.32724457128, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 60.55691568, 0.00712611, 73.83210498, 0.06483109, 7.3832105, 0.26570691, -109.6016778, -0.0077619, -133.62838067, -0.07404833, -13.36283807, -0.27492416, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 60.55691568, 0.00712611, 73.83210498, 0.0647626, 7.3832105, 0.2650734, -109.6016778, -0.0077619, -133.62838067, -0.07396967, -13.36283807, -0.27428047, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29450300.73866885, 0.1125, 0.00189844, 0.00058594, 12270958.64111202, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32496177043, 2012992, 0.32496177043, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 169.95676418, 0.00814265, 207.05287515, 0.07508606, 20.70528751, 0.29453831, -228.9302875, -0.00878575, -278.89842727, -0.08070181, -27.88984273, -0.30015406, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 169.95676418, 0.00814265, 207.05287515, 0.07518926, 20.70528751, 0.29544484, -228.9302875, -0.00878575, -278.89842727, -0.08081268, -27.88984273, -0.30106826, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29723669.94592623, 0.1125, 0.00189844, 0.00058594, 12384862.47746926, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.41550857104, 2112992, 0.41550857104, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 164.54464874, 0.00804024, 200.74635165, 0.07678527, 20.07463517, 0.29861212, -221.69939155, -0.00867868, -270.47579097, -0.08253019, -27.0475791, -0.30435704, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 164.54464874, 0.00804024, 200.74635165, 0.07692, 20.07463517, 0.29977955, -221.69939155, -0.00867868, -270.47579097, -0.08267494, -27.0475791, -0.30553448, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29217756.98807164, 0.1125, 0.00189844, 0.00058594, 12174065.41169652, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.41052913501, 2212992, 0.41052913501, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 62.46637765, 0.00723475, 75.92066163, 0.06201204, 7.59206616, 0.25908892, -113.07849333, -0.00787016, -137.43383805, -0.07079353, -13.7433838, -0.2678704, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 62.46637765, 0.00723475, 75.92066163, 0.06244178, 7.59206616, 0.26320589, -113.07849333, -0.00787016, -137.43383805, -0.07128717, -13.7433838, -0.27205128, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 30520251.128398, 0.1125, 0.00189844, 0.00058594, 12716771.30349917, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32804534773, 2312992, 0.32804534773, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 62.47632603, 0.00715807, 75.82698527, 0.0634646, 7.58269853, 0.2658167, -113.10080711, -0.00778369, -137.26948719, -0.07246371, -13.72694872, -0.27481582, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 62.50647205, 0.00717708, 75.86357324, 0.06281078, 7.58635732, 0.26335662, -93.34161342, -0.00758889, -113.28792195, -0.06870525, -11.32879219, -0.26925109, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 30967024.59966699, 0.1125, 0.00189844, 0.00058594, 12902926.91652791, 0.00152995)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32745581417, 2022992, 0.32745581417, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 167.40652778, 0.00819939, 203.98427845, 0.07617563, 20.39842784, 0.29830725, -225.59665878, -0.00884455, -274.88875298, -0.08187017, -27.4888753, -0.30400179, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 167.40652778, 0.00819939, 203.98427845, 0.07526762, 20.39842784, 0.29042522, -225.59665878, -0.00884455, -274.88875298, -0.08089472, -27.4888753, -0.29605231, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 29658427.53759028, 0.1125, 0.00189844, 0.00058594, 12357678.14066262, 0.00152995)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.41456847137, 2122992, 0.41456847137, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 164.9176772, 0.0079932, 200.79454694, 0.07466084, 20.07945469, 0.29289287, -222.21306895, -0.00862037, -270.55421385, -0.0802402, -27.05542138, -0.29847222, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 164.9176772, 0.0079932, 200.79454694, 0.07491289, 20.07945469, 0.29510707, -222.21306895, -0.00862037, -270.55421385, -0.08051096, -27.05542138, -0.30070515, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 29928124.38151863, 0.1125, 0.00189844, 0.00058594, 12470051.82563276, 0.00152995)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.41037210859, 2222992, 0.41037210859, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 62.23237509, 0.00712141, 75.78684044, 0.06521507, 7.57868404, 0.26877774, -112.62570393, -0.00775785, -137.15604204, -0.07449078, -13.7156042, -0.27805344, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 62.25887975, 0.00714184, 75.81911793, 0.06469204, 7.58191179, 0.26769651, -92.95395848, -0.00756038, -113.19971012, -0.07078211, -11.31997101, -0.27378659, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 29855053.11811835, 0.1125, 0.00189844, 0.00058594, 12439605.46588264, 0.00152995)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32677873356, 2322992, 0.32677873356, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 63.18974351, 0.00716989, 77.02885034, 0.05243275, 7.70288503, 0.25670434, -63.18974351, -0.00716989, -77.02885034, -0.05243275, -7.70288503, -0.25670434, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 63.17596856, 0.00714537, 77.01205855, 0.05228715, 7.70120586, 0.25133543, -83.58821431, -0.00739434, -101.89476476, -0.05555471, -10.18947648, -0.25460299, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 29511086.14089554, 0.1125, 0.00189844, 0.00058594, 12296285.89203981, 0.00152995)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32761843033000004, 2003992, 0.32761843033000004, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 108.81794347, 0.00751016, 132.6753717, 0.0685521, 13.26753717, 0.24653139, -147.12686692, -0.00796936, -179.3832077, -0.07354558, -17.93832077, -0.25152487, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 108.81794347, 0.00751016, 132.6753717, 0.06837489, 13.26753717, 0.24513096, -147.12686692, -0.00796936, -179.3832077, -0.07335521, -17.93832077, -0.25011128, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 29443530.26038954, 0.1125, 0.00189844, 0.00058594, 12268137.60849564, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36851582681, 2103992, 0.36851582681, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 106.99814206, 0.00757352, 130.20400107, 0.0676797, 13.02040011, 0.24510295, -144.7456877, -0.00802758, -176.13827039, -0.07259854, -17.61382704, -0.25002178, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 106.99814206, 0.00757352, 130.20400107, 0.06830813, 13.02040011, 0.25016322, -144.7456877, -0.00802758, -176.13827039, -0.07327364, -17.61382704, -0.25512874, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 30112730.54231684, 0.1125, 0.00189844, 0.00058594, 12546971.05929868, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36787803833, 2203992, 0.36787803833, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 61.75368049, 0.00723092, 75.38786215, 0.05196633, 7.53878621, 0.25334326, -61.75368049, -0.00723092, -75.38786215, -0.05196633, -7.53878621, -0.25334326, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 61.7202183, 0.00720879, 75.34701207, 0.05252277, 7.53470121, 0.25611345, -81.66629359, -0.00745944, -99.69684779, -0.05580353, -9.96968478, -0.25939421, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 28987343.69333288, 0.1125, 0.00189844, 0.00058594, 12078059.87222204, 0.00152995)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32655226251, 2303992, 0.32655226251, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 61.89748566, 0.00713058, 74.97472765, 0.05047887, 7.49747276, 0.25321704, -81.91760492, -0.00736688, -99.22454932, -0.05361384, -9.92245493, -0.256352, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 61.89748566, 0.00713058, 74.97472765, 0.05066496, 7.49747276, 0.25547364, -81.91760492, -0.00736688, -99.22454932, -0.05381236, -9.92245493, -0.25862104, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 31581430.57734618, 0.1125, 0.00189844, 0.00058594, 13158929.40722758, 0.00152995)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32636375494, 2013992, 0.32636375494, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 104.91566847, 0.00771651, 127.74408317, 0.06969469, 12.77440832, 0.25127259, -141.97509158, -0.00817596, -172.8672006, -0.07475797, -17.28672006, -0.25633587, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 104.91566847, 0.00771651, 127.74408317, 0.06884232, 12.77440832, 0.24455244, -141.97509158, -0.00817596, -172.8672006, -0.07384228, -17.28672006, -0.24955241, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29915752.01213691, 0.1125, 0.00189844, 0.00058594, 12464896.67172371, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36762316101, 2113992, 0.36762316101, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 107.48065853, 0.00751457, 130.51879469, 0.06671953, 13.05187947, 0.24389167, -145.39626812, -0.00796081, -176.5614942, -0.0715636, -17.65614942, -0.24873574, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 107.48065853, 0.00751457, 130.51879469, 0.06702772, 13.05187947, 0.24639542, -145.39626812, -0.00796081, -176.5614942, -0.07189469, -17.65614942, -0.25126239, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 30795799.47936068, 0.1125, 0.00189844, 0.00058594, 12831583.11640028, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36775899509, 2213992, 0.36775899509, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 61.3075873, 0.00704046, 74.73307683, 0.05138855, 7.47330768, 0.25146195, -81.12198051, -0.0072842, -98.8865403, -0.05459781, -9.88865403, -0.25467121, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 61.3075873, 0.00704046, 74.73307683, 0.05150736, 7.47330768, 0.25285454, -81.12198051, -0.0072842, -98.8865403, -0.05472457, -9.88865403, -0.25607175, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 29517731.19248837, 0.1125, 0.00189844, 0.00058594, 12299054.66353682, 0.00152995)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32475541739, 2313992, 0.32475541739, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 61.97899951, 0.00724848, 75.70338226, 0.05226855, 7.57033823, 0.25311913, -82.00735574, -0.00750145, -100.16673791, -0.05553198, -10.01667379, -0.25638256, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 62.01272856, 0.0072709, 75.74458014, 0.05221001, 7.57445801, 0.25615302, -62.01272856, -0.0072709, -75.74458014, -0.05221001, -7.57445801, -0.25615302, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 28789229.39049123, 0.1125, 0.00189844, 0.00058594, 11995512.24603801, 0.00152995)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32713902758, 2023992, 0.32713902758, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 108.83922548, 0.00755452, 132.3938214, 0.06650964, 13.23938214, 0.24164215, -147.19939333, -0.00800872, -179.05575959, -0.07134312, -17.90557596, -0.24647563, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 108.83922548, 0.00755452, 132.3938214, 0.06708568, 13.23938214, 0.24630453, -147.19939333, -0.00800872, -179.05575959, -0.07196195, -17.90557596, -0.2511808, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 30240546.27371808, 0.1125, 0.00189844, 0.00058594, 12600227.6140492, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36917602724, 2123992, 0.36917602724, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 108.23452112, 0.00748568, 131.47466075, 0.06803209, 13.14746608, 0.24842823, -146.38925038, -0.00793232, -177.82198167, -0.07297622, -17.78219817, -0.25337235, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 108.23452112, 0.00748568, 131.47466075, 0.06789784, 13.14746608, 0.24734658, -146.38925038, -0.00793232, -177.82198167, -0.07283199, -17.78219817, -0.25228073, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 30697273.79303498, 0.1125, 0.00189844, 0.00058594, 12790530.74709791, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36802878955, 2223992, 0.36802878955, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 62.29548302, 0.00706232, 75.8178895, 0.05093155, 7.58178895, 0.25123034, -82.42978183, -0.00730534, -100.32271663, -0.05410807, -10.03227166, -0.25440686, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 62.31334566, 0.0070855, 75.83962956, 0.05079139, 7.58396296, 0.25324512, -62.31334566, -0.0070855, -75.83962956, -0.05079139, -7.58396296, -0.25324512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 30060693.63695235, 0.1125, 0.00189844, 0.00058594, 12525289.01539681, 0.00152995)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32604487039999996, 2323992, 0.32604487039999996, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
