import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 62.11793664, 0.00718083, 75.08360811, 0.04774355, 7.50836081, 0.24521912, -62.11793664, -0.00718083, -75.08360811, -0.04774355, -7.50836081, -0.24521912, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 62.11793664, 0.00718083, 75.08360811, 0.04775503, 7.50836081, 0.24536317, -62.11793664, -0.00718083, -75.08360811, -0.04775503, -7.50836081, -0.24536317, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 32200555.28608678, 0.1125, 0.00189844, 0.00058594, 13416898.03586949, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32688764172, 1001992, 0.32688764172, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 62.7987198, 0.00732068, 76.15130541, 0.05967845, 7.61513054, 0.3095169, -62.7987198, -0.00732068, -76.15130541, -0.05967845, -7.61513054, -0.3095169, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 62.7987198, 0.00732068, 76.15130541, 0.0595384, 7.61513054, 0.30779458, -62.7987198, -0.00732068, -76.15130541, -0.0595384, -7.61513054, -0.30779458, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 31241210.72759739, 0.1125, 0.00189844, 0.00058594, 13017171.13649891, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.26068641441, 1101992, 0.26068641441, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 63.61571938, 0.00717896, 76.65900906, 0.04721384, 7.66590091, 0.24586802, -63.61571938, -0.00717896, -76.65900906, -0.04721384, -7.66590091, -0.24586802, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 63.61571938, 0.00717896, 76.65900906, 0.04730918, 7.66590091, 0.24708733, -63.61571938, -0.00717896, -76.65900906, -0.04730918, -7.66590091, -0.24708733, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 33054489.43143059, 0.1125, 0.00189844, 0.00058594, 13772703.92976275, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32855023827, 1201992, 0.32855023827, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 61.46106662, 0.00697959, 74.1381797, 0.04851575, 7.41381797, 0.24991508, -61.46106662, -0.00697959, -74.1381797, -0.04851575, -7.41381797, -0.24991508, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 61.46106662, 0.00697959, 74.1381797, 0.04856582, 7.41381797, 0.25054148, -61.46106662, -0.00697959, -74.1381797, -0.04856582, -7.41381797, -0.25054148, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 32775622.68276781, 0.1125, 0.00189844, 0.00058594, 13656509.45115326, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32454318476, 1011992, 0.32454318476, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 63.12426892, 0.00719198, 76.70107187, 0.05965699, 7.67010719, 0.30768309, -63.12426892, -0.00719198, -76.70107187, -0.05965699, -7.67010719, -0.30768309, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 63.12426892, 0.00719198, 76.70107187, 0.06021348, 7.67010719, 0.31452545, -63.12426892, -0.00719198, -76.70107187, -0.06021348, -7.67010719, -0.31452545, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 30601519.26553632, 0.1125, 0.00189844, 0.00058594, 12750633.0273068, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25987230072, 1111992, 0.25987230072, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 62.12628458, 0.00716564, 75.03566897, 0.04998668, 7.5035669, 0.25468878, -62.12628458, -0.00716564, -75.03566897, -0.04998668, -7.5035669, -0.25468878, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 62.12628458, 0.00716564, 75.03566897, 0.04937641, 7.5035669, 0.2472258, -62.12628458, -0.00716564, -75.03566897, -0.04937641, -7.5035669, -0.2472258, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 32421203.04103301, 0.1125, 0.00189844, 0.00058594, 13508834.60043042, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32679178434, 1211992, 0.32679178434, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 62.92852021, 0.0071207, 76.46146002, 0.049661, 7.646146, 0.24877722, -62.92852021, -0.0071207, -76.46146002, -0.049661, -7.646146, -0.24877722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 62.92852021, 0.0071207, 76.46146002, 0.04969115, 7.646146, 0.24914228, -62.92852021, -0.0071207, -76.46146002, -0.04969115, -7.646146, -0.24914228, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 30608981.30693617, 0.1125, 0.00189844, 0.00058594, 12753742.2112234, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32705612714, 1021992, 0.32705612714, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 62.69435854, 0.00712565, 75.93409157, 0.05928568, 7.59340916, 0.30939237, -62.69435854, -0.00712565, -75.93409157, -0.05928568, -7.59340916, -0.30939237, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 62.69435854, 0.00712565, 75.93409157, 0.05939718, 7.59340916, 0.310774, -62.69435854, -0.00712565, -75.93409157, -0.05939718, -7.59340916, -0.310774, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 31604667.08778505, 0.1125, 0.00189844, 0.00058594, 13168611.2865771, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25896737821, 1121992, 0.25896737821, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 63.14979253, 0.00726918, 76.49492199, 0.0477432, 7.6494922, 0.24370215, -63.14979253, -0.00726918, -76.49492199, -0.0477432, -7.6494922, -0.24370215, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 63.14979253, 0.00726918, 76.49492199, 0.04791798, 7.6494922, 0.24589018, -63.14979253, -0.00726918, -76.49492199, -0.04791798, -7.6494922, -0.24589018, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 31568400.19727487, 0.1125, 0.00189844, 0.00058594, 13153500.08219787, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.3286661503, 1221992, 0.3286661503, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 61.82069307, 0.00728435, 75.28610838, 0.05214611, 7.52861084, 0.25599737, -61.82069307, -0.00728435, -75.28610838, -0.05214611, -7.52861084, -0.25599737, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 61.78109532, 0.00726411, 75.23788568, 0.05207805, 7.52378857, 0.25147769, -81.75146983, -0.00751133, -99.55808827, -0.05532194, -9.95580883, -0.25472158, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29852244.50455546, 0.1125, 0.00189844, 0.00058594, 12438435.21023144, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32717160883, 2001992, 0.32717160883, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 107.47313016, 0.00752225, 129.63848483, 0.06389544, 12.96384848, 0.24035281, -145.44604166, -0.00795311, -175.44296362, -0.06851379, -17.54429636, -0.24497116, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 107.47313016, 0.00752225, 129.63848483, 0.06403823, 12.96384848, 0.24155764, -145.44604166, -0.00795311, -175.44296362, -0.06866718, -17.54429636, -0.24618659, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 32780565.56337185, 0.1125, 0.00189844, 0.00058594, 13658568.98473827, 0.00152995)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36818055378000003, 2101992, 0.36818055378000003, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 109.70465807, 0.00761411, 132.19834654, 0.06298711, 13.21983465, 0.23828186, -148.45924032, -0.00804918, -178.89911373, -0.06753537, -17.88991137, -0.24283012, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 109.70465807, 0.00761411, 132.19834654, 0.0634388, 13.21983465, 0.2421444, -148.45924032, -0.00804918, -178.89911373, -0.06802061, -17.88991137, -0.24672622, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 33053120.25226253, 0.1125, 0.00189844, 0.00058594, 13772133.43844272, 0.00152995)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.37102298476, 2201992, 0.37102298476, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.97404569, 0.00703313, 75.9991758, 0.0475898, 7.59991758, 0.2461926, -62.97404569, -0.00703313, -75.9991758, -0.0475898, -7.59991758, -0.2461926, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 62.95856762, 0.00701182, 75.98049634, 0.04827064, 7.59804963, 0.2511221, -83.32350782, -0.00724269, -100.55758447, -0.05126046, -10.05575845, -0.25411192, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 32644404.69840228, 0.1125, 0.00189844, 0.00058594, 13601835.29100095, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32657508537, 2301992, 0.32657508537, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 63.04208628, 0.00697921, 76.10615873, 0.04777228, 7.61061587, 0.24578702, -83.43035278, -0.00720998, -100.71944071, -0.05073085, -10.07194407, -0.24874559, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 63.05269964, 0.00700112, 76.11897148, 0.04758348, 7.61189715, 0.24704202, -63.05269964, -0.00700112, -76.11897148, -0.04758348, -7.61189715, -0.24704202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 32553032.22768604, 0.1125, 0.00189844, 0.00058594, 13563763.42820252, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32636739623, 2011992, 0.32636739623, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 108.5855679, 0.00764049, 130.78916745, 0.06247593, 13.07891674, 0.2366551, -146.96968681, -0.00807447, -177.02207899, -0.06698317, -17.7022079, -0.24116235, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 108.5855679, 0.00764049, 130.78916745, 0.06257075, 13.07891674, 0.23746518, -146.96968681, -0.00807447, -177.02207899, -0.06708503, -17.7022079, -0.24197946, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 33178028.5043145, 0.1125, 0.00189844, 0.00058594, 13824178.54346438, 0.00152995)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.37041979805, 2111992, 0.37041979805, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 108.14033719, 0.00768184, 130.60800764, 0.06585181, 13.06080076, 0.24633735, -146.36119358, -0.00812275, -176.76978254, -0.07061367, -17.67697825, -0.25109921, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 108.14033719, 0.00768184, 130.60800764, 0.06573698, 13.06080076, 0.2453785, -146.36119358, -0.00812275, -176.76978254, -0.07049031, -17.67697825, -0.25013184, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 32427911.84044701, 0.1125, 0.00189844, 0.00058594, 13511629.93351959, 0.00152995)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.37037233469, 2211992, 0.37037233469, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 61.66866031, 0.0071753, 74.26496148, 0.04961033, 7.42649615, 0.25451291, -81.61966733, -0.00740459, -98.2911161, -0.05267722, -9.82911161, -0.25757981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 61.70957491, 0.00719191, 74.31423321, 0.04863847, 7.43142332, 0.24622482, -61.70957491, -0.00719191, -74.31423321, -0.04863847, -7.43142332, -0.24622482, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 33227505.68375156, 0.1125, 0.00189844, 0.00058594, 13844794.03489648, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32664383426, 2311992, 0.32664383426, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
