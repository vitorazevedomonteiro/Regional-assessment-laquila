import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 30.89165945, 0.0098734, 37.8484265, 0.07354389, 3.78484265, 0.31294224, -53.57456604, -0.01074832, -65.6394982, -0.08321872, -6.56394982, -0.32261707, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 30.81969133, 0.00982495, 37.76025124, 0.07466653, 3.77602512, 0.31106229, -79.06557981, -0.01147549, -96.87105968, -0.09232857, -9.68710597, -0.32872433, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 27582024.89991548, 0.07, 0.00071458, 0.00023333, 11492510.37496478, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32773726693, 1001992, 0.32773726693, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 30.7433119, 0.00973159, 37.45073815, 0.08827323, 3.74507382, 0.38813426, -78.8859069, -0.0112932, -96.09685037, -0.10922933, -9.60968504, -0.40909036, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 30.7433119, 0.00973159, 37.45073815, 0.08860349, 3.74507382, 0.39146402, -78.8859069, -0.0112932, -96.09685037, -0.10964114, -9.60968504, -0.41250167, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 29750057.76286985, 0.07, 0.00071458, 0.00023333, 12395857.40119577, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25913761388, 1101992, 0.25913761388, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 31.73457816, 0.00959407, 38.5032157, 0.07182127, 3.85032157, 0.31480503, -81.55304354, -0.01111954, -98.94741347, -0.08871266, -9.89474135, -0.33169642, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.79806628, 0.00964369, 38.58024514, 0.07048651, 3.85802451, 0.31407526, -55.21134267, -0.01045488, -66.98731665, -0.0797068, -6.69873167, -0.32329555, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 31071140.41784862, 0.07, 0.00071458, 0.00023333, 12946308.50743693, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32872980071, 1201992, 0.32872980071, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 36.21688636, 0.00796765, 44.3485863, 0.09011127, 4.43485863, 0.36635893, -147.15906524, -0.01006465, -180.20037504, -0.1243565, -18.0200375, -0.40060416, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.76458778, 0.00823799, 65.83623554, 0.09107013, 6.58362355, 0.36671268, -147.19928553, -0.01000704, -180.24962591, -0.11520802, -18.02496259, -0.39085057, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 27806091.79193531, 0.1, 0.00133333, 0.00052083, 11585871.57997305, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.32662680231, 1011992, 0.32662680231, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 54.13763108, 0.00825134, 66.28818151, 0.11532705, 6.62881815, 0.47209305, -148.21134249, -0.0100249, -181.4756238, -0.14601643, -18.14756238, -0.50278243, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 54.13763108, 0.00825134, 66.28818151, 0.11394976, 6.62881815, 0.45992614, -148.21134249, -0.0100249, -181.4756238, -0.1442672, -18.14756238, -0.49024358, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27835735.00585717, 0.1, 0.00133333, 0.00052083, 11598222.91910715, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25919845756000004, 1111992, 0.25919845756000004, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 53.56878641, 0.00817543, 65.65631072, 0.09312787, 6.56563107, 0.37377266, -146.62520229, -0.00994747, -179.71043376, -0.11784133, -17.97104338, -0.39848613, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 36.07432467, 0.0079052, 44.21431263, 0.09248194, 4.42143126, 0.37636688, -146.57075975, -0.01000634, -179.64370653, -0.12768356, -17.96437065, -0.4115685, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 27430770.3248963, 0.1, 0.00133333, 0.00052083, 11429487.63537346, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.3259070829, 1211992, 0.3259070829, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 30.53847922, 0.00953942, 37.23224051, 0.07195831, 3.72322405, 0.31267961, -52.99110381, -0.0103589, -64.60627944, -0.08140471, -6.46062794, -0.32212601, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.47188249, 0.00949346, 37.15104638, 0.07337877, 3.71510464, 0.31391454, -78.23766878, -0.01103651, -95.38666548, -0.09069719, -9.53866655, -0.33123296, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 29458243.24841195, 0.07, 0.00071458, 0.00023333, 12274268.02017165, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32515307733, 1021992, 0.32515307733, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 30.9856105, 0.00953814, 37.74978217, 0.09152725, 3.77497822, 0.40111712, -79.58427811, -0.01108732, -96.95755914, -0.11332221, -9.69575591, -0.42291207, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 30.9856105, 0.00953814, 37.74978217, 0.09119038, 3.77497822, 0.39777134, -79.58427811, -0.01108732, -96.95755914, -0.11290214, -9.69575591, -0.41948311, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29714419.10524311, 0.07, 0.00071458, 0.00023333, 12381007.96051796, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25861529591, 1121992, 0.25861529591, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 31.42276827, 0.00976574, 38.41443065, 0.07477251, 3.84144306, 0.31672839, -80.67746982, -0.01139008, -98.62845444, -0.09244913, -9.86284544, -0.33440501, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 31.49219138, 0.00981842, 38.4993006, 0.07324521, 3.84993006, 0.31459442, -54.6468458, -0.01068003, -66.8059367, -0.08287304, -6.68059367, -0.32422225, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 28458565.48629918, 0.07, 0.00071458, 0.00023333, 11857735.61929133, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32886719549, 1221992, 0.32886719549, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.04749696, 0.00949048, 37.85494264, 0.05735663, 3.78549426, 0.29787801, -31.04749696, -0.00949048, -37.85494264, -0.05735663, -3.78549426, -0.29787801, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 31.00698013, 0.00945409, 37.80554213, 0.05799774, 3.78055421, 0.29898156, -45.98525728, -0.00994269, -56.06794259, -0.06312325, -5.60679426, -0.30410707, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 29438467.63170244, 0.07, 0.00071458, 0.00023333, 12266028.17987602, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32553537399, 1002992, 0.32553537399, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 31.43722727, 0.00970724, 38.4550599, 0.07361092, 3.84550599, 0.38226555, -46.61530221, -0.01021981, -57.02138498, -0.0802276, -5.7021385, -0.38888223, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 31.43722727, 0.00970724, 38.4550599, 0.07314643, 3.84550599, 0.3765059, -46.61530221, -0.01021981, -57.02138498, -0.07971875, -5.7021385, -0.38307821, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 28227209.95376022, 0.07, 0.00071458, 0.00023333, 11761337.48073342, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25989496686, 1102992, 0.25989496686, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 30.91584313, 0.00987236, 37.74745945, 0.05802243, 3.77474595, 0.29674305, -45.81245957, -0.01037748, -55.93584988, -0.06312688, -5.59358499, -0.30184749, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 30.96164002, 0.00990095, 37.80337629, 0.05757533, 3.78033763, 0.29818124, -30.96164002, -0.00990095, -37.80337629, -0.05757533, -3.78033763, -0.29818124, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 28929594.91652549, 0.07, 0.00071458, 0.00023333, 12053997.88188562, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.3277540529, 1202992, 0.3277540529, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 35.62144269, 0.00806917, 43.28555999, 0.09522029, 4.328556, 0.40196025, -144.45502096, -0.0103457, -175.53518338, -0.13160483, -17.55351834, -0.43834479, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 35.62144269, 0.00806917, 43.28555999, 0.09477921, 4.328556, 0.40151917, -144.45502096, -0.0103457, -175.53518338, -0.13099112, -17.55351834, -0.43773108, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 30581760.24569568, 0.08, 0.00106667, 0.00026667, 12742400.1023732, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32600903959, 1012992, 0.32600903959, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 36.17203332, 0.008234, 44.14559914, 0.11888543, 4.41455991, 0.50322173, -146.60072756, -0.01062723, -178.91659267, -0.16458388, -17.89165927, -0.54892018, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 36.17203332, 0.008234, 44.14559914, 0.11902626, 4.41455991, 0.50336256, -146.60072756, -0.01062723, -178.91659267, -0.16477983, -17.89165927, -0.54911613, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 29091960.49746678, 0.08, 0.00106667, 0.00026667, 12121650.20727783, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.26018879734, 1112992, 0.26018879734, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 36.5873162, 0.00803717, 44.73334503, 0.09684597, 4.4733345, 0.40206055, -148.2312757, -0.01043709, -181.23441372, -0.13400265, -18.12344137, -0.43921723, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 36.5873162, 0.00803717, 44.73334503, 0.09774873, 4.4733345, 0.40296331, -148.2312757, -0.01043709, -181.23441372, -0.13525872, -18.12344137, -0.44047331, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 28413529.62949894, 0.08, 0.00106667, 0.00026667, 11838970.67895789, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32763834397, 1212992, 0.32763834397, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 30.38899961, 0.00956671, 37.0019668, 0.05755029, 3.70019668, 0.29949333, -30.38899961, -0.00956671, -37.0019668, -0.05755029, -3.70019668, -0.29949333, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 30.3455689, 0.00953839, 36.9490851, 0.05805116, 3.69490851, 0.29869109, -44.98122063, -0.01001953, -54.76960918, -0.06316627, -5.47696092, -0.30380619, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 29909486.13904582, 0.07, 0.00071458, 0.00023333, 12462285.89126909, 0.00060032)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.32460302191, 1022992, 0.32460302191, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 31.5970633, 0.00976905, 38.51314426, 0.06967207, 3.85131443, 0.37061927, -46.85183305, -0.01026957, -57.1069339, -0.07589455, -5.71069339, -0.37684175, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 31.5970633, 0.00976905, 38.51314426, 0.06984189, 3.85131443, 0.37281679, -46.85183305, -0.01026957, -57.1069339, -0.07608059, -5.71069339, -0.37905549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 29547222.83195559, 0.07, 0.00071458, 0.00023333, 12311342.84664816, 0.00060032)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.26074960127, 1122992, 0.26074960127, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 30.72310489, 0.00951415, 37.47853572, 0.05828723, 3.74785357, 0.29905216, -45.55490903, -0.01000438, -55.57157363, -0.06343629, -5.55715736, -0.30420122, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 30.76619295, 0.00954782, 37.53109803, 0.05753976, 3.7531098, 0.29665389, -30.76619295, -0.00954782, -37.53109803, -0.05753976, -3.7531098, -0.29665389, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 29256252.10283967, 0.07, 0.00071458, 0.00023333, 12190105.04284986, 0.00060032)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.32525316441, 1222992, 0.32525316441, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 30.94654544, 0.00933254, 37.94425625, 0.09428903, 3.79442562, 0.40174998, -79.45093449, -0.01094605, -97.41657994, -0.11688107, -9.74165799, -0.42434201, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 30.94654544, 0.00933254, 37.94425625, 0.09461909, 3.79442562, 0.40492107, -79.45093449, -0.01094605, -97.41657994, -0.11729263, -9.74165799, -0.42759461, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 27266686.78400155, 0.07, 0.00071458, 0.00023333, 11361119.49333398, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.25714313329, 6200992, 0.25714313329, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 38.65413072, 0.01256776, 47.06505457, 0.12808019, 4.70650546, 0.50913691, -104.50452346, -0.0160597, -127.2441265, -0.16276629, -12.72441265, -0.54382301, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 38.65413072, 0.01256776, 47.06505457, 0.12864744, 4.70650546, 0.50970416, -104.50452346, -0.0160597, -127.2441265, -0.16348672, -12.72441265, -0.54454345, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 29914010.4518607, 0.06, 0.00045, 0.0002, 12464171.02160862, 0.00046953)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.26242812257000003, 6201992, 0.26242812257000003, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 62.40635653, 0.00834093, 76.27198734, 0.08183149, 7.62719873, 0.32777844, -145.85247749, -0.00982941, -178.25841684, -0.09966544, -17.82584168, -0.34561239, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 92.44524086, 0.00862422, 112.98500076, 0.0864076, 11.29850008, 0.33238212, -215.0327025, -0.01057203, -262.809311, -0.10565566, -26.2809311, -0.35163019, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28558663.04821951, 0.1, 0.00133333, 0.00052083, 11899442.93675813, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36709028866, 2001992, 0.36709028866, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 123.21674374, 0.00687698, 150.61077491, 0.07161153, 15.06107749, 0.29039839, -188.49299835, -0.00746241, -230.39950323, -0.07903482, -23.03995032, -0.29782168, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 123.07011204, 0.00679824, 150.43154347, 0.07394124, 15.04315435, 0.29499054, -278.14053472, -0.0080329, -339.97783255, -0.08935915, -33.99778325, -0.31040845, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28514683.5555286, 0.125, 0.00260417, 0.00065104, 11881118.14813692, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.41060321487, 2101992, 0.41060321487, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 124.69805626, 0.00674821, 152.0379089, 0.07223582, 15.20379089, 0.29671592, -190.71244229, -0.00731699, -232.5258452, -0.079722, -23.25258452, -0.3042021, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 124.63278106, 0.0066678, 151.95832222, 0.07445517, 15.19583222, 0.3001753, -281.48145732, -0.00786663, -343.19582396, -0.08997337, -34.3195824, -0.31569351, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29441566.92662327, 0.125, 0.00260417, 0.00065104, 12267319.55275969, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.41020487316, 2201992, 0.41020487316, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 63.04548958, 0.00831602, 76.85150586, 0.08177404, 7.68515059, 0.3318587, -147.37873711, -0.00977652, -179.65246924, -0.09957278, -17.96524692, -0.34965744, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 93.43338113, 0.00859472, 113.89388971, 0.08659957, 11.38938897, 0.33866957, -217.34124419, -0.01050396, -264.93571565, -0.10585833, -26.49357156, -0.35792834, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 29517956.5320708, 0.1, 0.00133333, 0.00052083, 12299148.5550295, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36788805268, 2301992, 0.36788805268, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 90.86265968, 0.00904701, 110.75915458, 0.08630981, 11.07591546, 0.33545513, -211.75241154, -0.01101153, -258.1205323, -0.10545881, -25.81205323, -0.35460412, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 61.57442848, 0.00873272, 75.05758324, 0.08129268, 7.50575832, 0.3268729, -143.86670978, -0.01023072, -175.36967556, -0.09892917, -17.53696756, -0.3445094, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 29521342.67394607, 0.1, 0.00133333, 0.00052083, 12300559.44747753, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.36936583315000004, 2011992, 0.36936583315000004, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 127.69342972, 0.00670599, 155.83617381, 0.07338386, 15.58361738, 0.29438297, -288.08734331, -0.00792747, -351.57979076, -0.08869034, -35.15797908, -0.30968945, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 127.68558974, 0.00679229, 155.82660594, 0.07175272, 15.58266059, 0.29597176, -195.1870016, -0.00737151, -238.20485966, -0.07919366, -23.82048597, -0.3034127, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29104353.20519364, 0.125, 0.00260417, 0.00065104, 12126813.83549735, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41337064279999997, 2111992, 0.41337064279999997, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 128.39692256, 0.00677252, 156.64780629, 0.07278152, 15.66478063, 0.29249811, -289.75694824, -0.00800158, -353.51151253, -0.0879543, -35.35115125, -0.30767088, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 128.40804588, 0.00685826, 156.66137705, 0.07091297, 15.66613771, 0.29174724, -196.31725987, -0.00744117, -239.51250141, -0.07826192, -23.95125014, -0.29909619, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 29212931.72206334, 0.125, 0.00260417, 0.00065104, 12172054.88419306, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.41502642305000004, 2211992, 0.41502642305000004, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 93.53219557, 0.00859885, 114.24084095, 0.08562692, 11.42408409, 0.33058403, -217.46700851, -0.01053861, -265.61563941, -0.10469895, -26.56156394, -0.34965606, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 63.09775857, 0.00831998, 77.06801875, 0.08089264, 7.70680187, 0.32419456, -147.45473142, -0.00980335, -180.10218211, -0.09851732, -18.01021821, -0.34181924, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28798224.42092803, 0.1, 0.00133333, 0.00052083, 11999260.17538668, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36791588531999997, 2311992, 0.36791588531999997, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 36.92293244, 0.00810484, 44.76057483, 0.09391238, 4.47605748, 0.39797533, -149.83748717, -0.01038204, -181.64353735, -0.12977175, -18.16435373, -0.4338347, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 54.85606055, 0.0083935, 66.50037364, 0.09522144, 6.65003736, 0.39928439, -149.93633812, -0.01031267, -181.76337141, -0.12058853, -18.17633714, -0.42465147, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 31331260.00520274, 0.08, 0.00106667, 0.00026667, 13054691.66883448, 0.00073242)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32887927143, 2002992, 0.32887927143, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 73.48903249, 0.00725365, 89.59419503, 0.07698006, 8.9594195, 0.31853611, -172.15328486, -0.00844652, -209.88077345, -0.0936812, -20.98807734, -0.33523725, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 73.38074482, 0.00717928, 89.46217605, 0.07980998, 8.94621761, 0.32427058, -253.68617956, -0.00912737, -309.28164758, -0.10639309, -30.92816476, -0.35085369, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 29469998.63537496, 0.1125, 0.00189844, 0.00058594, 12279166.0980729, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36998599564, 2102992, 0.36998599564, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 70.83029601, 0.00749188, 86.04160372, 0.07569275, 8.60416037, 0.31733918, -166.06730367, -0.00866734, -201.73143326, -0.09203717, -20.17314333, -0.33368361, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 70.64044708, 0.00744079, 85.81098338, 0.07805692, 8.58109834, 0.31914896, -244.67551482, -0.00935851, -297.22131448, -0.10392636, -29.72213145, -0.3450184, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 30687507.6287619, 0.1125, 0.00189844, 0.00058594, 12786461.51198413, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.36925073185, 2202992, 0.36925073185, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.6854096, 0.00815392, 43.54736463, 0.09964408, 4.35473646, 0.40576667, -144.61807413, -0.01051885, -176.4792972, -0.13781515, -17.64792972, -0.44393775, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 52.94025602, 0.00845069, 64.6036758, 0.10063922, 6.46036758, 0.40676182, -144.66356982, -0.01044582, -176.53481617, -0.12752987, -17.65348162, -0.43365247, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29128261.37175499, 0.08, 0.00106667, 0.00026667, 12136775.57156458, 0.00073242)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32666650736999997, 2302992, 0.32666650736999997, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 52.04361654, 0.00842695, 63.63093791, 0.10137209, 6.36309379, 0.40880113, -142.18996567, -0.01043847, -173.84804282, -0.12848348, -17.38480428, -0.43591252, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 35.1000686, 0.00812886, 42.91497083, 0.10013028, 4.29149708, 0.40755932, -142.16166418, -0.01051245, -173.8134401, -0.13852012, -17.38134401, -0.44594916, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 28413498.22961838, 0.08, 0.00106667, 0.00026667, 11838957.59567432, 0.00073242)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32527831529, 2012992, 0.32527831529, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 71.0917137, 0.00720914, 86.7884689, 0.08137409, 8.67884689, 0.32592082, -246.00865898, -0.00916286, -300.32634941, -0.10848321, -30.03263494, -0.35302994, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 71.24511601, 0.007276, 86.9757418, 0.07950203, 8.69757418, 0.32949075, -166.97446938, -0.00847177, -203.84173891, -0.09676202, -20.38417389, -0.34675074, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 28983565.27853007, 0.1125, 0.00189844, 0.00058594, 12076485.53272086, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.36739434538, 2112992, 0.36739434538, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 72.89332135, 0.00724082, 88.84845686, 0.08158047, 8.88484569, 0.32990595, -252.17382542, -0.00919257, -307.37048104, -0.10874687, -30.7370481, -0.35707235, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 73.02531373, 0.00731139, 89.00934017, 0.07870377, 8.90093402, 0.32428562, -171.13238803, -0.00850656, -208.59042107, -0.09577774, -20.85904211, -0.34135959, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29547308.72017888, 0.1125, 0.00189844, 0.00058594, 12311378.63340786, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.37006422368, 2212992, 0.37006422368, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 53.03639522, 0.00832329, 64.73030472, 0.09914808, 6.47303047, 0.40598429, -144.87469375, -0.01030012, -176.81788203, -0.12565217, -17.6817882, -0.43248838, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 35.71984666, 0.00802945, 43.59565822, 0.09869255, 4.35956582, 0.40552876, -144.79170429, -0.01037431, -176.71659435, -0.13651988, -17.67165943, -0.44335609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 29075864.18543861, 0.08, 0.00106667, 0.00026667, 12114943.41059942, 0.00073242)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32590678199, 2312992, 0.32590678199, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
