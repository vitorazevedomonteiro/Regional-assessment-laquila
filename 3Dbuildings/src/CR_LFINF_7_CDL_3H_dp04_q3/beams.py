import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 45.92896969, 0.0099609, 55.9677557, 0.09428099, 5.59677557, 0.34019239, -79.57075835, -0.01103495, -96.96269683, -0.10700893, -9.69626968, -0.35292033, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32672, 1001992, 0.32672, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 45.92896969, 0.0099609, 55.9677557, 0.11644304, 5.59677557, 0.42698793, -79.57075835, -0.01103495, -96.96269683, -0.132234, -9.69626968, -0.44277888, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 45.92896969, 0.0099609, 55.9677557, 0.11644304, 5.59677557, 0.42698793, -79.57075835, -0.01103495, -96.96269683, -0.132234, -9.69626968, -0.44277888, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25872, 1101992, 0.25872, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 45.92896969, 0.0099609, 55.9677557, 0.09428099, 5.59677557, 0.34019239, -79.57075835, -0.01103495, -96.96269683, -0.10700893, -9.69626968, -0.35292033, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32672, 1201992, 0.32672, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 71.05183368, 0.00848669, 86.5817739, 0.11492141, 8.65817739, 0.39892886, -147.12714449, -0.00990026, -179.28501629, -0.13660504, -17.92850163, -0.42061249, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32672, 1011992, 0.32672, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 71.05183368, 0.00848669, 86.5817739, 0.1428959, 8.65817739, 0.50154971, -147.12714449, -0.00990026, -179.28501629, -0.16990716, -17.92850163, -0.52856098, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 71.05183368, 0.00848669, 86.5817739, 0.1428959, 8.65817739, 0.50154971, -147.12714449, -0.00990026, -179.28501629, -0.16990716, -17.92850163, -0.52856098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25872, 1111992, 0.25872, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 71.05183368, 0.00848669, 86.5817739, 0.11492141, 8.65817739, 0.39892886, -147.12714449, -0.00990026, -179.28501629, -0.13660504, -17.92850163, -0.42061249, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32672, 1211992, 0.32672, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 92.64877272, 0.00905865, 112.89919874, 0.11607778, 11.28991987, 0.38710987, -145.80538465, -0.01019387, -177.67435678, -0.12960915, -17.76743568, -0.40064124, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.36896, 1021992, 0.36896, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 92.64877272, 0.00905865, 112.89919874, 0.14025807, 11.28991987, 0.47252814, -145.80538465, -0.01019387, -177.67435678, -0.15659027, -17.76743568, -0.48886034, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 92.64877272, 0.00905865, 112.89919874, 0.14025807, 11.28991987, 0.47252814, -145.80538465, -0.01019387, -177.67435678, -0.15659027, -17.76743568, -0.48886034, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.30096, 1121992, 0.30096, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 92.64877272, 0.00905865, 112.89919874, 0.11607778, 11.28991987, 0.38710987, -145.80538465, -0.01019387, -177.67435678, -0.12960915, -17.76743568, -0.40064124, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.36896, 1221992, 0.36896, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32672, 1031992, 0.32672, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25872, 1131992, 0.25872, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32672, 1231992, 0.32672, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32672, 1002992, 0.32672, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25872, 1102992, 0.25872, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32672, 1202992, 0.32672, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36896, 1012992, 0.36896, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 62.46588951, 0.0086053, 76.11918288, 0.13712924, 7.61191829, 0.46939931, -145.726362, -0.01031037, -177.578062, -0.16742009, -17.7578062, -0.49969016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 62.46588951, 0.0086053, 76.11918288, 0.13712924, 7.61191829, 0.46939931, -145.726362, -0.01031037, -177.578062, -0.16742009, -17.7578062, -0.49969016, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30096, 1112992, 0.30096, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36896, 1212992, 0.36896, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36896, 1022992, 0.36896, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 62.46588951, 0.0086053, 76.11918288, 0.13712924, 7.61191829, 0.46939931, -145.726362, -0.01031037, -177.578062, -0.16742009, -17.7578062, -0.49969016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 62.46588951, 0.0086053, 76.11918288, 0.13712924, 7.61191829, 0.46939931, -145.726362, -0.01031037, -177.578062, -0.16742009, -17.7578062, -0.49969016, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30096, 1122992, 0.30096, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.46588951, 0.0086053, 76.11918288, 0.11344204, 7.61191829, 0.38447413, -145.726362, -0.01031037, -177.578062, -0.13846449, -17.7578062, -0.40949658, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36896, 1222992, 0.36896, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32672, 1032992, 0.32672, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25872, 1132992, 0.25872, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 30.98949833, 0.00955543, 37.76293445, 0.09276606, 3.77629345, 0.33867746, -79.59040899, -0.01110896, -96.98664256, -0.11486701, -9.69866426, -0.36077841, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 31.05579868, 0.00960434, 37.8437262, 0.09087853, 3.78437262, 0.33678993, -53.90036335, -0.01042941, -65.68147268, -0.10293652, -6.56814727, -0.34884792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32672, 1232992, 0.32672, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32672, 1003992, 0.32672, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25872, 1103992, 0.25872, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32672, 1203992, 0.32672, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32672, 1013992, 0.32672, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 35.91753538, 0.00808882, 43.76810233, 0.1549251, 4.37681023, 0.54144335, -145.6251524, -0.01042126, -177.45473081, -0.2147243, -17.74547308, -0.60124255, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 35.91753538, 0.00808882, 43.76810233, 0.1549251, 4.37681023, 0.54144335, -145.6251524, -0.01042126, -177.45473081, -0.2147243, -17.74547308, -0.60124255, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25872, 1113992, 0.25872, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32672, 1213992, 0.32672, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 53.1380776, 0.01023011, 64.75257262, 0.11721234, 6.47525726, 0.38824443, -123.60580869, -0.01241941, -150.62257546, -0.14319619, -15.06225755, -0.41422828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 53.1380776, 0.01023011, 64.75257262, 0.11721234, 6.47525726, 0.38824443, -123.60580869, -0.01241941, -150.62257546, -0.14319619, -15.06225755, -0.41422828, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36896, 1023992, 0.36896, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 53.1380776, 0.01023011, 64.75257262, 0.14138429, 6.47525726, 0.47365436, -123.60580869, -0.01241941, -150.62257546, -0.17274437, -15.06225755, -0.50501444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 53.1380776, 0.01023011, 64.75257262, 0.14138429, 6.47525726, 0.47365436, -123.60580869, -0.01241941, -150.62257546, -0.17274437, -15.06225755, -0.50501444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30096, 1123992, 0.30096, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 53.1380776, 0.01023011, 64.75257262, 0.11721234, 6.47525726, 0.38824443, -123.60580869, -0.01241941, -150.62257546, -0.14319619, -15.06225755, -0.41422828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 53.1380776, 0.01023011, 64.75257262, 0.11721234, 6.47525726, 0.38824443, -123.60580869, -0.01241941, -150.62257546, -0.14319619, -15.06225755, -0.41422828, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36896, 1223992, 0.36896, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32672, 1033992, 0.32672, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25872, 1133992, 0.25872, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32672, 1233992, 0.32672, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 45.42916376, 0.00993999, 55.35870619, 0.16138858, 5.53587062, 0.54790682, -123.61387065, -0.01246984, -150.63239955, -0.20481717, -15.06323995, -0.59133541, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 45.42916376, 0.00993999, 55.35870619, 0.16138858, 5.53587062, 0.54790682, -123.61387065, -0.01246984, -150.63239955, -0.20481717, -15.06323995, -0.59133541, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25872, 6200992, 0.25872, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 45.42916376, 0.00993999, 55.35870619, 0.16138858, 5.53587062, 0.54790682, -123.61387065, -0.01246984, -150.63239955, -0.20481717, -15.06323995, -0.59133541, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 45.42916376, 0.00993999, 55.35870619, 0.16138858, 5.53587062, 0.54790682, -123.61387065, -0.01246984, -150.63239955, -0.20481717, -15.06323995, -0.59133541, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25872, 6201992, 0.25872, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 30.98949833, 0.00955543, 37.76293445, 0.11463651, 3.77629345, 0.4251814, -79.59040899, -0.01110896, -96.98664256, -0.14213799, -9.69866426, -0.45268288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25872, 6202992, 0.25872, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 62.92525288, 0.00844979, 76.67895022, 0.10231187, 7.66789502, 0.35380503, -147.12751361, -0.00992198, -179.2854661, -0.12466048, -17.92854661, -0.37615363, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 93.15914657, 0.00873791, 113.52112602, 0.10807807, 11.3521126, 0.35957123, -216.86872401, -0.01066378, -264.27015118, -0.13209878, -26.42701512, -0.38359193, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36896, 2001992, 0.36896, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 125.53638318, 0.00676299, 152.97511946, 0.09032425, 15.29751195, 0.31598309, -191.98923753, -0.00733153, -233.95270599, -0.0997193, -23.3952706, -0.32537814, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 125.48215226, 0.00668219, 152.90903518, 0.09297727, 15.29090352, 0.31863611, -283.37656698, -0.00788036, -345.3147453, -0.11240437, -34.53147453, -0.33806321, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.4112, 2101992, 0.4112, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 125.53638318, 0.00676299, 152.97511946, 0.09032425, 15.29751195, 0.31598309, -191.98923753, -0.00733153, -233.95270599, -0.0997193, -23.3952706, -0.32537814, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 125.48215226, 0.00668219, 152.90903518, 0.09297727, 15.29090352, 0.31863611, -283.37656698, -0.00788036, -345.3147453, -0.11240437, -34.53147453, -0.33806321, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.4112, 2201992, 0.4112, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.92525288, 0.00844979, 76.67895022, 0.10231187, 7.66789502, 0.35380503, -147.12751361, -0.00992198, -179.2854661, -0.12466048, -17.92854661, -0.37615363, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 93.15914657, 0.00873791, 113.52112602, 0.10807807, 11.3521126, 0.35957123, -216.86872401, -0.01066378, -264.27015118, -0.13209878, -26.42701512, -0.38359193, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36896, 2301992, 0.36896, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 93.15914657, 0.00873791, 113.52112602, 0.10807807, 11.3521126, 0.35957123, -216.86872401, -0.01066378, -264.27015118, -0.13209878, -26.42701512, -0.38359193, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 62.76056166, 0.00837129, 76.47826211, 0.10608748, 7.64782621, 0.35758064, -216.64454083, -0.0107728, -263.99696783, -0.14163255, -26.39969678, -0.39312571, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36896, 2011992, 0.36896, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 125.48215226, 0.00668219, 152.90903518, 0.09297727, 15.29090352, 0.31863611, -283.37656698, -0.00788036, -345.3147453, -0.11240437, -34.53147453, -0.33806321, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 125.40401728, 0.00661422, 152.81382207, 0.09573257, 15.28138221, 0.32139141, -372.8985877, -0.00837601, -454.40377166, -0.1235378, -45.44037717, -0.34919663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.4112, 2111992, 0.4112, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 125.48215226, 0.00668219, 152.90903518, 0.09297727, 15.29090352, 0.31863611, -283.37656698, -0.00788036, -345.3147453, -0.11240437, -34.53147453, -0.33806321, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 125.40401728, 0.00661422, 152.81382207, 0.09573257, 15.28138221, 0.32139141, -372.8985877, -0.00837601, -454.40377166, -0.1235378, -45.44037717, -0.34919663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.4112, 2211992, 0.4112, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 93.15914657, 0.00873791, 113.52112602, 0.10807807, 11.3521126, 0.35957123, -216.86872401, -0.01066378, -264.27015118, -0.13209878, -26.42701512, -0.38359193, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 62.76056166, 0.00837129, 76.47826211, 0.10608748, 7.64782621, 0.35758064, -216.64454083, -0.0107728, -263.99696783, -0.14163255, -26.39969678, -0.39312571, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36896, 2311992, 0.36896, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 62.76056166, 0.00837129, 76.47826211, 0.10608748, 7.64782621, 0.35758064, -216.64454083, -0.0107728, -263.99696783, -0.14163255, -26.39969678, -0.39312571, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 62.92525288, 0.00844979, 76.67895022, 0.10231187, 7.66789502, 0.35380503, -147.12751361, -0.00992198, -179.2854661, -0.12466048, -17.92854661, -0.37615363, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.36896, 2021992, 0.36896, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 125.40401728, 0.00661422, 152.81382207, 0.09573257, 15.28138221, 0.32139141, -372.8985877, -0.00837601, -454.40377166, -0.1235378, -45.44037717, -0.34919663, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 125.53638318, 0.00676299, 152.97511946, 0.09032425, 15.29751195, 0.31598309, -191.98923753, -0.00733153, -233.95270599, -0.0997193, -23.3952706, -0.32537814, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.4112, 2121992, 0.4112, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 125.40401728, 0.00661422, 152.81382207, 0.09573257, 15.28138221, 0.32139141, -372.8985877, -0.00837601, -454.40377166, -0.1235378, -45.44037717, -0.34919663, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 125.53638318, 0.00676299, 152.97511946, 0.09032425, 15.29751195, 0.31598309, -191.98923753, -0.00733153, -233.95270599, -0.0997193, -23.3952706, -0.32537814, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.4112, 2221992, 0.4112, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 62.76056166, 0.00837129, 76.47826211, 0.10608748, 7.64782621, 0.35758064, -216.64454083, -0.0107728, -263.99696783, -0.14163255, -26.39969678, -0.39312571, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 62.92525288, 0.00844979, 76.67895022, 0.10231187, 7.66789502, 0.35380503, -147.12751361, -0.00992198, -179.2854661, -0.12466048, -17.92854661, -0.37615363, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.36896, 2321992, 0.36896, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32672, 2002992, 0.32672, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 81.56608159, 0.0063522, 99.39414183, 0.10111052, 9.93941418, 0.35260368, -282.81590844, -0.00795683, -344.63154251, -0.13485545, -34.46315425, -0.38634861, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36896, 2102992, 0.36896, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 81.56608159, 0.0063522, 99.39414183, 0.10111052, 9.93941418, 0.35260368, -282.81590844, -0.00795683, -344.63154251, -0.13485545, -34.46315425, -0.38634861, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36896, 2202992, 0.36896, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32672, 2302992, 0.32672, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32672, 2012992, 0.32672, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 81.56608159, 0.0063522, 99.39414183, 0.10111052, 9.93941418, 0.35260368, -282.81590844, -0.00795683, -344.63154251, -0.13485545, -34.46315425, -0.38634861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 121.24734829, 0.00654156, 147.7486217, 0.10569896, 14.77486217, 0.35719211, -372.79160647, -0.00838561, -454.27340734, -0.13770254, -45.42734073, -0.38919569, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36896, 2112992, 0.36896, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 81.56608159, 0.0063522, 99.39414183, 0.10111052, 9.93941418, 0.35260368, -282.81590844, -0.00795683, -344.63154251, -0.13485545, -34.46315425, -0.38634861, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 121.24734829, 0.00654156, 147.7486217, 0.10569896, 14.77486217, 0.35719211, -372.79160647, -0.00838561, -454.27340734, -0.13770254, -45.42734073, -0.38919569, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36896, 2212992, 0.36896, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32672, 2312992, 0.32672, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32672, 2022992, 0.32672, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 121.24734829, 0.00654156, 147.7486217, 0.10569896, 14.77486217, 0.35719211, -372.79160647, -0.00838561, -454.27340734, -0.13770254, -45.42734073, -0.38919569, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.36896, 2122992, 0.36896, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 121.24734829, 0.00654156, 147.7486217, 0.10569896, 14.77486217, 0.35719211, -372.79160647, -0.00838561, -454.27340734, -0.13770254, -45.42734073, -0.38919569, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36896, 2222992, 0.36896, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 70.90165114, 0.00839377, 86.39876566, 0.11919885, 8.63987657, 0.4032063, -216.7049815, -0.01074484, -264.07061915, -0.15525218, -26.40706191, -0.43925964, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 36.1918963, 0.00798364, 44.10243086, 0.11246292, 4.41024309, 0.39647038, -147.11881615, -0.01000141, -179.2748676, -0.15537035, -17.92748676, -0.4393778, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32672, 2322992, 0.32672, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32672, 2003992, 0.32672, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36896, 2103992, 0.36896, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36896, 2203992, 0.36896, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32672, 2303992, 0.32672, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32672, 2013992, 0.32672, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 107.21510621, 0.00752873, 130.64932463, 0.10500822, 13.06493246, 0.35650138, -250.04380295, -0.00907836, -304.69637293, -0.12823886, -30.46963729, -0.37973202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36896, 2113992, 0.36896, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.2, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 107.21510621, 0.00752873, 130.64932463, 0.10500822, 13.06493246, 0.35650138, -250.04380295, -0.00907836, -304.69637293, -0.12823886, -30.46963729, -0.37973202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36896, 2213992, 0.36896, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32672, 2313992, 0.32672, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32672, 2023992, 0.32672, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 107.21510621, 0.00752873, 130.64932463, 0.10500822, 13.06493246, 0.35650138, -250.04380295, -0.00907836, -304.69637293, -0.12823886, -30.46963729, -0.37973202, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36896, 2123992, 0.36896, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.2, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 107.21510621, 0.00752873, 130.64932463, 0.10500822, 13.06493246, 0.35650138, -250.04380295, -0.00907836, -304.69637293, -0.12823886, -30.46963729, -0.37973202, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 72.28936195, 0.00729289, 88.08979118, 0.09997924, 8.80897912, 0.3514724, -169.43777496, -0.00848002, -206.47212552, -0.12178129, -20.64721255, -0.37327444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36896, 2223992, 0.36896, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32672, 2323992, 0.32672, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
