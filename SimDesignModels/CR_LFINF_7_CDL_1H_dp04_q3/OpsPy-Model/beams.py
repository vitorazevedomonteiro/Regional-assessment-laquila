import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32672, 1001992, 0.32672, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25872, 1101992, 0.25872, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32672, 1201992, 0.32672, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 53.7178027, 0.01025205, 65.45900939, 0.09722343, 6.54590094, 0.31498192, -82.09439728, -0.01116874, -100.03793253, -0.10732684, -10.00379325, -0.32508533, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.7178027, 0.01025205, 65.45900939, 0.09722343, 6.54590094, 0.31498192, -82.09439728, -0.01116874, -100.03793253, -0.10732684, -10.00379325, -0.32508533, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36896, 1011992, 0.36896, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 53.7178027, 0.01025205, 65.45900939, 0.11687406, 6.54590094, 0.3838337, -82.09439728, -0.01116874, -100.03793253, -0.12905315, -10.00379325, -0.39601279, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 53.7178027, 0.01025205, 65.45900939, 0.11687406, 6.54590094, 0.3838337, -82.09439728, -0.01116874, -100.03793253, -0.12905315, -10.00379325, -0.39601279, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30096, 1111992, 0.30096, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 53.7178027, 0.01025205, 65.45900939, 0.09722343, 6.54590094, 0.31498192, -82.09439728, -0.01116874, -100.03793253, -0.10732684, -10.00379325, -0.32508533, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 53.7178027, 0.01025205, 65.45900939, 0.09722343, 6.54590094, 0.31498192, -82.09439728, -0.01116874, -100.03793253, -0.10732684, -10.00379325, -0.32508533, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36896, 1211992, 0.36896, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32672, 1021992, 0.32672, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 31.0784854, 0.00962133, 37.8713716, 0.09000069, 3.78713716, 0.40054557, -46.08186539, -0.01011302, -56.15407011, -0.09817025, -5.61540701, -0.40871514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25872, 1121992, 0.25872, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 31.0784854, 0.00962133, 37.8713716, 0.07327139, 3.78713716, 0.31918279, -46.08186539, -0.01011302, -56.15407011, -0.07984296, -5.61540701, -0.32575436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 31.1219335, 0.00965426, 37.92431623, 0.07246683, 3.79243162, 0.31837824, -31.1219335, -0.00965426, -37.92431623, -0.07246683, -3.79243162, -0.31837824, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32672, 1221992, 0.32672, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 53.31782659, 0.00838212, 64.97160971, 0.12601287, 6.49716097, 0.43208535, -145.69401923, -0.01034897, -177.53865, -0.15974594, -17.753865, -0.46581842, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32672, 2001992, 0.32672, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 121.30412221, 0.00660923, 147.81780481, 0.10262532, 14.78178048, 0.35411848, -283.31839145, -0.00788861, -345.24385423, -0.12526021, -34.52438542, -0.37675337, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36896, 2101992, 0.36896, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 121.30412221, 0.00660923, 147.81780481, 0.10262532, 14.78178048, 0.35411848, -283.31839145, -0.00788861, -345.24385423, -0.12526021, -34.52438542, -0.37675337, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36896, 2201992, 0.36896, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 53.31782659, 0.00838212, 64.97160971, 0.12601287, 6.49716097, 0.43208535, -145.69401923, -0.01034897, -177.53865, -0.15974594, -17.753865, -0.46581842, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32672, 2301992, 0.32672, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 53.31782659, 0.00838212, 64.97160971, 0.12601287, 6.49716097, 0.43208535, -145.69401923, -0.01034897, -177.53865, -0.15974594, -17.753865, -0.46581842, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32672, 2011992, 0.32672, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 121.30412221, 0.00660923, 147.81780481, 0.10262532, 14.78178048, 0.35411848, -283.31839145, -0.00788861, -345.24385423, -0.12526021, -34.52438542, -0.37675337, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36896, 2111992, 0.36896, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 121.30412221, 0.00660923, 147.81780481, 0.10262532, 14.78178048, 0.35411848, -283.31839145, -0.00788861, -345.24385423, -0.12526021, -34.52438542, -0.37675337, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 81.68250914, 0.00641106, 99.53601719, 0.09816744, 9.95360172, 0.3496606, -191.81537027, -0.00739295, -233.74083622, -0.11955741, -23.37408362, -0.37105057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36896, 2211992, 0.36896, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 53.31782659, 0.00838212, 64.97160971, 0.12601287, 6.49716097, 0.43208535, -145.69401923, -0.01034897, -177.53865, -0.15974594, -17.753865, -0.46581842, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 35.91753538, 0.00808882, 43.76810233, 0.12436417, 4.37681023, 0.43043665, -145.6251524, -0.01042126, -177.45473081, -0.17220286, -17.74547308, -0.47827534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32672, 2311992, 0.32672, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
