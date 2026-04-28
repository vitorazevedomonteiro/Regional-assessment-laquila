import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32672, 1001992, 0.32672, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25872, 1101992, 0.25872, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32672, 1201992, 0.32672, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36896, 1011992, 0.36896, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 107.21510621, 0.00752873, 130.64932463, 0.10125764, 13.06493246, 0.40957408, -250.04380295, -0.00907836, -304.69637293, -0.12365409, -30.46963729, -0.43197053, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 107.21510621, 0.00752873, 130.64932463, 0.10125764, 13.06493246, 0.40957408, -250.04380295, -0.00907836, -304.69637293, -0.12365409, -30.46963729, -0.43197053, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30096, 1111992, 0.30096, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36896, 1211992, 0.36896, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 96.39099211, 0.00897184, 117.45936245, 0.07626319, 11.74593624, 0.30192203, -147.11736695, -0.00982747, -179.27310165, -0.08422676, -17.92731017, -0.3098856, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 142.64720334, 0.00937427, 173.82588552, 0.08125633, 17.38258855, 0.30691517, -217.1538374, -0.01049565, -264.61758237, -0.08997055, -26.46175824, -0.31562939, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.4112, 1021992, 0.4112, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 142.64720334, 0.00937427, 173.82588552, 0.09549869, 17.38258855, 0.36586849, -217.1538374, -0.01049565, -264.61758237, -0.10571733, -26.46175824, -0.37608713, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 142.64720334, 0.00937427, 173.82588552, 0.09549869, 17.38258855, 0.36586849, -217.1538374, -0.01049565, -264.61758237, -0.10571733, -26.46175824, -0.37608713, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.3432, 1121992, 0.3432, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 142.64720334, 0.00937427, 173.82588552, 0.08125633, 17.38258855, 0.30691517, -217.1538374, -0.01049565, -264.61758237, -0.08997055, -26.46175824, -0.31562939, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 96.39099211, 0.00897184, 117.45936245, 0.07626319, 11.74593624, 0.30192203, -147.11736695, -0.00982747, -179.27310165, -0.08422676, -17.92731017, -0.3098856, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.4112, 1221992, 0.4112, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 53.7178027, 0.01025205, 65.45900939, 0.0784649, 6.54590094, 0.29622339, -82.09439728, -0.01116874, -100.03793253, -0.08658686, -10.00379325, -0.30434535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 53.7178027, 0.01025205, 65.45900939, 0.0784649, 6.54590094, 0.29622339, -82.09439728, -0.01116874, -100.03793253, -0.08658686, -10.00379325, -0.30434535, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.36896, 1031992, 0.36896, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 53.7178027, 0.01025205, 65.45900939, 0.09387716, 6.54590094, 0.3608368, -82.09439728, -0.01116874, -100.03793253, -0.1036271, -10.00379325, -0.37058674, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 53.7178027, 0.01025205, 65.45900939, 0.09387716, 6.54590094, 0.3608368, -82.09439728, -0.01116874, -100.03793253, -0.1036271, -10.00379325, -0.37058674, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.30096, 1131992, 0.30096, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 53.7178027, 0.01025205, 65.45900939, 0.0784649, 6.54590094, 0.29622339, -82.09439728, -0.01116874, -100.03793253, -0.08658686, -10.00379325, -0.30434535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 53.7178027, 0.01025205, 65.45900939, 0.0784649, 6.54590094, 0.29622339, -82.09439728, -0.01116874, -100.03793253, -0.08658686, -10.00379325, -0.30434535, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.36896, 1231992, 0.36896, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32672, 1002992, 0.32672, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25872, 1102992, 0.25872, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32672, 1202992, 0.32672, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.36896, 1012992, 0.36896, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 93.15914657, 0.00873791, 113.52112602, 0.1042559, 11.3521126, 0.41257234, -216.86872401, -0.01066378, -264.27015118, -0.1274265, -26.42701512, -0.43574293, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 93.15914657, 0.00873791, 113.52112602, 0.1042559, 11.3521126, 0.41257234, -216.86872401, -0.01066378, -264.27015118, -0.1274265, -26.42701512, -0.43574293, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.30096, 1112992, 0.30096, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.36896, 1212992, 0.36896, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 92.64877272, 0.00905865, 112.89919874, 0.09299522, 11.28991987, 0.36402731, -145.80538465, -0.01019387, -177.67435678, -0.10385291, -17.76743568, -0.374885, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.36896, 1022992, 0.36896, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.225, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 92.64877272, 0.00905865, 112.89919874, 0.11196016, 11.28991987, 0.44423023, -145.80538465, -0.01019387, -177.67435678, -0.12501458, -17.76743568, -0.45728465, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 92.64877272, 0.00905865, 112.89919874, 0.11196016, 11.28991987, 0.44423023, -145.80538465, -0.01019387, -177.67435678, -0.12501458, -17.76743568, -0.45728465, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30096, 1122992, 0.30096, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.225, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 92.64877272, 0.00905865, 112.89919874, 0.09299522, 11.28991987, 0.36402731, -145.80538465, -0.01019387, -177.67435678, -0.10385291, -17.76743568, -0.374885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.36896, 1222992, 0.36896, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32672, 1032992, 0.32672, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 45.92896969, 0.0099609, 55.9677557, 0.09347631, 5.59677557, 0.40402119, -79.57075835, -0.01103495, -96.96269683, -0.10609303, -9.69626968, -0.41663791, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25872, 1132992, 0.25872, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 45.92896969, 0.0099609, 55.9677557, 0.07609431, 5.59677557, 0.32200571, -79.57075835, -0.01103495, -96.96269683, -0.08630866, -9.69626968, -0.33222006, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.32672, 1232992, 0.32672, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32672, 1003992, 0.32672, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25872, 1103992, 0.25872, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32672, 1203992, 0.32672, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 62.30666464, 0.00849778, 75.92515591, 0.09496447, 7.59251559, 0.36599656, -214.38659055, -0.01129431, -261.24549289, -0.12708893, -26.12454929, -0.39812102, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.36896, 1013992, 0.36896, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 62.30666464, 0.00849778, 75.92515591, 0.11450106, 7.59251559, 0.44677113, -214.38659055, -0.01129431, -261.24549289, -0.15325198, -26.12454929, -0.48552205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 62.30666464, 0.00849778, 75.92515591, 0.11450106, 7.59251559, 0.44677113, -214.38659055, -0.01129431, -261.24549289, -0.15325198, -26.12454929, -0.48552205, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.30096, 1113992, 0.30096, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 62.30666464, 0.00849778, 75.92515591, 0.09496447, 7.59251559, 0.36599656, -214.38659055, -0.01129431, -261.24549289, -0.12708893, -26.12454929, -0.39812102, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.36896, 1213992, 0.36896, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.36896, 1023992, 0.36896, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 62.46588951, 0.0086053, 76.11918288, 0.10940839, 7.61191829, 0.44167846, -145.726362, -0.01031037, -177.578062, -0.13353368, -17.7578062, -0.46580375, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 62.46588951, 0.0086053, 76.11918288, 0.10940839, 7.61191829, 0.44167846, -145.726362, -0.01031037, -177.578062, -0.13353368, -17.7578062, -0.46580375, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.30096, 1123992, 0.30096, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 62.46588951, 0.0086053, 76.11918288, 0.0908302, 7.61191829, 0.36186229, -145.726362, -0.01031037, -177.578062, -0.1108234, -17.7578062, -0.38185549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.36896, 1223992, 0.36896, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
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
    ops.uniaxialMaterial('Hysteretic', 1133990, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
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
    ops.uniaxialMaterial('Hysteretic', 1233990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32672, 1233992, 0.32672, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1004991, 1004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1004992, 1004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.32672, 1004992, 0.32672, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1104991, 1104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1104992, 1104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.25872, 1104992, 0.25872, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1204991, 1204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1204992, 1204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.32672, 1204992, 0.32672, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1014991, 1014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1014992, 1014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.32672, 1014992, 0.32672, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 35.91753538, 0.00808882, 43.76810233, 0.12325453, 4.37681023, 0.50977278, -145.6251524, -0.01042126, -177.45473081, -0.17065894, -17.74547308, -0.55717719, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 35.91753538, 0.00808882, 43.76810233, 0.12325453, 4.37681023, 0.50977278, -145.6251524, -0.01042126, -177.45473081, -0.17065894, -17.74547308, -0.55717719, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1114991, 1114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1114992, 1114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.25872, 1114992, 0.25872, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1214991, 1214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1214992, 1214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.32672, 1214992, 0.32672, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1024991, 1024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1024992, 1024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.36896, 1024992, 0.36896, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 53.1380776, 0.01023011, 64.75257262, 0.11309614, 6.47525726, 0.4453662, -123.60580869, -0.01241941, -150.62257546, -0.13816448, -15.06225755, -0.47043455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 53.1380776, 0.01023011, 64.75257262, 0.11309614, 6.47525726, 0.4453662, -123.60580869, -0.01241941, -150.62257546, -0.13816448, -15.06225755, -0.47043455, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1124991, 1124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1124992, 1124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.30096, 1124992, 0.30096, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1224991, 1224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1224992, 1224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.36896, 1224992, 0.36896, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1034991, 1034990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1034992, 1034991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.32672, 1034992, 0.32672, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1134991, 1134990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1134992, 1134991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.25872, 1134992, 0.25872, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1234991, 1234990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1234992, 1234991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.32672, 1234992, 0.32672, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 53.31782659, 0.00838212, 64.97160971, 0.12489029, 6.49716097, 0.51140854, -145.69401923, -0.01034897, -177.53865, -0.15832021, -17.753865, -0.54483845, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 53.31782659, 0.00838212, 64.97160971, 0.12489029, 6.49716097, 0.51140854, -145.69401923, -0.01034897, -177.53865, -0.15832021, -17.753865, -0.54483845, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25872, 6200992, 0.25872, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 62.46588951, 0.0086053, 76.11918288, 0.10940839, 7.61191829, 0.44167846, -145.726362, -0.01031037, -177.578062, -0.13353368, -17.7578062, -0.46580375, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 62.46588951, 0.0086053, 76.11918288, 0.10940839, 7.61191829, 0.44167846, -145.726362, -0.01031037, -177.578062, -0.13353368, -17.7578062, -0.46580375, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30096, 6201992, 0.30096, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 45.42916376, 0.00993999, 55.35870619, 0.1287232, 5.53587062, 0.51524144, -123.61387065, -0.01246984, -150.63239955, -0.16333049, -15.06323995, -0.54984874, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 45.42916376, 0.00993999, 55.35870619, 0.1287232, 5.53587062, 0.51524144, -123.61387065, -0.01246984, -150.63239955, -0.16333049, -15.06323995, -0.54984874, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25872, 6202992, 0.25872, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 6203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6203990, 37.59803772, 0.01219345, 45.8159154, 0.13407929, 4.58159154, 0.52059753, -101.65364409, -0.01560328, -123.87228271, -0.17040442, -12.38722827, -0.55692266, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6203991, 37.59803772, 0.01219345, 45.8159154, 0.13407929, 4.58159154, 0.52059753, -101.65364409, -0.01560328, -123.87228271, -0.17040442, -12.38722827, -0.55692266, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6203990, 29636834.16754785, 0.06, 0.00045, 0.0002, 12348680.90314494, 0.00046953)
    ops.section('Aggregator', 6203991, 6203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6203992, 6203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6203, 6203991, 0.25872, 6203992, 0.25872, 6203990)
    # Create element
    ops.element('forceBeamColumn', 6203, 1104, 1204, 6203, 6203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32672, 2001992, 0.32672, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36896, 2101992, 0.36896, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36896, 2201992, 0.36896, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32672, 2301992, 0.32672, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32672, 2011992, 0.32672, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36896, 2111992, 0.36896, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36896, 2211992, 0.36896, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32672, 2311992, 0.32672, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.32672, 2021992, 0.32672, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.36896, 2121992, 0.36896, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.36896, 2221992, 0.36896, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 70.90165114, 0.00839377, 86.39876566, 0.09529971, 8.63987657, 0.37930717, -216.7049815, -0.01074484, -264.07061915, -0.12408393, -26.40706191, -0.40809139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32672, 2321992, 0.32672, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32672, 2002992, 0.32672, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36896, 2102992, 0.36896, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36896, 2202992, 0.36896, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32672, 2302992, 0.32672, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32672, 2012992, 0.32672, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36896, 2112992, 0.36896, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.225, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36896, 2212992, 0.36896, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32672, 2312992, 0.32672, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32672, 2022992, 0.32672, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.36896, 2122992, 0.36896, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.225, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 121.30412221, 0.00660923, 147.81780481, 0.08191597, 14.78178048, 0.33340912, -283.31839145, -0.00788861, -345.24385423, -0.09994477, -34.52438542, -0.35143792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.36896, 2222992, 0.36896, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 53.5535113, 0.00817706, 65.25880849, 0.09428098, 6.52588085, 0.37828843, -216.56456043, -0.01080844, -263.89950597, -0.13061052, -26.3899506, -0.41461798, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32672, 2322992, 0.32672, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.36896, 2003992, 0.36896, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.36896, 2103992, 0.36896, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.36896, 2203992, 0.36896, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.36896, 2303992, 0.36896, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.36896, 2013992, 0.36896, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 121.24734829, 0.00654156, 147.7486217, 0.08431207, 14.77486217, 0.33580522, -372.79160647, -0.00838561, -454.27340734, -0.10981065, -45.42734073, -0.36130381, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36896, 2113992, 0.36896, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 81.56608159, 0.0063522, 99.39414183, 0.08067245, 9.93941418, 0.33216561, -282.81590844, -0.00795683, -344.63154251, -0.10748516, -34.46315425, -0.35897832, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 121.24734829, 0.00654156, 147.7486217, 0.08431207, 14.77486217, 0.33580522, -372.79160647, -0.00838561, -454.27340734, -0.10981065, -45.42734073, -0.36130381, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36896, 2213992, 0.36896, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.36896, 2313992, 0.36896, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.36896, 2023992, 0.36896, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 121.24734829, 0.00654156, 147.7486217, 0.08431207, 14.77486217, 0.33580522, -372.79160647, -0.00838561, -454.27340734, -0.10981065, -45.42734073, -0.36130381, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.36896, 2123992, 0.36896, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 121.24734829, 0.00654156, 147.7486217, 0.08431207, 14.77486217, 0.33580522, -372.79160647, -0.00838561, -454.27340734, -0.10981065, -45.42734073, -0.36130381, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 81.68250914, 0.00641106, 99.53601719, 0.07837685, 9.95360172, 0.32987001, -191.81537027, -0.00739295, -233.74083622, -0.09536508, -23.37408362, -0.34685823, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36896, 2223992, 0.36896, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 62.76056166, 0.00837129, 76.47826211, 0.08501144, 7.64782621, 0.3365046, -216.64454083, -0.0107728, -263.99696783, -0.1134079, -26.39969678, -0.36490106, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.36896, 2323992, 0.36896, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2004991, 2004990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2004992, 2004991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.36896, 2004992, 0.36896, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2104991, 2104990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2104992, 2104991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.36896, 2104992, 0.36896, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2204991, 2204990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2204992, 2204991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.36896, 2204992, 0.36896, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2304991, 2304990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2304992, 2304991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.36896, 2304992, 0.36896, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2014991, 2014990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2014992, 2014991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.36896, 2014992, 0.36896, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2114991, 2114990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2114992, 2114991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.36896, 2114992, 0.36896, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2214991, 2214990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2214992, 2214991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.36896, 2214992, 0.36896, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2314991, 2314990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2314992, 2314991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.36896, 2314992, 0.36896, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2024991, 2024990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2024992, 2024991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.36896, 2024992, 0.36896, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2124991, 2124990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2124992, 2124991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.36896, 2124992, 0.36896, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 107.21510621, 0.00752873, 130.64932463, 0.08398323, 13.06493246, 0.33547639, -250.04380295, -0.00907836, -304.69637293, -0.10253758, -30.46963729, -0.35403073, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2224991, 2224990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2224992, 2224991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.36896, 2224992, 0.36896, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 53.1380776, 0.01023011, 64.75257262, 0.09413774, 6.47525726, 0.36516983, -123.60580869, -0.01241941, -150.62257546, -0.11498943, -15.06225755, -0.38602152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 2324991, 2324990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2324992, 2324991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.36896, 2324992, 0.36896, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)
