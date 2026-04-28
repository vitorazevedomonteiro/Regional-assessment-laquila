import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 30.37874568, 0.00938818, 37.09782968, 0.05850549, 3.70978297, 0.26007994, -52.72381154, -0.01020761, -64.38511323, -0.06611343, -6.43851132, -0.26768788, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 30.31365606, 0.00933674, 37.01834372, 0.06028741, 3.70183437, 0.26822387, -77.84853995, -0.01088104, -95.06685714, -0.07441309, -9.50668571, -0.28234955, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 28868172.88343057, 0.07, 0.00071458, 0.00023333, 12028405.36809607, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32385413939, 1001992, 0.32385413939, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 29.79962607, 0.0093316, 36.22022427, 0.07579389, 3.62202243, 0.34329438, -76.49815312, -0.01081189, -92.98037014, -0.09368588, -9.29803701, -0.36118636, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 29.79962607, 0.0093316, 36.22022427, 0.07895214, 3.62202243, 0.37759419, -76.49815312, -0.01081189, -92.98037014, -0.09762401, -9.29803701, -0.39626605, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 30500222.45357825, 0.07, 0.00071458, 0.00023333, 12708426.02232427, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.25470570522, 1101992, 0.25470570522, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 31.69191829, 0.00920746, 38.68300648, 0.07049542, 3.86830065, 0.30273286, -81.38590386, -0.01075797, -99.33925165, -0.08717992, -9.93392516, -0.31941736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.73666875, 0.00927533, 38.73762868, 0.06783361, 3.87376287, 0.28825483, -55.09390728, -0.01009751, -67.24736423, -0.07674913, -6.72473642, -0.29717035, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29043845.45331434, 0.07, 0.00071458, 0.00023333, 12101602.27221431, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.3261154141, 1201992, 0.3261154141, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 35.3576991, 0.00860482, 43.04526836, 0.08284889, 4.30452684, 0.34454713, -141.9522551, -0.01067749, -172.81590913, -0.11397819, -17.28159091, -0.37567642, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 51.98903334, 0.00887778, 63.29263353, 0.07972441, 6.32926335, 0.30880844, -141.80747849, -0.0106363, -172.63965478, -0.10061508, -17.26396548, -0.32969911, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 29962091.16047658, 0.1, 0.00133333, 0.00052083, 12484204.65019858, 0.00127345)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.3282823443, 1011992, 0.3282823443, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 52.27686976, 0.00822252, 64.04082201, 0.1154222, 6.4040822, 0.46981849, -143.13434817, -0.00998077, -175.34411217, -0.14612975, -17.53441122, -0.50052605, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 52.27686976, 0.00822252, 64.04082201, 0.1071054, 6.4040822, 0.39971885, -143.13434817, -0.00998077, -175.34411217, -0.13556701, -17.53441122, -0.42818046, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 27638238.63243352, 0.1, 0.00133333, 0.00052083, 11515932.76351397, 0.00127345)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.25657566199000004, 1111992, 0.25657566199000004, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 49.11825761, 0.0086058, 59.94086942, 0.07705796, 5.99408694, 0.3139724, -133.66779507, -0.01032402, -163.11987112, -0.09726171, -16.31198711, -0.33417615, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 33.48691125, 0.0083396, 40.86534565, 0.07678475, 4.08653457, 0.31890852, -133.82432476, -0.01036288, -163.31089022, -0.10559515, -16.33108902, -0.34771893, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 29120814.15665651, 0.1, 0.00133333, 0.00052083, 12133672.56527355, 0.00127345)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.32237175279, 1211992, 0.32237175279, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 30.99086539, 0.00955467, 37.39691433, 0.06774231, 3.73969143, 0.30841175, -53.79243971, -0.01033018, -64.91174847, -0.07655995, -6.49117485, -0.31722939, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 30.92909325, 0.00951712, 37.32237341, 0.06873398, 3.73223734, 0.30599487, -79.45217425, -0.01097243, -95.8755464, -0.08481187, -9.58755464, -0.32207276, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 32673391.2385864, 0.07, 0.00071458, 0.00023333, 13613913.01607767, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32650298235, 1021992, 0.32650298235, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 30.47651818, 0.00991785, 37.10719286, 0.08810684, 3.71071929, 0.38781774, -78.06944826, -0.01148481, -95.05475842, -0.10898121, -9.50547584, -0.40869211, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 30.47651818, 0.00991785, 37.10719286, 0.08270284, 3.71071929, 0.33558691, -78.06944826, -0.01148481, -95.05475842, -0.10224278, -9.50547584, -0.35512685, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29921798.93408024, 0.07, 0.00071458, 0.00023333, 12467416.22253343, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.25947799228999996, 1121992, 0.25947799228999996, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 29.74084692, 0.00970251, 36.28112313, 0.05924127, 3.62811231, 0.25992275, -76.18601144, -0.01125661, -92.93999156, -0.0730281, -9.29399916, -0.27370958, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 29.80211014, 0.0097344, 36.35585867, 0.05896501, 3.63558587, 0.26805656, -51.63484892, -0.0105602, -62.98981049, -0.06659498, -6.29898105, -0.27568652, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 29248062.97016115, 0.07, 0.00071458, 0.00023333, 12186692.90423381, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32450917793, 1221992, 0.32450917793, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 31.36975011, 0.00943393, 38.31435127, 0.04997477, 3.83143513, 0.26655183, -31.36975011, -0.00943393, -38.31435127, -0.04997477, -3.83143513, -0.26655183, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 31.33458209, 0.00939204, 38.27139778, 0.0522159, 3.82713978, 0.29122094, -46.47500808, -0.00988794, -56.76359481, -0.05680235, -5.67635948, -0.2958074, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 28806684.93223737, 0.07, 0.00071458, 0.00023333, 12002785.38843224, 0.00060032)
    ops.section('Aggregator', 1002991, 1002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1002992, 1002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.32579826755, 1002992, 0.32579826755, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 31.49642166, 0.00940368, 38.21352607, 0.05262524, 3.82135261, 0.30667995, -46.72338695, -0.00987745, -56.6878798, -0.05722756, -5.66878798, -0.31128227, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 31.49642166, 0.00940368, 38.21352607, 0.05275846, 3.82135261, 0.30867451, -46.72338695, -0.00987745, -56.6878798, -0.0573735, -5.66878798, -0.31328956, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 31077169.63266048, 0.07, 0.00071458, 0.00023333, 12948820.6802752, 0.00060032)
    ops.section('Aggregator', 1102991, 1102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1102992, 1102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.25844388486000003, 1102992, 0.25844388486000003, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 32.36021296, 0.00984914, 38.98667487, 0.04491174, 3.89866749, 0.25461602, -47.99340526, -0.01032139, -57.82110549, -0.04873318, -5.78211055, -0.25843746, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 32.4017079, 0.00987695, 39.03666682, 0.04397684, 3.90366668, 0.24654488, -32.4017079, -0.00987695, -39.03666682, -0.04397684, -3.90366668, -0.24654488, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 33112910.60357147, 0.07, 0.00071458, 0.00023333, 13797046.08482145, 0.00060032)
    ops.section('Aggregator', 1202991, 1202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1202992, 1202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.33123653379, 1202992, 0.33123653379, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 37.08307477, 0.00799908, 44.87023439, 0.08581448, 4.48702344, 0.39026432, -150.51239449, -0.01023499, -182.11883622, -0.1185047, -18.21188362, -0.42295454, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 37.08307477, 0.00799908, 44.87023439, 0.08694975, 4.48702344, 0.39139958, -150.51239449, -0.01023499, -182.11883622, -0.12008427, -18.21188362, -0.42453411, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 31896123.52672926, 0.08, 0.00106667, 0.00026667, 13290051.46947052, 0.00073242)
    ops.section('Aggregator', 1012991, 1012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1012992, 1012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.32846133682, 1012992, 0.32846133682, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 37.00046804, 0.00834332, 45.34686598, 0.12461789, 4.5346866, 0.50550765, -149.86041533, -0.01086694, -183.66524885, -0.17264746, -18.36652488, -0.55353722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 37.00046804, 0.00834332, 45.34686598, 0.11705712, 4.5346866, 0.4815258, -149.86041533, -0.01086694, -183.66524885, -0.16212765, -18.36652488, -0.52659633, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 27454444.5895331, 0.08, 0.00106667, 0.00026667, 11439351.91230546, 0.00073242)
    ops.section('Aggregator', 1112991, 1112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1112992, 1112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.26254315780000004, 1112992, 0.26254315780000004, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 36.85851757, 0.00772171, 44.97609409, 0.08420574, 4.49760941, 0.37591149, -149.15883357, -0.01002571, -182.0089948, -0.11644301, -18.20089948, -0.40814875, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 36.85851757, 0.00772171, 44.97609409, 0.08344057, 4.49760941, 0.36827122, -149.15883357, -0.01002571, -182.0089948, -0.11537837, -18.20089948, -0.40020902, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 29151109.69092696, 0.08, 0.00106667, 0.00026667, 12146295.7045529, 0.00073242)
    ops.section('Aggregator', 1212991, 1212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1212992, 1212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.32584955853, 1212992, 0.32584955853, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 31.07523239, 0.00963354, 37.56474521, 0.05215772, 3.75647452, 0.2839943, -31.07523239, -0.00963354, -37.56474521, -0.05215772, -3.75647452, -0.2839943, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 31.03392176, 0.00960785, 37.51480759, 0.05128338, 3.75148076, 0.26545893, -46.01135776, -0.01007339, -55.62001627, -0.05572979, -5.56200163, -0.26990533, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 32175391.68621564, 0.07, 0.00071458, 0.00023333, 13406413.20258985, 0.00060032)
    ops.section('Aggregator', 1022991, 1022990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1022992, 1022991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.32675171246, 1022992, 0.32675171246, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 31.14514926, 0.0095785, 37.74025275, 0.06358494, 3.77402527, 0.3522917, -46.18423985, -0.01005088, -55.96392782, -0.06921605, -5.59639278, -0.35792281, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 31.14514926, 0.0095785, 37.74025275, 0.06289056, 3.77402527, 0.34286962, -46.18423985, -0.01005088, -55.96392782, -0.06845534, -5.59639278, -0.3484344, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 31461326.38735761, 0.07, 0.00071458, 0.00023333, 13108885.99473234, 0.00060032)
    ops.section('Aggregator', 1122991, 1122990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1122992, 1122991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.25877145947, 1122992, 0.25877145947, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 32.77444331, 0.00946287, 39.64185579, 0.04307649, 3.96418558, 0.24506047, -48.62872403, -0.00993761, -58.81817265, -0.04676201, -5.88181727, -0.248746, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 32.80224027, 0.00950363, 39.6754772, 0.04346551, 3.96754772, 0.25705526, -32.80224027, -0.00950363, -39.6754772, -0.04346551, -3.96754772, -0.25705526, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 32006721.27257799, 0.07, 0.00071458, 0.00023333, 13336133.86357416, 0.00060032)
    ops.section('Aggregator', 1222991, 1222990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1222992, 1222991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.32961936304, 1222992, 0.32961936304, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6200, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6200990, 34.51275797, 0.00978583, 41.72321101, 0.08235058, 4.1723211, 0.37885111, -88.70687255, -0.01134578, -107.23963481, -0.10182914, -10.72396348, -0.39832966, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6200991, 34.51275797, 0.00978583, 41.72321101, 0.08087405, 4.1723211, 0.3632627, -88.70687255, -0.01134578, -107.23963481, -0.099988, -10.72396348, -0.38237665, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6200990, 32154140.04840074, 0.07, 0.00071458, 0.00023333, 13397558.35350031, 0.00060032)
    ops.section('Aggregator', 6200991, 6200990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6200992, 6200991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6200, 6200991, 0.26804396502, 6200992, 0.26804396502, 6200990)
    # Create element
    ops.element('forceBeamColumn', 6200, 1101, 1201, 6200, 6200)

    # Create geometric transformation
    ops.geomTransf('Linear', 6201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6201990, 37.31142606, 0.01175185, 45.16660036, 0.10979834, 4.51666004, 0.48054569, -100.97314693, -0.01492712, -122.23102295, -0.13945108, -12.22310229, -0.51019843, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6201991, 37.31142606, 0.01175185, 45.16660036, 0.10960654, 4.51666004, 0.47863582, -100.97314693, -0.01492712, -122.23102295, -0.13920749, -12.22310229, -0.50823677, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6201990, 31764802.01449565, 0.06, 0.00045, 0.0002, 13235334.17270652, 0.00046953)
    ops.section('Aggregator', 6201991, 6201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 6201992, 6201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6201, 6201991, 0.25628933475000004, 6201992, 0.25628933475000004, 6201990)
    # Create element
    ops.element('forceBeamColumn', 6201, 1102, 1202, 6201, 6201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 62.48213049, 0.0083791, 75.16303127, 0.06439013, 7.51630313, 0.27708426, -146.22844521, -0.00973475, -175.90586483, -0.07820352, -17.59058648, -0.29089765, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 92.4131877, 0.00866325, 111.16866955, 0.07082541, 11.11686696, 0.30887251, -215.50813982, -0.01043303, -259.24604244, -0.08642104, -25.92460424, -0.32446815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 33514580.83301317, 0.1, 0.00133333, 0.00052083, 13964408.68042216, 0.00127345)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.36802015973, 2001992, 0.36802015973, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 123.54027064, 0.00670349, 149.63714571, 0.06904887, 14.96371457, 0.2919442, -189.06420509, -0.00724506, -229.00247715, -0.07617593, -22.90024772, -0.29907126, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 123.41969515, 0.00663265, 149.49109963, 0.07112214, 14.94910996, 0.29487574, -279.11016109, -0.00777168, -338.0699073, -0.08588391, -33.80699073, -0.3096375, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 31589068.50592288, 0.125, 0.00260417, 0.00065104, 13162111.87746787, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.40897513587, 2101992, 0.40897513587, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 116.53005373, 0.00634007, 141.97912935, 0.06276091, 14.19791294, 0.25775397, -178.25141485, -0.00687099, -217.1798594, -0.06925152, -21.71798594, -0.26424458, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 116.44591211, 0.00626664, 141.87661199, 0.06701286, 14.1876612, 0.2822666, -263.09175146, -0.00738533, -320.54853332, -0.08096355, -32.05485333, -0.29621729, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 29688686.90756895, 0.125, 0.00260417, 0.00065104, 12370286.21148706, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.39699714269999997, 2201992, 0.39699714269999997, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 64.87248778, 0.00809839, 79.28306365, 0.06716532, 7.92830636, 0.27149394, -151.32828931, -0.00957251, -184.9438923, -0.08177686, -18.49438923, -0.28610548, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 96.43790725, 0.00835597, 117.86032878, 0.07081679, 11.78603288, 0.2747314, -223.48981994, -0.01027944, -273.13516447, -0.08663255, -27.31351645, -0.29054715, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 28572998.91075121, 0.1, 0.00133333, 0.00052083, 11905416.212813, 0.00127345)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.36817811388000005, 2301992, 0.36817811388000005, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 95.75173529, 0.00908216, 114.23588606, 0.06061698, 11.42358861, 0.26075728, -223.46305014, -0.01086512, -266.60090762, -0.0738621, -26.66009076, -0.2740024, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 64.81111283, 0.00878218, 77.32240964, 0.05804765, 7.73224096, 0.26381509, -151.67575786, -0.01014883, -180.95561966, -0.07037172, -18.09556197, -0.27613917, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 35536371.86279219, 0.1, 0.00133333, 0.00052083, 14806821.60949675, 0.00127345)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.37522433713, 2011992, 0.37522433713, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 129.1236293, 0.00663632, 157.55459047, 0.06721611, 15.75545905, 0.2701994, -290.99114825, -0.00785139, -355.06275219, -0.08122802, -35.50627522, -0.28421132, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 129.03307305, 0.00672604, 157.44409518, 0.06722052, 15.74440952, 0.28558049, -197.14750336, -0.00730214, -240.5562353, -0.07418659, -24.05562353, -0.29254657, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29166588.32111454, 0.125, 0.00260417, 0.00065104, 12152745.13379772, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.41349602352, 2111992, 0.41349602352, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 126.39649877, 0.00727229, 152.33857312, 0.05527909, 15.23385731, 0.23552146, -286.27100573, -0.00845842, -345.02630186, -0.06660616, -34.50263019, -0.24684853, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 126.69670732, 0.00732801, 152.70039756, 0.05546914, 15.27003976, 0.25130842, -193.99228957, -0.00789337, -233.8079684, -0.06111961, -23.38079684, -0.25695889, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 33006993.94720515, 0.125, 0.00260417, 0.00065104, 13752914.14466881, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.42108445777, 2211992, 0.42108445777, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 90.57536774, 0.00883554, 110.76873598, 0.07565275, 11.0768736, 0.29023306, -210.93124654, -0.01081665, -257.95741314, -0.09249508, -25.79574131, -0.30707538, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 61.28519395, 0.00853381, 74.94845052, 0.07077255, 7.49484505, 0.27821606, -143.22440433, -0.01004482, -175.15563694, -0.08612644, -17.51556369, -0.29356996, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 28318890.5949828, 0.1, 0.00133333, 0.00052083, 11799537.7479095, 0.00127345)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.36712841524, 2311992, 0.36712841524, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 35.94660543, 0.00775128, 43.55502701, 0.0796366, 4.3555027, 0.36681012, -145.86479327, -0.00993569, -176.73838558, -0.10995448, -17.67383856, -0.39712801, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 53.44302435, 0.00802816, 64.75471999, 0.08236048, 6.475472, 0.38483543, -145.99847627, -0.00986787, -176.90036378, -0.10427364, -17.69003638, -0.4067486, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 31485073.4808508, 0.08, 0.00106667, 0.00026667, 13118780.61702117, 0.00073242)
    ops.section('Aggregator', 2002991, 2002990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2002992, 2002991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.32448961517999997, 2002992, 0.32448961517999997, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 71.41687221, 0.00724637, 86.72088926, 0.07637908, 8.67208893, 0.32105085, -167.4789602, -0.00839647, -203.36825055, -0.09290539, -20.33682505, -0.33757716, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 71.26193202, 0.0071852, 86.53274673, 0.07562242, 8.65327467, 0.29506352, -246.81968402, -0.00906137, -299.71100419, -0.10071125, -29.97110042, -0.32015234, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 30810375.9646239, 0.1125, 0.00189844, 0.00058594, 12837656.65192663, 0.00152995)
    ops.section('Aggregator', 2102991, 2102990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2102992, 2102991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.36749181197, 2102992, 0.36749181197, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 73.40897122, 0.00731764, 89.73158905, 0.07903204, 8.97315891, 0.32319757, -171.92631429, -0.00854167, -210.15444195, -0.09620649, -21.01544419, -0.34037202, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 73.29229489, 0.00724135, 89.58896953, 0.08137404, 8.95889695, 0.32403566, -253.30831946, -0.00924193, -309.63188349, -0.10851908, -30.96318835, -0.35118071, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 28505966.21590883, 0.1125, 0.00189844, 0.00058594, 11877485.92329535, 0.00152995)
    ops.section('Aggregator', 2202991, 2202990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2202992, 2202991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.37047497969, 2202992, 0.37047497969, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 35.34846207, 0.00769776, 43.03347472, 0.08826088, 4.30334747, 0.39568792, -143.33120487, -0.00992751, -174.49245091, -0.12202032, -17.44924509, -0.42944736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 52.54704773, 0.00797816, 63.97115795, 0.08962018, 6.39711579, 0.39829943, -143.46837928, -0.00985604, -174.65944803, -0.11354551, -17.4659448, -0.42222476, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 29966426.97168817, 0.08, 0.00106667, 0.00026667, 12486011.23820341, 0.00073242)
    ops.section('Aggregator', 2302991, 2302990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2302992, 2302991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.32290047086, 2302992, 0.32290047086, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 54.00292723, 0.00858387, 65.91550378, 0.08996971, 6.59155038, 0.39396408, -147.5515134, -0.01061646, -180.10009529, -0.11398057, -18.01000953, -0.41797494, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 36.39291815, 0.00828171, 44.42087971, 0.08635162, 4.44208797, 0.37113789, -147.49440124, -0.01069151, -180.03038468, -0.11931535, -18.00303847, -0.40410162, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 29045041.05018583, 0.08, 0.00106667, 0.00026667, 12102100.43757743, 0.00073242)
    ops.section('Aggregator', 2012991, 2012990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2012992, 2012991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.32895346714, 2012992, 0.32895346714, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 71.46442838, 0.00772056, 87.08361553, 0.06776288, 8.70836155, 0.27516393, -247.32708207, -0.00973661, -301.3826181, -0.09014419, -30.13826181, -0.29754524, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 71.66853159, 0.00776992, 87.33232732, 0.06658858, 8.73323273, 0.28159348, -167.91862301, -0.00900447, -204.61873325, -0.08090533, -20.46187332, -0.29591023, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 29640581.32479591, 0.1125, 0.00189844, 0.00058594, 12350242.21866496, 0.00152995)
    ops.section('Aggregator', 2112991, 2112990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2112992, 2112991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.37302542248, 2112992, 0.37302542248, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.15, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 74.10214559, 0.00735761, 90.33977347, 0.07447718, 9.03397735, 0.30146461, -256.33938476, -0.00934413, -312.50973595, -0.09922944, -31.25097359, -0.32621687, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 74.23518391, 0.00742973, 90.5019638, 0.07113711, 9.05019638, 0.28946091, -173.96077811, -0.00864612, -212.07992241, -0.08652304, -21.20799224, -0.30484684, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 29477432.28261197, 0.1125, 0.00189844, 0.00058594, 12282263.45108832, 0.00152995)
    ops.section('Aggregator', 2212991, 2212990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2212992, 2212991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.37284279345, 2212992, 0.37284279345, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 50.75070149, 0.00855762, 62.01443559, 0.09736689, 6.20144356, 0.40564534, -138.64202985, -0.01056589, -169.41257908, -0.12335813, -16.94125791, -0.43163658, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 34.31983046, 0.00825909, 41.93685708, 0.09668993, 4.19368571, 0.40496839, -138.6949034, -0.0106347, -169.47718752, -0.13367438, -16.94771875, -0.44195284, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 28633373.34161352, 0.08, 0.00106667, 0.00026667, 11930572.2256723, 0.00073242)
    ops.section('Aggregator', 2312991, 2312990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2312992, 2312991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.32438206017, 2312992, 0.32438206017, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)
