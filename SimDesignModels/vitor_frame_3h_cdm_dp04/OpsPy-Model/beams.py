import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 63.15809569, 0.00730847, 76.62964316, 0.04900735, 7.66296432, 0.24634713, -83.58260187, -0.00755269, -101.41067245, -0.05203994, -10.14106725, -0.24937973, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 63.15809569, 0.00730847, 76.62964316, 0.04904568, 7.66296432, 0.2468161, -83.58260187, -0.00755269, -101.41067245, -0.05208084, -10.14106725, -0.24985125, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 31068617.44050555, 0.1125, 0.00189844, 0.00058594, 12945257.26687731, 0.00152995)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32915854033, 1001992, 0.32915854033, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 60.16742163, 0.00706972, 73.14011817, 0.06249659, 7.31401182, 0.31631735, -79.61915975, -0.00730734, -96.78584514, -0.06644058, -9.67858451, -0.32026133, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 60.16742163, 0.00706972, 73.14011817, 0.06290576, 7.31401182, 0.32119371, -79.61915975, -0.00730734, -96.78584514, -0.0668771, -9.67858451, -0.32516505, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 30459606.17421288, 0.1125, 0.00189844, 0.00058594, 12691502.5725887, 0.00152995)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25587328749, 1101992, 0.25587328749, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 62.55674073, 0.00711438, 76.23814902, 0.05132023, 7.6238149, 0.25163364, -82.77234162, -0.00736125, -100.87498233, -0.05452311, -10.08749823, -0.25483652, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 62.55674073, 0.00711438, 76.23814902, 0.05156761, 7.6238149, 0.25455039, -82.77234162, -0.00736125, -100.87498233, -0.05478704, -10.08749823, -0.25776982, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29598957.6509242, 0.1125, 0.00189844, 0.00058594, 12332899.02121842, 0.00152995)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32671360521000004, 1201992, 0.32671360521000004, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 108.29039145, 0.00767402, 132.64715598, 0.06959676, 13.2647156, 0.24533175, -146.41011378, -0.00815688, -179.34079783, -0.07467933, -17.93407978, -0.25041432, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 108.29039145, 0.00767402, 132.64715598, 0.06984162, 13.2647156, 0.24722946, -146.41011378, -0.00815688, -179.34079783, -0.07494238, -17.93407978, -0.25233022, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 27675370.33320307, 0.1125, 0.00189844, 0.00058594, 11531404.30550128, 0.00152995)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36950936125, 1011992, 0.36950936125, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 105.70323179, 0.00746186, 128.85327353, 0.08187382, 12.88532735, 0.29856647, -142.9695217, -0.00791478, -174.28124546, -0.08785417, -17.42812455, -0.30454682, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 105.70323179, 0.00746186, 128.85327353, 0.08232399, 12.88532735, 0.3021392, -142.9695217, -0.00791478, -174.28124546, -0.08833778, -17.42812455, -0.30815299, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 29510788.03063509, 0.1125, 0.00189844, 0.00058594, 12296161.67943129, 0.00152995)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.29751864579, 1111992, 0.29751864579, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 106.38200591, 0.00765327, 129.20797555, 0.0678639, 12.92079755, 0.24757765, -143.95538104, -0.00810467, -174.84332237, -0.07278784, -17.48433224, -0.25250159, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 106.38200591, 0.00765327, 129.20797555, 0.06766486, 12.92079755, 0.24597257, -143.95538104, -0.00810467, -174.84332237, -0.07257402, -17.48433224, -0.25088173, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 30738029.83272482, 0.1125, 0.00189844, 0.00058594, 12807512.43030201, 0.00152995)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36833309174, 1211992, 0.36833309174, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 145.23519395, 0.00798744, 177.20825478, 0.07069111, 17.72082548, 0.24824283, -164.3063025, -0.00818125, -200.47780653, -0.07271462, -20.04778065, -0.25026634, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 145.23519395, 0.00798744, 177.20825478, 0.07063446, 17.72082548, 0.2478059, -164.3063025, -0.00818125, -200.47780653, -0.07265632, -20.04778065, -0.24982776, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29177647.35965841, 0.1125, 0.00189844, 0.00058594, 12157353.06652434, 0.00152995)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.36846368395, 1021992, 0.36846368395, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 144.66988442, 0.00791903, 175.47002817, 0.08192089, 17.54700282, 0.2996306, -163.68964956, -0.00810359, -198.5390915, -0.08426484, -19.85390915, -0.30197455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 144.66988442, 0.00791903, 175.47002817, 0.08267334, 17.54700282, 0.30567073, -163.68964956, -0.00810359, -198.5390915, -0.08503924, -19.85390915, -0.30803664, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 31171180.62367817, 0.1125, 0.00189844, 0.00058594, 12987991.92653257, 0.00152995)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.29987676893000004, 1121992, 0.29987676893000004, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 145.3247091, 0.00795697, 176.57357754, 0.06958075, 17.65735775, 0.2487088, -164.42354595, -0.00814453, -199.77919736, -0.0715665, -19.97791974, -0.25069455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 145.3247091, 0.00795697, 176.57357754, 0.06925617, 17.65735775, 0.24615432, -164.42354595, -0.00814453, -199.77919736, -0.07123245, -19.97791974, -0.2481306, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 30615551.30831674, 0.1125, 0.00189844, 0.00058594, 12756479.71179864, 0.00152995)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.3685361734, 1221992, 0.3685361734, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 61.87156462, 0.00719326, 75.4415969, 0.06548038, 7.54415969, 0.26956137, -92.37453877, -0.00761656, -112.63466117, -0.07164782, -11.26346612, -0.27572882, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 61.87156462, 0.00719326, 75.4415969, 0.06480978, 7.54415969, 0.26336506, -92.37453877, -0.00761656, -112.63466117, -0.07091114, -11.26346612, -0.26946642, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 29419036.48863567, 0.1125, 0.00189844, 0.00058594, 12257931.87026486, 0.00152995)
    ops.section('Aggregator', 1031991, 1031990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1031992, 1031991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.32674989835999996, 1031992, 0.32674989835999996, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 61.92379348, 0.00710202, 75.45226523, 0.07740602, 7.54522652, 0.32709572, -92.45033713, -0.00751977, -112.6479333, -0.08475218, -11.26479333, -0.33444188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 61.92379348, 0.00710202, 75.45226523, 0.07752431, 7.54522652, 0.32821167, -92.45033713, -0.00751977, -112.6479333, -0.08488212, -11.26479333, -0.33556948, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 29666113.27909523, 0.1125, 0.00189844, 0.00058594, 12360880.53295635, 0.00152995)
    ops.section('Aggregator', 1131991, 1131990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1131992, 1131991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.25806457992000004, 1131992, 0.25806457992000004, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 61.91745773, 0.0070819, 75.19612755, 0.0618703, 7.51961275, 0.26035722, -92.45744682, -0.00749027, -112.28564962, -0.06767802, -11.22856496, -0.26616494, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 61.91745773, 0.0070819, 75.19612755, 0.06257117, 7.51961275, 0.26713403, -92.45744682, -0.00749027, -112.28564962, -0.06844796, -11.22856496, -0.27301082, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 30766638.21203999, 0.1125, 0.00189844, 0.00058594, 12819432.58835, 0.00152995)
    ops.section('Aggregator', 1231991, 1231990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1231992, 1231991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.32600185618, 1231992, 0.32600185618, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 59.89055828, 0.00719374, 73.18582777, 0.05400086, 7.31858278, 0.25868072, -79.23815554, -0.00744287, -96.82845128, -0.05737995, -9.68284513, -0.26205981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 59.89055828, 0.00719374, 73.18582777, 0.05382411, 7.31858278, 0.25667533, -79.23815554, -0.00744287, -96.82845128, -0.05719138, -9.68284513, -0.26004259, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28617783.49298213, 0.1125, 0.00189844, 0.00058594, 11924076.45540922, 0.00152995)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32438984971, 1002992, 0.32438984971, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 61.19733767, 0.00719041, 74.47842368, 0.06367922, 7.44784237, 0.31971926, -80.98025913, -0.00743405, -98.55464761, -0.06770023, -9.85546476, -0.32374027, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 61.19733767, 0.00719041, 74.47842368, 0.06334271, 7.44784237, 0.3157794, -80.98025913, -0.00743405, -98.55464761, -0.06734121, -9.85546476, -0.3197779, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 30074053.67588359, 0.1125, 0.00189844, 0.00058594, 12530855.69828483, 0.00152995)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25795141629, 1102992, 0.25795141629, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 62.51755847, 0.00708679, 76.27220028, 0.05080353, 7.62722003, 0.24886982, -82.71513428, -0.00733503, -100.91349441, -0.05397508, -10.09134944, -0.25204137, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 62.51755847, 0.00708679, 76.27220028, 0.05079489, 7.62722003, 0.2487684, -82.71513428, -0.00733503, -100.91349441, -0.05396587, -10.09134944, -0.25193937, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 29217451.38481403, 0.1125, 0.00189844, 0.00058594, 12173938.07700585, 0.00152995)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.3263908828, 1202992, 0.3263908828, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 62.62217173, 0.00713835, 76.31194145, 0.06533116, 7.63119415, 0.26986065, -93.48798838, -0.00755937, -113.92530312, -0.07148704, -11.39253031, -0.27601653, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 62.59994344, 0.00711703, 76.28485386, 0.06575309, 7.62848539, 0.26996585, -113.27388205, -0.00775745, -138.03657102, -0.07511343, -13.8036571, -0.2793262, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 29626226.20142034, 0.1125, 0.00189844, 0.00058594, 12344260.91725848, 0.00152995)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32710953869000003, 1012992, 0.32710953869000003, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 62.37975714, 0.00717833, 75.70117953, 0.07713466, 7.57011795, 0.32969626, -112.9301902, -0.00780433, -137.04684011, -0.08816405, -13.70468401, -0.34072564, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 62.37975714, 0.00717833, 75.70117953, 0.07695637, 7.57011795, 0.32799373, -112.9301902, -0.00780433, -137.04684011, -0.08795924, -13.70468401, -0.33899661, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 31002782.25790391, 0.1125, 0.00189844, 0.00058594, 12917825.9407933, 0.00152995)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.25952506820000004, 1112992, 0.25952506820000004, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 62.60349048, 0.00707172, 76.10399884, 0.06461631, 7.61039988, 0.26850609, -113.29728699, -0.00769914, -137.72996572, -0.07380134, -13.77299657, -0.27769112, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 62.6245165, 0.00709244, 76.12955915, 0.06373325, 7.61295591, 0.2639854, -93.50150814, -0.00750513, -113.66520641, -0.06972784, -11.36652064, -0.26997999, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 30448535.44132333, 0.1125, 0.00189844, 0.00058594, 12686889.76721806, 0.00152995)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32680764323, 1212992, 0.32680764323, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 108.02712623, 0.00771213, 131.42819301, 0.06630906, 13.1428193, 0.24056825, -146.15483829, -0.00817278, -177.81521148, -0.07112238, -17.78152115, -0.24538157, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 108.02712623, 0.00771213, 131.42819301, 0.06687825, 13.1428193, 0.24517948, -146.15483829, -0.00817278, -177.81521148, -0.07173385, -17.78152115, -0.25003508, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 30184094.15564558, 0.1125, 0.00189844, 0.00058594, 12576705.89818566, 0.00152995)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.37020707848, 1022992, 0.37020707848, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 107.63960316, 0.00765206, 131.1006336, 0.08264045, 13.11006336, 0.30269835, -145.6119366, -0.00811294, -177.34938245, -0.08867158, -17.73493825, -0.30872948, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 107.63960316, 0.00765206, 131.1006336, 0.08173685, 13.11006336, 0.29555666, -145.6119366, -0.00811294, -177.34938245, -0.08770086, -17.73493825, -0.30152068, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29811291.08548203, 0.1125, 0.00189844, 0.00058594, 12421371.28561751, 0.00152995)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.30118170041000003, 1122992, 0.30118170041000003, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 109.53935422, 0.00760079, 132.84899269, 0.06572991, 13.28489927, 0.24190839, -148.17844997, -0.00804973, -179.71036945, -0.07049677, -17.97103695, -0.24667524, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 109.53935422, 0.00760079, 132.84899269, 0.06565222, 13.28489927, 0.2412726, -148.17844997, -0.00804973, -179.71036945, -0.0704133, -17.97103695, -0.24603369, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 31197398.15386972, 0.1125, 0.00189844, 0.00058594, 12998915.89744572, 0.00152995)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.37041961176, 1222992, 0.37041961176, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 62.58423138, 0.00710879, 76.00806634, 0.05140881, 7.60080663, 0.25480148, -82.81880946, -0.00734973, -100.58280535, -0.05461206, -10.05828054, -0.25800473, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 62.58423138, 0.00710879, 76.00806634, 0.05091214, 7.60080663, 0.24893721, -82.81880946, -0.00734973, -100.58280535, -0.05408218, -10.05828054, -0.25210725, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 30757497.87108343, 0.1125, 0.00189844, 0.00058594, 12815624.11295143, 0.00152995)
    ops.section('Aggregator', 1032991, 1032990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1032992, 1032991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.32682372435, 1032992, 0.32682372435, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 63.59754275, 0.00706258, 77.18761509, 0.06256722, 7.71876151, 0.3189947, -84.15099499, -0.00730316, -102.13310658, -0.06651935, -10.21331066, -0.32294684, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 63.59754275, 0.00706258, 77.18761509, 0.06210207, 7.71876151, 0.31346129, -84.15099499, -0.00730316, -102.13310658, -0.0660231, -10.21331066, -0.31738233, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 30967765.13783597, 0.1125, 0.00189844, 0.00058594, 12903235.47409832, 0.00152995)
    ops.section('Aggregator', 1132991, 1132990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1132992, 1132991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.25950254507, 1132992, 0.25950254507, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 62.61643076, 0.00716773, 76.05715463, 0.04991773, 7.60571546, 0.24896016, -82.86286433, -0.00741009, -100.64951975, -0.05301875, -10.06495198, -0.25206118, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 62.61643076, 0.00716773, 76.05715463, 0.04978186, 7.60571546, 0.24732692, -82.86286433, -0.00741009, -100.64951975, -0.05287379, -10.06495198, -0.25041886, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 30715402.58939965, 0.1125, 0.00189844, 0.00058594, 12798084.41224985, 0.00152995)
    ops.section('Aggregator', 1232991, 1232990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1232992, 1232991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.3273557002, 1232992, 0.3273557002, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 61.77556269, 0.00709239, 75.04969902, 0.04941149, 7.5049699, 0.24769692, -61.77556269, -0.00709239, -75.04969902, -0.04941149, -7.5049699, -0.24769692, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 61.77556269, 0.00709239, 75.04969902, 0.04938216, 7.5049699, 0.24734176, -61.77556269, -0.00709239, -75.04969902, -0.04938216, -7.5049699, -0.24734176, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 30655741.65503491, 0.1125, 0.00189844, 0.00058594, 12773225.68959788, 0.00152995)
    ops.section('Aggregator', 1003991, 1003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1003992, 1003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.32560719152, 1003992, 0.32560719152, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 63.14218014, 0.0071843, 76.74747954, 0.06055373, 7.67474795, 0.3107968, -63.14218014, -0.0071843, -76.74747954, -0.06055373, -7.67474795, -0.3107968, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 63.14218014, 0.0071843, 76.74747954, 0.06087332, 7.67474795, 0.31468557, -63.14218014, -0.0071843, -76.74747954, -0.06087332, -7.67474795, -0.31468557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 30497042.88276578, 0.1125, 0.00189844, 0.00058594, 12707101.20115241, 0.00152995)
    ops.section('Aggregator', 1103991, 1103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1103992, 1103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.25981299528, 1103992, 0.25981299528, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 61.98068343, 0.00730824, 75.38288872, 0.05078152, 7.53828887, 0.25187854, -61.98068343, -0.00730824, -75.38288872, -0.05078152, -7.53828887, -0.25187854, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 61.98068343, 0.00730824, 75.38288872, 0.05101389, 7.53828887, 0.25467006, -61.98068343, -0.00730824, -75.38288872, -0.05101389, -7.53828887, -0.25467006, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 30290964.32201796, 0.1125, 0.00189844, 0.00058594, 12621235.13417415, 0.00152995)
    ops.section('Aggregator', 1203991, 1203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1203992, 1203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.32759278526, 1203992, 0.32759278526, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 63.501822, 0.00714508, 77.05410733, 0.05035336, 7.70541073, 0.25263701, -63.501822, -0.00714508, -77.05410733, -0.05035336, -7.70541073, -0.25263701, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 63.48735981, 0.00712204, 77.03655869, 0.05066864, 7.70365587, 0.25274048, -84.01166709, -0.0073633, -101.94107521, -0.05382183, -10.19410752, -0.25589368, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 31038457.94933983, 0.1125, 0.00189844, 0.00058594, 12932690.81222493, 0.00152995)
    ops.section('Aggregator', 1013991, 1013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1013992, 1013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.32791480560999997, 1013992, 0.32791480560999997, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 62.39315793, 0.00713784, 76.15672032, 0.06278707, 7.61567203, 0.31372546, -82.5528754, -0.00738787, -100.76355249, -0.06675832, -10.07635525, -0.31769671, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 62.39315793, 0.00713784, 76.15672032, 0.06320317, 7.61567203, 0.31861521, -82.5528754, -0.00738787, -100.76355249, -0.06720225, -10.07635525, -0.32261429, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 29044205.58932386, 0.1125, 0.00189844, 0.00058594, 12101752.32888494, 0.00152995)
    ops.section('Aggregator', 1113991, 1113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1113992, 1113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.25867756591, 1113992, 0.25867756591, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 61.78153062, 0.00696931, 74.98496992, 0.05045163, 7.49849699, 0.25158415, -81.75602652, -0.00720523, -99.22825038, -0.05359517, -9.92282504, -0.25472769, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 61.79936976, 0.00699142, 75.0066215, 0.04991217, 7.50066215, 0.24878765, -61.79936976, -0.00699142, -75.0066215, -0.04991217, -7.50066215, -0.24878765, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 30961761.65478744, 0.1125, 0.00189844, 0.00058594, 12900734.0228281, 0.00152995)
    ops.section('Aggregator', 1213991, 1213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1213992, 1213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.32480388345, 1213992, 0.32480388345, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 61.79463148, 0.00714143, 75.13651774, 0.0494133, 7.51365177, 0.24700097, -61.79463148, -0.00714143, -75.13651774, -0.0494133, -7.51365177, -0.24700097, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 61.76450852, 0.00712027, 75.09989102, 0.05022731, 7.5099891, 0.25319398, -81.73390283, -0.00736197, -99.38081501, -0.05335155, -9.9380815, -0.25631822, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 30379367.76193625, 0.1125, 0.00189844, 0.00058594, 12658069.90080677, 0.00152995)
    ops.section('Aggregator', 1023991, 1023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1023992, 1023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.32601069937, 1023992, 0.32601069937, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 62.44192853, 0.00724889, 75.8057083, 0.06272789, 7.58057083, 0.31887988, -82.63346753, -0.00749171, -100.31862696, -0.06668055, -10.0318627, -0.32283254, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 62.44192853, 0.00724889, 75.8057083, 0.06274271, 7.58057083, 0.31905705, -82.63346753, -0.00749171, -100.31862696, -0.06669636, -10.0318627, -0.3230107, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 30881630.05786519, 0.1125, 0.00189844, 0.00058594, 12867345.85744383, 0.00152995)
    ops.section('Aggregator', 1123991, 1123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1123992, 1123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.25986947681, 1123992, 0.25986947681, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 62.37234808, 0.00721227, 75.30629365, 0.04878637, 7.53062937, 0.24927235, -82.55041413, -0.00744653, -99.66861789, -0.05180065, -9.96686179, -0.25228663, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 62.40991891, 0.00723049, 75.35165542, 0.04857785, 7.53516554, 0.25038684, -62.40991891, -0.00723049, -75.35165542, -0.04857785, -7.53516554, -0.25038684, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 32520731.52520507, 0.1125, 0.00189844, 0.00058594, 13550304.80216878, 0.00152995)
    ops.section('Aggregator', 1223991, 1223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1223992, 1223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.32765078358, 1223992, 0.32765078358, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 62.71459258, 0.00692267, 75.57062911, 0.04886587, 7.55706291, 0.25253018, -62.71459258, -0.00692267, -75.57062911, -0.04886587, -7.55706291, -0.25253018, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 62.71459258, 0.00692267, 75.57062911, 0.04880559, 7.55706291, 0.25177626, -62.71459258, -0.00692267, -75.57062911, -0.04880559, -7.55706291, -0.25177626, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 33063414.96690313, 0.1125, 0.00189844, 0.00058594, 13776422.9028763, 0.00152995)
    ops.section('Aggregator', 1033991, 1033990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1033992, 1033991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.32538560497999997, 1033992, 0.32538560497999997, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 62.47266114, 0.00706176, 75.52286756, 0.06144339, 7.55228676, 0.31976946, -62.47266114, -0.00706176, -75.52286756, -0.06144339, -7.55228676, -0.31976946, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 62.47266114, 0.00706176, 75.52286756, 0.061019, 7.55228676, 0.31458864, -62.47266114, -0.00706176, -75.52286756, -0.061019, -7.55228676, -0.31458864, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 32160514.95818883, 0.1125, 0.00189844, 0.00058594, 13400214.56591201, 0.00152995)
    ops.section('Aggregator', 1133991, 1133990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1133992, 1133991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.25824725915, 1133992, 0.25824725915, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 62.58983412, 0.00736306, 76.19432269, 0.05115248, 7.61943227, 0.25263864, -62.58983412, -0.00736306, -76.19432269, -0.05115248, -7.61943227, -0.25263864, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 62.58983412, 0.00736306, 76.19432269, 0.05132538, 7.61943227, 0.25470383, -62.58983412, -0.00736306, -76.19432269, -0.05132538, -7.61943227, -0.25470383, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 29979801.1643937, 0.1125, 0.00189844, 0.00058594, 12491583.81849738, 0.00152995)
    ops.section('Aggregator', 1233991, 1233990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1233992, 1233991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.32867011285000003, 1233992, 0.32867011285000003, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 78.56967174, 0.010403, 95.64930226, 0.08681027, 9.56493023, 0.30476398, -106.06300085, -0.01112474, -129.11918559, -0.09320766, -12.91191856, -0.31116138, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 78.56967174, 0.010403, 95.64930226, 0.086562, 9.56493023, 0.30283958, -106.06300085, -0.01112474, -129.11918559, -0.09294096, -12.91191856, -0.30921853, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 29973494.90156886, 0.0875, 0.00089323, 0.00045573, 12488956.20898703, 0.0010204)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.29865619724, 6200992, 0.29865619724, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 66.67034973, 0.01272133, 80.98021136, 0.0892976, 8.09802114, 0.30670078, -89.84691681, -0.01367983, -109.13130564, -0.0959443, -10.91313056, -0.31334748, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 66.67034973, 0.01272133, 80.98021136, 0.0896845, 8.09802114, 0.30970233, -89.84691681, -0.01367983, -109.13130564, -0.09635995, -10.91313056, -0.31637778, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 30719538.58974668, 0.075, 0.0005625, 0.00039062, 12799807.74572778, 0.00077515)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.30069416310999997, 6201992, 0.30069416310999997, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 6202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6202990, 38.21521285, 0.01199797, 46.50808225, 0.08641154, 4.65080822, 0.34253526, -56.74780105, -0.01287265, -69.06232366, -0.09461963, -6.90623237, -0.35074335, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6202991, 38.21521285, 0.01199797, 46.50808225, 0.08663378, 4.65080822, 0.34457571, -56.74780105, -0.01287265, -69.06232366, -0.09486377, -6.90623237, -0.3528057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6202990, 30078557.98516867, 0.075, 0.0005625, 0.00039062, 12532732.49382028, 0.00077515)
    ops.section('Aggregator', 6202991, 6202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6202992, 6202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6202, 6202991, 0.25848603465000003, 6202992, 0.25848603465000003, 6202990)
    # Create element
    ops.element('forceBeamColumn', 6202, 1103, 1203, 6202, 6202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 61.60011805, 0.00702451, 74.75051235, 0.06386169, 7.47505123, 0.26723934, -111.51164273, -0.00763883, -135.31715021, -0.07292842, -13.53171502, -0.27630607, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 61.60011805, 0.00702451, 74.75051235, 0.06401602, 7.47505123, 0.26870606, -111.51164273, -0.00763883, -135.31715021, -0.0731057, -13.53171502, -0.27779574, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 31021830.20629614, 0.1125, 0.00189844, 0.00058594, 12925762.58595672, 0.00152995)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32539328186, 2001992, 0.32539328186, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 184.16034423, 0.00684635, 222.83675056, 0.0704688, 22.28367506, 0.29000549, -248.43608067, -0.00733429, -300.61134588, -0.07568271, -30.06113459, -0.2952194, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 184.16034423, 0.00684635, 222.83675056, 0.07039648, 22.28367506, 0.28934169, -248.43608067, -0.00733429, -300.61134588, -0.07560501, -30.06113459, -0.29455022, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 31890637.8736608, 0.125, 0.00260417, 0.00065104, 13287765.780692, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.40722185251000004, 2101992, 0.40722185251000004, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 184.37921975, 0.00720788, 224.75460294, 0.07513137, 22.47546029, 0.29936422, -248.81445669, -0.00773849, -303.29987563, -0.08070744, -30.32998756, -0.30494028, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 184.37921975, 0.00720788, 224.75460294, 0.0743097, 22.47546029, 0.29216142, -248.81445669, -0.00773849, -303.29987563, -0.07982473, -30.32998756, -0.29767645, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29519366.99638949, 0.125, 0.00260417, 0.00065104, 12299736.24849562, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41200842692, 2201992, 0.41200842692, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 60.91410371, 0.00708778, 74.17289813, 0.06584799, 7.41728981, 0.27080598, -110.25542971, -0.00771701, -134.25404395, -0.07521561, -13.42540439, -0.2801736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 60.91410371, 0.00708778, 74.17289813, 0.06584787, 7.41728981, 0.27080487, -110.25542971, -0.00771701, -134.25404395, -0.07521548, -13.42540439, -0.28017248, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29894536.94563436, 0.1125, 0.00189844, 0.00058594, 12456057.06068098, 0.00152995)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.32507862329, 2301992, 0.32507862329, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 62.99320952, 0.00713328, 76.59641918, 0.06314061, 7.65964192, 0.26294458, -114.0039773, -0.00776662, -138.62282141, -0.07210295, -13.86228214, -0.27190691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 62.99320952, 0.00713328, 76.59641918, 0.06311995, 7.65964192, 0.26274912, -114.0039773, -0.00776662, -138.62282141, -0.07207921, -13.86228214, -0.27170838, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 30368424.77367707, 0.1125, 0.00189844, 0.00058594, 12653510.32236544, 0.00152995)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32773952444000004, 2011992, 0.32773952444000004, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 188.72536592, 0.00714118, 230.04700804, 0.0746207, 23.0047008, 0.29788047, -254.51175908, -0.00767091, -310.23740981, -0.08016291, -31.02374098, -0.30342267, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 188.72536592, 0.00714118, 230.04700804, 0.07472442, 23.0047008, 0.29879903, -254.51175908, -0.00767091, -310.23740981, -0.08027433, -31.02374098, -0.30434894, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29527729.43802147, 0.125, 0.00260417, 0.00065104, 12303220.59917562, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41356579542, 2111992, 0.41356579542, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 184.63402021, 0.0070295, 224.91685265, 0.07407648, 22.49168527, 0.29592475, -249.04495207, -0.00754794, -303.38074601, -0.07957528, -30.3380746, -0.30142355, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 184.63402021, 0.0070295, 224.91685265, 0.07456295, 22.49168527, 0.30024849, -249.04495207, -0.00754794, -303.38074601, -0.08009788, -30.3380746, -0.30578342, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29749626.9740264, 0.125, 0.00260417, 0.00065104, 12395677.90584433, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.40963380619, 2211992, 0.40963380619, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 60.98511873, 0.00690273, 74.56953023, 0.06555033, 7.45695302, 0.26559642, -110.29838421, -0.00754097, -134.86730645, -0.07491021, -13.48673064, -0.2749563, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 60.98511873, 0.00690273, 74.56953023, 0.06631717, 7.45695302, 0.27262366, -110.29838421, -0.00754097, -134.86730645, -0.0757911, -13.48673064, -0.28209758, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28380919.27694756, 0.1125, 0.00189844, 0.00058594, 11825383.03206148, 0.00152995)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32343795812000004, 2311992, 0.32343795812000004, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 62.12333888, 0.00704282, 75.56836295, 0.06492549, 7.55683629, 0.26885579, -112.42725993, -0.00766948, -136.75929428, -0.07416004, -13.67592943, -0.27809034, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 62.12333888, 0.00704282, 75.56836295, 0.06482556, 7.55683629, 0.26792171, -112.42725993, -0.00766948, -136.75929428, -0.07404525, -13.67592943, -0.2771414, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 30238283.60885995, 0.1125, 0.00189844, 0.00058594, 12599284.83702498, 0.00152995)
    ops.section('Aggregator', 2021991, 2021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2021992, 2021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.32603161579, 2021992, 0.32603161579, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 179.76391181, 0.00699527, 219.03142648, 0.07383023, 21.90314265, 0.2939428, -242.57633003, -0.00750923, -295.56454943, -0.07930879, -29.55645494, -0.29942137, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 179.76391181, 0.00699527, 219.03142648, 0.07369509, 21.90314265, 0.29275338, -242.57633003, -0.00750923, -295.56454943, -0.07916362, -29.55645494, -0.29822191, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 29674779.45085122, 0.125, 0.00260417, 0.00065104, 12364491.43785467, 0.00178813)
    ops.section('Aggregator', 2121991, 2121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2121992, 2121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.40628136409000004, 2121992, 0.40628136409000004, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 182.9103144, 0.00719764, 223.34198728, 0.07419625, 22.33419873, 0.29303403, -246.81919451, -0.00773309, -301.37769748, -0.07970846, -30.13776975, -0.29854624, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 182.9103144, 0.00719764, 223.34198728, 0.07467727, 22.33419873, 0.29726034, -246.81919451, -0.00773309, -301.37769748, -0.08022521, -30.13776975, -0.30280828, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 28907845.36571095, 0.125, 0.00260417, 0.00065104, 12044935.56904623, 0.00178813)
    ops.section('Aggregator', 2221991, 2221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2221992, 2221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.41082279525000004, 2221992, 0.41082279525000004, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 62.40857931, 0.00715673, 75.92182083, 0.06235194, 7.59218208, 0.25944389, -112.95776876, -0.00779135, -137.41635487, -0.07119479, -13.74163549, -0.26828674, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 62.40857931, 0.00715673, 75.92182083, 0.06305208, 7.59218208, 0.26612614, -112.95776876, -0.00779135, -137.41635487, -0.07199905, -13.74163549, -0.27507311, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 30209795.24527252, 0.1125, 0.00189844, 0.00058594, 12587414.68553022, 0.00152995)
    ops.section('Aggregator', 2321991, 2321990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2321992, 2321991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.32730033823000004, 2321992, 0.32730033823000004, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 60.57336317, 0.00690785, 73.93737226, 0.06558489, 7.39373723, 0.26850991, -90.41868768, -0.00731994, -110.36732682, -0.07177955, -11.03673268, -0.27470457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 60.55361798, 0.00688647, 73.91327077, 0.06618819, 7.39132708, 0.27024684, -109.55148392, -0.00751359, -133.72129966, -0.07563423, -13.37212997, -0.27969288, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 29034882.14128047, 0.1125, 0.00189844, 0.00058594, 12097867.55886686, 0.00152995)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32291298612, 2002992, 0.32291298612, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 162.72154346, 0.00801844, 198.01805952, 0.07594558, 19.80180595, 0.2984432, -219.33742653, -0.00864312, -266.9146977, -0.08161598, -26.69146977, -0.30411361, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 162.72154346, 0.00801844, 198.01805952, 0.07595726, 19.80180595, 0.2985457, -219.33742653, -0.00864312, -266.9146977, -0.08162853, -26.69146977, -0.30421697, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 30103701.33765722, 0.1125, 0.00189844, 0.00058594, 12543208.89069051, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.40930706991, 2102992, 0.40930706991, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 164.89350699, 0.00821509, 201.10810896, 0.07729636, 20.1108109, 0.30116898, -222.26130238, -0.00886306, -271.07525961, -0.0830758, -27.10752596, -0.30694842, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 164.89350699, 0.00821509, 201.10810896, 0.07694868, 20.1108109, 0.29815779, -222.26130238, -0.00886306, -271.07525961, -0.08270229, -27.10752596, -0.3039114, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 29331826.80961018, 0.1125, 0.00189844, 0.00058594, 12221594.50400424, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.41301574360000004, 2202992, 0.41301574360000004, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 62.08657741, 0.00718454, 75.73578935, 0.06379045, 7.57357893, 0.26306643, -92.69142395, -0.00760921, -113.06885404, -0.06979359, -11.3068854, -0.26906957, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 62.05707529, 0.00716404, 75.69980144, 0.06470038, 7.56998014, 0.26782397, -112.30083139, -0.00780998, -136.9892248, -0.0739027, -13.69892248, -0.27702629, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29267908.74294348, 0.1125, 0.00189844, 0.00058594, 12194961.97622645, 0.00152995)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.3268917742, 2302992, 0.3268917742, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 62.25598605, 0.00730355, 76.0205881, 0.06564403, 7.60205881, 0.2675634, -112.66249972, -0.00796344, -137.57182286, -0.07497988, -13.75718229, -0.27689925, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 62.25598605, 0.00730355, 76.0205881, 0.06496827, 7.60205881, 0.26138365, -112.66249972, -0.00796344, -137.57182286, -0.07420362, -13.75718229, -0.27061901, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28892558.99538959, 0.1125, 0.00189844, 0.00058594, 12038566.248079, 0.00152995)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32822950569, 2012992, 0.32822950569, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 163.78494947, 0.00806288, 200.04864918, 0.07589386, 20.00486492, 0.29340253, -220.68061858, -0.00870737, -269.54161412, -0.08157695, -26.95416141, -0.29908562, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 163.78494947, 0.00806288, 200.04864918, 0.07626234, 20.00486492, 0.29658426, -220.68061858, -0.00870737, -269.54161412, -0.0819728, -26.95416141, -0.30229472, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28797046.77646059, 0.1125, 0.00189844, 0.00058594, 11998769.49019191, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.41019769848, 2112992, 0.41019769848, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 166.8674516, 0.00812082, 202.94025374, 0.07529736, 20.29402537, 0.29728147, -224.8846034, -0.00875285, -273.49934357, -0.08091938, -27.34993436, -0.30290349, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 166.8674516, 0.00812082, 202.94025374, 0.07476073, 20.29402537, 0.29256142, -224.8846034, -0.00875285, -273.49934357, -0.08034288, -27.34993436, -0.29814357, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 30306121.56678017, 0.1125, 0.00189844, 0.00058594, 12627550.65282507, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.41339409809, 2212992, 0.41339409809, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 60.91136587, 0.00701316, 74.06955592, 0.06503368, 7.40695559, 0.26922131, -110.2553903, -0.00763248, -134.07297113, -0.07428139, -13.40729711, -0.27846902, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 60.91136587, 0.00701316, 74.06955592, 0.06474513, 7.40695559, 0.26653218, -110.2553903, -0.00763248, -134.07297113, -0.07394993, -13.40729711, -0.27573698, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 30348151.49521989, 0.1125, 0.00189844, 0.00058594, 12645063.12300829, 0.00152995)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.3244957028, 2312992, 0.3244957028, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 62.0218079, 0.00707646, 75.56821849, 0.063623, 7.55682185, 0.26245873, -112.23512481, -0.00771173, -136.74881015, -0.07266746, -13.67488101, -0.27150319, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 62.04607048, 0.00709726, 75.59778034, 0.06384881, 7.55977803, 0.26835797, -92.63146951, -0.00751495, -112.86344858, -0.06985932, -11.28634486, -0.27436849, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 29682119.09709789, 0.1125, 0.00189844, 0.00058594, 12367549.62379079, 0.00152995)
    ops.section('Aggregator', 2022991, 2022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2022992, 2022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.32615570107999997, 2022992, 0.32615570107999997, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 166.72724247, 0.00796263, 202.54054581, 0.07570886, 20.25405458, 0.30052591, -224.63176337, -0.00858071, -272.88305909, -0.08135924, -27.28830591, -0.30617629, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 166.72724247, 0.00796263, 202.54054581, 0.07560083, 20.25405458, 0.2995684, -224.63176337, -0.00858071, -272.88305909, -0.08124318, -27.28830591, -0.30521075, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 30675666.01145393, 0.1125, 0.00189844, 0.00058594, 12781527.50477247, 0.00152995)
    ops.section('Aggregator', 2122991, 2122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2122992, 2122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.41135648004, 2122992, 0.41135648004, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 161.33994261, 0.00804716, 197.55347188, 0.08009957, 19.75534719, 0.30622207, -217.37726361, -0.00870121, -266.1686402, -0.08610578, -26.61686402, -0.31222828, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 161.33994261, 0.00804716, 197.55347188, 0.08001033, 19.75534719, 0.30546904, -217.37726361, -0.00870121, -266.1686402, -0.08600991, -26.61686402, -0.31146862, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 27830232.21334922, 0.1125, 0.00189844, 0.00058594, 11595930.08889551, 0.00152995)
    ops.section('Aggregator', 2222991, 2222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2222992, 2222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.40809857971, 2222992, 0.40809857971, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 62.04671964, 0.007268, 75.60179324, 0.06295138, 7.56017932, 0.25994007, -112.30233198, -0.00791465, -136.83652789, -0.07187885, -13.68365279, -0.26886754, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 62.08409911, 0.00728683, 75.64733883, 0.06309128, 7.56473388, 0.26500643, -92.6966134, -0.00771225, -112.9476343, -0.06901619, -11.29476343, -0.27093134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 29667282.67081754, 0.1125, 0.00189844, 0.00058594, 12361367.77950731, 0.00152995)
    ops.section('Aggregator', 2322991, 2322990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2322992, 2322991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.32778245257, 2322992, 0.32778245257, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 63.00917649, 0.00717208, 77.00850759, 0.05168746, 7.70085076, 0.25172803, -63.00917649, -0.00717208, -77.00850759, -0.05168746, -7.70085076, -0.25172803, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 62.99786624, 0.00714636, 76.99468444, 0.0519022, 7.69946844, 0.2505931, -83.34376129, -0.00740021, -101.86101503, -0.05514884, -10.1861015, -0.25383973, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 28559829.91186772, 0.1125, 0.00189844, 0.00058594, 11899929.12994489, 0.00152995)
    ops.section('Aggregator', 2003991, 2003990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2003992, 2003991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.32732632693, 2003992, 0.32732632693, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 109.6227169, 0.00769035, 133.34718612, 0.06587117, 13.33471861, 0.23944119, -148.28259218, -0.00815141, -180.37380368, -0.07065399, -18.03738037, -0.24422401, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 109.6227169, 0.00769035, 133.34718612, 0.06585747, 13.33471861, 0.23933054, -148.28259218, -0.00815141, -180.37380368, -0.07063927, -18.03738037, -0.24411234, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 30239764.64957631, 0.1125, 0.00189844, 0.00058594, 12599901.93732346, 0.00152995)
    ops.section('Aggregator', 2103991, 2103990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2103992, 2103991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.37127860125, 2103992, 0.37127860125, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 109.76574377, 0.00759093, 132.82055619, 0.06529439, 13.28205562, 0.24265935, -148.4998481, -0.00803413, -179.69023615, -0.07002389, -17.96902361, -0.24738884, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 109.76574377, 0.00759093, 132.82055619, 0.06502371, 13.28205562, 0.24042145, -148.4998481, -0.00803413, -179.69023615, -0.0697331, -17.96902361, -0.24513084, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 31885371.11828148, 0.1125, 0.00189844, 0.00058594, 13285571.29928395, 0.00152995)
    ops.section('Aggregator', 2203991, 2203990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2203992, 2203991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.37061768329, 2203992, 0.37061768329, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 62.96513771, 0.00726839, 76.72409985, 0.05088445, 7.67240999, 0.2510312, -62.96513771, -0.00726839, -76.72409985, -0.05088445, -7.67240999, -0.2510312, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 62.93787323, 0.00724563, 76.69087762, 0.05124197, 7.66908776, 0.2515977, -83.28087216, -0.00749549, -101.4791706, -0.05443385, -10.14791706, -0.25478957, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 29652537.86489986, 0.1125, 0.00189844, 0.00058594, 12355224.11037494, 0.00152995)
    ops.section('Aggregator', 2303991, 2303990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2303992, 2303991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.32824029464, 2303992, 0.32824029464, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 61.5583756, 0.0072786, 74.84538874, 0.05189367, 7.48453887, 0.25532914, -81.45749495, -0.00752289, -99.03961591, -0.05512134, -9.90396159, -0.25855682, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 61.5583756, 0.0072786, 74.84538874, 0.05143877, 7.48453887, 0.24998832, -81.45749495, -0.00752289, -99.03961591, -0.05463603, -9.90396159, -0.25318558, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 30396370.24517302, 0.1125, 0.00189844, 0.00058594, 12665154.26882209, 0.00152995)
    ops.section('Aggregator', 2013991, 2013990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2013992, 2013991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.32710346758, 2013992, 0.32710346758, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 107.75829244, 0.00761789, 131.2834922, 0.06844673, 13.12834922, 0.24672956, -145.75867453, -0.00807831, -177.57990941, -0.07342561, -17.75799094, -0.25170844, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 107.75829244, 0.00761789, 131.2834922, 0.06843206, 13.12834922, 0.24661289, -145.75867453, -0.00807831, -177.57990941, -0.07340985, -17.75799094, -0.25159068, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 29710401.26112488, 0.1125, 0.00189844, 0.00058594, 12379333.85880203, 0.00152995)
    ops.section('Aggregator', 2113991, 2113990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2113992, 2113991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.36889302891000003, 2113992, 0.36889302891000003, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.15, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 108.41743615, 0.00756448, 131.69845252, 0.06607784, 13.16984525, 0.24140939, -146.65591295, -0.0080148, -178.14806801, -0.07087461, -17.8148068, -0.24620617, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 108.41743615, 0.00756448, 131.69845252, 0.06687119, 13.16984525, 0.24789426, -146.65591295, -0.0080148, -178.14806801, -0.07172689, -17.8148068, -0.25274997, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 30693362.39054975, 0.1125, 0.00189844, 0.00058594, 12788900.9960624, 0.00152995)
    ops.section('Aggregator', 2213991, 2213990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2213992, 2213991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.36903322673000005, 2213992, 0.36903322673000005, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 62.03625263, 0.00715683, 75.57569201, 0.05165332, 7.5575692, 0.25302381, -82.088791, -0.00740302, -100.00470569, -0.05487496, -10.00047057, -0.25624545, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 62.03625263, 0.00715683, 75.57569201, 0.05191558, 7.5575692, 0.25611286, -82.088791, -0.00740302, -100.00470569, -0.05515476, -10.00047057, -0.25935203, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 29728647.65513657, 0.1125, 0.00189844, 0.00058594, 12386936.52297357, 0.00152995)
    ops.section('Aggregator', 2313991, 2313990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2313992, 2313991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.32653836566, 2313992, 0.32653836566, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 62.82928352, 0.00726541, 76.56368208, 0.0518517, 7.65636821, 0.2536395, -83.13771921, -0.00751561, -101.31151504, -0.05508336, -10.1311515, -0.25687116, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 62.85932442, 0.00728779, 76.60028988, 0.05101355, 7.66002899, 0.24748865, -62.85932442, -0.00728779, -76.60028988, -0.05101355, -7.66002899, -0.24748865, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 29629181.95220903, 0.1125, 0.00189844, 0.00058594, 12345492.48008709, 0.00152995)
    ops.section('Aggregator', 2023991, 2023990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2023992, 2023991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.32828871482, 2023992, 0.32828871482, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 109.17594822, 0.00763336, 133.2326417, 0.06938348, 13.32326417, 0.24855041, -147.63096564, -0.00810147, -180.16114235, -0.07443848, -18.01611423, -0.25360541, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 109.17594822, 0.00763336, 133.2326417, 0.06919647, 13.32326417, 0.24707902, -147.63096564, -0.00810147, -180.16114235, -0.07423759, -18.01611423, -0.25212014, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 29117814.28341446, 0.1125, 0.00189844, 0.00058594, 12132422.61808936, 0.00152995)
    ops.section('Aggregator', 2123991, 2123990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2123992, 2123991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.37008122917999997, 2123992, 0.37008122917999997, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 109.27469777, 0.00756344, 133.29696896, 0.069044, 13.3296969, 0.24782501, -147.74514748, -0.00802711, -180.22452352, -0.07407454, -18.02245235, -0.25285555, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 109.27469777, 0.00756344, 133.29696896, 0.0687921, 13.3296969, 0.24584043, -147.74514748, -0.00802711, -180.22452352, -0.07380393, -18.02245235, -0.25085226, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 29270207.00851051, 0.1125, 0.00189844, 0.00058594, 12195919.58687938, 0.00152995)
    ops.section('Aggregator', 2223991, 2223990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2223992, 2223991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.36942695857, 2223992, 0.36942695857, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 60.43918337, 0.00711716, 73.40855666, 0.05010912, 7.34085567, 0.24925, -79.97923519, -0.00735481, -97.14162055, -0.0532216, -9.71416206, -0.25236249, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 60.48040184, 0.00713557, 73.45862001, 0.05017224, 7.345862, 0.25374582, -60.48040184, -0.00713557, -73.45862001, -0.05017224, -7.345862, -0.25374582, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 30732896.78823241, 0.1125, 0.00189844, 0.00058594, 12805373.66176351, 0.00152995)
    ops.section('Aggregator', 2323991, 2323990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2323992, 2323991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.32458746618, 2323992, 0.32458746618, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)
