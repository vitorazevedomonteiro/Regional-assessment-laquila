import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
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
    ops.uniaxialMaterial('Hysteretic', 1101990, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
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
    ops.uniaxialMaterial('Hysteretic', 1201990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32672, 1201992, 0.32672, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.69321728, 0.00824634, 65.42905028, 0.09095416, 6.54290503, 0.37496161, -147.12627266, -0.00994972, -179.28395391, -0.11499281, -17.92839539, -0.39900026, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32672, 1011992, 0.32672, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 53.69321728, 0.00824634, 65.42905028, 0.11269245, 6.54290503, 0.47134627, -147.12627266, -0.00994972, -179.28395391, -0.14260153, -17.92839539, -0.50125535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 53.69321728, 0.00824634, 65.42905028, 0.11269245, 6.54290503, 0.47134627, -147.12627266, -0.00994972, -179.28395391, -0.14260153, -17.92839539, -0.50125535, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25872, 1111992, 0.25872, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 53.69321728, 0.00824634, 65.42905028, 0.09095416, 6.54290503, 0.37496161, -147.12627266, -0.00994972, -179.28395391, -0.11499281, -17.92839539, -0.39900026, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 36.1918963, 0.00798364, 44.10243086, 0.08992818, 4.41024309, 0.37393563, -147.11881615, -0.01000141, -179.2748676, -0.12401627, -17.92748676, -0.40802372, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32672, 1211992, 0.32672, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32672, 1021992, 0.32672, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25872, 1121992, 0.25872, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 30.98949833, 0.00955543, 37.76293445, 0.07481867, 3.77629345, 0.32073007, -79.59040899, -0.01110896, -96.98664256, -0.09248782, -9.69866426, -0.33839923, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 31.05579868, 0.00960434, 37.8437262, 0.07334881, 3.78437262, 0.31926021, -53.90036335, -0.01042941, -65.68147268, -0.082984, -6.56814727, -0.3288954, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32672, 1221992, 0.32672, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32672, 1002992, 0.32672, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25872, 1102992, 0.25872, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.32672, 1202992, 0.32672, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32672, 1012992, 0.32672, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 35.91753538, 0.00808882, 43.76810233, 0.12325453, 4.37681023, 0.50977278, -145.6251524, -0.01042126, -177.45473081, -0.17065894, -17.74547308, -0.55717719, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 35.91753538, 0.00808882, 43.76810233, 0.12325453, 4.37681023, 0.50977278, -145.6251524, -0.01042126, -177.45473081, -0.17065894, -17.74547308, -0.55717719, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25872, 1112992, 0.25872, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32672, 1212992, 0.32672, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.32672, 1022992, 0.32672, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 31.0784854, 0.00962133, 37.8713716, 0.07266396, 3.78713716, 0.38320885, -46.08186539, -0.01011302, -56.15407011, -0.07917752, -5.61540701, -0.3897224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.25872, 1122992, 0.25872, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 31.0784854, 0.00962133, 37.8713716, 0.05954295, 3.78713716, 0.30545435, -46.08186539, -0.01011302, -56.15407011, -0.06480317, -5.61540701, -0.31071457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 31.1219335, 0.00965426, 37.92431623, 0.05891903, 3.79243162, 0.30483043, -31.1219335, -0.00965426, -37.92431623, -0.05891903, -3.79243162, -0.30483043, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.32672, 1222992, 0.32672, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 30.98949833, 0.00955543, 37.76293445, 0.09197197, 3.77629345, 0.40251685, -79.59040899, -0.01110896, -96.98664256, -0.11387683, -9.69866426, -0.42442171, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29636834.16754785, 0.07, 0.00071458, 0.00023333, 12348680.90314494, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25872, 6200992, 0.25872, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 37.59803772, 0.01219345, 45.8159154, 0.13407929, 4.58159154, 0.52059753, -101.65364409, -0.01560328, -123.87228271, -0.17040442, -12.38722827, -0.55692266, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 37.59803772, 0.01219345, 45.8159154, 0.13407929, 4.58159154, 0.52059753, -101.65364409, -0.01560328, -123.87228271, -0.17040442, -12.38722827, -0.55692266, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29636834.16754785, 0.06, 0.00045, 0.0002, 12348680.90314494, 0.00046953)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25872, 6201992, 0.25872, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36896, 2001992, 0.36896, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 125.53638318, 0.00676299, 152.97511946, 0.07230123, 15.29751195, 0.29796007, -191.98923753, -0.00733153, -233.95270599, -0.07979252, -23.3952706, -0.30545136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 125.48215226, 0.00668219, 152.90903518, 0.07436461, 15.29090352, 0.30002345, -283.37656698, -0.00788036, -345.3147453, -0.08985998, -34.53147453, -0.31551882, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.4112, 2101992, 0.4112, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 125.53638318, 0.00676299, 152.97511946, 0.07230123, 15.29751195, 0.29796007, -191.98923753, -0.00733153, -233.95270599, -0.07979252, -23.3952706, -0.30545136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 125.48215226, 0.00668219, 152.90903518, 0.07436461, 15.29090352, 0.30002345, -283.37656698, -0.00788036, -345.3147453, -0.08985998, -34.53147453, -0.31551882, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.4112, 2201992, 0.4112, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36896, 2301992, 0.36896, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36896, 2011992, 0.36896, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 125.48215226, 0.00668219, 152.90903518, 0.07436461, 15.29090352, 0.30002345, -283.37656698, -0.00788036, -345.3147453, -0.08985998, -34.53147453, -0.31551882, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 125.53638318, 0.00676299, 152.97511946, 0.07230123, 15.29751195, 0.29796007, -191.98923753, -0.00733153, -233.95270599, -0.07979252, -23.3952706, -0.30545136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.4112, 2111992, 0.4112, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 125.48215226, 0.00668219, 152.90903518, 0.07436461, 15.29090352, 0.30002345, -283.37656698, -0.00788036, -345.3147453, -0.08985998, -34.53147453, -0.31551882, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 125.53638318, 0.00676299, 152.97511946, 0.07230123, 15.29751195, 0.29796007, -191.98923753, -0.00733153, -233.95270599, -0.07979252, -23.3952706, -0.30545136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29636834.16754785, 0.125, 0.00260417, 0.00065104, 12348680.90314494, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.4112, 2211992, 0.4112, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 93.15914657, 0.00873791, 113.52112602, 0.08665176, 11.3521126, 0.33814492, -216.86872401, -0.01066378, -264.27015118, -0.10590691, -26.42701512, -0.35740007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 62.92525288, 0.00844979, 76.67895022, 0.08206711, 7.66789502, 0.33356026, -147.12751361, -0.00992198, -179.2854661, -0.09991296, -17.92854661, -0.35140611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 29636834.16754785, 0.1, 0.00133333, 0.00052083, 12348680.90314494, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36896, 2311992, 0.36896, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 53.31782659, 0.00838212, 64.97160971, 0.10064153, 6.49716097, 0.40671401, -145.69401923, -0.01034897, -177.53865, -0.12752306, -17.753865, -0.43359554, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32672, 2002992, 0.32672, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 72.14669726, 0.00722505, 87.91594399, 0.08256757, 8.7915944, 0.33406073, -249.67300087, -0.00916352, -304.24452391, -0.11006086, -30.42445239, -0.36155401, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36896, 2102992, 0.36896, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 72.14669726, 0.00722505, 87.91594399, 0.08256757, 8.7915944, 0.33406073, -249.67300087, -0.00916352, -304.24452391, -0.11006086, -30.42445239, -0.36155401, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36896, 2202992, 0.36896, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 53.31782659, 0.00838212, 64.97160971, 0.10064153, 6.49716097, 0.40671401, -145.69401923, -0.01034897, -177.53865, -0.12752306, -17.753865, -0.43359554, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32672, 2302992, 0.32672, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 53.31782659, 0.00838212, 64.97160971, 0.10064153, 6.49716097, 0.40671401, -145.69401923, -0.01034897, -177.53865, -0.12752306, -17.753865, -0.43359554, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32672, 2012992, 0.32672, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 72.14669726, 0.00722505, 87.91594399, 0.08256757, 8.7915944, 0.33406073, -249.67300087, -0.00916352, -304.24452391, -0.11006086, -30.42445239, -0.36155401, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36896, 2112992, 0.36896, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 72.14669726, 0.00722505, 87.91594399, 0.08256757, 8.7915944, 0.33406073, -249.67300087, -0.00916352, -304.24452391, -0.11006086, -30.42445239, -0.36155401, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 72.28936195, 0.00729289, 88.08979118, 0.07998807, 8.80897912, 0.33148123, -169.43777496, -0.00848002, -206.47212552, -0.09734376, -20.64721255, -0.34883691, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29636834.16754785, 0.1125, 0.00189844, 0.00058594, 12348680.90314494, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.36896, 2212992, 0.36896, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 53.31782659, 0.00838212, 64.97160971, 0.10064153, 6.49716097, 0.40671401, -145.69401923, -0.01034897, -177.53865, -0.12752306, -17.753865, -0.43359554, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 35.91753538, 0.00808882, 43.76810233, 0.09928517, 4.37681023, 0.40535765, -145.6251524, -0.01042126, -177.45473081, -0.13730879, -17.74547308, -0.44338127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29636834.16754785, 0.08, 0.00106667, 0.00026667, 12348680.90314494, 0.00073242)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32672, 2312992, 0.32672, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
