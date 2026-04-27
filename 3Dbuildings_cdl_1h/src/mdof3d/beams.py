import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 241.65811399, 0.00884228, 291.69940021, 0.06632434, 29.16994002, 0.25465038, -241.65811399, -0.00884228, -291.69940021, -0.06632434, -29.16994002, -0.25465038, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 358.08593716, 0.00918321, 432.23648223, 0.06694735, 43.22364822, 0.23745959, -472.21142979, -0.00977473, -569.99447926, -0.07140151, -56.99944793, -0.24191375, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 32588555.21165578, 0.15, 0.003125, 0.001125, 13578564.67152324, 0.00281737)
    ops.section('Aggregator', 1001991, 1001990, 'Mz')
    ops.section('Aggregator', 1001992, 1001991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.53099402625, 1001992, 0.53099402625, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 354.89758053, 0.00893371, 428.3549168, 0.12853844, 42.83549168, 0.34732471, -467.83791227, -0.00951225, -564.6718405, -0.13711487, -56.46718405, -0.35590113, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 354.89758053, 0.00893371, 428.3549168, 0.12864765, 42.83549168, 0.34743391, -467.83791227, -0.00951225, -564.6718405, -0.13723138, -56.46718405, -0.35601764, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 32610079.2017898, 0.15, 0.003125, 0.001125, 13587533.00074575, 0.00281737)
    ops.section('Aggregator', 1101991, 1101990, 'Mz')
    ops.section('Aggregator', 1101992, 1101991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.45706709104, 1101992, 0.45706709104, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 361.77268318, 0.00918246, 436.97296494, 0.07317096, 43.69729649, 0.26091869, -476.95866155, -0.00977797, -576.102205, -0.07804533, -57.6102205, -0.26579307, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 361.77268318, 0.00918246, 436.97296494, 0.0730592, 43.69729649, 0.26080694, -476.95866155, -0.00977797, -576.102205, -0.0779261, -57.6102205, -0.26567384, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 32403966.15878443, 0.15, 0.003125, 0.001125, 13501652.56616018, 0.00281737)
    ops.section('Aggregator', 1201991, 1201990, 'Mz')
    ops.section('Aggregator', 1201992, 1201991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.53262958581, 1201992, 0.53262958581, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1301, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1301990, 359.67486122, 0.0089587, 433.95438133, 0.12633413, 43.39543813, 0.34383451, -474.04095425, -0.00953954, -571.93919066, -0.13476379, -57.19391907, -0.35226417, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1301991, 359.67486122, 0.0089587, 433.95438133, 0.12660262, 43.39543813, 0.344103, -474.04095425, -0.00953954, -571.93919066, -0.13505024, -57.19391907, -0.35255062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1301990, 32716912.14164275, 0.15, 0.003125, 0.001125, 13632046.72568448, 0.00281737)
    ops.section('Aggregator', 1301991, 1301990, 'Mz')
    ops.section('Aggregator', 1301992, 1301991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1301, 1301991, 0.45976931176, 1301992, 0.45976931176, 1301990)
    # Create element
    ops.element('forceBeamColumn', 1301, 301, 401, 1301, 1301)

    # Create geometric transformation
    ops.geomTransf('Linear', 1401, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1401990, 361.57788984, 0.00911062, 434.52955369, 0.07131126, 43.45295537, 0.2593395, -476.7768684, -0.00968753, -572.97098538, -0.07604749, -57.29709854, -0.26407572, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1401991, 361.57788984, 0.00911062, 434.52955369, 0.07052514, 43.45295537, 0.25855337, -476.7768684, -0.00968753, -572.97098538, -0.0752088, -57.29709854, -0.26323703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1401990, 33772347.9267251, 0.15, 0.003125, 0.001125, 14071811.63613546, 0.00281737)
    ops.section('Aggregator', 1401991, 1401990, 'Mz')
    ops.section('Aggregator', 1401992, 1401991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1401, 1401991, 0.53183502816, 1401992, 0.53183502816, 1401990)
    # Create element
    ops.element('forceBeamColumn', 1401, 401, 501, 1401, 1401)

    # Create geometric transformation
    ops.geomTransf('Linear', 1501, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1501990, 360.15064887, 0.00904319, 432.87858029, 0.12271728, 43.28785803, 0.33919349, -474.85849368, -0.00961686, -570.75024362, -0.13089226, -57.07502436, -0.34736848, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1501991, 360.15064887, 0.00904319, 432.87858029, 0.12356855, 43.28785803, 0.34004476, -474.85849368, -0.00961686, -570.75024362, -0.13180046, -57.07502436, -0.34827667, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1501990, 33734099.42460507, 0.15, 0.003125, 0.001125, 14055874.76025211, 0.00281737)
    ops.section('Aggregator', 1501991, 1501990, 'Mz')
    ops.section('Aggregator', 1501992, 1501991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1501, 1501991, 0.46194452247, 1501992, 0.46194452247, 1501990)
    # Create element
    ops.element('forceBeamColumn', 1501, 501, 601, 1501, 1501)

    # Create geometric transformation
    ops.geomTransf('Linear', 1601, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1601990, 356.33365101, 0.00908403, 429.40210734, 0.06210768, 42.94021073, 0.2361933, -469.89445319, -0.00966506, -566.24926626, -0.06623436, -56.62492663, -0.24031999, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1601991, 240.43477832, 0.00874837, 289.73744186, 0.061686, 28.97374419, 0.25086234, -240.43477832, -0.00874837, -289.73744186, -0.061686, -28.97374419, -0.25086234, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1601990, 33049143.96269375, 0.15, 0.003125, 0.001125, 13770476.6511224, 0.00281737)
    ops.section('Aggregator', 1601991, 1601990, 'Mz')
    ops.section('Aggregator', 1601992, 1601991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1601, 1601991, 0.52860731299, 1601992, 0.52860731299, 1601990)
    # Create element
    ops.element('forceBeamColumn', 1601, 601, 701, 1601, 1601)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 321.5386697, 0.00616936, 384.36974089, 0.05135591, 38.43697409, 0.22114397, -476.0334712, -0.00655686, -569.05398704, -0.05605966, -56.9053987, -0.22584772, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 476.86671535, 0.00649359, 570.05005335, 0.05654972, 57.00500534, 0.24716506, -476.86671535, -0.00649359, -570.05005335, -0.05654972, -57.00500534, -0.24716506, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 35076767.34264888, 0.195, 0.00686563, 0.0014625, 14615319.7261037, 0.00415543)
    ops.section('Aggregator', 1011991, 1011990, 'Mz')
    ops.section('Aggregator', 1011992, 1011991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.5246167541, 1011992, 0.5246167541, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 481.7222856, 0.00651198, 579.80440828, 0.09068478, 57.98044083, 0.30901402, -481.7222856, -0.00651198, -579.80440828, -0.09068478, -57.98044083, -0.30901402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 481.7222856, 0.00651198, 579.80440828, 0.09013175, 57.98044083, 0.30846099, -481.7222856, -0.00651198, -579.80440828, -0.09013175, -57.98044083, -0.30846099, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 33371261.86012014, 0.195, 0.00686563, 0.0014625, 13904692.44171673, 0.00415543)
    ops.section('Aggregator', 1111991, 1111990, 'Mz')
    ops.section('Aggregator', 1111992, 1111991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.45802386777, 1111992, 0.45802386777, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 482.77338781, 0.00657865, 578.11848651, 0.07737326, 57.81184865, 0.266558, -482.77338781, -0.00657865, -578.11848651, -0.07737326, -57.81184865, -0.266558, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 638.98160588, 0.0068055, 765.1769717, 0.07958551, 76.51769717, 0.26877025, -638.98160588, -0.0068055, -765.1769717, -0.07958551, -76.51769717, -0.26877025, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 34659977.69653094, 0.195, 0.00686563, 0.0014625, 14441657.37355456, 0.00415543)
    ops.section('Aggregator', 1211991, 1211990, 'Mz')
    ops.section('Aggregator', 1211992, 1211991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.52858386391, 1211992, 0.52858386391, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1311, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1311990, 648.11088347, 0.00683442, 779.64694523, 0.12035083, 77.96469452, 0.33630098, -648.11088347, -0.00683442, -779.64694523, -0.12035083, -77.96469452, -0.33630098, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1311991, 806.09135623, 0.0070287, 969.6900322, 0.12380475, 96.96900322, 0.3397549, -806.09135623, -0.0070287, -969.6900322, -0.12380475, -96.96900322, -0.3397549, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1311990, 33514454.05250778, 0.195, 0.00686563, 0.0014625, 13964355.85521157, 0.00415543)
    ops.section('Aggregator', 1311991, 1311990, 'Mz')
    ops.section('Aggregator', 1311992, 1311991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1311, 1311991, 0.4630698214, 1311992, 0.4630698214, 1311990)
    # Create element
    ops.element('forceBeamColumn', 1311, 311, 411, 1311, 1311)

    # Create geometric transformation
    ops.geomTransf('Linear', 1411, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1411990, 783.29682481, 0.00697254, 947.0527275, 0.08839227, 94.70527275, 0.27911296, -783.29682481, -0.00697254, -947.0527275, -0.08839227, -94.70527275, -0.27911296, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1411991, 475.8484099, 0.00654644, 575.32919858, 0.08123672, 57.53291986, 0.27195741, -475.8484099, -0.00654644, -575.32919858, -0.08123672, -57.53291986, -0.27195741, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1411990, 32121041.14043293, 0.195, 0.00686563, 0.0014625, 13383767.14184706, 0.00415543)
    ops.section('Aggregator', 1411991, 1411990, 'Mz')
    ops.section('Aggregator', 1411992, 1411991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1411, 1411991, 0.5243269631099999, 1411992, 0.5243269631099999, 1411990)
    # Create element
    ops.element('forceBeamColumn', 1411, 411, 511, 1411, 1411)

    # Create geometric transformation
    ops.geomTransf('Linear', 1511, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1511990, 493.29351879, 0.00670544, 592.06211516, 0.08753918, 59.20621152, 0.30162833, -493.29351879, -0.00670544, -592.06211516, -0.08753918, -59.20621152, -0.30162833, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1511991, 493.29351879, 0.00670544, 592.06211516, 0.08727696, 59.20621152, 0.30136611, -493.29351879, -0.00670544, -592.06211516, -0.08727696, -59.20621152, -0.30136611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1511990, 34097998.08481565, 0.195, 0.00686563, 0.0014625, 14207499.20200652, 0.00415543)
    ops.section('Aggregator', 1511991, 1511990, 'Mz')
    ops.section('Aggregator', 1511992, 1511991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1511, 1511991, 0.46709513736, 1511992, 0.46709513736, 1511990)
    # Create element
    ops.element('forceBeamColumn', 1511, 511, 611, 1511, 1511)

    # Create geometric transformation
    ops.geomTransf('Linear', 1611, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1611990, 484.95503929, 0.00654443, 586.57393568, 0.06673019, 58.65739357, 0.2563698, -484.95503929, -0.00654443, -586.57393568, -0.06673019, -58.65739357, -0.2563698, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1611991, 327.04031389, 0.00620375, 395.56929717, 0.06042885, 39.55692972, 0.23014859, -483.6246085, -0.00661824, -584.96472254, -0.06602296, -58.49647225, -0.2357427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1611990, 32004953.36192733, 0.195, 0.00686563, 0.0014625, 13335397.23413639, 0.00415543)
    ops.section('Aggregator', 1611991, 1611990, 'Mz')
    ops.section('Aggregator', 1611992, 1611991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1611, 1611991, 0.52731599823, 1611992, 0.52731599823, 1611990)
    # Create element
    ops.element('forceBeamColumn', 1611, 611, 711, 1611, 1611)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 244.09968884, 0.00915967, 294.34298608, 0.06003749, 29.43429861, 0.24657591, -244.09968884, -0.00915967, -294.34298608, -0.06003749, -29.43429861, -0.24657591, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 244.09968884, 0.00915967, 294.34298608, 0.06018704, 29.43429861, 0.24672546, -244.09968884, -0.00915967, -294.34298608, -0.06018704, -29.43429861, -0.24672546, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 32874035.50955444, 0.125, 0.00260417, 0.00065104, 13697514.79564768, 0.00178813)
    ops.section('Aggregator', 1021991, 1021990, 'Mz')
    ops.section('Aggregator', 1021992, 1021991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.53608260038, 1021992, 0.53608260038, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 239.39761587, 0.00901204, 287.26069415, 0.0687044, 28.72606941, 0.28485322, -239.39761587, -0.00901204, -287.26069415, -0.0687044, -28.72606941, -0.28485322, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 239.39761587, 0.00901204, 287.26069415, 0.06803557, 28.72606941, 0.28418439, -239.39761587, -0.00901204, -287.26069415, -0.06803557, -28.72606941, -0.28418439, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 34159009.0406578, 0.125, 0.00260417, 0.00065104, 14232920.43360742, 0.00178813)
    ops.section('Aggregator', 1121991, 1121990, 'Mz')
    ops.section('Aggregator', 1121992, 1121991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.46264421397, 1121992, 0.46264421397, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 239.95320848, 0.00892091, 289.00697039, 0.07211399, 28.90069704, 0.26114286, -239.95320848, -0.00892091, -289.00697039, -0.07211399, -28.90069704, -0.26114286, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 355.51522844, 0.00938925, 428.19339549, 0.07734942, 42.81933955, 0.26637829, -355.51522844, -0.00938925, -428.19339549, -0.07734942, -42.81933955, -0.26637829, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 33189090.8521926, 0.125, 0.00260417, 0.00065104, 13828787.85508025, 0.00178813)
    ops.section('Aggregator', 1221991, 1221990, 'Mz')
    ops.section('Aggregator', 1221992, 1221991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.5290197224900001, 1221992, 0.5290197224900001, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 1321, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1321990, 363.44883887, 0.00934646, 435.9186434, 0.10262957, 43.59186434, 0.31791459, -363.44883887, -0.00934646, -435.9186434, -0.10262957, -43.59186434, -0.31791459, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1321991, 363.44883887, 0.00934646, 435.9186434, 0.10195423, 43.59186434, 0.31723925, -363.44883887, -0.00934646, -435.9186434, -0.10195423, -43.59186434, -0.31723925, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1321990, 34270693.56995139, 0.125, 0.00260417, 0.00065104, 14279455.65414641, 0.00178813)
    ops.section('Aggregator', 1321991, 1321990, 'Mz')
    ops.section('Aggregator', 1321992, 1321991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1321, 1321991, 0.46450048772999997, 1321992, 0.46450048772999997, 1321990)
    # Create element
    ops.element('forceBeamColumn', 1321, 321, 421, 1321, 1321)

    # Create geometric transformation
    ops.geomTransf('Linear', 1421, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1421990, 360.92667897, 0.00933199, 432.24736984, 0.07450976, 43.22473698, 0.26274255, -360.92667897, -0.00933199, -432.24736984, -0.07450976, -43.22473698, -0.26274255, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1421991, 243.49939946, 0.00887458, 291.61594614, 0.06941672, 29.16159461, 0.25764951, -243.49939946, -0.00887458, -291.61594614, -0.06941672, -29.16159461, -0.25764951, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1421990, 34637733.31045482, 0.125, 0.00260417, 0.00065104, 14432388.87935618, 0.00178813)
    ops.section('Aggregator', 1421991, 1421990, 'Mz')
    ops.section('Aggregator', 1421992, 1421991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1421, 1421991, 0.53125706754, 1421992, 0.53125706754, 1421990)
    # Create element
    ops.element('forceBeamColumn', 1421, 421, 521, 1421, 1421)

    # Create geometric transformation
    ops.geomTransf('Linear', 1521, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1521990, 248.04049154, 0.00903373, 299.37955731, 0.06880058, 29.93795573, 0.28227017, -248.04049154, -0.00903373, -299.37955731, -0.06880058, -29.93795573, -0.28227017, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1521991, 248.04049154, 0.00903373, 299.37955731, 0.06870729, 29.93795573, 0.28217688, -248.04049154, -0.00903373, -299.37955731, -0.06870729, -29.93795573, -0.28217688, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1521990, 32610824.7339427, 0.125, 0.00260417, 0.00065104, 13587843.63914279, 0.00178813)
    ops.section('Aggregator', 1521991, 1521990, 'Mz')
    ops.section('Aggregator', 1521992, 1521991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1521, 1521991, 0.46845080199, 1521992, 0.46845080199, 1521990)
    # Create element
    ops.element('forceBeamColumn', 1521, 521, 621, 1521, 1521)

    # Create geometric transformation
    ops.geomTransf('Linear', 1621, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1621990, 239.1648933, 0.00888673, 288.84511072, 0.06238084, 28.88451107, 0.2519427, -239.1648933, -0.00888673, -288.84511072, -0.06238084, -28.88451107, -0.2519427, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1621991, 239.1648933, 0.00888673, 288.84511072, 0.06253058, 28.88451107, 0.25209244, -239.1648933, -0.00888673, -288.84511072, -0.06253058, -28.88451107, -0.25209244, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1621990, 32437354.85746141, 0.125, 0.00260417, 0.00065104, 13515564.52394225, 0.00178813)
    ops.section('Aggregator', 1621991, 1621990, 'Mz')
    ops.section('Aggregator', 1621992, 1621991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1621, 1621991, 0.52753226447, 1621992, 0.52753226447, 1621990)
    # Create element
    ops.element('forceBeamColumn', 1621, 621, 721, 1621, 1621)

    # Create geometric transformation
    ops.geomTransf('Linear', 1031, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1031990, 246.7407964, 0.00907706, 298.16144467, 0.0615036, 29.81614447, 0.24800468, -246.7407964, -0.00907706, -298.16144467, -0.0615036, -29.81614447, -0.24800468, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1031991, 246.7407964, 0.00907706, 298.16144467, 0.06205206, 29.81614447, 0.24855315, -246.7407964, -0.00907706, -298.16144467, -0.06205206, -29.81614447, -0.24855315, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1031990, 32278237.70860775, 0.125, 0.00260417, 0.00065104, 13449265.7119199, 0.00178813)
    ops.section('Aggregator', 1031991, 1031990, 'Mz')
    ops.section('Aggregator', 1031992, 1031991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1031, 1031991, 0.53618990735, 1031992, 0.53618990735, 1031990)
    # Create element
    ops.element('forceBeamColumn', 1031, 31, 131, 1031, 1031)

    # Create geometric transformation
    ops.geomTransf('Linear', 1131, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1131990, 241.50639753, 0.00875568, 292.52810729, 0.08435291, 29.25281073, 0.30250689, -241.50639753, -0.00875568, -292.52810729, -0.08435291, -29.25281073, -0.30250689, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1131991, 241.50639753, 0.00875568, 292.52810729, 0.0847552, 29.25281073, 0.30290918, -241.50639753, -0.00875568, -292.52810729, -0.0847552, -29.25281073, -0.30290918, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1131990, 31583459.69641002, 0.125, 0.00260417, 0.00065104, 13159774.87350417, 0.00178813)
    ops.section('Aggregator', 1131991, 1131990, 'Mz')
    ops.section('Aggregator', 1131992, 1131991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1131, 1131991, 0.45839181987, 1131992, 0.45839181987, 1131990)
    # Create element
    ops.element('forceBeamColumn', 1131, 131, 231, 1131, 1131)

    # Create geometric transformation
    ops.geomTransf('Linear', 1231, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1231990, 242.4732677, 0.0090364, 292.72421948, 0.0718858, 29.27242195, 0.25964686, -242.4732677, -0.0090364, -292.72421948, -0.0718858, -29.27242195, -0.25964686, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1231991, 359.26988801, 0.00951302, 433.72615277, 0.07647411, 43.37261528, 0.26423517, -359.26988801, -0.00951302, -433.72615277, -0.07647411, -43.37261528, -0.26423517, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1231990, 32549437.00412921, 0.125, 0.00260417, 0.00065104, 13562265.41838717, 0.00178813)
    ops.section('Aggregator', 1231991, 1231990, 'Mz')
    ops.section('Aggregator', 1231992, 1231991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1231, 1231991, 0.53259177633, 1231992, 0.53259177633, 1231990)
    # Create element
    ops.element('forceBeamColumn', 1231, 231, 331, 1231, 1231)

    # Create geometric transformation
    ops.geomTransf('Linear', 1331, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1331990, 358.69784602, 0.00963145, 433.83389011, 0.10724144, 43.38338901, 0.32179835, -358.69784602, -0.00963145, -433.83389011, -0.10724144, -43.38338901, -0.32179835, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1331991, 358.69784602, 0.00963145, 433.83389011, 0.10793434, 43.38338901, 0.32249125, -358.69784602, -0.00963145, -433.83389011, -0.10793434, -43.38338901, -0.32249125, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1331990, 32022801.40491959, 0.125, 0.00260417, 0.00065104, 13342833.9187165, 0.00178813)
    ops.section('Aggregator', 1331991, 1331990, 'Mz')
    ops.section('Aggregator', 1331992, 1331991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1331, 1331991, 0.46607679750000003, 1331992, 0.46607679750000003, 1331990)
    # Create element
    ops.element('forceBeamColumn', 1331, 331, 431, 1331, 1331)

    # Create geometric transformation
    ops.geomTransf('Linear', 1431, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1431990, 357.66100394, 0.00928001, 431.35284301, 0.07754306, 43.1352843, 0.26696032, -357.66100394, -0.00928001, -431.35284301, -0.07754306, -43.1352843, -0.26696032, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1431991, 241.22738982, 0.00882021, 290.92945349, 0.07316613, 29.09294535, 0.26258339, -241.22738982, -0.00882021, -290.92945349, -0.07316613, -29.09294535, -0.26258339, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1431990, 32826861.0886979, 0.125, 0.00260417, 0.00065104, 13677858.78695746, 0.00178813)
    ops.section('Aggregator', 1431991, 1431990, 'Mz')
    ops.section('Aggregator', 1431992, 1431991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1431, 1431991, 0.52793499386, 1431992, 0.52793499386, 1431990)
    # Create element
    ops.element('forceBeamColumn', 1431, 431, 531, 1431, 1431)

    # Create geometric transformation
    ops.geomTransf('Linear', 1531, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1531990, 240.28646216, 0.00876903, 288.77264877, 0.08186964, 28.87726488, 0.2998555, -240.28646216, -0.00876903, -288.77264877, -0.08186964, -28.87726488, -0.2998555, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1531991, 240.28646216, 0.00876903, 288.77264877, 0.08119114, 28.87726488, 0.29917701, -240.28646216, -0.00876903, -288.77264877, -0.08119114, -28.87726488, -0.29917701, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1531990, 33766834.43394572, 0.125, 0.00260417, 0.00065104, 14069514.34747738, 0.00178813)
    ops.section('Aggregator', 1531991, 1531990, 'Mz')
    ops.section('Aggregator', 1531992, 1531991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1531, 1531991, 0.45874533599, 1531992, 0.45874533599, 1531990)
    # Create element
    ops.element('forceBeamColumn', 1531, 531, 631, 1531, 1531)

    # Create geometric transformation
    ops.geomTransf('Linear', 1631, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1631990, 240.55153228, 0.00901558, 289.49732471, 0.06099182, 28.94973247, 0.24923683, -240.55153228, -0.00901558, -289.49732471, -0.06099182, -28.94973247, -0.24923683, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1631991, 240.55153228, 0.00901558, 289.49732471, 0.06121879, 28.94973247, 0.24946379, -240.55153228, -0.00901558, -289.49732471, -0.06121879, -28.94973247, -0.24946379, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1631990, 33400700.03229083, 0.125, 0.00260417, 0.00065104, 13916958.34678785, 0.00178813)
    ops.section('Aggregator', 1631991, 1631990, 'Mz')
    ops.section('Aggregator', 1631992, 1631991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1631, 1631991, 0.53122260147, 1631992, 0.53122260147, 1631990)
    # Create element
    ops.element('forceBeamColumn', 1631, 631, 731, 1631, 1631)

    # Create geometric transformation
    ops.geomTransf('Linear', 1041, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1041990, 330.34945513, 0.00625131, 397.3710161, 0.05443779, 39.73710161, 0.22892526, -488.71034658, -0.00665727, -587.86029154, -0.05944654, -58.78602915, -0.23393402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1041991, 489.91608994, 0.00658714, 589.31065707, 0.05925719, 58.93106571, 0.24767084, -489.91608994, -0.00658714, -589.31065707, -0.05925719, -58.93106571, -0.24767084, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1041990, 33530180.54318935, 0.195, 0.00686563, 0.0014625, 13970908.55966223, 0.00415543)
    ops.section('Aggregator', 1041991, 1041990, 'Mz')
    ops.section('Aggregator', 1041992, 1041991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1041, 1041991, 0.53074710356, 1041992, 0.53074710356, 1041990)
    # Create element
    ops.element('forceBeamColumn', 1041, 41, 141, 1041, 1041)

    # Create geometric transformation
    ops.geomTransf('Linear', 1141, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1141990, 486.12523414, 0.00676228, 588.15918284, 0.09247352, 58.81591828, 0.30749655, -486.12523414, -0.00676228, -588.15918284, -0.09247352, -58.81591828, -0.30749655, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1141991, 486.12523414, 0.00676228, 588.15918284, 0.09168932, 58.81591828, 0.30671235, -486.12523414, -0.00676228, -588.15918284, -0.09168932, -58.81591828, -0.30671235, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1141990, 31920407.5823507, 0.195, 0.00686563, 0.0014625, 13300169.82597946, 0.00415543)
    ops.section('Aggregator', 1141991, 1141990, 'Mz')
    ops.section('Aggregator', 1141992, 1141991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1141, 1141991, 0.46506646121, 1141992, 0.46506646121, 1141990)
    # Create element
    ops.element('forceBeamColumn', 1141, 141, 241, 1141, 1141)

    # Create geometric transformation
    ops.geomTransf('Linear', 1241, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1241990, 488.5548321, 0.00664089, 582.59529088, 0.07441967, 58.25952909, 0.2622111, -488.5548321, -0.00664089, -582.59529088, -0.07441967, -58.25952909, -0.2622111, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1241991, 647.7071245, 0.00680603, 772.38233215, 0.0785823, 77.23823321, 0.26637373, -802.01338805, -0.00713251, -956.39054697, -0.08260448, -95.6390547, -0.27039591, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1241990, 35642454.87236623, 0.195, 0.00686563, 0.0014625, 14851022.86348593, 0.00415543)
    ops.section('Aggregator', 1241991, 1241990, 'Mz')
    ops.section('Aggregator', 1241992, 1241991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1241, 1241991, 0.5325056704600001, 1241992, 0.5325056704600001, 1241990)
    # Create element
    ops.element('forceBeamColumn', 1241, 241, 341, 1241, 1241)

    # Create geometric transformation
    ops.geomTransf('Linear', 1341, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1341990, 649.52993487, 0.00686314, 776.49089378, 0.11488018, 77.64908938, 0.32941501, -804.2671982, -0.00719517, -961.47401689, -0.12077391, -96.14740169, -0.33530874, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1341991, 806.10256169, 0.00712354, 963.66813136, 0.13710537, 96.36681314, 0.35164021, -806.10256169, -0.00712354, -963.66813136, -0.13710537, -96.36681314, -0.35164021, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1341990, 35065251.63227832, 0.195, 0.00686563, 0.0014625, 14610521.5134493, 0.00415543)
    ops.section('Aggregator', 1341991, 1341990, 'Mz')
    ops.section('Aggregator', 1341992, 1341991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1341, 1341991, 0.46612477182, 1341992, 0.46612477182, 1341990)
    # Create element
    ops.element('forceBeamColumn', 1341, 341, 441, 1341, 1341)

    # Create geometric transformation
    ops.geomTransf('Linear', 1441, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1441990, 800.64872985, 0.00696443, 957.89421369, 0.08207997, 95.78942137, 0.27106478, -800.64872985, -0.00696443, -957.89421369, -0.08207997, -95.78942137, -0.27106478, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1441991, 486.30633091, 0.00654912, 581.81572404, 0.07598717, 58.1815724, 0.26497198, -486.30633091, -0.00654912, -581.81572404, -0.07598717, -58.1815724, -0.26497198, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1441990, 34880399.08766434, 0.195, 0.00686563, 0.0014625, 14533499.61986014, 0.00415543)
    ops.section('Aggregator', 1441991, 1441990, 'Mz')
    ops.section('Aggregator', 1441992, 1441991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1441, 1441991, 0.52914304828, 1441992, 0.52914304828, 1441990)
    # Create element
    ops.element('forceBeamColumn', 1441, 441, 541, 1441, 1441)

    # Create geometric transformation
    ops.geomTransf('Linear', 1541, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1541990, 488.04166943, 0.00658844, 580.18919059, 0.08182146, 58.01891906, 0.29766811, -488.04166943, -0.00658844, -580.18919059, -0.08182146, -58.01891906, -0.29766811, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1541991, 488.04166943, 0.00658844, 580.18919059, 0.08195389, 58.01891906, 0.29780054, -488.04166943, -0.00658844, -580.18919059, -0.08195389, -58.01891906, -0.29780054, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1541990, 36327861.96961934, 0.195, 0.00686563, 0.0014625, 15136609.15400806, 0.00415543)
    ops.section('Aggregator', 1541991, 1541990, 'Mz')
    ops.section('Aggregator', 1541992, 1541991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1541, 1541991, 0.4632918769, 1541992, 0.4632918769, 1541990)
    # Create element
    ops.element('forceBeamColumn', 1541, 541, 641, 1541, 1541)

    # Create geometric transformation
    ops.geomTransf('Linear', 1641, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1641990, 495.45488256, 0.00671118, 594.96778337, 0.06267607, 59.49677834, 0.24927195, -495.45488256, -0.00671118, -594.96778337, -0.06267607, -59.49677834, -0.24927195, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1641991, 334.08292426, 0.00637111, 401.18401071, 0.05686289, 40.11840107, 0.22368134, -494.39326741, -0.00678038, -593.69294113, -0.06209517, -59.36929411, -0.22891362, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1641990, 33965547.83729073, 0.195, 0.00686563, 0.0014625, 14152311.59887114, 0.00415543)
    ops.section('Aggregator', 1641991, 1641990, 'Mz')
    ops.section('Aggregator', 1641992, 1641991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1641, 1641991, 0.53591752706, 1641992, 0.53591752706, 1641990)
    # Create element
    ops.element('forceBeamColumn', 1641, 641, 741, 1641, 1641)

    # Create geometric transformation
    ops.geomTransf('Linear', 1051, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1051990, 238.42133668, 0.00862667, 285.62600839, 0.06555326, 28.56260084, 0.25583762, -238.42133668, -0.00862667, -285.62600839, -0.06555326, -28.56260084, -0.25583762, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1051991, 353.27462486, 0.00895758, 423.21892146, 0.06512573, 42.32189215, 0.23492299, -465.95842099, -0.00951546, -558.21280811, -0.06943953, -55.82128081, -0.23923679, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1051990, 34559714.57382972, 0.15, 0.003125, 0.001125, 14399881.07242905, 0.00281737)
    ops.section('Aggregator', 1051991, 1051990, 'Mz')
    ops.section('Aggregator', 1051992, 1051991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1051, 1051991, 0.52552926899, 1051992, 0.52552926899, 1051990)
    # Create element
    ops.element('forceBeamColumn', 1051, 51, 151, 1051, 1051)

    # Create geometric transformation
    ops.geomTransf('Linear', 1151, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1151990, 356.75278901, 0.00898738, 430.15604077, 0.12532826, 43.01560408, 0.34318772, -470.32139093, -0.00956611, -567.0918172, -0.13368663, -56.70918172, -0.35154609, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1151991, 356.75278901, 0.00898738, 430.15604077, 0.12636738, 43.01560408, 0.34422684, -470.32139093, -0.00956611, -567.0918172, -0.13479523, -56.70918172, -0.35265469, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1151990, 32891583.45851314, 0.15, 0.003125, 0.001125, 13704826.44104714, 0.00281737)
    ops.section('Aggregator', 1151991, 1151990, 'Mz')
    ops.section('Aggregator', 1151992, 1151991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1151, 1151991, 0.45901150748999997, 1151992, 0.45901150748999997, 1151990)
    # Create element
    ops.element('forceBeamColumn', 1151, 151, 251, 1151, 1151)

    # Create geometric transformation
    ops.geomTransf('Linear', 1251, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1251990, 355.87324755, 0.00906069, 427.39992108, 0.07127756, 42.73999211, 0.26055002, -469.36247993, -0.0096308, -563.69926163, -0.07600806, -56.36992616, -0.26528052, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1251991, 355.87324755, 0.00906069, 427.39992108, 0.0713517, 42.73999211, 0.26062416, -469.36247993, -0.0096308, -563.69926163, -0.07608716, -56.36992616, -0.26535962, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1251990, 33936413.91653182, 0.15, 0.003125, 0.001125, 14140172.46522159, 0.00281737)
    ops.section('Aggregator', 1251991, 1251990, 'Mz')
    ops.section('Aggregator', 1251992, 1251991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1251, 1251991, 0.5283388825800001, 1251992, 0.5283388825800001, 1251990)
    # Create element
    ops.element('forceBeamColumn', 1251, 251, 351, 1251, 1251)

    # Create geometric transformation
    ops.geomTransf('Linear', 1351, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1351990, 356.28969586, 0.00911737, 429.15182586, 0.12634854, 42.91518259, 0.34316064, -469.88173888, -0.00969846, -565.97372452, -0.13476879, -56.59737245, -0.35158089, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1351991, 356.28969586, 0.00911737, 429.15182586, 0.12655192, 42.91518259, 0.34336402, -469.88173888, -0.00969846, -565.97372452, -0.13498577, -56.59737245, -0.35179787, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1351990, 33173064.04527586, 0.15, 0.003125, 0.001125, 13822110.01886494, 0.00281737)
    ops.section('Aggregator', 1351991, 1351990, 'Mz')
    ops.section('Aggregator', 1351992, 1351991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1351, 1351991, 0.46122886965, 1351992, 0.46122886965, 1351990)
    # Create element
    ops.element('forceBeamColumn', 1351, 351, 451, 1351, 1351)

    # Create geometric transformation
    ops.geomTransf('Linear', 1451, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1451990, 361.90382541, 0.00885403, 434.88267828, 0.07041137, 43.48826783, 0.26004405, -476.91224541, -0.00941958, -573.08284695, -0.07509322, -57.30828469, -0.2647259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1451991, 361.90382541, 0.00885403, 434.88267828, 0.07012703, 43.48826783, 0.2597597, -476.91224541, -0.00941958, -573.08284695, -0.07478987, -57.30828469, -0.26442254, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1451990, 33795161.45658783, 0.15, 0.003125, 0.001125, 14081317.27357826, 0.00281737)
    ops.section('Aggregator', 1451991, 1451990, 'Mz')
    ops.section('Aggregator', 1451992, 1451991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1451, 1451991, 0.52733528362, 1451992, 0.52733528362, 1451990)
    # Create element
    ops.element('forceBeamColumn', 1451, 451, 551, 1451, 1451)

    # Create geometric transformation
    ops.geomTransf('Linear', 1551, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1551990, 358.84277533, 0.00924579, 433.82231609, 0.12719678, 43.38223161, 0.34259099, -473.20583324, -0.00984562, -572.08132552, -0.1356839, -57.20813255, -0.35107811, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1551991, 358.84277533, 0.00924579, 433.82231609, 0.12715865, 43.38223161, 0.34255286, -473.20583324, -0.00984562, -572.08132552, -0.13564323, -57.20813255, -0.35103744, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1551990, 32147741.81246772, 0.15, 0.003125, 0.001125, 13394892.42186155, 0.00281737)
    ops.section('Aggregator', 1551991, 1551990, 'Mz')
    ops.section('Aggregator', 1551992, 1551991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1551, 1551991, 0.46426503129, 1551992, 0.46426503129, 1551990)
    # Create element
    ops.element('forceBeamColumn', 1551, 551, 651, 1551, 1551)

    # Create geometric transformation
    ops.geomTransf('Linear', 1651, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1651990, 349.84071754, 0.00915078, 421.11092369, 0.06054292, 42.11109237, 0.23039654, -461.56267745, -0.00972798, -555.5930905, -0.06455668, -55.55930905, -0.2344103, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1651991, 236.41710999, 0.00880233, 284.58044639, 0.06033122, 28.45804464, 0.25015195, -236.41710999, -0.00880233, -284.58044639, -0.06033122, -28.45804464, -0.25015195, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1651990, 33346019.56533594, 0.15, 0.003125, 0.001125, 13894174.81888998, 0.00281737)
    ops.section('Aggregator', 1651991, 1651990, 'Mz')
    ops.section('Aggregator', 1651992, 1651991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1651, 1651991, 0.52681285441, 1651992, 0.52681285441, 1651990)
    # Create element
    ops.element('forceBeamColumn', 1651, 651, 751, 1651, 1651)

    # Create geometric transformation
    ops.geomTransf('Linear', 1002, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1002990, 240.45355434, 0.0087147, 290.3369013, 0.06696448, 29.03369013, 0.25643176, -240.45355434, -0.0087147, -290.3369013, -0.06696448, -29.03369013, -0.25643176, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1002991, 356.52669358, 0.0090464, 430.49002012, 0.06749191, 43.04900201, 0.23900023, -470.0496026, -0.00963205, -567.56385013, -0.07198577, -56.75638501, -0.24349409, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1002990, 32500093.58236302, 0.15, 0.003125, 0.001125, 13541705.65931792, 0.00281737)
    ops.section('Aggregator', 1002991, 1002990, 'Mz')
    ops.section('Aggregator', 1002992, 1002991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1002, 1002991, 0.52779561861, 1002992, 0.52779561861, 1002990)
    # Create element
    ops.element('forceBeamColumn', 1002, 2, 102, 1002, 1002)

    # Create geometric transformation
    ops.geomTransf('Linear', 1102, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1102990, 366.31549699, 0.00927131, 439.45333902, 0.11852006, 43.9453339, 0.33169197, -483.10961349, -0.00985274, -579.56634242, -0.12640688, -57.95663424, -0.33957879, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1102991, 366.31549699, 0.00927131, 439.45333902, 0.11962594, 43.9453339, 0.33279786, -483.10961349, -0.00985274, -579.56634242, -0.12758671, -57.95663424, -0.34075863, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1102990, 34215989.37746244, 0.15, 0.003125, 0.001125, 14256662.24060935, 0.00281737)
    ops.section('Aggregator', 1102991, 1102990, 'Mz')
    ops.section('Aggregator', 1102992, 1102991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1102, 1102991, 0.46910494957, 1102992, 0.46910494957, 1102990)
    # Create element
    ops.element('forceBeamColumn', 1102, 102, 202, 1102, 1102)

    # Create geometric transformation
    ops.geomTransf('Linear', 1202, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1202990, 362.57044472, 0.00883591, 434.34960947, 0.06898865, 43.43496095, 0.25851854, -477.83572295, -0.00939307, -572.43430258, -0.07356817, -57.24343026, -0.26309806, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1202991, 362.57044472, 0.00883591, 434.34960947, 0.06965064, 43.43496095, 0.25918053, -477.83572295, -0.00939307, -572.43430258, -0.07427442, -57.24343026, -0.26380432, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1202990, 34562857.69100853, 0.15, 0.003125, 0.001125, 14401190.70458689, 0.00281737)
    ops.section('Aggregator', 1202991, 1202990, 'Mz')
    ops.section('Aggregator', 1202992, 1202991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1202, 1202991, 0.5276212575, 1202992, 0.5276212575, 1202990)
    # Create element
    ops.element('forceBeamColumn', 1202, 202, 302, 1202, 1202)

    # Create geometric transformation
    ops.geomTransf('Linear', 1302, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1302990, 354.08899873, 0.00905201, 427.9717363, 0.12728319, 42.79717363, 0.3453222, -466.87473163, -0.0096399, -564.29087107, -0.13577712, -56.42908711, -0.35381613, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1302991, 354.08899873, 0.00905201, 427.9717363, 0.12851878, 42.79717363, 0.34655779, -466.87473163, -0.0096399, -564.29087107, -0.13709533, -56.42908711, -0.35513434, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1302990, 32217410.29973291, 0.15, 0.003125, 0.001125, 13423920.95822205, 0.00281737)
    ops.section('Aggregator', 1302991, 1302990, 'Mz')
    ops.section('Aggregator', 1302992, 1302991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1302, 1302991, 0.45863352019000003, 1302992, 0.45863352019000003, 1302990)
    # Create element
    ops.element('forceBeamColumn', 1302, 302, 402, 1302, 1302)

    # Create geometric transformation
    ops.geomTransf('Linear', 1402, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1402990, 350.3403118, 0.0090656, 420.27985302, 0.07129173, 42.0279853, 0.26143754, -462.21718353, -0.00963003, -554.49105745, -0.07601718, -55.44910575, -0.26616299, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1402991, 350.3403118, 0.0090656, 420.27985302, 0.07096116, 42.0279853, 0.26110697, -462.21718353, -0.00963003, -554.49105745, -0.0756645, -55.44910575, -0.26581031, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1402990, 34221173.14169205, 0.15, 0.003125, 0.001125, 14258822.14237169, 0.00281737)
    ops.section('Aggregator', 1402991, 1402990, 'Mz')
    ops.section('Aggregator', 1402992, 1402991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1402, 1402991, 0.5259121945399999, 1402992, 0.5259121945399999, 1402990)
    # Create element
    ops.element('forceBeamColumn', 1402, 402, 502, 1402, 1402)

    # Create geometric transformation
    ops.geomTransf('Linear', 1502, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1502990, 355.2303108, 0.0089252, 427.40592831, 0.12562962, 42.74059283, 0.34424387, -468.34918397, -0.00949415, -563.50826961, -0.13400252, -56.35082696, -0.35261677, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1502991, 355.2303108, 0.0089252, 427.40592831, 0.12549369, 42.74059283, 0.34410794, -468.34918397, -0.00949415, -563.50826961, -0.1338575, -56.35082696, -0.35247175, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1502990, 33464970.96724679, 0.15, 0.003125, 0.001125, 13943737.9030195, 0.00281737)
    ops.section('Aggregator', 1502991, 1502990, 'Mz')
    ops.section('Aggregator', 1502992, 1502991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1502, 1502991, 0.45742672353, 1502992, 0.45742672353, 1502990)
    # Create element
    ops.element('forceBeamColumn', 1502, 502, 602, 1502, 1502)

    # Create geometric transformation
    ops.geomTransf('Linear', 1602, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1602990, 351.06183004, 0.00909024, 421.8276271, 0.0606328, 42.18276271, 0.23286168, -463.13928006, -0.00966045, -556.4972515, -0.06464962, -55.64972515, -0.2368785, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1602991, 237.14567759, 0.00874738, 284.94866117, 0.06047234, 28.49486612, 0.25039562, -237.14567759, -0.00874738, -284.94866117, -0.06047234, -28.49486612, -0.25039562, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1602990, 33811444.25412059, 0.15, 0.003125, 0.001125, 14088101.77255025, 0.00281737)
    ops.section('Aggregator', 1602991, 1602990, 'Mz')
    ops.section('Aggregator', 1602992, 1602991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1602, 1602991, 0.52652837282, 1602992, 0.52652837282, 1602990)
    # Create element
    ops.element('forceBeamColumn', 1602, 602, 702, 1602, 1602)

    # Create geometric transformation
    ops.geomTransf('Linear', 1012, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1012990, 268.39473063, 0.00760142, 323.79095867, 0.06741652, 32.37909587, 0.25734981, -397.03534651, -0.00814507, -478.98278469, -0.07367375, -47.89827847, -0.26360704, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1012991, 397.78495158, 0.00804714, 479.88710701, 0.06968659, 47.9887107, 0.25961988, -397.78495158, -0.00804714, -479.88710701, -0.06968659, -47.9887107, -0.25961988, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1012990, 32744499.60067207, 0.165, 0.00415938, 0.0012375, 13643541.50028003, 0.00326155)
    ops.section('Aggregator', 1012991, 1012990, 'Mz')
    ops.section('Aggregator', 1012992, 1012991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1012, 1012991, 0.52650063665, 1012992, 0.52650063665, 1012990)
    # Create element
    ops.element('forceBeamColumn', 1012, 12, 112, 1012, 1012)

    # Create geometric transformation
    ops.geomTransf('Linear', 1112, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1112990, 405.57296794, 0.00807451, 486.35259643, 0.09175412, 48.63525964, 0.30774503, -405.57296794, -0.00807451, -486.35259643, -0.09175412, -48.63525964, -0.30774503, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1112991, 405.57296794, 0.00807451, 486.35259643, 0.09123324, 48.63525964, 0.30722416, -405.57296794, -0.00807451, -486.35259643, -0.09123324, -48.63525964, -0.30722416, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1112990, 34316403.46264753, 0.165, 0.00415938, 0.0012375, 14298501.44276981, 0.00326155)
    ops.section('Aggregator', 1112991, 1112990, 'Mz')
    ops.section('Aggregator', 1112992, 1112991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1112, 1112991, 0.46298244072, 1112992, 0.46298244072, 1112990)
    # Create element
    ops.element('forceBeamColumn', 1112, 112, 212, 1112, 1112)

    # Create geometric transformation
    ops.geomTransf('Linear', 1212, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1212990, 404.31417602, 0.00816258, 486.2498402, 0.08225038, 48.62498402, 0.2702517, -404.31417602, -0.00816258, -486.2498402, -0.08225038, -48.62498402, -0.2702517, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1212991, 534.88636387, 0.00846366, 643.28293287, 0.08612992, 64.32829329, 0.27413124, -534.88636387, -0.00846366, -643.28293287, -0.08612992, -64.32829329, -0.27413124, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1212990, 33579578.35840987, 0.165, 0.00415938, 0.0012375, 13991490.98267078, 0.00326155)
    ops.section('Aggregator', 1212991, 1212990, 'Mz')
    ops.section('Aggregator', 1212992, 1212991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1212, 1212991, 0.5319111506499999, 1212992, 0.5319111506499999, 1212990)
    # Create element
    ops.element('forceBeamColumn', 1212, 212, 312, 1212, 1212)

    # Create geometric transformation
    ops.geomTransf('Linear', 1312, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1312990, 525.50633018, 0.00837108, 632.98426282, 0.12725818, 63.29842628, 0.34513714, -525.50633018, -0.00837108, -632.98426282, -0.12725818, -63.29842628, -0.34513714, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1312991, 525.50633018, 0.00837108, 632.98426282, 0.12603777, 63.29842628, 0.34391672, -525.50633018, -0.00837108, -632.98426282, -0.12603777, -63.29842628, -0.34391672, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1312990, 33168577.11223091, 0.165, 0.00415938, 0.0012375, 13820240.46342955, 0.00326155)
    ops.section('Aggregator', 1312991, 1312990, 'Mz')
    ops.section('Aggregator', 1312992, 1312991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1312, 1312991, 0.45897043666000004, 1312992, 0.45897043666000004, 1312990)
    # Create element
    ops.element('forceBeamColumn', 1312, 312, 412, 1312, 1312)

    # Create geometric transformation
    ops.geomTransf('Linear', 1412, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1412990, 525.00642654, 0.00848973, 634.48411938, 0.08958435, 63.44841194, 0.27875343, -525.00642654, -0.00848973, -634.48411938, -0.08958435, -63.44841194, -0.27875343, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1412991, 396.97198374, 0.00818259, 479.75111691, 0.08537722, 47.97511169, 0.2745463, -396.97198374, -0.00818259, -479.75111691, -0.08537722, -47.97511169, -0.2745463, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1412990, 32248155.51938838, 0.165, 0.00415938, 0.0012375, 13436731.46641183, 0.00326155)
    ops.section('Aggregator', 1412991, 1412990, 'Mz')
    ops.section('Aggregator', 1412992, 1412991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1412, 1412991, 0.52862761217, 1412992, 0.52862761217, 1412990)
    # Create element
    ops.element('forceBeamColumn', 1412, 412, 512, 1412, 1412)

    # Create geometric transformation
    ops.geomTransf('Linear', 1512, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1512990, 407.15011674, 0.00794234, 490.09665067, 0.09432475, 49.00966507, 0.31149174, -407.15011674, -0.00794234, -490.09665067, -0.09432475, -49.00966507, -0.31149174, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1512991, 407.15011674, 0.00794234, 490.09665067, 0.09301082, 49.00966507, 0.31017781, -407.15011674, -0.00794234, -490.09665067, -0.09301082, -49.00966507, -0.31017781, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1512990, 33345397.50942055, 0.165, 0.00415938, 0.0012375, 13893915.62892523, 0.00326155)
    ops.section('Aggregator', 1512991, 1512990, 'Mz')
    ops.section('Aggregator', 1512992, 1512991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1512, 1512991, 0.46047514561, 1512992, 0.46047514561, 1512990)
    # Create element
    ops.element('forceBeamColumn', 1512, 512, 612, 1512, 1512)

    # Create geometric transformation
    ops.geomTransf('Linear', 1612, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1612990, 397.26607224, 0.00807509, 478.66416677, 0.06775272, 47.86641668, 0.25750571, -397.26607224, -0.00807509, -478.66416677, -0.06775272, -47.86641668, -0.25750571, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1612991, 268.05144615, 0.00762994, 322.97402443, 0.0663402, 32.29740244, 0.25609319, -396.6059902, -0.00817108, -477.86883678, -0.07248939, -47.78688368, -0.26224238, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1612990, 33085192.44209452, 0.165, 0.00415938, 0.0012375, 13785496.85087272, 0.00326155)
    ops.section('Aggregator', 1612991, 1612990, 'Mz')
    ops.section('Aggregator', 1612992, 1612991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1612, 1612991, 0.5270009217, 1612992, 0.5270009217, 1612990)
    # Create element
    ops.element('forceBeamColumn', 1612, 612, 712, 1612, 1612)

    # Create geometric transformation
    ops.geomTransf('Linear', 1022, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1022990, 153.35175736, 0.00812334, 184.44816635, 0.06172728, 18.44481664, 0.25781374, -235.01471409, -0.00869682, -282.6705988, -0.0679629, -28.26705988, -0.26404936, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1022991, 227.27964472, 0.00843678, 273.36702521, 0.0649367, 27.33670252, 0.26507385, -347.49561364, -0.00918182, -417.96018419, -0.07164977, -41.79601842, -0.27178692, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1022990, 33552470.85266952, 0.15, 0.003125, 0.001125, 13980196.1886123, 0.00281737)
    ops.section('Aggregator', 1022991, 1022990, 'Mz')
    ops.section('Aggregator', 1022992, 1022991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1022, 1022991, 0.45819687808, 1022992, 0.45819687808, 1022990)
    # Create element
    ops.element('forceBeamColumn', 1022, 22, 122, 1022, 1022)

    # Create geometric transformation
    ops.geomTransf('Linear', 1122, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1122990, 233.30611105, 0.00833062, 279.48902714, 0.08438229, 27.94890271, 0.33926191, -356.51258034, -0.00906137, -427.08420192, -0.09314632, -42.70842019, -0.34802594, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1122991, 233.30611105, 0.00833062, 279.48902714, 0.084529, 27.94890271, 0.33940862, -356.51258034, -0.00906137, -427.08420192, -0.09330853, -42.70842019, -0.34818814, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1122990, 34567568.04757115, 0.15, 0.003125, 0.001125, 14403153.35315465, 0.00281737)
    ops.section('Aggregator', 1122991, 1122990, 'Mz')
    ops.section('Aggregator', 1122992, 1122991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1122, 1122991, 0.39234208284, 1122992, 0.39234208284, 1122990)
    # Create element
    ops.element('forceBeamColumn', 1122, 122, 222, 1122, 1122)

    # Create geometric transformation
    ops.geomTransf('Linear', 1222, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1222990, 231.113296, 0.00838202, 278.71154529, 0.07772186, 27.87115453, 0.29538547, -353.10696366, -0.00913657, -425.83005477, -0.08580072, -42.58300548, -0.30346432, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1222991, 305.60751834, 0.00872241, 368.54800292, 0.07921201, 36.85480029, 0.29687561, -353.48002122, -0.00905969, -426.2799443, -0.08211021, -42.62799443, -0.29977382, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1222990, 32846510.33795715, 0.15, 0.003125, 0.001125, 13686045.97414881, 0.00281737)
    ops.section('Aggregator', 1222991, 1222990, 'Mz')
    ops.section('Aggregator', 1222992, 1222991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1222, 1222991, 0.45942453032999997, 1222992, 0.45942453032999997, 1222990)
    # Create element
    ops.element('forceBeamColumn', 1222, 222, 322, 1222, 1222)

    # Create geometric transformation
    ops.geomTransf('Linear', 1322, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1322990, 313.26925821, 0.00885597, 376.7944058, 0.1071778, 37.67944058, 0.35912056, -362.34374642, -0.00919521, -435.82028255, -0.11108913, -43.58202826, -0.36303188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1322991, 313.26925821, 0.00885597, 376.7944058, 0.10684417, 37.67944058, 0.35878693, -362.34374642, -0.00919521, -435.82028255, -0.11074337, -43.58202826, -0.36268613, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1322990, 33551819.25351423, 0.15, 0.003125, 0.001125, 13979924.68896426, 0.00281737)
    ops.section('Aggregator', 1322991, 1322990, 'Mz')
    ops.section('Aggregator', 1322992, 1322991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1322, 1322991, 0.39691555454000005, 1322992, 0.39691555454000005, 1322990)
    # Create element
    ops.element('forceBeamColumn', 1322, 322, 422, 1322, 1322)

    # Create geometric transformation
    ops.geomTransf('Linear', 1422, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1422990, 310.28506717, 0.00882179, 374.28642156, 0.07876867, 37.42864216, 0.29481239, -358.87011283, -0.00916351, -432.89292508, -0.0816516, -43.28929251, -0.29769532, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1422991, 234.64533188, 0.00847712, 283.04475753, 0.07680217, 28.30447575, 0.29284589, -358.46013937, -0.00924204, -432.3983879, -0.0847842, -43.23983879, -0.30082792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1422990, 32774751.13491279, 0.15, 0.003125, 0.001125, 13656146.30621366, 0.00281737)
    ops.section('Aggregator', 1422991, 1422990, 'Mz')
    ops.section('Aggregator', 1422992, 1422991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1422, 1422991, 0.46286927589, 1422992, 0.46286927589, 1422990)
    # Create element
    ops.element('forceBeamColumn', 1422, 422, 522, 1422, 1422)

    # Create geometric transformation
    ops.geomTransf('Linear', 1522, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1522990, 237.73623237, 0.00863451, 285.67875867, 0.0862057, 28.56787587, 0.33664484, -363.34472184, -0.00939849, -436.61779304, -0.09516347, -43.6617793, -0.34560261, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1522991, 237.73623237, 0.00863451, 285.67875867, 0.08539413, 28.56787587, 0.33583327, -363.34472184, -0.00939849, -436.61779304, -0.09426618, -43.6617793, -0.34470532, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1522990, 33793008.03980222, 0.15, 0.003125, 0.001125, 14080420.01658426, 0.00281737)
    ops.section('Aggregator', 1522991, 1522990, 'Mz')
    ops.section('Aggregator', 1522992, 1522991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1522, 1522991, 0.39929860295999997, 1522992, 0.39929860295999997, 1522990)
    # Create element
    ops.element('forceBeamColumn', 1522, 522, 622, 1522, 1522)

    # Create geometric transformation
    ops.geomTransf('Linear', 1622, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1622990, 233.37858007, 0.00854258, 281.16140039, 0.06479841, 28.11614004, 0.26056278, -356.67516555, -0.00930584, -429.70219888, -0.07150393, -42.97021989, -0.2672683, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1622991, 157.36592151, 0.00822736, 189.58562029, 0.06213436, 18.95856203, 0.2585254, -241.12457723, -0.00881499, -290.49334253, -0.06841614, -29.04933425, -0.26480718, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1622990, 33119190.81718307, 0.15, 0.003125, 0.001125, 13799662.84049295, 0.00281737)
    ops.section('Aggregator', 1622991, 1622990, 'Mz')
    ops.section('Aggregator', 1622992, 1622991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1622, 1622991, 0.46322049420000005, 1622992, 0.46322049420000005, 1622990)
    # Create element
    ops.element('forceBeamColumn', 1622, 622, 722, 1622, 1622)

    # Create geometric transformation
    ops.geomTransf('Linear', 1032, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1032990, 159.86121652, 0.00813339, 192.52515151, 0.06163619, 19.25251515, 0.25678393, -244.86534634, -0.00871816, -294.89790539, -0.06787243, -29.48979054, -0.26302016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1032991, 237.34506992, 0.00843892, 285.84103476, 0.06402955, 28.58410348, 0.25654909, -362.4831523, -0.00919775, -436.54818434, -0.07066037, -43.65481843, -0.26317992, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1032990, 33212158.26318944, 0.15, 0.003125, 0.001125, 13838399.27632893, 0.00281737)
    ops.section('Aggregator', 1032991, 1032990, 'Mz')
    ops.section('Aggregator', 1032992, 1032991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1032, 1032991, 0.46393657986000003, 1032992, 0.46393657986000003, 1032990)
    # Create element
    ops.element('forceBeamColumn', 1032, 32, 132, 1032, 1032)

    # Create geometric transformation
    ops.geomTransf('Linear', 1132, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1132990, 232.3913936, 0.00838481, 277.19257396, 0.10279147, 27.7192574, 0.35731402, -355.30585094, -0.00910569, -423.80288634, -0.11348445, -42.38028863, -0.368007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1132991, 232.3913936, 0.00838481, 277.19257396, 0.10286641, 27.7192574, 0.35738895, -355.30585094, -0.00910569, -423.80288634, -0.1135673, -42.38028863, -0.36808985, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1132990, 35585953.13802951, 0.15, 0.003125, 0.001125, 14827480.47417896, 0.00281737)
    ops.section('Aggregator', 1132991, 1132990, 'Mz')
    ops.section('Aggregator', 1132992, 1132991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1132, 1132991, 0.39289250339000004, 1132992, 0.39289250339000004, 1132990)
    # Create element
    ops.element('forceBeamColumn', 1132, 132, 232, 1132, 1132)

    # Create geometric transformation
    ops.geomTransf('Linear', 1232, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1232990, 236.4640987, 0.0085767, 284.17371777, 0.07519689, 28.41737178, 0.28993309, -361.38694535, -0.00933615, -434.30132682, -0.08299337, -43.43013268, -0.29772957, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1232991, 312.68482061, 0.00892054, 375.77293318, 0.07686196, 37.57729332, 0.29159817, -361.71752131, -0.00926059, -434.69860066, -0.07967036, -43.46986007, -0.29440657, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1232990, 33771611.46501855, 0.15, 0.003125, 0.001125, 14071504.77709106, 0.00281737)
    ops.section('Aggregator', 1232991, 1232990, 'Mz')
    ops.section('Aggregator', 1232992, 1232991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1232, 1232991, 0.46568765907, 1232992, 0.46568765907, 1232990)
    # Create element
    ops.element('forceBeamColumn', 1232, 232, 332, 1232, 1232)

    # Create geometric transformation
    ops.geomTransf('Linear', 1332, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1332990, 315.57909196, 0.00880022, 380.24683702, 0.10738976, 38.0246837, 0.3593379, -364.92622036, -0.00914054, -439.706066, -0.11131189, -43.9706066, -0.36326004, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1332991, 315.57909196, 0.00880022, 380.24683702, 0.10766595, 38.0246837, 0.3596141, -364.92622036, -0.00914054, -439.706066, -0.11159812, -43.9706066, -0.36354626, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1332990, 33080249.19951515, 0.15, 0.003125, 0.001125, 13783437.16646465, 0.00281737)
    ops.section('Aggregator', 1332991, 1332990, 'Mz')
    ops.section('Aggregator', 1332992, 1332991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1332, 1332991, 0.39690707121, 1332992, 0.39690707121, 1332990)
    # Create element
    ops.element('forceBeamColumn', 1332, 332, 432, 1332, 1332)

    # Create geometric transformation
    ops.geomTransf('Linear', 1432, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1432990, 310.4491452, 0.00874177, 372.23117438, 0.07463079, 37.22311744, 0.29094907, -359.11114879, -0.00907281, -430.57733196, -0.07735561, -43.0577332, -0.29367389, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1432991, 234.75323325, 0.00840715, 281.47112998, 0.07408104, 28.147113, 0.29039931, -358.72641199, -0.00914675, -430.11602925, -0.08175773, -43.01160292, -0.298076, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1432990, 34350606.4881773, 0.15, 0.003125, 0.001125, 14312752.70340721, 0.00281737)
    ops.section('Aggregator', 1432991, 1432990, 'Mz')
    ops.section('Aggregator', 1432992, 1432991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1432, 1432991, 0.46228179489000004, 1432992, 0.46228179489000004, 1432990)
    # Create element
    ops.element('forceBeamColumn', 1432, 432, 532, 1432, 1432)

    # Create geometric transformation
    ops.geomTransf('Linear', 1532, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1532990, 235.69104552, 0.00843768, 282.52957636, 0.10512349, 28.25295764, 0.35809741, -360.16264995, -0.0091793, -431.73723754, -0.11607796, -43.17372375, -0.36905189, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1532991, 235.69104552, 0.00843768, 282.52957636, 0.10464364, 28.25295764, 0.35761757, -360.16264995, -0.0091793, -431.73723754, -0.11554743, -43.17372375, -0.36852136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1532990, 34408286.43668364, 0.15, 0.003125, 0.001125, 14336786.01528485, 0.00281737)
    ops.section('Aggregator', 1532991, 1532990, 'Mz')
    ops.section('Aggregator', 1532992, 1532991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1532, 1532991, 0.39529765335, 1532992, 0.39529765335, 1532990)
    # Create element
    ops.element('forceBeamColumn', 1532, 532, 632, 1532, 1532)

    # Create geometric transformation
    ops.geomTransf('Linear', 1632, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1632990, 239.07198635, 0.00861489, 287.23670551, 0.06377415, 28.72367055, 0.25997757, -365.3231392, -0.00937826, -438.92308987, -0.07036395, -43.89230899, -0.26656737, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1632991, 161.12506251, 0.00830131, 193.5861781, 0.06104357, 19.35861781, 0.25686993, -246.88172347, -0.00888955, -296.61983398, -0.06720293, -29.6619834, -0.26302929, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1632990, 33835166.03036326, 0.15, 0.003125, 0.001125, 14097985.84598469, 0.00281737)
    ops.section('Aggregator', 1632991, 1632990, 'Mz')
    ops.section('Aggregator', 1632992, 1632991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1632, 1632991, 0.46778021367000006, 1632992, 0.46778021367000006, 1632990)
    # Create element
    ops.element('forceBeamColumn', 1632, 632, 732, 1632, 1632)

    # Create geometric transformation
    ops.geomTransf('Linear', 1042, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1042990, 329.91406654, 0.00624366, 396.02272124, 0.05384055, 39.60227212, 0.22851636, -488.14155543, -0.00664509, -585.95606171, -0.05878847, -58.59560617, -0.23346428, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1042991, 489.28730104, 0.00657656, 587.33139347, 0.05914828, 58.73313935, 0.24764964, -489.28730104, -0.00657656, -587.33139347, -0.05914828, -58.73313935, -0.24764964, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1042990, 34064684.82340682, 0.195, 0.00686563, 0.0014625, 14193618.67641951, 0.00415543)
    ops.section('Aggregator', 1042991, 1042990, 'Mz')
    ops.section('Aggregator', 1042992, 1042991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1042, 1042991, 0.53050013169, 1042992, 0.53050013169, 1042990)
    # Create element
    ops.element('forceBeamColumn', 1042, 42, 142, 1042, 1042)

    # Create geometric transformation
    ops.geomTransf('Linear', 1142, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1142990, 471.61496251, 0.00658741, 567.38400121, 0.09039857, 56.73840012, 0.30947539, -471.61496251, -0.00658741, -567.38400121, -0.09039857, -56.73840012, -0.30947539, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1142991, 471.61496251, 0.00658741, 567.38400121, 0.09017832, 56.73840012, 0.30925514, -471.61496251, -0.00658741, -567.38400121, -0.09017832, -56.73840012, -0.30925514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1142990, 33489785.8345525, 0.195, 0.00686563, 0.0014625, 13954077.43106354, 0.00415543)
    ops.section('Aggregator', 1142991, 1142990, 'Mz')
    ops.section('Aggregator', 1142992, 1142991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1142, 1142991, 0.45646088043, 1142992, 0.45646088043, 1142990)
    # Create element
    ops.element('forceBeamColumn', 1142, 142, 242, 1142, 1142)

    # Create geometric transformation
    ops.geomTransf('Linear', 1242, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1242990, 483.72955819, 0.00655117, 579.05893105, 0.07683409, 57.90589311, 0.26613402, -483.72955819, -0.00655117, -579.05893105, -0.07683409, -57.90589311, -0.26613402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1242991, 640.3370393, 0.00677624, 766.52930384, 0.07972297, 76.65293038, 0.2690229, -640.3370393, -0.00677624, -766.52930384, -0.07972297, -76.65293038, -0.2690229, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1242990, 34745317.79771817, 0.195, 0.00686563, 0.0014625, 14477215.74904924, 0.00415543)
    ops.section('Aggregator', 1242991, 1242990, 'Mz')
    ops.section('Aggregator', 1242992, 1242991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1242, 1242991, 0.5282622377599999, 1242992, 0.5282622377599999, 1242990)
    # Create element
    ops.element('forceBeamColumn', 1242, 242, 342, 1242, 1242)

    # Create geometric transformation
    ops.geomTransf('Linear', 1342, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1342990, 652.37925832, 0.00696846, 787.45922559, 0.12047206, 78.74592256, 0.33463165, -652.37925832, -0.00696846, -787.45922559, -0.12047206, -78.74592256, -0.33463165, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1342991, 811.3036987, 0.00716869, 979.29015086, 0.12438229, 97.92901509, 0.33854188, -811.3036987, -0.00716869, -979.29015086, -0.12438229, -97.92901509, -0.33854188, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1342990, 32592564.04078744, 0.195, 0.00686563, 0.0014625, 13580235.01699477, 0.00415543)
    ops.section('Aggregator', 1342991, 1342990, 'Mz')
    ops.section('Aggregator', 1342992, 1342991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1342, 1342991, 0.46694149237, 1342992, 0.46694149237, 1342990)
    # Create element
    ops.element('forceBeamColumn', 1342, 342, 442, 1342, 1342)

    # Create geometric transformation
    ops.geomTransf('Linear', 1442, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1442990, 798.45239064, 0.00693483, 952.09496401, 0.08201399, 95.2094964, 0.27127406, -798.45239064, -0.00693483, -952.09496401, -0.08201399, -95.2094964, -0.27127406, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1442991, 485.04044871, 0.00652317, 578.37458309, 0.07474647, 57.83745831, 0.26400654, -485.04044871, -0.00652317, -578.37458309, -0.07474647, -57.83745831, -0.26400654, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1442990, 35654166.58409047, 0.195, 0.00686563, 0.0014625, 14855902.74337103, 0.00415543)
    ops.section('Aggregator', 1442991, 1442990, 'Mz')
    ops.section('Aggregator', 1442992, 1442991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1442, 1442991, 0.52837348231, 1442992, 0.52837348231, 1442990)
    # Create element
    ops.element('forceBeamColumn', 1442, 442, 542, 1442, 1442)

    # Create geometric transformation
    ops.geomTransf('Linear', 1542, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1542990, 480.80287272, 0.00665208, 579.05381398, 0.09107668, 57.9053814, 0.3079461, -480.80287272, -0.00665208, -579.05381398, -0.09107668, -57.9053814, -0.3079461, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1542991, 480.80287272, 0.00665208, 579.05381398, 0.08992291, 57.9053814, 0.30679233, -480.80287272, -0.00665208, -579.05381398, -0.08992291, -57.9053814, -0.30679233, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1542990, 33207527.30073932, 0.195, 0.00686563, 0.0014625, 13836469.70864138, 0.00415543)
    ops.section('Aggregator', 1542991, 1542990, 'Mz')
    ops.section('Aggregator', 1542992, 1542991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1542, 1542991, 0.4611069559, 1542992, 0.4611069559, 1542990)
    # Create element
    ops.element('forceBeamColumn', 1542, 542, 642, 1542, 1542)

    # Create geometric transformation
    ops.geomTransf('Linear', 1642, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1642990, 482.58338151, 0.006564, 580.7539978, 0.06558131, 58.07539978, 0.2551079, -482.58338151, -0.006564, -580.7539978, -0.06558131, -58.07539978, -0.2551079, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1642991, 325.41880073, 0.00622894, 391.61785657, 0.05951904, 39.16178566, 0.23278364, -481.54325398, -0.00663273, -579.50227998, -0.06501312, -57.950228, -0.23827772, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1642990, 33410782.16014967, 0.195, 0.00686563, 0.0014625, 13921159.2333957, 0.00415543)
    ops.section('Aggregator', 1642991, 1642990, 'Mz')
    ops.section('Aggregator', 1642992, 1642991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1642, 1642991, 0.5276304483300001, 1642992, 0.5276304483300001, 1642990)
    # Create element
    ops.element('forceBeamColumn', 1642, 642, 742, 1642, 1642)

    # Create geometric transformation
    ops.geomTransf('Linear', 1052, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1052990, 238.71422967, 0.00873491, 288.27093917, 0.05688175, 28.82709392, 0.22581308, -238.71422967, -0.00873491, -288.27093917, -0.05688175, -28.82709392, -0.22581308, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1052991, 353.49011239, 0.00917595, 426.87411986, 0.06081554, 42.68741199, 0.23643938, -353.49011239, -0.00917595, -426.87411986, -0.06081554, -42.68741199, -0.23643938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1052990, 32466652.91366718, 0.15, 0.003125, 0.001125, 13527772.04736133, 0.00281737)
    ops.section('Aggregator', 1052991, 1052990, 'Mz')
    ops.section('Aggregator', 1052992, 1052991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1052, 1052991, 0.5269207649600001, 1052992, 0.5269207649600001, 1052990)
    # Create element
    ops.element('forceBeamColumn', 1052, 52, 152, 1052, 1052)

    # Create geometric transformation
    ops.geomTransf('Linear', 1152, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1152990, 352.48630739, 0.00910542, 427.20539322, 0.10121015, 42.72053932, 0.32017037, -352.48630739, -0.00910542, -427.20539322, -0.10121015, -42.72053932, -0.32017037, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1152991, 352.48630739, 0.00910542, 427.20539322, 0.10084808, 42.72053932, 0.3198083, -352.48630739, -0.00910542, -427.20539322, -0.10084808, -42.72053932, -0.3198083, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1152990, 31405198.8347488, 0.15, 0.003125, 0.001125, 13085499.51447867, 0.00281737)
    ops.section('Aggregator', 1152991, 1152990, 'Mz')
    ops.section('Aggregator', 1152992, 1152991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1152, 1152991, 0.45670395853, 1152992, 0.45670395853, 1152990)
    # Create element
    ops.element('forceBeamColumn', 1152, 152, 252, 1152, 1152)

    # Create geometric transformation
    ops.geomTransf('Linear', 1252, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1252990, 367.79963603, 0.00908627, 442.82424162, 0.06892774, 44.28242416, 0.25677263, -367.79963603, -0.00908627, -442.82424162, -0.06892774, -44.28242416, -0.25677263, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1252991, 367.79963603, 0.00908627, 442.82424162, 0.06950299, 44.28242416, 0.25734788, -367.79963603, -0.00908627, -442.82424162, -0.06950299, -44.28242416, -0.25734788, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1252990, 33288545.19487693, 0.15, 0.003125, 0.001125, 13870227.16453206, 0.00281737)
    ops.section('Aggregator', 1252991, 1252990, 'Mz')
    ops.section('Aggregator', 1252992, 1252991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1252, 1252991, 0.5323541267, 1252992, 0.5323541267, 1252990)
    # Create element
    ops.element('forceBeamColumn', 1252, 252, 352, 1252, 1252)

    # Create geometric transformation
    ops.geomTransf('Linear', 1352, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1352990, 360.32957961, 0.00935535, 434.55727317, 0.09624373, 43.45572732, 0.31108763, -360.32957961, -0.00935535, -434.55727317, -0.09624373, -43.45572732, -0.31108763, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1352991, 360.32957961, 0.00935535, 434.55727317, 0.09681422, 43.45572732, 0.31165812, -360.32957961, -0.00935535, -434.55727317, -0.09681422, -43.45572732, -0.31165812, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1352990, 32835703.44126585, 0.15, 0.003125, 0.001125, 13681543.10052744, 0.00281737)
    ops.section('Aggregator', 1352991, 1352990, 'Mz')
    ops.section('Aggregator', 1352992, 1352991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1352, 1352991, 0.46545421642999996, 1352992, 0.46545421642999996, 1352990)
    # Create element
    ops.element('forceBeamColumn', 1352, 352, 452, 1352, 1352)

    # Create geometric transformation
    ops.geomTransf('Linear', 1452, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1452990, 359.11762115, 0.00939099, 435.94618998, 0.0735171, 43.594619, 0.26129343, -359.11762115, -0.00939099, -435.94618998, -0.0735171, -43.594619, -0.26129343, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1452991, 359.11762115, 0.00939099, 435.94618998, 0.07327828, 43.594619, 0.26105461, -359.11762115, -0.00939099, -435.94618998, -0.07327828, -43.594619, -0.26105461, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1452990, 30903108.7228809, 0.15, 0.003125, 0.001125, 12876295.30120037, 0.00281737)
    ops.section('Aggregator', 1452991, 1452990, 'Mz')
    ops.section('Aggregator', 1452992, 1452991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1452, 1452991, 0.53254847895, 1452992, 0.53254847895, 1452990)
    # Create element
    ops.element('forceBeamColumn', 1452, 452, 552, 1452, 1452)

    # Create geometric transformation
    ops.geomTransf('Linear', 1552, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1552990, 362.2545199, 0.00924947, 435.45543757, 0.09411104, 43.54554376, 0.30920635, -362.2545199, -0.00924947, -435.45543757, -0.09411104, -43.54554376, -0.30920635, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1552991, 362.2545199, 0.00924947, 435.45543757, 0.09475112, 43.54554376, 0.30984643, -362.2545199, -0.00924947, -435.45543757, -0.09475112, -43.54554376, -0.30984643, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1552990, 33705537.66410982, 0.15, 0.003125, 0.001125, 14043974.02671243, 0.00281737)
    ops.section('Aggregator', 1552991, 1552990, 'Mz')
    ops.section('Aggregator', 1552992, 1552991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1552, 1552991, 0.46491017809, 1552992, 0.46491017809, 1552990)
    # Create element
    ops.element('forceBeamColumn', 1552, 552, 652, 1552, 1552)

    # Create geometric transformation
    ops.geomTransf('Linear', 1652, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1652990, 354.69093184, 0.00896178, 427.60215907, 0.06181466, 42.76021591, 0.23890271, -354.69093184, -0.00896178, -427.60215907, -0.06181466, -42.76021591, -0.23890271, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1652991, 239.32033181, 0.00853782, 288.51566647, 0.05824673, 28.85156665, 0.23214063, -239.32033181, -0.00853782, -288.51566647, -0.05824673, -28.85156665, -0.23214063, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1652990, 32934920.46621047, 0.15, 0.003125, 0.001125, 13722883.5275877, 0.00281737)
    ops.section('Aggregator', 1652991, 1652990, 'Mz')
    ops.section('Aggregator', 1652992, 1652991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1652, 1652991, 0.52392935474, 1652992, 0.52392935474, 1652990)
    # Create element
    ops.element('forceBeamColumn', 1652, 652, 752, 1652, 1652)

    # Create geometric transformation
    ops.geomTransf('Linear', 1003, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1003990, 241.77909632, 0.00868086, 290.21109524, 0.0651404, 29.02110952, 0.25427985, -241.77909632, -0.00868086, -290.21109524, -0.0651404, -29.02110952, -0.25427985, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1003991, 358.48309567, 0.00900985, 430.29266551, 0.06576149, 43.02926655, 0.23960532, -472.70367844, -0.00957758, -567.39335342, -0.07012416, -56.73933534, -0.243968, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1003990, 34078626.00910544, 0.15, 0.003125, 0.001125, 14199427.50379393, 0.00281737)
    ops.section('Aggregator', 1003991, 1003990, 'Mz')
    ops.section('Aggregator', 1003992, 1003991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1003, 1003991, 0.52871043079, 1003992, 0.52871043079, 1003990)
    # Create element
    ops.element('forceBeamColumn', 1003, 3, 103, 1003, 1003)

    # Create geometric transformation
    ops.geomTransf('Linear', 1103, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1103990, 356.23760574, 0.00889452, 428.15249947, 0.09782304, 42.81524995, 0.31642296, -469.64689243, -0.00945962, -564.45610352, -0.10433473, -56.44561035, -0.32293464, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1103991, 355.85489792, 0.00899626, 427.69253313, 0.11017933, 42.76925331, 0.32877925, -355.85489792, -0.00899626, -427.69253313, -0.11017933, -42.76925331, -0.32877925, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1103990, 33747866.08841468, 0.15, 0.003125, 0.001125, 14061610.87017279, 0.00281737)
    ops.section('Aggregator', 1103991, 1103990, 'Mz')
    ops.section('Aggregator', 1103992, 1103991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1103, 1103991, 0.45745671385000003, 1103992, 0.45745671385000003, 1103990)
    # Create element
    ops.element('forceBeamColumn', 1103, 103, 203, 1103, 1103)

    # Create geometric transformation
    ops.geomTransf('Linear', 1203, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1203990, 361.14427751, 0.00914854, 435.71363915, 0.0709477, 43.57136391, 0.25957537, -361.14427751, -0.00914854, -435.71363915, -0.0709477, -43.57136391, -0.25957537, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1203991, 361.14427751, 0.00914854, 435.71363915, 0.07084136, 43.57136391, 0.25946903, -361.14427751, -0.00914854, -435.71363915, -0.07084136, -43.57136391, -0.25946903, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1203990, 32725575.24903189, 0.15, 0.003125, 0.001125, 13635656.35376329, 0.00281737)
    ops.section('Aggregator', 1203991, 1203990, 'Mz')
    ops.section('Aggregator', 1203992, 1203991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1203, 1203991, 0.5301449055199999, 1203992, 0.5301449055199999, 1203990)
    # Create element
    ops.element('forceBeamColumn', 1203, 203, 303, 1203, 1203)

    # Create geometric transformation
    ops.geomTransf('Linear', 1303, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1303990, 356.95338, 0.00921261, 428.49801573, 0.09390852, 42.84980157, 0.31039455, -356.95338, -0.00921261, -428.49801573, -0.09390852, -42.84980157, -0.31039455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1303991, 356.95338, 0.00921261, 428.49801573, 0.09415006, 42.84980157, 0.31063609, -356.95338, -0.00921261, -428.49801573, -0.09415006, -42.84980157, -0.31063609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1303990, 34054197.30670778, 0.15, 0.003125, 0.001125, 14189248.87779491, 0.00281737)
    ops.section('Aggregator', 1303991, 1303990, 'Mz')
    ops.section('Aggregator', 1303992, 1303991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1303, 1303991, 0.46192357843000004, 1303992, 0.46192357843000004, 1303990)
    # Create element
    ops.element('forceBeamColumn', 1303, 303, 403, 1303, 1303)

    # Create geometric transformation
    ops.geomTransf('Linear', 1403, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1403990, 357.62083893, 0.00909879, 430.38983668, 0.06966776, 43.03898367, 0.2590833, -357.62083893, -0.00909879, -430.38983668, -0.06966776, -43.03898367, -0.2590833, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1403991, 357.62083893, 0.00909879, 430.38983668, 0.0696834, 43.03898367, 0.25909895, -357.62083893, -0.00909879, -430.38983668, -0.0696834, -43.03898367, -0.25909895, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1403990, 33399019.58907492, 0.15, 0.003125, 0.001125, 13916258.16211455, 0.00281737)
    ops.section('Aggregator', 1403991, 1403990, 'Mz')
    ops.section('Aggregator', 1403992, 1403991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1403, 1403991, 0.5279397719900001, 1403992, 0.5279397719900001, 1403990)
    # Create element
    ops.element('forceBeamColumn', 1403, 403, 503, 1403, 1403)

    # Create geometric transformation
    ops.geomTransf('Linear', 1503, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1503990, 359.67713827, 0.00921782, 434.73299684, 0.12500432, 43.47329968, 0.34124854, -359.67713827, -0.00921782, -434.73299684, -0.12500432, -43.47329968, -0.34124854, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1503991, 360.05894267, 0.0091093, 435.19447452, 0.11083558, 43.51944745, 0.32707979, -474.64710871, -0.00970287, -573.69439994, -0.11823152, -57.36943999, -0.33447573, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1503990, 32212701.11544399, 0.15, 0.003125, 0.001125, 13421958.79810166, 0.00281737)
    ops.section('Aggregator', 1503991, 1503990, 'Mz')
    ops.section('Aggregator', 1503992, 1503991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1503, 1503991, 0.46244010939999997, 1503992, 0.46244010939999997, 1503990)
    # Create element
    ops.element('forceBeamColumn', 1503, 503, 603, 1503, 1503)

    # Create geometric transformation
    ops.geomTransf('Linear', 1603, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1603990, 362.06921646, 0.00913296, 435.6646976, 0.06055466, 43.56646976, 0.23157445, -477.40135858, -0.00971465, -574.43966254, -0.06457488, -57.44396625, -0.23559467, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1603991, 244.19383666, 0.00879895, 293.82954741, 0.06019944, 29.38295474, 0.24805319, -244.19383666, -0.00879895, -293.82954741, -0.06019944, -29.38295474, -0.24805319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1603990, 33446646.68104288, 0.15, 0.003125, 0.001125, 13936102.78376787, 0.00281737)
    ops.section('Aggregator', 1603991, 1603990, 'Mz')
    ops.section('Aggregator', 1603992, 1603991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1603, 1603991, 0.5323290025699999, 1603992, 0.5323290025699999, 1603990)
    # Create element
    ops.element('forceBeamColumn', 1603, 603, 703, 1603, 1603)

    # Create geometric transformation
    ops.geomTransf('Linear', 1013, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1013990, 268.23880347, 0.00789749, 322.75437232, 0.0648324, 32.27543723, 0.25254021, -397.14479431, -0.00844688, -477.85859893, -0.07082025, -47.78585989, -0.25852806, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1013991, 397.4081962, 0.00835533, 478.17553336, 0.06732571, 47.81755334, 0.25503352, -397.4081962, -0.00835533, -478.17553336, -0.06732571, -47.81755334, -0.25503352, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1013990, 33452851.94710712, 0.165, 0.00415938, 0.0012375, 13938688.31129463, 0.00326155)
    ops.section('Aggregator', 1013991, 1013990, 'Mz')
    ops.section('Aggregator', 1013992, 1013991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1013, 1013991, 0.53274288822, 1013992, 0.53274288822, 1013990)
    # Create element
    ops.element('forceBeamColumn', 1013, 13, 113, 1013, 1013)

    # Create geometric transformation
    ops.geomTransf('Linear', 1113, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1113990, 401.70874208, 0.0080944, 485.65032844, 0.09459133, 48.56503284, 0.31160958, -401.70874208, -0.0080944, -485.65032844, -0.09459133, -48.56503284, -0.31160958, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1113991, 401.70874208, 0.0080944, 485.65032844, 0.09568465, 48.56503284, 0.3127029, -401.70874208, -0.0080944, -485.65032844, -0.09568465, -48.56503284, -0.3127029, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1113990, 32144601.24154914, 0.165, 0.00415938, 0.0012375, 13393583.85064548, 0.00326155)
    ops.section('Aggregator', 1113991, 1113990, 'Mz')
    ops.section('Aggregator', 1113992, 1113991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1113, 1113991, 0.46079074286000005, 1113992, 0.46079074286000005, 1113990)
    # Create element
    ops.element('forceBeamColumn', 1113, 113, 213, 1113, 1113)

    # Create geometric transformation
    ops.geomTransf('Linear', 1213, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1213990, 405.59896829, 0.00813694, 485.78113228, 0.079992, 48.57811323, 0.26782403, -405.59896829, -0.00813694, -485.78113228, -0.079992, -48.57811323, -0.26782403, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1213991, 536.582459, 0.00843455, 642.6585245, 0.08420211, 64.26585245, 0.27203414, -536.582459, -0.00843455, -642.6585245, -0.08420211, -64.26585245, -0.27203414, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1213990, 34620721.58893697, 0.165, 0.00415938, 0.0012375, 14425300.66205707, 0.00326155)
    ops.section('Aggregator', 1213991, 1213990, 'Mz')
    ops.section('Aggregator', 1213992, 1213991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1213, 1213991, 0.53239056236, 1213992, 0.53239056236, 1213990)
    # Create element
    ops.element('forceBeamColumn', 1213, 213, 313, 1213, 1213)

    # Create geometric transformation
    ops.geomTransf('Linear', 1313, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1313990, 533.70141015, 0.00862958, 645.37863468, 0.12838377, 64.53786347, 0.34299338, -533.70141015, -0.00862958, -645.37863468, -0.12838377, -64.53786347, -0.34299338, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1313991, 533.70141015, 0.00862958, 645.37863468, 0.12690239, 64.53786347, 0.341512, -533.70141015, -0.00862958, -645.37863468, -0.12690239, -64.53786347, -0.341512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1313990, 32075362.82710204, 0.165, 0.00415938, 0.0012375, 13364734.51129252, 0.00326155)
    ops.section('Aggregator', 1313991, 1313990, 'Mz')
    ops.section('Aggregator', 1313992, 1313991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1313, 1313991, 0.46596237023, 1313992, 0.46596237023, 1313990)
    # Create element
    ops.element('forceBeamColumn', 1313, 313, 413, 1313, 1313)

    # Create geometric transformation
    ops.geomTransf('Linear', 1413, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1413990, 518.82894956, 0.00826944, 622.8546364, 0.08515131, 62.28546364, 0.27623238, -518.82894956, -0.00826944, -622.8546364, -0.08515131, -62.28546364, -0.27623238, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1413991, 392.27926703, 0.00797487, 470.93162485, 0.08220407, 47.09316248, 0.27328514, -392.27926703, -0.00797487, -470.93162485, -0.08220407, -47.09316248, -0.27328514, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1413990, 34039548.52744535, 0.165, 0.00415938, 0.0012375, 14183145.2197689, 0.00326155)
    ops.section('Aggregator', 1413991, 1413990, 'Mz')
    ops.section('Aggregator', 1413992, 1413991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1413, 1413991, 0.5233380766300001, 1413992, 0.5233380766300001, 1413990)
    # Create element
    ops.element('forceBeamColumn', 1413, 413, 513, 1413, 1413)

    # Create geometric transformation
    ops.geomTransf('Linear', 1513, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1513990, 402.36626213, 0.00801741, 482.57840647, 0.09100752, 48.25784065, 0.30816929, -402.36626213, -0.00801741, -482.57840647, -0.09100752, -48.25784065, -0.30816929, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1513991, 402.36626213, 0.00801741, 482.57840647, 0.09116974, 48.25784065, 0.30833151, -402.36626213, -0.00801741, -482.57840647, -0.09116974, -48.25784065, -0.30833151, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1513990, 34279759.47576403, 0.165, 0.00415938, 0.0012375, 14283233.11490168, 0.00326155)
    ops.section('Aggregator', 1513991, 1513990, 'Mz')
    ops.section('Aggregator', 1513992, 1513991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1513, 1513991, 0.46048620360000003, 1513992, 0.46048620360000003, 1513990)
    # Create element
    ops.element('forceBeamColumn', 1513, 513, 613, 1513, 1513)

    # Create geometric transformation
    ops.geomTransf('Linear', 1613, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1613990, 406.50573753, 0.0082485, 488.60918511, 0.0665232, 48.86091851, 0.25357461, -406.50573753, -0.0082485, -488.60918511, -0.0665232, -48.86091851, -0.25357461, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1613991, 274.278538, 0.00779763, 329.67557545, 0.06431795, 32.96755754, 0.25136936, -405.87368467, -0.00834418, -487.84947422, -0.07026335, -48.78494742, -0.25731476, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1613990, 33726340.1862438, 0.165, 0.00415938, 0.0012375, 14052641.74426825, 0.00326155)
    ops.section('Aggregator', 1613991, 1613990, 'Mz')
    ops.section('Aggregator', 1613992, 1613991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1613, 1613991, 0.5346123850200001, 1613992, 0.5346123850200001, 1613990)
    # Create element
    ops.element('forceBeamColumn', 1613, 613, 713, 1613, 1613)

    # Create geometric transformation
    ops.geomTransf('Linear', 1023, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1023990, 244.77843117, 0.00909919, 295.44910574, 0.07244315, 29.54491057, 0.25923228, -244.77843117, -0.00909919, -295.44910574, -0.07244315, -29.54491057, -0.25923228, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1023991, 244.8982102, 0.00897982, 295.59367979, 0.06902444, 29.55936798, 0.25581357, -361.93173815, -0.00973124, -436.85388401, -0.07551136, -43.6853884, -0.26230049, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1023990, 32604407.8843842, 0.125, 0.00260417, 0.00065104, 13585169.95182675, 0.00178813)
    ops.section('Aggregator', 1023991, 1023990, 'Mz')
    ops.section('Aggregator', 1023992, 1023991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1023, 1023991, 0.53536306928, 1023992, 0.53536306928, 1023990)
    # Create element
    ops.element('forceBeamColumn', 1023, 23, 123, 1023, 1023)

    # Create geometric transformation
    ops.geomTransf('Linear', 1123, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1123990, 241.91732599, 0.00866274, 290.81490233, 0.08393126, 29.08149023, 0.30139261, -357.42497103, -0.00937814, -429.66954771, -0.09183636, -42.96695477, -0.3092977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1123991, 241.91732599, 0.00866274, 290.81490233, 0.08289338, 29.08149023, 0.30035472, -357.42497103, -0.00937814, -429.66954771, -0.09069933, -42.96695477, -0.30816068, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1123990, 33693754.46140881, 0.125, 0.00260417, 0.00065104, 14039064.35892034, 0.00178813)
    ops.section('Aggregator', 1123991, 1123990, 'Mz')
    ops.section('Aggregator', 1123992, 1123991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1123, 1123991, 0.45985184336, 1123992, 0.45985184336, 1123990)
    # Create element
    ops.element('forceBeamColumn', 1123, 123, 223, 1123, 1123)

    # Create geometric transformation
    ops.geomTransf('Linear', 1223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1223990, 238.43129686, 0.00890654, 286.17404301, 0.07170046, 28.6174043, 0.26038204, -352.64198059, -0.00962618, -423.25392115, -0.07841822, -42.32539212, -0.26709979, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1223991, 353.07489492, 0.00948781, 423.77352091, 0.07486065, 42.37735209, 0.26354223, -353.07489492, -0.00948781, -423.77352091, -0.07486065, -42.37735209, -0.26354223, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1223990, 34095032.79786015, 0.125, 0.00260417, 0.00065104, 14206263.66577506, 0.00178813)
    ops.section('Aggregator', 1223991, 1223990, 'Mz')
    ops.section('Aggregator', 1223992, 1223991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1223, 1223991, 0.52999345839, 1223992, 0.52999345839, 1223990)
    # Create element
    ops.element('forceBeamColumn', 1223, 223, 323, 1223, 1223)

    # Create geometric transformation
    ops.geomTransf('Linear', 1323, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1323990, 354.37635647, 0.00953019, 428.48160441, 0.10877252, 42.84816044, 0.32505977, -354.37635647, -0.00953019, -428.48160441, -0.10877252, -42.84816044, -0.32505977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1323991, 354.37635647, 0.00953019, 428.48160441, 0.10904673, 42.84816044, 0.32533398, -354.37635647, -0.00953019, -428.48160441, -0.10904673, -42.84816044, -0.32533398, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1323990, 32107942.06613375, 0.125, 0.00260417, 0.00065104, 13378309.1942224, 0.00178813)
    ops.section('Aggregator', 1323991, 1323990, 'Mz')
    ops.section('Aggregator', 1323992, 1323991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1323, 1323991, 0.46234810470000004, 1323992, 0.46234810470000004, 1323990)
    # Create element
    ops.element('forceBeamColumn', 1323, 323, 423, 1323, 1323)

    # Create geometric transformation
    ops.geomTransf('Linear', 1423, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1423990, 356.72532375, 0.00935183, 430.30259084, 0.07875221, 43.03025908, 0.26788509, -356.72532375, -0.00935183, -430.30259084, -0.07875221, -43.03025908, -0.26788509, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1423991, 240.84064666, 0.00876866, 290.51583203, 0.07590287, 29.0515832, 0.26503575, -355.89123812, -0.00950166, -429.29646881, -0.08304857, -42.92964688, -0.27218145, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1423990, 32776770.40078261, 0.125, 0.00260417, 0.00065104, 13656987.66699276, 0.00178813)
    ops.section('Aggregator', 1423991, 1423990, 'Mz')
    ops.section('Aggregator', 1423992, 1423991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1423, 1423991, 0.52872880032, 1423992, 0.52872880032, 1423990)
    # Create element
    ops.element('forceBeamColumn', 1423, 423, 523, 1423, 1423)

    # Create geometric transformation
    ops.geomTransf('Linear', 1523, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1523990, 243.54629776, 0.00877219, 293.28393579, 0.08263854, 29.32839358, 0.29869571, -359.83872207, -0.00950159, -433.32589175, -0.09042369, -43.33258918, -0.30648086, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1523991, 243.54629776, 0.00877219, 293.28393579, 0.08305323, 29.32839358, 0.2991104, -359.83872207, -0.00950159, -433.32589175, -0.09087799, -43.33258918, -0.30693516, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1523990, 33235324.2709069, 0.125, 0.00260417, 0.00065104, 13848051.77954454, 0.00178813)
    ops.section('Aggregator', 1523991, 1523990, 'Mz')
    ops.section('Aggregator', 1523992, 1523991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1523, 1523991, 0.4628404564, 1523992, 0.4628404564, 1523990)
    # Create element
    ops.element('forceBeamColumn', 1523, 523, 623, 1523, 1523)

    # Create geometric transformation
    ops.geomTransf('Linear', 1623, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1623990, 242.25822356, 0.00898028, 293.28057598, 0.06336084, 29.3280576, 0.25091235, -358.03556772, -0.00974196, -433.44195288, -0.06931699, -43.34419529, -0.25686849, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1623991, 242.16983716, 0.00910162, 293.17357438, 0.06657535, 29.31735744, 0.25412685, -242.16983716, -0.00910162, -293.17357438, -0.06657535, -29.31735744, -0.25412685, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1623990, 31744806.13278959, 0.125, 0.00260417, 0.00065104, 13227002.55532899, 0.00178813)
    ops.section('Aggregator', 1623991, 1623990, 'Mz')
    ops.section('Aggregator', 1623992, 1623991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1623, 1623991, 0.53318687594, 1623992, 0.53318687594, 1623990)
    # Create element
    ops.element('forceBeamColumn', 1623, 623, 723, 1623, 1623)

    # Create geometric transformation
    ops.geomTransf('Linear', 1033, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1033990, 248.84848021, 0.00900656, 299.69309498, 0.07052471, 29.9693095, 0.25682175, -248.84848021, -0.00900656, -299.69309498, -0.07052471, -29.9693095, -0.25682175, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1033991, 249.14245567, 0.00888483, 300.04713539, 0.06781203, 30.00471354, 0.25410907, -368.00633558, -0.0096263, -443.19723227, -0.07418226, -44.31972323, -0.2604793, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1033990, 33213770.67120652, 0.125, 0.00260417, 0.00065104, 13839071.11300272, 0.00178813)
    ops.section('Aggregator', 1033991, 1033990, 'Mz')
    ops.section('Aggregator', 1033992, 1033991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1033, 1033991, 0.53677718448, 1033992, 0.53677718448, 1033990)
    # Create element
    ops.element('forceBeamColumn', 1033, 33, 133, 1033, 1033)

    # Create geometric transformation
    ops.geomTransf('Linear', 1133, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1133990, 237.33898749, 0.00885885, 285.51462474, 0.10106473, 28.55146247, 0.31838137, -350.97483984, -0.00958289, -422.2165551, -0.11059633, -42.22165551, -0.32791297, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1133991, 237.33898749, 0.00885885, 285.51462474, 0.10200532, 28.55146247, 0.31932196, -350.97483984, -0.00958289, -422.2165551, -0.11162676, -42.22165551, -0.3289434, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1133990, 33508052.22488997, 0.125, 0.00260417, 0.00065104, 13961688.42703749, 0.00178813)
    ops.section('Aggregator', 1133991, 1133990, 'Mz')
    ops.section('Aggregator', 1133992, 1133991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1133, 1133991, 0.46015804519000003, 1133992, 0.46015804519000003, 1133990)
    # Create element
    ops.element('forceBeamColumn', 1133, 133, 233, 1133, 1133)

    # Create geometric transformation
    ops.geomTransf('Linear', 1233, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1233990, 239.65969886, 0.00863297, 289.06981982, 0.07485133, 28.90698198, 0.26517783, -354.05125076, -0.00935687, -427.04523017, -0.08190044, -42.70452302, -0.27222694, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1233991, 354.99957629, 0.00920715, 428.18906992, 0.07719236, 42.81890699, 0.26751886, -354.99957629, -0.00920715, -428.18906992, -0.07719236, -42.81890699, -0.26751886, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1233990, 32797271.79096055, 0.125, 0.00260417, 0.00065104, 13665529.91290023, 0.00178813)
    ops.section('Aggregator', 1233991, 1233990, 'Mz')
    ops.section('Aggregator', 1233992, 1233991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1233, 1233991, 0.52541291516, 1233992, 0.52541291516, 1233990)
    # Create element
    ops.element('forceBeamColumn', 1233, 233, 333, 1233, 1233)

    # Create geometric transformation
    ops.geomTransf('Linear', 1333, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1333990, 347.97740327, 0.00925836, 419.19692039, 0.10667308, 41.91969204, 0.32636072, -347.97740327, -0.00925836, -419.19692039, -0.10667308, -41.91969204, -0.32636072, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1333991, 347.97740327, 0.00925836, 419.19692039, 0.10627859, 41.91969204, 0.32596623, -347.97740327, -0.00925836, -419.19692039, -0.10627859, -41.91969204, -0.32596623, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1333990, 33136342.97695247, 0.125, 0.00260417, 0.00065104, 13806809.57373019, 0.00178813)
    ops.section('Aggregator', 1333991, 1333990, 'Mz')
    ops.section('Aggregator', 1333992, 1333991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1333, 1333991, 0.45519175309000004, 1333992, 0.45519175309000004, 1333990)
    # Create element
    ops.element('forceBeamColumn', 1333, 333, 433, 1333, 1333)

    # Create geometric transformation
    ops.geomTransf('Linear', 1433, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1433990, 360.51950152, 0.00925754, 433.07456415, 0.07440325, 43.30745642, 0.26330021, -360.51950152, -0.00925754, -433.07456415, -0.07440325, -43.30745642, -0.26330021, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1433991, 243.36812491, 0.00868805, 292.34630632, 0.07231864, 29.23463063, 0.2612156, -359.55888318, -0.00940373, -431.92062002, -0.07911235, -43.192062, -0.26800931, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1433990, 33880734.93765924, 0.125, 0.00260417, 0.00065104, 14116972.89069135, 0.00178813)
    ops.section('Aggregator', 1433991, 1433990, 'Mz')
    ops.section('Aggregator', 1433992, 1433991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1433, 1433991, 0.52938913257, 1433992, 0.52938913257, 1433990)
    # Create element
    ops.element('forceBeamColumn', 1433, 433, 533, 1433, 1433)

    # Create geometric transformation
    ops.geomTransf('Linear', 1533, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1533990, 240.26231888, 0.0085396, 287.05476297, 0.09670018, 28.7054763, 0.31554475, -355.06197919, -0.00922707, -424.21230576, -0.1058088, -42.42123058, -0.32465337, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1533991, 240.26231888, 0.0085396, 287.05476297, 0.09734269, 28.7054763, 0.31618726, -355.06197919, -0.00922707, -424.21230576, -0.10651268, -42.42123058, -0.32535725, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1533990, 35204754.59945215, 0.125, 0.00260417, 0.00065104, 14668647.74977173, 0.00178813)
    ops.section('Aggregator', 1533991, 1533990, 'Mz')
    ops.section('Aggregator', 1533992, 1533991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1533, 1533991, 0.45694530944, 1533992, 0.45694530944, 1533990)
    # Create element
    ops.element('forceBeamColumn', 1533, 533, 633, 1533, 1533)

    # Create geometric transformation
    ops.geomTransf('Linear', 1633, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1633990, 242.3037432, 0.00903102, 291.52991277, 0.06281188, 29.15299128, 0.24980689, -358.30344122, -0.00977005, -431.09598549, -0.06868808, -43.10959855, -0.2556831, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1633991, 242.33802687, 0.00914241, 291.57116147, 0.06543587, 29.15711615, 0.25243088, -242.33802687, -0.00914241, -291.57116147, -0.06543587, -29.15711615, -0.25243088, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1633990, 33469527.86354483, 0.125, 0.00260417, 0.00065104, 13945636.60981034, 0.00178813)
    ops.section('Aggregator', 1633991, 1633990, 'Mz')
    ops.section('Aggregator', 1633992, 1633991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1633, 1633991, 0.53477361981, 1633992, 0.53477361981, 1633990)
    # Create element
    ops.element('forceBeamColumn', 1633, 633, 733, 1633, 1633)

    # Create geometric transformation
    ops.geomTransf('Linear', 1043, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1043990, 271.93801446, 0.00764331, 327.37106093, 0.06533331, 32.73710609, 0.25409387, -402.2687441, -0.00818539, -484.26898239, -0.07138597, -48.42689824, -0.26014653, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1043991, 403.06406892, 0.00808796, 485.22642973, 0.06759857, 48.52264297, 0.25635912, -403.06406892, -0.00808796, -485.22642973, -0.06759857, -48.52264297, -0.25635912, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1043990, 33318999.00239687, 0.165, 0.00415938, 0.0012375, 13882916.2509987, 0.00326155)
    ops.section('Aggregator', 1043991, 1043990, 'Mz')
    ops.section('Aggregator', 1043992, 1043991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1043, 1043991, 0.5297717067, 1043992, 0.5297717067, 1043990)
    # Create element
    ops.element('forceBeamColumn', 1043, 43, 143, 1043, 1043)

    # Create geometric transformation
    ops.geomTransf('Linear', 1143, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1143990, 399.27399761, 0.00825553, 482.08046011, 0.09588421, 48.20804601, 0.31179168, -399.27399761, -0.00825553, -482.08046011, -0.09588421, -48.20804601, -0.31179168, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1143991, 399.27399761, 0.00825553, 482.08046011, 0.0952058, 48.20804601, 0.31111327, -399.27399761, -0.00825553, -482.08046011, -0.0952058, -48.20804601, -0.31111327, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1143990, 32514696.07713829, 0.165, 0.00415938, 0.0012375, 13547790.03214095, 0.00326155)
    ops.section('Aggregator', 1143991, 1143990, 'Mz')
    ops.section('Aggregator', 1143992, 1143991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1143, 1143991, 0.46316136518, 1143992, 0.46316136518, 1143990)
    # Create element
    ops.element('forceBeamColumn', 1143, 143, 243, 1143, 1143)

    # Create geometric transformation
    ops.geomTransf('Linear', 1243, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1243990, 397.81019571, 0.00824136, 479.90901714, 0.08342898, 47.99090171, 0.27197568, -397.81019571, -0.00824136, -479.90901714, -0.08342898, -47.99090171, -0.27197568, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1243991, 525.99508675, 0.00855078, 634.54830426, 0.08770625, 63.45483043, 0.27625295, -525.99508675, -0.00855078, -634.54830426, -0.08770625, -63.45483043, -0.27625295, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1243990, 32749424.74636066, 0.165, 0.00415938, 0.0012375, 13645593.64431694, 0.00326155)
    ops.section('Aggregator', 1243991, 1243990, 'Mz')
    ops.section('Aggregator', 1243992, 1243991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1243, 1243991, 0.53037258716, 1243992, 0.53037258716, 1243990)
    # Create element
    ops.element('forceBeamColumn', 1243, 243, 343, 1243, 1243)

    # Create geometric transformation
    ops.geomTransf('Linear', 1343, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1343990, 538.83511663, 0.00846089, 649.25049721, 0.12555767, 64.92504972, 0.34069319, -538.83511663, -0.00846089, -649.25049721, -0.12555767, -64.92504972, -0.34069319, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1343991, 538.83511663, 0.00846089, 649.25049721, 0.1250837, 64.92504972, 0.34021922, -538.83511663, -0.00846089, -649.25049721, -0.1250837, -64.92504972, -0.34021922, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1343990, 33080864.203237, 0.165, 0.00415938, 0.0012375, 13783693.41801542, 0.00326155)
    ops.section('Aggregator', 1343991, 1343990, 'Mz')
    ops.section('Aggregator', 1343992, 1343991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1343, 1343991, 0.46482329084, 1343992, 0.46482329084, 1343990)
    # Create element
    ops.element('forceBeamColumn', 1343, 343, 443, 1343, 1343)

    # Create geometric transformation
    ops.geomTransf('Linear', 1443, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1443990, 526.83798341, 0.00843897, 635.01868637, 0.08670157, 63.50186864, 0.27587694, -526.83798341, -0.00843897, -635.01868637, -0.08670157, -63.50186864, -0.27587694, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1443991, 398.31308221, 0.00813612, 480.10253283, 0.08297039, 48.01025328, 0.27214575, -398.31308221, -0.00813612, -480.10253283, -0.08297039, -48.01025328, -0.27214575, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1443990, 32985349.31304377, 0.165, 0.00415938, 0.0012375, 13743895.54710157, 0.00326155)
    ops.section('Aggregator', 1443991, 1443990, 'Mz')
    ops.section('Aggregator', 1443992, 1443991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1443, 1443991, 0.52861004682, 1443992, 0.52861004682, 1443990)
    # Create element
    ops.element('forceBeamColumn', 1443, 443, 543, 1443, 1443)

    # Create geometric transformation
    ops.geomTransf('Linear', 1543, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1543990, 405.34026151, 0.00786305, 487.17033465, 0.09413391, 48.71703347, 0.31233718, -405.34026151, -0.00786305, -487.17033465, -0.09413391, -48.71703347, -0.31233718, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1543991, 405.34026151, 0.00786305, 487.17033465, 0.0933748, 48.71703347, 0.31157807, -405.34026151, -0.00786305, -487.17033465, -0.0933748, -48.71703347, -0.31157807, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1543990, 33746458.17099302, 0.165, 0.00415938, 0.0012375, 14061024.23791376, 0.00326155)
    ops.section('Aggregator', 1543991, 1543990, 'Mz')
    ops.section('Aggregator', 1543992, 1543991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1543, 1543991, 0.45828828147, 1543992, 0.45828828147, 1543990)
    # Create element
    ops.element('forceBeamColumn', 1543, 543, 643, 1543, 1543)

    # Create geometric transformation
    ops.geomTransf('Linear', 1643, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1643990, 418.87133196, 0.00825198, 502.59766903, 0.06511861, 50.2597669, 0.25030863, -418.87133196, -0.00825198, -502.59766903, -0.06511861, -50.2597669, -0.25030863, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1643991, 282.56656302, 0.00780308, 339.04754297, 0.0636125, 33.9047543, 0.24880252, -417.90880091, -0.00835108, -501.44274192, -0.06949144, -50.14427419, -0.25468146, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1643990, 34168560.17058229, 0.165, 0.00415938, 0.0012375, 14236900.07107596, 0.00326155)
    ops.section('Aggregator', 1643991, 1643990, 'Mz')
    ops.section('Aggregator', 1643992, 1643991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1643, 1643991, 0.53998589996, 1643992, 0.53998589996, 1643990)
    # Create element
    ops.element('forceBeamColumn', 1643, 643, 743, 1643, 1643)

    # Create geometric transformation
    ops.geomTransf('Linear', 1053, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1053990, 237.76906847, 0.00869725, 286.93258722, 0.06859306, 28.69325872, 0.25883548, -237.76906847, -0.00869725, -286.93258722, -0.06859306, -28.69325872, -0.25883548, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1053991, 352.32031021, 0.00903258, 425.1695933, 0.06819154, 42.51695933, 0.23902879, -464.6125733, -0.00961365, -560.68053163, -0.07272853, -56.06805316, -0.24356577, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1053990, 32659007.12633397, 0.15, 0.003125, 0.001125, 13607919.63597249, 0.00281737)
    ops.section('Aggregator', 1053991, 1053990, 'Mz')
    ops.section('Aggregator', 1053992, 1053991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1053, 1053991, 0.5256451188800001, 1053992, 0.5256451188800001, 1053990)
    # Create element
    ops.element('forceBeamColumn', 1053, 53, 153, 1053, 1053)

    # Create geometric transformation
    ops.geomTransf('Linear', 1153, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1153990, 361.42876181, 0.00914467, 434.58330136, 0.09555226, 43.45833014, 0.31092218, -476.60426527, -0.0097245, -573.07075952, -0.10191009, -57.30707595, -0.31728002, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1153991, 361.14122592, 0.00924734, 434.23756713, 0.10933392, 43.42375671, 0.32470384, -361.14122592, -0.00924734, -434.23756713, -0.10933392, -43.42375671, -0.32470384, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1153990, 33633648.9239043, 0.15, 0.003125, 0.001125, 14014020.38496013, 0.00281737)
    ops.section('Aggregator', 1153991, 1153990, 'Mz')
    ops.section('Aggregator', 1153992, 1153991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1153, 1153991, 0.46431739195, 1153992, 0.46431739195, 1153990)
    # Create element
    ops.element('forceBeamColumn', 1153, 153, 253, 1153, 1153)

    # Create geometric transformation
    ops.geomTransf('Linear', 1253, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1253990, 364.34880994, 0.0091601, 438.65073096, 0.06856705, 43.8650731, 0.25649895, -364.34880994, -0.0091601, -438.65073096, -0.06856705, -43.8650731, -0.25649895, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1253991, 364.34880994, 0.0091601, 438.65073096, 0.06935946, 43.8650731, 0.25729136, -364.34880994, -0.0091601, -438.65073096, -0.06935946, -43.8650731, -0.25729136, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1253990, 33299937.48424854, 0.15, 0.003125, 0.001125, 13874973.95177023, 0.00281737)
    ops.section('Aggregator', 1253991, 1253990, 'Mz')
    ops.section('Aggregator', 1253992, 1253991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1253, 1253991, 0.5321076341100001, 1253992, 0.5321076341100001, 1253990)
    # Create element
    ops.element('forceBeamColumn', 1253, 253, 353, 1253, 1253)

    # Create geometric transformation
    ops.geomTransf('Linear', 1353, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1353990, 361.81453312, 0.00925982, 438.23209553, 0.09895775, 43.82320955, 0.31453425, -361.81453312, -0.00925982, -438.23209553, -0.09895775, -43.82320955, -0.31453425, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1353991, 361.81453312, 0.00925982, 438.23209553, 0.09834264, 43.82320955, 0.31391913, -361.81453312, -0.00925982, -438.23209553, -0.09834264, -43.82320955, -0.31391913, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1353990, 31597859.11967116, 0.15, 0.003125, 0.001125, 13165774.63319632, 0.00281737)
    ops.section('Aggregator', 1353991, 1353990, 'Mz')
    ops.section('Aggregator', 1353992, 1353991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1353, 1353991, 0.46387247247, 1353992, 0.46387247247, 1353990)
    # Create element
    ops.element('forceBeamColumn', 1353, 353, 453, 1353, 1353)

    # Create geometric transformation
    ops.geomTransf('Linear', 1453, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1453990, 358.50471116, 0.00923053, 432.9386662, 0.07203075, 43.29386662, 0.26062655, -358.50471116, -0.00923053, -432.9386662, -0.07203075, -43.29386662, -0.26062655, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1453991, 358.50471116, 0.00923053, 432.9386662, 0.07196048, 43.29386662, 0.26055628, -358.50471116, -0.00923053, -432.9386662, -0.07196048, -43.29386662, -0.26055628, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1453990, 32460833.62902899, 0.15, 0.003125, 0.001125, 13525347.34542875, 0.00281737)
    ops.section('Aggregator', 1453991, 1453990, 'Mz')
    ops.section('Aggregator', 1453992, 1453991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1453, 1453991, 0.530234502, 1453992, 0.530234502, 1453990)
    # Create element
    ops.element('forceBeamColumn', 1453, 453, 553, 1453, 1453)

    # Create geometric transformation
    ops.geomTransf('Linear', 1553, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1553990, 359.79808507, 0.00936403, 432.27243631, 0.09333424, 43.22724363, 0.30801136, -359.79808507, -0.00936403, -432.27243631, -0.09333424, -43.22724363, -0.30801136, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1553991, 359.79808507, 0.00936403, 432.27243631, 0.09309139, 43.22724363, 0.30776851, -359.79808507, -0.00936403, -432.27243631, -0.09309139, -43.22724363, -0.30776851, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1553990, 33842571.49089243, 0.15, 0.003125, 0.001125, 14101071.45453851, 0.00281737)
    ops.section('Aggregator', 1553991, 1553990, 'Mz')
    ops.section('Aggregator', 1553992, 1553991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1553, 1553991, 0.46581582920000003, 1553992, 0.46581582920000003, 1553990)
    # Create element
    ops.element('forceBeamColumn', 1553, 553, 653, 1553, 1553)

    # Create geometric transformation
    ops.geomTransf('Linear', 1653, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1653990, 360.47119083, 0.00907657, 436.25217293, 0.06138012, 43.62521729, 0.23290555, -360.47119083, -0.00907657, -436.25217293, -0.06138012, -43.62521729, -0.23290555, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1653991, 243.13637691, 0.00864508, 294.25034634, 0.05810071, 29.42503463, 0.22867914, -243.13637691, -0.00864508, -294.25034634, -0.05810071, -29.42503463, -0.22867914, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1653990, 31838809.90521385, 0.15, 0.003125, 0.001125, 13266170.7938391, 0.00281737)
    ops.section('Aggregator', 1653991, 1653990, 'Mz')
    ops.section('Aggregator', 1653992, 1653991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1653, 1653991, 0.52811574694, 1653992, 0.52811574694, 1653990)
    # Create element
    ops.element('forceBeamColumn', 1653, 653, 753, 1653, 1653)

    # Create geometric transformation
    ops.geomTransf('Linear', 1004, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1004990, 210.79338924, 0.01045657, 254.44349374, 0.0752363, 25.44434937, 0.26332361, -210.79338924, -0.01045657, -254.44349374, -0.0752363, -25.44434937, -0.26332361, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1004991, 311.65260129, 0.011041, 376.18815748, 0.08028701, 37.61881575, 0.26837433, -311.65260129, -0.011041, -376.18815748, -0.08028701, -37.61881575, -0.26837433, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1004990, 32588420.49967103, 0.1125, 0.00189844, 0.00058594, 13578508.5415296, 0.00152995)
    ops.section('Aggregator', 1004991, 1004990, 'Mz')
    ops.section('Aggregator', 1004992, 1004991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1004, 1004991, 0.53166797189, 1004992, 0.53166797189, 1004990)
    # Create element
    ops.element('forceBeamColumn', 1004, 4, 104, 1004, 1004)

    # Create geometric transformation
    ops.geomTransf('Linear', 1104, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1104990, 312.52474728, 0.01081698, 375.9558861, 0.10708947, 37.59558861, 0.32385986, -312.52474728, -0.01081698, -375.9558861, -0.10708947, -37.59558861, -0.32385986, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1104991, 312.52474728, 0.01081698, 375.9558861, 0.10839389, 37.59558861, 0.32516427, -312.52474728, -0.01081698, -375.9558861, -0.10839389, -37.59558861, -0.32516427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1104990, 33512155.39305948, 0.1125, 0.00189844, 0.00058594, 13963398.08044145, 0.00152995)
    ops.section('Aggregator', 1104991, 1104990, 'Mz')
    ops.section('Aggregator', 1104992, 1104991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1104, 1104991, 0.46131763721, 1104992, 0.46131763721, 1104990)
    # Create element
    ops.element('forceBeamColumn', 1104, 104, 204, 1104, 1104)

    # Create geometric transformation
    ops.geomTransf('Linear', 1204, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1204990, 303.6374231, 0.01085575, 367.29166549, 0.08153022, 36.72916655, 0.27227399, -303.6374231, -0.01085575, -367.29166549, -0.08153022, -36.72916655, -0.27227399, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1204991, 303.6374231, 0.01085575, 367.29166549, 0.08262236, 36.72916655, 0.27336613, -303.6374231, -0.01085575, -367.29166549, -0.08262236, -36.72916655, -0.27336613, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1204990, 31981756.56228222, 0.1125, 0.00189844, 0.00058594, 13325731.90095092, 0.00152995)
    ops.section('Aggregator', 1204991, 1204990, 'Mz')
    ops.section('Aggregator', 1204992, 1204991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1204, 1204991, 0.52426353082, 1204992, 0.52426353082, 1204990)
    # Create element
    ops.element('forceBeamColumn', 1204, 204, 304, 1204, 1204)

    # Create geometric transformation
    ops.geomTransf('Linear', 1304, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1304990, 312.20606731, 0.01076556, 377.31023448, 0.11098095, 37.73102345, 0.32849687, -312.20606731, -0.01076556, -377.31023448, -0.11098095, -37.73102345, -0.32849687, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1304991, 312.20606731, 0.01076556, 377.31023448, 0.1108779, 37.73102345, 0.32839381, -312.20606731, -0.01076556, -377.31023448, -0.1108779, -37.73102345, -0.32839381, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1304990, 32247422.78103225, 0.1125, 0.00189844, 0.00058594, 13436426.15876344, 0.00152995)
    ops.section('Aggregator', 1304991, 1304990, 'Mz')
    ops.section('Aggregator', 1304992, 1304991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1304, 1304991, 0.45973648546, 1304992, 0.45973648546, 1304990)
    # Create element
    ops.element('forceBeamColumn', 1304, 304, 404, 1304, 1304)

    # Create geometric transformation
    ops.geomTransf('Linear', 1404, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1404990, 323.88231165, 0.01085197, 391.891905, 0.08037425, 39.1891905, 0.26727872, -323.88231165, -0.01085197, -391.891905, -0.08037425, -39.1891905, -0.26727872, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1404991, 323.88231165, 0.01085197, 391.891905, 0.08095174, 39.1891905, 0.2678562, -323.88231165, -0.01085197, -391.891905, -0.08095174, -39.1891905, -0.2678562, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1404990, 31898520.40565799, 0.1125, 0.00189844, 0.00058594, 13291050.16902416, 0.00152995)
    ops.section('Aggregator', 1404991, 1404990, 'Mz')
    ops.section('Aggregator', 1404992, 1404991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1404, 1404991, 0.5350327006500001, 1404992, 0.5350327006500001, 1404990)
    # Create element
    ops.element('forceBeamColumn', 1404, 404, 504, 1404, 1404)

    # Create geometric transformation
    ops.geomTransf('Linear', 1504, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1504990, 321.03806265, 0.01063308, 381.71595713, 0.09958835, 38.17159571, 0.31491302, -321.03806265, -0.01063308, -381.71595713, -0.09958835, -38.17159571, -0.31491302, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1504991, 321.03806265, 0.01063308, 381.71595713, 0.10073404, 38.17159571, 0.31605871, -321.03806265, -0.01063308, -381.71595713, -0.10073404, -38.17159571, -0.31605871, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1504990, 36292292.13499263, 0.1125, 0.00189844, 0.00058594, 15121788.38958026, 0.00152995)
    ops.section('Aggregator', 1504991, 1504990, 'Mz')
    ops.section('Aggregator', 1504992, 1504991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1504, 1504991, 0.46441497091000006, 1504992, 0.46441497091000006, 1504990)
    # Create element
    ops.element('forceBeamColumn', 1504, 504, 604, 1504, 1504)

    # Create geometric transformation
    ops.geomTransf('Linear', 1604, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1604990, 318.02049072, 0.01071405, 384.30866726, 0.08129277, 38.43086673, 0.26995039, -318.02049072, -0.01071405, -384.30866726, -0.08129277, -38.43086673, -0.26995039, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1604991, 214.66893181, 0.0101598, 259.41451414, 0.0758155, 25.94145141, 0.26447312, -214.66893181, -0.0101598, -259.41451414, -0.0758155, -25.94145141, -0.26447312, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1604990, 32268646.81888162, 0.1125, 0.00189844, 0.00058594, 13445269.50786734, 0.00152995)
    ops.section('Aggregator', 1604991, 1604990, 'Mz')
    ops.section('Aggregator', 1604992, 1604991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1604, 1604991, 0.53006075308, 1604992, 0.53006075308, 1604990)
    # Create element
    ops.element('forceBeamColumn', 1604, 604, 704, 1604, 1604)

    # Create geometric transformation
    ops.geomTransf('Linear', 1014, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1014990, 245.8579646, 0.00873086, 296.38402531, 0.06690189, 29.63840253, 0.25425705, -363.69821789, -0.00938368, -438.44152859, -0.07311124, -43.84415286, -0.2604664, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1014991, 364.25782701, 0.00926391, 439.11614251, 0.06909902, 43.91161425, 0.25645418, -364.25782701, -0.00926391, -439.11614251, -0.06909902, -43.91161425, -0.25645418, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1014990, 32947041.90511159, 0.15, 0.003125, 0.001125, 13727934.12712983, 0.00281737)
    ops.section('Aggregator', 1014991, 1014990, 'Mz')
    ops.section('Aggregator', 1014992, 1014991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1014, 1014991, 0.5337456463800001, 1014992, 0.5337456463800001, 1014990)
    # Create element
    ops.element('forceBeamColumn', 1014, 14, 114, 1014, 1014)

    # Create geometric transformation
    ops.geomTransf('Linear', 1114, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1114990, 360.90407411, 0.0093302, 436.37340257, 0.09643063, 43.63734026, 0.3115135, -360.90407411, -0.0093302, -436.37340257, -0.09643063, -43.63734026, -0.3115135, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1114991, 360.90407411, 0.0093302, 436.37340257, 0.09759714, 43.63734026, 0.31268001, -360.90407411, -0.0093302, -436.37340257, -0.09759714, -43.63734026, -0.31268001, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1114990, 32108579.36203895, 0.15, 0.003125, 0.001125, 13378574.7341829, 0.00281737)
    ops.section('Aggregator', 1114991, 1114990, 'Mz')
    ops.section('Aggregator', 1114992, 1114991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1114, 1114991, 0.46493707101000004, 1114992, 0.46493707101000004, 1114990)
    # Create element
    ops.element('forceBeamColumn', 1114, 114, 214, 1114, 1114)

    # Create geometric transformation
    ops.geomTransf('Linear', 1214, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1214990, 361.63375467, 0.00926159, 437.56833461, 0.0854952, 43.75683346, 0.27347539, -361.63375467, -0.00926159, -437.56833461, -0.0854952, -43.75683346, -0.27347539, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1214991, 478.24170335, 0.0096197, 578.66120896, 0.09035005, 57.8661209, 0.27833024, -478.24170335, -0.0096197, -578.66120896, -0.09035005, -57.8661209, -0.27833024, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1214990, 31899967.41723426, 0.15, 0.003125, 0.001125, 13291653.09051428, 0.00281737)
    ops.section('Aggregator', 1214991, 1214990, 'Mz')
    ops.section('Aggregator', 1214992, 1214991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1214, 1214991, 0.53197094368, 1214992, 0.53197094368, 1214990)
    # Create element
    ops.element('forceBeamColumn', 1214, 214, 314, 1214, 1214)

    # Create geometric transformation
    ops.geomTransf('Linear', 1314, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1314990, 472.27888662, 0.00938848, 570.63367184, 0.13102575, 57.06336718, 0.34929809, -472.27888662, -0.00938848, -570.63367184, -0.13102575, -57.06336718, -0.34929809, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1314991, 472.27888662, 0.00938848, 570.63367184, 0.13247274, 57.06336718, 0.35074507, -472.27888662, -0.00938848, -570.63367184, -0.13247274, -57.06336718, -0.35074507, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1314990, 32312226.12227696, 0.15, 0.003125, 0.001125, 13463427.55094874, 0.00281737)
    ops.section('Aggregator', 1314991, 1314990, 'Mz')
    ops.section('Aggregator', 1314992, 1314991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1314, 1314991, 0.45814326463, 1314992, 0.45814326463, 1314990)
    # Create element
    ops.element('forceBeamColumn', 1314, 314, 414, 1314, 1314)

    # Create geometric transformation
    ops.geomTransf('Linear', 1414, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1414990, 481.32151012, 0.0095801, 582.78891908, 0.09093171, 58.27889191, 0.27881429, -481.32151012, -0.0095801, -582.78891908, -0.09093171, -58.27889191, -0.27881429, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1414991, 363.84708152, 0.00922497, 440.54970097, 0.08660165, 44.0549701, 0.27448423, -363.84708152, -0.00922497, -440.54970097, -0.08660165, -44.0549701, -0.27448423, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1414990, 31695925.49139202, 0.15, 0.003125, 0.001125, 13206635.62141334, 0.00281737)
    ops.section('Aggregator', 1414991, 1414990, 'Mz')
    ops.section('Aggregator', 1414992, 1414991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1414, 1414991, 0.53224731351, 1414992, 0.53224731351, 1414990)
    # Create element
    ops.element('forceBeamColumn', 1414, 414, 514, 1414, 1414)

    # Create geometric transformation
    ops.geomTransf('Linear', 1514, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1514990, 361.00442132, 0.00925396, 434.04699133, 0.09526312, 43.40469913, 0.31060553, -361.00442132, -0.00925396, -434.04699133, -0.09526312, -43.40469913, -0.31060553, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1514991, 361.00442132, 0.00925396, 434.04699133, 0.09395347, 43.40469913, 0.30929588, -361.00442132, -0.00925396, -434.04699133, -0.09395347, -43.40469913, -0.30929588, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1514990, 33649257.97785749, 0.15, 0.003125, 0.001125, 14020524.15744062, 0.00281737)
    ops.section('Aggregator', 1514991, 1514990, 'Mz')
    ops.section('Aggregator', 1514992, 1514991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1514, 1514991, 0.46437670874000003, 1514992, 0.46437670874000003, 1514990)
    # Create element
    ops.element('forceBeamColumn', 1514, 514, 614, 1514, 1514)

    # Create geometric transformation
    ops.geomTransf('Linear', 1614, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1614990, 361.59192979, 0.0092524, 433.54508974, 0.06868463, 43.35450897, 0.25632174, -361.59192979, -0.0092524, -433.54508974, -0.06868463, -43.35450897, -0.25632174, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1614991, 244.07403239, 0.00872983, 292.64231183, 0.06583184, 29.26423118, 0.25346895, -361.22134571, -0.00936365, -433.10076314, -0.07192008, -43.31007631, -0.25955719, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1614990, 34354441.07296239, 0.15, 0.003125, 0.001125, 14314350.44706766, 0.00281737)
    ops.section('Aggregator', 1614991, 1614990, 'Mz')
    ops.section('Aggregator', 1614992, 1614991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1614, 1614991, 0.53294362519, 1614992, 0.53294362519, 1614990)
    # Create element
    ops.element('forceBeamColumn', 1614, 614, 714, 1614, 1614)

    # Create geometric transformation
    ops.geomTransf('Linear', 1024, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1024990, 240.50054183, 0.00888805, 288.03346194, 0.05938597, 28.80334619, 0.24827962, -240.50054183, -0.00888805, -288.03346194, -0.05938597, -28.80334619, -0.24827962, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1024991, 240.50054183, 0.00888805, 288.03346194, 0.05982783, 28.80334619, 0.24872148, -240.50054183, -0.00888805, -288.03346194, -0.05982783, -28.80334619, -0.24872148, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1024990, 34630181.64041931, 0.125, 0.00260417, 0.00065104, 14429242.35017471, 0.00178813)
    ops.section('Aggregator', 1024991, 1024990, 'Mz')
    ops.section('Aggregator', 1024992, 1024991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1024, 1024991, 0.52939841524, 1024992, 0.52939841524, 1024990)
    # Create element
    ops.element('forceBeamColumn', 1024, 24, 124, 1024, 1024)

    # Create geometric transformation
    ops.geomTransf('Linear', 1124, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1124990, 248.35289449, 0.00900808, 297.45564731, 0.07793203, 29.74556473, 0.29112529, -248.35289449, -0.00900808, -297.45564731, -0.07793203, -29.74556473, -0.29112529, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1124991, 248.54466813, 0.00889399, 297.6853372, 0.0739454, 29.76853372, 0.28713866, -367.30573837, -0.00961612, -439.92709, -0.08088127, -43.992709, -0.29407453, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1124990, 34615578.87775043, 0.125, 0.00260417, 0.00065104, 14423157.86572935, 0.00178813)
    ops.section('Aggregator', 1124991, 1124990, 'Mz')
    ops.section('Aggregator', 1124992, 1124991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1124, 1124991, 0.46905798195000004, 1124992, 0.46905798195000004, 1124990)
    # Create element
    ops.element('forceBeamColumn', 1124, 124, 224, 1124, 1124)

    # Create geometric transformation
    ops.geomTransf('Linear', 1224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1224990, 239.65549987, 0.00900394, 288.45418712, 0.07466256, 28.84541871, 0.26250605, -354.43204862, -0.00974017, -426.60155318, -0.08167053, -42.66015532, -0.26951403, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1224991, 354.86855342, 0.00959729, 427.12693915, 0.07646385, 42.71269392, 0.26430734, -354.86855342, -0.00959729, -427.12693915, -0.07646385, -42.71269392, -0.26430734, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1224990, 33368413.56798939, 0.125, 0.00260417, 0.00065104, 13903505.65332891, 0.00178813)
    ops.section('Aggregator', 1224991, 1224990, 'Mz')
    ops.section('Aggregator', 1224992, 1224991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1224, 1224991, 0.53235807521, 1224992, 0.53235807521, 1224990)
    # Create element
    ops.element('forceBeamColumn', 1224, 224, 324, 1224, 1224)

    # Create geometric transformation
    ops.geomTransf('Linear', 1324, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1324990, 355.98703697, 0.00933169, 428.36274199, 0.10601931, 42.8362742, 0.32323734, -355.98703697, -0.00933169, -428.36274199, -0.10601931, -42.8362742, -0.32323734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1324991, 355.98703697, 0.00933169, 428.36274199, 0.10627382, 42.8362742, 0.32349185, -355.98703697, -0.00933169, -428.36274199, -0.10627382, -42.8362742, -0.32349185, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1324990, 33436494.44893077, 0.125, 0.00260417, 0.00065104, 13931872.68705449, 0.00178813)
    ops.section('Aggregator', 1324991, 1324990, 'Mz')
    ops.section('Aggregator', 1324992, 1324991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1324, 1324991, 0.4603669407, 1324992, 0.4603669407, 1324990)
    # Create element
    ops.element('forceBeamColumn', 1324, 324, 424, 1324, 1324)

    # Create geometric transformation
    ops.geomTransf('Linear', 1424, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1424990, 353.72926675, 0.00933952, 424.78346599, 0.07550488, 42.4783466, 0.2650065, -353.72926675, -0.00933952, -424.78346599, -0.07550488, -42.4783466, -0.2650065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1424991, 238.83074137, 0.00876606, 286.80507846, 0.07353314, 28.68050785, 0.26303476, -353.0991112, -0.00948043, -424.02673002, -0.08043411, -42.402673, -0.26993573, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1424990, 33961293.10558241, 0.125, 0.00260417, 0.00065104, 14150538.79399267, 0.00178813)
    ops.section('Aggregator', 1424991, 1424990, 'Mz')
    ops.section('Aggregator', 1424992, 1424991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1424, 1424991, 0.52769998238, 1424992, 0.52769998238, 1424990)
    # Create element
    ops.element('forceBeamColumn', 1424, 424, 524, 1424, 1424)

    # Create geometric transformation
    ops.geomTransf('Linear', 1524, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1524990, 237.83127762, 0.008708, 285.91904692, 0.07079119, 28.59190469, 0.28920755, -351.57728766, -0.00942205, -422.66367994, -0.07743545, -42.26636799, -0.29585182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1524991, 237.75870414, 0.0088187, 285.8317996, 0.07371244, 28.58317996, 0.29212881, -237.75870414, -0.0088187, -285.8317996, -0.07371244, -28.58317996, -0.29212881, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1524990, 33679184.46057869, 0.125, 0.00260417, 0.00065104, 14032993.52524112, 0.00178813)
    ops.section('Aggregator', 1524991, 1524990, 'Mz')
    ops.section('Aggregator', 1524992, 1524991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1524, 1524991, 0.45784115012000004, 1524992, 0.45784115012000004, 1524990)
    # Create element
    ops.element('forceBeamColumn', 1524, 524, 624, 1524, 1524)

    # Create geometric transformation
    ops.geomTransf('Linear', 1624, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1624990, 240.41048762, 0.00900512, 290.37129448, 0.06128471, 29.03712945, 0.24977897, -240.41048762, -0.00900512, -290.37129448, -0.06128471, -29.03712945, -0.24977897, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1624991, 240.41048762, 0.00900512, 290.37129448, 0.06159266, 29.03712945, 0.25008692, -240.41048762, -0.00900512, -290.37129448, -0.06159266, -29.03712945, -0.25008692, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1624990, 32416055.02890305, 0.125, 0.00260417, 0.00065104, 13506689.59537627, 0.00178813)
    ops.section('Aggregator', 1624991, 1624990, 'Mz')
    ops.section('Aggregator', 1624992, 1624991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1624, 1624991, 0.53052012777, 1624992, 0.53052012777, 1624990)
    # Create element
    ops.element('forceBeamColumn', 1624, 624, 724, 1624, 1624)

    # Create geometric transformation
    ops.geomTransf('Linear', 1034, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1034990, 237.92332061, 0.00921027, 288.66819514, 0.07613639, 28.86681951, 0.26419133, -237.92332061, -0.00921027, -288.66819514, -0.07613639, -28.86681951, -0.26419133, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1034991, 237.84212527, 0.00909153, 288.56968226, 0.07250783, 28.85696823, 0.26056277, -351.6723458, -0.00986531, -426.67789388, -0.07933918, -42.66778939, -0.26739412, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1034990, 31072831.11960534, 0.125, 0.00260417, 0.00065104, 12947012.96650223, 0.00178813)
    ops.section('Aggregator', 1034991, 1034990, 'Mz')
    ops.section('Aggregator', 1034992, 1034991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1034, 1034991, 0.53175949737, 1034992, 0.53175949737, 1034990)
    # Create element
    ops.element('forceBeamColumn', 1034, 34, 134, 1034, 1034)

    # Create geometric transformation
    ops.geomTransf('Linear', 1134, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1134990, 242.66736302, 0.008894, 292.05546801, 0.09929032, 29.2055468, 0.3145638, -358.70733391, -0.0096271, -431.71210575, -0.10865812, -43.17121057, -0.3239316, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1134991, 242.66736302, 0.008894, 292.05546801, 0.1009157, 29.2055468, 0.31618918, -358.70733391, -0.0096271, -431.71210575, -0.11043875, -43.17121057, -0.32571223, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1134990, 33390024.84696152, 0.125, 0.00260417, 0.00065104, 13912510.35290063, 0.00178813)
    ops.section('Aggregator', 1134991, 1134990, 'Mz')
    ops.section('Aggregator', 1134992, 1134991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1134, 1134991, 0.46452540587, 1134992, 0.46452540587, 1134990)
    # Create element
    ops.element('forceBeamColumn', 1134, 134, 234, 1134, 1134)

    # Create geometric transformation
    ops.geomTransf('Linear', 1234, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1234990, 245.28697086, 0.00870958, 295.60329889, 0.07481761, 29.56032989, 0.26321674, -362.2468919, -0.00943998, -436.55550021, -0.08186269, -43.65555002, -0.27026182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1234991, 363.36217958, 0.00928723, 437.89956963, 0.07730268, 43.78995696, 0.26570181, -363.36217958, -0.00928723, -437.89956963, -0.07730268, -43.78995696, -0.26570181, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1234990, 33032011.64751701, 0.125, 0.00260417, 0.00065104, 13763338.18646542, 0.00178813)
    ops.section('Aggregator', 1234991, 1234990, 'Mz')
    ops.section('Aggregator', 1234992, 1234991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1234, 1234991, 0.53078801157, 1234992, 0.53078801157, 1234990)
    # Create element
    ops.element('forceBeamColumn', 1234, 234, 334, 1234, 1234)

    # Create geometric transformation
    ops.geomTransf('Linear', 1334, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1334990, 360.69190873, 0.00940073, 434.63642104, 0.10421209, 43.4636421, 0.31992913, -360.69190873, -0.00940073, -434.63642104, -0.10421209, -43.4636421, -0.31992913, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1334991, 360.69190873, 0.00940073, 434.63642104, 0.10524484, 43.4636421, 0.32096188, -360.69190873, -0.00940073, -434.63642104, -0.10524484, -43.4636421, -0.32096188, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1334990, 33060123.86109239, 0.125, 0.00260417, 0.00065104, 13775051.6087885, 0.00178813)
    ops.section('Aggregator', 1334991, 1334990, 'Mz')
    ops.section('Aggregator', 1334992, 1334991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1334, 1334991, 0.46357023941000003, 1334992, 0.46357023941000003, 1334990)
    # Create element
    ops.element('forceBeamColumn', 1334, 334, 434, 1334, 1334)

    # Create geometric transformation
    ops.geomTransf('Linear', 1434, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1434990, 354.31448519, 0.0094936, 424.86546176, 0.0752274, 42.48654618, 0.26362451, -354.31448519, -0.0094936, -424.86546176, -0.0752274, -42.48654618, -0.26362451, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1434991, 239.26192621, 0.00891362, 286.90367741, 0.0718598, 28.69036774, 0.26025691, -353.8714754, -0.00963136, -424.33424001, -0.07859018, -42.433424, -0.26698729, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1434990, 34327659.13157528, 0.125, 0.00260417, 0.00065104, 14303191.30482303, 0.00178813)
    ops.section('Aggregator', 1434991, 1434990, 'Mz')
    ops.section('Aggregator', 1434992, 1434991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1434, 1434991, 0.53079370775, 1434992, 0.53079370775, 1434990)
    # Create element
    ops.element('forceBeamColumn', 1434, 434, 534, 1434, 1434)

    # Create geometric transformation
    ops.geomTransf('Linear', 1534, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1534990, 245.37805967, 0.00881515, 294.81932221, 0.10051006, 29.48193222, 0.31550752, -362.582717, -0.00954049, -435.63956376, -0.10999416, -43.56395638, -0.32499162, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1534991, 245.37805967, 0.00881515, 294.81932221, 0.10031946, 29.48193222, 0.31531692, -362.582717, -0.00954049, -435.63956376, -0.10978535, -43.56395638, -0.32478281, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1534990, 33829871.94072932, 0.125, 0.00260417, 0.00065104, 14095779.97530388, 0.00178813)
    ops.section('Aggregator', 1534991, 1534990, 'Mz')
    ops.section('Aggregator', 1534992, 1534991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1534, 1534991, 0.46512177724, 1534992, 0.46512177724, 1534990)
    # Create element
    ops.element('forceBeamColumn', 1534, 534, 634, 1534, 1534)

    # Create geometric transformation
    ops.geomTransf('Linear', 1634, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1634990, 242.23801208, 0.0088184, 292.23582836, 0.06336812, 29.22358284, 0.25183297, -357.95165473, -0.00955606, -431.83271458, -0.06931639, -43.18327146, -0.25778124, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1634991, 242.07608199, 0.00893665, 292.04047597, 0.06639577, 29.2040476, 0.25486062, -242.07608199, -0.00893665, -292.04047597, -0.06639577, -29.2040476, -0.25486062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1634990, 32744223.47874217, 0.125, 0.00260417, 0.00065104, 13643426.4494759, 0.00178813)
    ops.section('Aggregator', 1634991, 1634990, 'Mz')
    ops.section('Aggregator', 1634992, 1634991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1634, 1634991, 0.53060292146, 1634992, 0.53060292146, 1634990)
    # Create element
    ops.element('forceBeamColumn', 1634, 634, 734, 1634, 1634)

    # Create geometric transformation
    ops.geomTransf('Linear', 1044, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1044990, 243.09924883, 0.00859099, 293.99979471, 0.06928628, 29.39997947, 0.25835763, -359.4958628, -0.00924598, -434.76773528, -0.07573892, -43.47677353, -0.26481028, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1044991, 360.1794457, 0.00912239, 435.59444796, 0.07167683, 43.5594448, 0.26074818, -360.1794457, -0.00912239, -435.59444796, -0.07167683, -43.5594448, -0.26074818, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1044990, 32043787.79870098, 0.15, 0.003125, 0.001125, 13351578.24945874, 0.00281737)
    ops.section('Aggregator', 1044991, 1044990, 'Mz')
    ops.section('Aggregator', 1044992, 1044991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1044, 1044991, 0.5289008565300001, 1044992, 0.5289008565300001, 1044990)
    # Create element
    ops.element('forceBeamColumn', 1044, 44, 144, 1044, 1044)

    # Create geometric transformation
    ops.geomTransf('Linear', 1144, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1144990, 362.01476375, 0.00921536, 433.9633, 0.09132881, 43.39633, 0.30660873, -362.01476375, -0.00921536, -433.9633, -0.09132881, -43.39633, -0.30660873, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1144991, 362.01476375, 0.00921536, 433.9633, 0.09145441, 43.39633, 0.30673432, -362.01476375, -0.00921536, -433.9633, -0.09145441, -43.39633, -0.30673432, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1144990, 34404946.07327066, 0.15, 0.003125, 0.001125, 14335394.19719611, 0.00281737)
    ops.section('Aggregator', 1144991, 1144990, 'Mz')
    ops.section('Aggregator', 1144992, 1144991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1144, 1144991, 0.46451151879999997, 1144992, 0.46451151879999997, 1144990)
    # Create element
    ops.element('forceBeamColumn', 1144, 144, 244, 1144, 1144)

    # Create geometric transformation
    ops.geomTransf('Linear', 1244, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1244990, 357.3334239, 0.00905922, 430.06877551, 0.08462568, 43.00687755, 0.274344, -357.3334239, -0.00905922, -430.06877551, -0.08462568, -43.00687755, -0.274344, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1244991, 472.54894573, 0.0094054, 568.73645975, 0.0890076, 56.87364598, 0.27872592, -472.54894573, -0.0094054, -568.73645975, -0.0890076, -56.87364598, -0.27872592, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1244990, 33383753.24677617, 0.15, 0.003125, 0.001125, 13909897.18615674, 0.00281737)
    ops.section('Aggregator', 1244991, 1244990, 'Mz')
    ops.section('Aggregator', 1244992, 1244991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1244, 1244991, 0.5270972270300001, 1244992, 0.5270972270300001, 1244990)
    # Create element
    ops.element('forceBeamColumn', 1244, 244, 344, 1244, 1244)

    # Create geometric transformation
    ops.geomTransf('Linear', 1344, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1344990, 472.17323676, 0.00940679, 567.84088872, 0.12876149, 56.78408887, 0.34658097, -472.17323676, -0.00940679, -567.84088872, -0.12876149, -56.78408887, -0.34658097, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1344991, 472.17323676, 0.00940679, 567.84088872, 0.12805613, 56.78408887, 0.34587561, -472.17323676, -0.00940679, -567.84088872, -0.12805613, -56.78408887, -0.34587561, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1344990, 33588711.4806549, 0.15, 0.003125, 0.001125, 13995296.45027287, 0.00281737)
    ops.section('Aggregator', 1344991, 1344990, 'Mz')
    ops.section('Aggregator', 1344992, 1344991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1344, 1344991, 0.45909576026000004, 1344992, 0.45909576026000004, 1344990)
    # Create element
    ops.element('forceBeamColumn', 1344, 344, 444, 1344, 1344)

    # Create geometric transformation
    ops.geomTransf('Linear', 1444, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1444990, 479.53453115, 0.00948739, 572.64761633, 0.08523432, 57.26476163, 0.27323129, -479.53453115, -0.00948739, -572.64761633, -0.08523432, -57.26476163, -0.27323129, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1444991, 362.68407374, 0.00914207, 433.10785108, 0.08042306, 43.31078511, 0.26842003, -362.68407374, -0.00914207, -433.10785108, -0.08042306, -43.31078511, -0.26842003, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1444990, 35318126.65915621, 0.15, 0.003125, 0.001125, 14715886.10798175, 0.00281737)
    ops.section('Aggregator', 1444991, 1444990, 'Mz')
    ops.section('Aggregator', 1444992, 1444991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1444, 1444991, 0.5319234671699999, 1444992, 0.5319234671699999, 1444990)
    # Create element
    ops.element('forceBeamColumn', 1444, 444, 544, 1444, 1444)

    # Create geometric transformation
    ops.geomTransf('Linear', 1544, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1544990, 356.94264981, 0.00936897, 431.18256831, 0.09678612, 43.11825683, 0.31236714, -356.94264981, -0.00936897, -431.18256831, -0.09678612, -43.11825683, -0.31236714, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1544991, 356.94264981, 0.00936897, 431.18256831, 0.09629438, 43.11825683, 0.3118754, -356.94264981, -0.00936897, -431.18256831, -0.09629438, -43.11825683, -0.3118754, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1544990, 32375242.57974003, 0.15, 0.003125, 0.001125, 13489684.40822501, 0.00281737)
    ops.section('Aggregator', 1544991, 1544990, 'Mz')
    ops.section('Aggregator', 1544992, 1544991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1544, 1544991, 0.46386272795000005, 1544992, 0.46386272795000005, 1544990)
    # Create element
    ops.element('forceBeamColumn', 1544, 544, 644, 1544, 1544)

    # Create geometric transformation
    ops.geomTransf('Linear', 1644, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1644990, 357.96930798, 0.00923527, 432.09682818, 0.07064835, 43.20968282, 0.25928259, -357.96930798, -0.00923527, -432.09682818, -0.07064835, -43.20968282, -0.25928259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1644991, 241.64683399, 0.00870155, 291.68654458, 0.06878327, 29.16865446, 0.2574175, -357.53190856, -0.00935355, -431.56885302, -0.07517432, -43.1568853, -0.26380855, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1644990, 32587826.05532669, 0.15, 0.003125, 0.001125, 13578260.85638612, 0.00281737)
    ops.section('Aggregator', 1644991, 1644990, 'Mz')
    ops.section('Aggregator', 1644992, 1644991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1644, 1644991, 0.5301264727, 1644992, 0.5301264727, 1644990)
    # Create element
    ops.element('forceBeamColumn', 1644, 644, 744, 1644, 1644)

    # Create geometric transformation
    ops.geomTransf('Linear', 1054, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1054990, 206.73921411, 0.01027202, 249.79205451, 0.07587777, 24.97920545, 0.26620016, -206.73921411, -0.01027202, -249.79205451, -0.07587777, -24.97920545, -0.26620016, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1054991, 305.66058321, 0.01084737, 369.31351119, 0.08172773, 36.93135112, 0.27205012, -305.66058321, -0.01084737, -369.31351119, -0.08172773, -36.93135112, -0.27205012, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1054990, 32314266.47782638, 0.1125, 0.00189844, 0.00058594, 13464277.69909433, 0.00152995)
    ops.section('Aggregator', 1054991, 1054990, 'Mz')
    ops.section('Aggregator', 1054992, 1054991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1054, 1054991, 0.5254242692300001, 1054992, 0.5254242692300001, 1054990)
    # Create element
    ops.element('forceBeamColumn', 1054, 54, 154, 1054, 1054)

    # Create geometric transformation
    ops.geomTransf('Linear', 1154, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1154990, 312.80339765, 0.01073228, 375.56774776, 0.10608947, 37.55677478, 0.32326767, -312.80339765, -0.01073228, -375.56774776, -0.10608947, -37.55677478, -0.32326767, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1154991, 312.80339765, 0.01073228, 375.56774776, 0.10589128, 37.55677478, 0.32306948, -312.80339765, -0.01073228, -375.56774776, -0.10589128, -37.55677478, -0.32306948, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1154990, 34007898.18383702, 0.1125, 0.00189844, 0.00058594, 14169957.57659876, 0.00152995)
    ops.section('Aggregator', 1154991, 1154990, 'Mz')
    ops.section('Aggregator', 1154992, 1154991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1154, 1154991, 0.46045136974, 1154992, 0.46045136974, 1154990)
    # Create element
    ops.element('forceBeamColumn', 1154, 154, 254, 1154, 1154)

    # Create geometric transformation
    ops.geomTransf('Linear', 1254, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1254990, 317.7518445, 0.01067494, 379.72283685, 0.07688708, 37.97228368, 0.26528827, -317.7518445, -0.01067494, -379.72283685, -0.07688708, -37.97228368, -0.26528827, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1254991, 317.7518445, 0.01067494, 379.72283685, 0.07639821, 37.97228368, 0.26479941, -317.7518445, -0.01067494, -379.72283685, -0.07639821, -37.97228368, -0.26479941, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1254990, 35151104.90801687, 0.1125, 0.00189844, 0.00058594, 14646293.7116737, 0.00152995)
    ops.section('Aggregator', 1254991, 1254990, 'Mz')
    ops.section('Aggregator', 1254992, 1254991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1254, 1254991, 0.53078219806, 1254992, 0.53078219806, 1254990)
    # Create element
    ops.element('forceBeamColumn', 1254, 254, 354, 1254, 1254)

    # Create geometric transformation
    ops.geomTransf('Linear', 1354, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1354990, 308.90094891, 0.0106904, 371.94704597, 0.10937733, 37.1947046, 0.32802387, -308.90094891, -0.0106904, -371.94704597, -0.10937733, -37.1947046, -0.32802387, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1354991, 308.90094891, 0.0106904, 371.94704597, 0.10903691, 37.1947046, 0.32768345, -308.90094891, -0.0106904, -371.94704597, -0.10903691, -37.1947046, -0.32768345, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1354990, 33262909.44749759, 0.1125, 0.00189844, 0.00058594, 13859545.60312399, 0.00152995)
    ops.section('Aggregator', 1354991, 1354990, 'Mz')
    ops.section('Aggregator', 1354992, 1354991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1354, 1354991, 0.45735916985, 1354992, 0.45735916985, 1354990)
    # Create element
    ops.element('forceBeamColumn', 1354, 354, 454, 1354, 1354)

    # Create geometric transformation
    ops.geomTransf('Linear', 1454, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1454990, 317.82923102, 0.0107066, 381.87397349, 0.07917591, 38.18739735, 0.26762161, -317.82923102, -0.0107066, -381.87397349, -0.07917591, -38.18739735, -0.26762161, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1454991, 317.82923102, 0.0107066, 381.87397349, 0.07872035, 38.18739735, 0.26716605, -317.82923102, -0.0107066, -381.87397349, -0.07872035, -38.18739735, -0.26716605, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1454990, 33826324.60028463, 0.1125, 0.00189844, 0.00058594, 14094301.91678526, 0.00152995)
    ops.section('Aggregator', 1454991, 1454990, 'Mz')
    ops.section('Aggregator', 1454992, 1454991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1454, 1454991, 0.53065684184, 1454992, 0.53065684184, 1454990)
    # Create element
    ops.element('forceBeamColumn', 1454, 454, 554, 1454, 1454)

    # Create geometric transformation
    ops.geomTransf('Linear', 1554, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1554990, 319.40690497, 0.01059754, 378.51081822, 0.09923859, 37.85108182, 0.31506778, -319.40690497, -0.01059754, -378.51081822, -0.09923859, -37.85108182, -0.31506778, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1554991, 319.40690497, 0.01059754, 378.51081822, 0.09804142, 37.85108182, 0.31387061, -319.40690497, -0.01059754, -378.51081822, -0.09804142, -37.85108182, -0.31387061, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1554990, 37002474.26519019, 0.1125, 0.00189844, 0.00058594, 15417697.61049591, 0.00152995)
    ops.section('Aggregator', 1554991, 1554990, 'Mz')
    ops.section('Aggregator', 1554992, 1554991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1554, 1554991, 0.46332935942000003, 1554992, 0.46332935942000003, 1554990)
    # Create element
    ops.element('forceBeamColumn', 1554, 554, 654, 1554, 1554)

    # Create geometric transformation
    ops.geomTransf('Linear', 1654, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1654990, 316.45528609, 0.0108488, 377.85560752, 0.07546163, 37.78556075, 0.26315082, -316.45528609, -0.0108488, -377.85560752, -0.07546163, -37.78556075, -0.26315082, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1654991, 213.91638395, 0.01029053, 255.4215675, 0.07019005, 25.54215675, 0.25787923, -213.91638395, -0.01029053, -255.4215675, -0.07019005, -25.54215675, -0.25787923, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1654990, 35346962.89968122, 0.1125, 0.00189844, 0.00058594, 14727901.20820051, 0.00152995)
    ops.section('Aggregator', 1654991, 1654990, 'Mz')
    ops.section('Aggregator', 1654992, 1654991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1654, 1654991, 0.5327957465700001, 1654992, 0.5327957465700001, 1654990)
    # Create element
    ops.element('forceBeamColumn', 1654, 654, 754, 1654, 1654)

    # Create geometric transformation
    ops.geomTransf('Linear', 1005, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1005990, 213.40000157, 0.01027726, 255.69676435, 0.07281115, 25.56967644, 0.26083586, -213.40000157, -0.01027726, -255.69676435, -0.07281115, -25.56967644, -0.26083586, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1005991, 315.73835944, 0.01083734, 378.31900795, 0.07779759, 37.83190079, 0.2658223, -315.73835944, -0.01083734, -378.31900795, -0.07779759, -37.83190079, -0.2658223, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1005990, 34515732.82833986, 0.1125, 0.00189844, 0.00058594, 14381555.34514161, 0.00152995)
    ops.section('Aggregator', 1005991, 1005990, 'Mz')
    ops.section('Aggregator', 1005992, 1005991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1005, 1005991, 0.5318450007200001, 1005992, 0.5318450007200001, 1005990)
    # Create element
    ops.element('forceBeamColumn', 1005, 5, 105, 1005, 1005)

    # Create geometric transformation
    ops.geomTransf('Linear', 1105, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1105990, 318.0229053, 0.01070992, 380.85074269, 0.10519865, 38.08507427, 0.32108114, -318.0229053, -0.01070992, -380.85074269, -0.10519865, -38.08507427, -0.32108114, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1105991, 318.0229053, 0.01070992, 380.85074269, 0.10423598, 38.08507427, 0.32011847, -318.0229053, -0.01070992, -380.85074269, -0.10423598, -38.08507427, -0.32011847, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1105990, 34647211.47405041, 0.1125, 0.00189844, 0.00058594, 14436338.11418767, 0.00152995)
    ops.section('Aggregator', 1105991, 1105990, 'Mz')
    ops.section('Aggregator', 1105992, 1105991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1105, 1105991, 0.46321496253, 1105992, 0.46321496253, 1105990)
    # Create element
    ops.element('forceBeamColumn', 1105, 105, 205, 1105, 1105)

    # Create geometric transformation
    ops.geomTransf('Linear', 1205, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1205990, 319.73823179, 0.010808, 385.76534671, 0.07916063, 38.57653467, 0.2669073, -319.73823179, -0.010808, -385.76534671, -0.07916063, -38.57653467, -0.2669073, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1205991, 319.73823179, 0.010808, 385.76534671, 0.0791509, 38.57653467, 0.26689757, -319.73823179, -0.010808, -385.76534671, -0.0791509, -38.57653467, -0.26689757, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1205990, 32720326.37117116, 0.1125, 0.00189844, 0.00058594, 13633469.32132132, 0.00152995)
    ops.section('Aggregator', 1205991, 1205990, 'Mz')
    ops.section('Aggregator', 1205992, 1205991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1205, 1205991, 0.5326326140600001, 1205992, 0.5326326140600001, 1205990)
    # Create element
    ops.element('forceBeamColumn', 1205, 205, 305, 1205, 1205)

    # Create geometric transformation
    ops.geomTransf('Linear', 1305, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1305990, 314.67014199, 0.01130249, 380.70434637, 0.1095323, 38.07043464, 0.32285552, -314.67014199, -0.01130249, -380.70434637, -0.1095323, -38.07043464, -0.32285552, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1305991, 314.67014199, 0.01130249, 380.70434637, 0.11018829, 38.07043464, 0.32351151, -314.67014199, -0.01130249, -380.70434637, -0.11018829, -38.07043464, -0.32351151, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1305990, 31930152.2572084, 0.1125, 0.00189844, 0.00058594, 13304230.10717016, 0.00152995)
    ops.section('Aggregator', 1305991, 1305990, 'Mz')
    ops.section('Aggregator', 1305992, 1305991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1305, 1305991, 0.46877222134, 1305992, 0.46877222134, 1305990)
    # Create element
    ops.element('forceBeamColumn', 1305, 305, 405, 1305, 1305)

    # Create geometric transformation
    ops.geomTransf('Linear', 1405, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1405990, 312.2170701, 0.01089092, 376.64881111, 0.08121939, 37.66488111, 0.26994803, -312.2170701, -0.01089092, -376.64881111, -0.08121939, -37.66488111, -0.26994803, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1405991, 312.2170701, 0.01089092, 376.64881111, 0.08036897, 37.66488111, 0.26909761, -312.2170701, -0.01089092, -376.64881111, -0.08036897, -37.66488111, -0.26909761, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1405990, 32751362.8064764, 0.1125, 0.00189844, 0.00058594, 13646401.16936517, 0.00152995)
    ops.section('Aggregator', 1405991, 1405990, 'Mz')
    ops.section('Aggregator', 1405992, 1405991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1405, 1405991, 0.52986128566, 1405992, 0.52986128566, 1405990)
    # Create element
    ops.element('forceBeamColumn', 1405, 405, 505, 1405, 1405)

    # Create geometric transformation
    ops.geomTransf('Linear', 1505, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1505990, 312.78115553, 0.01059666, 375.43513888, 0.10894222, 37.54351389, 0.32707394, -312.78115553, -0.01059666, -375.43513888, -0.10894222, -37.54351389, -0.32707394, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1505991, 312.78115553, 0.01059666, 375.43513888, 0.10737077, 37.54351389, 0.32550248, -312.78115553, -0.01059666, -375.43513888, -0.10737077, -37.54351389, -0.32550248, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1505990, 34079162.24772188, 0.1125, 0.00189844, 0.00058594, 14199650.93655078, 0.00152995)
    ops.section('Aggregator', 1505991, 1505990, 'Mz')
    ops.section('Aggregator', 1505992, 1505991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1505, 1505991, 0.45843860975, 1505992, 0.45843860975, 1505990)
    # Create element
    ops.element('forceBeamColumn', 1505, 505, 605, 1505, 1505)

    # Create geometric transformation
    ops.geomTransf('Linear', 1605, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1605990, 307.05549327, 0.01087668, 369.59723233, 0.07902083, 36.95972323, 0.26872631, -307.05549327, -0.01087668, -369.59723233, -0.07902083, -36.95972323, -0.26872631, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1605991, 207.7246855, 0.01030292, 250.03450689, 0.07435941, 25.00345069, 0.26406489, -207.7246855, -0.01030292, -250.03450689, -0.07435941, -25.00345069, -0.26406489, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1605990, 33354756.32291915, 0.1125, 0.00189844, 0.00058594, 13897815.13454964, 0.00152995)
    ops.section('Aggregator', 1605991, 1605990, 'Mz')
    ops.section('Aggregator', 1605992, 1605991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1605, 1605991, 0.52713289733, 1605992, 0.52713289733, 1605990)
    # Create element
    ops.element('forceBeamColumn', 1605, 605, 705, 1605, 1605)

    # Create geometric transformation
    ops.geomTransf('Linear', 1015, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1015990, 210.90285236, 0.01038425, 254.66849123, 0.07593814, 25.46684912, 0.26439826, -210.90285236, -0.01038425, -254.66849123, -0.07593814, -25.46684912, -0.26439826, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1015991, 210.74648873, 0.01024659, 254.47967971, 0.07817568, 25.44796797, 0.26663581, -311.63402589, -0.01114454, -376.30295799, -0.08556225, -37.6302958, -0.27402238, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1015990, 32486001.31897964, 0.1125, 0.00189844, 0.00058594, 13535833.88290819, 0.00152995)
    ops.section('Aggregator', 1015991, 1015990, 'Mz')
    ops.section('Aggregator', 1015992, 1015991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1015, 1015991, 0.53061621229, 1015992, 0.53061621229, 1015990)
    # Create element
    ops.element('forceBeamColumn', 1015, 15, 115, 1015, 1015)

    # Create geometric transformation
    ops.geomTransf('Linear', 1115, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1115990, 212.41071331, 0.01044782, 255.52555034, 0.0852567, 25.55255503, 0.29919294, -314.20738181, -0.01134153, -377.98476784, -0.0932962, -37.79847678, -0.30723244, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1115991, 212.41071331, 0.01044782, 255.52555034, 0.08484812, 25.55255503, 0.29878437, -314.20738181, -0.01134153, -377.98476784, -0.09284859, -37.79847678, -0.30678484, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1115990, 33508872.3512964, 0.1125, 0.00189844, 0.00058594, 13962030.1463735, 0.00152995)
    ops.section('Aggregator', 1115991, 1115990, 'Mz')
    ops.section('Aggregator', 1115992, 1115991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1115, 1115991, 0.46742897718000004, 1115992, 0.46742897718000004, 1115990)
    # Create element
    ops.element('forceBeamColumn', 1115, 115, 215, 1115, 1115)

    # Create geometric transformation
    ops.geomTransf('Linear', 1215, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1215990, 212.12559516, 0.00985439, 254.8101666, 0.07677361, 25.48101666, 0.26686929, -313.49906238, -0.01070773, -376.58231792, -0.08401911, -37.65823179, -0.27411479, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1215991, 314.10991569, 0.01053087, 377.31608903, 0.07912436, 37.7316089, 0.26922004, -314.10991569, -0.01053087, -377.31608903, -0.07912436, -37.7316089, -0.26922004, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1215990, 33886756.58161057, 0.1125, 0.00189844, 0.00058594, 14119481.9090044, 0.00152995)
    ops.section('Aggregator', 1215991, 1215990, 'Mz')
    ops.section('Aggregator', 1215992, 1215991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1215, 1215991, 0.52605088949, 1215992, 0.52605088949, 1215990)
    # Create element
    ops.element('forceBeamColumn', 1215, 215, 315, 1215, 1215)

    # Create geometric transformation
    ops.geomTransf('Linear', 1315, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1315990, 318.33288309, 0.01084972, 379.00876886, 0.10080106, 37.90087689, 0.31533709, -318.33288309, -0.01084972, -379.00876886, -0.10080106, -37.90087689, -0.31533709, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1315991, 318.33288309, 0.01084972, 379.00876886, 0.1000893, 37.90087689, 0.31462532, -318.33288309, -0.01084972, -379.00876886, -0.1000893, -37.90087689, -0.31462532, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1315990, 35996852.87882105, 0.1125, 0.00189844, 0.00058594, 14998688.69950877, 0.00152995)
    ops.section('Aggregator', 1315991, 1315990, 'Mz')
    ops.section('Aggregator', 1315992, 1315991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1315, 1315991, 0.46612218576, 1315992, 0.46612218576, 1315990)
    # Create element
    ops.element('forceBeamColumn', 1315, 315, 415, 1315, 1315)

    # Create geometric transformation
    ops.geomTransf('Linear', 1415, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1415990, 306.96977953, 0.01088528, 369.87162498, 0.08075109, 36.9871625, 0.27047661, -306.96977953, -0.01088528, -369.87162498, -0.08075109, -36.9871625, -0.27047661, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1415991, 207.43590789, 0.01018, 249.94205114, 0.07771186, 24.99420511, 0.26743737, -306.81671577, -0.01105882, -369.6871966, -0.08504135, -36.96871966, -0.27476687, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1415990, 33081490.18380328, 0.1125, 0.00189844, 0.00058594, 13783954.24325137, 0.00152995)
    ops.section('Aggregator', 1415991, 1415990, 'Mz')
    ops.section('Aggregator', 1415992, 1415991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1415, 1415991, 0.52707723026, 1415992, 0.52707723026, 1415990)
    # Create element
    ops.element('forceBeamColumn', 1415, 415, 515, 1415, 1415)

    # Create geometric transformation
    ops.geomTransf('Linear', 1515, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1515990, 209.58426765, 0.01002677, 251.20616481, 0.08561986, 25.12061648, 0.30351542, -309.95809876, -0.01087759, -371.51350201, -0.09369137, -37.1513502, -0.31158692, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1515991, 209.58426765, 0.01002677, 251.20616481, 0.08452525, 25.12061648, 0.3024208, -309.95809876, -0.01087759, -371.51350201, -0.09249219, -37.1513502, -0.31038775, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1515990, 34436193.61732797, 0.1125, 0.00189844, 0.00058594, 14348414.00721999, 0.00152995)
    ops.section('Aggregator', 1515991, 1515990, 'Mz')
    ops.section('Aggregator', 1515992, 1515991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1515, 1515991, 0.45893546939, 1515992, 0.45893546939, 1515990)
    # Create element
    ops.element('forceBeamColumn', 1515, 515, 615, 1515, 1515)

    # Create geometric transformation
    ops.geomTransf('Linear', 1615, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1615990, 210.82648541, 0.01034191, 254.61726396, 0.07828432, 25.4617264, 0.26620875, -311.79222933, -0.01124627, -376.55460697, -0.08567858, -37.6554607, -0.27360301, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1615991, 211.0288679, 0.0104784, 254.86168332, 0.07533542, 25.48616833, 0.26325985, -211.0288679, -0.0104784, -254.86168332, -0.07533542, -25.48616833, -0.26325985, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1615990, 32440553.43578966, 0.1125, 0.00189844, 0.00058594, 13516897.26491236, 0.00152995)
    ops.section('Aggregator', 1615991, 1615990, 'Mz')
    ops.section('Aggregator', 1615992, 1615991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1615, 1615991, 0.5321287860899999, 1615992, 0.5321287860899999, 1615990)
    # Create element
    ops.element('forceBeamColumn', 1615, 615, 715, 1615, 1615)

    # Create geometric transformation
    ops.geomTransf('Linear', 1025, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1025990, 210.71373575, 0.01074809, 254.63207179, 0.07575915, 25.46320718, 0.26238999, -210.71373575, -0.01074809, -254.63207179, -0.07575915, -25.46320718, -0.26238999, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1025991, 210.71373575, 0.01074809, 254.63207179, 0.07614625, 25.46320718, 0.26277708, -210.71373575, -0.01074809, -254.63207179, -0.07614625, -25.46320718, -0.26277708, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1025990, 32271823.18160999, 0.1125, 0.00189844, 0.00058594, 13446592.9923375, 0.00152995)
    ops.section('Aggregator', 1025991, 1025990, 'Mz')
    ops.section('Aggregator', 1025992, 1025991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1025, 1025991, 0.53581714109, 1025992, 0.53581714109, 1025990)
    # Create element
    ops.element('forceBeamColumn', 1025, 25, 125, 1025, 1025)

    # Create geometric transformation
    ops.geomTransf('Linear', 1125, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1125990, 210.78070998, 0.01030386, 254.50496543, 0.08606978, 25.45049654, 0.30285054, -210.78070998, -0.01030386, -254.50496543, -0.08606978, -25.45049654, -0.30285054, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1125991, 210.78070998, 0.01030386, 254.50496543, 0.08612434, 25.45049654, 0.3029051, -210.78070998, -0.01030386, -254.50496543, -0.08612434, -25.45049654, -0.3029051, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1125990, 32503749.23017623, 0.1125, 0.00189844, 0.00058594, 13543228.84590676, 0.00152995)
    ops.section('Aggregator', 1125991, 1125990, 'Mz')
    ops.section('Aggregator', 1125992, 1125991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1125, 1125991, 0.46129554185, 1125992, 0.46129554185, 1125990)
    # Create element
    ops.element('forceBeamColumn', 1125, 125, 225, 1125, 1125)

    # Create geometric transformation
    ops.geomTransf('Linear', 1225, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1225990, 217.22038004, 0.01057282, 260.33833641, 0.07101738, 26.03383364, 0.25638043, -217.22038004, -0.01057282, -260.33833641, -0.07101738, -26.03383364, -0.25638043, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1225991, 217.04087156, 0.01044189, 260.12319574, 0.07358378, 26.01231957, 0.25894683, -321.01490588, -0.01132588, -384.73593751, -0.08049912, -38.47359375, -0.26586217, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1225990, 34455472.41063469, 0.1125, 0.00189844, 0.00058594, 14356446.83776446, 0.00152995)
    ops.section('Aggregator', 1225991, 1225990, 'Mz')
    ops.section('Aggregator', 1225992, 1225991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1225, 1225991, 0.53948184796, 1225992, 0.53948184796, 1225990)
    # Create element
    ops.element('forceBeamColumn', 1225, 225, 325, 1225, 1225)

    # Create geometric transformation
    ops.geomTransf('Linear', 1325, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1325990, 214.16253756, 0.01019382, 256.75213019, 0.08381289, 25.67521302, 0.29875349, -316.69858167, -0.01106123, -379.67908112, -0.09171245, -37.96790811, -0.30665304, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1325991, 214.16253756, 0.01019382, 256.75213019, 0.0840244, 25.67521302, 0.298965, -316.69858167, -0.01106123, -379.67908112, -0.09194416, -37.96790811, -0.30688476, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1325990, 34380045.16889855, 0.1125, 0.00189844, 0.00058594, 14325018.82037439, 0.00152995)
    ops.section('Aggregator', 1325991, 1325990, 'Mz')
    ops.section('Aggregator', 1325992, 1325991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1325, 1325991, 0.46524482289999997, 1325992, 0.46524482289999997, 1325990)
    # Create element
    ops.element('forceBeamColumn', 1325, 325, 425, 1325, 1325)

    # Create geometric transformation
    ops.geomTransf('Linear', 1425, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1425990, 209.43054919, 0.00984133, 251.87123479, 0.07617037, 25.18712348, 0.26715765, -309.56920542, -0.01069526, -372.30279117, -0.08336009, -37.23027912, -0.27434737, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1425991, 209.43922821, 0.00997662, 251.88167259, 0.07469223, 25.18816726, 0.26567951, -209.43922821, -0.00997662, -251.88167259, -0.07469223, -25.18816726, -0.26567951, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1425990, 33580757.60597618, 0.1125, 0.00189844, 0.00058594, 13991982.33582341, 0.00152995)
    ops.section('Aggregator', 1425991, 1425990, 'Mz')
    ops.section('Aggregator', 1425992, 1425991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1425, 1425991, 0.5235950832, 1425992, 0.5235950832, 1425990)
    # Create element
    ops.element('forceBeamColumn', 1425, 425, 525, 1425, 1425)

    # Create geometric transformation
    ops.geomTransf('Linear', 1525, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1525990, 207.09771135, 0.01054401, 250.4827509, 0.08706683, 25.04827509, 0.30367703, -207.09771135, -0.01054401, -250.4827509, -0.08706683, -25.04827509, -0.30367703, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1525991, 207.09771135, 0.01054401, 250.4827509, 0.08604698, 25.04827509, 0.30265717, -207.09771135, -0.01054401, -250.4827509, -0.08604698, -25.04827509, -0.30265717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1525990, 32017553.58100997, 0.1125, 0.00189844, 0.00058594, 13340647.32542082, 0.00152995)
    ops.section('Aggregator', 1525991, 1525990, 'Mz')
    ops.section('Aggregator', 1525992, 1525991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1525, 1525991, 0.46165879528, 1525992, 0.46165879528, 1525990)
    # Create element
    ops.element('forceBeamColumn', 1525, 525, 625, 1525, 1525)

    # Create geometric transformation
    ops.geomTransf('Linear', 1625, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1625990, 207.19905211, 0.01019315, 248.78571179, 0.07348179, 24.87857118, 0.26385221, -207.19905211, -0.01019315, -248.78571179, -0.07348179, -24.87857118, -0.26385221, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1625991, 207.19905211, 0.01019315, 248.78571179, 0.07390861, 24.87857118, 0.26427903, -207.19905211, -0.01019315, -248.78571179, -0.07390861, -24.87857118, -0.26427903, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1625990, 33995737.58695683, 0.1125, 0.00189844, 0.00058594, 14164890.66123201, 0.00152995)
    ops.section('Aggregator', 1625991, 1625990, 'Mz')
    ops.section('Aggregator', 1625992, 1625991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1625, 1625991, 0.52529168899, 1625992, 0.52529168899, 1625990)
    # Create element
    ops.element('forceBeamColumn', 1625, 625, 725, 1625, 1625)

    # Create geometric transformation
    ops.geomTransf('Linear', 1035, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1035990, 211.63130387, 0.01019418, 255.34897499, 0.07448468, 25.5348975, 0.26374409, -211.63130387, -0.01019418, -255.34897499, -0.07448468, -25.5348975, -0.26374409, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1035991, 211.63130387, 0.01019418, 255.34897499, 0.07465974, 25.5348975, 0.26391915, -211.63130387, -0.01019418, -255.34897499, -0.07465974, -25.5348975, -0.26391915, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1035990, 32704000.0442133, 0.1125, 0.00189844, 0.00058594, 13626666.68508888, 0.00152995)
    ops.section('Aggregator', 1035991, 1035990, 'Mz')
    ops.section('Aggregator', 1035992, 1035991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1035, 1035991, 0.52837530649, 1035992, 0.52837530649, 1035990)
    # Create element
    ops.element('forceBeamColumn', 1035, 35, 135, 1035, 1035)

    # Create geometric transformation
    ops.geomTransf('Linear', 1135, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1135990, 213.50854011, 0.01015592, 256.15035205, 0.08090678, 25.6150352, 0.29739759, -213.50854011, -0.01015592, -256.15035205, -0.08090678, -25.6150352, -0.29739759, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1135991, 213.50854011, 0.01015592, 256.15035205, 0.0816634, 25.6150352, 0.29815421, -213.50854011, -0.01015592, -256.15035205, -0.0816634, -25.6150352, -0.29815421, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1135990, 34203202.44616299, 0.1125, 0.00189844, 0.00058594, 14251334.35256791, 0.00152995)
    ops.section('Aggregator', 1135991, 1135990, 'Mz')
    ops.section('Aggregator', 1135992, 1135991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1135, 1135991, 0.46191336851000003, 1135992, 0.46191336851000003, 1135990)
    # Create element
    ops.element('forceBeamColumn', 1135, 135, 235, 1135, 1135)

    # Create geometric transformation
    ops.geomTransf('Linear', 1235, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1235990, 205.76769436, 0.01030326, 248.04599135, 0.07578896, 24.80459914, 0.26613624, -205.76769436, -0.01030326, -248.04599135, -0.07578896, -24.80459914, -0.26613624, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1235991, 205.50537467, 0.01017518, 247.72977383, 0.07809693, 24.77297738, 0.26844421, -303.98855034, -0.01105301, -366.44790895, -0.08546268, -36.64479089, -0.27580996, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1235990, 32956765.14493662, 0.1125, 0.00189844, 0.00058594, 13731985.47705692, 0.00152995)
    ops.section('Aggregator', 1235991, 1235990, 'Mz')
    ops.section('Aggregator', 1235992, 1235991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1235, 1235991, 0.5253555515, 1235992, 0.5253555515, 1235990)
    # Create element
    ops.element('forceBeamColumn', 1235, 235, 335, 1235, 1235)

    # Create geometric transformation
    ops.geomTransf('Linear', 1335, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1335990, 212.25840443, 0.01018938, 256.3840076, 0.08831892, 25.63840076, 0.3043357, -313.79335488, -0.01108773, -379.02667787, -0.09668025, -37.90266779, -0.31269703, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1335991, 212.25840443, 0.01018938, 256.3840076, 0.0883799, 25.63840076, 0.30439667, -313.79335488, -0.01108773, -379.02667787, -0.09674705, -37.90266779, -0.31276382, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1335990, 32399239.60404587, 0.1125, 0.00189844, 0.00058594, 13499683.16835245, 0.00152995)
    ops.section('Aggregator', 1335991, 1335990, 'Mz')
    ops.section('Aggregator', 1335992, 1335991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1335, 1335991, 0.46292700507, 1335992, 0.46292700507, 1335990)
    # Create element
    ops.element('forceBeamColumn', 1335, 335, 435, 1335, 1335)

    # Create geometric transformation
    ops.geomTransf('Linear', 1435, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1435990, 215.69798349, 0.01003088, 258.27508149, 0.07478827, 25.82750815, 0.26276027, -318.84866831, -0.01088637, -381.7869062, -0.08182942, -38.17869062, -0.26980143, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1435991, 215.6917864, 0.01016522, 258.26766114, 0.07178341, 25.82676611, 0.25975542, -215.6917864, -0.01016522, -258.26766114, -0.07178341, -25.82676611, -0.25975542, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1435990, 34680669.79161512, 0.1125, 0.00189844, 0.00058594, 14450279.07983963, 0.00152995)
    ops.section('Aggregator', 1435991, 1435990, 'Mz')
    ops.section('Aggregator', 1435992, 1435991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1435, 1435991, 0.5319941180800001, 1435992, 0.5319941180800001, 1435990)
    # Create element
    ops.element('forceBeamColumn', 1435, 435, 535, 1435, 1435)

    # Create geometric transformation
    ops.geomTransf('Linear', 1535, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1535990, 213.07250943, 0.01012764, 254.56250551, 0.08081704, 25.45625055, 0.29749013, -213.07250943, -0.01012764, -254.56250551, -0.08081704, -25.45625055, -0.29749013, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1535991, 213.07250943, 0.01012764, 254.56250551, 0.07996426, 25.45625055, 0.29663735, -213.07250943, -0.01012764, -254.56250551, -0.07996426, -25.45625055, -0.29663735, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1535990, 35211250.57149435, 0.1125, 0.00189844, 0.00058594, 14671354.40478931, 0.00152995)
    ops.section('Aggregator', 1535991, 1535990, 'Mz')
    ops.section('Aggregator', 1535992, 1535991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1535, 1535991, 0.46152477366, 1535992, 0.46152477366, 1535990)
    # Create element
    ops.element('forceBeamColumn', 1535, 535, 635, 1535, 1535)

    # Create geometric transformation
    ops.geomTransf('Linear', 1635, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1635990, 209.42400056, 0.01026486, 253.00397449, 0.07528841, 25.30039745, 0.2648516, -209.42400056, -0.01026486, -253.00397449, -0.07528841, -25.30039745, -0.2648516, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1635991, 209.42400056, 0.01026486, 253.00397449, 0.07599691, 25.30039745, 0.2655601, -209.42400056, -0.01026486, -253.00397449, -0.07599691, -25.30039745, -0.2655601, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1635990, 32350269.93425506, 0.1125, 0.00189844, 0.00058594, 13479279.13927294, 0.00152995)
    ops.section('Aggregator', 1635991, 1635990, 'Mz')
    ops.section('Aggregator', 1635992, 1635991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1635, 1635991, 0.5275285857400001, 1635992, 0.5275285857400001, 1635990)
    # Create element
    ops.element('forceBeamColumn', 1635, 635, 735, 1635, 1635)

    # Create geometric transformation
    ops.geomTransf('Linear', 1045, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1045990, 210.75107214, 0.01029993, 254.7668916, 0.07627298, 25.47668916, 0.26528526, -210.75107214, -0.01029993, -254.7668916, -0.07627298, -25.47668916, -0.26528526, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1045991, 210.65318695, 0.0101589, 254.64856286, 0.07881944, 25.46485629, 0.26783172, -311.43034567, -0.01105728, -376.47325021, -0.08627631, -37.64732502, -0.27528859, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1045990, 32170656.6586239, 0.1125, 0.00189844, 0.00058594, 13404440.27442663, 0.00152995)
    ops.section('Aggregator', 1045991, 1045990, 'Mz')
    ops.section('Aggregator', 1045992, 1045991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1045, 1045991, 0.52906615116, 1045992, 0.52906615116, 1045990)
    # Create element
    ops.element('forceBeamColumn', 1045, 45, 145, 1045, 1045)

    # Create geometric transformation
    ops.geomTransf('Linear', 1145, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1145990, 203.57540536, 0.01034452, 245.85012863, 0.08751731, 24.58501286, 0.30581962, -301.18555116, -0.01123771, -363.73011938, -0.09578208, -36.37301194, -0.3140844, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1145991, 203.57540536, 0.01034452, 245.85012863, 0.08812031, 24.58501286, 0.30642262, -301.18555116, -0.01123771, -363.73011938, -0.09644268, -36.37301194, -0.314745, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1145990, 32451973.22917267, 0.1125, 0.00189844, 0.00058594, 13521655.51215528, 0.00152995)
    ops.section('Aggregator', 1145991, 1145990, 'Mz')
    ops.section('Aggregator', 1145992, 1145991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1145, 1145991, 0.45808034281, 1145992, 0.45808034281, 1145990)
    # Create element
    ops.element('forceBeamColumn', 1145, 145, 245, 1145, 1145)

    # Create geometric transformation
    ops.geomTransf('Linear', 1245, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1245990, 213.7347201, 0.01014243, 257.70321162, 0.07699904, 25.77032116, 0.2651231, -315.94246706, -0.01103125, -380.93665085, -0.08427405, -38.09366508, -0.27239811, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1245991, 316.43151179, 0.01084757, 381.52629954, 0.08049614, 38.15262995, 0.2686202, -316.43151179, -0.01084757, -381.52629954, -0.08049614, -38.15262995, -0.2686202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1245990, 32900340.89289008, 0.1125, 0.00189844, 0.00058594, 13708475.37203753, 0.00152995)
    ops.section('Aggregator', 1245991, 1245990, 'Mz')
    ops.section('Aggregator', 1245992, 1245991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1245, 1245991, 0.53156411286, 1245992, 0.53156411286, 1245990)
    # Create element
    ops.element('forceBeamColumn', 1245, 245, 345, 1245, 1245)

    # Create geometric transformation
    ops.geomTransf('Linear', 1345, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1345990, 319.96008908, 0.01066684, 385.93903224, 0.10921594, 38.59390322, 0.3253688, -319.96008908, -0.01066684, -385.93903224, -0.10921594, -38.59390322, -0.3253688, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1345991, 319.96008908, 0.01066684, 385.93903224, 0.10953768, 38.59390322, 0.32569054, -319.96008908, -0.01066684, -385.93903224, -0.10953768, -38.59390322, -0.32569054, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1345990, 32787651.62550879, 0.1125, 0.00189844, 0.00058594, 13661521.51062866, 0.00152995)
    ops.section('Aggregator', 1345991, 1345990, 'Mz')
    ops.section('Aggregator', 1345992, 1345991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1345, 1345991, 0.46263556566, 1345992, 0.46263556566, 1345990)
    # Create element
    ops.element('forceBeamColumn', 1345, 345, 445, 1345, 1345)

    # Create geometric transformation
    ops.geomTransf('Linear', 1445, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1445990, 306.58900424, 0.0108874, 367.90166033, 0.07752915, 36.79016603, 0.26713563, -306.58900424, -0.0108874, -367.90166033, -0.07752915, -36.79016603, -0.26713563, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1445991, 207.19957353, 0.01019145, 248.6360113, 0.07519996, 24.86360113, 0.26480644, -306.53045561, -0.01105254, -367.83140296, -0.08227071, -36.7831403, -0.27187719, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1445990, 34148160.07235008, 0.1125, 0.00189844, 0.00058594, 14228400.03014587, 0.00152995)
    ops.section('Aggregator', 1445991, 1445990, 'Mz')
    ops.section('Aggregator', 1445992, 1445991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1445, 1445991, 0.5274081349299999, 1445992, 0.5274081349299999, 1445990)
    # Create element
    ops.element('forceBeamColumn', 1445, 445, 545, 1445, 1445)

    # Create geometric transformation
    ops.geomTransf('Linear', 1545, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1545990, 210.2297655, 0.01013843, 253.4760675, 0.08773496, 25.34760675, 0.30481027, -310.85511423, -0.01102206, -374.80102653, -0.09603066, -37.48010265, -0.31310597, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1545991, 210.2297655, 0.01013843, 253.4760675, 0.08698989, 25.34760675, 0.3040652, -310.85511423, -0.01102206, -374.80102653, -0.09521442, -37.48010265, -0.31228973, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1545990, 32901600.52462185, 0.1125, 0.00189844, 0.00058594, 13709000.21859244, 0.00152995)
    ops.section('Aggregator', 1545991, 1545990, 'Mz')
    ops.section('Aggregator', 1545992, 1545991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1545, 1545991, 0.46066962011, 1545992, 0.46066962011, 1545990)
    # Create element
    ops.element('forceBeamColumn', 1545, 545, 645, 1545, 1545)

    # Create geometric transformation
    ops.geomTransf('Linear', 1645, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1645990, 215.99428739, 0.01002476, 260.09217769, 0.07736576, 26.00921777, 0.26547326, -319.15617632, -0.01090376, -384.31583504, -0.08467722, -38.4315835, -0.27278471, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1645991, 215.911783, 0.0101682, 259.99282901, 0.07448416, 25.9992829, 0.26259166, -215.911783, -0.0101682, -259.99282901, -0.07448416, -25.9992829, -0.26259166, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1645990, 33248681.98324158, 0.1125, 0.00189844, 0.00058594, 13853617.49301733, 0.00152995)
    ops.section('Aggregator', 1645991, 1645990, 'Mz')
    ops.section('Aggregator', 1645992, 1645991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1645, 1645991, 0.53161092118, 1645992, 0.53161092118, 1645990)
    # Create element
    ops.element('forceBeamColumn', 1645, 645, 745, 1645, 1645)

    # Create geometric transformation
    ops.geomTransf('Linear', 1055, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1055990, 212.65538108, 0.01021398, 255.60719037, 0.07238176, 25.56071904, 0.26108257, -212.65538108, -0.01021398, -255.60719037, -0.07238176, -25.56071904, -0.26108257, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1055991, 314.7318308, 0.01077186, 378.30088562, 0.07805772, 37.83008856, 0.26675853, -314.7318308, -0.01077186, -378.30088562, -0.07805772, -37.83008856, -0.26675853, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1055990, 33725303.7607789, 0.1125, 0.00189844, 0.00058594, 14052209.90032454, 0.00152995)
    ops.section('Aggregator', 1055991, 1055990, 'Mz')
    ops.section('Aggregator', 1055992, 1055991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1055, 1055991, 0.5299394373799999, 1055992, 0.5299394373799999, 1055990)
    # Create element
    ops.element('forceBeamColumn', 1055, 55, 155, 1055, 1055)

    # Create geometric transformation
    ops.geomTransf('Linear', 1155, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1155990, 315.06443441, 0.01065527, 375.83494343, 0.10346265, 37.58349434, 0.3202662, -315.06443441, -0.01065527, -375.83494343, -0.10346265, -37.58349434, -0.3202662, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1155991, 315.06443441, 0.01065527, 375.83494343, 0.1027978, 37.58349434, 0.31960134, -315.06443441, -0.01065527, -375.83494343, -0.1027978, -37.58349434, -0.31960134, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1155990, 35566936.32676633, 0.1125, 0.00189844, 0.00058594, 14819556.8028193, 0.00152995)
    ops.section('Aggregator', 1155991, 1155990, 'Mz')
    ops.section('Aggregator', 1155992, 1155991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1155, 1155991, 0.46124706734, 1155992, 0.46124706734, 1155990)
    # Create element
    ops.element('forceBeamColumn', 1155, 155, 255, 1155, 1155)

    # Create geometric transformation
    ops.geomTransf('Linear', 1255, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1255990, 312.71103004, 0.010771, 376.98844029, 0.07904725, 37.69884403, 0.26828137, -312.71103004, -0.010771, -376.98844029, -0.07904725, -37.69884403, -0.26828137, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1255991, 312.71103004, 0.010771, 376.98844029, 0.07971766, 37.69884403, 0.26895178, -312.71103004, -0.010771, -376.98844029, -0.07971766, -37.69884403, -0.26895178, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1255990, 32938044.31000369, 0.1125, 0.00189844, 0.00058594, 13724185.12916821, 0.00152995)
    ops.section('Aggregator', 1255991, 1255990, 'Mz')
    ops.section('Aggregator', 1255992, 1255991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1255, 1255991, 0.5284459273, 1255992, 0.5284459273, 1255990)
    # Create element
    ops.element('forceBeamColumn', 1255, 255, 355, 1255, 1255)

    # Create geometric transformation
    ops.geomTransf('Linear', 1355, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1355990, 305.74243229, 0.01076922, 368.24467732, 0.10851728, 36.82446773, 0.32744786, -305.74243229, -0.01076922, -368.24467732, -0.10851728, -36.82446773, -0.32744786, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1355991, 305.74243229, 0.01076922, 368.24467732, 0.10889216, 36.82446773, 0.32782274, -305.74243229, -0.01076922, -368.24467732, -0.10889216, -36.82446773, -0.32782274, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1355990, 33189704.49800519, 0.1125, 0.00189844, 0.00058594, 13829043.54083549, 0.00152995)
    ops.section('Aggregator', 1355991, 1355990, 'Mz')
    ops.section('Aggregator', 1355992, 1355991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1355, 1355991, 0.45676579879, 1355992, 0.45676579879, 1355990)
    # Create element
    ops.element('forceBeamColumn', 1355, 355, 455, 1355, 1355)

    # Create geometric transformation
    ops.geomTransf('Linear', 1455, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1455990, 300.20314001, 0.01079331, 362.61348627, 0.08243443, 36.26134863, 0.27412577, -300.20314001, -0.01079331, -362.61348627, -0.08243443, -36.26134863, -0.27412577, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1455991, 300.20314001, 0.01079331, 362.61348627, 0.08270229, 36.26134863, 0.27439363, -300.20314001, -0.01079331, -362.61348627, -0.08270229, -36.26134863, -0.27439363, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1455990, 32397485.93105464, 0.1125, 0.00189844, 0.00058594, 13498952.47127277, 0.00152995)
    ops.section('Aggregator', 1455991, 1455990, 'Mz')
    ops.section('Aggregator', 1455992, 1455991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1455, 1455991, 0.52167195938, 1455992, 0.52167195938, 1455990)
    # Create element
    ops.element('forceBeamColumn', 1455, 455, 555, 1455, 1455)

    # Create geometric transformation
    ops.geomTransf('Linear', 1555, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1555990, 321.03846222, 0.01065311, 383.26486103, 0.1026565, 38.3264861, 0.3180355, -321.03846222, -0.01065311, -383.26486103, -0.1026565, -38.3264861, -0.3180355, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1555991, 321.03846222, 0.01065311, 383.26486103, 0.10193388, 38.3264861, 0.31731287, -321.03846222, -0.01065311, -383.26486103, -0.10193388, -38.3264861, -0.31731287, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1555990, 35385064.45344514, 0.1125, 0.00189844, 0.00058594, 14743776.85560214, 0.00152995)
    ops.section('Aggregator', 1555991, 1555990, 'Mz')
    ops.section('Aggregator', 1555992, 1555991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1555, 1555991, 0.46429783612000003, 1555992, 0.46429783612000003, 1555990)
    # Create element
    ops.element('forceBeamColumn', 1555, 555, 655, 1555, 1555)

    # Create geometric transformation
    ops.geomTransf('Linear', 1655, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1655990, 311.3855993, 0.01032412, 373.66818741, 0.07878169, 37.36681874, 0.27050604, -311.3855993, -0.01032412, -373.66818741, -0.07878169, -37.36681874, -0.27050604, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1655991, 210.16652262, 0.00979855, 252.20351788, 0.07415946, 25.22035179, 0.26588381, -210.16652262, -0.00979855, -252.20351788, -0.07415946, -25.22035179, -0.26588381, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1655990, 34140978.95822734, 0.1125, 0.00189844, 0.00058594, 14225407.89926139, 0.00152995)
    ops.section('Aggregator', 1655991, 1655990, 'Mz')
    ops.section('Aggregator', 1655992, 1655991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1655, 1655991, 0.52158216993, 1655992, 0.52158216993, 1655990)
    # Create element
    ops.element('forceBeamColumn', 1655, 655, 755, 1655, 1655)

    # Create geometric transformation
    ops.geomTransf('Linear', 1006, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1006990, 138.45331795, 0.00961659, 166.30381302, 0.05897499, 16.6303813, 0.22692331, -138.45331795, -0.00961659, -166.30381302, -0.05897499, -16.6303813, -0.22692331, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1006991, 204.90534148, 0.01007715, 246.12295395, 0.06199084, 24.61229539, 0.23181782, -204.90534148, -0.01007715, -246.12295395, -0.06199084, -24.61229539, -0.23181782, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1006990, 33901356.91945792, 0.1125, 0.00189844, 0.00058594, 14125565.38310747, 0.00152995)
    ops.section('Aggregator', 1006991, 1006990, 'Mz')
    ops.section('Aggregator', 1006992, 1006991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1006, 1006991, 0.46325384039, 1006992, 0.46325384039, 1006990)
    # Create element
    ops.element('forceBeamColumn', 1006, 6, 106, 1006, 1006)

    # Create geometric transformation
    ops.geomTransf('Linear', 1106, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1106990, 206.63948676, 0.00993652, 249.12476178, 0.11629673, 24.91247618, 0.36993056, -206.63948676, -0.00993652, -249.12476178, -0.11629673, -24.91247618, -0.36993056, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1106991, 206.63948676, 0.00993652, 249.12476178, 0.11536838, 24.91247618, 0.3690022, -206.63948676, -0.00993652, -249.12476178, -0.11536838, -24.91247618, -0.3690022, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1106990, 32926258.16416155, 0.1125, 0.00189844, 0.00058594, 13719274.23506731, 0.00152995)
    ops.section('Aggregator', 1106991, 1106990, 'Mz')
    ops.section('Aggregator', 1106992, 1106991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1106, 1106991, 0.39426917699, 1106992, 0.39426917699, 1106990)
    # Create element
    ops.element('forceBeamColumn', 1106, 106, 206, 1106, 1106)

    # Create geometric transformation
    ops.geomTransf('Linear', 1206, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1206990, 201.21161981, 0.00997071, 242.16611487, 0.07793156, 24.21661149, 0.29566003, -201.21161981, -0.00997071, -242.16611487, -0.07793156, -24.21661149, -0.29566003, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1206991, 201.21161981, 0.00997071, 242.16611487, 0.0782597, 24.21661149, 0.29598817, -201.21161981, -0.00997071, -242.16611487, -0.0782597, -24.21661149, -0.29598817, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1206990, 33386161.33024418, 0.1125, 0.00189844, 0.00058594, 13910900.55426841, 0.00152995)
    ops.section('Aggregator', 1206991, 1206990, 'Mz')
    ops.section('Aggregator', 1206992, 1206991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1206, 1206991, 0.45928765429, 1206992, 0.45928765429, 1206990)
    # Create element
    ops.element('forceBeamColumn', 1206, 206, 306, 1206, 1206)

    # Create geometric transformation
    ops.geomTransf('Linear', 1306, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1306990, 207.54534058, 0.01009289, 248.91720551, 0.11006022, 24.89172055, 0.36174377, -207.54534058, -0.01009289, -248.91720551, -0.11006022, -24.89172055, -0.36174377, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1306991, 207.54534058, 0.01009289, 248.91720551, 0.11005724, 24.89172055, 0.36174079, -207.54534058, -0.01009289, -248.91720551, -0.11005724, -24.89172055, -0.36174079, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1306990, 34282276.81059825, 0.1125, 0.00189844, 0.00058594, 14284282.00441594, 0.00152995)
    ops.section('Aggregator', 1306991, 1306990, 'Mz')
    ops.section('Aggregator', 1306992, 1306991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1306, 1306991, 0.39732434579, 1306992, 0.39732434579, 1306990)
    # Create element
    ops.element('forceBeamColumn', 1306, 306, 406, 1306, 1306)

    # Create geometric transformation
    ops.geomTransf('Linear', 1406, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1406990, 204.2293843, 0.00996927, 244.68432284, 0.07409888, 24.46843228, 0.28759985, -204.2293843, -0.00996927, -244.68432284, -0.07409888, -24.46843228, -0.28759985, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1406991, 204.2293843, 0.00996927, 244.68432284, 0.07451513, 24.46843228, 0.29113128, -204.2293843, -0.00996927, -244.68432284, -0.07451513, -24.46843228, -0.29113128, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1406990, 34539881.33542266, 0.1125, 0.00189844, 0.00058594, 14391617.22309278, 0.00152995)
    ops.section('Aggregator', 1406991, 1406990, 'Mz')
    ops.section('Aggregator', 1406992, 1406991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1406, 1406991, 0.46164609043000004, 1406992, 0.46164609043000004, 1406990)
    # Create element
    ops.element('forceBeamColumn', 1406, 406, 506, 1406, 1406)

    # Create geometric transformation
    ops.geomTransf('Linear', 1506, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1506990, 212.26744287, 0.01003473, 255.38415504, 0.11124766, 25.5384155, 0.36164302, -212.26744287, -0.01003473, -255.38415504, -0.11124766, -25.5384155, -0.36164302, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1506991, 212.26744287, 0.01003473, 255.38415504, 0.11179097, 25.5384155, 0.36218633, -212.26744287, -0.01003473, -255.38415504, -0.11179097, -25.5384155, -0.36218633, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1506990, 33477055.71145195, 0.1125, 0.00189844, 0.00058594, 13948773.21310498, 0.00152995)
    ops.section('Aggregator', 1506991, 1506990, 'Mz')
    ops.section('Aggregator', 1506992, 1506991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1506, 1506991, 0.39936841546, 1506992, 0.39936841546, 1506990)
    # Create element
    ops.element('forceBeamColumn', 1506, 506, 606, 1506, 1506)

    # Create geometric transformation
    ops.geomTransf('Linear', 1606, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1606990, 209.27610565, 0.00993257, 252.20391526, 0.06234074, 25.22039153, 0.22921947, -209.27610565, -0.00993257, -252.20391526, -0.06234074, -25.22039153, -0.22921947, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1606991, 141.21470657, 0.00948392, 170.18140594, 0.05968963, 17.01814059, 0.22770094, -141.21470657, -0.00948392, -170.18140594, -0.05968963, -17.01814059, -0.22770094, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1606990, 33033645.22538763, 0.1125, 0.00189844, 0.00058594, 13764018.84391151, 0.00152995)
    ops.section('Aggregator', 1606991, 1606990, 'Mz')
    ops.section('Aggregator', 1606992, 1606991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1606, 1606991, 0.46395785217, 1606992, 0.46395785217, 1606990)
    # Create element
    ops.element('forceBeamColumn', 1606, 606, 706, 1606, 1606)

    # Create geometric transformation
    ops.geomTransf('Linear', 1016, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1016990, 140.04745016, 0.00984137, 169.21195065, 0.0830093, 16.92119506, 0.29640376, -214.15422191, -0.01067325, -258.751256, -0.09156985, -25.8751256, -0.30496431, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1016991, 207.43475212, 0.01040112, 250.6324749, 0.08474483, 25.06324749, 0.29813929, -214.08341089, -0.0105696, -258.66569878, -0.0855993, -25.86656988, -0.29899376, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1016990, 32314222.50594323, 0.1125, 0.00189844, 0.00058594, 13464259.37747635, 0.00152995)
    ops.section('Aggregator', 1016991, 1016990, 'Mz')
    ops.section('Aggregator', 1016992, 1016991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1016, 1016991, 0.46861572655, 1016992, 0.46861572655, 1016990)
    # Create element
    ops.element('forceBeamColumn', 1016, 16, 116, 1016, 1016)

    # Create geometric transformation
    ops.geomTransf('Linear', 1116, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1116990, 202.23273157, 0.00998575, 244.54677925, 0.09840468, 24.45467793, 0.35359512, -208.69870856, -0.01014761, -252.36566117, -0.09938241, -25.23656612, -0.35457284, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1116991, 202.23273157, 0.00998575, 244.54677925, 0.09802361, 24.45467793, 0.35321404, -208.69870856, -0.01014761, -252.36566117, -0.09899782, -25.23656612, -0.35418825, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1116990, 32079195.72745452, 0.1125, 0.00189844, 0.00058594, 13366331.55310605, 0.00152995)
    ops.section('Aggregator', 1116991, 1116990, 'Mz')
    ops.section('Aggregator', 1116992, 1116991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1116, 1116991, 0.39186421997000004, 1116992, 0.39186421997000004, 1116990)
    # Create element
    ops.element('forceBeamColumn', 1116, 116, 216, 1116, 1116)

    # Create geometric transformation
    ops.geomTransf('Linear', 1216, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1216990, 211.56636526, 0.01006842, 252.34769616, 0.07655489, 25.23476962, 0.29013701, -218.35837307, -0.01022562, -260.44892491, -0.07732559, -26.04489249, -0.29090771, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1216991, 211.56636526, 0.01006842, 252.34769616, 0.07773527, 25.23476962, 0.29131739, -218.35837307, -0.01022562, -260.44892491, -0.07851686, -26.04489249, -0.29209898, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1216990, 35590585.96787701, 0.1125, 0.00189844, 0.00058594, 14829410.81994875, 0.00152995)
    ops.section('Aggregator', 1216991, 1216990, 'Mz')
    ops.section('Aggregator', 1216992, 1216991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1216, 1216991, 0.46820398795, 1216992, 0.46820398795, 1216990)
    # Create element
    ops.element('forceBeamColumn', 1216, 216, 316, 1216, 1216)

    # Create geometric transformation
    ops.geomTransf('Linear', 1316, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1316990, 208.1592801, 0.01002219, 251.25377145, 0.09521183, 25.12537715, 0.34748433, -214.80273346, -0.01018335, -259.27259585, -0.09615905, -25.92725958, -0.34843156, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1316991, 208.1592801, 0.01002219, 251.25377145, 0.0956894, 25.12537715, 0.34796191, -214.80273346, -0.01018335, -259.27259585, -0.09664103, -25.92725958, -0.34891354, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1316990, 32599722.89934143, 0.1125, 0.00189844, 0.00058594, 13583217.8747256, 0.00152995)
    ops.section('Aggregator', 1316991, 1316990, 'Mz')
    ops.section('Aggregator', 1316992, 1316991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1316, 1316991, 0.39639674584, 1316992, 0.39639674584, 1316990)
    # Create element
    ops.element('forceBeamColumn', 1316, 316, 416, 1316, 1316)

    # Create geometric transformation
    ops.geomTransf('Linear', 1416, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1416990, 207.97596776, 0.00987002, 249.71177676, 0.08233986, 24.97117768, 0.29842274, -214.62502641, -0.01002634, -257.69514266, -0.08316488, -25.76951427, -0.29924776, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1416991, 207.97596776, 0.00987002, 249.71177676, 0.08192105, 24.97117768, 0.29800393, -214.62502641, -0.01002634, -257.69514266, -0.08274221, -25.76951427, -0.29882509, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1416990, 34002623.23528772, 0.1125, 0.00189844, 0.00058594, 14167759.68136988, 0.00152995)
    ops.section('Aggregator', 1416991, 1416990, 'Mz')
    ops.section('Aggregator', 1416992, 1416991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1416, 1416991, 0.46278538753, 1416992, 0.46278538753, 1416990)
    # Create element
    ops.element('forceBeamColumn', 1416, 416, 516, 1416, 1416)

    # Create geometric transformation
    ops.geomTransf('Linear', 1516, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1516990, 207.11901932, 0.01014199, 250.45921207, 0.09819149, 25.04592121, 0.35003953, -213.7342877, -0.01030624, -258.45874253, -0.09916819, -25.84587425, -0.35101623, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1516991, 207.11901932, 0.01014199, 250.45921207, 0.09858818, 25.04592121, 0.35043622, -213.7342877, -0.01030624, -258.45874253, -0.09956855, -25.84587425, -0.35141659, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1516990, 32074831.19153674, 0.1125, 0.00189844, 0.00058594, 13364512.99647364, 0.00152995)
    ops.section('Aggregator', 1516991, 1516990, 'Mz')
    ops.section('Aggregator', 1516992, 1516991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1516, 1516991, 0.3970648333, 1516992, 0.3970648333, 1516990)
    # Create element
    ops.element('forceBeamColumn', 1516, 516, 616, 1516, 1516)

    # Create geometric transformation
    ops.geomTransf('Linear', 1616, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1616990, 206.89478985, 0.00998576, 249.62608563, 0.08420912, 24.96260856, 0.3001242, -213.50191271, -0.01014619, -257.59781957, -0.08505444, -25.75978196, -0.30096951, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1616991, 139.60432466, 0.00945049, 168.43769303, 0.08246648, 16.8437693, 0.29838155, -213.39910786, -0.01025226, -257.47378178, -0.09098087, -25.74737818, -0.30689595, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1616990, 32712813.59279149, 0.1125, 0.00189844, 0.00058594, 13630338.99699645, 0.00152995)
    ops.section('Aggregator', 1616991, 1616990, 'Mz')
    ops.section('Aggregator', 1616992, 1616991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1616, 1616991, 0.46314506101, 1616992, 0.46314506101, 1616990)
    # Create element
    ops.element('forceBeamColumn', 1616, 616, 716, 1616, 1616)

    # Create geometric transformation
    ops.geomTransf('Linear', 1026, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1026990, 139.03793228, 0.00925681, 166.82513948, 0.07451381, 16.68251395, 0.29180764, -205.87757182, -0.00987392, -247.02291002, -0.08136431, -24.702291, -0.29865814, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1026991, 139.03793228, 0.00925681, 166.82513948, 0.07457001, 16.68251395, 0.29186385, -205.87757182, -0.00987392, -247.02291002, -0.08142588, -24.702291, -0.29871972, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1026990, 34175270.86136969, 0.1125, 0.00189844, 0.00058594, 14239696.19223737, 0.00152995)
    ops.section('Aggregator', 1026991, 1026990, 'Mz')
    ops.section('Aggregator', 1026992, 1026991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1026, 1026991, 0.46020633528000005, 1026992, 0.46020633528000005, 1026990)
    # Create element
    ops.element('forceBeamColumn', 1026, 26, 126, 1026, 1026)

    # Create geometric transformation
    ops.geomTransf('Linear', 1126, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1126990, 136.21851653, 0.00940681, 164.1915184, 0.08709365, 16.41915184, 0.34125391, -201.74851416, -0.01003962, -243.17835575, -0.09514715, -24.31783558, -0.34930742, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1126991, 136.21851653, 0.00940681, 164.1915184, 0.08813339, 16.41915184, 0.343789, -201.74851416, -0.01003962, -243.17835575, -0.09628621, -24.31783558, -0.35194182, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1126990, 32982125.95240894, 0.1125, 0.00189844, 0.00058594, 13742552.48017039, 0.00152995)
    ops.section('Aggregator', 1126991, 1126990, 'Mz')
    ops.section('Aggregator', 1126992, 1126991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1126, 1126991, 0.39115120217, 1126992, 0.39115120217, 1126990)
    # Create element
    ops.element('forceBeamColumn', 1126, 126, 226, 1126, 1126)

    # Create geometric transformation
    ops.geomTransf('Linear', 1226, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1226990, 142.06477382, 0.00949016, 170.02179627, 0.0727469, 17.00217963, 0.28713081, -210.39530119, -0.01011473, -251.79913411, -0.07941379, -25.17991341, -0.2937977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1226991, 210.5500706, 0.01001482, 251.98436069, 0.08434132, 25.19843607, 0.29872522, -210.5500706, -0.01001482, -251.98436069, -0.08434132, -25.19843607, -0.29872522, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1226990, 34801762.97945986, 0.1125, 0.00189844, 0.00058594, 14500734.57477494, 0.00152995)
    ops.section('Aggregator', 1226991, 1226990, 'Mz')
    ops.section('Aggregator', 1226992, 1226991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1226, 1226991, 0.46645293054000003, 1226992, 0.46645293054000003, 1226990)
    # Create element
    ops.element('forceBeamColumn', 1226, 226, 326, 1226, 1226)

    # Create geometric transformation
    ops.geomTransf('Linear', 1326, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1326990, 205.94289685, 0.00982036, 248.87236604, 0.11660688, 24.8872366, 0.37165662, -205.94289685, -0.00982036, -248.87236604, -0.11660688, -24.8872366, -0.37165662, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1326991, 205.94289685, 0.00982036, 248.87236604, 0.11672486, 24.8872366, 0.3717746, -205.94289685, -0.00982036, -248.87236604, -0.11672486, -24.8872366, -0.3717746, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1326990, 32265493.05474525, 0.1125, 0.00189844, 0.00058594, 13443955.43947719, 0.00152995)
    ops.section('Aggregator', 1326991, 1326990, 'Mz')
    ops.section('Aggregator', 1326992, 1326991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1326, 1326991, 0.39208038376000004, 1326992, 0.39208038376000004, 1326990)
    # Create element
    ops.element('forceBeamColumn', 1326, 326, 426, 1326, 1326)

    # Create geometric transformation
    ops.geomTransf('Linear', 1426, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1426990, 212.26546855, 0.01006803, 257.48816629, 0.10159481, 25.74881663, 0.31575984, -212.26546855, -0.01006803, -257.48816629, -0.10159481, -25.74881663, -0.31575984, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1426991, 143.2235225, 0.00951362, 173.73698337, 0.08656851, 17.37369834, 0.30030333, -211.91541598, -0.01018735, -257.06353578, -0.09460256, -25.70635358, -0.30833738, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1426990, 31133168.28462791, 0.1125, 0.00189844, 0.00058594, 12972153.4519283, 0.00152995)
    ops.section('Aggregator', 1426991, 1426990, 'Mz')
    ops.section('Aggregator', 1426992, 1426991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1426, 1426991, 0.46692963386999997, 1426992, 0.46692963386999997, 1426990)
    # Create element
    ops.element('forceBeamColumn', 1426, 426, 526, 1426, 1426)

    # Create geometric transformation
    ops.geomTransf('Linear', 1526, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1526990, 144.0252166, 0.00936931, 173.81487321, 0.08709277, 17.38148732, 0.33827522, -213.09112948, -0.01001788, -257.16613054, -0.09516553, -25.71661305, -0.34634798, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1526991, 144.0252166, 0.00936931, 173.81487321, 0.08751092, 17.38148732, 0.33869336, -213.09112948, -0.01001788, -257.16613054, -0.09562362, -25.71661305, -0.34680606, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1526990, 32643691.54455018, 0.1125, 0.00189844, 0.00058594, 13601538.14356257, 0.00152995)
    ops.section('Aggregator', 1526991, 1526990, 'Mz')
    ops.section('Aggregator', 1526992, 1526991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1526, 1526991, 0.39811699234000003, 1526992, 0.39811699234000003, 1526990)
    # Create element
    ops.element('forceBeamColumn', 1526, 526, 626, 1526, 1526)

    # Create geometric transformation
    ops.geomTransf('Linear', 1626, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1626990, 138.71074462, 0.00967998, 167.66634555, 0.0762774, 16.76663455, 0.29129069, -205.43233716, -0.01033876, -248.31594209, -0.08329759, -24.83159421, -0.29831089, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1626991, 138.71074462, 0.00967998, 167.66634555, 0.07664632, 16.76663455, 0.29169226, -205.43233716, -0.01033876, -248.31594209, -0.08370175, -24.83159421, -0.29874769, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1626990, 32195464.82758787, 0.1125, 0.00189844, 0.00058594, 13414777.01149495, 0.00152995)
    ops.section('Aggregator', 1626991, 1626990, 'Mz')
    ops.section('Aggregator', 1626992, 1626991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1626, 1626991, 0.46501691687, 1626992, 0.46501691687, 1626990)
    # Create element
    ops.element('forceBeamColumn', 1626, 626, 726, 1626, 1626)

    # Create geometric transformation
    ops.geomTransf('Linear', 1036, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1036990, 137.57763435, 0.0093751, 165.54313975, 0.07585906, 16.55431398, 0.29315927, -203.75003793, -0.01000332, -245.16645574, -0.08283786, -24.51664557, -0.30013807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1036991, 137.57763435, 0.0093751, 165.54313975, 0.07611816, 16.55431398, 0.29341837, -203.75003793, -0.01000332, -245.16645574, -0.08312171, -24.51664557, -0.30042192, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1036990, 33445080.70795995, 0.1125, 0.00189844, 0.00058594, 13935450.29498331, 0.00152995)
    ops.section('Aggregator', 1036991, 1036990, 'Mz')
    ops.section('Aggregator', 1036992, 1036991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1036, 1036991, 0.4601928289, 1036992, 0.4601928289, 1036990)
    # Create element
    ops.element('forceBeamColumn', 1036, 36, 136, 1036, 1036)

    # Create geometric transformation
    ops.geomTransf('Linear', 1136, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1136990, 137.89592039, 0.00960374, 167.30131871, 0.08945536, 16.73013187, 0.34041636, -204.18357859, -0.01027287, -247.72438416, -0.09775197, -24.77243842, -0.34871297, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1136991, 137.89592039, 0.00960374, 167.30131871, 0.08960355, 16.73013187, 0.34167073, -204.18357859, -0.01027287, -247.72438416, -0.09791432, -24.77243842, -0.3499815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1136990, 31082890.67619837, 0.1125, 0.00189844, 0.00058594, 12951204.44841599, 0.00152995)
    ops.section('Aggregator', 1136991, 1136990, 'Mz')
    ops.section('Aggregator', 1136992, 1136991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1136, 1136991, 0.39492531519, 1136992, 0.39492531519, 1136990)
    # Create element
    ops.element('forceBeamColumn', 1136, 136, 236, 1136, 1136)

    # Create geometric transformation
    ops.geomTransf('Linear', 1236, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1236990, 138.33786988, 0.00939116, 167.1345747, 0.07791137, 16.71345747, 0.29488754, -204.82287688, -0.0100352, -247.45924198, -0.08510049, -24.7459242, -0.30207666, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1236991, 204.98478969, 0.00992839, 247.6548589, 0.0917967, 24.76548589, 0.30877287, -204.98478969, -0.00992839, -247.6548589, -0.0917967, -24.76548589, -0.30877287, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1236990, 32334319.94834678, 0.1125, 0.00189844, 0.00058594, 13472633.31181116, 0.00152995)
    ops.section('Aggregator', 1236991, 1236990, 'Mz')
    ops.section('Aggregator', 1236992, 1236991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1236, 1236991, 0.46088010069, 1236992, 0.46088010069, 1236990)
    # Create element
    ops.element('forceBeamColumn', 1236, 236, 336, 1236, 1236)

    # Create geometric transformation
    ops.geomTransf('Linear', 1336, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1336990, 211.38223473, 0.01006603, 255.43191901, 0.11452707, 25.5431919, 0.36529387, -211.38223473, -0.01006603, -255.43191901, -0.11452707, -25.5431919, -0.36529387, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1336991, 211.38223473, 0.01006603, 255.43191901, 0.11481533, 25.5431919, 0.36558213, -211.38223473, -0.01006603, -255.43191901, -0.11481533, -25.5431919, -0.36558213, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1336990, 32280767.54312511, 0.1125, 0.00189844, 0.00058594, 13450319.80963546, 0.00152995)
    ops.section('Aggregator', 1336991, 1336990, 'Mz')
    ops.section('Aggregator', 1336992, 1336991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1336, 1336991, 0.3987768752, 1336992, 0.3987768752, 1336990)
    # Create element
    ops.element('forceBeamColumn', 1336, 336, 436, 1336, 1336)

    # Create geometric transformation
    ops.geomTransf('Linear', 1436, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1436990, 205.86737159, 0.0104181, 249.14238679, 0.10236788, 24.91423868, 0.31629496, -205.86737159, -0.0104181, -249.14238679, -0.10236788, -24.91423868, -0.31629496, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1436991, 139.02260749, 0.00985132, 168.24630334, 0.08616226, 16.82463033, 0.29882776, -205.90375588, -0.01052256, -249.18641936, -0.09412276, -24.91864194, -0.30678826, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1436990, 31843530.11069036, 0.1125, 0.00189844, 0.00058594, 13268137.54612098, 0.00152995)
    ops.section('Aggregator', 1436991, 1436990, 'Mz')
    ops.section('Aggregator', 1436992, 1436991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1436, 1436991, 0.46744899284, 1436992, 0.46744899284, 1436990)
    # Create element
    ops.element('forceBeamColumn', 1436, 436, 536, 1436, 1436)

    # Create geometric transformation
    ops.geomTransf('Linear', 1536, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1536990, 140.84056655, 0.00943732, 169.69956077, 0.08702339, 16.96995608, 0.33946666, -208.5203644, -0.01007816, -251.24731544, -0.0950753, -25.12473154, -0.34751857, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1536991, 140.84056655, 0.00943732, 169.69956077, 0.0860964, 16.96995608, 0.33496611, -208.5203644, -0.01007816, -251.24731544, -0.09405977, -25.12473154, -0.34292947, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1536990, 33083006.76340811, 0.1125, 0.00189844, 0.00058594, 13784586.15142004, 0.00152995)
    ops.section('Aggregator', 1536991, 1536990, 'Mz')
    ops.section('Aggregator', 1536992, 1536991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1536, 1536991, 0.3961285928, 1536992, 0.3961285928, 1536990)
    # Create element
    ops.element('forceBeamColumn', 1536, 536, 636, 1536, 1536)

    # Create geometric transformation
    ops.geomTransf('Linear', 1636, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1636990, 138.06068997, 0.00919203, 165.54412424, 0.07410302, 16.55441242, 0.29224359, -204.43734448, -0.00980296, -245.13423164, -0.08091428, -24.51342316, -0.29905485, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1636991, 138.06068997, 0.00919203, 165.54412424, 0.07418328, 16.55441242, 0.29232385, -204.43734448, -0.00980296, -245.13423164, -0.0810022, -24.51342316, -0.29914278, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1636990, 34338376.59198092, 0.1125, 0.00189844, 0.00058594, 14307656.91332538, 0.00152995)
    ops.section('Aggregator', 1636991, 1636990, 'Mz')
    ops.section('Aggregator', 1636992, 1636991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1636, 1636991, 0.45841998697, 1636992, 0.45841998697, 1636990)
    # Create element
    ops.element('forceBeamColumn', 1636, 636, 736, 1636, 1636)

    # Create geometric transformation
    ops.geomTransf('Linear', 1046, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1046990, 139.98567267, 0.00962015, 168.95462739, 0.08164787, 16.89546274, 0.29635512, -214.02432454, -0.01043415, -258.31500692, -0.0900701, -25.83150069, -0.30477736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1046991, 207.41757731, 0.01016541, 250.34104434, 0.0833238, 25.03410443, 0.29803105, -214.05254178, -0.01032916, -258.3490635, -0.0841626, -25.83490635, -0.29886985, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1046990, 32619219.86720371, 0.1125, 0.00189844, 0.00058594, 13591341.61133488, 0.00152995)
    ops.section('Aggregator', 1046991, 1046990, 'Mz')
    ops.section('Aggregator', 1046992, 1046991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1046, 1046991, 0.4657504458, 1046992, 0.4657504458, 1046990)
    # Create element
    ops.element('forceBeamColumn', 1046, 46, 146, 1046, 1046)

    # Create geometric transformation
    ops.geomTransf('Linear', 1146, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1146990, 206.47861111, 0.01006892, 246.84656252, 0.09087371, 24.68465625, 0.34295084, -213.11889195, -0.01022733, -254.78506274, -0.09177772, -25.47850627, -0.34385486, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1146991, 206.47861111, 0.01006892, 246.84656252, 0.09072788, 24.68465625, 0.34280501, -213.11889195, -0.01022733, -254.78506274, -0.09163055, -25.47850627, -0.34370768, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1146990, 35057203.30682264, 0.1125, 0.00189844, 0.00058594, 14607168.04450944, 0.00152995)
    ops.section('Aggregator', 1146991, 1146990, 'Mz')
    ops.section('Aggregator', 1146992, 1146991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1146, 1146991, 0.39670397356000003, 1146992, 0.39670397356000003, 1146990)
    # Create element
    ops.element('forceBeamColumn', 1146, 146, 246, 1146, 1146)

    # Create geometric transformation
    ops.geomTransf('Linear', 1246, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1246990, 207.4887604, 0.00999306, 249.14500258, 0.08195889, 24.91450026, 0.29744979, -214.13439178, -0.01015162, -257.1248365, -0.0827815, -25.71248365, -0.2982724, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1246991, 207.4887604, 0.00999306, 249.14500258, 0.08113628, 24.91450026, 0.29662718, -214.13439178, -0.01015162, -257.1248365, -0.0819513, -25.71248365, -0.29744219, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1246990, 33984097.23873732, 0.1125, 0.00189844, 0.00058594, 14160040.51614055, 0.00152995)
    ops.section('Aggregator', 1246991, 1246990, 'Mz')
    ops.section('Aggregator', 1246992, 1246991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1246, 1246991, 0.46405672443, 1246992, 0.46405672443, 1246990)
    # Create element
    ops.element('forceBeamColumn', 1246, 246, 346, 1246, 1246)

    # Create geometric transformation
    ops.geomTransf('Linear', 1346, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1346990, 206.25890193, 0.00994384, 247.84591467, 0.09326635, 24.78459147, 0.34671316, -212.86299539, -0.0101019, -255.78156044, -0.09419325, -25.57815604, -0.34764006, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1346991, 206.25890193, 0.00994384, 247.84591467, 0.09336853, 24.78459147, 0.34681534, -212.86299539, -0.0101019, -255.78156044, -0.09429637, -25.57815604, -0.34774319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1346990, 33801003.13382454, 0.1125, 0.00189844, 0.00058594, 14083751.30576023, 0.00152995)
    ops.section('Aggregator', 1346991, 1346990, 'Mz')
    ops.section('Aggregator', 1346992, 1346991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1346, 1346991, 0.3945601006, 1346992, 0.3945601006, 1346990)
    # Create element
    ops.element('forceBeamColumn', 1346, 346, 446, 1346, 1346)

    # Create geometric transformation
    ops.geomTransf('Linear', 1446, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1446990, 209.38849264, 0.01017031, 252.2363775, 0.08314703, 25.22363775, 0.29714689, -216.088018, -0.01033313, -260.3068497, -0.08398323, -26.03068497, -0.29798309, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1446991, 209.38849264, 0.01017031, 252.2363775, 0.08242306, 25.22363775, 0.29642292, -216.088018, -0.01033313, -260.3068497, -0.08325258, -26.03068497, -0.29725244, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1446990, 33143857.47774325, 0.1125, 0.00189844, 0.00058594, 13809940.61572635, 0.00152995)
    ops.section('Aggregator', 1446991, 1446990, 'Mz')
    ops.section('Aggregator', 1446992, 1446991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1446, 1446991, 0.4672900163, 1446992, 0.4672900163, 1446990)
    # Create element
    ops.element('forceBeamColumn', 1446, 446, 546, 1446, 1446)

    # Create geometric transformation
    ops.geomTransf('Linear', 1546, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1546990, 207.54415716, 0.01006484, 249.65979382, 0.09430477, 24.96597938, 0.34628283, -214.18966347, -0.01022536, -257.65383113, -0.0952426, -25.76538311, -0.34722066, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1546991, 207.54415716, 0.01006484, 249.65979382, 0.09418374, 24.96597938, 0.3461618, -214.18966347, -0.01022536, -257.65383113, -0.09512045, -25.76538311, -0.34709851, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1546990, 33520831.82449481, 0.1125, 0.00189844, 0.00058594, 13967013.26020617, 0.00152995)
    ops.section('Aggregator', 1546991, 1546990, 'Mz')
    ops.section('Aggregator', 1546992, 1546991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1546, 1546991, 0.39685995054, 1546992, 0.39685995054, 1546990)
    # Create element
    ops.element('forceBeamColumn', 1546, 546, 646, 1546, 1546)

    # Create geometric transformation
    ops.geomTransf('Linear', 1646, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1646990, 207.9164235, 0.01015314, 251.13104553, 0.08556732, 25.11310455, 0.30022916, -214.56072033, -0.01031697, -259.15633368, -0.08642701, -25.91563337, -0.30108885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1646991, 140.3143497, 0.00960688, 169.47814295, 0.08245614, 16.9478143, 0.29711798, -214.50517753, -0.01042375, -259.08924652, -0.09096802, -25.90892465, -0.30562986, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1646990, 32408658.27734364, 0.1125, 0.00189844, 0.00058594, 13503607.61555985, 0.00152995)
    ops.section('Aggregator', 1646991, 1646990, 'Mz')
    ops.section('Aggregator', 1646992, 1646991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1646, 1646991, 0.46584898742, 1646992, 0.46584898742, 1646990)
    # Create element
    ops.element('forceBeamColumn', 1646, 646, 746, 1646, 1646)

    # Create geometric transformation
    ops.geomTransf('Linear', 1056, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1056990, 139.51041344, 0.00960324, 167.80027283, 0.06007168, 16.78002728, 0.23028494, -139.51041344, -0.00960324, -167.80027283, -0.06007168, -16.78002728, -0.23028494, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1056991, 206.54922398, 0.010062, 248.43318345, 0.06273232, 24.84331835, 0.23170612, -206.54922398, -0.010062, -248.43318345, -0.06273232, -24.84331835, -0.23170612, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1056990, 33552198.85687022, 0.1125, 0.00189844, 0.00058594, 13980082.85702926, 0.00152995)
    ops.section('Aggregator', 1056991, 1056990, 'Mz')
    ops.section('Aggregator', 1056992, 1056991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1056, 1056991, 0.46403292311, 1056992, 0.46403292311, 1056990)
    # Create element
    ops.element('forceBeamColumn', 1056, 56, 156, 1056, 1056)

    # Create geometric transformation
    ops.geomTransf('Linear', 1156, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1156990, 206.23290041, 0.00996913, 249.0358573, 0.11748001, 24.90358573, 0.37111523, -206.23290041, -0.00996913, -249.0358573, -0.11748001, -24.90358573, -0.37111523, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1156991, 206.23290041, 0.00996913, 249.0358573, 0.11781012, 24.90358573, 0.37144534, -206.23290041, -0.00996913, -249.0358573, -0.11781012, -24.90358573, -0.37144534, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1156990, 32478749.30693726, 0.1125, 0.00189844, 0.00058594, 13532812.21122386, 0.00152995)
    ops.section('Aggregator', 1156991, 1156990, 'Mz')
    ops.section('Aggregator', 1156992, 1156991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1156, 1156991, 0.39426701064, 1156992, 0.39426701064, 1156990)
    # Create element
    ops.element('forceBeamColumn', 1156, 156, 256, 1156, 1156)

    # Create geometric transformation
    ops.geomTransf('Linear', 1256, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1256990, 206.62924971, 0.01010415, 248.35472394, 0.07532985, 24.83547239, 0.28860796, -206.62924971, -0.01010415, -248.35472394, -0.07532985, -24.83547239, -0.28860796, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1256991, 206.62924971, 0.01010415, 248.35472394, 0.07588543, 24.83547239, 0.29108608, -206.62924971, -0.01010415, -248.35472394, -0.07588543, -24.83547239, -0.29108608, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1256990, 33734853.39873993, 0.1125, 0.00189844, 0.00058594, 14056188.91614164, 0.00152995)
    ops.section('Aggregator', 1256991, 1256990, 'Mz')
    ops.section('Aggregator', 1256992, 1256991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1256, 1256991, 0.46468260878, 1256992, 0.46468260878, 1256990)
    # Create element
    ops.element('forceBeamColumn', 1256, 256, 356, 1256, 1256)

    # Create geometric transformation
    ops.geomTransf('Linear', 1356, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1356990, 210.19681812, 0.01005561, 252.92426756, 0.1145622, 25.29242676, 0.3656325, -210.19681812, -0.01005561, -252.92426756, -0.1145622, -25.29242676, -0.3656325, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1356991, 210.19681812, 0.01005561, 252.92426756, 0.11301766, 25.29242676, 0.36408797, -210.19681812, -0.01005561, -252.92426756, -0.11301766, -25.29242676, -0.36408797, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1356990, 33444466.44466048, 0.1125, 0.00189844, 0.00058594, 13935194.35194187, 0.00152995)
    ops.section('Aggregator', 1356991, 1356990, 'Mz')
    ops.section('Aggregator', 1356992, 1356991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1356, 1356991, 0.39829481423, 1356992, 0.39829481423, 1356990)
    # Create element
    ops.element('forceBeamColumn', 1356, 356, 456, 1356, 1356)

    # Create geometric transformation
    ops.geomTransf('Linear', 1456, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1456990, 209.09759018, 0.00998065, 252.6416901, 0.07796368, 25.26416901, 0.29287523, -209.09759018, -0.00998065, -252.6416901, -0.07796368, -25.26416901, -0.29287523, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1456991, 209.09759018, 0.00998065, 252.6416901, 0.07845831, 25.26416901, 0.29387796, -209.09759018, -0.00998065, -252.6416901, -0.07845831, -25.26416901, -0.29387796, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1456990, 32314114.49498385, 0.1125, 0.00189844, 0.00058594, 13464214.37290994, 0.00152995)
    ops.section('Aggregator', 1456991, 1456990, 'Mz')
    ops.section('Aggregator', 1456992, 1456991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1456, 1456991, 0.46421021553999997, 1456992, 0.46421021553999997, 1456990)
    # Create element
    ops.element('forceBeamColumn', 1456, 456, 556, 1456, 1456)

    # Create geometric transformation
    ops.geomTransf('Linear', 1556, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1556990, 203.14876566, 0.0100364, 243.59258579, 0.11106016, 24.35925858, 0.36505426, -203.14876566, -0.0100364, -243.59258579, -0.11106016, -24.35925858, -0.36505426, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1556991, 203.14876566, 0.0100364, 243.59258579, 0.11183101, 24.35925858, 0.36582512, -203.14876566, -0.0100364, -243.59258579, -0.11183101, -24.35925858, -0.36582512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1556990, 34334871.41710211, 0.1125, 0.00189844, 0.00058594, 14306196.42379254, 0.00152995)
    ops.section('Aggregator', 1556991, 1556990, 'Mz')
    ops.section('Aggregator', 1556992, 1556991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1556, 1556991, 0.39370992136, 1556992, 0.39370992136, 1556990)
    # Create element
    ops.element('forceBeamColumn', 1556, 556, 656, 1556, 1556)

    # Create geometric transformation
    ops.geomTransf('Linear', 1656, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1656990, 210.6139978, 0.01004292, 253.66412154, 0.06322117, 25.36641215, 0.23338794, -210.6139978, -0.01004292, -253.66412154, -0.06322117, -25.36641215, -0.23338794, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1656991, 142.14372996, 0.00958874, 171.19832855, 0.05984521, 17.11983286, 0.22573742, -142.14372996, -0.00958874, -171.19832855, -0.05984521, -17.11983286, -0.22573742, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1656990, 33195227.94338664, 0.1125, 0.00189844, 0.00058594, 13831344.9764111, 0.00152995)
    ops.section('Aggregator', 1656991, 1656990, 'Mz')
    ops.section('Aggregator', 1656992, 1656991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1656, 1656991, 0.46631250995, 1656992, 0.46631250995, 1656990)
    # Create element
    ops.element('forceBeamColumn', 1656, 656, 756, 1656, 1656)

    # Create geometric transformation
    ops.geomTransf('Linear', 1007, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1007990, 77.22499596, 0.00885784, 92.47569926, 0.06335163, 9.24756993, 0.28360916, -134.4649887, -0.00952801, -161.01967635, -0.07155339, -16.10196763, -0.29181093, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1007991, 102.20775999, 0.00910297, 122.39216017, 0.06361276, 12.23921602, 0.27975673, -134.43607438, -0.00949776, -160.98505191, -0.06765258, -16.09850519, -0.28379654, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1007990, 34662100.58061712, 0.1125, 0.00189844, 0.00058594, 14442541.90859047, 0.00152995)
    ops.section('Aggregator', 1007991, 1007990, 'Mz')
    ops.section('Aggregator', 1007992, 1007991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1007, 1007991, 0.35796196259, 1007992, 0.35796196259, 1007990)
    # Create element
    ops.element('forceBeamColumn', 1007, 7, 107, 1007, 1007)

    # Create geometric transformation
    ops.geomTransf('Linear', 1107, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1107990, 99.38673142, 0.00894987, 120.06004897, 0.08256299, 12.0060049, 0.35890155, -130.69616155, -0.00935166, -157.88211697, -0.08788724, -15.7882117, -0.36422579, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1107991, 99.38673142, 0.00894987, 120.06004897, 0.08241573, 12.0060049, 0.35744476, -130.69616155, -0.00935166, -157.88211697, -0.08773013, -15.7882117, -0.36275916, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1107990, 32370429.38328198, 0.1125, 0.00189844, 0.00058594, 13487678.90970083, 0.00152995)
    ops.section('Aggregator', 1107991, 1107990, 'Mz')
    ops.section('Aggregator', 1107992, 1107991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1107, 1107991, 0.28611776831999997, 1107992, 0.28611776831999997, 1107990)
    # Create element
    ops.element('forceBeamColumn', 1107, 107, 207, 1107, 1107)

    # Create geometric transformation
    ops.geomTransf('Linear', 1207, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1207990, 104.08536281, 0.00920766, 126.06166733, 0.067687, 12.60616673, 0.28633845, -136.84459119, -0.0096285, -165.73759138, -0.07201832, -16.57375914, -0.29066977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1207991, 104.08536281, 0.00920766, 126.06166733, 0.06737284, 12.60616673, 0.28324816, -136.84459119, -0.0096285, -165.73759138, -0.07168314, -16.57375914, -0.28755847, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1207990, 31615009.65608818, 0.1125, 0.00189844, 0.00058594, 13172920.69003674, 0.00152995)
    ops.section('Aggregator', 1207991, 1207990, 'Mz')
    ops.section('Aggregator', 1207992, 1207991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1207, 1207991, 0.35992312416, 1207992, 0.35992312416, 1207990)
    # Create element
    ops.element('forceBeamColumn', 1207, 207, 307, 1207, 1207)

    # Create geometric transformation
    ops.geomTransf('Linear', 1307, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1307990, 102.02762121, 0.00893126, 122.11336998, 0.07599296, 12.211337, 0.3456323, -134.18965289, -0.0093197, -160.6070056, -0.08086576, -16.06070056, -0.35050511, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1307991, 102.02762121, 0.00893126, 122.11336998, 0.07635733, 12.211337, 0.34948485, -134.18965289, -0.0093197, -160.6070056, -0.0812545, -16.06070056, -0.35438202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1307990, 34786690.36647946, 0.1125, 0.00189844, 0.00058594, 14494454.31936644, 0.00152995)
    ops.section('Aggregator', 1307991, 1307990, 'Mz')
    ops.section('Aggregator', 1307992, 1307991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1307, 1307991, 0.28840160755, 1307992, 0.28840160755, 1307990)
    # Create element
    ops.element('forceBeamColumn', 1307, 307, 407, 1307, 1307)

    # Create geometric transformation
    ops.geomTransf('Linear', 1407, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1407990, 102.15292064, 0.00909158, 123.25279033, 0.06759782, 12.32527903, 0.29024741, -134.33151679, -0.00949873, -162.07793345, -0.07191724, -16.20779335, -0.29456683, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1407991, 102.15292064, 0.00909158, 123.25279033, 0.06686432, 12.32527903, 0.28294935, -134.33151679, -0.00949873, -162.07793345, -0.07113469, -16.20779335, -0.28721972, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1407990, 32709263.24198916, 0.1125, 0.00189844, 0.00058594, 13628859.68416215, 0.00152995)
    ops.section('Aggregator', 1407991, 1407990, 'Mz')
    ops.section('Aggregator', 1407992, 1407991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1407, 1407991, 0.35756770051000003, 1407992, 0.35756770051000003, 1407990)
    # Create element
    ops.element('forceBeamColumn', 1407, 407, 507, 1407, 1407)

    # Create geometric transformation
    ops.geomTransf('Linear', 1507, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1507990, 102.40018698, 0.00901637, 123.39470447, 0.07838546, 12.33947045, 0.34593036, -134.65337223, -0.00941899, -162.26057356, -0.08342674, -16.22605736, -0.35097165, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1507991, 102.40018698, 0.00901637, 123.39470447, 0.0793984, 12.33947045, 0.35630343, -134.65337223, -0.00941899, -162.26057356, -0.08450741, -16.22605736, -0.36141244, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1507990, 33056350.15480347, 0.1125, 0.00189844, 0.00058594, 13773479.23116811, 0.00152995)
    ops.section('Aggregator', 1507991, 1507990, 'Mz')
    ops.section('Aggregator', 1507992, 1507991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1507, 1507991, 0.28918519678000004, 1507992, 0.28918519678000004, 1507990)
    # Create element
    ops.element('forceBeamColumn', 1507, 507, 607, 1507, 1507)

    # Create geometric transformation
    ops.geomTransf('Linear', 1607, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1607990, 101.08060698, 0.00903854, 121.90446501, 0.06614298, 12.1904465, 0.28452542, -132.92703007, -0.00944194, -160.31164603, -0.07036491, -16.0311646, -0.28874736, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1607991, 76.37384633, 0.00878889, 92.1078054, 0.06526822, 9.21078054, 0.28222253, -132.94583797, -0.00947466, -160.33432859, -0.07376, -16.03343286, -0.29071432, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1607990, 32832751.23275715, 0.1125, 0.00189844, 0.00058594, 13680313.01364882, 0.00152995)
    ops.section('Aggregator', 1607991, 1607990, 'Mz')
    ops.section('Aggregator', 1607992, 1607991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1607, 1607991, 0.35628144044, 1607992, 0.35628144044, 1607990)
    # Create element
    ops.element('forceBeamColumn', 1607, 607, 707, 1607, 1607)

    # Create geometric transformation
    ops.geomTransf('Linear', 1017, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1017990, 91.21842361, 0.00917553, 109.92904979, 0.06469009, 10.99290498, 0.25309329, -139.98615132, -0.00976728, -168.69996202, -0.0711458, -16.8699962, -0.259549, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1017991, 91.21842361, 0.00917553, 109.92904979, 0.06467154, 10.99290498, 0.2529255, -139.98615132, -0.00976728, -168.69996202, -0.07112529, -16.8699962, -0.25937925, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1017990, 33035060.70176668, 0.1125, 0.00189844, 0.00058594, 13764608.62573612, 0.00152995)
    ops.section('Aggregator', 1017991, 1017990, 'Mz')
    ops.section('Aggregator', 1017992, 1017991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1017, 1017991, 0.41249576328000004, 1017992, 0.41249576328000004, 1017990)
    # Create element
    ops.element('forceBeamColumn', 1017, 17, 117, 1017, 1017)

    # Create geometric transformation
    ops.geomTransf('Linear', 1117, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1117990, 91.96489185, 0.00916035, 111.00557462, 0.07671662, 11.10055746, 0.30369356, -141.1209961, -0.00975768, -170.33910385, -0.08444986, -17.03391038, -0.31142681, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1117991, 91.96489185, 0.00916035, 111.00557462, 0.07708285, 11.10055746, 0.30698945, -141.1209961, -0.00975768, -170.33910385, -0.08485478, -17.03391038, -0.31476138, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1117990, 32595916.40036874, 0.1125, 0.00189844, 0.00058594, 13581631.83348698, 0.00152995)
    ops.section('Aggregator', 1117991, 1117990, 'Mz')
    ops.section('Aggregator', 1117992, 1117991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1117, 1117991, 0.34517945956, 1117992, 0.34517945956, 1117990)
    # Create element
    ops.element('forceBeamColumn', 1117, 117, 217, 1117, 1117)

    # Create geometric transformation
    ops.geomTransf('Linear', 1217, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1217990, 92.07965462, 0.00903115, 110.86913185, 0.06466449, 11.08691318, 0.25437908, -141.30183589, -0.00961602, -170.13543262, -0.07112587, -17.01354326, -0.26084046, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1217991, 136.60967246, 0.00944248, 164.48580145, 0.07224435, 16.44858015, 0.31496514, -141.29098913, -0.0095576, -170.12237251, -0.07293896, -17.01223725, -0.31565975, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1217990, 33272061.24631007, 0.1125, 0.00189844, 0.00058594, 13863358.8526292, 0.00152995)
    ops.section('Aggregator', 1217991, 1217990, 'Mz')
    ops.section('Aggregator', 1217992, 1217991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1217, 1217991, 0.41199602191, 1217992, 0.41199602191, 1217990)
    # Create element
    ops.element('forceBeamColumn', 1217, 217, 317, 1217, 1217)

    # Create geometric transformation
    ops.geomTransf('Linear', 1317, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1317990, 138.6846084, 0.00947028, 167.85034435, 0.09807533, 16.78503444, 0.38742604, -143.41894734, -0.00958731, -173.58032715, -0.09900994, -17.35803271, -0.38836065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1317991, 138.75509082, 0.00937847, 167.93564941, 0.10004177, 16.79356494, 0.38939248, -212.26080225, -0.01016134, -256.89980424, -0.11040133, -25.68998042, -0.39975205, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1317990, 31820480.48899851, 0.1125, 0.00189844, 0.00058594, 13258533.53708271, 0.00152995)
    ops.section('Aggregator', 1317991, 1317990, 'Mz')
    ops.section('Aggregator', 1317992, 1317991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1317, 1317991, 0.34560135895000005, 1317992, 0.34560135895000005, 1317990)
    # Create element
    ops.element('forceBeamColumn', 1317, 317, 417, 1317, 1317)

    # Create geometric transformation
    ops.geomTransf('Linear', 1417, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1417990, 135.48427223, 0.00945201, 163.95961668, 0.08578654, 16.39596167, 0.32861444, -207.40095831, -0.01023328, -250.99135909, -0.09463096, -25.09913591, -0.33745887, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1417991, 91.37317545, 0.00911312, 110.57749047, 0.08234423, 11.05774905, 0.32517213, -140.19678761, -0.00971516, -169.6625828, -0.0906816, -16.96625828, -0.33350951, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1417990, 31851747.73390201, 0.1125, 0.00189844, 0.00058594, 13271561.5557925, 0.00152995)
    ops.section('Aggregator', 1417991, 1417990, 'Mz')
    ops.section('Aggregator', 1417992, 1417991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1417, 1417991, 0.41181428597, 1417992, 0.41181428597, 1417990)
    # Create element
    ops.element('forceBeamColumn', 1417, 417, 517, 1417, 1417)

    # Create geometric transformation
    ops.geomTransf('Linear', 1517, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1517990, 92.58252777, 0.00886413, 111.83320714, 0.07736731, 11.18332071, 0.30569833, -142.00955092, -0.00945165, -171.53758821, -0.08519077, -17.15375882, -0.3135218, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1517991, 92.58252777, 0.00886413, 111.83320714, 0.0775453, 11.18332071, 0.3072861, -142.00955092, -0.00945165, -171.53758821, -0.08538756, -17.15375882, -0.31512836, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1517990, 32388977.21681993, 0.1125, 0.00189844, 0.00058594, 13495407.17367497, 0.00152995)
    ops.section('Aggregator', 1517991, 1517990, 'Mz')
    ops.section('Aggregator', 1517992, 1517991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1517, 1517991, 0.34254852656, 1517992, 0.34254852656, 1517990)
    # Create element
    ops.element('forceBeamColumn', 1517, 517, 617, 1517, 1517)

    # Create geometric transformation
    ops.geomTransf('Linear', 1617, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1617990, 91.52373091, 0.0091551, 110.45522533, 0.06482654, 11.04552253, 0.25209331, -140.44660525, -0.00975078, -169.49769503, -0.07130275, -16.9497695, -0.25856951, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1617991, 91.52373091, 0.0091551, 110.45522533, 0.06495618, 11.04552253, 0.253259, -140.44660525, -0.00975078, -169.49769503, -0.07144608, -16.9497695, -0.2597489, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1617990, 32641027.3739432, 0.1125, 0.00189844, 0.00058594, 13600428.07247633, 0.00152995)
    ops.section('Aggregator', 1617991, 1617990, 'Mz')
    ops.section('Aggregator', 1617992, 1617991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1617, 1617991, 0.41258831316, 1617992, 0.41258831316, 1617990)
    # Create element
    ops.element('forceBeamColumn', 1617, 617, 717, 1617, 1617)

    # Create geometric transformation
    ops.geomTransf('Linear', 1027, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1027990, 77.00260714, 0.00871449, 92.88378118, 0.07330161, 9.28837812, 0.29108591, -138.66399501, -0.00951103, -167.26233887, -0.08370308, -16.72623389, -0.30148738, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1027991, 77.00260714, 0.00871449, 92.88378118, 0.0735304, 9.28837812, 0.29314911, -138.66399501, -0.00951103, -167.26233887, -0.08396589, -16.72623389, -0.3035846, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1027990, 32780306.05334105, 0.1125, 0.00189844, 0.00058594, 13658460.85555877, 0.00152995)
    ops.section('Aggregator', 1027991, 1027990, 'Mz')
    ops.section('Aggregator', 1027992, 1027991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1027, 1027991, 0.35637640166, 1027992, 0.35637640166, 1027990)
    # Create element
    ops.element('forceBeamColumn', 1027, 27, 127, 1027, 1027)

    # Create geometric transformation
    ops.geomTransf('Linear', 1127, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1127990, 77.63787975, 0.00857733, 93.4065339, 0.08848958, 9.34065339, 0.36216423, -139.79354074, -0.00935761, -168.18633051, -0.10115382, -16.81863305, -0.37482847, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1127991, 77.63787975, 0.00857733, 93.4065339, 0.08818762, 9.34065339, 0.35941563, -139.79354074, -0.00935761, -168.18633051, -0.10080696, -16.81863305, -0.37203497, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1127990, 33481272.2526076, 0.1125, 0.00189844, 0.00058594, 13950530.10525317, 0.00152995)
    ops.section('Aggregator', 1127991, 1127990, 'Mz')
    ops.section('Aggregator', 1127992, 1127991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1127, 1127991, 0.28793920872, 1127992, 0.28793920872, 1127990)
    # Create element
    ops.element('forceBeamColumn', 1127, 127, 227, 1127, 1127)

    # Create geometric transformation
    ops.geomTransf('Linear', 1227, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1227990, 77.82544941, 0.0086528, 93.1200463, 0.08841076, 9.31200463, 0.36857435, -140.19421565, -0.00942119, -167.74579461, -0.10104017, -16.77457946, -0.38120376, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1227991, 103.00960096, 0.00882495, 123.25349719, 0.09008728, 12.32534972, 0.36958722, -207.40614882, -0.00993582, -248.16651016, -0.10578977, -24.81665102, -0.38528971, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1227990, 34855081.01783908, 0.1125, 0.00189844, 0.00058594, 14522950.42409962, 0.00152995)
    ops.section('Aggregator', 1227991, 1227990, 'Mz')
    ops.section('Aggregator', 1227992, 1227991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1227, 1227991, 0.35693431279, 1227992, 0.35693431279, 1227990)
    # Create element
    ops.element('forceBeamColumn', 1227, 227, 327, 1227, 1227)

    # Create geometric transformation
    ops.geomTransf('Linear', 1327, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1327990, 103.19448783, 0.00915341, 124.17896844, 0.11300557, 12.41789684, 0.45583447, -207.83260551, -0.01032198, -250.09512722, -0.13282202, -25.00951272, -0.47565092, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1327991, 103.19448783, 0.00915341, 124.17896844, 0.11268177, 12.41789684, 0.45551067, -207.83260551, -0.01032198, -250.09512722, -0.13244008, -25.00951272, -0.47526899, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1327990, 33427972.1843187, 0.1125, 0.00189844, 0.00058594, 13928321.74346613, 0.00152995)
    ops.section('Aggregator', 1327991, 1327990, 'Mz')
    ops.section('Aggregator', 1327992, 1327991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1327, 1327991, 0.29169069169, 1327992, 0.29169069169, 1327990)
    # Create element
    ops.element('forceBeamColumn', 1327, 327, 427, 1327, 1327)

    # Create geometric transformation
    ops.geomTransf('Linear', 1427, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1427990, 102.13294541, 0.00898764, 123.06084401, 0.09230543, 12.3060844, 0.36964392, -205.63802502, -0.01014488, -247.77498404, -0.10842336, -24.7774984, -0.38576186, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1427991, 77.21864584, 0.00880617, 93.04139513, 0.08950881, 9.30413951, 0.36634982, -139.06923257, -0.00960518, -167.56568673, -0.10230932, -16.75656867, -0.37915033, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1427990, 33082336.37426144, 0.1125, 0.00189844, 0.00058594, 13784306.82260893, 0.00152995)
    ops.section('Aggregator', 1427991, 1427990, 'Mz')
    ops.section('Aggregator', 1427992, 1427991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1427, 1427991, 0.35741484487, 1427992, 0.35741484487, 1427990)
    # Create element
    ops.element('forceBeamColumn', 1427, 427, 527, 1427, 1427)

    # Create geometric transformation
    ops.geomTransf('Linear', 1527, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1527990, 77.30015851, 0.00863772, 93.11890429, 0.08802768, 9.31189043, 0.35789705, -139.19475319, -0.00942536, -167.67964192, -0.1006216, -16.76796419, -0.37049098, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1527991, 77.30015851, 0.00863772, 93.11890429, 0.08905038, 9.31189043, 0.36723925, -139.19475319, -0.00942536, -167.67964192, -0.1017964, -16.76796419, -0.37998527, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1527990, 33142270.44082912, 0.1125, 0.00189844, 0.00058594, 13809279.35034547, 0.00152995)
    ops.section('Aggregator', 1527991, 1527990, 'Mz')
    ops.section('Aggregator', 1527992, 1527991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1527, 1527991, 0.28807330869, 1527992, 0.28807330869, 1527990)
    # Create element
    ops.element('forceBeamColumn', 1527, 527, 627, 1527, 1527)

    # Create geometric transformation
    ops.geomTransf('Linear', 1627, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1627990, 77.91430247, 0.00904464, 93.81844145, 0.07236196, 9.38184415, 0.28960041, -140.32621921, -0.00985849, -168.97009617, -0.08259189, -16.89700962, -0.29983034, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1627991, 77.91430247, 0.00904464, 93.81844145, 0.07289521, 9.38184415, 0.29449869, -140.32621921, -0.00985849, -168.97009617, -0.08320445, -16.89700962, -0.30480793, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1627990, 33257285.40552783, 0.1125, 0.00189844, 0.00058594, 13857202.25230326, 0.00152995)
    ops.section('Aggregator', 1627991, 1627990, 'Mz')
    ops.section('Aggregator', 1627992, 1627991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1627, 1627991, 0.36017146918, 1627992, 0.36017146918, 1627990)
    # Create element
    ops.element('forceBeamColumn', 1627, 627, 727, 1627, 1627)

    # Create geometric transformation
    ops.geomTransf('Linear', 1037, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1037990, 78.3552441, 0.00885877, 94.09102759, 0.07154523, 9.40910276, 0.29010714, -141.13804292, -0.00965282, -169.48225538, -0.08166154, -16.94822554, -0.30022345, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1037991, 78.3552441, 0.00885877, 94.09102759, 0.0716196, 9.40910276, 0.29079716, -141.13804292, -0.00965282, -169.48225538, -0.08174698, -16.94822554, -0.30092454, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1037990, 33970924.37441329, 0.1125, 0.00189844, 0.00058594, 14154551.82267221, 0.00152995)
    ops.section('Aggregator', 1037991, 1037990, 'Mz')
    ops.section('Aggregator', 1037992, 1037991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1037, 1037991, 0.35917250268, 1037992, 0.35917250268, 1037990)
    # Create element
    ops.element('forceBeamColumn', 1037, 37, 137, 1037, 1037)

    # Create geometric transformation
    ops.geomTransf('Linear', 1137, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1137990, 77.48436116, 0.00881204, 93.21636022, 0.0870279, 9.32163602, 0.35597041, -139.55877818, -0.00960671, -167.89402588, -0.09945425, -16.78940259, -0.36839676, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1137991, 77.48436116, 0.00881204, 93.21636022, 0.08691911, 9.32163602, 0.35497518, -139.55877818, -0.00960671, -167.89402588, -0.09932929, -16.78940259, -0.36738535, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1137990, 33496691.12277072, 0.1125, 0.00189844, 0.00058594, 13956954.6344878, 0.00152995)
    ops.section('Aggregator', 1137991, 1137990, 'Mz')
    ops.section('Aggregator', 1137992, 1137991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1137, 1137991, 0.28979299246, 1137992, 0.28979299246, 1137990)
    # Create element
    ops.element('forceBeamColumn', 1137, 137, 237, 1137, 1137)

    # Create geometric transformation
    ops.geomTransf('Linear', 1237, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1237990, 76.31472901, 0.0086886, 92.06012237, 0.09039969, 9.20601224, 0.36798627, -137.43031794, -0.00948162, -165.78519051, -0.10334418, -16.57851905, -0.38093077, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1237991, 100.94799572, 0.00886726, 121.77576937, 0.0944554, 12.17757694, 0.37581462, -203.21932509, -0.01001619, -245.14790499, -0.1109727, -24.5147905, -0.39233191, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1237990, 32762040.92013962, 0.1125, 0.00189844, 0.00058594, 13650850.38339151, 0.00152995)
    ops.section('Aggregator', 1237991, 1237990, 'Mz')
    ops.section('Aggregator', 1237992, 1237991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1237, 1237991, 0.35541754291, 1237992, 0.35541754291, 1237990)
    # Create element
    ops.element('forceBeamColumn', 1237, 237, 337, 1237, 1237)

    # Create geometric transformation
    ops.geomTransf('Linear', 1337, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1337990, 102.87760614, 0.00890578, 123.73200174, 0.11260798, 12.37320017, 0.45817952, -207.09374874, -0.0100483, -249.07387567, -0.13237146, -24.90738757, -0.47794301, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1337991, 102.87760614, 0.00890578, 123.73200174, 0.11229234, 12.37320017, 0.45786388, -207.09374874, -0.0100483, -249.07387567, -0.13199914, -24.90738757, -0.47757069, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1337990, 33567146.30484916, 0.1125, 0.00189844, 0.00058594, 13986310.96035382, 0.00152995)
    ops.section('Aggregator', 1337991, 1337990, 'Mz')
    ops.section('Aggregator', 1337992, 1337991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1337, 1337991, 0.28937567898, 1337992, 0.28937567898, 1337990)
    # Create element
    ops.element('forceBeamColumn', 1337, 337, 437, 1337, 1337)

    # Create geometric transformation
    ops.geomTransf('Linear', 1437, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1437990, 105.7277707, 0.00910519, 128.08273014, 0.0949711, 12.80827301, 0.3719208, -212.60721125, -0.01031868, -257.56063788, -0.11160284, -25.75606379, -0.38855253, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1437991, 79.85855682, 0.00892619, 96.74375913, 0.09272675, 9.67437591, 0.36967644, -143.73523763, -0.00976285, -174.12645258, -0.10602561, -17.41264526, -0.38297531, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1437990, 31540045.58814553, 0.1125, 0.00189844, 0.00058594, 13141685.66172731, 0.00152995)
    ops.section('Aggregator', 1437991, 1437990, 'Mz')
    ops.section('Aggregator', 1437992, 1437991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1437, 1437991, 0.36107640155000004, 1437992, 0.36107640155000004, 1437990)
    # Create element
    ops.element('forceBeamColumn', 1437, 437, 537, 1437, 1437)

    # Create geometric transformation
    ops.geomTransf('Linear', 1537, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1537990, 78.01328545, 0.00906693, 93.98545656, 0.08741164, 9.39854566, 0.35541264, -140.50059834, -0.00988436, -169.26620648, -0.09987992, -16.92662065, -0.36788092, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1537991, 78.01328545, 0.00906693, 93.98545656, 0.08728004, 9.39854566, 0.35421441, -140.50059834, -0.00988436, -169.26620648, -0.09972875, -16.92662065, -0.36666312, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1537990, 33120814.43721087, 0.1125, 0.00189844, 0.00058594, 13800339.34883786, 0.00152995)
    ops.section('Aggregator', 1537991, 1537990, 'Mz')
    ops.section('Aggregator', 1537992, 1537991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1537, 1537991, 0.29245013413, 1537992, 0.29245013413, 1537990)
    # Create element
    ops.element('forceBeamColumn', 1537, 537, 637, 1537, 1537)

    # Create geometric transformation
    ops.geomTransf('Linear', 1637, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1637990, 77.71329746, 0.00888509, 93.13382414, 0.07206541, 9.31338241, 0.29491081, -139.99912765, -0.00967241, -167.77893308, -0.08224845, -16.77789331, -0.30509385, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1637991, 77.71329746, 0.00888509, 93.13382414, 0.07121626, 9.31338241, 0.28702246, -139.99912765, -0.00967241, -167.77893308, -0.08127302, -16.77789331, -0.29707922, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1637990, 34469866.49499127, 0.1125, 0.00189844, 0.00058594, 14362444.37291303, 0.00152995)
    ops.section('Aggregator', 1637991, 1637990, 'Mz')
    ops.section('Aggregator', 1637992, 1637991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1637, 1637991, 0.35874809112000006, 1637992, 0.35874809112000006, 1637990)
    # Create element
    ops.element('forceBeamColumn', 1637, 637, 737, 1637, 1637)

    # Create geometric transformation
    ops.geomTransf('Linear', 1047, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1047990, 90.41134494, 0.00900707, 109.17455742, 0.06718864, 10.91745574, 0.26116221, -138.73466448, -0.00959557, -167.52649352, -0.07392281, -16.75264935, -0.26789638, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1047991, 90.41134494, 0.00900707, 109.17455742, 0.06675842, 10.91745574, 0.25734684, -138.73466448, -0.00959557, -167.52649352, -0.07344714, -16.75264935, -0.26403557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1047990, 32482270.33051851, 0.1125, 0.00189844, 0.00058594, 13534279.30438272, 0.00152995)
    ops.section('Aggregator', 1047991, 1047990, 'Mz')
    ops.section('Aggregator', 1047992, 1047991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1047, 1047991, 0.40957620639, 1047992, 0.40957620639, 1047990)
    # Create element
    ops.element('forceBeamColumn', 1047, 47, 147, 1047, 1047)

    # Create geometric transformation
    ops.geomTransf('Linear', 1147, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1147990, 91.01022289, 0.0089762, 109.82347289, 0.07677588, 10.98234729, 0.3041667, -139.65109594, -0.00956262, -168.51918238, -0.08452393, -16.85191824, -0.31191475, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1147991, 91.01022289, 0.0089762, 109.82347289, 0.07729283, 10.98234729, 0.30881787, -139.65109594, -0.00956262, -168.51918238, -0.08509548, -16.85191824, -0.31662052, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1147990, 32671515.3500814, 0.1125, 0.00189844, 0.00058594, 13613131.39586725, 0.00152995)
    ops.section('Aggregator', 1147991, 1147990, 'Mz')
    ops.section('Aggregator', 1147992, 1147991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1147, 1147991, 0.34199391932, 1147992, 0.34199391932, 1147990)
    # Create element
    ops.element('forceBeamColumn', 1147, 147, 247, 1147, 1147)

    # Create geometric transformation
    ops.geomTransf('Linear', 1247, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1247990, 91.51037629, 0.00881704, 110.0961154, 0.06611949, 11.00961154, 0.26161066, -140.41098305, -0.00938922, -168.92842561, -0.07274449, -16.89284256, -0.26823565, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1247991, 135.79873382, 0.00921773, 163.37942948, 0.07346941, 16.33794295, 0.31800881, -140.44561222, -0.00932971, -168.97008796, -0.07417426, -16.8970088, -0.31871366, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1247990, 33482442.99478295, 0.1125, 0.00189844, 0.00058594, 13951017.9144929, 0.00152995)
    ops.section('Aggregator', 1247991, 1247990, 'Mz')
    ops.section('Aggregator', 1247992, 1247991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1247, 1247991, 0.40893204312000003, 1247992, 0.40893204312000003, 1247990)
    # Create element
    ops.element('forceBeamColumn', 1247, 247, 347, 1247, 1247)

    # Create geometric transformation
    ops.geomTransf('Linear', 1347, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1347990, 135.52621182, 0.00940349, 162.63380309, 0.09535054, 16.26338031, 0.38698506, -140.17871057, -0.00951723, -168.21688223, -0.09625733, -16.82168822, -0.38789185, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1347991, 135.48195845, 0.00932596, 162.58069828, 0.09704963, 16.25806983, 0.38868415, -207.47218085, -0.0100686, -248.97021288, -0.10705846, -24.89702129, -0.39869298, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1347990, 34141026.90867218, 0.1125, 0.00189844, 0.00058594, 14225427.87861341, 0.00152995)
    ops.section('Aggregator', 1347991, 1347990, 'Mz')
    ops.section('Aggregator', 1347992, 1347991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1347, 1347991, 0.34289493774, 1347992, 0.34289493774, 1347990)
    # Create element
    ops.element('forceBeamColumn', 1347, 347, 447, 1347, 1347)

    # Create geometric transformation
    ops.geomTransf('Linear', 1447, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1447990, 136.22326959, 0.00949534, 163.88742593, 0.08320216, 16.38874259, 0.32521092, -208.61627682, -0.01025732, -250.9819704, -0.09174973, -25.09819704, -0.3337585, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1447991, 91.89188226, 0.00915828, 110.55324169, 0.08005856, 11.05532417, 0.32206733, -141.02763332, -0.00974608, -169.66745754, -0.0881355, -16.96674575, -0.33014427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1447990, 33486869.63798828, 0.1125, 0.00189844, 0.00058594, 13952862.34916178, 0.00152995)
    ops.section('Aggregator', 1447991, 1447990, 'Mz')
    ops.section('Aggregator', 1447992, 1447991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1447, 1447991, 0.41320817195000004, 1447992, 0.41320817195000004, 1447990)
    # Create element
    ops.element('forceBeamColumn', 1447, 447, 547, 1447, 1447)

    # Create geometric transformation
    ops.geomTransf('Linear', 1547, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1547990, 93.50067702, 0.00896058, 112.62018614, 0.07674608, 11.26201861, 0.30741306, -143.44581717, -0.00954615, -172.77837064, -0.08449178, -17.27783706, -0.31515875, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1547991, 93.50067702, 0.00896058, 112.62018614, 0.07636745, 11.26201861, 0.30398983, -143.44581717, -0.00954615, -172.77837064, -0.08407315, -17.27783706, -0.31169553, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1547990, 33176905.83851214, 0.1125, 0.00189844, 0.00058594, 13823710.76604673, 0.00152995)
    ops.section('Aggregator', 1547991, 1547990, 'Mz')
    ops.section('Aggregator', 1547992, 1547991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1547, 1547991, 0.34487256158, 1547992, 0.34487256158, 1547990)
    # Create element
    ops.element('forceBeamColumn', 1547, 547, 647, 1547, 1547)

    # Create geometric transformation
    ops.geomTransf('Linear', 1647, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1647990, 89.67515592, 0.0091003, 108.22855888, 0.06763639, 10.82285589, 0.26343052, -137.60912361, -0.00968969, -166.07985775, -0.07440889, -16.60798577, -0.27020303, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1647991, 89.67515592, 0.0091003, 108.22855888, 0.06732777, 10.82285589, 0.26068204, -137.60912361, -0.00968969, -166.07985775, -0.07406767, -16.60798577, -0.26742195, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1647990, 32629993.73132914, 0.1125, 0.00189844, 0.00058594, 13595830.72138714, 0.00152995)
    ops.section('Aggregator', 1647991, 1647990, 'Mz')
    ops.section('Aggregator', 1647992, 1647991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1647, 1647991, 0.40970257623, 1647992, 0.40970257623, 1647990)
    # Create element
    ops.element('forceBeamColumn', 1647, 647, 747, 1647, 1647)

    # Create geometric transformation
    ops.geomTransf('Linear', 1057, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1057990, 78.13447579, 0.00885072, 94.28415354, 0.06723975, 9.42841535, 0.29123489, -135.99937636, -0.00954712, -164.10919703, -0.0760061, -16.4109197, -0.30000125, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1057991, 103.43517324, 0.00910306, 124.81427252, 0.06782519, 12.48142725, 0.29046807, -136.00623901, -0.00951219, -164.11747813, -0.07216103, -16.41174781, -0.29480391, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1057990, 32677272.35094302, 0.1125, 0.00189844, 0.00058594, 13615530.14622626, 0.00152995)
    ops.section('Aggregator', 1057991, 1057990, 'Mz')
    ops.section('Aggregator', 1057992, 1057991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1057, 1057991, 0.35868335467, 1057992, 0.35868335467, 1057990)
    # Create element
    ops.element('forceBeamColumn', 1057, 57, 157, 1057, 1057)

    # Create geometric transformation
    ops.geomTransf('Linear', 1157, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1157990, 103.22658657, 0.00913479, 124.35530026, 0.08082697, 12.43553003, 0.35673482, -135.74632843, -0.00954162, -163.53127612, -0.08602781, -16.35312761, -0.36193566, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1157991, 103.22658657, 0.00913479, 124.35530026, 0.07986222, 12.43553003, 0.34704397, -135.74632843, -0.00954162, -163.53127612, -0.08499854, -16.35312761, -0.3521803, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1157990, 33132814.72431946, 0.1125, 0.00189844, 0.00058594, 13805339.46846644, 0.00152995)
    ops.section('Aggregator', 1157991, 1157990, 'Mz')
    ops.section('Aggregator', 1157992, 1157991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1157, 1157991, 0.29084650655, 1157992, 0.29084650655, 1157990)
    # Create element
    ops.element('forceBeamColumn', 1157, 157, 257, 1157, 1157)

    # Create geometric transformation
    ops.geomTransf('Linear', 1257, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1257990, 104.14785585, 0.0090382, 124.85709749, 0.06474718, 12.48570975, 0.28644992, -136.96174804, -0.00943473, -164.19585585, -0.06886893, -16.41958558, -0.29057167, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1257991, 104.14785585, 0.0090382, 124.85709749, 0.06466058, 12.48570975, 0.28554674, -136.96174804, -0.00943473, -164.19585585, -0.06877655, -16.41958558, -0.2896627, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1257990, 34384394.24646216, 0.1125, 0.00189844, 0.00058594, 14326830.9360259, 0.00152995)
    ops.section('Aggregator', 1257991, 1257990, 'Mz')
    ops.section('Aggregator', 1257992, 1257991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1257, 1257991, 0.35893360137, 1257992, 0.35893360137, 1257990)
    # Create element
    ops.element('forceBeamColumn', 1257, 257, 357, 1257, 1257)

    # Create geometric transformation
    ops.geomTransf('Linear', 1357, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1357990, 102.73103995, 0.00897502, 123.66210793, 0.08039308, 12.36621079, 0.35604512, -135.08553299, -0.00937476, -162.6087088, -0.0855685, -16.26087088, -0.36122054, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1357991, 102.73103995, 0.00897502, 123.66210793, 0.07979151, 12.36621079, 0.3499676, -135.08553299, -0.00937476, -162.6087088, -0.0849267, -16.26087088, -0.35510279, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1357990, 33340640.18703087, 0.1125, 0.00189844, 0.00058594, 13891933.41126286, 0.00152995)
    ops.section('Aggregator', 1357991, 1357990, 'Mz')
    ops.section('Aggregator', 1357992, 1357991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1357, 1357991, 0.28913820872, 1357992, 0.28913820872, 1357990)
    # Create element
    ops.element('forceBeamColumn', 1357, 357, 457, 1357, 1357)

    # Create geometric transformation
    ops.geomTransf('Linear', 1457, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1457990, 103.8288243, 0.0091371, 124.63375066, 0.06389596, 12.46337507, 0.28109476, -136.55046357, -0.00953849, -163.91205952, -0.06795904, -16.39120595, -0.28515784, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1457991, 103.8288243, 0.0091371, 124.63375066, 0.06370639, 12.46337507, 0.27912579, -136.55046357, -0.00953849, -163.91205952, -0.06775679, -16.39120595, -0.28317619, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1457990, 34065580.87319858, 0.1125, 0.00189844, 0.00058594, 14193992.03049941, 0.00152995)
    ops.section('Aggregator', 1457991, 1457990, 'Mz')
    ops.section('Aggregator', 1457992, 1457991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1457, 1457991, 0.35947294953, 1457992, 0.35947294953, 1457990)
    # Create element
    ops.element('forceBeamColumn', 1457, 457, 557, 1457, 1457)

    # Create geometric transformation
    ops.geomTransf('Linear', 1557, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1557990, 104.09339848, 0.00921831, 125.37563634, 0.07929223, 12.53756363, 0.35068493, -136.88782088, -0.00962842, -164.87498632, -0.08438814, -16.48749863, -0.35578084, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1557991, 104.09339848, 0.00921831, 125.37563634, 0.07967003, 12.53756363, 0.35454641, -136.88782088, -0.00962842, -164.87498632, -0.0847912, -16.48749863, -0.35966758, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1557990, 33184023.68910489, 0.1125, 0.00189844, 0.00058594, 13826676.53712704, 0.00152995)
    ops.section('Aggregator', 1557991, 1557990, 'Mz')
    ops.section('Aggregator', 1557992, 1557991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1557, 1557991, 0.29224423976, 1557992, 0.29224423976, 1557990)
    # Create element
    ops.element('forceBeamColumn', 1557, 557, 657, 1557, 1557)

    # Create geometric transformation
    ops.geomTransf('Linear', 1657, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1657990, 103.29312079, 0.00928448, 124.52346712, 0.06717427, 12.45234671, 0.28958179, -135.84156268, -0.00969751, -163.76175135, -0.07145835, -16.37617514, -0.29386586, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1657991, 78.05249859, 0.00902856, 94.09501492, 0.06586968, 9.40950149, 0.28304312, -135.86925031, -0.00973035, -163.79512976, -0.07442749, -16.37951298, -0.29160093, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1657990, 32941203.51418099, 0.1125, 0.00189844, 0.00058594, 13725501.46424208, 0.00152995)
    ops.section('Aggregator', 1657991, 1657990, 'Mz')
    ops.section('Aggregator', 1657992, 1657991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1657, 1657991, 0.36011304402000005, 1657992, 0.36011304402000005, 1657990)
    # Create element
    ops.element('forceBeamColumn', 1657, 657, 757, 1657, 1657)

    # Create geometric transformation
    ops.geomTransf('Linear', 1008, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1008990, 77.09141001, 0.00884044, 92.75151669, 0.06972344, 9.27515167, 0.34980905, -77.09141001, -0.00884044, -92.75151669, -0.06972344, -9.27515167, -0.34980905, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1008991, 77.09141001, 0.00884044, 92.75151669, 0.07002104, 9.27515167, 0.35010666, -77.09141001, -0.00884044, -92.75151669, -0.07002104, -9.27515167, -0.35010666, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1008990, 33474350.67958036, 0.1125, 0.00189844, 0.00058594, 13947646.11649182, 0.00152995)
    ops.section('Aggregator', 1008991, 1008990, 'Mz')
    ops.section('Aggregator', 1008992, 1008991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1008, 1008991, 0.35703368921, 1008992, 0.35703368921, 1008990)
    # Create element
    ops.element('forceBeamColumn', 1008, 8, 108, 1008, 1008)

    # Create geometric transformation
    ops.geomTransf('Linear', 1108, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1108990, 77.22627991, 0.00882037, 93.21604687, 0.08587975, 9.32160469, 0.43202482, -77.22627991, -0.00882037, -93.21604687, -0.08587975, -9.32160469, -0.43202482, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1108991, 77.189017, 0.00879642, 93.17106864, 0.08599236, 9.31710686, 0.42763249, -102.16284987, -0.00908353, -123.31575486, -0.09144151, -12.33157549, -0.43308164, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1108990, 32594086.593676, 0.1125, 0.00189844, 0.00058594, 13580869.41403167, 0.00152995)
    ops.section('Aggregator', 1108991, 1108990, 'Mz')
    ops.section('Aggregator', 1108992, 1108991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1108, 1108991, 0.288896212, 1108992, 0.288896212, 1108990)
    # Create element
    ops.element('forceBeamColumn', 1108, 108, 208, 1108, 1108)

    # Create geometric transformation
    ops.geomTransf('Linear', 1208, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1208990, 78.00925002, 0.00899565, 93.97980834, 0.07003516, 9.39798083, 0.3477279, -103.2502138, -0.00928482, -124.38826551, -0.07440601, -12.43882655, -0.35209875, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1208991, 78.00925002, 0.00899565, 93.97980834, 0.07008603, 9.39798083, 0.34823722, -103.2502138, -0.00928482, -124.38826551, -0.07446028, -12.43882655, -0.35261147, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1208990, 33123069.10840173, 0.1125, 0.00189844, 0.00058594, 13801278.79516739, 0.00152995)
    ops.section('Aggregator', 1208991, 1208990, 'Mz')
    ops.section('Aggregator', 1208992, 1208991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1208, 1208991, 0.35951671351, 1208992, 0.35951671351, 1208990)
    # Create element
    ops.element('forceBeamColumn', 1208, 208, 308, 1208, 1208)

    # Create geometric transformation
    ops.geomTransf('Linear', 1308, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1308990, 77.20710315, 0.00888416, 92.76579209, 0.08257794, 9.27657921, 0.4232111, -102.19288474, -0.00916629, -122.78668039, -0.08778792, -12.27866804, -0.42842108, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1308991, 77.20710315, 0.00888416, 92.76579209, 0.08375569, 9.27657921, 0.42882571, -102.19288474, -0.00916629, -122.78668039, -0.08904442, -12.27866804, -0.43411445, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1308990, 33823739.91541705, 0.1125, 0.00189844, 0.00058594, 14093224.9647571, 0.00152995)
    ops.section('Aggregator', 1308991, 1308990, 'Mz')
    ops.section('Aggregator', 1308992, 1308991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1308, 1308991, 0.28979624939000004, 1308992, 0.28979624939000004, 1308990)
    # Create element
    ops.element('forceBeamColumn', 1308, 308, 408, 1308, 1308)

    # Create geometric transformation
    ops.geomTransf('Linear', 1408, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1408990, 77.10817637, 0.00861225, 93.17606443, 0.07190077, 9.31760644, 0.35184432, -102.04757296, -0.00889745, -123.31236038, -0.07641803, -12.33123604, -0.35636158, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1408991, 77.10817637, 0.00861225, 93.17606443, 0.07173139, 9.31760644, 0.34990096, -102.04757296, -0.00889745, -123.31236038, -0.07623732, -12.33123604, -0.3544069, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1408990, 32282579.04258852, 0.1125, 0.00189844, 0.00058594, 13451074.60107855, 0.00152995)
    ops.section('Aggregator', 1408991, 1408990, 'Mz')
    ops.section('Aggregator', 1408992, 1408991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1408, 1408991, 0.35519088794, 1408992, 0.35519088794, 1408990)
    # Create element
    ops.element('forceBeamColumn', 1408, 408, 508, 1408, 1408)

    # Create geometric transformation
    ops.geomTransf('Linear', 1508, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1508990, 77.22004459, 0.00905304, 93.05311582, 0.08342295, 9.30531158, 0.42175867, -102.1968502, -0.00934232, -123.15112466, -0.08868529, -12.31511247, -0.42702101, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1508991, 77.27443838, 0.00907325, 93.11866242, 0.08346409, 9.31186624, 0.42696152, -77.27443838, -0.00907325, -93.11866242, -0.08346409, -9.31186624, -0.42696152, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1508990, 33053172.27225608, 0.1125, 0.00189844, 0.00058594, 13772155.11344003, 0.00152995)
    ops.section('Aggregator', 1508991, 1508990, 'Mz')
    ops.section('Aggregator', 1508992, 1508991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1508, 1508991, 0.29112299708, 1508992, 0.29112299708, 1508990)
    # Create element
    ops.element('forceBeamColumn', 1508, 508, 608, 1508, 1508)

    # Create geometric transformation
    ops.geomTransf('Linear', 1608, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1608990, 79.69601527, 0.0090061, 95.66200483, 0.06921353, 9.56620048, 0.34600515, -79.69601527, -0.0090061, -95.66200483, -0.06921353, -9.56620048, -0.34600515, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1608991, 79.69601527, 0.0090061, 95.66200483, 0.06849447, 9.56620048, 0.34330241, -79.69601527, -0.0090061, -95.66200483, -0.06849447, -9.56620048, -0.34330241, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1608990, 34074209.34174081, 0.1125, 0.00189844, 0.00058594, 14197587.22572534, 0.00152995)
    ops.section('Aggregator', 1608991, 1608990, 'Mz')
    ops.section('Aggregator', 1608992, 1608991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1608, 1608991, 0.36128261092, 1608992, 0.36128261092, 1608990)
    # Create element
    ops.element('forceBeamColumn', 1608, 608, 708, 1608, 1608)

    # Create geometric transformation
    ops.geomTransf('Linear', 1018, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1018990, 77.7618075, 0.00876675, 93.99626614, 0.07262241, 9.39962661, 0.35277536, -77.7618075, -0.00876675, -93.99626614, -0.07262241, -9.39962661, -0.35277536, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1018991, 77.7618075, 0.00876675, 93.99626614, 0.07216762, 9.39962661, 0.351662, -77.7618075, -0.00876675, -93.99626614, -0.07216762, -9.39962661, -0.351662, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1018990, 32189857.08079821, 0.1125, 0.00189844, 0.00058594, 13412440.45033259, 0.00152995)
    ops.section('Aggregator', 1018991, 1018990, 'Mz')
    ops.section('Aggregator', 1018992, 1018991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1018, 1018991, 0.35694786354, 1018992, 0.35694786354, 1018990)
    # Create element
    ops.element('forceBeamColumn', 1018, 18, 118, 1018, 1018)

    # Create geometric transformation
    ops.geomTransf('Linear', 1118, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1118990, 78.07631404, 0.0090917, 93.7917114, 0.08245943, 9.37917114, 0.42463526, -78.07631404, -0.0090917, -93.7917114, -0.08245943, -9.37917114, -0.42463526, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1118991, 78.02394898, 0.00907156, 93.72880618, 0.08314888, 9.37288062, 0.42532471, -103.2690236, -0.00935805, -124.05527307, -0.08838887, -12.40552731, -0.4305647, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1118990, 33874118.63323915, 0.1125, 0.00189844, 0.00058594, 14114216.09718298, 0.00152995)
    ops.section('Aggregator', 1118991, 1118990, 'Mz')
    ops.section('Aggregator', 1118992, 1118991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1118, 1118991, 0.29224740702999996, 1118992, 0.29224740702999996, 1118990)
    # Create element
    ops.element('forceBeamColumn', 1118, 118, 218, 1118, 1118)

    # Create geometric transformation
    ops.geomTransf('Linear', 1218, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1218990, 76.91306553, 0.008764, 92.72426718, 0.07133285, 9.27242672, 0.35194236, -101.80015177, -0.00904822, -122.72745089, -0.075801, -12.27274509, -0.35641052, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1218991, 76.91306553, 0.008764, 92.72426718, 0.0712944, 9.27242672, 0.35190392, -101.80015177, -0.00904822, -122.72745089, -0.07575999, -12.27274509, -0.35636951, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1218990, 32932730.4252723, 0.1125, 0.00189844, 0.00058594, 13721971.01053013, 0.00152995)
    ops.section('Aggregator', 1218991, 1218990, 'Mz')
    ops.section('Aggregator', 1218992, 1218991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1218, 1218991, 0.35636709831, 1218992, 0.35636709831, 1218990)
    # Create element
    ops.element('forceBeamColumn', 1218, 218, 318, 1218, 1218)

    # Create geometric transformation
    ops.geomTransf('Linear', 1318, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1318990, 75.27258089, 0.00882528, 90.94879845, 0.08700034, 9.09487985, 0.43297983, -99.61705819, -0.00911133, -120.36324038, -0.0925139, -12.03632404, -0.4384934, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1318991, 75.27258089, 0.00882528, 90.94879845, 0.08752029, 9.09487985, 0.43591262, -99.61705819, -0.00911133, -120.36324038, -0.09306863, -12.03632404, -0.44146096, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1318990, 32311375.27593573, 0.1125, 0.00189844, 0.00058594, 13463073.03163989, 0.00152995)
    ops.section('Aggregator', 1318991, 1318990, 'Mz')
    ops.section('Aggregator', 1318992, 1318991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1318, 1318991, 0.28703271923, 1318992, 0.28703271923, 1318990)
    # Create element
    ops.element('forceBeamColumn', 1318, 318, 418, 1318, 1318)

    # Create geometric transformation
    ops.geomTransf('Linear', 1418, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1418990, 77.47897337, 0.00879553, 93.51473748, 0.0716109, 9.35147375, 0.3515667, -102.54650533, -0.00908299, -123.77047744, -0.07609877, -12.37704774, -0.35605457, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1418991, 77.47897337, 0.00879553, 93.51473748, 0.07202887, 9.35147375, 0.35198467, -102.54650533, -0.00908299, -123.77047744, -0.0765447, -12.37704774, -0.35650049, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1418990, 32612983.76917143, 0.1125, 0.00189844, 0.00058594, 13588743.23715476, 0.00152995)
    ops.section('Aggregator', 1418991, 1418990, 'Mz')
    ops.section('Aggregator', 1418992, 1418991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1418, 1418991, 0.35719924572, 1418992, 0.35719924572, 1418990)
    # Create element
    ops.element('forceBeamColumn', 1418, 418, 518, 1418, 1418)

    # Create geometric transformation
    ops.geomTransf('Linear', 1518, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1518990, 79.17805976, 0.00903408, 94.96887426, 0.08069214, 9.49688743, 0.41798703, -104.80675474, -0.00931972, -125.708808, -0.08576951, -12.5708808, -0.4230644, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1518991, 79.2219279, 0.00905601, 95.02149121, 0.080927, 9.50214912, 0.42195854, -79.2219279, -0.00905601, -95.02149121, -0.080927, -9.50214912, -0.42195854, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1518990, 34262512.82812946, 0.1125, 0.00189844, 0.00058594, 14276047.01172061, 0.00152995)
    ops.section('Aggregator', 1518991, 1518990, 'Mz')
    ops.section('Aggregator', 1518992, 1518991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1518, 1518991, 0.29322800883000005, 1518992, 0.29322800883000005, 1518990)
    # Create element
    ops.element('forceBeamColumn', 1518, 518, 618, 1518, 1518)

    # Create geometric transformation
    ops.geomTransf('Linear', 1618, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1618990, 78.09071666, 0.00885147, 93.79335789, 0.06799841, 9.37933579, 0.34441002, -78.09071666, -0.00885147, -93.79335789, -0.06799841, -9.37933579, -0.34441002, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1618991, 78.09071666, 0.00885147, 93.79335789, 0.06873232, 9.37933579, 0.34787185, -78.09071666, -0.00885147, -93.79335789, -0.06873232, -9.37933579, -0.34787185, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1618990, 33916719.84886967, 0.1125, 0.00189844, 0.00058594, 14131966.60369569, 0.00152995)
    ops.section('Aggregator', 1618991, 1618990, 'Mz')
    ops.section('Aggregator', 1618992, 1618991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1618, 1618991, 0.35824377664999996, 1618992, 0.35824377664999996, 1618990)
    # Create element
    ops.element('forceBeamColumn', 1618, 618, 718, 1618, 1618)

    # Create geometric transformation
    ops.geomTransf('Linear', 1028, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1028990, 78.92852494, 0.00888565, 94.88175825, 0.07004096, 9.48817583, 0.34828868, -78.92852494, -0.00888565, -94.88175825, -0.07004096, -9.48817583, -0.34828868, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1028991, 78.8974991, 0.00886135, 94.8444614, 0.0702186, 9.48444614, 0.34846631, -104.43154749, -0.00914641, -125.5395163, -0.07460657, -12.55395163, -0.35285429, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1028990, 33694318.59379384, 0.1125, 0.00189844, 0.00058594, 14039299.41408077, 0.00152995)
    ops.section('Aggregator', 1028991, 1028990, 'Mz')
    ops.section('Aggregator', 1028992, 1028991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1028, 1028991, 0.3593919915, 1028992, 0.3593919915, 1028990)
    # Create element
    ops.element('forceBeamColumn', 1028, 28, 128, 1028, 1028)

    # Create geometric transformation
    ops.geomTransf('Linear', 1128, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1128990, 77.07596649, 0.00885827, 92.96073347, 0.08561722, 9.29607335, 0.43067481, -102.01403759, -0.00914513, -123.03835024, -0.0910369, -12.30383502, -0.43609448, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1128991, 77.07596649, 0.00885827, 92.96073347, 0.08560215, 9.29607335, 0.43049914, -102.01403759, -0.00914513, -123.03835024, -0.09102083, -12.30383502, -0.43591781, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1128990, 32814512.16139767, 0.1125, 0.00189844, 0.00058594, 13672713.40058236, 0.00152995)
    ops.section('Aggregator', 1128991, 1128990, 'Mz')
    ops.section('Aggregator', 1128992, 1128991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1128, 1128991, 0.28932347642, 1128992, 0.28932347642, 1128990)
    # Create element
    ops.element('forceBeamColumn', 1128, 128, 228, 1128, 1128)

    # Create geometric transformation
    ops.geomTransf('Linear', 1228, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1228990, 79.94893526, 0.00911689, 96.29098287, 0.06950889, 9.62909829, 0.3452722, -105.82024738, -0.009411, -127.45054822, -0.07384137, -12.74505482, -0.34960467, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1228991, 79.94893526, 0.00911689, 96.29098287, 0.0693127, 9.62909829, 0.34391632, -105.82024738, -0.009411, -127.45054822, -0.07363206, -12.74505482, -0.34823568, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1228990, 33194535.16964265, 0.1125, 0.00189844, 0.00058594, 13831056.32068444, 0.00152995)
    ops.section('Aggregator', 1228991, 1228990, 'Mz')
    ops.section('Aggregator', 1228992, 1228991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1228, 1228991, 0.36262983303, 1228992, 0.36262983303, 1228990)
    # Create element
    ops.element('forceBeamColumn', 1228, 228, 328, 1228, 1228)

    # Create geometric transformation
    ops.geomTransf('Linear', 1328, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1328990, 78.01589062, 0.00896998, 93.92433238, 0.0841823, 9.39243324, 0.42743585, -103.26090219, -0.00925772, -124.31712594, -0.08949944, -12.43171259, -0.43275298, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1328991, 78.01589062, 0.00896998, 93.92433238, 0.08477257, 9.39243324, 0.42802611, -103.26090219, -0.00925772, -124.31712594, -0.09012917, -12.43171259, -0.43338272, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1328990, 33303891.64743691, 0.1125, 0.00189844, 0.00058594, 13876621.51976538, 0.00152995)
    ops.section('Aggregator', 1328991, 1328990, 'Mz')
    ops.section('Aggregator', 1328992, 1328991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1328, 1328991, 0.29132983587, 1328992, 0.29132983587, 1328990)
    # Create element
    ops.element('forceBeamColumn', 1328, 328, 428, 1328, 1328)

    # Create geometric transformation
    ops.geomTransf('Linear', 1428, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1428990, 76.85526331, 0.00874471, 91.96309145, 0.06987934, 9.19630914, 0.35049828, -101.73605869, -0.00901864, -121.73483072, -0.0742413, -12.17348307, -0.35486023, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1428991, 76.85526331, 0.00874471, 91.96309145, 0.06887831, 9.19630914, 0.34546038, -101.73605869, -0.00901864, -121.73483072, -0.07317333, -12.17348307, -0.3497554, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1428990, 34844944.36065159, 0.1125, 0.00189844, 0.00058594, 14518726.81693816, 0.00152995)
    ops.section('Aggregator', 1428991, 1428990, 'Mz')
    ops.section('Aggregator', 1428992, 1428991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1428, 1428991, 0.35635513794, 1428992, 0.35635513794, 1428990)
    # Create element
    ops.element('forceBeamColumn', 1428, 428, 528, 1428, 1428)

    # Create geometric transformation
    ops.geomTransf('Linear', 1528, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1528990, 77.39502147, 0.00876762, 93.00191112, 0.0836463, 9.30019111, 0.42836106, -102.44442386, -0.0090481, -123.10258492, -0.08893386, -12.31025849, -0.43364863, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1528991, 77.39502147, 0.00876762, 93.00191112, 0.08434354, 9.30019111, 0.43035147, -102.44442386, -0.0090481, -123.10258492, -0.08967773, -12.31025849, -0.43568566, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1528990, 33795213.51706742, 0.1125, 0.00189844, 0.00058594, 14081338.96544476, 0.00152995)
    ops.section('Aggregator', 1528991, 1528990, 'Mz')
    ops.section('Aggregator', 1528992, 1528991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1528, 1528991, 0.28901071713, 1528992, 0.28901071713, 1528990)
    # Create element
    ops.element('forceBeamColumn', 1528, 528, 628, 1528, 1528)

    # Create geometric transformation
    ops.geomTransf('Linear', 1628, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1628990, 77.53051512, 0.00890352, 93.41584801, 0.0700933, 9.3415848, 0.3476748, -102.61749119, -0.00919045, -123.64292879, -0.07447196, -12.36429288, -0.35205346, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1628991, 77.57449177, 0.00892602, 93.46883509, 0.06940159, 9.34688351, 0.34468839, -77.57449177, -0.00892602, -93.46883509, -0.06940159, -9.34688351, -0.34468839, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1628990, 33086155.93770842, 0.1125, 0.00189844, 0.00058594, 13785898.30737851, 0.00152995)
    ops.section('Aggregator', 1628991, 1628990, 'Mz')
    ops.section('Aggregator', 1628992, 1628991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1628, 1628991, 0.35822413131, 1628992, 0.35822413131, 1628990)
    # Create element
    ops.element('forceBeamColumn', 1628, 628, 728, 1628, 1628)

    # Create geometric transformation
    ops.geomTransf('Linear', 1038, 0, -1, 0, '-jntOffset', 0.15, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1038990, 77.67479521, 0.00881737, 93.57771966, 0.07085031, 9.35777197, 0.35063871, -77.67479521, -0.00881737, -93.57771966, -0.07085031, -9.35777197, -0.35063871, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1038991, 77.6399895, 0.00879345, 93.53578794, 0.0711434, 9.35357879, 0.3509318, -102.76351968, -0.00907836, -123.80304075, -0.07559761, -12.38030408, -0.355386, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1038990, 33120657.06374566, 0.1125, 0.00189844, 0.00058594, 13800273.77656069, 0.00152995)
    ops.section('Aggregator', 1038991, 1038990, 'Mz')
    ops.section('Aggregator', 1038992, 1038991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1038, 1038991, 0.35741296573, 1038992, 0.35741296573, 1038990)
    # Create element
    ops.element('forceBeamColumn', 1038, 38, 138, 1038, 1038)

    # Create geometric transformation
    ops.geomTransf('Linear', 1138, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1138990, 78.33597866, 0.00906337, 94.75087223, 0.0852016, 9.47508722, 0.4237672, -103.67520156, -0.00936065, -125.39979641, -0.09059019, -12.53997964, -0.42915579, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1138991, 78.33597866, 0.00906337, 94.75087223, 0.08606274, 9.47508722, 0.42817365, -103.67520156, -0.00936065, -125.39979641, -0.09150892, -12.53997964, -0.43361982, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1138990, 32004510.99299468, 0.1125, 0.00189844, 0.00058594, 13335212.91374779, 0.00152995)
    ops.section('Aggregator', 1138991, 1138990, 'Mz')
    ops.section('Aggregator', 1138992, 1138991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1138, 1138991, 0.29230287175, 1138992, 0.29230287175, 1138990)
    # Create element
    ops.element('forceBeamColumn', 1138, 138, 238, 1138, 1138)

    # Create geometric transformation
    ops.geomTransf('Linear', 1238, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1238990, 77.72898375, 0.00887975, 93.66618597, 0.07209651, 9.3666186, 0.35124436, -102.88079636, -0.00916675, -123.97501345, -0.07661076, -12.39750135, -0.35575862, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1238991, 77.72898375, 0.00887975, 93.66618597, 0.07152206, 9.3666186, 0.35066693, -102.88079636, -0.00916675, -123.97501345, -0.0759979, -12.39750135, -0.35514278, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1238990, 33053811.08071245, 0.1125, 0.00189844, 0.00058594, 13772421.28363019, 0.00152995)
    ops.section('Aggregator', 1238991, 1238990, 'Mz')
    ops.section('Aggregator', 1238992, 1238991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1238, 1238991, 0.35823309397, 1238992, 0.35823309397, 1238990)
    # Create element
    ops.element('forceBeamColumn', 1238, 238, 338, 1238, 1238)

    # Create geometric transformation
    ops.geomTransf('Linear', 1338, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.25, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1338990, 78.64620905, 0.00884305, 94.99066228, 0.08793013, 9.49906623, 0.43179246, -104.08733954, -0.00913434, -125.7190326, -0.09350991, -12.57190326, -0.43737225, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1338991, 78.64620905, 0.00884305, 94.99066228, 0.08780447, 9.49906623, 0.43166681, -104.08733954, -0.00913434, -125.7190326, -0.09337585, -12.57190326, -0.43723819, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1338990, 32414195.3801684, 0.1125, 0.00189844, 0.00058594, 13505914.74173683, 0.00152995)
    ops.section('Aggregator', 1338991, 1338990, 'Mz')
    ops.section('Aggregator', 1338992, 1338991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1338, 1338991, 0.29081405516000003, 1338992, 0.29081405516000003, 1338990)
    # Create element
    ops.element('forceBeamColumn', 1338, 338, 438, 1338, 1338)

    # Create geometric transformation
    ops.geomTransf('Linear', 1438, 0, -1, 0, '-jntOffset', 0.25, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1438990, 78.46994031, 0.00888361, 93.98546826, 0.06707399, 9.39854683, 0.3423921, -103.87296769, -0.00916366, -124.41132833, -0.0712452, -12.44113283, -0.34656331, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1438991, 78.46994031, 0.00888361, 93.98546826, 0.06761514, 9.39854683, 0.34598485, -103.87296769, -0.00916366, -124.41132833, -0.07182253, -12.44113283, -0.35019225, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1438990, 34613119.39407305, 0.1125, 0.00189844, 0.00058594, 14422133.08086377, 0.00152995)
    ops.section('Aggregator', 1438991, 1438990, 'Mz')
    ops.section('Aggregator', 1438992, 1438991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1438, 1438991, 0.35923448584, 1438992, 0.35923448584, 1438990)
    # Create element
    ops.element('forceBeamColumn', 1438, 438, 538, 1438, 1438)

    # Create geometric transformation
    ops.geomTransf('Linear', 1538, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1538990, 77.304194, 0.00866565, 92.64403102, 0.08445185, 9.2644031, 0.43153314, -102.32863134, -0.00894073, -122.63418588, -0.08979469, -12.26341859, -0.43687598, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1538991, 77.304194, 0.00866565, 92.64403102, 0.08363387, 9.2644031, 0.42783359, -102.32863134, -0.00894073, -122.63418588, -0.08892201, -12.26341859, -0.43312174, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1538990, 34468573.35119361, 0.1125, 0.00189844, 0.00058594, 14361905.56299734, 0.00152995)
    ops.section('Aggregator', 1538991, 1538990, 'Mz')
    ops.section('Aggregator', 1538992, 1538991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1538, 1538991, 0.28811694522, 1538992, 0.28811694522, 1538990)
    # Create element
    ops.element('forceBeamColumn', 1538, 538, 638, 1538, 1538)

    # Create geometric transformation
    ops.geomTransf('Linear', 1638, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.15, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1638990, 77.7404728, 0.00883497, 93.06744109, 0.06891156, 9.30674411, 0.34819825, -102.90745132, -0.00911246, -123.19622995, -0.07320632, -12.31962299, -0.35249301, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1638991, 77.78226712, 0.00885627, 93.11747539, 0.0677881, 9.31174754, 0.34369556, -77.78226712, -0.00885627, -93.11747539, -0.0677881, -9.31174754, -0.34369556, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1638990, 34728412.42036859, 0.1125, 0.00189844, 0.00058594, 14470171.84182025, 0.00152995)
    ops.section('Aggregator', 1638991, 1638990, 'Mz')
    ops.section('Aggregator', 1638992, 1638991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1638, 1638991, 0.35805501039000004, 1638992, 0.35805501039000004, 1638990)
    # Create element
    ops.element('forceBeamColumn', 1638, 638, 738, 1638, 1638)

    # Create geometric transformation
    ops.geomTransf('Linear', 1048, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1048990, 77.84497358, 0.00879752, 93.904436, 0.0724056, 9.3904436, 0.35222256, -77.84497358, -0.00879752, -93.904436, -0.0724056, -9.3904436, -0.35222256, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1048991, 77.84497358, 0.00879752, 93.904436, 0.07185457, 9.3904436, 0.35167153, -77.84497358, -0.00879752, -93.904436, -0.07185457, -9.3904436, -0.35167153, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1048990, 32766906.68635767, 0.1125, 0.00189844, 0.00058594, 13652877.78598236, 0.00152995)
    ops.section('Aggregator', 1048991, 1048990, 'Mz')
    ops.section('Aggregator', 1048992, 1048991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1048, 1048991, 0.35737647893, 1048992, 0.35737647893, 1048990)
    # Create element
    ops.element('forceBeamColumn', 1048, 48, 148, 1048, 1048)

    # Create geometric transformation
    ops.geomTransf('Linear', 1148, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1148990, 79.39426544, 0.0091126, 95.73335227, 0.0838455, 9.57333523, 0.42430949, -79.39426544, -0.0091126, -95.73335227, -0.0838455, -9.57333523, -0.42430949, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1148991, 79.35150087, 0.00908896, 95.68178688, 0.08405423, 9.56817869, 0.42190105, -105.02683983, -0.00938335, -126.64102877, -0.08936149, -12.66410288, -0.42720831, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1148990, 32881818.98265785, 0.1125, 0.00189844, 0.00058594, 13700757.90944077, 0.00152995)
    ops.section('Aggregator', 1148991, 1148990, 'Mz')
    ops.section('Aggregator', 1148992, 1148991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1148, 1148991, 0.29371681912000003, 1148992, 0.29371681912000003, 1148990)
    # Create element
    ops.element('forceBeamColumn', 1148, 148, 248, 1148, 1148)

    # Create geometric transformation
    ops.geomTransf('Linear', 1248, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.275, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1248990, 77.12866658, 0.00867449, 91.9829878, 0.06822287, 9.19829878, 0.34901788, -102.10460459, -0.00894386, -121.76907775, -0.0724742, -12.17690777, -0.35326921, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1248991, 77.12866658, 0.00867449, 91.9829878, 0.06812715, 9.19829878, 0.34892216, -102.10460459, -0.00894386, -121.76907775, -0.07237208, -12.17690777, -0.35316709, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1248990, 35622562.13639143, 0.1125, 0.00189844, 0.00058594, 14842734.22349643, 0.00152995)
    ops.section('Aggregator', 1248991, 1248990, 'Mz')
    ops.section('Aggregator', 1248992, 1248991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1248, 1248991, 0.35613168416, 1248992, 0.35613168416, 1248990)
    # Create element
    ops.element('forceBeamColumn', 1248, 248, 348, 1248, 1248)

    # Create geometric transformation
    ops.geomTransf('Linear', 1348, 0, -1, 0, '-jntOffset', 0.275, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1348990, 76.73679881, 0.00869957, 92.49807857, 0.08755692, 9.24980786, 0.43521817, -101.56697948, -0.00898211, -122.42822992, -0.09311259, -12.24282299, -0.44077384, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1348991, 76.73679881, 0.00869957, 92.49807857, 0.08757473, 9.24980786, 0.43523598, -101.56697948, -0.00898211, -122.42822992, -0.09313159, -12.24282299, -0.44079284, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1348990, 32973064.55508237, 0.1125, 0.00189844, 0.00058594, 13738776.89795099, 0.00152995)
    ops.section('Aggregator', 1348991, 1348990, 'Mz')
    ops.section('Aggregator', 1348992, 1348991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1348, 1348991, 0.28763630828, 1348992, 0.28763630828, 1348990)
    # Create element
    ops.element('forceBeamColumn', 1348, 348, 448, 1348, 1348)

    # Create geometric transformation
    ops.geomTransf('Linear', 1448, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1448990, 76.91039693, 0.00886702, 92.4932358, 0.06988261, 9.24932358, 0.34937386, -101.79827568, -0.0091496, -122.42365522, -0.07424526, -12.24236552, -0.35373651, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1448991, 76.91039693, 0.00886702, 92.4932358, 0.07020105, 9.24932358, 0.35007319, -101.79827568, -0.0091496, -122.42365522, -0.07458499, -12.24236552, -0.35445713, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1448990, 33588936.06455743, 0.1125, 0.00189844, 0.00058594, 13995390.02689893, 0.00152995)
    ops.section('Aggregator', 1448991, 1448990, 'Mz')
    ops.section('Aggregator', 1448992, 1448991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1448, 1448991, 0.35730601698, 1448992, 0.35730601698, 1448990)
    # Create element
    ops.element('forceBeamColumn', 1448, 448, 548, 1448, 1448)

    # Create geometric transformation
    ops.geomTransf('Linear', 1548, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.2, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1548990, 77.8591674, 0.00876721, 93.56175162, 0.08319429, 9.35617516, 0.42631011, -103.05838665, -0.00904843, -123.84313236, -0.0884524, -12.38431324, -0.43156823, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1548991, 77.89206922, 0.00879079, 93.60128906, 0.08291873, 9.36012891, 0.42834367, -77.89206922, -0.00879079, -93.60128906, -0.08291873, -9.36012891, -0.42834367, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1548990, 33789447.65444377, 0.1125, 0.00189844, 0.00058594, 14078936.52268491, 0.00152995)
    ops.section('Aggregator', 1548991, 1548990, 'Mz')
    ops.section('Aggregator', 1548992, 1548991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1548, 1548991, 0.28949849961, 1548992, 0.28949849961, 1548990)
    # Create element
    ops.element('forceBeamColumn', 1548, 548, 648, 1548, 1548)

    # Create geometric transformation
    ops.geomTransf('Linear', 1648, 0, -1, 0, '-jntOffset', 0.2, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1648990, 78.03779109, 0.00870275, 94.00069581, 0.07076979, 9.40006958, 0.35103117, -78.03779109, -0.00870275, -94.00069581, -0.07076979, -9.40006958, -0.35103117, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1648991, 78.03779109, 0.00870275, 94.00069581, 0.07053552, 9.40006958, 0.35079689, -78.03779109, -0.00870275, -94.00069581, -0.07053552, -9.40006958, -0.35079689, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1648990, 33161688.57715548, 0.1125, 0.00189844, 0.00058594, 13817370.24048145, 0.00152995)
    ops.section('Aggregator', 1648991, 1648990, 'Mz')
    ops.section('Aggregator', 1648992, 1648991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1648, 1648991, 0.35680978357, 1648992, 0.35680978357, 1648990)
    # Create element
    ops.element('forceBeamColumn', 1648, 648, 748, 1648, 1648)

    # Create geometric transformation
    ops.geomTransf('Linear', 1058, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1058990, 78.05967037, 0.008777, 94.11395512, 0.07003188, 9.41139551, 0.34852412, -78.05967037, -0.008777, -94.11395512, -0.07003188, -9.41139551, -0.34852412, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1058991, 78.05967037, 0.008777, 94.11395512, 0.07076323, 9.41139551, 0.35052758, -78.05967037, -0.008777, -94.11395512, -0.07076323, -9.41139551, -0.35052758, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1058990, 32911326.30877657, 0.1125, 0.00189844, 0.00058594, 13713052.62865691, 0.00152995)
    ops.section('Aggregator', 1058991, 1058990, 'Mz')
    ops.section('Aggregator', 1058992, 1058991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1058, 1058991, 0.35744368826, 1058992, 0.35744368826, 1058990)
    # Create element
    ops.element('forceBeamColumn', 1058, 58, 158, 1058, 1058)

    # Create geometric transformation
    ops.geomTransf('Linear', 1158, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1158990, 77.7424851, 0.00893775, 93.22384464, 0.08205682, 9.32238446, 0.42610889, -77.7424851, -0.00893775, -93.22384464, -0.08205682, -9.32238446, -0.42610889, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1158991, 77.6959883, 0.00891693, 93.16808863, 0.08239228, 9.31680886, 0.42452256, -102.8434566, -0.00919783, -123.32333353, -0.08758642, -12.33233335, -0.42971671, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1158990, 34324194.78913687, 0.1125, 0.00189844, 0.00058594, 14301747.82880703, 0.00152995)
    ops.section('Aggregator', 1158991, 1158990, 'Mz')
    ops.section('Aggregator', 1158992, 1158991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1158, 1158991, 0.29065367705, 1158992, 0.29065367705, 1158990)
    # Create element
    ops.element('forceBeamColumn', 1158, 158, 258, 1158, 1158)

    # Create geometric transformation
    ops.geomTransf('Linear', 1258, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1258990, 77.8406646, 0.00907955, 94.02690591, 0.07134501, 9.40269059, 0.34916506, -103.0187982, -0.00937409, -124.44059792, -0.0758032, -12.44405979, -0.35362325, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1258991, 77.8406646, 0.00907955, 94.02690591, 0.07117609, 9.40269059, 0.34782363, -103.0187982, -0.00937409, -124.44059792, -0.07562299, -12.44405979, -0.35227053, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1258990, 32386451.5599242, 0.1125, 0.00189844, 0.00058594, 13494354.81663509, 0.00152995)
    ops.section('Aggregator', 1258991, 1258990, 'Mz')
    ops.section('Aggregator', 1258992, 1258991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1258, 1258991, 0.3599452247, 1258992, 0.3599452247, 1258990)
    # Create element
    ops.element('forceBeamColumn', 1258, 258, 358, 1258, 1258)

    # Create geometric transformation
    ops.geomTransf('Linear', 1358, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1358990, 78.43999012, 0.00904857, 94.34464916, 0.08339703, 9.43446492, 0.42530755, -103.82244695, -0.00933704, -124.87370685, -0.08865713, -12.48737068, -0.43056765, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1358991, 78.43999012, 0.00904857, 94.34464916, 0.08405069, 9.43446492, 0.42596121, -103.82244695, -0.00933704, -124.87370685, -0.0893545, -12.48737068, -0.43126501, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1358990, 33555986.15746585, 0.1125, 0.00189844, 0.00058594, 13981660.89894411, 0.00152995)
    ops.section('Aggregator', 1358991, 1358990, 'Mz')
    ops.section('Aggregator', 1358992, 1358991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1358, 1358991, 0.29247418478, 1358992, 0.29247418478, 1358990)
    # Create element
    ops.element('forceBeamColumn', 1358, 358, 458, 1358, 1358)

    # Create geometric transformation
    ops.geomTransf('Linear', 1458, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1458990, 78.03737122, 0.00872272, 94.09254317, 0.07095379, 9.40925432, 0.35091249, -103.28411667, -0.00900812, -124.53347741, -0.07540054, -12.45334774, -0.35535924, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1458991, 78.03737122, 0.00872272, 94.09254317, 0.07065689, 9.40925432, 0.34760503, -103.28411667, -0.00900812, -124.53347741, -0.07508379, -12.45334774, -0.35203193, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1458990, 32895411.98740538, 0.1125, 0.00189844, 0.00058594, 13706421.66141891, 0.00152995)
    ops.section('Aggregator', 1458991, 1458990, 'Mz')
    ops.section('Aggregator', 1458992, 1458991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1458, 1458991, 0.35719554155, 1458992, 0.35719554155, 1458990)
    # Create element
    ops.element('forceBeamColumn', 1458, 458, 558, 1458, 1458)

    # Create geometric transformation
    ops.geomTransf('Linear', 1558, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.325, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1558990, 78.13016266, 0.00903804, 93.91272627, 0.08376249, 9.39127263, 0.42614777, -103.41187494, -0.00932494, -124.30143203, -0.08904616, -12.4301432, -0.43143144, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1558991, 78.17994844, 0.00905899, 93.97256894, 0.08375437, 9.39725689, 0.42613965, -78.17994844, -0.00905899, -93.97256894, -0.08375437, -9.39725689, -0.42613965, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1558990, 33719932.87820066, 0.1125, 0.00189844, 0.00058594, 14049972.03258361, 0.00152995)
    ops.section('Aggregator', 1558991, 1558990, 'Mz')
    ops.section('Aggregator', 1558992, 1558991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1558, 1558991, 0.29206863069000005, 1558992, 0.29206863069000005, 1558990)
    # Create element
    ops.element('forceBeamColumn', 1558, 558, 658, 1558, 1558)

    # Create geometric transformation
    ops.geomTransf('Linear', 1658, 0, -1, 0, '-jntOffset', 0.325, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1658990, 79.29876121, 0.00870158, 95.04034722, 0.06822042, 9.50403472, 0.34734161, -79.29876121, -0.00870158, -95.04034722, -0.06822042, -9.50403472, -0.34734161, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1658991, 79.29876121, 0.00870158, 95.04034722, 0.06869587, 9.50403472, 0.34781705, -79.29876121, -0.00870158, -95.04034722, -0.06869587, -9.50403472, -0.34781705, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1658990, 34453178.19398928, 0.1125, 0.00189844, 0.00058594, 14355490.9141622, 0.00152995)
    ops.section('Aggregator', 1658991, 1658990, 'Mz')
    ops.section('Aggregator', 1658992, 1658991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1658, 1658991, 0.35826732804, 1658992, 0.35826732804, 1658990)
    # Create element
    ops.element('forceBeamColumn', 1658, 658, 758, 1658, 1658)

    # Create geometric transformation
    ops.geomTransf('Linear', 6220, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6220990, 100.30220017, 0.01291915, 121.60370235, 0.10839319, 12.16037023, 0.40016634, -153.1881286, -0.01416161, -185.72118619, -0.1197205, -18.57211862, -0.41149365, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6220991, 100.30220017, 0.01291915, 121.60370235, 0.10810217, 12.16037023, 0.39904263, -153.1881286, -0.01416161, -185.72118619, -0.11939874, -18.57211862, -0.4103392, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6220990, 31305199.68962622, 0.0875, 0.00089323, 0.00045573, 13043833.20401092, 0.0010204)
    ops.section('Aggregator', 6220991, 6220990, 'Mz')
    ops.section('Aggregator', 6220992, 6220991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6220, 6220991, 0.34273201764, 6220992, 0.34273201764, 6220990)
    # Create element
    ops.element('forceBeamColumn', 6220, 1121, 1221, 6220, 6220)

    # Create geometric transformation
    ops.geomTransf('Linear', 6620, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6620990, 100.79466075, 0.0131061, 121.34510336, 0.10261517, 12.13451034, 0.39050883, -154.0007537, -0.01431701, -185.39908002, -0.11328085, -18.539908, -0.40117451, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6620991, 100.79466075, 0.0131061, 121.34510336, 0.10259891, 12.13451034, 0.39036853, -154.0007537, -0.01431701, -185.39908002, -0.11326287, -18.539908, -0.40103249, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6620990, 33310208.66788986, 0.0875, 0.00089323, 0.00045573, 13879253.61162077, 0.0010204)
    ops.section('Aggregator', 6620991, 6620990, 'Mz')
    ops.section('Aggregator', 6620992, 6620991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6620, 6620991, 0.34509154160000005, 6620992, 0.34509154160000005, 6620990)
    # Create element
    ops.element('forceBeamColumn', 6620, 1521, 1621, 6620, 6620)

    # Create geometric transformation
    ops.geomTransf('Linear', 6221, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6221990, 366.62747076, 0.00931803, 441.24026357, 0.10464925, 44.12402636, 0.31969766, -366.62747076, -0.00931803, -441.24026357, -0.10464925, -44.12402636, -0.31969766, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6221991, 366.62747076, 0.00931803, 441.24026357, 0.10396974, 44.12402636, 0.31901815, -366.62747076, -0.00931803, -441.24026357, -0.10396974, -44.12402636, -0.31901815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6221990, 33392361.10792591, 0.125, 0.00260417, 0.00065104, 13913483.79496913, 0.00178813)
    ops.section('Aggregator', 6221991, 6221990, 'Mz')
    ops.section('Aggregator', 6221992, 6221991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6221, 6221991, 0.46501157038, 6221992, 0.46501157038, 6221990)
    # Create element
    ops.element('forceBeamColumn', 6221, 1122, 1222, 6221, 6221)

    # Create geometric transformation
    ops.geomTransf('Linear', 6621, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6621990, 350.36834372, 0.00916629, 423.38314587, 0.11015167, 42.33831459, 0.33027577, -350.36834372, -0.00916629, -423.38314587, -0.11015167, -42.33831459, -0.33027577, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6621991, 350.36834372, 0.00916629, 423.38314587, 0.10910405, 42.33831459, 0.32922815, -350.36834372, -0.00916629, -423.38314587, -0.10910405, -42.33831459, -0.32922815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6621990, 32279434.28210397, 0.125, 0.00260417, 0.00065104, 13449764.28420999, 0.00178813)
    ops.section('Aggregator', 6621991, 6621990, 'Mz')
    ops.section('Aggregator', 6621992, 6621991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6621, 6621991, 0.45428920042, 6621992, 0.45428920042, 6621990)
    # Create element
    ops.element('forceBeamColumn', 6621, 1522, 1622, 6621, 6621)

    # Create geometric transformation
    ops.geomTransf('Linear', 6222, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6222990, 318.28767776, 0.0111345, 384.43937374, 0.10808249, 38.44393737, 0.3215, -318.28767776, -0.0111345, -384.43937374, -0.10808249, -38.44393737, -0.3215, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6222991, 318.28767776, 0.0111345, 384.43937374, 0.10834296, 38.44393737, 0.32176048, -318.28767776, -0.0111345, -384.43937374, -0.10834296, -38.44393737, -0.32176048, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6222990, 32410989.96155597, 0.1125, 0.00189844, 0.00058594, 13504579.15064832, 0.00152995)
    ops.section('Aggregator', 6222991, 6222990, 'Mz')
    ops.section('Aggregator', 6222992, 6222991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6222, 6222991, 0.46856510280999997, 6222992, 0.46856510280999997, 6222990)
    # Create element
    ops.element('forceBeamColumn', 6222, 1123, 1223, 6222, 6222)

    # Create geometric transformation
    ops.geomTransf('Linear', 6622, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6622990, 313.61003966, 0.01099658, 377.11609384, 0.10698951, 37.71160938, 0.32222617, -313.61003966, -0.01099658, -377.11609384, -0.10698951, -37.71160938, -0.32222617, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6622991, 313.61003966, 0.01099658, 377.11609384, 0.10774915, 37.71160938, 0.32298581, -313.61003966, -0.01099658, -377.11609384, -0.10774915, -37.71160938, -0.32298581, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6622990, 33612816.20328889, 0.1125, 0.00189844, 0.00058594, 14005340.0847037, 0.00152995)
    ops.section('Aggregator', 6622991, 6622990, 'Mz')
    ops.section('Aggregator', 6622992, 6622991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6622, 6622991, 0.46460486902000003, 6622992, 0.46460486902000003, 6622990)
    # Create element
    ops.element('forceBeamColumn', 6622, 1523, 1623, 6622, 6622)

    # Create geometric transformation
    ops.geomTransf('Linear', 6223, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6223990, 176.90304538, 0.01159564, 213.78905403, 0.10371909, 21.3789054, 0.35726847, -269.51249438, -0.01291523, -325.70847551, -0.11476961, -32.57084755, -0.36831899, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6223991, 176.90304538, 0.01159564, 213.78905403, 0.10423272, 21.3789054, 0.3577821, -269.51249438, -0.01291523, -325.70847551, -0.1153375, -32.57084755, -0.36888687, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6223990, 32252103.36149421, 0.1, 0.00133333, 0.00052083, 13438376.40062259, 0.00127345)
    ops.section('Aggregator', 6223991, 6223990, 'Mz')
    ops.section('Aggregator', 6223992, 6223991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6223, 6223991, 0.39440049692999996, 6223992, 0.39440049692999996, 6223990)
    # Create element
    ops.element('forceBeamColumn', 6223, 1124, 1224, 6223, 6223)

    # Create geometric transformation
    ops.geomTransf('Linear', 6623, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6623990, 175.06601285, 0.01188475, 210.21390589, 0.1005476, 21.02139059, 0.35277939, -266.95248989, -0.01318325, -320.548373, -0.11121148, -32.0548373, -0.36344327, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6623991, 175.06601285, 0.01188475, 210.21390589, 0.10126654, 21.02139059, 0.35349833, -266.95248989, -0.01318325, -320.548373, -0.11200637, -32.0548373, -0.36423816, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6623990, 33982930.79420396, 0.1, 0.00133333, 0.00052083, 14159554.49758498, 0.00127345)
    ops.section('Aggregator', 6623991, 6623990, 'Mz')
    ops.section('Aggregator', 6623992, 6623991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6623, 6623991, 0.39646073206, 6623992, 0.39646073206, 6623990)
    # Create element
    ops.element('forceBeamColumn', 6623, 1524, 1624, 6623, 6623)

    # Create geometric transformation
    ops.geomTransf('Linear', 6224, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6224990, 82.72846681, 0.01563326, 99.34247396, 0.10930168, 9.9342474, 0.40216642, -126.15984737, -0.01719593, -151.49599449, -0.12075846, -15.14959945, -0.41362321, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6224991, 82.72846681, 0.01563326, 99.34247396, 0.10916074, 9.9342474, 0.40202548, -126.15984737, -0.01719593, -151.49599449, -0.12060264, -15.14959945, -0.41346738, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6224990, 33971011.04367407, 0.075, 0.0005625, 0.00039062, 14154587.9348642, 0.00077515)
    ops.section('Aggregator', 6224991, 6224990, 'Mz')
    ops.section('Aggregator', 6224992, 6224991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6224, 6224991, 0.34145455218000004, 6224992, 0.34145455218000004, 6224990)
    # Create element
    ops.element('forceBeamColumn', 6224, 1125, 1225, 6224, 6224)

    # Create geometric transformation
    ops.geomTransf('Linear', 6624, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6624990, 85.53484516, 0.01548645, 102.03948278, 0.10181238, 10.20394828, 0.38926602, -130.46550124, -0.01701151, -155.63987101, -0.11245598, -15.5639871, -0.39990962, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6624991, 85.53484516, 0.01548645, 102.03948278, 0.10276909, 10.20394828, 0.39291993, -130.46550124, -0.01701151, -155.63987101, -0.11351374, -15.5639871, -0.40366458, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6624990, 35552536.26900686, 0.075, 0.0005625, 0.00039062, 14813556.77875286, 0.00077515)
    ops.section('Aggregator', 6624991, 6624990, 'Mz')
    ops.section('Aggregator', 6624992, 6624991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6624, 6624991, 0.34464832192, 6624992, 0.34464832192, 6624990)
    # Create element
    ops.element('forceBeamColumn', 6624, 1525, 1625, 6624, 6624)

    # Create geometric transformation
    ops.geomTransf('Linear', 6225, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6225990, 63.85150654, 0.01517415, 77.28567444, 0.12795916, 7.72856744, 0.47161218, -127.43681745, -0.0177146, -154.24914648, -0.15075149, -15.42491465, -0.49440451, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6225991, 63.85150654, 0.01517415, 77.28567444, 0.1280432, 7.72856744, 0.47169621, -127.43681745, -0.0177146, -154.24914648, -0.15085062, -15.42491465, -0.49450363, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6225990, 31797385.33880816, 0.075, 0.0005625, 0.00039062, 13248910.55783673, 0.00077515)
    ops.section('Aggregator', 6225991, 6225990, 'Mz')
    ops.section('Aggregator', 6225992, 6225991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6225, 6225991, 0.29099119025, 6225992, 0.29099119025, 6225990)
    # Create element
    ops.element('forceBeamColumn', 6225, 1126, 1226, 6225, 6225)

    # Create geometric transformation
    ops.geomTransf('Linear', 6625, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6625990, 63.32292136, 0.01572885, 76.40182309, 0.12367931, 7.64018231, 0.46381805, -126.26152029, -0.01828424, -152.33994468, -0.14561848, -15.23399447, -0.48575722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6625991, 63.32292136, 0.01572885, 76.40182309, 0.12482921, 7.64018231, 0.46637227, -126.26152029, -0.01828424, -152.33994468, -0.14697485, -15.23399447, -0.48851792, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6625990, 32711302.28011872, 0.075, 0.0005625, 0.00039062, 13629709.2833828, 0.00077515)
    ops.section('Aggregator', 6625991, 6625990, 'Mz')
    ops.section('Aggregator', 6625992, 6625991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6625, 6625991, 0.29278884422, 6625992, 0.29278884422, 6625990)
    # Create element
    ops.element('forceBeamColumn', 6625, 1526, 1626, 6625, 6625)

    # Create geometric transformation
    ops.geomTransf('Linear', 6226, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6226990, 47.82529148, 0.01452988, 57.56425503, 0.10757794, 5.7564255, 0.45101895, -82.74858292, -0.01593574, -99.59919497, -0.12184398, -9.9599195, -0.46528499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6226991, 47.82529148, 0.01452988, 57.56425503, 0.10822538, 5.7564255, 0.45477393, -82.74858292, -0.01593574, -99.59919497, -0.1225809, -9.9599195, -0.46912945, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6226990, 33364867.69311781, 0.075, 0.0005625, 0.00039062, 13902028.20546576, 0.00077515)
    ops.section('Aggregator', 6226991, 6226990, 'Mz')
    ops.section('Aggregator', 6226992, 6226991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6226, 6226991, 0.28855986016999996, 6226992, 0.28855986016999996, 6226990)
    # Create element
    ops.element('forceBeamColumn', 6226, 1127, 1227, 6226, 6226)

    # Create geometric transformation
    ops.geomTransf('Linear', 6626, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6626990, 47.79648455, 0.01489349, 57.53511958, 0.10693274, 5.75351196, 0.44728815, -82.6200218, -0.01632193, -99.45402636, -0.12108194, -9.94540264, -0.46143734, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6626991, 47.79648455, 0.01489349, 57.53511958, 0.10796693, 5.75351196, 0.45260144, -82.6200218, -0.01632193, -99.45402636, -0.12225906, -9.94540264, -0.46689357, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6626990, 33339354.85004572, 0.075, 0.0005625, 0.00039062, 13891397.85418572, 0.00077515)
    ops.section('Aggregator', 6626991, 6626990, 'Mz')
    ops.section('Aggregator', 6626992, 6626991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6626, 6626991, 0.29016247125, 6626992, 0.29016247125, 6626990)
    # Create element
    ops.element('forceBeamColumn', 6626, 1527, 1627, 6626, 6626)

    # Create geometric transformation
    ops.geomTransf('Linear', 6227, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6227990, 32.05938628, 0.01433947, 38.63273132, 0.09078206, 3.86327313, 0.43493276, -47.38970266, -0.01497212, -57.10632245, -0.09871655, -5.71063225, -0.44286725, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6227991, 32.05938628, 0.01433947, 38.63273132, 0.09163758, 3.86327313, 0.43772831, -47.38970266, -0.01497212, -57.10632245, -0.09965378, -5.71063225, -0.44574452, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6227990, 33053585.02795198, 0.075, 0.0005625, 0.00039062, 13772327.09497999, 0.00077515)
    ops.section('Aggregator', 6227991, 6227990, 'Mz')
    ops.section('Aggregator', 6227992, 6227991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6227, 6227991, 0.28894156875, 6227992, 0.28894156875, 6227990)
    # Create element
    ops.element('forceBeamColumn', 6227, 1128, 1228, 6227, 6227)

    # Create geometric transformation
    ops.geomTransf('Linear', 6627, 0, -1, 0, '-jntOffset', 0.175, 0.0, 0.0, -0.175, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 6627990, 32.73508425, 0.01446534, 39.06681895, 0.08738389, 3.9066819, 0.43033827, -48.39060399, -0.01507862, -57.75048419, -0.0949624, -5.77504842, -0.43791677, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 6627991, 32.73508425, 0.01446534, 39.06681895, 0.08716672, 3.9066819, 0.43012109, -48.39060399, -0.01507862, -57.75048419, -0.09472448, -5.77504842, -0.43767885, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 6627990, 35463197.94043221, 0.075, 0.0005625, 0.00039062, 14776332.47518009, 0.00077515)
    ops.section('Aggregator', 6627991, 6627990, 'Mz')
    ops.section('Aggregator', 6627992, 6627991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 6627, 6627991, 0.29158397734, 6627992, 0.29158397734, 6627990)
    # Create element
    ops.element('forceBeamColumn', 6627, 1528, 1628, 6627, 6627)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 242.73438701, 0.00883797, 292.52017313, 0.07265104, 29.25201731, 0.26154642, -242.73438701, -0.00883797, -292.52017313, -0.07265104, -29.25201731, -0.26154642, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 242.98504404, 0.0087191, 292.82224091, 0.06866, 29.28222409, 0.25755539, -358.95286207, -0.00944773, -432.57551866, -0.07511422, -43.25755187, -0.2640096, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 33038426.99165027, 0.125, 0.00260417, 0.00065104, 13766011.24652095, 0.00178813)
    ops.section('Aggregator', 2001991, 2001990, 'Mz')
    ops.section('Aggregator', 2001992, 2001991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.5293935579100001, 2001992, 0.5293935579100001, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 246.25224652, 0.00867929, 297.71395599, 0.08341336, 29.7713956, 0.27111211, -364.14629127, -0.00934036, -440.24545752, -0.09121307, -44.02454575, -0.27891182, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 246.29240984, 0.00859297, 297.76251263, 0.07792547, 29.77625126, 0.26562421, -480.01940781, -0.00984707, -580.33369795, -0.09088132, -58.0333698, -0.27858007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 32140217.92657796, 0.15, 0.003125, 0.001125, 13391757.46940748, 0.00281737)
    ops.section('Aggregator', 2101991, 2101990, 'Mz')
    ops.section('Aggregator', 2101992, 2101991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.5327685996500001, 2101992, 0.5327685996500001, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 249.57064042, 0.0087487, 300.87400909, 0.08267497, 30.08740091, 0.26901703, -369.08744469, -0.00940597, -444.95946721, -0.09039372, -44.49594672, -0.27673578, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 249.61133515, 0.00866359, 300.92306931, 0.07629356, 30.09230693, 0.26263562, -486.5647524, -0.00991034, -586.58617654, -0.08895471, -58.65861765, -0.27529678, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 32934055.97837185, 0.15, 0.003125, 0.001125, 13722523.32432161, 0.00281737)
    ops.section('Aggregator', 2201991, 2201990, 'Mz')
    ops.section('Aggregator', 2201992, 2201991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.53664748563, 2201992, 0.53664748563, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 245.15065613, 0.00901732, 296.54283453, 0.07514224, 29.65428345, 0.26171497, -362.26838379, -0.00978045, -438.21254687, -0.08222166, -43.82125469, -0.26879438, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 245.15065613, 0.00901732, 296.54283453, 0.07516441, 29.65428345, 0.26173713, -362.26838379, -0.00978045, -438.21254687, -0.08224594, -43.82125469, -0.26881866, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 31982700.20448657, 0.125, 0.00260417, 0.00065104, 13326125.08520274, 0.00178813)
    ops.section('Aggregator', 2301991, 2301990, 'Mz')
    ops.section('Aggregator', 2301992, 2301991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.53598402906, 2301992, 0.53598402906, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2401, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2401990, 244.76062845, 0.0090451, 294.03181938, 0.07241615, 29.40318194, 0.25866486, -361.90965299, -0.00978179, -434.76336204, -0.07920607, -43.4763362, -0.26545479, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2401991, 244.76062845, 0.0090451, 294.03181938, 0.0723747, 29.40318194, 0.25862342, -361.90965299, -0.00978179, -434.76336204, -0.07916067, -43.4763362, -0.26540939, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2401990, 33869636.6646871, 0.125, 0.00260417, 0.00065104, 14112348.61028629, 0.00178813)
    ops.section('Aggregator', 2401991, 2401990, 'Mz')
    ops.section('Aggregator', 2401992, 2401991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2401, 2401991, 0.53691644611, 2401992, 0.53691644611, 2401990)
    # Create element
    ops.element('forceBeamColumn', 2401, 401, 411, 2401, 2401)

    # Create geometric transformation
    ops.geomTransf('Linear', 2501, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2501990, 244.03709779, 0.00865689, 291.60555548, 0.07807289, 29.16055555, 0.26610326, -361.17887495, -0.00927785, -431.58096621, -0.08532449, -43.15809662, -0.27335487, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2501991, 243.94166058, 0.00858283, 291.49151535, 0.07280883, 29.14915154, 0.26083921, -476.20274008, -0.00976083, -569.02563504, -0.08482673, -56.9025635, -0.2728571, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2501990, 35171982.22361099, 0.15, 0.003125, 0.001125, 14654992.59317125, 0.00281737)
    ops.section('Aggregator', 2501991, 2501990, 'Mz')
    ops.section('Aggregator', 2501992, 2501991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2501, 2501991, 0.53182897187, 2501992, 0.53182897187, 2501990)
    # Create element
    ops.element('forceBeamColumn', 2501, 501, 511, 2501, 2501)

    # Create geometric transformation
    ops.geomTransf('Linear', 2601, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2601990, 246.23336916, 0.00857738, 294.55206817, 0.07860475, 29.45520682, 0.26664905, -364.28413782, -0.00919957, -435.76809497, -0.08591599, -43.5768095, -0.27396029, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2601991, 246.23836404, 0.00849954, 294.5580432, 0.07342345, 29.45580432, 0.26146775, -480.30540241, -0.0096795, -574.55636543, -0.0855611, -57.45563654, -0.2736054, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2601990, 34913545.98957976, 0.15, 0.003125, 0.001125, 14547310.82899157, 0.00281737)
    ops.section('Aggregator', 2601991, 2601990, 'Mz')
    ops.section('Aggregator', 2601992, 2601991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2601, 2601991, 0.5317895784500001, 2601992, 0.5317895784500001, 2601990)
    # Create element
    ops.element('forceBeamColumn', 2601, 601, 611, 2601, 2601)

    # Create geometric transformation
    ops.geomTransf('Linear', 2701, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2701990, 241.84453615, 0.00882615, 291.31515109, 0.0729976, 29.13151511, 0.26217139, -241.84453615, -0.00882615, -291.31515109, -0.0729976, -29.13151511, -0.26217139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2701991, 242.06873924, 0.00870866, 291.58521614, 0.06900651, 29.15852161, 0.2581803, -357.63682249, -0.00943409, -430.79337924, -0.07549162, -43.07933792, -0.26466541, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2701990, 33161260.51153638, 0.125, 0.00260417, 0.00065104, 13817191.87980682, 0.00178813)
    ops.section('Aggregator', 2701991, 2701990, 'Mz')
    ops.section('Aggregator', 2701992, 2701991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2701, 2701991, 0.52861445957, 2701992, 0.52861445957, 2701990)
    # Create element
    ops.element('forceBeamColumn', 2701, 701, 711, 2701, 2701)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 236.63924287, 0.00875894, 283.53926936, 0.07281077, 28.35392694, 0.26284962, -349.96521332, -0.00946328, -419.32555093, -0.07963338, -41.93255509, -0.26967223, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 350.45454733, 0.00932753, 419.91186706, 0.07589374, 41.99118671, 0.2659326, -350.45454733, -0.00932753, -419.91186706, -0.07589374, -41.99118671, -0.2659326, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 34518192.0157375, 0.125, 0.00260417, 0.00065104, 14382580.00655729, 0.00178813)
    ops.section('Aggregator', 2011991, 2011990, 'Mz')
    ops.section('Aggregator', 2011992, 2011991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.52620818938, 2011992, 0.52620818938, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 243.99860471, 0.00850505, 293.00704261, 0.08328691, 29.30070426, 0.27194056, -475.92542004, -0.00970306, -571.51761173, -0.09710639, -57.15176117, -0.28576004, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 478.18138912, 0.00944668, 574.22670438, 0.10122833, 57.42267044, 0.28988198, -478.18138912, -0.00944668, -574.22670438, -0.10122833, -57.42267044, -0.28988198, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 33964741.32455829, 0.15, 0.003125, 0.001125, 14151975.55189929, 0.00281737)
    ops.section('Aggregator', 2111991, 2111990, 'Mz')
    ops.section('Aggregator', 2111992, 2111991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.53007189783, 2111992, 0.53007189783, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 245.44817512, 0.00843552, 293.91489624, 0.08167074, 29.39148962, 0.27036671, -478.62942247, -0.00961373, -573.14061094, -0.09520939, -57.31406109, -0.28390536, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 481.1113892, 0.00936138, 576.11267212, 0.09950813, 57.61126721, 0.2882041, -481.1113892, -0.00936138, -576.11267212, -0.09950813, -57.61126721, -0.2882041, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 34666529.07530504, 0.15, 0.003125, 0.001125, 14444387.11471044, 0.00281737)
    ops.section('Aggregator', 2211991, 2211990, 'Mz')
    ops.section('Aggregator', 2211992, 2211991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.52995302497, 2211992, 0.52995302497, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 241.31346831, 0.00899413, 290.57864912, 0.07480231, 29.05786491, 0.26230423, -356.82051961, -0.00973326, -429.66696096, -0.08182747, -42.9666961, -0.26932939, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 357.355007, 0.00958794, 430.31056625, 0.08549784, 43.03105662, 0.27299977, -357.355007, -0.00958794, -430.31056625, -0.08549784, -43.03105662, -0.27299977, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 33250456.73187896, 0.125, 0.00260417, 0.00065104, 13854356.97161623, 0.00178813)
    ops.section('Aggregator', 2311991, 2311990, 'Mz')
    ops.section('Aggregator', 2311992, 2311991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.53332786812, 2311992, 0.53332786812, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)

    # Create geometric transformation
    ops.geomTransf('Linear', 2411, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2411990, 245.05523862, 0.00892074, 296.24506906, 0.07496559, 29.62450691, 0.26215471, -362.0527324, -0.00967557, -437.68228468, -0.08202906, -43.76822847, -0.26921818, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2411991, 362.96491927, 0.00951916, 438.78501917, 0.08566084, 43.87850192, 0.27284996, -362.96491927, -0.00951916, -438.78501917, -0.08566084, -43.87850192, -0.27284996, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2411990, 32161396.12386554, 0.125, 0.00260417, 0.00065104, 13400581.71827731, 0.00178813)
    ops.section('Aggregator', 2411991, 2411990, 'Mz')
    ops.section('Aggregator', 2411992, 2411991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2411, 2411991, 0.53421908673, 2411992, 0.53421908673, 2411990)
    # Create element
    ops.element('forceBeamColumn', 2411, 411, 421, 2411, 2411)

    # Create geometric transformation
    ops.geomTransf('Linear', 2511, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2511990, 237.3549326, 0.00845099, 286.90614279, 0.08720523, 28.69061428, 0.2780839, -462.97997301, -0.0096747, -559.63361195, -0.10172087, -55.96336119, -0.29259954, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2511991, 465.02119771, 0.00940893, 562.10097128, 0.10640376, 56.21009713, 0.29728243, -465.02119771, -0.00940893, -562.10097128, -0.10640376, -56.21009713, -0.29728243, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2511990, 32191627.22414859, 0.15, 0.003125, 0.001125, 13413178.01006191, 0.00281737)
    ops.section('Aggregator', 2511991, 2511990, 'Mz')
    ops.section('Aggregator', 2511992, 2511991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2511, 2511991, 0.5238930038, 2511992, 0.5238930038, 2511990)
    # Create element
    ops.element('forceBeamColumn', 2511, 511, 521, 2511, 2511)

    # Create geometric transformation
    ops.geomTransf('Linear', 2611, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2611990, 242.92463435, 0.00865275, 292.51224372, 0.08287892, 29.25122437, 0.2708935, -474.06017914, -0.00987922, -570.82891996, -0.09663308, -57.082892, -0.28464765, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2611991, 475.91788345, 0.00961893, 573.06583289, 0.10170044, 57.30658329, 0.28971502, -475.91788345, -0.00961893, -573.06583289, -0.10170044, -57.30658329, -0.28971502, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2611990, 33256385.66011746, 0.15, 0.003125, 0.001125, 13856827.35838228, 0.00281737)
    ops.section('Aggregator', 2611991, 2611990, 'Mz')
    ops.section('Aggregator', 2611992, 2611991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2611, 2611991, 0.53187365559, 2611992, 0.53187365559, 2611990)
    # Create element
    ops.element('forceBeamColumn', 2611, 611, 621, 2611, 2611)

    # Create geometric transformation
    ops.geomTransf('Linear', 2711, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2711990, 236.39644675, 0.00889842, 283.63475937, 0.07228875, 28.36347594, 0.26153458, -349.68458029, -0.00961432, -419.56088236, -0.07905973, -41.95608824, -0.26830556, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2711991, 350.02919842, 0.00947835, 419.97436437, 0.07568466, 41.99743644, 0.26493048, -350.02919842, -0.00947835, -419.97436437, -0.07568466, -41.99743644, -0.26493048, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2711990, 34180855.73169159, 0.125, 0.00260417, 0.00065104, 14242023.22153816, 0.00178813)
    ops.section('Aggregator', 2711991, 2711990, 'Mz')
    ops.section('Aggregator', 2711992, 2711991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2711, 2711991, 0.52841323331, 2711992, 0.52841323331, 2711990)
    # Create element
    ops.element('forceBeamColumn', 2711, 711, 721, 2711, 2711)

    # Create geometric transformation
    ops.geomTransf('Linear', 2021, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2021990, 349.69466571, 0.00956135, 419.43988396, 0.10245122, 41.9439884, 0.31904977, -349.69466571, -0.00956135, -419.43988396, -0.10245122, -41.9439884, -0.31904977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2021991, 349.69466571, 0.00956135, 419.43988396, 0.10335931, 41.9439884, 0.31995786, -349.69466571, -0.00956135, -419.43988396, -0.10335931, -41.9439884, -0.31995786, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2021990, 34260058.21881391, 0.125, 0.00260417, 0.00065104, 14275024.25783913, 0.00178813)
    ops.section('Aggregator', 2021991, 2021990, 'Mz')
    ops.section('Aggregator', 2021992, 2021991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2021, 2021991, 0.46168360066, 2021992, 0.46168360066, 2021990)
    # Create element
    ops.element('forceBeamColumn', 2021, 21, 31, 2021, 2021)

    # Create geometric transformation
    ops.geomTransf('Linear', 2121, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2121990, 477.02979112, 0.00947609, 574.75859726, 0.13042953, 57.47585973, 0.34700838, -477.02979112, -0.00947609, -574.75859726, -0.13042953, -57.47585973, -0.34700838, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2121991, 477.02979112, 0.00947609, 574.75859726, 0.1295205, 57.47585973, 0.34609935, -477.02979112, -0.00947609, -574.75859726, -0.1295205, -57.47585973, -0.34609935, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2121990, 33091078.20368017, 0.15, 0.003125, 0.001125, 13787949.2515334, 0.00281737)
    ops.section('Aggregator', 2121991, 2121990, 'Mz')
    ops.section('Aggregator', 2121992, 2121991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2121, 2121991, 0.46172559104, 2121992, 0.46172559104, 2121990)
    # Create element
    ops.element('forceBeamColumn', 2121, 121, 131, 2121, 2121)

    # Create geometric transformation
    ops.geomTransf('Linear', 2221, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2221990, 471.17885334, 0.00944917, 568.61384785, 0.13141138, 56.86138479, 0.34928169, -471.17885334, -0.00944917, -568.61384785, -0.13141138, -56.86138479, -0.34928169, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2221991, 471.17885334, 0.00944917, 568.61384785, 0.13133164, 56.86138479, 0.34920195, -471.17885334, -0.00944917, -568.61384785, -0.13133164, -56.86138479, -0.34920195, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2221990, 32654440.53805745, 0.15, 0.003125, 0.001125, 13606016.89085727, 0.00281737)
    ops.section('Aggregator', 2221991, 2221990, 'Mz')
    ops.section('Aggregator', 2221992, 2221991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2221, 2221991, 0.45898866265, 2221992, 0.45898866265, 2221990)
    # Create element
    ops.element('forceBeamColumn', 2221, 221, 231, 2221, 2221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2321, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2321990, 354.02277974, 0.00938473, 424.93419718, 0.10471666, 42.49341972, 0.32178951, -354.02277974, -0.00938473, -424.93419718, -0.10471666, -42.49341972, -0.32178951, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2321991, 354.02277974, 0.00938473, 424.93419718, 0.10445414, 42.49341972, 0.32152699, -354.02277974, -0.00938473, -424.93419718, -0.10445414, -42.49341972, -0.32152699, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2321990, 34081404.1200583, 0.125, 0.00260417, 0.00065104, 14200585.05002429, 0.00178813)
    ops.section('Aggregator', 2321991, 2321990, 'Mz')
    ops.section('Aggregator', 2321992, 2321991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2321, 2321991, 0.46067482810000004, 2321992, 0.46067482810000004, 2321990)
    # Create element
    ops.element('forceBeamColumn', 2321, 321, 331, 2321, 2321)

    # Create geometric transformation
    ops.geomTransf('Linear', 2421, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2421990, 352.20744083, 0.00922109, 426.18062765, 0.11124292, 42.61806276, 0.33059264, -352.20744083, -0.00922109, -426.18062765, -0.11124292, -42.61806276, -0.33059264, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2421991, 352.20744083, 0.00922109, 426.18062765, 0.11060487, 42.61806276, 0.32995459, -352.20744083, -0.00922109, -426.18062765, -0.11060487, -42.61806276, -0.32995459, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2421990, 31887602.52310491, 0.125, 0.00260417, 0.00065104, 13286501.05129371, 0.00178813)
    ops.section('Aggregator', 2421991, 2421990, 'Mz')
    ops.section('Aggregator', 2421992, 2421991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2421, 2421991, 0.45589299226999996, 2421992, 0.45589299226999996, 2421990)
    # Create element
    ops.element('forceBeamColumn', 2421, 421, 431, 2421, 2421)

    # Create geometric transformation
    ops.geomTransf('Linear', 2521, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2521990, 479.78841083, 0.00955259, 579.98905412, 0.12928626, 57.99890541, 0.3450322, -479.78841083, -0.00955259, -579.98905412, -0.12928626, -57.99890541, -0.3450322, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2521991, 479.78841083, 0.00955259, 579.98905412, 0.1306976, 57.99890541, 0.34644354, -479.78841083, -0.00955259, -579.98905412, -0.1306976, -57.99890541, -0.34644354, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2521990, 32172748.97123253, 0.15, 0.003125, 0.001125, 13405312.07134689, 0.00281737)
    ops.section('Aggregator', 2521991, 2521990, 'Mz')
    ops.section('Aggregator', 2521992, 2521991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2521, 2521991, 0.46350813826000004, 2521992, 0.46350813826000004, 2521990)
    # Create element
    ops.element('forceBeamColumn', 2521, 521, 531, 2521, 2521)

    # Create geometric transformation
    ops.geomTransf('Linear', 2621, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2621990, 480.14606, 0.00942729, 579.67884572, 0.13057872, 57.96788457, 0.34718922, -480.14606, -0.00942729, -579.67884572, -0.13057872, -57.96788457, -0.34718922, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2621991, 480.14606, 0.00942729, 579.67884572, 0.12933242, 57.96788457, 0.34594292, -480.14606, -0.00942729, -579.67884572, -0.12933242, -57.96788457, -0.34594292, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2621990, 32536968.90164581, 0.15, 0.003125, 0.001125, 13557070.37568576, 0.00281737)
    ops.section('Aggregator', 2621991, 2621990, 'Mz')
    ops.section('Aggregator', 2621992, 2621991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2621, 2621991, 0.46165813675, 2621992, 0.46165813675, 2621990)
    # Create element
    ops.element('forceBeamColumn', 2621, 621, 631, 2621, 2621)

    # Create geometric transformation
    ops.geomTransf('Linear', 2721, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2721990, 356.3513696, 0.00942174, 430.25075724, 0.1066733, 43.02507572, 0.32329595, -356.3513696, -0.00942174, -430.25075724, -0.1066733, -43.02507572, -0.32329595, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2721991, 356.3513696, 0.00942174, 430.25075724, 0.10595483, 43.02507572, 0.32257749, -356.3513696, -0.00942174, -430.25075724, -0.10595483, -43.02507572, -0.32257749, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2721990, 32518121.48995537, 0.125, 0.00260417, 0.00065104, 13549217.28748141, 0.00178813)
    ops.section('Aggregator', 2721991, 2721990, 'Mz')
    ops.section('Aggregator', 2721992, 2721991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2721, 2721991, 0.46163223262, 2721992, 0.46163223262, 2721990)
    # Create element
    ops.element('forceBeamColumn', 2721, 721, 731, 2721, 2721)

    # Create geometric transformation
    ops.geomTransf('Linear', 2031, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2031990, 353.03586866, 0.00962723, 426.64549628, 0.07951353, 42.66454963, 0.26768653, -353.03586866, -0.00962723, -426.64549628, -0.07951353, -42.66454963, -0.26768653, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2031991, 238.43262771, 0.00902344, 288.14694428, 0.07590943, 28.81469443, 0.26408243, -352.57994123, -0.00977573, -426.09450584, -0.0830507, -42.60945058, -0.27122371, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2031990, 32253306.4929692, 0.125, 0.00260417, 0.00065104, 13438877.70540383, 0.00178813)
    ops.section('Aggregator', 2031991, 2031990, 'Mz')
    ops.section('Aggregator', 2031992, 2031991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2031, 2031991, 0.5314258536300001, 2031992, 0.5314258536300001, 2031990)
    # Create element
    ops.element('forceBeamColumn', 2031, 31, 41, 2031, 2031)

    # Create geometric transformation
    ops.geomTransf('Linear', 2131, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2131990, 486.11930306, 0.00967947, 586.78006649, 0.11279133, 58.67800665, 0.29931365, -486.11930306, -0.00967947, -586.78006649, -0.11279133, -58.67800665, -0.29931365, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2131991, 248.06907603, 0.00869823, 299.43675969, 0.09273952, 29.94367597, 0.27926184, -483.68292245, -0.00995422, -583.83918436, -0.10817977, -58.38391844, -0.29470209, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2131990, 32589630.36286679, 0.15, 0.003125, 0.001125, 13579012.65119449, 0.00281737)
    ops.section('Aggregator', 2131991, 2131990, 'Mz')
    ops.section('Aggregator', 2131992, 2131991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2131, 2131991, 0.5361288577300001, 2131992, 0.5361288577300001, 2131990)
    # Create element
    ops.element('forceBeamColumn', 2131, 131, 141, 2131, 2131)

    # Create geometric transformation
    ops.geomTransf('Linear', 2231, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2231990, 481.39193366, 0.00946014, 577.148235, 0.10927298, 57.7148235, 0.29737491, -481.39193366, -0.00946014, -577.148235, -0.10927298, -57.7148235, -0.29737491, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2231991, 245.62088161, 0.0085216, 294.47867401, 0.0898637, 29.4478674, 0.27796563, -479.0858764, -0.00971464, -574.38346729, -0.10478545, -57.43834673, -0.29288737, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2231990, 34369800.29381094, 0.15, 0.003125, 0.001125, 14320750.12242123, 0.00281737)
    ops.section('Aggregator', 2231991, 2231990, 'Mz')
    ops.section('Aggregator', 2231992, 2231991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2231, 2231991, 0.53162667856, 2231992, 0.53162667856, 2231990)
    # Create element
    ops.element('forceBeamColumn', 2231, 231, 241, 2231, 2231)

    # Create geometric transformation
    ops.geomTransf('Linear', 2331, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2331990, 363.01315848, 0.00953317, 436.73544274, 0.09227357, 43.67354427, 0.27912901, -363.01315848, -0.00953317, -436.73544274, -0.09227357, -43.67354427, -0.27912901, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2331991, 245.08803821, 0.00894416, 294.86157836, 0.0797343, 29.48615784, 0.26658974, -362.25894436, -0.0096811, -435.82805955, -0.08723315, -43.58280596, -0.27408859, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2331990, 33485819.90089375, 0.125, 0.00260417, 0.00065104, 13952424.95870573, 0.00178813)
    ops.section('Aggregator', 2331991, 2331990, 'Mz')
    ops.section('Aggregator', 2331992, 2331991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2331, 2331991, 0.5351730732700001, 2331992, 0.5351730732700001, 2331990)
    # Create element
    ops.element('forceBeamColumn', 2331, 331, 341, 2331, 2331)

    # Create geometric transformation
    ops.geomTransf('Linear', 2431, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2431990, 353.14120053, 0.00957713, 423.99042847, 0.09237472, 42.39904285, 0.28052188, -353.14120053, -0.00957713, -423.99042847, -0.09237472, -42.39904285, -0.28052188, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2431991, 238.50135441, 0.00898994, 286.35087408, 0.08077602, 28.63508741, 0.26892318, -352.79389521, -0.00971516, -423.57344475, -0.08835829, -42.35734447, -0.27650545, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2431990, 34013242.16720361, 0.125, 0.00260417, 0.00065104, 14172184.23633484, 0.00178813)
    ops.section('Aggregator', 2431991, 2431990, 'Mz')
    ops.section('Aggregator', 2431992, 2431991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2431, 2431991, 0.53149884947, 2431992, 0.53149884947, 2431990)
    # Create element
    ops.element('forceBeamColumn', 2431, 431, 441, 2431, 2431)

    # Create geometric transformation
    ops.geomTransf('Linear', 2531, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2531990, 483.34011977, 0.00942402, 576.57424156, 0.10547777, 57.65742416, 0.2933546, -483.34011977, -0.00942402, -576.57424156, -0.10547777, -57.65742416, -0.2933546, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2531991, 246.59211184, 0.00850204, 294.15861428, 0.08702483, 29.41586143, 0.27490166, -481.10426803, -0.00966877, -573.90710413, -0.10144441, -57.39071041, -0.28932124, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2531990, 35564511.3922241, 0.15, 0.003125, 0.001125, 14818546.41342671, 0.00281737)
    ops.section('Aggregator', 2531991, 2531990, 'Mz')
    ops.section('Aggregator', 2531992, 2531991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2531, 2531991, 0.53226361473, 2531992, 0.53226361473, 2531990)
    # Create element
    ops.element('forceBeamColumn', 2531, 531, 541, 2531, 2531)

    # Create geometric transformation
    ops.geomTransf('Linear', 2631, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2631990, 468.34411038, 0.00948691, 564.45647467, 0.1148951, 56.44564747, 0.30471147, -468.34411038, -0.00948691, -564.45647467, -0.1148951, -56.44564747, -0.30471147, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2631991, 239.06510027, 0.00853117, 288.12542044, 0.0939651, 28.81254204, 0.28378148, -466.5121101, -0.00974543, -562.24851604, -0.10959867, -56.2248516, -0.29941505, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2631990, 33012898.0116969, 0.15, 0.003125, 0.001125, 13755374.17154037, 0.00281737)
    ops.section('Aggregator', 2631991, 2631990, 'Mz')
    ops.section('Aggregator', 2631992, 2631991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2631, 2631991, 0.52682493337, 2631992, 0.52682493337, 2631990)
    # Create element
    ops.element('forceBeamColumn', 2631, 631, 641, 2631, 2631)

    # Create geometric transformation
    ops.geomTransf('Linear', 2731, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2731990, 354.99696965, 0.00945231, 424.18862739, 0.07453005, 42.41886274, 0.26292258, -354.99696965, -0.00945231, -424.18862739, -0.07453005, -42.41886274, -0.26292258, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2731991, 239.7102579, 0.0088808, 286.43164298, 0.07150837, 28.6431643, 0.2599009, -354.56410093, -0.0095861, -423.67138921, -0.07819589, -42.36713892, -0.26658842, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2731990, 35174983.55770183, 0.125, 0.00260417, 0.00065104, 14656243.14904243, 0.00178813)
    ops.section('Aggregator', 2731991, 2731990, 'Mz')
    ops.section('Aggregator', 2731992, 2731991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2731, 2731991, 0.53080661473, 2731992, 0.53080661473, 2731990)
    # Create element
    ops.element('forceBeamColumn', 2731, 731, 741, 2731, 2731)

    # Create geometric transformation
    ops.geomTransf('Linear', 2041, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2041990, 235.39425635, 0.00908824, 282.86010784, 0.06257545, 28.28601078, 0.25094417, -348.30026892, -0.00981817, -418.5329462, -0.06841451, -41.85329462, -0.25678323, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2041991, 235.6471229, 0.00918952, 283.16396343, 0.06494389, 28.31639634, 0.25331261, -235.6471229, -0.00918952, -283.16396343, -0.06494389, -28.31639634, -0.25331261, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2041990, 33796993.1225135, 0.125, 0.00260417, 0.00065104, 14082080.46771396, 0.00178813)
    ops.section('Aggregator', 2041991, 2041990, 'Mz')
    ops.section('Aggregator', 2041992, 2041991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2041, 2041991, 0.53087369852, 2041992, 0.53087369852, 2041990)
    # Create element
    ops.element('forceBeamColumn', 2041, 41, 51, 2041, 2041)

    # Create geometric transformation
    ops.geomTransf('Linear', 2141, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2141990, 240.54607477, 0.0085012, 287.94805299, 0.06726824, 28.7948053, 0.25673379, -469.56786558, -0.00967542, -562.10084813, -0.078361, -56.21008481, -0.26782655, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2141991, 240.64938205, 0.00857506, 288.07171799, 0.07282549, 28.8071718, 0.26229104, -356.1601713, -0.00919395, -426.34504835, -0.07958162, -42.63450484, -0.26904717, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2141990, 34747684.58792995, 0.15, 0.003125, 0.001125, 14478201.91163748, 0.00281737)
    ops.section('Aggregator', 2141991, 2141990, 'Mz')
    ops.section('Aggregator', 2141992, 2141991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2141, 2141991, 0.52780043876, 2141992, 0.52780043876, 2141990)
    # Create element
    ops.element('forceBeamColumn', 2141, 141, 151, 2141, 2141)

    # Create geometric transformation
    ops.geomTransf('Linear', 2241, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2241990, 246.30201767, 0.00851787, 295.26438635, 0.06666196, 29.52643864, 0.2546198, -480.35909342, -0.00971112, -575.84965925, -0.07766861, -57.58496593, -0.26562644, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2241991, 246.29074644, 0.00859722, 295.25087452, 0.07149173, 29.52508745, 0.25944956, -364.33927708, -0.00922637, -436.76626805, -0.0781286, -43.6766268, -0.26608644, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2241990, 34395646.9824809, 0.15, 0.003125, 0.001125, 14331519.57603371, 0.00281737)
    ops.section('Aggregator', 2241991, 2241990, 'Mz')
    ops.section('Aggregator', 2241992, 2241991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2241, 2241991, 0.5320342150599999, 2241992, 0.5320342150599999, 2241990)
    # Create element
    ops.element('forceBeamColumn', 2241, 241, 251, 2241, 2241)

    # Create geometric transformation
    ops.geomTransf('Linear', 2341, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2341990, 237.53097175, 0.00876512, 285.98230646, 0.07558886, 28.59823065, 0.26551152, -351.15838765, -0.00948733, -422.78733124, -0.08269411, -42.27873312, -0.27261678, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2341991, 237.53097175, 0.00876512, 285.98230646, 0.07451561, 28.59823065, 0.26443828, -351.15838765, -0.00948733, -422.78733124, -0.08151835, -42.27873312, -0.27144102, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2341990, 33289264.53998853, 0.125, 0.00260417, 0.00065104, 13870526.89166189, 0.00178813)
    ops.section('Aggregator', 2341991, 2341990, 'Mz')
    ops.section('Aggregator', 2341992, 2341991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2341, 2341991, 0.5265301009500001, 2341992, 0.5265301009500001, 2341990)
    # Create element
    ops.element('forceBeamColumn', 2341, 341, 351, 2341, 2341)

    # Create geometric transformation
    ops.geomTransf('Linear', 2441, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2441990, 241.366202, 0.00871834, 289.41114062, 0.07288423, 28.94111406, 0.26201563, -356.75276994, -0.0094276, -427.76588111, -0.07972265, -42.77658811, -0.26885405, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2441991, 241.366202, 0.00871834, 289.41114062, 0.07289314, 28.94111406, 0.26202454, -356.75276994, -0.0094276, -427.76588111, -0.07973241, -42.77658811, -0.26886381, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2441990, 34341194.8664395, 0.125, 0.00260417, 0.00065104, 14308831.19434979, 0.00178813)
    ops.section('Aggregator', 2441991, 2441990, 'Mz')
    ops.section('Aggregator', 2441992, 2441991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2441, 2441991, 0.5287329304, 2441992, 0.5287329304, 2441990)
    # Create element
    ops.element('forceBeamColumn', 2441, 441, 451, 2441, 2441)

    # Create geometric transformation
    ops.geomTransf('Linear', 2541, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2541990, 243.61062502, 0.0088079, 294.5521098, 0.07099128, 29.45521098, 0.25795171, -475.41320759, -0.01007869, -574.82699415, -0.08275722, -57.48269942, -0.26971765, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2541991, 243.7462546, 0.00888926, 294.71610092, 0.07669637, 29.47161009, 0.26365681, -360.67639651, -0.00955867, -436.09753696, -0.08384276, -43.6097537, -0.27080319, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2541990, 32108963.18219455, 0.15, 0.003125, 0.001125, 13378734.65924773, 0.00281737)
    ops.section('Aggregator', 2541991, 2541990, 'Mz')
    ops.section('Aggregator', 2541992, 2541991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2541, 2541991, 0.53487252253, 2541992, 0.53487252253, 2541990)
    # Create element
    ops.element('forceBeamColumn', 2541, 541, 551, 2541, 2541)

    # Create geometric transformation
    ops.geomTransf('Linear', 2641, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2641990, 243.79588117, 0.00847266, 291.36107523, 0.06567663, 29.13610752, 0.25448059, -475.70798482, -0.00964131, -568.51981785, -0.07650001, -56.85198178, -0.26530397, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2641991, 243.8313349, 0.00854825, 291.40344607, 0.07084088, 29.14034461, 0.25964484, -360.79538982, -0.00916441, -431.18748443, -0.07740726, -43.11874844, -0.26621122, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2641990, 35136773.79703639, 0.15, 0.003125, 0.001125, 14640322.41543183, 0.00281737)
    ops.section('Aggregator', 2641991, 2641990, 'Mz')
    ops.section('Aggregator', 2641992, 2641991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2641, 2641991, 0.52964990846, 2641992, 0.52964990846, 2641990)
    # Create element
    ops.element('forceBeamColumn', 2641, 641, 651, 2641, 2641)

    # Create geometric transformation
    ops.geomTransf('Linear', 2741, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2741990, 243.4796339, 0.00881902, 295.77511004, 0.06585022, 29.577511, 0.25429696, -359.50652838, -0.00958924, -436.72269951, -0.07206809, -43.67226995, -0.26051483, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2741991, 243.15906043, 0.00894993, 295.38568259, 0.06910692, 29.53856826, 0.25755366, -243.15906043, -0.00894993, -295.38568259, -0.06910692, -29.53856826, -0.25755366, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2741990, 30680431.03746118, 0.125, 0.00260417, 0.00065104, 12783512.93227549, 0.00178813)
    ops.section('Aggregator', 2741991, 2741990, 'Mz')
    ops.section('Aggregator', 2741992, 2741991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2741, 2741991, 0.53065391609, 2741992, 0.53065391609, 2741990)
    # Create element
    ops.element('forceBeamColumn', 2741, 741, 751, 2741, 2741)

    # Create geometric transformation
    ops.geomTransf('Linear', 2002, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2002990, 242.48614828, 0.00884658, 290.88659176, 0.0697288, 29.08865918, 0.25845205, -242.48614828, -0.00884658, -290.88659176, -0.0697288, -29.08865918, -0.25845205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2002991, 242.65138407, 0.00873411, 291.08480875, 0.06638931, 29.10848087, 0.25511257, -358.61084282, -0.00944698, -430.18987506, -0.07260945, -43.01898751, -0.2613327, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2002990, 34227891.57404801, 0.125, 0.00260417, 0.00065104, 14261621.48918667, 0.00178813)
    ops.section('Aggregator', 2002991, 2002990, 'Mz')
    ops.section('Aggregator', 2002992, 2002991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2002, 2002991, 0.52987640277, 2002992, 0.52987640277, 2002990)
    # Create element
    ops.element('forceBeamColumn', 2002, 2, 12, 2002, 2002)

    # Create geometric transformation
    ops.geomTransf('Linear', 2102, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2102990, 276.21626128, 0.00778439, 330.66184189, 0.07583517, 33.06618419, 0.26244737, -408.76735211, -0.00832151, -489.34036298, -0.08287254, -48.9340363, -0.26948474, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2102991, 409.90166329, 0.00814436, 490.69826067, 0.07958464, 49.06982607, 0.26619684, -540.48153234, -0.0086285, -647.01700822, -0.08484595, -64.70170082, -0.27145815, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2102990, 34737161.15832325, 0.165, 0.00415938, 0.0012375, 14473817.14930136, 0.00326155)
    ops.section('Aggregator', 2102991, 2102990, 'Mz')
    ops.section('Aggregator', 2102992, 2102991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2102, 2102991, 0.53587064921, 2102992, 0.53587064921, 2102990)
    # Create element
    ops.element('forceBeamColumn', 2102, 102, 112, 2102, 2102)

    # Create geometric transformation
    ops.geomTransf('Linear', 2202, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2202990, 262.67098522, 0.00760945, 315.94055686, 0.08117152, 31.59405569, 0.27225289, -388.81559375, -0.008141, -467.66724197, -0.08872976, -46.7667242, -0.27981113, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2202991, 389.52064107, 0.00796848, 468.51527261, 0.08511485, 46.85152726, 0.27619622, -513.77281005, -0.00844822, -617.96573218, -0.09075332, -61.79657322, -0.28183469, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2202990, 33547841.03735894, 0.165, 0.00415938, 0.0012375, 13978267.09889956, 0.00326155)
    ops.section('Aggregator', 2202991, 2202990, 'Mz')
    ops.section('Aggregator', 2202992, 2202991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2202, 2202991, 0.52333726365, 2202992, 0.52333726365, 2202990)
    # Create element
    ops.element('forceBeamColumn', 2202, 202, 212, 2202, 2202)

    # Create geometric transformation
    ops.geomTransf('Linear', 2302, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2302990, 245.09092214, 0.0087161, 294.58741971, 0.08163092, 29.45874197, 0.26917707, -362.64100729, -0.00935773, -435.87692962, -0.08923742, -43.58769296, -0.27678357, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2302991, 245.02712313, 0.00863711, 294.51073639, 0.07565514, 29.45107364, 0.26320129, -478.08286672, -0.00985449, -574.6324543, -0.08818365, -57.46324543, -0.2757298, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2302990, 33731082.54525032, 0.15, 0.003125, 0.001125, 14054617.72718763, 0.00281737)
    ops.section('Aggregator', 2302991, 2302990, 'Mz')
    ops.section('Aggregator', 2302992, 2302991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2302, 2302991, 0.53320209468, 2302992, 0.53320209468, 2302990)
    # Create element
    ops.element('forceBeamColumn', 2302, 302, 312, 2302, 2302)

    # Create geometric transformation
    ops.geomTransf('Linear', 2402, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2402990, 235.16374617, 0.00855966, 282.83192726, 0.08262924, 28.28319273, 0.27374086, -348.07096087, -0.00918646, -418.62566952, -0.09033121, -41.86256695, -0.28144283, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2402991, 234.99886782, 0.00848622, 282.63362773, 0.07664576, 28.26336277, 0.26775738, -458.84131758, -0.00967601, -551.84940822, -0.08933932, -55.18494082, -0.28045094, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2402990, 33569025.64963435, 0.15, 0.003125, 0.001125, 13987094.02068098, 0.00281737)
    ops.section('Aggregator', 2402991, 2402990, 'Mz')
    ops.section('Aggregator', 2402992, 2402991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2402, 2402991, 0.52325442002, 2402992, 0.52325442002, 2402990)
    # Create element
    ops.element('forceBeamColumn', 2402, 402, 412, 2402, 2402)

    # Create geometric transformation
    ops.geomTransf('Linear', 2502, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2502990, 267.37967662, 0.00772377, 321.44283455, 0.07998347, 32.14428346, 0.26911928, -395.77787079, -0.00826253, -475.80265729, -0.08742451, -47.58026573, -0.27656032, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2502991, 396.53298688, 0.00808741, 476.71045499, 0.0838677, 47.6710455, 0.27300352, -523.00668125, -0.00857359, -628.75665135, -0.08942126, -62.87566514, -0.27855707, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2502990, 33678446.56240132, 0.165, 0.00415938, 0.0012375, 14032686.06766722, 0.00326155)
    ops.section('Aggregator', 2502991, 2502990, 'Mz')
    ops.section('Aggregator', 2502992, 2502991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2502, 2502991, 0.52872059099, 2502992, 0.52872059099, 2502990)
    # Create element
    ops.element('forceBeamColumn', 2502, 502, 512, 2502, 2502)

    # Create geometric transformation
    ops.geomTransf('Linear', 2602, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2602990, 273.97656222, 0.00770784, 330.46368554, 0.08000784, 33.04636855, 0.26790118, -405.23556086, -0.00825984, -488.7850109, -0.08746598, -48.87850109, -0.27535932, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2602991, 406.71384024, 0.00806931, 490.56807457, 0.08418782, 49.05680746, 0.27208117, -536.0168459, -0.00856691, -646.53013006, -0.08977541, -64.65301301, -0.27766876, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2602990, 32795629.33712209, 0.165, 0.00415938, 0.0012375, 13664845.55713421, 0.00326155)
    ops.section('Aggregator', 2602991, 2602990, 'Mz')
    ops.section('Aggregator', 2602992, 2602991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2602, 2602991, 0.53221682326, 2602992, 0.53221682326, 2602990)
    # Create element
    ops.element('forceBeamColumn', 2602, 602, 612, 2602, 2602)

    # Create geometric transformation
    ops.geomTransf('Linear', 2702, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2702990, 237.46901292, 0.00892115, 286.8455028, 0.07360073, 28.68455028, 0.26337868, -237.46901292, -0.00892115, -286.8455028, -0.07360073, -28.68455028, -0.26337868, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2702991, 237.5216885, 0.00880567, 286.90913112, 0.07061268, 28.69091311, 0.26039062, -351.09806333, -0.00954295, -424.10123017, -0.07725379, -42.41012302, -0.26703174, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2702990, 32389400.24606666, 0.125, 0.00260417, 0.00065104, 13495583.43586111, 0.00178813)
    ops.section('Aggregator', 2702991, 2702990, 'Mz')
    ops.section('Aggregator', 2702992, 2702991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2702, 2702991, 0.52693161564, 2702992, 0.52693161564, 2702990)
    # Create element
    ops.element('forceBeamColumn', 2702, 702, 712, 2702, 2702)

    # Create geometric transformation
    ops.geomTransf('Linear', 2012, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2012990, 235.28140804, 0.00897652, 284.55611254, 0.07685844, 28.45561125, 0.26616578, -347.95265893, -0.00972614, -420.82396904, -0.08409217, -42.0823969, -0.27339952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2012991, 348.33867937, 0.0095789, 421.29083327, 0.07891897, 42.12908333, 0.26822632, -348.33867937, -0.0095789, -421.29083327, -0.07891897, -42.12908333, -0.26822632, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2012990, 32032460.19816848, 0.125, 0.00260417, 0.00065104, 13346858.41590353, 0.00178813)
    ops.section('Aggregator', 2012991, 2012990, 'Mz')
    ops.section('Aggregator', 2012992, 2012991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2012, 2012991, 0.5282415105699999, 2012992, 0.5282415105699999, 2012990)
    # Create element
    ops.element('forceBeamColumn', 2012, 12, 22, 2012, 2012)

    # Create geometric transformation
    ops.geomTransf('Linear', 2112, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2112990, 390.58813208, 0.00813407, 471.27505642, 0.08635124, 47.12750564, 0.2762012, -515.25608528, -0.00862891, -621.69666898, -0.0920764, -62.1696669, -0.28192636, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2112991, 516.50966669, 0.00843798, 623.20921276, 0.09085093, 62.32092128, 0.28070089, -639.75417581, -0.00889716, -771.91332899, -0.09555348, -77.1913329, -0.28540344, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2112990, 32703233.53263032, 0.165, 0.00415938, 0.0012375, 13626347.30526264, 0.00326155)
    ops.section('Aggregator', 2112991, 2112990, 'Mz')
    ops.section('Aggregator', 2112992, 2112991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2112, 2112991, 0.52673173622, 2112992, 0.52673173622, 2112990)
    # Create element
    ops.element('forceBeamColumn', 2112, 112, 122, 2112, 2112)

    # Create geometric transformation
    ops.geomTransf('Linear', 2212, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2212990, 397.67517602, 0.00794502, 478.33019252, 0.08473574, 47.83301925, 0.27475267, -524.27966075, -0.008427, -630.61213317, -0.09035266, -63.06121332, -0.28036959, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2212991, 525.41902473, 0.00832668, 631.98257876, 0.08689745, 63.19825788, 0.27691438, -525.41902473, -0.00832668, -631.98257876, -0.08689745, -63.19825788, -0.27691438, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2212990, 33544206.29718937, 0.165, 0.00415938, 0.0012375, 13976752.6238289, 0.00326155)
    ops.section('Aggregator', 2212991, 2212990, 'Mz')
    ops.section('Aggregator', 2212992, 2212991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2212, 2212991, 0.52626889337, 2212992, 0.52626889337, 2212990)
    # Create element
    ops.element('forceBeamColumn', 2212, 212, 222, 2212, 2212)

    # Create geometric transformation
    ops.geomTransf('Linear', 2312, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2312990, 241.67055821, 0.00875314, 291.39705376, 0.08487745, 29.13970538, 0.27259573, -471.79263975, -0.00999557, -568.86939902, -0.09896794, -56.8869399, -0.28668622, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2312991, 358.34976999, 0.00926658, 432.08435468, 0.08781879, 43.20843547, 0.27553707, -472.65934882, -0.00985842, -569.91444344, -0.09366337, -56.99144434, -0.28138165, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2312990, 32889842.00001991, 0.15, 0.003125, 0.001125, 13704100.83334163, 0.00281737)
    ops.section('Aggregator', 2312991, 2312990, 'Mz')
    ops.section('Aggregator', 2312992, 2312991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2312, 2312991, 0.53271317177, 2312992, 0.53271317177, 2312990)
    # Create element
    ops.element('forceBeamColumn', 2312, 312, 322, 2312, 2312)

    # Create geometric transformation
    ops.geomTransf('Linear', 2412, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2412990, 242.33019935, 0.00842241, 291.28093045, 0.08224394, 29.12809304, 0.2718962, -472.56726352, -0.00961551, -568.02591087, -0.09589644, -56.80259109, -0.2855487, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2412991, 359.50895581, 0.00891258, 432.12981063, 0.08485193, 43.21298106, 0.27450419, -473.88615181, -0.00948036, -569.61121476, -0.09049772, -56.96112148, -0.28014998, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2412990, 33720650.36498053, 0.15, 0.003125, 0.001125, 14050270.98540856, 0.00281737)
    ops.section('Aggregator', 2412991, 2412990, 'Mz')
    ops.section('Aggregator', 2412992, 2412991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2412, 2412991, 0.52728082103, 2412992, 0.52728082103, 2412990)
    # Create element
    ops.element('forceBeamColumn', 2412, 412, 422, 2412, 2412)

    # Create geometric transformation
    ops.geomTransf('Linear', 2512, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2512990, 403.75894929, 0.00813171, 488.51275699, 0.08680375, 48.8512757, 0.27481309, -532.18477254, -0.00863945, -643.89668865, -0.09257223, -64.38966886, -0.28058157, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2512991, 533.42421646, 0.00853112, 645.3963066, 0.08900408, 64.53963066, 0.27701343, -533.42421646, -0.00853112, -645.3963066, -0.08900408, -64.53963066, -0.27701343, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2512990, 31915652.84606848, 0.165, 0.00415938, 0.0012375, 13298188.68586187, 0.00326155)
    ops.section('Aggregator', 2512991, 2512990, 'Mz')
    ops.section('Aggregator', 2512992, 2512991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2512, 2512991, 0.53188845678, 2512992, 0.53188845678, 2512990)
    # Create element
    ops.element('forceBeamColumn', 2512, 512, 522, 2512, 2512)

    # Create geometric transformation
    ops.geomTransf('Linear', 2612, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2612990, 399.54178335, 0.00808594, 482.86851681, 0.08630544, 48.28685168, 0.27521446, -526.72331486, -0.00858685, -636.57448711, -0.09203683, -63.65744871, -0.28094585, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2612991, 527.85103446, 0.00848125, 637.93739911, 0.08850316, 63.79373991, 0.27741218, -527.85103446, -0.00848125, -637.93739911, -0.08850316, -63.79373991, -0.27741218, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2612990, 32241189.02235328, 0.165, 0.00415938, 0.0012375, 13433828.75931387, 0.00326155)
    ops.section('Aggregator', 2612991, 2612990, 'Mz')
    ops.section('Aggregator', 2612992, 2612991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2612, 2612991, 0.52935535019, 2612992, 0.52935535019, 2612990)
    # Create element
    ops.element('forceBeamColumn', 2612, 612, 622, 2612, 2612)

    # Create geometric transformation
    ops.geomTransf('Linear', 2712, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2712990, 239.84477905, 0.0088686, 288.06567013, 0.07279839, 28.80656701, 0.26138455, -354.6497171, -0.00959003, -425.95218802, -0.07962643, -42.5952188, -0.26821259, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2712991, 355.20671742, 0.00944892, 426.62117348, 0.07510746, 42.66211735, 0.26369362, -355.20671742, -0.00944892, -426.62117348, -0.07510746, -42.66211735, -0.26369362, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2712990, 33923432.3173915, 0.125, 0.00260417, 0.00065104, 14134763.46557979, 0.00178813)
    ops.section('Aggregator', 2712991, 2712990, 'Mz')
    ops.section('Aggregator', 2712992, 2712991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2712, 2712991, 0.53026160897, 2712992, 0.53026160897, 2712990)
    # Create element
    ops.element('forceBeamColumn', 2712, 712, 722, 2712, 2712)

    # Create geometric transformation
    ops.geomTransf('Linear', 2022, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2022990, 359.82918758, 0.00947305, 435.66639723, 0.10835324, 43.56663972, 0.32400239, -359.82918758, -0.00947305, -435.66639723, -0.10835324, -43.56663972, -0.32400239, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2022991, 359.82918758, 0.00947305, 435.66639723, 0.10908362, 43.56663972, 0.32473277, -359.82918758, -0.00947305, -435.66639723, -0.10908362, -43.56663972, -0.32473277, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2022990, 31708524.98393104, 0.125, 0.00260417, 0.00065104, 13211885.40997127, 0.00178813)
    ops.section('Aggregator', 2022991, 2022990, 'Mz')
    ops.section('Aggregator', 2022992, 2022991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2022, 2022991, 0.46371617657, 2022992, 0.46371617657, 2022990)
    # Create element
    ops.element('forceBeamColumn', 2022, 22, 32, 2022, 2022)

    # Create geometric transformation
    ops.geomTransf('Linear', 2122, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2122990, 535.47276597, 0.00840948, 647.48140736, 0.13152584, 64.74814074, 0.34711396, -662.67570345, -0.00887776, -801.29228668, -0.13833326, -80.12922867, -0.35392138, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2122991, 535.47276597, 0.00840948, 647.48140736, 0.12975158, 64.74814074, 0.3453397, -662.67570345, -0.00887776, -801.29228668, -0.13646765, -80.12922867, -0.35205576, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2122990, 32092946.64905696, 0.165, 0.00415938, 0.0012375, 13372061.10377373, 0.00326155)
    ops.section('Aggregator', 2122991, 2122990, 'Mz')
    ops.section('Aggregator', 2122992, 2122991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2122, 2122991, 0.46384746148, 2122992, 0.46384746148, 2122990)
    # Create element
    ops.element('forceBeamColumn', 2122, 122, 132, 2122, 2122)

    # Create geometric transformation
    ops.geomTransf('Linear', 2222, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2222990, 531.07244076, 0.00845743, 643.70217101, 0.13166573, 64.3702171, 0.34838389, -531.07244076, -0.00845743, -643.70217101, -0.13166573, -64.3702171, -0.34838389, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2222991, 532.16242681, 0.00835718, 645.02332107, 0.13341878, 64.50233211, 0.35013693, -658.47394023, -0.00882905, -798.12295339, -0.14032995, -79.81229534, -0.35704811, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2222990, 31379376.72707991, 0.165, 0.00415938, 0.0012375, 13074740.30294996, 0.00326155)
    ops.section('Aggregator', 2222991, 2222990, 'Mz')
    ops.section('Aggregator', 2222992, 2222991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2222, 2222991, 0.46142880963, 2222992, 0.46142880963, 2222990)
    # Create element
    ops.element('forceBeamColumn', 2222, 222, 232, 2222, 2222)

    # Create geometric transformation
    ops.geomTransf('Linear', 2322, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2322990, 355.47117998, 0.00913974, 426.13029053, 0.12281406, 42.61302905, 0.33939222, -468.95344265, -0.0097081, -562.17009428, -0.13098374, -56.21700943, -0.34756189, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2322991, 355.47117998, 0.00913974, 426.13029053, 0.12286813, 42.61302905, 0.33944628, -468.95344265, -0.0097081, -562.17009428, -0.13104142, -56.21700943, -0.34761957, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2322990, 34398536.28080919, 0.15, 0.003125, 0.001125, 14332723.45033716, 0.00281737)
    ops.section('Aggregator', 2322991, 2322990, 'Mz')
    ops.section('Aggregator', 2322992, 2322991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2322, 2322991, 0.46172708785, 2322992, 0.46172708785, 2322990)
    # Create element
    ops.element('forceBeamColumn', 2322, 322, 332, 2322, 2322)

    # Create geometric transformation
    ops.geomTransf('Linear', 2422, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2422990, 346.45955344, 0.00914916, 417.00976812, 0.12561196, 41.70097681, 0.34435415, -457.16771131, -0.00972424, -550.26163773, -0.13397482, -55.02616377, -0.35271701, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2422991, 346.45955344, 0.00914916, 417.00976812, 0.12481267, 41.70097681, 0.34355486, -457.16771131, -0.00972424, -550.26163773, -0.13312208, -55.02616377, -0.35186427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2422990, 33365828.80807327, 0.15, 0.003125, 0.001125, 13902428.67003053, 0.00281737)
    ops.section('Aggregator', 2422991, 2422990, 'Mz')
    ops.section('Aggregator', 2422992, 2422991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2422, 2422991, 0.45715917961, 2422992, 0.45715917961, 2422990)
    # Create element
    ops.element('forceBeamColumn', 2422, 422, 432, 2422, 2422)

    # Create geometric transformation
    ops.geomTransf('Linear', 2522, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2522990, 530.31993459, 0.00864934, 640.18432751, 0.12687277, 64.01843275, 0.34168029, -530.31993459, -0.00864934, -640.18432751, -0.12687277, -64.01843275, -0.34168029, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2522991, 530.31993459, 0.00864934, 640.18432751, 0.12737275, 64.01843275, 0.34218027, -530.31993459, -0.00864934, -640.18432751, -0.12737275, -64.01843275, -0.34218027, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2522990, 32567324.30112639, 0.165, 0.00415938, 0.0012375, 13569718.45880266, 0.00326155)
    ops.section('Aggregator', 2522991, 2522990, 'Mz')
    ops.section('Aggregator', 2522992, 2522991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2522, 2522991, 0.46553304282, 2522992, 0.46553304282, 2522990)
    # Create element
    ops.element('forceBeamColumn', 2522, 522, 532, 2522, 2522)

    # Create geometric transformation
    ops.geomTransf('Linear', 2622, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2622990, 538.90755076, 0.00852226, 650.16834559, 0.12662968, 65.01683456, 0.34128489, -538.90755076, -0.00852226, -650.16834559, -0.12662968, -65.01683456, -0.34128489, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2622991, 539.94960359, 0.00842546, 651.42553667, 0.12960709, 65.14255367, 0.3442623, -668.22178886, -0.00888978, -806.18030744, -0.13631094, -80.61803074, -0.35096615, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2622990, 32731229.11338743, 0.165, 0.00415938, 0.0012375, 13638012.1305781, 0.00326155)
    ops.section('Aggregator', 2622991, 2622990, 'Mz')
    ops.section('Aggregator', 2622992, 2622991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2622, 2622991, 0.46586337765, 2622992, 0.46586337765, 2622990)
    # Create element
    ops.element('forceBeamColumn', 2622, 622, 632, 2622, 2622)

    # Create geometric transformation
    ops.geomTransf('Linear', 2722, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2722990, 352.91770855, 0.00949324, 429.9727974, 0.11393821, 42.99727974, 0.33146722, -352.91770855, -0.00949324, -429.9727974, -0.11393821, -42.99727974, -0.33146722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2722991, 352.91770855, 0.00949324, 429.9727974, 0.11408319, 42.99727974, 0.33161219, -352.91770855, -0.00949324, -429.9727974, -0.11408319, -42.99727974, -0.33161219, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2722990, 29703917.02438633, 0.125, 0.00260417, 0.00065104, 12376632.0934943, 0.00178813)
    ops.section('Aggregator', 2722991, 2722990, 'Mz')
    ops.section('Aggregator', 2722992, 2722991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2722, 2722991, 0.45970881604, 2722992, 0.45970881604, 2722990)
    # Create element
    ops.element('forceBeamColumn', 2722, 722, 732, 2722, 2722)

    # Create geometric transformation
    ops.geomTransf('Linear', 2032, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2032990, 354.10748204, 0.00954759, 427.97958898, 0.07781166, 42.7979589, 0.26628535, -354.10748204, -0.00954759, -427.97958898, -0.07781166, -42.7979589, -0.26628535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2032991, 239.12785759, 0.00894839, 289.01349843, 0.07531395, 28.90134984, 0.26378765, -353.52786889, -0.00969768, -427.27905987, -0.08240252, -42.72790599, -0.27087621, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2032990, 32227133.92320176, 0.125, 0.00260417, 0.00065104, 13427972.46800073, 0.00178813)
    ops.section('Aggregator', 2032991, 2032990, 'Mz')
    ops.section('Aggregator', 2032992, 2032991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2032, 2032991, 0.5305780199900001, 2032992, 0.5305780199900001, 2032990)
    # Create element
    ops.element('forceBeamColumn', 2032, 32, 42, 2032, 2032)

    # Create geometric transformation
    ops.geomTransf('Linear', 2132, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2132990, 530.48438745, 0.00829069, 643.23301129, 0.09132337, 64.32330113, 0.28088443, -656.31436386, -0.0087605, -795.80676568, -0.09606845, -79.58067657, -0.28562951, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2132991, 400.66547767, 0.00799478, 485.82251961, 0.08836132, 48.58225196, 0.27792238, -527.90633293, -0.00850193, -640.10701963, -0.09424252, -64.01070196, -0.28380358, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2132990, 31263120.59906319, 0.165, 0.00415938, 0.0012375, 13026300.24960966, 0.00326155)
    ops.section('Aggregator', 2132991, 2132990, 'Mz')
    ops.section('Aggregator', 2132992, 2132991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2132, 2132991, 0.5275345062300001, 2132992, 0.5275345062300001, 2132990)
    # Create element
    ops.element('forceBeamColumn', 2132, 132, 142, 2132, 2132)

    # Create geometric transformation
    ops.geomTransf('Linear', 2232, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2232990, 532.0601659, 0.00848037, 640.04659465, 0.08678358, 64.00465946, 0.27444921, -658.83190325, -0.00893815, -792.54780408, -0.09127312, -79.25478041, -0.27893875, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2232991, 402.16696984, 0.00817928, 483.7903982, 0.08267002, 48.37903982, 0.27033566, -530.39045244, -0.00867296, -638.03799772, -0.08814485, -63.80379977, -0.27581048, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2232990, 33513139.31620337, 0.165, 0.00415938, 0.0012375, 13963808.04841807, 0.00326155)
    ops.section('Aggregator', 2232991, 2232990, 'Mz')
    ops.section('Aggregator', 2232992, 2232991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2232, 2232991, 0.5328626225499999, 2232992, 0.5328626225499999, 2232990)
    # Create element
    ops.element('forceBeamColumn', 2232, 232, 242, 2232, 2232)

    # Create geometric transformation
    ops.geomTransf('Linear', 2332, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2332990, 360.31931618, 0.00926327, 435.02554059, 0.08756249, 43.50255406, 0.27502687, -475.17218118, -0.00986017, -573.69123916, -0.09339521, -57.36912392, -0.28085958, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2332991, 242.97232825, 0.00874733, 293.34860414, 0.0854486, 29.33486041, 0.27291298, -474.18177227, -0.01000059, -572.49548542, -0.09964729, -57.24954854, -0.28711167, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2332990, 32528477.4961849, 0.15, 0.003125, 0.001125, 13553532.29007704, 0.00281737)
    ops.section('Aggregator', 2332991, 2332990, 'Mz')
    ops.section('Aggregator', 2332992, 2332991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2332, 2332991, 0.53343467762, 2332992, 0.53343467762, 2332990)
    # Create element
    ops.element('forceBeamColumn', 2332, 332, 342, 2332, 2332)

    # Create geometric transformation
    ops.geomTransf('Linear', 2432, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2432990, 354.38679979, 0.00906816, 430.04164923, 0.09203588, 43.00416492, 0.28195834, -467.14667597, -0.00967117, -566.87361686, -0.09818689, -56.68736169, -0.28810934, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2432991, 238.93918326, 0.00855254, 289.94815974, 0.08940786, 28.99481597, 0.27933032, -465.91825715, -0.00981889, -565.38295397, -0.10432075, -56.5382954, -0.29424321, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2432990, 31021575.41619943, 0.15, 0.003125, 0.001125, 12925656.42341643, 0.00281737)
    ops.section('Aggregator', 2432991, 2432990, 'Mz')
    ops.section('Aggregator', 2432992, 2432991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2432, 2432991, 0.52653067499, 2432992, 0.52653067499, 2432990)
    # Create element
    ops.element('forceBeamColumn', 2432, 432, 442, 2432, 2432)

    # Create geometric transformation
    ops.geomTransf('Linear', 2532, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2532990, 524.48349501, 0.00838447, 630.75780734, 0.08719489, 63.07578073, 0.276905, -524.48349501, -0.00838447, -630.75780734, -0.08719489, -63.07578073, -0.276905, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2532991, 396.97595283, 0.00800043, 477.41384421, 0.08492675, 47.74138442, 0.27463686, -523.45792493, -0.00848407, -629.52442948, -0.0905544, -62.95244295, -0.28026451, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2532990, 33585400.57704963, 0.165, 0.00415938, 0.0012375, 13993916.90710401, 0.00326155)
    ops.section('Aggregator', 2532991, 2532990, 'Mz')
    ops.section('Aggregator', 2532992, 2532991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2532, 2532991, 0.5271200392900001, 2532992, 0.5271200392900001, 2532990)
    # Create element
    ops.element('forceBeamColumn', 2532, 532, 542, 2532, 2532)

    # Create geometric transformation
    ops.geomTransf('Linear', 2632, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2632990, 527.0535554, 0.00830214, 637.51268631, 0.09130692, 63.75126863, 0.28103377, -652.28203288, -0.00876492, -788.98636914, -0.09604353, -78.89863691, -0.28577038, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2632991, 398.18714457, 0.00800618, 481.63863727, 0.08674149, 48.16386373, 0.27646833, -524.83202912, -0.00850554, -634.82557574, -0.09250583, -63.48255757, -0.28223267, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2632990, 31996349.90704375, 0.165, 0.00415938, 0.0012375, 13331812.46126823, 0.00326155)
    ops.section('Aggregator', 2632991, 2632990, 'Mz')
    ops.section('Aggregator', 2632992, 2632991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2632, 2632991, 0.52707354793, 2632992, 0.52707354793, 2632990)
    # Create element
    ops.element('forceBeamColumn', 2632, 632, 642, 2632, 2632)

    # Create geometric transformation
    ops.geomTransf('Linear', 2732, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2732990, 350.50909346, 0.0094237, 420.76889367, 0.07461828, 42.07688937, 0.26413555, -350.50909346, -0.0094237, -420.76889367, -0.07461828, -42.07688937, -0.26413555, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2732991, 236.69972522, 0.00884603, 284.1463556, 0.07210847, 28.41463556, 0.26162574, -350.08047884, -0.00956127, -420.25436293, -0.07886658, -42.02543629, -0.26838385, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2732990, 34050115.51127616, 0.125, 0.00260417, 0.00065104, 14187548.1296984, 0.00178813)
    ops.section('Aggregator', 2732991, 2732990, 'Mz')
    ops.section('Aggregator', 2732992, 2732991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2732, 2732991, 0.5276564037000001, 2732992, 0.5276564037000001, 2732990)
    # Create element
    ops.element('forceBeamColumn', 2732, 732, 742, 2732, 2732)

    # Create geometric transformation
    ops.geomTransf('Linear', 2042, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2042990, 240.80812628, 0.00895737, 290.43086652, 0.06325692, 29.04308665, 0.25117294, -356.02119853, -0.00970018, -429.38561412, -0.06918645, -42.93856141, -0.25710247, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2042991, 240.79853071, 0.0090717, 290.41929362, 0.06669614, 29.04192936, 0.25461216, -240.79853071, -0.0090717, -290.41929362, -0.06669614, -29.04192936, -0.25461216, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2042990, 32820172.11654161, 0.125, 0.00260417, 0.00065104, 13675071.71522567, 0.00178813)
    ops.section('Aggregator', 2042991, 2042990, 'Mz')
    ops.section('Aggregator', 2042992, 2042991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2042, 2042991, 0.53215261316, 2042992, 0.53215261316, 2042990)
    # Create element
    ops.element('forceBeamColumn', 2042, 42, 52, 2042, 2042)

    # Create geometric transformation
    ops.geomTransf('Linear', 2142, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2142990, 399.54090681, 0.00805309, 481.60336223, 0.08380087, 48.16033622, 0.27283626, -526.76800632, -0.00854557, -634.96187408, -0.08935855, -63.49618741, -0.27839394, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2142991, 269.27878315, 0.00769073, 324.58645694, 0.07998631, 32.45864569, 0.26902169, -398.43856331, -0.00823671, -480.27460634, -0.08743801, -48.02746063, -0.27647339, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2142990, 32973549.80633813, 0.165, 0.00415938, 0.0012375, 13738979.08597422, 0.00326155)
    ops.section('Aggregator', 2142991, 2142990, 'Mz')
    ops.section('Aggregator', 2142992, 2142991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2142, 2142991, 0.52900148341, 2142992, 0.52900148341, 2142990)
    # Create element
    ops.element('forceBeamColumn', 2142, 142, 152, 2142, 2142)

    # Create geometric transformation
    ops.geomTransf('Linear', 2242, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2242990, 393.12498537, 0.0080738, 476.18125352, 0.08674329, 47.61812535, 0.27680522, -518.34002945, -0.0085782, -627.85071965, -0.09250826, -62.78507196, -0.28257019, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2242991, 265.04590104, 0.00770424, 321.04265589, 0.08293704, 32.10426559, 0.27299897, -392.17553228, -0.00826297, -475.03120766, -0.09068205, -47.50312077, -0.28074398, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2242990, 31581598.07857012, 0.165, 0.00415938, 0.0012375, 13158999.19940422, 0.00326155)
    ops.section('Aggregator', 2242991, 2242990, 'Mz')
    ops.section('Aggregator', 2242992, 2242991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2242, 2242991, 0.52614429365, 2242992, 0.52614429365, 2242990)
    # Create element
    ops.element('forceBeamColumn', 2242, 242, 252, 2242, 2242)

    # Create geometric transformation
    ops.geomTransf('Linear', 2342, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2342990, 240.20694817, 0.00867838, 289.33067595, 0.06979445, 28.93306759, 0.25833761, -468.94975303, -0.00990441, -564.85272414, -0.08133549, -56.48527241, -0.26987864, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2342991, 240.36709715, 0.00875479, 289.52357634, 0.07474528, 28.95235763, 0.26328843, -355.74821771, -0.00940066, -428.50081184, -0.0816946, -42.85008118, -0.27023775, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2342990, 33172313.74788621, 0.15, 0.003125, 0.001125, 13821797.39495259, 0.00281737)
    ops.section('Aggregator', 2342991, 2342990, 'Mz')
    ops.section('Aggregator', 2342992, 2342991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2342, 2342991, 0.53038256429, 2342992, 0.53038256429, 2342990)
    # Create element
    ops.element('forceBeamColumn', 2342, 342, 352, 2342, 2342)

    # Create geometric transformation
    ops.geomTransf('Linear', 2442, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2442990, 248.27113528, 0.00860473, 299.38158738, 0.06840457, 29.93815874, 0.25546594, -483.90754773, -0.00984526, -583.52739888, -0.07973795, -58.35273989, -0.26679933, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2442991, 248.22068054, 0.00868979, 299.32074575, 0.07393584, 29.93207457, 0.26099721, -367.07319119, -0.00934379, -442.64088348, -0.08082218, -44.26408835, -0.26788356, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2442990, 32866211.64803222, 0.15, 0.003125, 0.001125, 13694254.85334676, 0.00281737)
    ops.section('Aggregator', 2442991, 2442990, 'Mz')
    ops.section('Aggregator', 2442992, 2442991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2442, 2442991, 0.53458390936, 2442992, 0.53458390936, 2442990)
    # Create element
    ops.element('forceBeamColumn', 2442, 442, 452, 2442, 2442)

    # Create geometric transformation
    ops.geomTransf('Linear', 2542, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2542990, 402.16438448, 0.00787474, 478.82588552, 0.07882874, 47.88258855, 0.268356, -530.26078039, -0.00833462, -631.34031139, -0.08403327, -63.13403114, -0.27356053, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2542991, 270.93239672, 0.00753159, 322.57815406, 0.07531869, 32.25781541, 0.26484595, -400.95140379, -0.00804215, -477.38168365, -0.08230431, -47.73816837, -0.27183157, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2542990, 35993656.06254683, 0.165, 0.00415938, 0.0012375, 14997356.69272785, 0.00326155)
    ops.section('Aggregator', 2542991, 2542990, 'Mz')
    ops.section('Aggregator', 2542992, 2542991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2542, 2542991, 0.5276285844799999, 2542992, 0.5276285844799999, 2542990)
    # Create element
    ops.element('forceBeamColumn', 2542, 542, 552, 2542, 2542)

    # Create geometric transformation
    ops.geomTransf('Linear', 2642, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2642990, 395.97214052, 0.00805884, 477.8970938, 0.08550353, 47.78970938, 0.27508232, -522.12539488, -0.00855343, -630.15092044, -0.09117679, -63.01509204, -0.28075558, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2642991, 266.93802817, 0.00769401, 322.16637191, 0.08129373, 32.21663719, 0.27087252, -395.01329169, -0.00824211, -476.73986323, -0.08887211, -47.67398632, -0.2784509, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2642990, 32629978.94395714, 0.165, 0.00415938, 0.0012375, 13595824.55998214, 0.00326155)
    ops.section('Aggregator', 2642991, 2642990, 'Mz')
    ops.section('Aggregator', 2642992, 2642991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2642, 2642991, 0.5274851628599999, 2642992, 0.5274851628599999, 2642990)
    # Create element
    ops.element('forceBeamColumn', 2642, 642, 652, 2642, 2642)

    # Create geometric transformation
    ops.geomTransf('Linear', 2742, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2742990, 238.55798787, 0.0087202, 285.92520822, 0.06200649, 28.59252082, 0.25181792, -352.70693385, -0.00942542, -422.73916041, -0.06780164, -42.27391604, -0.25761308, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2742991, 238.51017983, 0.00882779, 285.86790758, 0.06481836, 28.58679076, 0.25462979, -238.51017983, -0.00882779, -285.86790758, -0.06481836, -28.58679076, -0.25462979, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2742990, 34443629.45026185, 0.125, 0.00260417, 0.00065104, 14351512.27094244, 0.00178813)
    ops.section('Aggregator', 2742991, 2742990, 'Mz')
    ops.section('Aggregator', 2742992, 2742991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2742, 2742991, 0.52683865294, 2742992, 0.52683865294, 2742990)
    # Create element
    ops.element('forceBeamColumn', 2742, 742, 752, 2742, 2742)

    # Create geometric transformation
    ops.geomTransf('Linear', 2003, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2003990, 241.8386046, 0.00881999, 290.13874977, 0.07140536, 29.01387498, 0.26046583, -241.8386046, -0.00881999, -290.13874977, -0.07140536, -29.01387498, -0.26046583, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2003991, 242.00730696, 0.00870765, 290.34114547, 0.06792177, 29.03411455, 0.25698224, -357.65320338, -0.00941878, -429.08390682, -0.07428907, -42.90839068, -0.26334954, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2003990, 34202971.72877697, 0.125, 0.00260417, 0.00065104, 14251238.22032374, 0.00178813)
    ops.section('Aggregator', 2003991, 2003990, 'Mz')
    ops.section('Aggregator', 2003992, 2003991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2003, 2003991, 0.5289312986700001, 2003992, 0.5289312986700001, 2003990)
    # Create element
    ops.element('forceBeamColumn', 2003, 3, 13, 2003, 2003)

    # Create geometric transformation
    ops.geomTransf('Linear', 2103, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2103990, 247.4894318, 0.00855077, 298.11047085, 0.08064797, 29.81104709, 0.26877628, -365.90667264, -0.00919351, -440.74855914, -0.08817747, -44.07485591, -0.27630578, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2103991, 247.60302308, 0.00846556, 298.24729589, 0.07531492, 29.82472959, 0.26344323, -482.38516903, -0.0096844, -581.0513557, -0.0878164, -58.10513557, -0.27594472, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2103990, 33165107.76771796, 0.15, 0.003125, 0.001125, 13818794.90321582, 0.00281737)
    ops.section('Aggregator', 2103991, 2103990, 'Mz')
    ops.section('Aggregator', 2103992, 2103991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2103, 2103991, 0.53155210235, 2103992, 0.53155210235, 2103990)
    # Create element
    ops.element('forceBeamColumn', 2103, 103, 113, 2103, 2103)

    # Create geometric transformation
    ops.geomTransf('Linear', 2203, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2203990, 250.76360588, 0.00849814, 302.23617267, 0.08219209, 30.22361727, 0.26992061, -370.53738791, -0.00914308, -446.59511719, -0.08987632, -44.65951172, -0.27760484, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2203991, 251.00157048, 0.00840913, 302.52298268, 0.07558679, 30.25229827, 0.26331531, -488.48248557, -0.00963173, -588.75001554, -0.08814746, -58.87500155, -0.27587598, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2203990, 33002556.37064884, 0.15, 0.003125, 0.001125, 13751065.15443702, 0.00281737)
    ops.section('Aggregator', 2203991, 2203990, 'Mz')
    ops.section('Aggregator', 2203992, 2203991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2203, 2203991, 0.53268411551, 2203992, 0.53268411551, 2203990)
    # Create element
    ops.element('forceBeamColumn', 2203, 203, 213, 2203, 2203)

    # Create geometric transformation
    ops.geomTransf('Linear', 2303, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2303990, 241.33693906, 0.00881458, 291.37749775, 0.07521177, 29.13774978, 0.26395417, -356.62680918, -0.00955428, -430.57240924, -0.08229377, -43.05724092, -0.27103617, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2303991, 241.33693906, 0.00881458, 291.37749775, 0.07570085, 29.13774978, 0.26444325, -356.62680918, -0.00955428, -430.57240924, -0.08282957, -43.05724092, -0.27157197, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2303990, 32525243.09843915, 0.125, 0.00260417, 0.00065104, 13552184.62434964, 0.00178813)
    ops.section('Aggregator', 2303991, 2303990, 'Mz')
    ops.section('Aggregator', 2303992, 2303991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2303, 2303991, 0.5298226553, 2303992, 0.5298226553, 2303990)
    # Create element
    ops.element('forceBeamColumn', 2303, 303, 313, 2303, 2303)

    # Create geometric transformation
    ops.geomTransf('Linear', 2403, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2403990, 242.66873163, 0.00861687, 293.01499331, 0.08343931, 29.30149933, 0.27238719, -358.93918224, -0.00926689, -433.40796887, -0.09123641, -43.34079689, -0.28018429, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2403991, 242.65527272, 0.00853401, 292.99874209, 0.07688045, 29.29987421, 0.26582833, -473.16330994, -0.00976732, -571.33007275, -0.08964909, -57.13300727, -0.27859696, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2403990, 32496860.11117297, 0.15, 0.003125, 0.001125, 13540358.3796554, 0.00281737)
    ops.section('Aggregator', 2403991, 2403990, 'Mz')
    ops.section('Aggregator', 2403992, 2403991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2403, 2403991, 0.52924648604, 2403992, 0.52924648604, 2403990)
    # Create element
    ops.element('forceBeamColumn', 2403, 403, 413, 2403, 2403)

    # Create geometric transformation
    ops.geomTransf('Linear', 2503, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2503990, 244.85571787, 0.00867217, 294.41126441, 0.08106315, 29.44112644, 0.26896578, -362.25702199, -0.00931264, -435.57303383, -0.08861845, -43.55730338, -0.27652108, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2503991, 244.81606629, 0.00859242, 294.36358788, 0.07499558, 29.43635879, 0.2628982, -477.57741199, -0.0098075, -574.23273974, -0.087418, -57.42327397, -0.27532063, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2503990, 33637330.58855011, 0.15, 0.003125, 0.001125, 14015554.41189588, 0.00281737)
    ops.section('Aggregator', 2503991, 2503990, 'Mz')
    ops.section('Aggregator', 2503992, 2503991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2503, 2503991, 0.53219055259, 2503992, 0.53219055259, 2503990)
    # Create element
    ops.element('forceBeamColumn', 2503, 503, 513, 2503, 2503)

    # Create geometric transformation
    ops.geomTransf('Linear', 2603, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2603990, 244.51909257, 0.00851778, 294.03806915, 0.08194114, 29.40380692, 0.27095905, -361.62984714, -0.00915085, -434.86560041, -0.08958764, -43.48656004, -0.27860555, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2603991, 244.56888721, 0.00843608, 294.097948, 0.07620348, 29.4097948, 0.26522139, -476.76058167, -0.00963674, -573.31212631, -0.08884174, -57.33121263, -0.27785965, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2603990, 33609413.09645505, 0.15, 0.003125, 0.001125, 14003922.12352294, 0.00281737)
    ops.section('Aggregator', 2603991, 2603990, 'Mz')
    ops.section('Aggregator', 2603992, 2603991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2603, 2603991, 0.5290504018200001, 2603992, 0.5290504018200001, 2603990)
    # Create element
    ops.element('forceBeamColumn', 2603, 603, 613, 2603, 2603)

    # Create geometric transformation
    ops.geomTransf('Linear', 2703, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2703990, 236.48623888, 0.0091565, 285.35355472, 0.07354307, 28.53535547, 0.26205172, -236.48623888, -0.0091565, -285.35355472, -0.07354307, -28.53535547, -0.26205172, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2703991, 236.3228042, 0.00904775, 285.15634804, 0.06985952, 28.5156348, 0.25836817, -349.5622031, -0.00979255, -421.79544028, -0.0764131, -42.17954403, -0.26492175, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2703990, 32689168.13257025, 0.125, 0.00260417, 0.00065104, 13620486.72190427, 0.00178813)
    ops.section('Aggregator', 2703991, 2703990, 'Mz')
    ops.section('Aggregator', 2703992, 2703991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2703, 2703991, 0.53047962157, 2703992, 0.53047962157, 2703990)
    # Create element
    ops.element('forceBeamColumn', 2703, 703, 713, 2703, 2703)

    # Create geometric transformation
    ops.geomTransf('Linear', 2013, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2013990, 234.31804907, 0.00880759, 281.39298781, 0.07350682, 28.13929878, 0.26390031, -346.58559795, -0.00951959, -416.21529936, -0.08039892, -41.62152994, -0.27079241, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2013991, 346.95945889, 0.00938338, 416.66426966, 0.07568982, 41.66642697, 0.26608332, -346.95945889, -0.00938338, -416.66426966, -0.07568982, -41.66642697, -0.26608332, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2013990, 33954903.88642378, 0.125, 0.00260417, 0.00065104, 14147876.61934324, 0.00178813)
    ops.section('Aggregator', 2013991, 2013990, 'Mz')
    ops.section('Aggregator', 2013992, 2013991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2013, 2013991, 0.52522802797, 2013992, 0.52522802797, 2013990)
    # Create element
    ops.element('forceBeamColumn', 2013, 13, 23, 2013, 2013)

    # Create geometric transformation
    ops.geomTransf('Linear', 2113, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2113990, 234.67411511, 0.00874841, 284.05101746, 0.08716327, 28.40510175, 0.27683476, -458.30001019, -0.01000513, -554.72920026, -0.10165464, -55.47292003, -0.29132612, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2113991, 459.32683873, 0.00974319, 555.97207995, 0.10670859, 55.597208, 0.29638007, -459.32683873, -0.00974319, -555.97207995, -0.10670859, -55.597208, -0.29638007, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2113990, 31795128.45563447, 0.15, 0.003125, 0.001125, 13247970.18984769, 0.00281737)
    ops.section('Aggregator', 2113991, 2113990, 'Mz')
    ops.section('Aggregator', 2113992, 2113991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2113, 2113991, 0.5272273744, 2113992, 0.5272273744, 2113990)
    # Create element
    ops.element('forceBeamColumn', 2113, 113, 123, 2113, 2113)

    # Create geometric transformation
    ops.geomTransf('Linear', 2213, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2213990, 247.21189636, 0.00879105, 297.43491275, 0.0835088, 29.74349127, 0.269546, -482.44111841, -0.01003265, -580.45277786, -0.09736104, -58.04527779, -0.28339825, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2213991, 484.32858627, 0.00976986, 582.72369948, 0.10174952, 58.27236995, 0.28778672, -484.32858627, -0.00976986, -582.72369948, -0.10174952, -58.27236995, -0.28778672, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2213990, 33469782.70727253, 0.15, 0.003125, 0.001125, 13945742.79469689, 0.00281737)
    ops.section('Aggregator', 2213991, 2213990, 'Mz')
    ops.section('Aggregator', 2213992, 2213991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2213, 2213991, 0.5375268770599999, 2213992, 0.5375268770599999, 2213990)
    # Create element
    ops.element('forceBeamColumn', 2213, 213, 223, 2213, 2213)

    # Create geometric transformation
    ops.geomTransf('Linear', 2313, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2313990, 238.66046033, 0.0088487, 286.83399533, 0.07389659, 28.68339953, 0.26293157, -352.90328817, -0.00957018, -424.13670018, -0.08083149, -42.41367002, -0.26986646, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2313991, 353.44362664, 0.00942901, 424.7861058, 0.08493428, 42.47861058, 0.27396926, -353.44362664, -0.00942901, -424.7861058, -0.08493428, -42.47861058, -0.27396926, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2313990, 33752954.97386087, 0.125, 0.00260417, 0.00065104, 14063731.2391087, 0.00178813)
    ops.section('Aggregator', 2313991, 2313990, 'Mz')
    ops.section('Aggregator', 2313992, 2313991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2313, 2313991, 0.52900262518, 2313992, 0.52900262518, 2313990)
    # Create element
    ops.element('forceBeamColumn', 2313, 313, 323, 2313, 2313)

    # Create geometric transformation
    ops.geomTransf('Linear', 2413, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2413990, 237.82465921, 0.00848875, 286.11851391, 0.08369419, 28.61185139, 0.27406237, -464.18194272, -0.00968563, -558.44102994, -0.09758403, -55.84410299, -0.28795221, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2413991, 352.71408255, 0.00898322, 424.3379533, 0.08698277, 42.43379533, 0.27735095, -465.15620747, -0.00955316, -559.61313372, -0.09276849, -55.96131337, -0.28313667, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2413990, 33490047.54346641, 0.15, 0.003125, 0.001125, 13954186.47644434, 0.00281737)
    ops.section('Aggregator', 2413991, 2413990, 'Mz')
    ops.section('Aggregator', 2413992, 2413991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2413, 2413991, 0.52529787184, 2413992, 0.52529787184, 2413990)
    # Create element
    ops.element('forceBeamColumn', 2413, 413, 423, 2413, 2413)

    # Create geometric transformation
    ops.geomTransf('Linear', 2513, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2513990, 239.40476213, 0.0086871, 286.28371941, 0.07954326, 28.62837194, 0.26806372, -467.71899124, -0.00987019, -559.30521708, -0.09268525, -55.93052171, -0.28120572, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2513991, 468.79629162, 0.00963345, 560.59346864, 0.09820582, 56.05934686, 0.28672628, -468.79629162, -0.00963345, -560.59346864, -0.09820582, -56.05934686, -0.28672628, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2513990, 34996310.80266236, 0.15, 0.003125, 0.001125, 14581796.16777598, 0.00281737)
    ops.section('Aggregator', 2513991, 2513990, 'Mz')
    ops.section('Aggregator', 2513992, 2513991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2513, 2513991, 0.53044638704, 2513992, 0.53044638704, 2513990)
    # Create element
    ops.element('forceBeamColumn', 2513, 513, 523, 2513, 2513)

    # Create geometric transformation
    ops.geomTransf('Linear', 2613, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2613990, 244.06072785, 0.00842418, 294.64285832, 0.08415735, 29.46428583, 0.27349761, -475.54303081, -0.00964803, -574.10038513, -0.09816324, -57.41003851, -0.2875035, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2613991, 478.35017672, 0.00937593, 577.48931829, 0.10378973, 57.74893183, 0.29312999, -478.35017672, -0.00937593, -577.48931829, -0.10378973, -57.74893183, -0.29312999, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2613990, 32547353.12016071, 0.15, 0.003125, 0.001125, 13561397.1334003, 0.00281737)
    ops.section('Aggregator', 2613991, 2613990, 'Mz')
    ops.section('Aggregator', 2613992, 2613991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2613, 2613991, 0.52814969293, 2613992, 0.52814969293, 2613990)
    # Create element
    ops.element('forceBeamColumn', 2613, 613, 623, 2613, 2613)

    # Create geometric transformation
    ops.geomTransf('Linear', 2713, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2713990, 241.61201017, 0.00885365, 291.39380401, 0.07554173, 29.1393804, 0.26392161, -357.09162814, -0.00959146, -430.66686889, -0.08264962, -43.06668689, -0.27102951, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2713991, 357.85138519, 0.00944194, 431.58316646, 0.07779411, 43.15831665, 0.26617399, -357.85138519, -0.00944194, -431.58316646, -0.07779411, -43.15831665, -0.26617399, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2713990, 32826404.50172782, 0.125, 0.00260417, 0.00065104, 13677668.54238659, 0.00178813)
    ops.section('Aggregator', 2713991, 2713990, 'Mz')
    ops.section('Aggregator', 2713992, 2713991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2713, 2713991, 0.53084224027, 2713992, 0.53084224027, 2713990)
    # Create element
    ops.element('forceBeamColumn', 2713, 713, 723, 2713, 2713)

    # Create geometric transformation
    ops.geomTransf('Linear', 2023, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2023990, 345.21417519, 0.00941305, 413.90550417, 0.10268415, 41.39055042, 0.32146854, -345.21417519, -0.00941305, -413.90550417, -0.10268415, -41.39055042, -0.32146854, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2023991, 345.21417519, 0.00941305, 413.90550417, 0.1029014, 41.39055042, 0.32168578, -345.21417519, -0.00941305, -413.90550417, -0.1029014, -41.39055042, -0.32168578, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2023990, 34356127.758529, 0.125, 0.00260417, 0.00065104, 14315053.23272042, 0.00178813)
    ops.section('Aggregator', 2023991, 2023990, 'Mz')
    ops.section('Aggregator', 2023992, 2023991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2023, 2023991, 0.45707100248, 2023992, 0.45707100248, 2023990)
    # Create element
    ops.element('forceBeamColumn', 2023, 23, 33, 2023, 2023)

    # Create geometric transformation
    ops.geomTransf('Linear', 2123, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2123990, 482.93083128, 0.00976359, 582.20880054, 0.12920256, 58.22088005, 0.3425856, -482.93083128, -0.00976359, -582.20880054, -0.12920256, -58.22088005, -0.3425856, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2123991, 482.93083128, 0.00976359, 582.20880054, 0.12854329, 58.22088005, 0.34192633, -482.93083128, -0.00976359, -582.20880054, -0.12854329, -58.22088005, -0.34192633, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2123990, 32932387.80231593, 0.15, 0.003125, 0.001125, 13721828.25096497, 0.00281737)
    ops.section('Aggregator', 2123991, 2123990, 'Mz')
    ops.section('Aggregator', 2123992, 2123991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2123, 2123991, 0.46864080434, 2123992, 0.46864080434, 2123990)
    # Create element
    ops.element('forceBeamColumn', 2123, 123, 133, 2123, 2123)

    # Create geometric transformation
    ops.geomTransf('Linear', 2223, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2223990, 477.86958933, 0.00937135, 575.10531444, 0.12793102, 57.51053144, 0.34515221, -477.86958933, -0.00937135, -575.10531444, -0.12793102, -57.51053144, -0.34515221, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2223991, 477.86958933, 0.00937135, 575.10531444, 0.12882012, 57.51053144, 0.34604131, -477.86958933, -0.00937135, -575.10531444, -0.12882012, -57.51053144, -0.34604131, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2223990, 33399751.10210735, 0.15, 0.003125, 0.001125, 13916562.9592114, 0.00281737)
    ops.section('Aggregator', 2223991, 2223990, 'Mz')
    ops.section('Aggregator', 2223992, 2223991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2223, 2223991, 0.46036023679, 2223992, 0.46036023679, 2223990)
    # Create element
    ops.element('forceBeamColumn', 2223, 223, 233, 2223, 2223)

    # Create geometric transformation
    ops.geomTransf('Linear', 2323, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2323990, 363.21207451, 0.00919775, 433.90236925, 0.09931762, 43.39023693, 0.31566669, -363.21207451, -0.00919775, -433.90236925, -0.09931762, -43.39023693, -0.31566669, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2323991, 363.21207451, 0.00919775, 433.90236925, 0.09943286, 43.39023693, 0.31578194, -363.21207451, -0.00919775, -433.90236925, -0.09943286, -43.39023693, -0.31578194, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2323990, 35230206.92149717, 0.125, 0.00260417, 0.00065104, 14679252.88395715, 0.00178813)
    ops.section('Aggregator', 2323991, 2323990, 'Mz')
    ops.section('Aggregator', 2323992, 2323991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2323, 2323991, 0.46221598445, 2323992, 0.46221598445, 2323990)
    # Create element
    ops.element('forceBeamColumn', 2323, 323, 333, 2323, 2323)

    # Create geometric transformation
    ops.geomTransf('Linear', 2423, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2423990, 360.27563172, 0.00923247, 431.8358327, 0.12161125, 43.18358327, 0.33636312, -475.26814558, -0.00980689, -569.66887941, -0.12970036, -56.96688794, -0.34445223, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2423991, 360.27563172, 0.00923247, 431.8358327, 0.1212655, 43.18358327, 0.33601737, -475.26814558, -0.00980689, -569.66887941, -0.12933148, -56.96688794, -0.34408336, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2423990, 34429296.17383516, 0.15, 0.003125, 0.001125, 14345540.07243132, 0.00281737)
    ops.section('Aggregator', 2423991, 2423990, 'Mz')
    ops.section('Aggregator', 2423992, 2423991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2423, 2423991, 0.46565368012, 2423992, 0.46565368012, 2423990)
    # Create element
    ops.element('forceBeamColumn', 2423, 423, 433, 2423, 2423)

    # Create geometric transformation
    ops.geomTransf('Linear', 2523, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2523990, 477.13625723, 0.00954197, 575.96081276, 0.12894491, 57.59608128, 0.34510339, -477.13625723, -0.00954197, -575.96081276, -0.12894491, -57.59608128, -0.34510339, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2523991, 477.13625723, 0.00954197, 575.96081276, 0.12941847, 57.59608128, 0.34557695, -477.13625723, -0.00954197, -575.96081276, -0.12941847, -57.59608128, -0.34557695, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2523990, 32578010.55711797, 0.15, 0.003125, 0.001125, 13574171.06546582, 0.00281737)
    ops.section('Aggregator', 2523991, 2523990, 'Mz')
    ops.section('Aggregator', 2523992, 2523991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2523, 2523991, 0.46262352463, 2523992, 0.46262352463, 2523990)
    # Create element
    ops.element('forceBeamColumn', 2523, 523, 533, 2523, 2523)

    # Create geometric transformation
    ops.geomTransf('Linear', 2623, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2623990, 476.97229394, 0.00947772, 573.67257732, 0.12724717, 57.36725773, 0.34370662, -476.97229394, -0.00947772, -573.67257732, -0.12724717, -57.36725773, -0.34370662, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2623991, 476.97229394, 0.00947772, 573.67257732, 0.12741569, 57.36725773, 0.34387513, -476.97229394, -0.00947772, -573.67257732, -0.12741569, -57.36725773, -0.34387513, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2623990, 33561283.84296738, 0.15, 0.003125, 0.001125, 13983868.26790307, 0.00281737)
    ops.section('Aggregator', 2623991, 2623990, 'Mz')
    ops.section('Aggregator', 2623992, 2623991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2623, 2623991, 0.46198030077, 2623992, 0.46198030077, 2623990)
    # Create element
    ops.element('forceBeamColumn', 2623, 623, 633, 2623, 2623)

    # Create geometric transformation
    ops.geomTransf('Linear', 2723, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2723990, 362.31785597, 0.00923366, 436.98951977, 0.10700781, 43.69895198, 0.32381162, -362.31785597, -0.00923366, -436.98951977, -0.10700781, -43.69895198, -0.32381162, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2723991, 362.31785597, 0.00923366, 436.98951977, 0.10719004, 43.69895198, 0.32399385, -362.31785597, -0.00923366, -436.98951977, -0.10719004, -43.69895198, -0.32399385, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2723990, 32814054.91761269, 0.125, 0.00260417, 0.00065104, 13672522.88233862, 0.00178813)
    ops.section('Aggregator', 2723991, 2723990, 'Mz')
    ops.section('Aggregator', 2723992, 2723991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2723, 2723991, 0.46124650854, 2723992, 0.46124650854, 2723990)
    # Create element
    ops.element('forceBeamColumn', 2723, 723, 733, 2723, 2723)

    # Create geometric transformation
    ops.geomTransf('Linear', 2033, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2033990, 358.16580112, 0.0093542, 431.85667337, 0.07675129, 43.18566734, 0.26560867, -358.16580112, -0.0093542, -431.85667337, -0.07675129, -43.18566734, -0.26560867, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2033991, 241.80690868, 0.00877171, 291.55750452, 0.07461679, 29.15575045, 0.26347417, -357.29841976, -0.00950418, -430.81083251, -0.08163882, -43.08108325, -0.2704962, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2033990, 32893556.45879851, 0.125, 0.00260417, 0.00065104, 13705648.52449938, 0.00178813)
    ops.section('Aggregator', 2033991, 2033990, 'Mz')
    ops.section('Aggregator', 2033992, 2033991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2033, 2033991, 0.52950009181, 2033992, 0.52950009181, 2033990)
    # Create element
    ops.element('forceBeamColumn', 2033, 33, 43, 2033, 2033)

    # Create geometric transformation
    ops.geomTransf('Linear', 2133, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2133990, 469.58403197, 0.00949415, 563.98711827, 0.11139273, 56.39871183, 0.30083962, -469.58403197, -0.00949415, -563.98711827, -0.11139273, -56.39871183, -0.30083962, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2133991, 239.70182529, 0.00854845, 287.89041468, 0.09135229, 28.78904147, 0.28079918, -467.91079103, -0.00974396, -561.97749641, -0.10652319, -56.19774964, -0.29597008, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2133990, 33926583.00715474, 0.15, 0.003125, 0.001125, 14136076.25298114, 0.00281737)
    ops.section('Aggregator', 2133991, 2133990, 'Mz')
    ops.section('Aggregator', 2133992, 2133991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2133, 2133991, 0.52785242328, 2133992, 0.52785242328, 2133990)
    # Create element
    ops.element('forceBeamColumn', 2133, 133, 143, 2133, 2133)

    # Create geometric transformation
    ops.geomTransf('Linear', 2233, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2233990, 463.93617477, 0.00936055, 561.37446405, 0.11783469, 56.13744641, 0.3092137, -463.93617477, -0.00936055, -561.37446405, -0.11783469, -56.13744641, -0.3092137, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2233991, 236.7879709, 0.00840364, 286.51941256, 0.09672973, 28.65194126, 0.28810874, -461.75706564, -0.00962936, -558.73768709, -0.11286288, -55.87376871, -0.3042419, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2233990, 31888118.8190327, 0.15, 0.003125, 0.001125, 13286716.17459696, 0.00281737)
    ops.section('Aggregator', 2233991, 2233990, 'Mz')
    ops.section('Aggregator', 2233992, 2233991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2233, 2233991, 0.52252333618, 2233992, 0.52252333618, 2233990)
    # Create element
    ops.element('forceBeamColumn', 2233, 233, 243, 2233, 2233)

    # Create geometric transformation
    ops.geomTransf('Linear', 2333, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2333990, 349.96014391, 0.00941357, 422.72543739, 0.09544612, 42.27254374, 0.2854115, -349.96014391, -0.00941357, -422.72543739, -0.09544612, -42.27254374, -0.2854115, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2333991, 236.32244026, 0.00882401, 285.45966924, 0.08302104, 28.54596692, 0.27298641, -349.37895059, -0.00956104, -422.02339974, -0.09084541, -42.20233997, -0.28081078, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2333990, 32390251.45537147, 0.125, 0.00260417, 0.00065104, 13495938.10640478, 0.00178813)
    ops.section('Aggregator', 2333991, 2333990, 'Mz')
    ops.section('Aggregator', 2333992, 2333991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2333, 2333991, 0.5264117203600001, 2333992, 0.5264117203600001, 2333990)
    # Create element
    ops.element('forceBeamColumn', 2333, 333, 343, 2333, 2333)

    # Create geometric transformation
    ops.geomTransf('Linear', 2433, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2433990, 370.67751695, 0.00925204, 445.84681825, 0.0840257, 44.58468183, 0.26972333, -488.65878545, -0.00984209, -587.75338331, -0.08961582, -58.77533833, -0.27531345, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2433991, 249.87509992, 0.00874236, 300.54700694, 0.08240418, 30.05470069, 0.26810181, -487.3703123, -0.00998207, -586.20362206, -0.09607633, -58.62036221, -0.28177396, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2433990, 33550158.575197, 0.15, 0.003125, 0.001125, 13979232.73966542, 0.00281737)
    ops.section('Aggregator', 2433991, 2433990, 'Mz')
    ops.section('Aggregator', 2433992, 2433991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2433, 2433991, 0.53850983635, 2433992, 0.53850983635, 2433990)
    # Create element
    ops.element('forceBeamColumn', 2433, 433, 443, 2433, 2433)

    # Create geometric transformation
    ops.geomTransf('Linear', 2533, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2533990, 464.0916315, 0.00932801, 559.52192268, 0.11560809, 55.95219227, 0.30697079, -464.0916315, -0.00932801, -559.52192268, -0.11560809, -55.95219227, -0.30697079, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2533991, 236.86257983, 0.0083868, 285.56818758, 0.09387986, 28.55681876, 0.28524257, -462.07093874, -0.00958593, -557.08571866, -0.10950827, -55.70857187, -0.30087098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2533990, 32920101.0269438, 0.15, 0.003125, 0.001125, 13716708.76122658, 0.00281737)
    ops.section('Aggregator', 2533991, 2533990, 'Mz')
    ops.section('Aggregator', 2533992, 2533991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2533, 2533991, 0.52256786946, 2533992, 0.52256786946, 2533990)
    # Create element
    ops.element('forceBeamColumn', 2533, 533, 543, 2533, 2533)

    # Create geometric transformation
    ops.geomTransf('Linear', 2633, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2633990, 490.77410658, 0.00971764, 590.60782216, 0.10948321, 59.06078222, 0.2950619, -490.77410658, -0.00971764, -590.60782216, -0.10948321, -59.06078222, -0.2950619, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2633991, 250.42960931, 0.00874244, 301.37222843, 0.09003444, 30.13722284, 0.27561313, -488.38068829, -0.00998642, -587.72753253, -0.10499866, -58.77275325, -0.29057735, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2633990, 33412175.48253567, 0.15, 0.003125, 0.001125, 13921739.78438986, 0.00281737)
    ops.section('Aggregator', 2633991, 2633990, 'Mz')
    ops.section('Aggregator', 2633992, 2633991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2633, 2633991, 0.5388549728199999, 2633992, 0.5388549728199999, 2633990)
    # Create element
    ops.element('forceBeamColumn', 2633, 633, 643, 2633, 2633)

    # Create geometric transformation
    ops.geomTransf('Linear', 2733, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2733990, 356.05326004, 0.00947279, 429.5669665, 0.07657294, 42.95669665, 0.26508184, -356.05326004, -0.00947279, -429.5669665, -0.07657294, -42.95669665, -0.26508184, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2733991, 240.41399155, 0.00888197, 290.05185641, 0.07387466, 29.00518564, 0.26238356, -355.37797897, -0.00962154, -428.75226131, -0.08082237, -42.87522613, -0.26933128, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2733990, 32728450.04927316, 0.125, 0.00260417, 0.00065104, 13636854.18719715, 0.00178813)
    ops.section('Aggregator', 2733991, 2733990, 'Mz')
    ops.section('Aggregator', 2733992, 2733991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2733, 2733991, 0.5304789093000001, 2733992, 0.5304789093000001, 2733990)
    # Create element
    ops.element('forceBeamColumn', 2733, 733, 743, 2733, 2733)

    # Create geometric transformation
    ops.geomTransf('Linear', 2043, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2043990, 241.37761238, 0.00881796, 291.4112836, 0.06352264, 29.14112836, 0.25223088, -356.69030024, -0.00955768, -430.62642479, -0.06948778, -43.06264248, -0.25819602, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2043991, 241.23014223, 0.00893642, 291.23324528, 0.06700165, 29.12332453, 0.25570988, -241.23014223, -0.00893642, -291.23324528, -0.06700165, -29.12332453, -0.25570988, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2043990, 32540011.26077046, 0.125, 0.00260417, 0.00065104, 13558338.02532103, 0.00178813)
    ops.section('Aggregator', 2043991, 2043990, 'Mz')
    ops.section('Aggregator', 2043992, 2043991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2043, 2043991, 0.5299185837, 2043992, 0.5299185837, 2043990)
    # Create element
    ops.element('forceBeamColumn', 2043, 43, 53, 2043, 2043)

    # Create geometric transformation
    ops.geomTransf('Linear', 2143, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2143990, 242.39811693, 0.00853423, 291.36901545, 0.06884673, 29.13690155, 0.25772851, -472.92995884, -0.00973799, -568.47445117, -0.08022986, -56.84744512, -0.26911164, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2143991, 242.45497778, 0.00861257, 291.43736371, 0.07372159, 29.14373637, 0.26260337, -358.73192063, -0.00924703, -431.20535691, -0.08057531, -43.12053569, -0.26945708, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2143990, 33714931.77475709, 0.15, 0.003125, 0.001125, 14047888.23948212, 0.00281737)
    ops.section('Aggregator', 2143991, 2143990, 'Mz')
    ops.section('Aggregator', 2143992, 2143991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2143, 2143991, 0.5294317011399999, 2143992, 0.5294317011399999, 2143990)
    # Create element
    ops.element('forceBeamColumn', 2143, 143, 153, 2143, 2143)

    # Create geometric transformation
    ops.geomTransf('Linear', 2243, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2243990, 238.44305735, 0.00860987, 287.15085797, 0.06868595, 28.7150858, 0.25812161, -465.50737616, -0.00982522, -560.59859298, -0.08004078, -56.0598593, -0.26947643, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2243991, 238.6009615, 0.0086856, 287.34101789, 0.07498297, 28.73410179, 0.26441863, -353.13509168, -0.00932586, -425.27153309, -0.08195599, -42.52715331, -0.27139165, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2243990, 33223817.12672528, 0.15, 0.003125, 0.001125, 13843257.13613553, 0.00281737)
    ops.section('Aggregator', 2243991, 2243990, 'Mz')
    ops.section('Aggregator', 2243992, 2243991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2243, 2243991, 0.52788372955, 2243992, 0.52788372955, 2243990)
    # Create element
    ops.element('forceBeamColumn', 2243, 243, 253, 2243, 2243)

    # Create geometric transformation
    ops.geomTransf('Linear', 2343, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2343990, 242.29726443, 0.00886179, 290.52233118, 0.07084273, 29.05223312, 0.25880655, -358.23104015, -0.00957964, -429.53071356, -0.07748103, -42.95307136, -0.26544485, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2343991, 242.29726443, 0.00886179, 290.52233118, 0.07189233, 29.05223312, 0.25985615, -358.23104015, -0.00957964, -429.53071356, -0.07863089, -42.95307136, -0.26659471, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2343990, 34345628.86905148, 0.125, 0.00260417, 0.00065104, 14310678.69543812, 0.00178813)
    ops.section('Aggregator', 2343991, 2343990, 'Mz')
    ops.section('Aggregator', 2343992, 2343991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2343, 2343991, 0.53201729243, 2343992, 0.53201729243, 2343990)
    # Create element
    ops.element('forceBeamColumn', 2343, 343, 353, 2343, 2343)

    # Create geometric transformation
    ops.geomTransf('Linear', 2443, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2443990, 248.12701703, 0.00858572, 296.63828151, 0.06692562, 29.66382815, 0.25392043, -484.0642766, -0.0097735, -578.70358846, -0.07795984, -57.87035885, -0.26495466, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2443991, 248.13882389, 0.00866342, 296.65239673, 0.0712085, 29.66523967, 0.25820332, -367.13258984, -0.0092897, -438.91061054, -0.07780913, -43.89106105, -0.26480395, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2443990, 35056590.21712608, 0.15, 0.003125, 0.001125, 14606912.5904692, 0.00281737)
    ops.section('Aggregator', 2443991, 2443990, 'Mz')
    ops.section('Aggregator', 2443992, 2443991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2443, 2443991, 0.53477418753, 2443992, 0.53477418753, 2443990)
    # Create element
    ops.element('forceBeamColumn', 2443, 443, 453, 2443, 2443)

    # Create geometric transformation
    ops.geomTransf('Linear', 2543, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2543990, 242.25619441, 0.00842671, 292.18989806, 0.07115967, 29.21898981, 0.26089884, -472.24286395, -0.0096415, -569.58128403, -0.08296235, -56.9581284, -0.27270152, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2543991, 242.22381137, 0.00850953, 292.15084025, 0.07674035, 29.21508402, 0.26647952, -358.22766862, -0.00914992, -432.06534401, -0.08389818, -43.2065344, -0.27363736, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2543990, 32808334.06393952, 0.15, 0.003125, 0.001125, 13670139.19330814, 0.00281737)
    ops.section('Aggregator', 2543991, 2543990, 'Mz')
    ops.section('Aggregator', 2543992, 2543991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2543, 2543991, 0.52703929783, 2543992, 0.52703929783, 2543990)
    # Create element
    ops.element('forceBeamColumn', 2543, 543, 553, 2543, 2543)

    # Create geometric transformation
    ops.geomTransf('Linear', 2643, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2643990, 245.16078967, 0.00857662, 295.2091431, 0.06827122, 29.52091431, 0.2562342, -478.11142643, -0.00979992, -575.71549143, -0.07956961, -57.57154914, -0.2675326, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2643991, 245.17210657, 0.0086582, 295.2227703, 0.07433713, 29.52227703, 0.26230011, -362.67010509, -0.00930303, -436.70739965, -0.08125564, -43.67073996, -0.26921863, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2643990, 33252513.45090696, 0.15, 0.003125, 0.001125, 13855213.9378779, 0.00281737)
    ops.section('Aggregator', 2643991, 2643990, 'Mz')
    ops.section('Aggregator', 2643992, 2643991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2643, 2643991, 0.53201964983, 2643992, 0.53201964983, 2643990)
    # Create element
    ops.element('forceBeamColumn', 2643, 643, 653, 2643, 2643)

    # Create geometric transformation
    ops.geomTransf('Linear', 2743, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2743990, 245.38154851, 0.00884856, 296.72905946, 0.06481424, 29.67290595, 0.25240457, -362.4342442, -0.00960089, -438.27571001, -0.07091244, -43.827571, -0.25850277, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2743991, 245.10996361, 0.00897311, 296.40064384, 0.0674234, 29.64006438, 0.25501373, -245.10996361, -0.00897311, -296.40064384, -0.0674234, -29.64006438, -0.25501373, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2743990, 32074063.44811839, 0.125, 0.00260417, 0.00065104, 13364193.10338266, 0.00178813)
    ops.section('Aggregator', 2743991, 2743990, 'Mz')
    ops.section('Aggregator', 2743992, 2743991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2743, 2743991, 0.53307649567, 2743992, 0.53307649567, 2743990)
    # Create element
    ops.element('forceBeamColumn', 2743, 743, 753, 2743, 2743)

    # Create geometric transformation
    ops.geomTransf('Linear', 2004, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2004990, 242.68046465, 0.00888917, 292.34960213, 0.07193134, 29.23496021, 0.2604926, -242.68046465, -0.00888917, -292.34960213, -0.07193134, -29.23496021, -0.2604926, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2004991, 242.87881615, 0.00877162, 292.58855001, 0.06908943, 29.258855, 0.25765069, -358.86697085, -0.00950173, -432.31586975, -0.07558112, -43.23158698, -0.26414239, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2004990, 33135940.95330801, 0.125, 0.00260417, 0.00065104, 13806642.06387834, 0.00178813)
    ops.section('Aggregator', 2004991, 2004990, 'Mz')
    ops.section('Aggregator', 2004992, 2004991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2004, 2004991, 0.53033162443, 2004992, 0.53033162443, 2004990)
    # Create element
    ops.element('forceBeamColumn', 2004, 4, 14, 2004, 2004)

    # Create geometric transformation
    ops.geomTransf('Linear', 2104, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2104990, 243.21287411, 0.00868893, 291.76010883, 0.08090945, 29.17601088, 0.2690413, -359.93033062, -0.00932157, -431.77530309, -0.08844064, -43.17753031, -0.27657249, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2104991, 243.11141218, 0.00861284, 291.63839429, 0.07417216, 29.16383943, 0.26230401, -474.51969802, -0.00981324, -569.23762463, -0.08643747, -56.92376246, -0.27456932, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2104990, 34226406.77941479, 0.15, 0.003125, 0.001125, 14261002.82475616, 0.00281737)
    ops.section('Aggregator', 2104991, 2104990, 'Mz')
    ops.section('Aggregator', 2104992, 2104991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2104, 2104991, 0.53154211208, 2104992, 0.53154211208, 2104990)
    # Create element
    ops.element('forceBeamColumn', 2104, 104, 114, 2104, 2104)

    # Create geometric transformation
    ops.geomTransf('Linear', 2204, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2204990, 242.56753452, 0.00855036, 291.88440922, 0.08286295, 29.18844092, 0.27216437, -358.81994555, -0.00918533, -431.77232283, -0.0905963, -43.17723228, -0.27989772, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2204991, 242.55973924, 0.00847007, 291.87502906, 0.07586893, 29.18750291, 0.26517035, -473.0432466, -0.00967462, -569.21858418, -0.08844887, -56.92185842, -0.27775029, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2204990, 33436058.84092671, 0.15, 0.003125, 0.001125, 13931691.18371947, 0.00281737)
    ops.section('Aggregator', 2204991, 2204990, 'Mz')
    ops.section('Aggregator', 2204992, 2204991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2204, 2204991, 0.52825804938, 2204992, 0.52825804938, 2204990)
    # Create element
    ops.element('forceBeamColumn', 2204, 204, 214, 2204, 2204)

    # Create geometric transformation
    ops.geomTransf('Linear', 2304, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2304990, 240.75878045, 0.00884638, 290.5961842, 0.0758268, 29.05961842, 0.26449554, -355.8316511, -0.00958612, -429.48929977, -0.08296454, -42.94892998, -0.27163327, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2304991, 240.75878045, 0.00884638, 290.5961842, 0.07593954, 29.05961842, 0.26460828, -355.8316511, -0.00958612, -429.48929977, -0.08308805, -42.94892998, -0.27175679, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2304990, 32605540.55335176, 0.125, 0.00260417, 0.00065104, 13585641.8972299, 0.00178813)
    ops.section('Aggregator', 2304991, 2304990, 'Mz')
    ops.section('Aggregator', 2304992, 2304991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2304, 2304991, 0.53002951439, 2304992, 0.53002951439, 2304990)
    # Create element
    ops.element('forceBeamColumn', 2304, 304, 314, 2304, 2304)

    # Create geometric transformation
    ops.geomTransf('Linear', 2404, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2404990, 240.48481173, 0.00878977, 289.74697649, 0.07486276, 28.97469765, 0.26390383, -355.43050493, -0.00951905, -428.23874579, -0.08190337, -42.82387458, -0.27094444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2404991, 240.48481173, 0.00878977, 289.74697649, 0.07473799, 28.97469765, 0.26377905, -355.43050493, -0.00951905, -428.23874579, -0.08176668, -42.82387458, -0.27080774, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2404990, 33096494.06773043, 0.125, 0.00260417, 0.00065104, 13790205.86155435, 0.00178813)
    ops.section('Aggregator', 2404991, 2404990, 'Mz')
    ops.section('Aggregator', 2404992, 2404991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2404, 2404991, 0.52898559178, 2404992, 0.52898559178, 2404990)
    # Create element
    ops.element('forceBeamColumn', 2404, 404, 414, 2404, 2404)

    # Create geometric transformation
    ops.geomTransf('Linear', 2504, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2504990, 249.51045032, 0.00870599, 299.15387417, 0.07977061, 29.91538742, 0.26623525, -369.09571063, -0.00934362, -442.53221311, -0.08719637, -44.25322131, -0.27366101, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2504991, 249.52536171, 0.00862544, 299.17175237, 0.0736986, 29.91717524, 0.26016324, -486.62918063, -0.00983475, -583.45053075, -0.08589078, -58.34505308, -0.27235542, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2504990, 34359937.26125113, 0.15, 0.003125, 0.001125, 14316640.5255213, 0.00281737)
    ops.section('Aggregator', 2504991, 2504990, 'Mz')
    ops.section('Aggregator', 2504992, 2504991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2504, 2504991, 0.53629470809, 2504992, 0.53629470809, 2504990)
    # Create element
    ops.element('forceBeamColumn', 2504, 504, 514, 2504, 2504)

    # Create geometric transformation
    ops.geomTransf('Linear', 2604, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2604990, 238.07726149, 0.00881587, 282.9634328, 0.07544024, 28.29634328, 0.26384989, -352.58811633, -0.00942469, -419.06372386, -0.08241306, -41.90637239, -0.27082271, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2604991, 237.77710692, 0.00875331, 282.60668824, 0.07064401, 28.26066882, 0.25905366, -464.82739191, -0.00990918, -552.46416081, -0.08224562, -55.24641608, -0.27065527, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2604990, 36377946.0931697, 0.15, 0.003125, 0.001125, 15157477.53882071, 0.00281737)
    ops.section('Aggregator', 2604991, 2604990, 'Mz')
    ops.section('Aggregator', 2604992, 2604991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2604, 2604991, 0.5307583747500001, 2604992, 0.5307583747500001, 2604990)
    # Create element
    ops.element('forceBeamColumn', 2604, 604, 614, 2604, 2604)

    # Create geometric transformation
    ops.geomTransf('Linear', 2704, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2704990, 240.40316967, 0.0086662, 287.7588656, 0.06941575, 28.77588656, 0.25976708, -240.40316967, -0.0086662, -287.7588656, -0.06941575, -28.77588656, -0.25976708, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2704991, 240.62695369, 0.00855564, 288.0267316, 0.06627012, 28.80267316, 0.25662145, -355.56074288, -0.00924989, -425.60069471, -0.07247729, -42.56006947, -0.26282862, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2704990, 34762845.94470785, 0.125, 0.00260417, 0.00065104, 14484519.14362827, 0.00178813)
    ops.section('Aggregator', 2704991, 2704990, 'Mz')
    ops.section('Aggregator', 2704992, 2704991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2704, 2704991, 0.52534435603, 2704992, 0.52534435603, 2704990)
    # Create element
    ops.element('forceBeamColumn', 2704, 704, 714, 2704, 2704)

    # Create geometric transformation
    ops.geomTransf('Linear', 2014, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2014990, 245.06195977, 0.00882991, 294.46265261, 0.07333414, 29.44626526, 0.26089166, -362.14077025, -0.00955604, -435.14273665, -0.08022174, -43.51427367, -0.26777927, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2014991, 245.06195977, 0.00882991, 294.46265261, 0.07347377, 29.44626526, 0.26103129, -362.14077025, -0.00955604, -435.14273665, -0.08037471, -43.51427367, -0.26793224, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2014990, 33809723.74013401, 0.125, 0.00260417, 0.00065104, 14087384.8917225, 0.00178813)
    ops.section('Aggregator', 2014991, 2014990, 'Mz')
    ops.section('Aggregator', 2014992, 2014991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2014, 2014991, 0.53316976281, 2014992, 0.53316976281, 2014990)
    # Create element
    ops.element('forceBeamColumn', 2014, 14, 24, 2014, 2014)

    # Create geometric transformation
    ops.geomTransf('Linear', 2114, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2114990, 238.50903188, 0.00849379, 287.55522273, 0.08455211, 28.75552227, 0.27476986, -465.37662481, -0.00970586, -561.07510036, -0.09860109, -56.10751004, -0.28881884, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2114991, 467.27292075, 0.00944671, 563.36134419, 0.10453087, 56.33613442, 0.29474862, -467.27292075, -0.00944671, -563.36134419, -0.10453087, -56.33613442, -0.29474862, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2114990, 32918175.43497995, 0.15, 0.003125, 0.001125, 13715906.43124164, 0.00281737)
    ops.section('Aggregator', 2114991, 2114990, 'Mz')
    ops.section('Aggregator', 2114992, 2114991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2114, 2114991, 0.52571329546, 2114992, 0.52571329546, 2114990)
    # Create element
    ops.element('forceBeamColumn', 2114, 114, 124, 2114, 2114)

    # Create geometric transformation
    ops.geomTransf('Linear', 2214, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2214990, 242.2217737, 0.00873823, 292.0288242, 0.08375575, 29.20288242, 0.27142718, -472.8184616, -0.00997953, -570.04214481, -0.0976583, -57.00421448, -0.28532973, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2214991, 474.43081022, 0.00971783, 571.98603392, 0.10223149, 57.19860339, 0.28990292, -474.43081022, -0.00971783, -571.98603392, -0.10223149, -57.19860339, -0.28990292, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2214990, 32920623.3511312, 0.15, 0.003125, 0.001125, 13716926.39630467, 0.00281737)
    ops.section('Aggregator', 2214991, 2214990, 'Mz')
    ops.section('Aggregator', 2214992, 2214991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2214, 2214991, 0.5328461685900001, 2214992, 0.5328461685900001, 2214990)
    # Create element
    ops.element('forceBeamColumn', 2214, 214, 224, 2214, 2214)

    # Create geometric transformation
    ops.geomTransf('Linear', 2314, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2314990, 245.02808149, 0.0087727, 295.31364337, 0.07433477, 29.53136434, 0.26238051, -361.94601883, -0.00950672, -436.22590878, -0.08133132, -43.62259088, -0.26937706, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2314991, 362.96502458, 0.00935455, 437.45403863, 0.08433449, 43.74540386, 0.27238023, -362.96502458, -0.00935455, -437.45403863, -0.08433449, -43.74540386, -0.27238023, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2314990, 33011487.69454599, 0.125, 0.00260417, 0.00065104, 13754786.53939416, 0.00178813)
    ops.section('Aggregator', 2314991, 2314990, 'Mz')
    ops.section('Aggregator', 2314992, 2314991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2314, 2314991, 0.53178551207, 2314992, 0.53178551207, 2314990)
    # Create element
    ops.element('forceBeamColumn', 2314, 314, 324, 2314, 2314)

    # Create geometric transformation
    ops.geomTransf('Linear', 2414, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2414990, 239.68982288, 0.00866016, 288.81805439, 0.07543009, 28.88180544, 0.26553025, -354.15211557, -0.00938181, -426.74120974, -0.08252964, -42.67412097, -0.2726298, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2414991, 355.03995796, 0.00923392, 427.8110295, 0.08656999, 42.78110295, 0.27667015, -355.03995796, -0.00923392, -427.8110295, -0.08656999, -42.78110295, -0.27667015, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2414990, 33069448.22254925, 0.125, 0.00260417, 0.00065104, 13778936.75939552, 0.00178813)
    ops.section('Aggregator', 2414991, 2414990, 'Mz')
    ops.section('Aggregator', 2414992, 2414991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2414, 2414991, 0.52603848494, 2414992, 0.52603848494, 2414990)
    # Create element
    ops.element('forceBeamColumn', 2414, 414, 424, 2414, 2414)

    # Create geometric transformation
    ops.geomTransf('Linear', 2514, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2514990, 248.01602552, 0.00855106, 300.42128244, 0.08639648, 30.04212824, 0.27402582, -482.98609539, -0.00981838, -585.04002664, -0.10080233, -58.50400266, -0.28843168, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2514991, 486.0956723, 0.00953076, 588.80665051, 0.10532184, 58.88066505, 0.29295119, -486.0956723, -0.00953076, -588.80665051, -0.10532184, -58.88066505, -0.29295119, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2514990, 31575146.76232428, 0.15, 0.003125, 0.001125, 13156311.15096845, 0.00281737)
    ops.section('Aggregator', 2514991, 2514990, 'Mz')
    ops.section('Aggregator', 2514992, 2514991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2514, 2514991, 0.53296567304, 2514992, 0.53296567304, 2514990)
    # Create element
    ops.element('forceBeamColumn', 2514, 514, 524, 2514, 2514)

    # Create geometric transformation
    ops.geomTransf('Linear', 2614, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2614990, 241.02106391, 0.00839916, 291.39826752, 0.08593188, 29.13982675, 0.2762427, -469.72024456, -0.00962568, -567.89918385, -0.10024416, -56.78991838, -0.29055497, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2614991, 472.34228845, 0.0093532, 571.06927627, 0.10526495, 57.10692763, 0.29557577, -472.34228845, -0.0093532, -571.06927627, -0.10526495, -57.10692763, -0.29557577, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2614990, 32131582.69934277, 0.15, 0.003125, 0.001125, 13388159.45805949, 0.00281737)
    ops.section('Aggregator', 2614991, 2614990, 'Mz')
    ops.section('Aggregator', 2614992, 2614991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2614, 2614991, 0.5254562080299999, 2614992, 0.5254562080299999, 2614990)
    # Create element
    ops.element('forceBeamColumn', 2614, 614, 624, 2614, 2614)

    # Create geometric transformation
    ops.geomTransf('Linear', 2714, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2714990, 241.52412245, 0.00866045, 288.84991627, 0.07084841, 28.88499163, 0.26024647, -356.98277303, -0.00935858, -426.93227928, -0.07748677, -42.69322793, -0.26688483, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2714991, 241.52412245, 0.00866045, 288.84991627, 0.07089866, 28.88499163, 0.26029673, -356.98277303, -0.00935858, -426.93227928, -0.07754182, -42.69322793, -0.26693988, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2714990, 34970176.20896265, 0.125, 0.00260417, 0.00065104, 14570906.75373444, 0.00178813)
    ops.section('Aggregator', 2714991, 2714990, 'Mz')
    ops.section('Aggregator', 2714992, 2714991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2714, 2714991, 0.5279885013000001, 2714992, 0.5279885013000001, 2714990)
    # Create element
    ops.element('forceBeamColumn', 2714, 714, 724, 2714, 2714)

    # Create geometric transformation
    ops.geomTransf('Linear', 2024, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2024990, 239.55373065, 0.00889649, 288.91438333, 0.08398353, 28.89143833, 0.30035526, -354.15510003, -0.00963459, -427.12965501, -0.09189399, -42.7129655, -0.30826572, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2024991, 239.55373065, 0.00889649, 288.91438333, 0.08469581, 28.89143833, 0.30106754, -354.15510003, -0.00963459, -427.12965501, -0.09267431, -42.7129655, -0.30904604, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2024990, 32823598.177427, 0.125, 0.00260417, 0.00065104, 13676499.24059458, 0.00178813)
    ops.section('Aggregator', 2024991, 2024990, 'Mz')
    ops.section('Aggregator', 2024992, 2024991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2024, 2024991, 0.46216758446, 2024992, 0.46216758446, 2024990)
    # Create element
    ops.element('forceBeamColumn', 2024, 24, 34, 2024, 2024)

    # Create geometric transformation
    ops.geomTransf('Linear', 2124, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2124990, 472.34397123, 0.0092822, 566.1510867, 0.12434415, 56.61510867, 0.34295986, -472.34397123, -0.0092822, -566.1510867, -0.12434415, -56.61510867, -0.34295986, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2124991, 472.34397123, 0.0092822, 566.1510867, 0.12478228, 56.61510867, 0.34339799, -472.34397123, -0.0092822, -566.1510867, -0.12478228, -56.61510867, -0.34339799, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2124990, 34434859.6549335, 0.15, 0.003125, 0.001125, 14347858.18955563, 0.00281737)
    ops.section('Aggregator', 2124991, 2124990, 'Mz')
    ops.section('Aggregator', 2124992, 2124991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2124, 2124991, 0.45742366847, 2124992, 0.45742366847, 2124990)
    # Create element
    ops.element('forceBeamColumn', 2124, 124, 134, 2124, 2124)

    # Create geometric transformation
    ops.geomTransf('Linear', 2224, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2224990, 470.26183903, 0.00933377, 562.83633199, 0.12355045, 56.2836332, 0.3420025, -470.26183903, -0.00933377, -562.83633199, -0.12355045, -56.2836332, -0.3420025, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2224991, 470.26183903, 0.00933377, 562.83633199, 0.12484765, 56.2836332, 0.34329969, -470.26183903, -0.00933377, -562.83633199, -0.12484765, -56.2836332, -0.34329969, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2224990, 34788388.28093243, 0.15, 0.003125, 0.001125, 14495161.78372185, 0.00281737)
    ops.section('Aggregator', 2224991, 2224990, 'Mz')
    ops.section('Aggregator', 2224992, 2224991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2224, 2224991, 0.45776637473, 2224992, 0.45776637473, 2224990)
    # Create element
    ops.element('forceBeamColumn', 2224, 224, 234, 2224, 2224)

    # Create geometric transformation
    ops.geomTransf('Linear', 2324, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2324990, 351.60540921, 0.0094152, 425.1116644, 0.10769475, 42.51116644, 0.325521, -351.60540921, -0.0094152, -425.1116644, -0.10769475, -42.51116644, -0.325521, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2324991, 351.60540921, 0.0094152, 425.1116644, 0.1074886, 42.51116644, 0.32531485, -351.60540921, -0.0094152, -425.1116644, -0.1074886, -42.51116644, -0.32531485, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2324990, 32121253.94204538, 0.125, 0.00260417, 0.00065104, 13383855.80918557, 0.00178813)
    ops.section('Aggregator', 2324991, 2324990, 'Mz')
    ops.section('Aggregator', 2324992, 2324991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2324, 2324991, 0.45908148369, 2324992, 0.45908148369, 2324990)
    # Create element
    ops.element('forceBeamColumn', 2324, 324, 334, 2324, 2324)

    # Create geometric transformation
    ops.geomTransf('Linear', 2424, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2424990, 355.65473363, 0.00928894, 428.65167431, 0.10501091, 42.86516743, 0.32275592, -355.65473363, -0.00928894, -428.65167431, -0.10501091, -42.86516743, -0.32275592, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2424991, 355.65473363, 0.00928894, 428.65167431, 0.10626484, 42.86516743, 0.32400986, -355.65473363, -0.00928894, -428.65167431, -0.10626484, -42.86516743, -0.32400986, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2424990, 33006311.3332638, 0.125, 0.00260417, 0.00065104, 13752629.72219325, 0.00178813)
    ops.section('Aggregator', 2424991, 2424990, 'Mz')
    ops.section('Aggregator', 2424992, 2424991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2424, 2424991, 0.45925275738, 2424992, 0.45925275738, 2424990)
    # Create element
    ops.element('forceBeamColumn', 2424, 424, 434, 2424, 2424)

    # Create geometric transformation
    ops.geomTransf('Linear', 2524, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2524990, 471.2846364, 0.00949191, 569.86416123, 0.13322439, 56.98641612, 0.35087313, -471.2846364, -0.00949191, -569.86416123, -0.13322439, -56.98641612, -0.35087313, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2524991, 471.2846364, 0.00949191, 569.86416123, 0.1330089, 56.98641612, 0.35065764, -471.2846364, -0.00949191, -569.86416123, -0.1330089, -56.98641612, -0.35065764, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2524990, 32094182.87050232, 0.15, 0.003125, 0.001125, 13372576.19604263, 0.00281737)
    ops.section('Aggregator', 2524991, 2524990, 'Mz')
    ops.section('Aggregator', 2524992, 2524991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2524, 2524991, 0.45945592560000004, 2524992, 0.45945592560000004, 2524990)
    # Create element
    ops.element('forceBeamColumn', 2524, 524, 534, 2524, 2524)

    # Create geometric transformation
    ops.geomTransf('Linear', 2624, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2624990, 478.30286564, 0.00973333, 576.08784506, 0.12729047, 57.60878451, 0.34159535, -478.30286564, -0.00973333, -576.08784506, -0.12729047, -57.60878451, -0.34159535, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2624991, 478.30286564, 0.00973333, 576.08784506, 0.12664795, 57.60878451, 0.34095283, -478.30286564, -0.00973333, -576.08784506, -0.12664795, -57.60878451, -0.34095283, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2624990, 33186637.76622731, 0.15, 0.003125, 0.001125, 13827765.73592805, 0.00281737)
    ops.section('Aggregator', 2624991, 2624990, 'Mz')
    ops.section('Aggregator', 2624992, 2624991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2624, 2624991, 0.46662492157, 2624992, 0.46662492157, 2624990)
    # Create element
    ops.element('forceBeamColumn', 2624, 624, 634, 2624, 2624)

    # Create geometric transformation
    ops.geomTransf('Linear', 2724, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2724990, 237.64635073, 0.00895643, 285.15964068, 0.08205485, 28.51596407, 0.2983476, -351.53883396, -0.00967699, -421.822962, -0.08975781, -42.1822962, -0.30605056, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2724991, 237.64635073, 0.00895643, 285.15964068, 0.08225056, 28.51596407, 0.29854331, -351.53883396, -0.00967699, -421.822962, -0.08997222, -42.1822962, -0.30626497, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2724990, 34158706.27476905, 0.125, 0.00260417, 0.00065104, 14232794.28115377, 0.00178813)
    ops.section('Aggregator', 2724991, 2724990, 'Mz')
    ops.section('Aggregator', 2724992, 2724991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2724, 2724991, 0.46233635319, 2724992, 0.46233635319, 2724990)
    # Create element
    ops.element('forceBeamColumn', 2724, 724, 734, 2724, 2724)

    # Create geometric transformation
    ops.geomTransf('Linear', 2034, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2034990, 240.87268697, 0.00869119, 289.11339203, 0.07206235, 28.9113392, 0.26152835, -355.98973266, -0.00940185, -427.28546948, -0.07882626, -42.72854695, -0.26829226, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2034991, 240.87268697, 0.00869119, 289.11339203, 0.07205105, 28.9113392, 0.26151705, -355.98973266, -0.00940185, -427.28546948, -0.07881389, -42.72854695, -0.26827989, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2034990, 34087103.39608756, 0.125, 0.00260417, 0.00065104, 14202959.74836982, 0.00178813)
    ops.section('Aggregator', 2034991, 2034990, 'Mz')
    ops.section('Aggregator', 2034992, 2034991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2034, 2034991, 0.52779918272, 2034992, 0.52779918272, 2034990)
    # Create element
    ops.element('forceBeamColumn', 2034, 34, 44, 2034, 2034)

    # Create geometric transformation
    ops.geomTransf('Linear', 2134, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2134990, 471.00110367, 0.00975218, 567.1729466, 0.11408095, 56.71729466, 0.30192303, -471.00110367, -0.00975218, -567.1729466, -0.11408095, -56.71729466, -0.30192303, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2134991, 240.53387539, 0.00877365, 289.64753118, 0.09179607, 28.96475312, 0.27963816, -469.72238758, -0.0100072, -565.63313455, -0.10704192, -56.56331346, -0.294884, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2134990, 33243420.57320224, 0.15, 0.003125, 0.001125, 13851425.23883427, 0.00281737)
    ops.section('Aggregator', 2134991, 2134990, 'Mz')
    ops.section('Aggregator', 2134992, 2134991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2134, 2134991, 0.5323620670300001, 2134992, 0.5323620670300001, 2134990)
    # Create element
    ops.element('forceBeamColumn', 2134, 134, 144, 2134, 2134)

    # Create geometric transformation
    ops.geomTransf('Linear', 2234, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2234990, 482.46933398, 0.00962774, 581.01014795, 0.11245498, 58.10101479, 0.29961155, -482.46933398, -0.00962774, -581.01014795, -0.11245498, -58.10101479, -0.29961155, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2234991, 246.21765655, 0.00865975, 296.50580252, 0.09088452, 29.65058025, 0.27804108, -480.26599113, -0.00989319, -578.35678853, -0.10599562, -57.83567885, -0.29315219, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2234990, 33230856.4033906, 0.15, 0.003125, 0.001125, 13846190.16807942, 0.00281737)
    ops.section('Aggregator', 2234991, 2234990, 'Mz')
    ops.section('Aggregator', 2234992, 2234991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2234, 2234991, 0.53431201894, 2234992, 0.53431201894, 2234990)
    # Create element
    ops.element('forceBeamColumn', 2234, 234, 244, 2234, 2234)

    # Create geometric transformation
    ops.geomTransf('Linear', 2334, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2334990, 358.50892951, 0.00924068, 430.61257916, 0.09063247, 43.06125792, 0.27996219, -358.50892951, -0.00924068, -430.61257916, -0.09063247, -43.06125792, -0.27996219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2334991, 242.01577966, 0.0086725, 290.69021856, 0.08024636, 29.06902186, 0.26957608, -357.5992544, -0.00938564, -429.51994934, -0.08779628, -42.95199493, -0.277126, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2334990, 33908466.30866837, 0.125, 0.00260417, 0.00065104, 14128527.62861182, 0.00178813)
    ops.section('Aggregator', 2334991, 2334990, 'Mz')
    ops.section('Aggregator', 2334992, 2334991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2334, 2334991, 0.52817908262, 2334992, 0.52817908262, 2334990)
    # Create element
    ops.element('forceBeamColumn', 2334, 334, 344, 2334, 2334)

    # Create geometric transformation
    ops.geomTransf('Linear', 2434, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2434990, 351.38484856, 0.00932227, 422.19762606, 0.09177213, 42.21976261, 0.28180279, -351.38484856, -0.00932227, -422.19762606, -0.09177213, -42.21976261, -0.28180279, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2434991, 237.25787549, 0.00874894, 285.07123231, 0.08094372, 28.50712323, 0.27097438, -350.7962475, -0.00946268, -421.49040726, -0.08855354, -42.14904073, -0.27858419, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2434990, 33822466.10142522, 0.125, 0.00260417, 0.00065104, 14092694.20892717, 0.00178813)
    ops.section('Aggregator', 2434991, 2434990, 'Mz')
    ops.section('Aggregator', 2434992, 2434991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2434, 2434991, 0.52623087414, 2434992, 0.52623087414, 2434990)
    # Create element
    ops.element('forceBeamColumn', 2434, 434, 444, 2434, 2434)

    # Create geometric transformation
    ops.geomTransf('Linear', 2534, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2534990, 486.94223605, 0.00945838, 586.66165136, 0.11338809, 58.66616514, 0.3010597, -486.94223605, -0.00945838, -586.66165136, -0.11338809, -58.66616514, -0.3010597, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2534991, 248.42228029, 0.00850466, 299.29592137, 0.09169004, 29.92959214, 0.27936166, -483.99681074, -0.00972993, -583.1130414, -0.10695511, -58.31130414, -0.29462672, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2534990, 33109540.39432023, 0.15, 0.003125, 0.001125, 13795641.83096676, 0.00281737)
    ops.section('Aggregator', 2534991, 2534990, 'Mz')
    ops.section('Aggregator', 2534992, 2534991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2534, 2534991, 0.5328456299700001, 2534992, 0.5328456299700001, 2534990)
    # Create element
    ops.element('forceBeamColumn', 2534, 534, 544, 2534, 2534)

    # Create geometric transformation
    ops.geomTransf('Linear', 2634, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2634990, 472.49017874, 0.00947178, 567.33139985, 0.11275821, 56.73313999, 0.30196269, -472.49017874, -0.00947178, -567.33139985, -0.11275821, -56.73313999, -0.30196269, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2634991, 241.1489942, 0.00852867, 289.55394759, 0.09142794, 28.95539476, 0.28063241, -470.61959579, -0.00972338, -565.08534164, -0.10661416, -56.50853416, -0.29581864, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2634990, 33992021.7224564, 0.15, 0.003125, 0.001125, 14163342.38435683, 0.00281737)
    ops.section('Aggregator', 2634991, 2634990, 'Mz')
    ops.section('Aggregator', 2634992, 2634991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2634, 2634991, 0.52852872629, 2634992, 0.52852872629, 2634990)
    # Create element
    ops.element('forceBeamColumn', 2634, 634, 644, 2634, 2634)

    # Create geometric transformation
    ops.geomTransf('Linear', 2734, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2734990, 242.41911286, 0.00859483, 291.46233971, 0.07249625, 29.14623397, 0.26228216, -358.06528042, -0.00930745, -430.50460488, -0.07931278, -43.05046049, -0.26909868, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2734991, 242.41911286, 0.00859483, 291.46233971, 0.07303974, 29.14623397, 0.26282564, -358.06528042, -0.00930745, -430.50460488, -0.07990818, -43.05046049, -0.26969408, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2734990, 33654422.30144837, 0.125, 0.00260417, 0.00065104, 14022675.95893682, 0.00178813)
    ops.section('Aggregator', 2734991, 2734990, 'Mz')
    ops.section('Aggregator', 2734992, 2734991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2734, 2734991, 0.52690952467, 2734992, 0.52690952467, 2734990)
    # Create element
    ops.element('forceBeamColumn', 2734, 734, 744, 2734, 2734)

    # Create geometric transformation
    ops.geomTransf('Linear', 2044, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2044990, 239.77392514, 0.00881425, 289.46094528, 0.06351558, 28.94609453, 0.2526466, -354.37483189, -0.00955193, -427.80996208, -0.06947837, -42.78099621, -0.25860939, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2044991, 239.67151998, 0.00893106, 289.33731927, 0.06707864, 28.93373193, 0.25620966, -239.67151998, -0.00893106, -289.33731927, -0.06707864, -28.93373193, -0.25620966, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2044990, 32553808.72931506, 0.125, 0.00260417, 0.00065104, 13564086.97054794, 0.00178813)
    ops.section('Aggregator', 2044991, 2044990, 'Mz')
    ops.section('Aggregator', 2044992, 2044991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2044, 2044991, 0.52873399988, 2044992, 0.52873399988, 2044990)
    # Create element
    ops.element('forceBeamColumn', 2044, 44, 54, 2044, 2044)

    # Create geometric transformation
    ops.geomTransf('Linear', 2144, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2144990, 243.3887498, 0.0086781, 293.5964252, 0.06878737, 29.35964252, 0.25657084, -474.88888567, -0.00991959, -572.85178266, -0.08017394, -57.28517827, -0.26795741, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2144991, 243.47840543, 0.00875861, 293.70457552, 0.07496802, 29.37045755, 0.26275149, -360.25046404, -0.00941278, -434.56506723, -0.08194655, -43.45650672, -0.26973002, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2144990, 32770258.06407381, 0.15, 0.003125, 0.001125, 13654274.19336409, 0.00281737)
    ops.section('Aggregator', 2144991, 2144990, 'Mz')
    ops.section('Aggregator', 2144992, 2144991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2144, 2144991, 0.5325282443999999, 2144992, 0.5325282443999999, 2144990)
    # Create element
    ops.element('forceBeamColumn', 2144, 144, 154, 2144, 2144)

    # Create geometric transformation
    ops.geomTransf('Linear', 2244, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2244990, 245.57548609, 0.0084631, 295.4452873, 0.06778152, 29.54452873, 0.2563821, -478.67740047, -0.00967079, -575.88395468, -0.07900081, -57.58839547, -0.26760139, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2244991, 245.5166375, 0.00854566, 295.37448813, 0.07330098, 29.53744881, 0.26190155, -363.08682261, -0.00918244, -436.82002762, -0.08012322, -43.68200276, -0.26872379, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2244990, 33488247.93930773, 0.15, 0.003125, 0.001125, 13953436.64137822, 0.00281737)
    ops.section('Aggregator', 2244991, 2244990, 'Mz')
    ops.section('Aggregator', 2244992, 2244991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2244, 2244991, 0.5302210792, 2244992, 0.5302210792, 2244990)
    # Create element
    ops.element('forceBeamColumn', 2244, 244, 254, 2244, 2244)

    # Create geometric transformation
    ops.geomTransf('Linear', 2344, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2344990, 239.56817904, 0.00879403, 286.8867386, 0.07302191, 28.68867386, 0.26206988, -354.24995907, -0.00950141, -424.22001041, -0.07986437, -42.42200104, -0.26891234, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2344991, 239.56817904, 0.00879403, 286.8867386, 0.0729059, 28.68867386, 0.26195387, -354.24995907, -0.00950141, -424.22001041, -0.07973728, -42.42200104, -0.26878525, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2344990, 34655621.3935004, 0.125, 0.00260417, 0.00065104, 14439842.24729183, 0.00178813)
    ops.section('Aggregator', 2344991, 2344990, 'Mz')
    ops.section('Aggregator', 2344992, 2344991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2344, 2344991, 0.52896626296, 2344992, 0.52896626296, 2344990)
    # Create element
    ops.element('forceBeamColumn', 2344, 344, 354, 2344, 2344)

    # Create geometric transformation
    ops.geomTransf('Linear', 2444, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2444990, 238.88777597, 0.00894903, 289.41603757, 0.07752884, 28.94160376, 0.26615382, -353.11578947, -0.00970885, -427.80494806, -0.08483943, -42.78049481, -0.27346442, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2444991, 238.88777597, 0.00894903, 289.41603757, 0.07702906, 28.94160376, 0.26565404, -353.11578947, -0.00970885, -427.80494806, -0.08429192, -42.78049481, -0.2729169, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2444990, 31521144.55922864, 0.125, 0.00260417, 0.00065104, 13133810.23301193, 0.00178813)
    ops.section('Aggregator', 2444991, 2444990, 'Mz')
    ops.section('Aggregator', 2444992, 2444991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2444, 2444991, 0.53015246647, 2444992, 0.53015246647, 2444990)
    # Create element
    ops.element('forceBeamColumn', 2444, 444, 454, 2444, 2444)

    # Create geometric transformation
    ops.geomTransf('Linear', 2544, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2544990, 243.10084359, 0.00849988, 294.28109595, 0.07222604, 29.4281096, 0.26137518, -473.75594689, -0.009749, -573.49623805, -0.08423068, -57.34962381, -0.27337981, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2544991, 243.05928729, 0.00858627, 294.23079077, 0.07760105, 29.42307908, 0.26675018, -359.40591413, -0.00924466, -435.07198388, -0.08485177, -43.50719839, -0.2740009, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2544990, 31764566.62457573, 0.15, 0.003125, 0.001125, 13235236.09357322, 0.00281737)
    ops.section('Aggregator', 2544991, 2544990, 'Mz')
    ops.section('Aggregator', 2544992, 2544991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2544, 2544991, 0.5286833682200001, 2544992, 0.5286833682200001, 2544990)
    # Create element
    ops.element('forceBeamColumn', 2544, 544, 554, 2544, 2544)

    # Create geometric transformation
    ops.geomTransf('Linear', 2644, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2644990, 242.26393769, 0.00865613, 291.31626037, 0.06966665, 29.13162604, 0.25778844, -472.88518459, -0.00987312, -568.63247942, -0.08118083, -56.86324794, -0.26930262, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2644991, 242.3874906, 0.00873299, 291.46482963, 0.07491262, 29.14648296, 0.26303441, -358.71229743, -0.00937425, -431.34246902, -0.0818754, -43.1342469, -0.26999719, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2644990, 33618302.0937572, 0.15, 0.003125, 0.001125, 14007625.87239883, 0.00281737)
    ops.section('Aggregator', 2644991, 2644990, 'Mz')
    ops.section('Aggregator', 2644992, 2644991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2644, 2644991, 0.5315705283500001, 2644992, 0.5315705283500001, 2644990)
    # Create element
    ops.element('forceBeamColumn', 2644, 644, 654, 2644, 2644)

    # Create geometric transformation
    ops.geomTransf('Linear', 2744, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2744990, 241.04828744, 0.00867041, 289.64454231, 0.06127249, 28.96445423, 0.2508691, -356.1937119, -0.00938388, -428.00372387, -0.06701054, -42.80037239, -0.25660715, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2744991, 240.85777928, 0.00878425, 289.41562699, 0.06466276, 28.9415627, 0.25425938, -240.85777928, -0.00878425, -289.41562699, -0.06466276, -28.9415627, -0.25425938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2744990, 33805595.4733381, 0.125, 0.00260417, 0.00065104, 14085664.78055754, 0.00178813)
    ops.section('Aggregator', 2744991, 2744990, 'Mz')
    ops.section('Aggregator', 2744992, 2744991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2744, 2744991, 0.52743557686, 2744992, 0.52743557686, 2744990)
    # Create element
    ops.element('forceBeamColumn', 2744, 744, 754, 2744, 2744)

    # Create geometric transformation
    ops.geomTransf('Linear', 2005, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2005990, 139.12221682, 0.00960537, 168.02923494, 0.08337907, 16.80292349, 0.29859536, -212.70694159, -0.0104199, -256.90350167, -0.09198627, -25.69035017, -0.30720255, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2005991, 138.93395517, 0.00950018, 167.801856, 0.08542996, 16.7801856, 0.30064625, -313.8850229, -0.01120814, -379.10451301, -0.1031773, -37.9104513, -0.31839358, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2005990, 32423821.49681959, 0.1125, 0.00189844, 0.00058594, 13509925.62367483, 0.00152995)
    ops.section('Aggregator', 2005991, 2005990, 'Mz')
    ops.section('Aggregator', 2005992, 2005991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2005, 2005991, 0.46464885744, 2005992, 0.46464885744, 2005990)
    # Create element
    ops.element('forceBeamColumn', 2005, 5, 15, 2005, 2005)

    # Create geometric transformation
    ops.geomTransf('Linear', 2105, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2105990, 241.87819347, 0.0089246, 292.67929365, 0.07558434, 29.26792936, 0.26356654, -357.44936747, -0.00968054, -432.52360573, -0.08270766, -43.25236057, -0.27068986, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2105991, 241.87819347, 0.0089246, 292.67929365, 0.07626286, 29.26792936, 0.26424506, -357.44936747, -0.00968054, -432.52360573, -0.083451, -43.25236057, -0.2714332, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2105990, 31887532.01659039, 0.125, 0.00260417, 0.00065104, 13286471.67357933, 0.00178813)
    ops.section('Aggregator', 2105991, 2105990, 'Mz')
    ops.section('Aggregator', 2105992, 2105991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2105, 2105991, 0.53196527348, 2105992, 0.53196527348, 2105990)
    # Create element
    ops.element('forceBeamColumn', 2105, 105, 115, 2105, 2105)

    # Create geometric transformation
    ops.geomTransf('Linear', 2205, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2205990, 239.88056668, 0.00873396, 288.86159697, 0.07498249, 28.8861597, 0.26452212, -354.51911472, -0.00945749, -426.90810285, -0.08203412, -42.69081029, -0.27157375, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2205991, 239.88056668, 0.00873396, 288.86159697, 0.07457938, 28.8861597, 0.26411901, -354.51911472, -0.00945749, -426.90810285, -0.08159251, -42.69081029, -0.27113214, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2205990, 33242707.66562568, 0.125, 0.00260417, 0.00065104, 13851128.1940107, 0.00178813)
    ops.section('Aggregator', 2205991, 2205990, 'Mz')
    ops.section('Aggregator', 2205992, 2205991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2205, 2205991, 0.52759414112, 2205992, 0.52759414112, 2205990)
    # Create element
    ops.element('forceBeamColumn', 2205, 205, 215, 2205, 2205)

    # Create geometric transformation
    ops.geomTransf('Linear', 2305, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2305990, 142.76933774, 0.00942046, 171.27698218, 0.08177508, 17.12769822, 0.29557549, -322.4302122, -0.01107646, -386.8118644, -0.09871523, -38.68118644, -0.31251565, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2305991, 142.76933774, 0.00942046, 171.27698218, 0.08072242, 17.12769822, 0.29452283, -322.4302122, -0.01107646, -386.8118644, -0.09744021, -38.68118644, -0.31124062, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2305990, 34212205.21145217, 0.1125, 0.00189844, 0.00058594, 14255085.50477174, 0.00152995)
    ops.section('Aggregator', 2305991, 2305990, 'Mz')
    ops.section('Aggregator', 2305992, 2305991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2305, 2305991, 0.46772594594, 2305992, 0.46772594594, 2305990)
    # Create element
    ops.element('forceBeamColumn', 2305, 305, 315, 2305, 2305)

    # Create geometric transformation
    ops.geomTransf('Linear', 2405, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2405990, 140.28806652, 0.00933471, 169.53734585, 0.08480357, 16.95373459, 0.30044018, -316.61730398, -0.01103306, -382.63024576, -0.10244393, -38.26302458, -0.31808054, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2405991, 140.28806652, 0.00933471, 169.53734585, 0.08421821, 16.95373459, 0.29985483, -316.61730398, -0.01103306, -382.63024576, -0.10173492, -38.26302458, -0.31737154, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2405990, 32255736.96473103, 0.1125, 0.00189844, 0.00058594, 13439890.40197126, 0.00152995)
    ops.section('Aggregator', 2405991, 2405990, 'Mz')
    ops.section('Aggregator', 2405992, 2405991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2405, 2405991, 0.46374314033, 2405992, 0.46374314033, 2405990)
    # Create element
    ops.element('forceBeamColumn', 2405, 405, 415, 2405, 2405)

    # Create geometric transformation
    ops.geomTransf('Linear', 2505, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2505990, 247.92919512, 0.0088357, 297.96433021, 0.07331741, 29.79643302, 0.26015155, -366.26780533, -0.0095656, -440.18511511, -0.08020663, -44.01851151, -0.26704078, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2505991, 247.92919512, 0.0088357, 297.96433021, 0.07272133, 29.79643302, 0.25955548, -366.26780533, -0.0095656, -440.18511511, -0.07955362, -44.01851151, -0.26638776, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2505990, 33760990.43006968, 0.125, 0.00260417, 0.00065104, 14067079.34586237, 0.00178813)
    ops.section('Aggregator', 2505991, 2505990, 'Mz')
    ops.section('Aggregator', 2505992, 2505991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2505, 2505991, 0.53523407796, 2505992, 0.53523407796, 2505990)
    # Create element
    ops.element('forceBeamColumn', 2505, 505, 515, 2505, 2505)

    # Create geometric transformation
    ops.geomTransf('Linear', 2605, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2605990, 244.41421286, 0.00882867, 292.54117051, 0.07114955, 29.25411705, 0.25875208, -361.29951225, -0.00954111, -432.44204574, -0.07781492, -43.24420457, -0.26541745, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2605991, 244.41421286, 0.00882867, 292.54117051, 0.07091798, 29.25411705, 0.25852052, -361.29951225, -0.00954111, -432.44204574, -0.07756123, -43.24420457, -0.26516376, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2605990, 34778344.37718842, 0.125, 0.00260417, 0.00065104, 14490976.82382851, 0.00178813)
    ops.section('Aggregator', 2605991, 2605990, 'Mz')
    ops.section('Aggregator', 2605992, 2605991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2605, 2605991, 0.5330418461599999, 2605992, 0.5330418461599999, 2605990)
    # Create element
    ops.element('forceBeamColumn', 2605, 605, 615, 2605, 2605)

    # Create geometric transformation
    ops.geomTransf('Linear', 2705, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2705990, 140.31313293, 0.00965223, 169.92572655, 0.08313712, 16.99257266, 0.29761399, -214.47649268, -0.01048356, -259.74100275, -0.0917306, -25.97410027, -0.30620747, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2705991, 140.15315694, 0.0095409, 169.73198819, 0.08533844, 16.97319882, 0.29981531, -316.48050354, -0.01128554, -383.27260165, -0.10309452, -38.32726016, -0.31757139, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2705990, 31637513.73935881, 0.1125, 0.00189844, 0.00058594, 13182297.3913995, 0.00152995)
    ops.section('Aggregator', 2705991, 2705990, 'Mz')
    ops.section('Aggregator', 2705992, 2705991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2705, 2705991, 0.46625074383, 2705992, 0.46625074383, 2705990)
    # Create element
    ops.element('forceBeamColumn', 2705, 705, 715, 2705, 2705)

    # Create geometric transformation
    ops.geomTransf('Linear', 2015, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2015990, 139.29146055, 0.00942816, 167.04832871, 0.08078513, 16.70483287, 0.29611374, -314.85066651, -0.01106945, -377.59154384, -0.09749984, -37.75915438, -0.31282844, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2015991, 206.6802407, 0.0100539, 247.86579629, 0.08083683, 24.78657963, 0.29616544, -213.31315778, -0.01021313, -255.82046708, -0.0816492, -25.58204671, -0.29697781, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2015990, 34296171.28273383, 0.1125, 0.00189844, 0.00058594, 14290071.36780576, 0.00152995)
    ops.section('Aggregator', 2015991, 2015990, 'Mz')
    ops.section('Aggregator', 2015992, 2015991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2015, 2015991, 0.46440648383000005, 2015992, 0.46440648383000005, 2015990)
    # Create element
    ops.element('forceBeamColumn', 2015, 15, 25, 2015, 2015)

    # Create geometric transformation
    ops.geomTransf('Linear', 2115, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2115990, 236.64942989, 0.00910245, 286.63847543, 0.07648136, 28.66384754, 0.26470643, -349.98916637, -0.0098673, -423.91972425, -0.08368228, -42.39197243, -0.27190735, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2115991, 350.33310373, 0.00971699, 424.3363138, 0.08699234, 42.43363138, 0.27521741, -350.33310373, -0.00971699, -424.3363138, -0.08699234, -42.43363138, -0.27521741, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2115990, 31590346.24743705, 0.125, 0.00260417, 0.00065104, 13162644.26976544, 0.00178813)
    ops.section('Aggregator', 2115991, 2115990, 'Mz')
    ops.section('Aggregator', 2115992, 2115991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2115, 2115991, 0.53127884247, 2115992, 0.53127884247, 2115990)
    # Create element
    ops.element('forceBeamColumn', 2115, 115, 125, 2115, 2115)

    # Create geometric transformation
    ops.geomTransf('Linear', 2215, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2215990, 242.82579996, 0.0088442, 292.63602698, 0.07504785, 29.2636027, 0.26316128, -358.85394167, -0.00957976, -432.46472069, -0.08210721, -43.24647207, -0.27022064, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2215991, 359.66593251, 0.0094303, 433.4432731, 0.08542595, 43.34432731, 0.27353938, -359.66593251, -0.0094303, -433.4432731, -0.08542595, -43.34432731, -0.27353938, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2215990, 33033155.58413218, 0.125, 0.00260417, 0.00065104, 13763814.82672174, 0.00178813)
    ops.section('Aggregator', 2215991, 2215990, 'Mz')
    ops.section('Aggregator', 2215992, 2215991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2215, 2215991, 0.53159414205, 2215992, 0.53159414205, 2215990)
    # Create element
    ops.element('forceBeamColumn', 2215, 215, 225, 2215, 2215)

    # Create geometric transformation
    ops.geomTransf('Linear', 2315, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2315990, 136.39717504, 0.00956618, 164.11123218, 0.08249397, 16.41112322, 0.29843345, -308.44330075, -0.01123776, -371.11479858, -0.0995708, -37.11147986, -0.31551027, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2315991, 202.23306011, 0.01006988, 243.3240767, 0.08484186, 24.33240767, 0.30078133, -308.62286821, -0.01111351, -371.33085173, -0.09378359, -37.13308517, -0.30972306, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2315990, 33463514.74735133, 0.1125, 0.00189844, 0.00058594, 13943131.14472972, 0.00152995)
    ops.section('Aggregator', 2315991, 2315990, 'Mz')
    ops.section('Aggregator', 2315992, 2315991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2315, 2315991, 0.46309272992, 2315992, 0.46309272992, 2315990)
    # Create element
    ops.element('forceBeamColumn', 2315, 315, 325, 2315, 2315)

    # Create geometric transformation
    ops.geomTransf('Linear', 2415, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2415990, 139.55425926, 0.00936008, 168.20875473, 0.08386944, 16.82087547, 0.29961241, -315.17246491, -0.01103494, -379.88641929, -0.10128362, -37.98864193, -0.3170266, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2415991, 207.12506432, 0.00985879, 249.65378576, 0.086721, 24.96537858, 0.30246397, -315.71860131, -0.01090168, -380.54469318, -0.09588279, -38.05446932, -0.31162576, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2415990, 32987808.32078357, 0.1125, 0.00189844, 0.00058594, 13744920.13365982, 0.00152995)
    ops.section('Aggregator', 2415991, 2415990, 'Mz')
    ops.section('Aggregator', 2415992, 2415991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2415, 2415991, 0.4635145098, 2415992, 0.4635145098, 2415990)
    # Create element
    ops.element('forceBeamColumn', 2415, 415, 425, 2415, 2415)

    # Create geometric transformation
    ops.geomTransf('Linear', 2515, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2515990, 241.65615254, 0.00882696, 292.98178181, 0.07699673, 29.29817818, 0.26574873, -356.9686009, -0.00958606, -432.78557422, -0.08426745, -43.27855742, -0.27301945, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2515991, 357.91793198, 0.00942638, 433.93653483, 0.08880439, 43.39365348, 0.2775564, -357.91793198, -0.00942638, -433.93653483, -0.08880439, -43.39365348, -0.2775564, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2515990, 31300655.78167607, 0.125, 0.00260417, 0.00065104, 13041939.9090317, 0.00178813)
    ops.section('Aggregator', 2515991, 2515990, 'Mz')
    ops.section('Aggregator', 2515992, 2515991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2515, 2515991, 0.5297957049, 2515992, 0.5297957049, 2515990)
    # Create element
    ops.element('forceBeamColumn', 2515, 515, 525, 2515, 2515)

    # Create geometric transformation
    ops.geomTransf('Linear', 2615, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2615990, 240.45031205, 0.00874896, 290.28368574, 0.07543187, 29.02836857, 0.26482246, -355.28543501, -0.00948375, -428.91841016, -0.08253624, -42.89184102, -0.27192684, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2615991, 356.14750508, 0.00933269, 429.95914442, 0.08555734, 42.99591444, 0.27494793, -356.14750508, -0.00933269, -429.95914442, -0.08555734, -42.99591444, -0.27494793, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2615990, 32547826.81906927, 0.125, 0.00260417, 0.00065104, 13561594.50794553, 0.00178813)
    ops.section('Aggregator', 2615991, 2615990, 'Mz')
    ops.section('Aggregator', 2615992, 2615991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2615, 2615991, 0.52800933264, 2615992, 0.52800933264, 2615990)
    # Create element
    ops.element('forceBeamColumn', 2615, 615, 625, 2615, 2615)

    # Create geometric transformation
    ops.geomTransf('Linear', 2715, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2715990, 136.90229338, 0.00961134, 165.01033936, 0.08538534, 16.50103394, 0.30085109, -309.54375377, -0.01130553, -373.09762019, -0.10308601, -37.30976202, -0.31855176, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2715991, 203.14316807, 0.01025271, 244.85143583, 0.08380726, 24.48514358, 0.29927301, -209.67030286, -0.01041781, -252.718687, -0.08465106, -25.2718687, -0.30011681, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2715990, 32990980.02581321, 0.1125, 0.00189844, 0.00058594, 13746241.67742217, 0.00152995)
    ops.section('Aggregator', 2715991, 2715990, 'Mz')
    ops.section('Aggregator', 2715992, 2715991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2715, 2715991, 0.4641108878, 2715992, 0.4641108878, 2715990)
    # Create element
    ops.element('forceBeamColumn', 2715, 715, 725, 2715, 2715)

    # Create geometric transformation
    ops.geomTransf('Linear', 2025, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2025990, 209.07906912, 0.01026652, 252.52129578, 0.09502472, 25.25212958, 0.3449871, -215.76539427, -0.01043225, -260.59689847, -0.09597253, -26.05968985, -0.34593492, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2025991, 209.07906912, 0.01026652, 252.52129578, 0.09595579, 25.25212958, 0.34591818, -215.76539427, -0.01043225, -260.59689847, -0.0969122, -26.05968985, -0.34687458, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2025990, 32424414.29102699, 0.1125, 0.00189844, 0.00058594, 13510172.62126124, 0.00152995)
    ops.section('Aggregator', 2025991, 2025990, 'Mz')
    ops.section('Aggregator', 2025992, 2025991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2025, 2025991, 0.40006019748, 2025992, 0.40006019748, 2025990)
    # Create element
    ops.element('forceBeamColumn', 2025, 25, 35, 2025, 2025)

    # Create geometric transformation
    ops.geomTransf('Linear', 2125, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2125990, 358.51023328, 0.00945315, 431.17117217, 0.10449017, 43.11711722, 0.32013674, -358.51023328, -0.00945315, -431.17117217, -0.10449017, -43.11711722, -0.32013674, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2125991, 358.51023328, 0.00945315, 431.17117217, 0.10364979, 43.11711722, 0.31929635, -358.51023328, -0.00945315, -431.17117217, -0.10364979, -43.11711722, -0.31929635, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2125990, 33574977.83777252, 0.125, 0.00260417, 0.00065104, 13989574.09907188, 0.00178813)
    ops.section('Aggregator', 2125991, 2125990, 'Mz')
    ops.section('Aggregator', 2125992, 2125991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2125, 2125991, 0.46372173732, 2125992, 0.46372173732, 2125990)
    # Create element
    ops.element('forceBeamColumn', 2125, 125, 135, 2125, 2125)

    # Create geometric transformation
    ops.geomTransf('Linear', 2225, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2225990, 359.54674826, 0.00949335, 434.44798916, 0.10564184, 43.44479892, 0.32104319, -359.54674826, -0.00949335, -434.44798916, -0.10564184, -43.44479892, -0.32104319, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2225991, 359.54674826, 0.00949335, 434.44798916, 0.10581615, 43.44479892, 0.32121749, -359.54674826, -0.00949335, -434.44798916, -0.10581615, -43.44479892, -0.32121749, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2225990, 32296733.7864488, 0.125, 0.00260417, 0.00065104, 13456972.41102033, 0.00178813)
    ops.section('Aggregator', 2225991, 2225990, 'Mz')
    ops.section('Aggregator', 2225992, 2225991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2225, 2225991, 0.46424964513, 2225992, 0.46424964513, 2225990)
    # Create element
    ops.element('forceBeamColumn', 2225, 225, 235, 2225, 2225)

    # Create geometric transformation
    ops.geomTransf('Linear', 2325, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2325990, 205.7544254, 0.01008137, 248.41559329, 0.11978342, 24.84155933, 0.37145289, -313.80881168, -0.01114872, -378.87399983, -0.13243852, -37.88739998, -0.38410799, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2325991, 205.7544254, 0.01008137, 248.41559329, 0.12073566, 24.84155933, 0.37240513, -313.80881168, -0.01114872, -378.87399983, -0.13349134, -37.88739998, -0.38516081, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2325990, 32526887.18711117, 0.1125, 0.00189844, 0.00058594, 13552869.66129632, 0.00152995)
    ops.section('Aggregator', 2325991, 2325990, 'Mz')
    ops.section('Aggregator', 2325992, 2325991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2325, 2325991, 0.39734656869, 2325992, 0.39734656869, 2325990)
    # Create element
    ops.element('forceBeamColumn', 2325, 325, 335, 2325, 2325)

    # Create geometric transformation
    ops.geomTransf('Linear', 2425, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2425990, 198.46520553, 0.00975785, 237.83790013, 0.11796518, 23.78379001, 0.37510523, -302.88407051, -0.0107546, -362.97199361, -0.13039178, -36.29719936, -0.38753183, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2425991, 198.46520553, 0.00975785, 237.83790013, 0.11826517, 23.78379001, 0.37540522, -302.88407051, -0.0107546, -362.97199361, -0.13072346, -36.29719936, -0.38786351, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2425990, 34478575.75101084, 0.1125, 0.00189844, 0.00058594, 14366073.22958785, 0.00152995)
    ops.section('Aggregator', 2425991, 2425990, 'Mz')
    ops.section('Aggregator', 2425992, 2425991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2425, 2425991, 0.38889313828000005, 2425992, 0.38889313828000005, 2425990)
    # Create element
    ops.element('forceBeamColumn', 2425, 425, 435, 2425, 2425)

    # Create geometric transformation
    ops.geomTransf('Linear', 2525, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2525990, 369.94389388, 0.00971254, 447.24633212, 0.10542408, 44.72463321, 0.31692263, -369.94389388, -0.00971254, -447.24633212, -0.10542408, -44.72463321, -0.31692263, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2525991, 369.94389388, 0.00971254, 447.24633212, 0.10591011, 44.72463321, 0.31740866, -369.94389388, -0.00971254, -447.24633212, -0.10591011, -44.72463321, -0.31740866, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2525990, 32145585.38202542, 0.125, 0.00260417, 0.00065104, 13393993.90917726, 0.00178813)
    ops.section('Aggregator', 2525991, 2525990, 'Mz')
    ops.section('Aggregator', 2525992, 2525991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2525, 2525991, 0.47281647656000003, 2525992, 0.47281647656000003, 2525990)
    # Create element
    ops.element('forceBeamColumn', 2525, 525, 535, 2525, 2525)

    # Create geometric transformation
    ops.geomTransf('Linear', 2625, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2625990, 352.83458417, 0.00932034, 425.16446316, 0.1059688, 42.51644632, 0.32406728, -352.83458417, -0.00932034, -425.16446316, -0.1059688, -42.51644632, -0.32406728, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2625991, 352.83458417, 0.00932034, 425.16446316, 0.10580351, 42.51644632, 0.32390199, -352.83458417, -0.00932034, -425.16446316, -0.10580351, -42.51644632, -0.32390199, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2625990, 33062556.82320538, 0.125, 0.00260417, 0.00065104, 13776065.34300224, 0.00178813)
    ops.section('Aggregator', 2625991, 2625990, 'Mz')
    ops.section('Aggregator', 2625992, 2625991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2625, 2625991, 0.45850846548, 2625992, 0.45850846548, 2625990)
    # Create element
    ops.element('forceBeamColumn', 2625, 625, 635, 2625, 2625)

    # Create geometric transformation
    ops.geomTransf('Linear', 2725, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2725990, 205.78656149, 0.00997201, 247.95228549, 0.09774595, 24.79522855, 0.35131298, -212.36791199, -0.01013171, -255.88215655, -0.09871557, -25.58821566, -0.3522826, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2725991, 205.78656149, 0.00997201, 247.95228549, 0.0977415, 24.79522855, 0.35130853, -212.36791199, -0.01013171, -255.88215655, -0.09871107, -25.58821566, -0.3522781, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2725990, 33084157.15847049, 0.1125, 0.00189844, 0.00058594, 13785065.48269604, 0.00152995)
    ops.section('Aggregator', 2725991, 2725990, 'Mz')
    ops.section('Aggregator', 2725992, 2725991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2725, 2725991, 0.39437303841, 2725992, 0.39437303841, 2725990)
    # Create element
    ops.element('forceBeamColumn', 2725, 725, 735, 2725, 2725)

    # Create geometric transformation
    ops.geomTransf('Linear', 2035, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2035990, 201.97797933, 0.01016353, 243.92471882, 0.08620873, 24.39247188, 0.30263963, -208.45664325, -0.01032801, -251.74887014, -0.0870749, -25.17488701, -0.3035058, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2035991, 136.12181139, 0.00951963, 164.39155733, 0.08612162, 16.43915573, 0.30255252, -307.70151519, -0.01121771, -371.60489387, -0.10400107, -37.16048939, -0.32043198, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2035990, 32447640.85780955, 0.1125, 0.00189844, 0.00058594, 13519850.35742065, 0.00152995)
    ops.section('Aggregator', 2035991, 2035990, 'Mz')
    ops.section('Aggregator', 2035992, 2035991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2035, 2035991, 0.4620412266, 2035992, 0.4620412266, 2035990)
    # Create element
    ops.element('forceBeamColumn', 2035, 35, 45, 2035, 2035)

    # Create geometric transformation
    ops.geomTransf('Linear', 2135, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2135990, 359.09392519, 0.00940607, 432.24519287, 0.09297293, 43.22451929, 0.28127351, -359.09392519, -0.00940607, -432.24519287, -0.09297293, -43.22451929, -0.28127351, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2135991, 242.43748375, 0.00882384, 291.82458841, 0.08055473, 29.18245884, 0.2688553, -358.30527329, -0.00955343, -431.29588415, -0.08813608, -43.12958841, -0.27643666, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2135990, 33348485.09640383, 0.125, 0.00260417, 0.00065104, 13895202.1235016, 0.00178813)
    ops.section('Aggregator', 2135991, 2135990, 'Mz')
    ops.section('Aggregator', 2135992, 2135991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2135, 2135991, 0.53106582527, 2135992, 0.53106582527, 2135990)
    # Create element
    ops.element('forceBeamColumn', 2135, 135, 145, 2135, 2135)

    # Create geometric transformation
    ops.geomTransf('Linear', 2235, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2235990, 357.35684955, 0.00926254, 427.15237319, 0.08966869, 42.71523732, 0.27884892, -357.35684955, -0.00926254, -427.15237319, -0.08966869, -42.71523732, -0.27884892, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2235991, 241.24350902, 0.0087015, 288.36088499, 0.07794794, 28.8360885, 0.26712817, -356.62950417, -0.00939995, -426.28296966, -0.08526084, -42.62829697, -0.27444107, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2235990, 35095891.01303406, 0.125, 0.00260417, 0.00065104, 14623287.92209753, 0.00178813)
    ops.section('Aggregator', 2235991, 2235990, 'Mz')
    ops.section('Aggregator', 2235992, 2235991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2235, 2235991, 0.52859646503, 2235992, 0.52859646503, 2235990)
    # Create element
    ops.element('forceBeamColumn', 2235, 235, 245, 2235, 2235)

    # Create geometric transformation
    ops.geomTransf('Linear', 2335, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2335990, 205.037888, 0.01022345, 246.53943104, 0.08539962, 24.6539431, 0.29955049, -312.92453269, -0.0112794, -376.26331894, -0.09439637, -37.62633189, -0.30854724, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2335991, 138.29705091, 0.00971326, 166.28963836, 0.08270289, 16.62896384, 0.29685376, -312.7616058, -0.01140429, -376.06741416, -0.09981221, -37.60674142, -0.31396308, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2335990, 33632484.9612041, 0.1125, 0.00189844, 0.00058594, 14013535.40050171, 0.00152995)
    ops.section('Aggregator', 2335991, 2335990, 'Mz')
    ops.section('Aggregator', 2335992, 2335991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2335, 2335991, 0.46696051399, 2335992, 0.46696051399, 2335990)
    # Create element
    ops.element('forceBeamColumn', 2335, 335, 345, 2335, 2335)

    # Create geometric transformation
    ops.geomTransf('Linear', 2435, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2435990, 211.04251306, 0.01012717, 254.85029733, 0.08495803, 25.48502973, 0.29799179, -321.70238957, -0.01120631, -388.48073046, -0.0939415, -38.84807305, -0.30697526, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2435991, 142.20840441, 0.00961183, 171.72774159, 0.08374849, 17.17277416, 0.29678224, -321.17275945, -0.0113447, -387.84116077, -0.10114195, -38.78411608, -0.31417571, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2435990, 32471435.33960048, 0.1125, 0.00189844, 0.00058594, 13529764.72483354, 0.00152995)
    ops.section('Aggregator', 2435991, 2435990, 'Mz')
    ops.section('Aggregator', 2435992, 2435991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2435, 2435991, 0.4694091776, 2435992, 0.4694091776, 2435990)
    # Create element
    ops.element('forceBeamColumn', 2435, 435, 445, 2435, 2435)

    # Create geometric transformation
    ops.geomTransf('Linear', 2535, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2535990, 356.79237895, 0.00957745, 433.11221657, 0.09596828, 43.31122166, 0.28406068, -356.79237895, -0.00957745, -433.11221657, -0.09596828, -43.31122166, -0.28406068, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2535991, 240.92792406, 0.00896551, 292.46372227, 0.08444745, 29.24637223, 0.27253986, -356.01674864, -0.00973803, -432.17067471, -0.09243004, -43.21706747, -0.28052245, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2535990, 30911350.74960041, 0.125, 0.00260417, 0.00065104, 12879729.47900017, 0.00178813)
    ops.section('Aggregator', 2535991, 2535990, 'Mz')
    ops.section('Aggregator', 2535992, 2535991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2535, 2535991, 0.5316535731, 2535992, 0.5316535731, 2535990)
    # Create element
    ops.element('forceBeamColumn', 2535, 535, 545, 2535, 2535)

    # Create geometric transformation
    ops.geomTransf('Linear', 2635, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2635990, 355.94566267, 0.00937965, 429.06747582, 0.09391799, 42.90674758, 0.2829743, -355.94566267, -0.00937965, -429.06747582, -0.09391799, -42.90674758, -0.2829743, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2635991, 240.32293682, 0.00879627, 289.69240728, 0.08157812, 28.96924073, 0.27063443, -355.19030701, -0.00952761, -428.15694766, -0.08926162, -42.81569477, -0.27831793, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2635990, 32965003.34575969, 0.125, 0.00260417, 0.00065104, 13735418.06073321, 0.00178813)
    ops.section('Aggregator', 2635991, 2635990, 'Mz')
    ops.section('Aggregator', 2635992, 2635991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2635, 2635991, 0.52894293213, 2635992, 0.52894293213, 2635990)
    # Create element
    ops.element('forceBeamColumn', 2635, 635, 645, 2635, 2635)

    # Create geometric transformation
    ops.geomTransf('Linear', 2735, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2735990, 209.30212633, 0.01047093, 252.7520852, 0.08354709, 25.27520852, 0.29595549, -216.01146359, -0.01064024, -260.8542436, -0.08439069, -26.08542436, -0.29679909, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2735991, 141.06030666, 0.00980569, 170.3436428, 0.08316979, 17.03436428, 0.29557818, -318.82805807, -0.01155762, -385.014992, -0.10041912, -38.5014992, -0.31282751, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2735990, 32467594.12143791, 0.1125, 0.00189844, 0.00058594, 13528164.2172658, 0.00152995)
    ops.section('Aggregator', 2735991, 2735990, 'Mz')
    ops.section('Aggregator', 2735992, 2735991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2735, 2735991, 0.47079117997, 2735992, 0.47079117997, 2735990)
    # Create element
    ops.element('forceBeamColumn', 2735, 735, 745, 2735, 2735)

    # Create geometric transformation
    ops.geomTransf('Linear', 2045, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2045990, 138.67462026, 0.00937193, 167.75759914, 0.08482423, 16.77575991, 0.30099445, -313.11332207, -0.01107858, -378.77975849, -0.10246938, -37.87797585, -0.3186396, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2045991, 138.8143839, 0.00948181, 167.92667415, 0.08340008, 16.79266742, 0.2995703, -212.18060487, -0.01029521, -256.67933174, -0.09202141, -25.66793317, -0.30819163, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2045990, 31961925.96060545, 0.1125, 0.00189844, 0.00058594, 13317469.15025227, 0.00152995)
    ops.section('Aggregator', 2045991, 2045990, 'Mz')
    ops.section('Aggregator', 2045992, 2045991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2045, 2045991, 0.46259841153000003, 2045992, 0.46259841153000003, 2045990)
    # Create element
    ops.element('forceBeamColumn', 2045, 45, 55, 2045, 2045)

    # Create geometric transformation
    ops.geomTransf('Linear', 2145, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2145990, 244.19929363, 0.00904746, 293.31219451, 0.0732476, 29.33121945, 0.25961498, -361.10161828, -0.00978315, -433.72569398, -0.08011572, -43.3725694, -0.2664831, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2145991, 244.19929363, 0.00904746, 293.31219451, 0.07316095, 29.33121945, 0.25952833, -361.10161828, -0.00978315, -433.72569398, -0.08002079, -43.3725694, -0.26638817, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2145990, 33909064.82664821, 0.125, 0.00260417, 0.00065104, 14128777.01110342, 0.00178813)
    ops.section('Aggregator', 2145991, 2145990, 'Mz')
    ops.section('Aggregator', 2145992, 2145991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2145, 2145991, 0.5365745940100001, 2145992, 0.5365745940100001, 2145990)
    # Create element
    ops.element('forceBeamColumn', 2145, 145, 155, 2145, 2145)

    # Create geometric transformation
    ops.geomTransf('Linear', 2245, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2245990, 238.85964955, 0.00860214, 288.9957676, 0.07770038, 28.89957676, 0.26855644, -352.77125407, -0.00933609, -426.81716879, -0.08503462, -42.68171688, -0.27589069, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2245991, 238.85964955, 0.00860214, 288.9957676, 0.07776103, 28.89957676, 0.2686171, -352.77125407, -0.00933609, -426.81716879, -0.08510107, -42.68171688, -0.27595714, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2245990, 31919072.13700275, 0.125, 0.00260417, 0.00065104, 13299613.39041781, 0.00178813)
    ops.section('Aggregator', 2245991, 2245990, 'Mz')
    ops.section('Aggregator', 2245992, 2245991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2245, 2245991, 0.52395505673, 2245992, 0.52395505673, 2245990)
    # Create element
    ops.element('forceBeamColumn', 2245, 245, 255, 2245, 2245)

    # Create geometric transformation
    ops.geomTransf('Linear', 2345, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2345990, 138.61816569, 0.00943575, 166.27162384, 0.08145066, 16.62716238, 0.29705111, -313.36935108, -0.01107671, -375.88457911, -0.09830401, -37.58845791, -0.31390446, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2345991, 138.61816569, 0.00943575, 166.27162384, 0.08106919, 16.62716238, 0.29666965, -313.36935108, -0.01107671, -375.88457911, -0.09784197, -37.58845791, -0.31344242, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2345990, 34250152.72004593, 0.1125, 0.00189844, 0.00058594, 14270896.96668581, 0.00152995)
    ops.section('Aggregator', 2345991, 2345990, 'Mz')
    ops.section('Aggregator', 2345992, 2345991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2345, 2345991, 0.46382091598, 2345992, 0.46382091598, 2345990)
    # Create element
    ops.element('forceBeamColumn', 2345, 345, 355, 2345, 2345)

    # Create geometric transformation
    ops.geomTransf('Linear', 2445, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2445990, 140.96317701, 0.00978194, 169.57850615, 0.0821358, 16.95785062, 0.29464203, -318.71754568, -0.01149602, -383.41676475, -0.09913388, -38.34167648, -0.31164011, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2445991, 140.96317701, 0.00978194, 169.57850615, 0.08217171, 16.95785062, 0.29467794, -318.71754568, -0.01149602, -383.41676475, -0.09917738, -38.34167648, -0.31168361, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2445990, 33504518.53894109, 0.1125, 0.00189844, 0.00058594, 13960216.05789212, 0.00152995)
    ops.section('Aggregator', 2445991, 2445990, 'Mz')
    ops.section('Aggregator', 2445992, 2445991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2445, 2445991, 0.47057444984, 2445992, 0.47057444984, 2445990)
    # Create element
    ops.element('forceBeamColumn', 2445, 445, 455, 2445, 2445)

    # Create geometric transformation
    ops.geomTransf('Linear', 2545, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2545990, 239.36413723, 0.00879382, 286.98988266, 0.07241673, 28.69898827, 0.26155356, -353.92921919, -0.0095049, -424.34972198, -0.0792051, -42.4349722, -0.26834194, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2545991, 239.36413723, 0.00879382, 286.98988266, 0.07211508, 28.69898827, 0.26125192, -353.92921919, -0.0095049, -424.34972198, -0.07887464, -42.4349722, -0.26801148, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2545990, 34359019.1175016, 0.125, 0.00260417, 0.00065104, 14316257.96562567, 0.00178813)
    ops.section('Aggregator', 2545991, 2545990, 'Mz')
    ops.section('Aggregator', 2545992, 2545991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2545, 2545991, 0.5287177428000001, 2545992, 0.5287177428000001, 2545990)
    # Create element
    ops.element('forceBeamColumn', 2545, 545, 555, 2545, 2545)

    # Create geometric transformation
    ops.geomTransf('Linear', 2645, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2645990, 233.53796356, 0.00860626, 279.47851833, 0.07190607, 27.94785183, 0.26371689, -345.37294368, -0.00929555, -413.31318085, -0.0786418, -41.33131809, -0.27045261, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2645991, 233.53796356, 0.00860626, 279.47851833, 0.07194439, 27.94785183, 0.26375521, -345.37294368, -0.00929555, -413.31318085, -0.07868377, -41.33131809, -0.27049459, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2645990, 34816816.50688168, 0.125, 0.00260417, 0.00065104, 14507006.87786737, 0.00178813)
    ops.section('Aggregator', 2645991, 2645990, 'Mz')
    ops.section('Aggregator', 2645992, 2645991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2645, 2645991, 0.5213470346000001, 2645992, 0.5213470346000001, 2645990)
    # Create element
    ops.element('forceBeamColumn', 2645, 645, 655, 2645, 2645)

    # Create geometric transformation
    ops.geomTransf('Linear', 2745, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2745990, 137.78688058, 0.00948413, 166.26876167, 0.08529203, 16.62687617, 0.30112208, -311.38223105, -0.01117732, -375.74795035, -0.10299885, -37.57479504, -0.3188289, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2745991, 137.99844405, 0.00958574, 166.52405735, 0.08299236, 16.65240574, 0.29882241, -211.01450617, -0.01039351, -254.63324584, -0.09155402, -25.46332458, -0.30738407, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2745990, 32672924.71985362, 0.1125, 0.00189844, 0.00058594, 13613718.63327234, 0.00152995)
    ops.section('Aggregator', 2745991, 2745990, 'Mz')
    ops.section('Aggregator', 2745992, 2745991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2745, 2745991, 0.46332751045, 2745992, 0.46332751045, 2745990)
    # Create element
    ops.element('forceBeamColumn', 2745, 745, 755, 2745, 2745)

    # Create geometric transformation
    ops.geomTransf('Linear', 2006, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2006990, 140.29782412, 0.00936734, 169.72793472, 0.07779281, 16.97279347, 0.294075, -207.65073465, -0.01001863, -251.20938658, -0.08498013, -25.12093866, -0.30126232, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2006991, 140.29782412, 0.00936734, 169.72793472, 0.077372, 16.97279347, 0.29365419, -207.65073465, -0.01001863, -251.20938658, -0.08451913, -25.12093866, -0.30080132, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2006990, 31950344.32571819, 0.1125, 0.00189844, 0.00058594, 13312643.46904925, 0.00152995)
    ops.section('Aggregator', 2006991, 2006990, 'Mz')
    ops.section('Aggregator', 2006992, 2006991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2006, 2006991, 0.46235892689999997, 2006992, 0.46235892689999997, 2006990)
    # Create element
    ops.element('forceBeamColumn', 2006, 6, 16, 2006, 2006)

    # Create geometric transformation
    ops.geomTransf('Linear', 2106, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2106990, 136.55354207, 0.00942104, 165.32211039, 0.08305673, 16.53221104, 0.30068414, -208.74315632, -0.0102304, -252.72035137, -0.09164416, -25.27203514, -0.30927158, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2106991, 136.38558694, 0.00931385, 165.11877113, 0.08586012, 16.51187711, 0.30348754, -308.0181918, -0.01101215, -372.91026462, -0.10372803, -37.29102646, -0.32135544, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2106990, 31728908.61925929, 0.1125, 0.00189844, 0.00058594, 13220378.59135804, 0.00152995)
    ops.section('Aggregator', 2106991, 2106990, 'Mz')
    ops.section('Aggregator', 2106992, 2106991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2106, 2106991, 0.45950093889, 2106992, 0.45950093889, 2106990)
    # Create element
    ops.element('forceBeamColumn', 2106, 106, 116, 2106, 2106)

    # Create geometric transformation
    ops.geomTransf('Linear', 2206, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2206990, 139.69536347, 0.0094947, 167.40312708, 0.07791023, 16.74031271, 0.29331396, -213.64034066, -0.01027472, -256.01466082, -0.08591692, -25.60146608, -0.30132066, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2206991, 139.52005051, 0.00939611, 167.1930418, 0.08053493, 16.71930418, 0.29593866, -315.34728238, -0.01102878, -377.89458343, -0.09719493, -37.78945834, -0.31259867, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2206990, 34487107.16471525, 0.1125, 0.00189844, 0.00058594, 14369627.98529802, 0.00152995)
    ops.section('Aggregator', 2206991, 2206990, 'Mz')
    ops.section('Aggregator', 2206992, 2206991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2206, 2206991, 0.46424450595000005, 2206992, 0.46424450595000005, 2206990)
    # Create element
    ops.element('forceBeamColumn', 2206, 206, 216, 2206, 2206)

    # Create geometric transformation
    ops.geomTransf('Linear', 2306, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2306990, 141.66402051, 0.00947457, 169.99186311, 0.07819887, 16.99918631, 0.29286969, -216.5839586, -0.01026107, -259.89316489, -0.08624465, -25.98931649, -0.30091548, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2306991, 141.55173512, 0.00936937, 169.85712457, 0.0811768, 16.98571246, 0.29584763, -319.70873795, -0.01101658, -383.63928837, -0.09799258, -38.36392884, -0.31266341, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2306990, 34151973.35748302, 0.1125, 0.00189844, 0.00058594, 14229988.89895126, 0.00152995)
    ops.section('Aggregator', 2306991, 2306990, 'Mz')
    ops.section('Aggregator', 2306992, 2306991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2306, 2306991, 0.4658294838, 2306992, 0.4658294838, 2306990)
    # Create element
    ops.element('forceBeamColumn', 2306, 306, 316, 2306, 2306)

    # Create geometric transformation
    ops.geomTransf('Linear', 2406, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2406990, 136.02765106, 0.00962057, 163.07631433, 0.07847979, 16.30763143, 0.29486207, -208.08387694, -0.01040292, -249.46069022, -0.08653569, -24.94606902, -0.30291797, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2406991, 135.74334069, 0.00953351, 162.73546975, 0.08072837, 16.27354698, 0.29711064, -307.05202322, -0.01117003, -368.10833579, -0.09740406, -36.81083358, -0.31378634, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2406990, 34383946.73592405, 0.1125, 0.00189844, 0.00058594, 14326644.47330169, 0.00152995)
    ops.section('Aggregator', 2406991, 2406990, 'Mz')
    ops.section('Aggregator', 2406992, 2406991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2406, 2406991, 0.46214506012, 2406992, 0.46214506012, 2406990)
    # Create element
    ops.element('forceBeamColumn', 2406, 406, 416, 2406, 2406)

    # Create geometric transformation
    ops.geomTransf('Linear', 2506, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2506990, 137.22756488, 0.00963689, 166.3352293, 0.08569736, 16.63352293, 0.30172788, -209.80018722, -0.01046606, -254.30140278, -0.09456074, -25.43014028, -0.31059126, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2506991, 137.00643046, 0.00953118, 166.06718954, 0.0879543, 16.60671895, 0.30398483, -309.53497353, -0.01127124, -375.19117128, -0.10626043, -37.51911713, -0.32229095, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2506990, 31371158.93367697, 0.1125, 0.00189844, 0.00058594, 13071316.22236541, 0.00152995)
    ops.section('Aggregator', 2506991, 2506990, 'Mz')
    ops.section('Aggregator', 2506992, 2506991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2506, 2506991, 0.46289755339, 2506992, 0.46289755339, 2506990)
    # Create element
    ops.element('forceBeamColumn', 2506, 506, 516, 2506, 2506)

    # Create geometric transformation
    ops.geomTransf('Linear', 2606, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2606990, 139.99429575, 0.00928016, 167.18929155, 0.07684714, 16.71892915, 0.29337244, -214.06022879, -0.01003767, -255.64311609, -0.08474169, -25.56431161, -0.301267, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2606991, 139.89231828, 0.00917974, 167.06750415, 0.07892087, 16.70675042, 0.29544618, -316.02973467, -0.01076475, -377.42100251, -0.09523797, -37.74210025, -0.31176328, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2606990, 35301806.89034536, 0.1125, 0.00189844, 0.00058594, 14709086.20431057, 0.00152995)
    ops.section('Aggregator', 2606991, 2606990, 'Mz')
    ops.section('Aggregator', 2606992, 2606991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2606, 2606991, 0.46183977771999996, 2606992, 0.46183977771999996, 2606990)
    # Create element
    ops.element('forceBeamColumn', 2606, 606, 616, 2606, 2606)

    # Create geometric transformation
    ops.geomTransf('Linear', 2706, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2706990, 141.3192555, 0.00988517, 170.90041481, 0.07503928, 17.09004148, 0.28528197, -209.29494895, -0.01055916, -253.10488276, -0.08193683, -25.31048828, -0.29217952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2706991, 141.3192555, 0.00988517, 170.90041481, 0.07569117, 17.09004148, 0.28833688, -209.29494895, -0.01055916, -253.10488276, -0.08265099, -25.31048828, -0.2952967, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2706990, 32058276.46430947, 0.1125, 0.00189844, 0.00058594, 13357615.19346228, 0.00152995)
    ops.section('Aggregator', 2706991, 2706990, 'Mz')
    ops.section('Aggregator', 2706992, 2706991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2706, 2706991, 0.47026576868000003, 2706992, 0.47026576868000003, 2706990)
    # Create element
    ops.element('forceBeamColumn', 2706, 706, 716, 2706, 2706)

    # Create geometric transformation
    ops.geomTransf('Linear', 2016, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2016990, 140.13062375, 0.00960336, 167.47825159, 0.07271543, 16.74782516, 0.28724948, -207.59554395, -0.01022548, -248.10949818, -0.07936606, -24.81094982, -0.29390011, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2016991, 207.60795363, 0.01013148, 248.1243297, 0.07376492, 24.81243297, 0.28657784, -207.60795363, -0.01013148, -248.1243297, -0.07376492, -24.81243297, -0.28657784, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2016990, 35125855.19014736, 0.1125, 0.00189844, 0.00058594, 14635772.99589474, 0.00152995)
    ops.section('Aggregator', 2016991, 2016990, 'Mz')
    ops.section('Aggregator', 2016992, 2016991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2016, 2016991, 0.46612647196, 2016992, 0.46612647196, 2016990)
    # Create element
    ops.element('forceBeamColumn', 2016, 16, 26, 2016, 2016)

    # Create geometric transformation
    ops.geomTransf('Linear', 2116, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2116990, 138.82069209, 0.00937532, 166.62857701, 0.08073857, 16.6628577, 0.29663001, -313.73873496, -0.01101518, -376.58535031, -0.09745317, -37.65853503, -0.31334461, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2116991, 205.99553774, 0.00986708, 247.25956058, 0.08364549, 24.72595606, 0.29953692, -314.16221712, -0.01088915, -377.09366235, -0.09246071, -37.70936624, -0.30835214, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2116990, 34078615.51541766, 0.1125, 0.00189844, 0.00058594, 14199423.13142402, 0.00152995)
    ops.section('Aggregator', 2116991, 2116990, 'Mz')
    ops.section('Aggregator', 2116992, 2116991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2116, 2116991, 0.46319577046, 2116992, 0.46319577046, 2116990)
    # Create element
    ops.element('forceBeamColumn', 2116, 116, 126, 2116, 2116)

    # Create geometric transformation
    ops.geomTransf('Linear', 2216, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2216990, 136.79510877, 0.00942612, 164.28319728, 0.08280277, 16.42831973, 0.29935092, -309.29892675, -0.01106803, -371.45053693, -0.09994472, -37.14505369, -0.31649288, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2216991, 202.90327282, 0.00992024, 243.67536747, 0.08452667, 24.36753675, 0.30107482, -309.57757036, -0.01094462, -371.78517216, -0.09343167, -37.17851722, -0.30997982, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2216990, 33946092.12458348, 0.1125, 0.00189844, 0.00058594, 14144205.05190979, 0.00152995)
    ops.section('Aggregator', 2216991, 2216990, 'Mz')
    ops.section('Aggregator', 2216992, 2216991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2216, 2216991, 0.46179105428000006, 2216992, 0.46179105428000006, 2216990)
    # Create element
    ops.element('forceBeamColumn', 2216, 216, 226, 2216, 2216)

    # Create geometric transformation
    ops.geomTransf('Linear', 2316, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2316990, 137.91972814, 0.00924557, 166.11882971, 0.08519822, 16.61188297, 0.30240052, -311.50412969, -0.0108941, -375.19434075, -0.10289094, -37.51943407, -0.32009325, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2316991, 204.59652733, 0.00987626, 246.42838368, 0.08465313, 24.64283837, 0.30185543, -211.13828241, -0.01003421, -254.30766762, -0.08550106, -25.43076676, -0.30270337, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2316990, 33182474.76577109, 0.1125, 0.00189844, 0.00058594, 13826031.15240462, 0.00152995)
    ops.section('Aggregator', 2316991, 2316990, 'Mz')
    ops.section('Aggregator', 2316992, 2316991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2316, 2316991, 0.46040027438, 2316992, 0.46040027438, 2316990)
    # Create element
    ops.element('forceBeamColumn', 2316, 316, 326, 2316, 2316)

    # Create geometric transformation
    ops.geomTransf('Linear', 2416, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2416990, 134.7682645, 0.00956267, 162.49996001, 0.08595017, 16.249996, 0.3027523, -304.75063193, -0.0112456, -367.46014119, -0.10376915, -36.74601412, -0.32057129, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2416991, 199.97208955, 0.01019823, 241.12098405, 0.08541819, 24.11209841, 0.30222033, -206.40326297, -0.01036282, -248.87552054, -0.08627685, -24.88755205, -0.30307899, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2416990, 32887186.24504921, 0.1125, 0.00189844, 0.00058594, 13702994.2687705, 0.00152995)
    ops.section('Aggregator', 2416991, 2416990, 'Mz')
    ops.section('Aggregator', 2416992, 2416991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2416, 2416991, 0.46125006186, 2416992, 0.46125006186, 2416990)
    # Create element
    ops.element('forceBeamColumn', 2416, 416, 426, 2416, 2416)

    # Create geometric transformation
    ops.geomTransf('Linear', 2516, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2516990, 139.00674499, 0.00936293, 167.32151048, 0.0819132, 16.73215105, 0.29785812, -314.03418278, -0.01102448, -378.00089346, -0.09890024, -37.80008935, -0.31484515, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2516991, 206.29222907, 0.00985905, 248.31260791, 0.0844437, 24.83126079, 0.30038862, -314.52241518, -0.01089409, -378.5885756, -0.09335706, -37.85885756, -0.30930198, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2516990, 33352276.49962775, 0.1125, 0.00189844, 0.00058594, 13896781.8748449, 0.00152995)
    ops.section('Aggregator', 2516991, 2516990, 'Mz')
    ops.section('Aggregator', 2516992, 2516991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2516, 2516991, 0.46308105718000003, 2516992, 0.46308105718000003, 2516990)
    # Create element
    ops.element('forceBeamColumn', 2516, 516, 526, 2516, 2516)

    # Create geometric transformation
    ops.geomTransf('Linear', 2616, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2616990, 138.33440621, 0.00958767, 166.74494386, 0.08400447, 16.67449439, 0.29892737, -312.706856, -0.01128544, -376.92927289, -0.10142201, -37.69292729, -0.31634491, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2616991, 205.17762618, 0.01009661, 247.31614278, 0.08655724, 24.73161428, 0.30148015, -313.0017727, -0.0111556, -377.28475833, -0.09569271, -37.72847583, -0.31061561, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2616990, 32977182.08086959, 0.1125, 0.00189844, 0.00058594, 13740492.53369566, 0.00152995)
    ops.section('Aggregator', 2616991, 2616990, 'Mz')
    ops.section('Aggregator', 2616992, 2616991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2616, 2616991, 0.46528312109000003, 2616992, 0.46528312109000003, 2616990)
    # Create element
    ops.element('forceBeamColumn', 2616, 616, 626, 2616, 2616)

    # Create geometric transformation
    ops.geomTransf('Linear', 2716, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2716990, 141.57989016, 0.00952376, 169.67555057, 0.07343797, 16.96755506, 0.28786783, -209.68327925, -0.01015279, -251.29363932, -0.08017212, -25.12936393, -0.29460199, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2716991, 209.81318178, 0.01005257, 251.44932021, 0.07470276, 25.14493202, 0.28788851, -209.81318178, -0.01005257, -251.44932021, -0.07470276, -25.14493202, -0.28788851, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2716990, 34466702.91501053, 0.1125, 0.00189844, 0.00058594, 14361126.21458772, 0.00152995)
    ops.section('Aggregator', 2716991, 2716990, 'Mz')
    ops.section('Aggregator', 2716992, 2716991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2716, 2716991, 0.46635295734, 2716992, 0.46635295734, 2716990)
    # Create element
    ops.element('forceBeamColumn', 2716, 716, 726, 2716, 2716)

    # Create geometric transformation
    ops.geomTransf('Linear', 2026, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2026990, 205.95044519, 0.00998944, 248.49689137, 0.11615161, 24.84968914, 0.36968722, -205.95044519, -0.00998944, -248.49689137, -0.11615161, -24.84968914, -0.36968722, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2026991, 205.95044519, 0.00998944, 248.49689137, 0.11643537, 24.84968914, 0.36997098, -205.95044519, -0.00998944, -248.49689137, -0.11643537, -24.84968914, -0.36997098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2026990, 32701435.22577892, 0.1125, 0.00189844, 0.00058594, 13625598.01074122, 0.00152995)
    ops.section('Aggregator', 2026991, 2026990, 'Mz')
    ops.section('Aggregator', 2026992, 2026991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2026, 2026991, 0.39442191523000003, 2026992, 0.39442191523000003, 2026990)
    # Create element
    ops.element('forceBeamColumn', 2026, 26, 36, 2026, 2026)

    # Create geometric transformation
    ops.geomTransf('Linear', 2126, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2126990, 209.76761587, 0.00957354, 251.59117834, 0.11745102, 25.15911783, 0.37139903, -319.49240838, -0.01057414, -383.19294978, -0.12984664, -38.31929498, -0.38379465, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2126991, 209.76761587, 0.00957354, 251.59117834, 0.11639973, 25.15911783, 0.37034774, -319.49240838, -0.01057414, -383.19294978, -0.1286843, -38.31929498, -0.38263232, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2126990, 34273666.69579335, 0.1125, 0.00189844, 0.00058594, 14280694.45658056, 0.00152995)
    ops.section('Aggregator', 2126991, 2126990, 'Mz')
    ops.section('Aggregator', 2126992, 2126991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2126, 2126991, 0.39378138539, 2126992, 0.39378138539, 2126990)
    # Create element
    ops.element('forceBeamColumn', 2126, 126, 136, 2126, 2126)

    # Create geometric transformation
    ops.geomTransf('Linear', 2226, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2226990, 205.08163225, 0.00991049, 245.85726512, 0.1185858, 24.58572651, 0.37159863, -312.86276884, -0.01092915, -375.06813194, -0.13108375, -37.50681319, -0.38409657, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2226991, 205.08163225, 0.00991049, 245.85726512, 0.11842556, 24.58572651, 0.37143838, -312.86276884, -0.01092915, -375.06813194, -0.13090658, -37.50681319, -0.3839194, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2226990, 34388157.07005812, 0.1125, 0.00189844, 0.00058594, 14328398.77919088, 0.00152995)
    ops.section('Aggregator', 2226991, 2226990, 'Mz')
    ops.section('Aggregator', 2226992, 2226991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2226, 2226991, 0.39523688427000003, 2226992, 0.39523688427000003, 2226990)
    # Create element
    ops.element('forceBeamColumn', 2226, 226, 236, 2226, 2226)

    # Create geometric transformation
    ops.geomTransf('Linear', 2326, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2326990, 205.17839065, 0.00987168, 246.91824418, 0.09703709, 24.69182442, 0.35162169, -211.73978447, -0.01002915, -254.81443557, -0.09799886, -25.48144356, -0.35258346, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2326991, 205.17839065, 0.00987168, 246.91824418, 0.09580455, 24.69182442, 0.35038915, -211.73978447, -0.01002915, -254.81443557, -0.09675495, -25.48144356, -0.35133955, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2326990, 33409739.57850688, 0.1125, 0.00189844, 0.00058594, 13920724.82437787, 0.00152995)
    ops.section('Aggregator', 2326991, 2326990, 'Mz')
    ops.section('Aggregator', 2326992, 2326991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2326, 2326991, 0.39279674028, 2326992, 0.39279674028, 2326990)
    # Create element
    ops.element('forceBeamColumn', 2326, 326, 336, 2326, 2326)

    # Create geometric transformation
    ops.geomTransf('Linear', 2426, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2426990, 207.28008397, 0.01032101, 249.79726547, 0.09492503, 24.97972655, 0.34507492, -213.93039154, -0.01048688, -257.81168062, -0.09587156, -25.78116806, -0.34602145, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2426991, 207.28008397, 0.01032101, 249.79726547, 0.09429947, 24.97972655, 0.34444936, -213.93039154, -0.01048688, -257.81168062, -0.09524023, -25.78116806, -0.34539012, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2426990, 33034940.48318752, 0.1125, 0.00189844, 0.00058594, 13764558.53466146, 0.00152995)
    ops.section('Aggregator', 2426991, 2426990, 'Mz')
    ops.section('Aggregator', 2426992, 2426991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2426, 2426991, 0.39976032193, 2426992, 0.39976032193, 2426990)
    # Create element
    ops.element('forceBeamColumn', 2426, 426, 436, 2426, 2426)

    # Create geometric transformation
    ops.geomTransf('Linear', 2526, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2526990, 202.31224076, 0.01017827, 243.52252108, 0.11982662, 24.35225211, 0.37205788, -308.78852552, -0.01123227, -371.68764445, -0.13246269, -37.16876444, -0.38469395, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2526991, 202.31224076, 0.01017827, 243.52252108, 0.11998497, 24.35225211, 0.37221623, -308.78852552, -0.01123227, -371.68764445, -0.13263776, -37.16876444, -0.38486902, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2526990, 33351624.42875382, 0.1125, 0.00189844, 0.00058594, 13896510.17864742, 0.00152995)
    ops.section('Aggregator', 2526991, 2526990, 'Mz')
    ops.section('Aggregator', 2526992, 2526991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2526, 2526991, 0.39646156553, 2526992, 0.39646156553, 2526990)
    # Create element
    ops.element('forceBeamColumn', 2526, 526, 536, 2526, 2526)

    # Create geometric transformation
    ops.geomTransf('Linear', 2626, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2626990, 204.96556468, 0.00998311, 246.40595852, 0.11976434, 24.64059585, 0.37235564, -312.67463148, -0.01101987, -375.89188407, -0.13239721, -37.58918841, -0.3849885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2626991, 204.96556468, 0.00998311, 246.40595852, 0.11855017, 24.64059585, 0.37114147, -312.67463148, -0.01101987, -375.89188407, -0.13105479, -37.58918841, -0.38364608, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2626990, 33681461.06803645, 0.1125, 0.00189844, 0.00058594, 14033942.11168186, 0.00152995)
    ops.section('Aggregator', 2626991, 2626990, 'Mz')
    ops.section('Aggregator', 2626992, 2626991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2626, 2626991, 0.39589646446, 2626992, 0.39589646446, 2626990)
    # Create element
    ops.element('forceBeamColumn', 2626, 626, 636, 2626, 2626)

    # Create geometric transformation
    ops.geomTransf('Linear', 2726, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2726990, 206.17567273, 0.0099964, 246.63869026, 0.10854214, 24.66386903, 0.36145501, -206.17567273, -0.0099964, -246.63869026, -0.10854214, -24.66386903, -0.36145501, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2726991, 206.17567273, 0.0099964, 246.63869026, 0.10991845, 24.66386903, 0.36283132, -206.17567273, -0.0099964, -246.63869026, -0.10991845, -24.66386903, -0.36283132, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2726990, 34908818.9933704, 0.1125, 0.00189844, 0.00058594, 14545341.24723767, 0.00152995)
    ops.section('Aggregator', 2726991, 2726990, 'Mz')
    ops.section('Aggregator', 2726992, 2726991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2726, 2726991, 0.39539308273, 2726992, 0.39539308273, 2726990)
    # Create element
    ops.element('forceBeamColumn', 2726, 726, 736, 2726, 2726)

    # Create geometric transformation
    ops.geomTransf('Linear', 2036, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2036990, 205.11324001, 0.0098131, 249.28853644, 0.08096536, 24.92885364, 0.29627441, -205.11324001, -0.0098131, -249.28853644, -0.08096536, -24.92885364, -0.29627441, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2036991, 138.40873967, 0.00926812, 168.21786902, 0.07935668, 16.8217869, 0.29731659, -204.79188456, -0.0099309, -248.89797057, -0.08671436, -24.88979706, -0.30467427, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2036990, 30524040.75975097, 0.1125, 0.00189844, 0.00058594, 12718350.3165629, 0.00152995)
    ops.section('Aggregator', 2036991, 2036990, 'Mz')
    ops.section('Aggregator', 2036992, 2036991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2036, 2036991, 0.45879996744, 2036992, 0.45879996744, 2036990)
    # Create element
    ops.element('forceBeamColumn', 2036, 36, 46, 2036, 2036)

    # Create geometric transformation
    ops.geomTransf('Linear', 2136, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2136990, 211.03246137, 0.00978829, 254.03511687, 0.08444029, 25.40351169, 0.29940278, -321.47122261, -0.01082409, -386.97828323, -0.09336153, -38.69782832, -0.30832401, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2136991, 142.13468575, 0.00929397, 171.09785515, 0.08194046, 17.10978551, 0.29690294, -320.7334256, -0.01095931, -386.09014333, -0.09895161, -38.60901433, -0.31391409, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2136990, 33334817.2518427, 0.1125, 0.00189844, 0.00058594, 13889507.18826779, 0.00152995)
    ops.section('Aggregator', 2136991, 2136990, 'Mz')
    ops.section('Aggregator', 2136992, 2136991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2136, 2136991, 0.46519744725, 2136992, 0.46519744725, 2136990)
    # Create element
    ops.element('forceBeamColumn', 2136, 136, 146, 2136, 2136)

    # Create geometric transformation
    ops.geomTransf('Linear', 2236, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2236990, 209.2258538, 0.01010109, 251.55154146, 0.0831154, 25.15515415, 0.29668671, -319.10705289, -0.01115302, -383.66133816, -0.09187977, -38.36613382, -0.30545108, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2236991, 141.01471484, 0.00959537, 169.54151814, 0.08072925, 16.95415181, 0.29430057, -318.70875075, -0.01128284, -383.18246083, -0.09744302, -38.31824608, -0.31101433, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2236990, 33656785.73846079, 0.1125, 0.00189844, 0.00058594, 14023660.72435866, 0.00152995)
    ops.section('Aggregator', 2236991, 2236990, 'Mz')
    ops.section('Aggregator', 2236992, 2236991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2236, 2236991, 0.46822767468000004, 2236992, 0.46822767468000004, 2236990)
    # Create element
    ops.element('forceBeamColumn', 2236, 236, 246, 2236, 2236)

    # Create geometric transformation
    ops.geomTransf('Linear', 2336, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2336990, 211.09918249, 0.00996903, 254.08425612, 0.08277508, 25.40842561, 0.29742693, -217.83293364, -0.0101278, -262.18916743, -0.08360565, -26.21891674, -0.29825749, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2336991, 142.34882709, 0.0093273, 171.33460875, 0.08249803, 17.13346088, 0.29714987, -321.25130759, -0.01099652, -386.66610904, -0.09962379, -38.6666109, -0.31427564, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2336990, 33367342.51800728, 0.1125, 0.00189844, 0.00058594, 13903059.38250303, 0.00152995)
    ops.section('Aggregator', 2336991, 2336990, 'Mz')
    ops.section('Aggregator', 2336992, 2336991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2336, 2336991, 0.46587067063000004, 2336992, 0.46587067063000004, 2336990)
    # Create element
    ops.element('forceBeamColumn', 2336, 336, 346, 2336, 2336)

    # Create geometric transformation
    ops.geomTransf('Linear', 2436, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2436990, 210.82438421, 0.01008328, 253.69817482, 0.08147702, 25.36981748, 0.29551697, -217.56148271, -0.010244, -261.80534706, -0.0822965, -26.18053471, -0.29633646, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2436991, 142.1309189, 0.00943924, 171.03502921, 0.08235686, 17.10350292, 0.29639681, -320.94407205, -0.01111957, -386.21208645, -0.09944027, -38.62120864, -0.31348022, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2436990, 33424964.05365477, 0.1125, 0.00189844, 0.00058594, 13927068.35568949, 0.00152995)
    ops.section('Aggregator', 2436991, 2436990, 'Mz')
    ops.section('Aggregator', 2436992, 2436991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2436, 2436991, 0.46720249115, 2436992, 0.46720249115, 2436990)
    # Create element
    ops.element('forceBeamColumn', 2436, 436, 446, 2436, 2436)

    # Create geometric transformation
    ops.geomTransf('Linear', 2536, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2536990, 210.63278627, 0.00978448, 253.58809017, 0.08630582, 25.35880902, 0.30141444, -320.87313909, -0.01082014, -386.31026048, -0.09542437, -38.63102605, -0.31053299, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2536991, 141.86806891, 0.0092902, 170.79987066, 0.08331482, 17.07998707, 0.29842343, -320.14629623, -0.01095523, -385.43518925, -0.10061677, -38.54351893, -0.31572538, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2536990, 33299093.21791074, 0.1125, 0.00189844, 0.00058594, 13874622.17412947, 0.00152995)
    ops.section('Aggregator', 2536991, 2536990, 'Mz')
    ops.section('Aggregator', 2536992, 2536991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2536, 2536991, 0.46488142346, 2536992, 0.46488142346, 2536990)
    # Create element
    ops.element('forceBeamColumn', 2536, 536, 546, 2536, 2536)

    # Create geometric transformation
    ops.geomTransf('Linear', 2636, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2636990, 208.26061069, 0.00989042, 251.20852067, 0.08472085, 25.12085207, 0.29995724, -317.40683437, -0.01094112, -382.86309181, -0.09367582, -38.28630918, -0.30891221, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2636991, 140.31211568, 0.00938865, 169.24755428, 0.08334441, 16.92475543, 0.2985808, -316.82576247, -0.01107644, -382.16219012, -0.10065458, -38.21621901, -0.31589097, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2636990, 32784898.72446055, 0.1125, 0.00189844, 0.00058594, 13660374.46852523, 0.00152995)
    ops.section('Aggregator', 2636991, 2636990, 'Mz')
    ops.section('Aggregator', 2636992, 2636991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2636, 2636991, 0.46460545226, 2636992, 0.46460545226, 2636990)
    # Create element
    ops.element('forceBeamColumn', 2636, 636, 646, 2636, 2636)

    # Create geometric transformation
    ops.geomTransf('Linear', 2736, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2736990, 209.6527434, 0.00988967, 250.74078032, 0.07317791, 25.07407803, 0.2869154, -209.6527434, -0.00988967, -250.74078032, -0.07317791, -25.07407803, -0.2869154, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2736991, 141.44604352, 0.0093725, 169.16683631, 0.07207162, 16.91668363, 0.28745201, -209.46111512, -0.00998937, -250.51159646, -0.07867755, -25.05115965, -0.29405794, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2736990, 34963239.94443515, 0.1125, 0.00189844, 0.00058594, 14568016.64351465, 0.00152995)
    ops.section('Aggregator', 2736991, 2736990, 'Mz')
    ops.section('Aggregator', 2736992, 2736991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2736, 2736991, 0.46429481436, 2736992, 0.46429481436, 2736990)
    # Create element
    ops.element('forceBeamColumn', 2736, 736, 746, 2736, 2736)

    # Create geometric transformation
    ops.geomTransf('Linear', 2046, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2046990, 143.64613759, 0.00941727, 172.02507968, 0.07157307, 17.20250797, 0.28503958, -212.66752461, -0.01004317, -254.68243337, -0.07813613, -25.46824334, -0.29160263, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2046991, 143.64613759, 0.00941727, 172.02507968, 0.07187189, 17.20250797, 0.28603026, -212.66752461, -0.01004317, -254.68243337, -0.07846349, -25.46824334, -0.29262186, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2046990, 34646424.87952992, 0.1125, 0.00189844, 0.00058594, 14436010.3664708, 0.00152995)
    ops.section('Aggregator', 2046991, 2046990, 'Mz')
    ops.section('Aggregator', 2046992, 2046991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2046, 2046991, 0.46694415170000003, 2046992, 0.46694415170000003, 2046990)
    # Create element
    ops.element('forceBeamColumn', 2046, 46, 56, 2046, 2046)

    # Create geometric transformation
    ops.geomTransf('Linear', 2146, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2146990, 140.63917029, 0.00941766, 169.2004774, 0.08383235, 16.92004774, 0.29867511, -317.67964199, -0.01108782, -382.19471129, -0.10122184, -38.21947113, -0.3160646, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2146991, 140.77888599, 0.00952307, 169.36856687, 0.08077462, 16.93685669, 0.29561738, -215.23410514, -0.01032016, -258.94431307, -0.08909795, -25.89443131, -0.30394071, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2146990, 33486292.68003235, 0.1125, 0.00189844, 0.00058594, 13952621.95001348, 0.00152995)
    ops.section('Aggregator', 2146991, 2146990, 'Mz')
    ops.section('Aggregator', 2146992, 2146991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2146, 2146991, 0.46545669517, 2146992, 0.46545669517, 2146990)
    # Create element
    ops.element('forceBeamColumn', 2146, 146, 156, 2146, 2146)

    # Create geometric transformation
    ops.geomTransf('Linear', 2246, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2246990, 139.50427108, 0.00925791, 168.05872891, 0.08329708, 16.80587289, 0.29969444, -314.9578919, -0.01091548, -379.42510693, -0.10059466, -37.94251069, -0.31699201, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2246991, 139.60388569, 0.00936601, 168.17873315, 0.08129511, 16.81787331, 0.29769247, -213.38937817, -0.01015672, -257.06702296, -0.08968363, -25.7067023, -0.30608099, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2246990, 33132296.31551937, 0.1125, 0.00189844, 0.00058594, 13805123.46479974, 0.00152995)
    ops.section('Aggregator', 2246991, 2246990, 'Mz')
    ops.section('Aggregator', 2246992, 2246991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2246, 2246991, 0.46211285818, 2246992, 0.46211285818, 2246990)
    # Create element
    ops.element('forceBeamColumn', 2246, 246, 256, 2246, 2246)

    # Create geometric transformation
    ops.geomTransf('Linear', 2346, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2346990, 139.59987765, 0.00934304, 168.52331991, 0.08326078, 16.85233199, 0.2991292, -315.18517618, -0.01102974, -380.48781397, -0.10056183, -38.0487814, -0.31643026, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2346991, 139.7183789, 0.00945244, 168.66637322, 0.08169699, 16.86663732, 0.29756541, -213.56283528, -0.0102567, -257.8105269, -0.09013238, -25.78105269, -0.3060008, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2346990, 32562237.2364218, 0.1125, 0.00189844, 0.00058594, 13567598.84850909, 0.00152995)
    ops.section('Aggregator', 2346991, 2346990, 'Mz')
    ops.section('Aggregator', 2346992, 2346991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2346, 2346991, 0.46324515324, 2346992, 0.46324515324, 2346990)
    # Create element
    ops.element('forceBeamColumn', 2346, 346, 356, 2346, 2346)

    # Create geometric transformation
    ops.geomTransf('Linear', 2446, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2446990, 133.90311279, 0.00975696, 161.61036705, 0.08373477, 16.16103671, 0.29987169, -302.81000608, -0.01146706, -365.46750268, -0.10107192, -36.54675027, -0.31720884, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2446991, 134.24627481, 0.00984248, 162.02453622, 0.08246139, 16.20245362, 0.29859831, -205.30503391, -0.01065903, -247.78678552, -0.09094862, -24.77867855, -0.30708554, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2446990, 32624334.81379082, 0.1125, 0.00189844, 0.00058594, 13593472.83907951, 0.00152995)
    ops.section('Aggregator', 2446991, 2446990, 'Mz')
    ops.section('Aggregator', 2446992, 2446991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2446, 2446991, 0.46266967893, 2446992, 0.46266967893, 2446990)
    # Create element
    ops.element('forceBeamColumn', 2446, 446, 456, 2446, 2446)

    # Create geometric transformation
    ops.geomTransf('Linear', 2546, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2546990, 136.52673062, 0.00968562, 164.68140611, 0.08489525, 16.46814061, 0.30012527, -308.71731302, -0.01139368, -372.38129828, -0.10249056, -37.23812983, -0.31772058, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2546991, 136.82033958, 0.00977877, 165.0355634, 0.08196616, 16.50355634, 0.29719618, -209.25362708, -0.01059412, -252.40611407, -0.0904066, -25.24061141, -0.30563663, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2546990, 32785122.54207423, 0.1125, 0.00189844, 0.00058594, 13660467.72586427, 0.00152995)
    ops.section('Aggregator', 2546991, 2546990, 'Mz')
    ops.section('Aggregator', 2546992, 2546991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2546, 2546991, 0.46461918945, 2546992, 0.46461918945, 2546990)
    # Create element
    ops.element('forceBeamColumn', 2546, 546, 556, 2546, 2546)

    # Create geometric transformation
    ops.geomTransf('Linear', 2646, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2646990, 139.59207568, 0.00941387, 166.39996424, 0.07907693, 16.63999642, 0.2942381, -315.67458422, -0.01101286, -376.29814778, -0.0953915, -37.62981478, -0.31055267, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2646991, 139.79080981, 0.00950657, 166.63686415, 0.07593268, 16.66368642, 0.29109385, -213.8410443, -0.01027143, -254.90803793, -0.08371408, -25.49080379, -0.29887525, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2646990, 35726480.84119301, 0.1125, 0.00189844, 0.00058594, 14886033.68383042, 0.00152995)
    ops.section('Aggregator', 2646991, 2646990, 'Mz')
    ops.section('Aggregator', 2646992, 2646991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2646, 2646991, 0.46476787551000004, 2646992, 0.46476787551000004, 2646990)
    # Create element
    ops.element('forceBeamColumn', 2646, 646, 656, 2646, 2646)

    # Create geometric transformation
    ops.geomTransf('Linear', 2746, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2746990, 139.02271466, 0.00933938, 167.41272203, 0.07624049, 16.7412722, 0.29312241, -205.84367583, -0.00997108, -247.87927762, -0.08326262, -24.78792776, -0.30014455, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2746991, 139.02271466, 0.00933938, 167.41272203, 0.07640222, 16.7412722, 0.29328414, -205.84367583, -0.00997108, -247.87927762, -0.0834398, -24.78792776, -0.30032172, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2746990, 33237816.49743187, 0.1125, 0.00189844, 0.00058594, 13849090.20726328, 0.00152995)
    ops.section('Aggregator', 2746991, 2746990, 'Mz')
    ops.section('Aggregator', 2746992, 2746991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2746, 2746991, 0.46108038182, 2746992, 0.46108038182, 2746990)
    # Create element
    ops.element('forceBeamColumn', 2746, 746, 756, 2746, 2746)

    # Create geometric transformation
    ops.geomTransf('Linear', 2007, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2007990, 77.29942039, 0.0089495, 93.54958142, 0.09277277, 9.35495814, 0.37165914, -139.18305129, -0.00977533, -168.44261085, -0.10606418, -16.84426109, -0.38495055, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2007991, 77.18134142, 0.00889637, 93.40667946, 0.08620214, 9.34066795, 0.30555565, -205.68103472, -0.01037969, -248.92003854, -0.10766423, -24.89200385, -0.32701774, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2007990, 31839783.06538494, 0.1125, 0.00189844, 0.00058594, 13266576.27724373, 0.00152995)
    ops.section('Aggregator', 2007991, 2007990, 'Mz')
    ops.section('Aggregator', 2007992, 2007991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2007, 2007991, 0.35856897364, 2007992, 0.35856897364, 2007990)
    # Create element
    ops.element('forceBeamColumn', 2007, 7, 17, 2007, 2007)

    # Create geometric transformation
    ops.geomTransf('Linear', 2107, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2107990, 90.07566956, 0.00896952, 108.50042373, 0.10659419, 10.85004237, 0.35071802, -204.66854422, -0.01018498, -246.5329859, -0.12843184, -24.65329859, -0.37255567, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2107991, 133.7046652, 0.00935912, 161.05362192, 0.10808731, 16.10536219, 0.35221115, -204.756295, -0.01011356, -246.63868588, -0.11927033, -24.66386859, -0.36339417, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2107990, 33163027.7760362, 0.1125, 0.00189844, 0.00058594, 13817928.24001508, 0.00152995)
    ops.section('Aggregator', 2107991, 2107990, 'Mz')
    ops.section('Aggregator', 2107992, 2107991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2107, 2107991, 0.40962817069, 2107992, 0.40962817069, 2107990)
    # Create element
    ops.element('forceBeamColumn', 2107, 107, 117, 2107, 2107)

    # Create geometric transformation
    ops.geomTransf('Linear', 2207, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2207990, 90.49360495, 0.00877597, 108.78307082, 0.10402165, 10.87830708, 0.34907508, -205.57370057, -0.00996484, -247.12175452, -0.12533018, -24.71217545, -0.37038361, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2207991, 134.40063978, 0.00915562, 161.56406106, 0.10674601, 16.15640611, 0.35179944, -205.75256146, -0.00989267, -247.33676458, -0.11779146, -24.73367646, -0.36284489, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2207990, 33697484.32857507, 0.1125, 0.00189844, 0.00058594, 14040618.47023961, 0.00152995)
    ops.section('Aggregator', 2207991, 2207990, 'Mz')
    ops.section('Aggregator', 2207992, 2207991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2207, 2207991, 0.40807427172000005, 2207992, 0.40807427172000005, 2207990)
    # Create element
    ops.element('forceBeamColumn', 2207, 207, 217, 2207, 2207)

    # Create geometric transformation
    ops.geomTransf('Linear', 2307, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2307990, 101.99873624, 0.00893579, 122.93907613, 0.12086479, 12.29390761, 0.40108468, -205.34023745, -0.01008971, -247.49658688, -0.14211689, -24.74965869, -0.42233678, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2307991, 101.99873624, 0.00893579, 122.93907613, 0.12183528, 12.29390761, 0.40205517, -205.34023745, -0.01008971, -247.49658688, -0.14326164, -24.74965869, -0.42348153, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2307990, 32994284.93777287, 0.1125, 0.00189844, 0.00058594, 13747618.72407203, 0.00152995)
    ops.section('Aggregator', 2307991, 2307990, 'Mz')
    ops.section('Aggregator', 2307992, 2307991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2307, 2307991, 0.35686260342000004, 2307992, 0.35686260342000004, 2307990)
    # Create element
    ops.element('forceBeamColumn', 2307, 307, 317, 2307, 2307)

    # Create geometric transformation
    ops.geomTransf('Linear', 2407, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2407990, 103.04299365, 0.00897401, 123.92339136, 0.11817027, 12.39233914, 0.39743154, -207.46007327, -0.01012291, -249.49931035, -0.13892664, -24.94993103, -0.41818792, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2407991, 103.04299365, 0.00897401, 123.92339136, 0.11944746, 12.39233914, 0.39870873, -207.46007327, -0.01012291, -249.49931035, -0.14043317, -24.94993103, -0.41969444, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2407990, 33582990.23379633, 0.1125, 0.00189844, 0.00058594, 13992912.59741514, 0.00152995)
    ops.section('Aggregator', 2407991, 2407990, 'Mz')
    ops.section('Aggregator', 2407992, 2407991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2407, 2407991, 0.35808759654, 2407992, 0.35808759654, 2407990)
    # Create element
    ops.element('forceBeamColumn', 2407, 407, 417, 2407, 2407)

    # Create geometric transformation
    ops.geomTransf('Linear', 2507, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2507990, 92.23686046, 0.00889829, 110.75708216, 0.10299275, 11.07570822, 0.34595083, -209.53163186, -0.01009979, -251.60344845, -0.12407072, -25.16034485, -0.36702881, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2507991, 137.00208562, 0.00928198, 164.51070838, 0.1050567, 16.45107084, 0.34801479, -209.72771022, -0.01002674, -251.83889735, -0.11591807, -25.18388974, -0.35887616, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2507990, 33978611.07812114, 0.1125, 0.00189844, 0.00058594, 14157754.61588381, 0.00152995)
    ops.section('Aggregator', 2507991, 2507990, 'Mz')
    ops.section('Aggregator', 2507992, 2507991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2507, 2507991, 0.4115936212, 2507992, 0.4115936212, 2507990)
    # Create element
    ops.element('forceBeamColumn', 2507, 507, 517, 2507, 2507)

    # Create geometric transformation
    ops.geomTransf('Linear', 2607, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2607990, 91.97735682, 0.00877665, 110.87056351, 0.10583526, 11.08705635, 0.34988106, -208.79467951, -0.00998875, -251.68350751, -0.12754998, -25.16835075, -0.37159578, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2607991, 136.6453633, 0.00916114, 164.71389214, 0.10752506, 16.47138921, 0.35157086, -209.06840714, -0.00991174, -252.01346194, -0.11866576, -25.20134619, -0.36271156, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2607990, 32969117.18679815, 0.1125, 0.00189844, 0.00058594, 13737132.16116589, 0.00152995)
    ops.section('Aggregator', 2607991, 2607990, 'Mz')
    ops.section('Aggregator', 2607992, 2607991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2607, 2607991, 0.40975915239, 2607992, 0.40975915239, 2607990)
    # Create element
    ops.element('forceBeamColumn', 2607, 607, 617, 2607, 2607)

    # Create geometric transformation
    ops.geomTransf('Linear', 2707, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2707990, 77.78909596, 0.00887025, 93.78897558, 0.09196707, 9.37889756, 0.37086702, -140.09114027, -0.00967748, -168.90547924, -0.10513184, -16.89054792, -0.3840318, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2707991, 77.68387031, 0.00881679, 93.66210682, 0.08493841, 9.36621068, 0.30480372, -207.0681206, -0.01026541, -249.65847289, -0.10605977, -24.96584729, -0.32592509, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2707990, 32907702.03893184, 0.1125, 0.00189844, 0.00058594, 13711542.5162216, 0.00152995)
    ops.section('Aggregator', 2707991, 2707990, 'Mz')
    ops.section('Aggregator', 2707992, 2707991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2707, 2707991, 0.35855150956, 2707992, 0.35855150956, 2707990)
    # Create element
    ops.element('forceBeamColumn', 2707, 707, 717, 2707, 2707)

    # Create geometric transformation
    ops.geomTransf('Linear', 2017, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2017990, 78.24657714, 0.00896537, 94.77162879, 0.0767781, 9.47716288, 0.29559642, -208.4871865, -0.0104702, -252.51801379, -0.09580834, -25.25180138, -0.31462665, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2017991, 103.71397178, 0.00928133, 125.61753361, 0.08337725, 12.56175336, 0.36092804, -141.05882114, -0.00982318, -170.84931664, -0.08960326, -17.08493166, -0.36715406, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2017990, 31601443.68762345, 0.1125, 0.00189844, 0.00058594, 13167268.20317644, 0.00152995)
    ops.section('Aggregator', 2017991, 2017990, 'Mz')
    ops.section('Aggregator', 2017992, 2017991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2017, 2017991, 0.36029440691000003, 2017992, 0.36029440691000003, 2017990)
    # Create element
    ops.element('forceBeamColumn', 2017, 17, 27, 2017, 2017)

    # Create geometric transformation
    ops.geomTransf('Linear', 2117, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2117990, 135.45035263, 0.00923458, 161.98952111, 0.10439521, 16.19895211, 0.34828438, -207.43162975, -0.00996163, -248.07429228, -0.11517401, -24.80742923, -0.35906318, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2117991, 135.45035263, 0.00923458, 161.98952111, 0.1036872, 16.19895211, 0.34757637, -207.43162975, -0.00996163, -248.07429228, -0.11439121, -24.80742923, -0.35828038, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2117990, 34972881.82609151, 0.1125, 0.00189844, 0.00058594, 14572034.09420479, 0.00152995)
    ops.section('Aggregator', 2117991, 2117990, 'Mz')
    ops.section('Aggregator', 2117992, 2117991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2117, 2117991, 0.41002230636000003, 2117992, 0.41002230636000003, 2117990)
    # Create element
    ops.element('forceBeamColumn', 2117, 117, 127, 2117, 2117)

    # Create geometric transformation
    ops.geomTransf('Linear', 2217, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2217990, 139.46704759, 0.00930427, 168.25142527, 0.10689661, 16.82514253, 0.34872062, -213.34322719, -0.01007074, -257.37478972, -0.11797168, -25.73747897, -0.35979569, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2217991, 139.46704759, 0.00930427, 168.25142527, 0.10773123, 16.82514253, 0.34955524, -213.34322719, -0.01007074, -257.37478972, -0.11889446, -25.73747897, -0.36071847, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2217990, 32746785.25844603, 0.1125, 0.00189844, 0.00058594, 13644493.85768585, 0.00152995)
    ops.section('Aggregator', 2217991, 2217990, 'Mz')
    ops.section('Aggregator', 2217992, 2217991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2217, 2217991, 0.4135238683, 2217992, 0.4135238683, 2217990)
    # Create element
    ops.element('forceBeamColumn', 2217, 217, 227, 2217, 2217)

    # Create geometric transformation
    ops.geomTransf('Linear', 2317, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2317990, 100.50654292, 0.00913172, 120.74307189, 0.11913687, 12.07430719, 0.39898593, -202.49791045, -0.01028006, -243.26993097, -0.14003795, -24.3269931, -0.41988701, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2317991, 100.50654292, 0.00913172, 120.74307189, 0.11996322, 12.07430719, 0.39981227, -202.49791045, -0.01028006, -243.26993097, -0.14101267, -24.3269931, -0.42086173, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2317990, 33860734.85466072, 0.1125, 0.00189844, 0.00058594, 14108639.5227753, 0.00152995)
    ops.section('Aggregator', 2317991, 2317990, 'Mz')
    ops.section('Aggregator', 2317992, 2317991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2317, 2317991, 0.35733549111, 2317992, 0.35733549111, 2317990)
    # Create element
    ops.element('forceBeamColumn', 2317, 317, 327, 2317, 2317)

    # Create geometric transformation
    ops.geomTransf('Linear', 2417, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2417990, 103.49169109, 0.00903148, 124.13135185, 0.11605069, 12.41313518, 0.39459673, -208.42583031, -0.0101735, -249.99282362, -0.13640928, -24.99928236, -0.41495532, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2417991, 103.49169109, 0.00903148, 124.13135185, 0.11731314, 12.41313518, 0.39585918, -208.42583031, -0.0101735, -249.99282362, -0.13789842, -24.99928236, -0.41644446, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2417990, 34262761.09598312, 0.1125, 0.00189844, 0.00058594, 14276150.45665963, 0.00152995)
    ops.section('Aggregator', 2417991, 2417990, 'Mz')
    ops.section('Aggregator', 2417992, 2417991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2417, 2417991, 0.35900707593, 2417992, 0.35900707593, 2417990)
    # Create element
    ops.element('forceBeamColumn', 2417, 417, 427, 2417, 2417)

    # Create geometric transformation
    ops.geomTransf('Linear', 2517, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2517990, 135.17309244, 0.00939676, 163.29296137, 0.10805936, 16.32929614, 0.35132712, -206.94018542, -0.0101669, -249.9896621, -0.11925116, -24.99896621, -0.36251891, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2517991, 135.17309244, 0.00939676, 163.29296137, 0.10803154, 16.32929614, 0.3512993, -206.94018542, -0.0101669, -249.9896621, -0.1192204, -24.99896621, -0.36248816, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2517990, 32365777.51815652, 0.1125, 0.00189844, 0.00058594, 13485740.63256522, 0.00152995)
    ops.section('Aggregator', 2517991, 2517990, 'Mz')
    ops.section('Aggregator', 2517992, 2517991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2517, 2517991, 0.41106968865, 2517992, 0.41106968865, 2517990)
    # Create element
    ops.element('forceBeamColumn', 2517, 517, 527, 2517, 2517)

    # Create geometric transformation
    ops.geomTransf('Linear', 2617, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2617990, 133.81267328, 0.00934446, 160.40795554, 0.10403062, 16.04079555, 0.34805895, -204.972454, -0.01008195, -245.71074982, -0.11476973, -24.57107498, -0.35879806, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2617991, 133.81267328, 0.00934446, 160.40795554, 0.10401075, 16.04079555, 0.34803908, -204.972454, -0.01008195, -245.71074982, -0.11474776, -24.57107498, -0.35877609, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2617990, 34403847.16358948, 0.1125, 0.00189844, 0.00058594, 14334936.31816229, 0.00152995)
    ops.section('Aggregator', 2617991, 2617990, 'Mz')
    ops.section('Aggregator', 2617992, 2617991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2617, 2617991, 0.40978848236, 2617992, 0.40978848236, 2617990)
    # Create element
    ops.element('forceBeamColumn', 2617, 617, 627, 2617, 2617)

    # Create geometric transformation
    ops.geomTransf('Linear', 2717, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2717990, 76.21337294, 0.00874828, 91.91861363, 0.07706335, 9.19186136, 0.30209339, -203.16579227, -0.01018229, -245.03203628, -0.0961526, -24.50320363, -0.32118264, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2717991, 101.02247081, 0.0090473, 121.84010633, 0.08334566, 12.18401063, 0.3639626, -137.42918386, -0.00956538, -165.7491273, -0.08956344, -16.57491273, -0.37018037, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2717990, 32819759.63991064, 0.1125, 0.00189844, 0.00058594, 13674899.84996277, 0.00152995)
    ops.section('Aggregator', 2717991, 2717990, 'Mz')
    ops.section('Aggregator', 2717992, 2717991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2717, 2717991, 0.35635768257, 2717992, 0.35635768257, 2717990)
    # Create element
    ops.element('forceBeamColumn', 2717, 717, 727, 2717, 2717)

    # Create geometric transformation
    ops.geomTransf('Linear', 2027, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2027990, 103.38443234, 0.00905559, 124.57693507, 0.08786022, 12.45769351, 0.35414859, -140.6215457, -0.00957451, -169.44718631, -0.09442452, -16.94471863, -0.36071289, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2027991, 103.38443234, 0.00905559, 124.57693507, 0.08850536, 12.45769351, 0.359994, -140.6215457, -0.00957451, -169.44718631, -0.09511915, -16.94471863, -0.36660779, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2027990, 33064621.99282331, 0.1125, 0.00189844, 0.00058594, 13776925.83034305, 0.00152995)
    ops.section('Aggregator', 2027991, 2027990, 'Mz')
    ops.section('Aggregator', 2027992, 2027991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2027, 2027991, 0.29035181746, 2027992, 0.29035181746, 2027990)
    # Create element
    ops.element('forceBeamColumn', 2027, 27, 37, 2027, 2027)

    # Create geometric transformation
    ops.geomTransf('Linear', 2127, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2127990, 137.18008491, 0.00923738, 164.48054743, 0.0961093, 16.44805474, 0.38739128, -209.99441321, -0.00997515, -251.78578993, -0.10602328, -25.17857899, -0.39730526, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2127991, 137.18008491, 0.00923738, 164.48054743, 0.09635944, 16.44805474, 0.38764142, -209.99441321, -0.00997515, -251.78578993, -0.10629984, -25.17857899, -0.39758182, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2127990, 34349922.06012194, 0.1125, 0.00189844, 0.00058594, 14312467.52505081, 0.00152995)
    ops.section('Aggregator', 2127991, 2127990, 'Mz')
    ops.section('Aggregator', 2127992, 2127991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2127, 2127991, 0.34330993941000004, 2127992, 0.34330993941000004, 2127990)
    # Create element
    ops.element('forceBeamColumn', 2127, 127, 137, 2127, 2127)

    # Create geometric transformation
    ops.geomTransf('Linear', 2227, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2227990, 135.86377977, 0.00927231, 163.57276895, 0.09786987, 16.35727689, 0.38988471, -207.97714316, -0.01002366, -250.39342525, -0.10797972, -25.03934253, -0.39999456, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2227991, 135.86377977, 0.00927231, 163.57276895, 0.09829311, 16.35727689, 0.39030795, -207.97714316, -0.01002366, -250.39342525, -0.10844767, -25.03934253, -0.40046251, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2227990, 33296377.57944445, 0.1125, 0.00189844, 0.00058594, 13873490.65810186, 0.00152995)
    ops.section('Aggregator', 2227991, 2227990, 'Mz')
    ops.section('Aggregator', 2227992, 2227991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2227, 2227991, 0.34244834809, 2227992, 0.34244834809, 2227990)
    # Create element
    ops.element('forceBeamColumn', 2227, 227, 237, 2227, 2227)

    # Create geometric transformation
    ops.geomTransf('Linear', 2327, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2327990, 101.93223551, 0.00916303, 123.16433469, 0.11516167, 12.31643347, 0.459265, -205.25680717, -0.01035186, -248.01102388, -0.13538382, -24.80110239, -0.47948715, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2327991, 101.93223551, 0.00916303, 123.16433469, 0.11511687, 12.31643347, 0.45922021, -205.25680717, -0.01035186, -248.01102388, -0.13533097, -24.80110239, -0.47943431, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2327990, 32302659.92676003, 0.1125, 0.00189844, 0.00058594, 13459441.63615001, 0.00152995)
    ops.section('Aggregator', 2327991, 2327990, 'Mz')
    ops.section('Aggregator', 2327992, 2327991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2327, 2327991, 0.29061037704000003, 2327992, 0.29061037704000003, 2327990)
    # Create element
    ops.element('forceBeamColumn', 2327, 327, 337, 2327, 2327)

    # Create geometric transformation
    ops.geomTransf('Linear', 2427, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2427990, 103.17838211, 0.00916052, 124.58052857, 0.11312364, 12.45805286, 0.45578028, -207.73674842, -0.01034911, -250.82728953, -0.13298005, -25.08272895, -0.47563668, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2427991, 103.17838211, 0.00916052, 124.58052857, 0.11364477, 12.45805286, 0.45654244, -207.73674842, -0.01034911, -250.82728953, -0.13359476, -25.08272895, -0.47649242, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2427990, 32506303.54526448, 0.1125, 0.00189844, 0.00058594, 13544293.1438602, 0.00152995)
    ops.section('Aggregator', 2427991, 2427990, 'Mz')
    ops.section('Aggregator', 2427992, 2427991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2427, 2427991, 0.29163220028000003, 2427992, 0.29163220028000003, 2427990)
    # Create element
    ops.element('forceBeamColumn', 2427, 427, 437, 2427, 2427)

    # Create geometric transformation
    ops.geomTransf('Linear', 2527, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2527990, 131.87611399, 0.00935723, 158.43789474, 0.09852994, 15.84378947, 0.39244953, -202.01948266, -0.01009927, -242.70916513, -0.10869123, -24.27091651, -0.40261082, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2527991, 131.87611399, 0.00935723, 158.43789474, 0.09857341, 15.84378947, 0.392493, -202.01948266, -0.01009927, -242.70916513, -0.10873929, -24.27091651, -0.40265888, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2527990, 33845977.36274056, 0.1125, 0.00189844, 0.00058594, 14102490.56780857, 0.00152995)
    ops.section('Aggregator', 2527991, 2527990, 'Mz')
    ops.section('Aggregator', 2527992, 2527991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2527, 2527991, 0.34022911171, 2527992, 0.34022911171, 2527990)
    # Create element
    ops.element('forceBeamColumn', 2527, 527, 537, 2527, 2527)

    # Create geometric transformation
    ops.geomTransf('Linear', 2627, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2627990, 134.03248295, 0.00915104, 162.06284958, 0.10249523, 16.20628496, 0.39712254, -205.10402779, -0.0099087, -247.99766796, -0.11311277, -24.7997668, -0.40774007, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2627991, 134.03248295, 0.00915104, 162.06284958, 0.10148485, 16.20628496, 0.394682, -205.10402779, -0.0099087, -247.99766796, -0.11199566, -24.7997668, -0.40519281, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2627990, 32103963.14440565, 0.1125, 0.00189844, 0.00058594, 13376651.31016902, 0.00152995)
    ops.section('Aggregator', 2627991, 2627990, 'Mz')
    ops.section('Aggregator', 2627992, 2627991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2627, 2627991, 0.33941185266, 2627992, 0.33941185266, 2627990)
    # Create element
    ops.element('forceBeamColumn', 2627, 627, 637, 2627, 2627)

    # Create geometric transformation
    ops.geomTransf('Linear', 2727, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2727990, 102.22602151, 0.00894176, 123.42608952, 0.09071389, 12.34260895, 0.36237001, -139.02832663, -0.00945863, -167.86061351, -0.09750379, -16.78606135, -0.36915992, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2727991, 102.22602151, 0.00894176, 123.42608952, 0.09074126, 12.34260895, 0.36261311, -139.02832663, -0.00945863, -167.86061351, -0.09753326, -16.78606135, -0.36940512, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2727990, 32516632.54575614, 0.1125, 0.00189844, 0.00058594, 13548596.89406506, 0.00152995)
    ops.section('Aggregator', 2727991, 2727990, 'Mz')
    ops.section('Aggregator', 2727992, 2727991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2727, 2727991, 0.28839707107, 2727992, 0.28839707107, 2727990)
    # Create element
    ops.element('forceBeamColumn', 2727, 727, 737, 2727, 2727)

    # Create geometric transformation
    ops.geomTransf('Linear', 2037, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2037990, 103.52876026, 0.00911629, 124.27960326, 0.08860195, 12.42796033, 0.36683121, -140.85076751, -0.00963046, -169.0822672, -0.09521374, -16.90822672, -0.373443, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2037991, 78.10017292, 0.00881817, 93.75422327, 0.08161074, 9.37542233, 0.29972861, -208.253867, -0.01023982, -249.99534335, -0.10184478, -24.99953433, -0.31996266, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2037990, 34053308.79865776, 0.1125, 0.00189844, 0.00058594, 14188878.6661074, 0.00152995)
    ops.section('Aggregator', 2037991, 2037990, 'Mz')
    ops.section('Aggregator', 2037992, 2037991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2037, 2037991, 0.35910959579, 2037992, 0.35910959579, 2037990)
    # Create element
    ops.element('forceBeamColumn', 2037, 37, 47, 2037, 2037)

    # Create geometric transformation
    ops.geomTransf('Linear', 2137, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2137990, 138.78135206, 0.00924606, 166.8396315, 0.10603021, 16.68396315, 0.34843752, -212.35044126, -0.00999545, -255.28263591, -0.11700283, -25.52826359, -0.35941014, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2137991, 138.78135206, 0.00924606, 166.8396315, 0.10609012, 16.68396315, 0.34849743, -212.35044126, -0.00999545, -255.28263591, -0.11706907, -25.52826359, -0.35947638, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2137990, 33682770.03680911, 0.1125, 0.00189844, 0.00058594, 14034487.51533713, 0.00152995)
    ops.section('Aggregator', 2137991, 2137990, 'Mz')
    ops.section('Aggregator', 2137992, 2137991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2137, 2137991, 0.41252881602999997, 2137992, 0.41252881602999997, 2137990)
    # Create element
    ops.element('forceBeamColumn', 2137, 137, 147, 2137, 2137)

    # Create geometric transformation
    ops.geomTransf('Linear', 2237, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2237990, 137.5282193, 0.00919138, 165.59045933, 0.10853499, 16.55904593, 0.35193193, -210.42281072, -0.00994104, -253.35898376, -0.11977824, -25.33589838, -0.36317519, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2237991, 137.5282193, 0.00919138, 165.59045933, 0.10778365, 16.55904593, 0.3511806, -210.42281072, -0.00994104, -253.35898376, -0.11894754, -25.33589838, -0.36234449, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2237990, 33274193.42416103, 0.1125, 0.00189844, 0.00058594, 13864247.2600671, 0.00152995)
    ops.section('Aggregator', 2237991, 2237990, 'Mz')
    ops.section('Aggregator', 2237992, 2237991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2237, 2237991, 0.41085150137, 2237992, 0.41085150137, 2237990)
    # Create element
    ops.element('forceBeamColumn', 2237, 237, 247, 2237, 2237)

    # Create geometric transformation
    ops.geomTransf('Linear', 2337, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2337990, 101.40036627, 0.00925324, 121.61548134, 0.11566093, 12.16154813, 0.39413827, -204.32113755, -0.01040686, -245.0544747, -0.1359213, -24.50544747, -0.41439865, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2337991, 101.40036627, 0.00925324, 121.61548134, 0.11700104, 12.16154813, 0.39547839, -204.32113755, -0.01040686, -245.0544747, -0.13750205, -24.50544747, -0.41597939, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2337990, 34278034.55520701, 0.1125, 0.00189844, 0.00058594, 14282514.39800292, 0.00152995)
    ops.section('Aggregator', 2337991, 2337990, 'Mz')
    ops.section('Aggregator', 2337992, 2337991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2337, 2337991, 0.35909564115000003, 2337992, 0.35909564115000003, 2337990)
    # Create element
    ops.element('forceBeamColumn', 2337, 337, 347, 2337, 2337)

    # Create geometric transformation
    ops.geomTransf('Linear', 2437, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2437990, 102.2200685, 0.00899438, 123.04622187, 0.12170475, 12.30462219, 0.40136974, -205.83262286, -0.01014719, -247.76863245, -0.14309605, -24.77686324, -0.42276104, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2437991, 102.2200685, 0.00899438, 123.04622187, 0.12091882, 12.30462219, 0.40058382, -205.83262286, -0.01014719, -247.76863245, -0.142169, -24.77686324, -0.42183399, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2437990, 33342377.87650637, 0.1125, 0.00189844, 0.00058594, 13892657.44854432, 0.00152995)
    ops.section('Aggregator', 2437991, 2437990, 'Mz')
    ops.section('Aggregator', 2437992, 2437991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2437, 2437991, 0.35757067436, 2437992, 0.35757067436, 2437990)
    # Create element
    ops.element('forceBeamColumn', 2437, 437, 447, 2437, 2437)

    # Create geometric transformation
    ops.geomTransf('Linear', 2537, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2537990, 136.06376119, 0.00945425, 164.89656463, 0.11187671, 16.48965646, 0.35446841, -208.24704874, -0.01024299, -252.37596427, -0.12348425, -25.23759643, -0.36607595, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2537991, 136.06376119, 0.00945425, 164.89656463, 0.11058023, 16.48965646, 0.35317192, -208.24704874, -0.01024299, -252.37596427, -0.12205082, -25.23759643, -0.36464252, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2537990, 31422982.81397255, 0.1125, 0.00189844, 0.00058594, 13092909.50582189, 0.00152995)
    ops.section('Aggregator', 2537991, 2537990, 'Mz')
    ops.section('Aggregator', 2537992, 2537991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2537, 2537991, 0.41221526132999997, 2537992, 0.41221526132999997, 2537990)
    # Create element
    ops.element('forceBeamColumn', 2537, 537, 547, 2537, 2537)

    # Create geometric transformation
    ops.geomTransf('Linear', 2637, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2637990, 133.98801282, 0.00943683, 161.99986233, 0.11025076, 16.19998623, 0.35386242, -205.15709918, -0.01021073, -248.04772551, -0.12167355, -24.80477255, -0.36528521, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2637991, 133.98801282, 0.00943683, 161.99986233, 0.11111784, 16.19998623, 0.3547295, -205.15709918, -0.01021073, -248.04772551, -0.12263222, -24.80477255, -0.36624387, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2637990, 32120437.27240646, 0.1125, 0.00189844, 0.00058594, 13383515.53016936, 0.00152995)
    ops.section('Aggregator', 2637991, 2637990, 'Mz')
    ops.section('Aggregator', 2637992, 2637991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2637, 2637991, 0.41048938648, 2637992, 0.41048938648, 2637990)
    # Create element
    ops.element('forceBeamColumn', 2637, 637, 647, 2637, 2637)

    # Create geometric transformation
    ops.geomTransf('Linear', 2737, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2737990, 104.581252, 0.00911392, 125.9867461, 0.09092169, 12.59867461, 0.36885308, -142.24331664, -0.00963615, -171.35741134, -0.09771969, -17.13574113, -0.37565108, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2737991, 78.90161901, 0.00880647, 95.05105409, 0.08390448, 9.50510541, 0.30498603, -210.2671182, -0.0102557, -253.30419675, -0.10476191, -25.33041967, -0.32584347, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2737990, 33133875.25398125, 0.1125, 0.00189844, 0.00058594, 13805781.35582552, 0.00152995)
    ops.section('Aggregator', 2737991, 2737990, 'Mz')
    ops.section('Aggregator', 2737992, 2737991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2737, 2737991, 0.35980102431, 2737992, 0.35980102431, 2737990)
    # Create element
    ops.element('forceBeamColumn', 2737, 737, 747, 2737, 2737)

    # Create geometric transformation
    ops.geomTransf('Linear', 2047, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2047990, 77.05048872, 0.00885429, 93.13673437, 0.07612023, 9.31367344, 0.29528609, -205.35317391, -0.01032237, -248.22586242, -0.09497241, -24.82258624, -0.31413827, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2047991, 77.16632593, 0.00890685, 93.27675555, 0.0814342, 9.32767555, 0.35808989, -138.95297849, -0.00972449, -167.96294045, -0.09303757, -16.79629404, -0.36969326, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2047990, 32188959.91647541, 0.1125, 0.00189844, 0.00058594, 13412066.63186475, 0.00152995)
    ops.section('Aggregator', 2047991, 2047990, 'Mz')
    ops.section('Aggregator', 2047992, 2047991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2047, 2047991, 0.35810677232, 2047992, 0.35810677232, 2047990)
    # Create element
    ops.element('forceBeamColumn', 2047, 47, 57, 2047, 2047)

    # Create geometric transformation
    ops.geomTransf('Linear', 2147, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2147990, 133.52014378, 0.00935042, 161.43193133, 0.11056545, 16.14319313, 0.35495585, -204.4224757, -0.0101185, -247.15607791, -0.12202478, -24.71560779, -0.36641518, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2147991, 89.94466223, 0.00895549, 108.74719069, 0.10806282, 10.87471907, 0.35245322, -204.30569023, -0.01019349, -247.01487896, -0.1302362, -24.7014879, -0.3746266, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2147990, 32124466.7756358, 0.1125, 0.00189844, 0.00058594, 13385194.48984825, 0.00152995)
    ops.section('Aggregator', 2147991, 2147990, 'Mz')
    ops.section('Aggregator', 2147992, 2147991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2147, 2147991, 0.40918137484, 2147992, 0.40918137484, 2147990)
    # Create element
    ops.element('forceBeamColumn', 2147, 147, 157, 2147, 2147)

    # Create geometric transformation
    ops.geomTransf('Linear', 2247, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2247990, 135.84658667, 0.00925622, 163.46068862, 0.10786472, 16.34606886, 0.35159697, -207.95254143, -0.01000466, -250.22392137, -0.11902911, -25.02239214, -0.36276135, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2247991, 91.46645453, 0.00887108, 110.05922202, 0.10513078, 11.0059222, 0.34886302, -207.76472423, -0.01007844, -249.99792579, -0.126672, -24.99979258, -0.37040424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2247990, 33444326.93646751, 0.1125, 0.00189844, 0.00058594, 13935136.22352813, 0.00152995)
    ops.section('Aggregator', 2247991, 2247990, 'Mz')
    ops.section('Aggregator', 2247992, 2247991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2247, 2247991, 0.41028630073, 2247992, 0.41028630073, 2247990)
    # Create element
    ops.element('forceBeamColumn', 2247, 247, 257, 2247, 2247)

    # Create geometric transformation
    ops.geomTransf('Linear', 2347, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2347990, 102.14998571, 0.00910152, 121.83441578, 0.1147153, 12.18344158, 0.39355348, -205.8738266, -0.01021959, -245.54597062, -0.13479757, -24.55459706, -0.41363575, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2347991, 102.14998571, 0.00910152, 121.83441578, 0.11330091, 12.18344158, 0.39213909, -205.8738266, -0.01021959, -245.54597062, -0.13312922, -24.55459706, -0.4119674, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2347990, 35601619.4918951, 0.1125, 0.00189844, 0.00058594, 14834008.12162296, 0.00152995)
    ops.section('Aggregator', 2347991, 2347990, 'Mz')
    ops.section('Aggregator', 2347992, 2347991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2347, 2347991, 0.3586309432, 2347992, 0.3586309432, 2347990)
    # Create element
    ops.element('forceBeamColumn', 2347, 347, 357, 2347, 2347)

    # Create geometric transformation
    ops.geomTransf('Linear', 2447, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2447990, 104.67938986, 0.00895726, 126.19726795, 0.11973439, 12.6197268, 0.39816196, -210.59060401, -0.01012323, -253.87957379, -0.14079169, -25.38795738, -0.41921927, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2447991, 104.67938986, 0.00895726, 126.19726795, 0.12040859, 12.6197268, 0.39883617, -210.59060401, -0.01012323, -253.87957379, -0.14158696, -25.38795738, -0.42001454, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2447990, 32935570.20382217, 0.1125, 0.00189844, 0.00058594, 13723154.25159257, 0.00152995)
    ops.section('Aggregator', 2447991, 2447990, 'Mz')
    ops.section('Aggregator', 2447992, 2447991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2447, 2447991, 0.35915983002, 2447992, 0.35915983002, 2447990)
    # Create element
    ops.element('forceBeamColumn', 2447, 447, 457, 2447, 2447)

    # Create geometric transformation
    ops.geomTransf('Linear', 2547, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2547990, 134.87776768, 0.0093799, 162.64500527, 0.10897223, 16.26450053, 0.3524305, -206.51646214, -0.0101416, -249.03193204, -0.12025378, -24.9031932, -0.36371205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2547991, 90.84976879, 0.0089875, 109.55297806, 0.10723894, 10.95529781, 0.3506972, -206.39392121, -0.01021524, -248.88416365, -0.12922127, -24.88841637, -0.37267953, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2547990, 32865261.17600119, 0.1125, 0.00189844, 0.00058594, 13693858.82333383, 0.00152995)
    ops.section('Aggregator', 2547991, 2547990, 'Mz')
    ops.section('Aggregator', 2547992, 2547991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2547, 2547991, 0.41074801676, 2547992, 0.41074801676, 2547990)
    # Create element
    ops.element('forceBeamColumn', 2547, 547, 557, 2547, 2547)

    # Create geometric transformation
    ops.geomTransf('Linear', 2647, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2647990, 136.43289256, 0.00919631, 163.39172563, 0.1052493, 16.33917256, 0.34896306, -208.87180122, -0.00992695, -250.14439991, -0.11612594, -25.01443999, -0.35983969, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2647991, 91.84755222, 0.00881927, 109.9964222, 0.10224485, 10.99964222, 0.34595861, -208.67585396, -0.00999797, -249.90973391, -0.12315872, -24.99097339, -0.36687248, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2647990, 34639075.0068533, 0.1125, 0.00189844, 0.00058594, 14432947.91952221, 0.00152995)
    ops.section('Aggregator', 2647991, 2647990, 'Mz')
    ops.section('Aggregator', 2647992, 2647991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2647, 2647991, 0.41031741778999997, 2647992, 0.41031741778999997, 2647990)
    # Create element
    ops.element('forceBeamColumn', 2647, 647, 657, 2647, 2647)

    # Create geometric transformation
    ops.geomTransf('Linear', 2747, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2747990, 78.70578954, 0.00881653, 94.2559961, 0.07223515, 9.42559961, 0.29233994, -209.89155532, -0.0102271, -251.36063986, -0.09003552, -25.13606399, -0.3101403, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2747991, 78.80376351, 0.00886828, 94.37332717, 0.07688927, 9.43733272, 0.35129095, -141.96324611, -0.00965565, -170.01147246, -0.08779222, -17.00114725, -0.3621939, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2747990, 34643915.65648535, 0.1125, 0.00189844, 0.00058594, 14434964.8568689, 0.00152995)
    ops.section('Aggregator', 2747991, 2747990, 'Mz')
    ops.section('Aggregator', 2747992, 2747991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2747, 2747991, 0.35980102688, 2747992, 0.35980102688, 2747990)
    # Create element
    ops.element('forceBeamColumn', 2747, 747, 757, 2747, 2747)

    # Create geometric transformation
    ops.geomTransf('Linear', 2008, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2008990, 76.29120634, 0.00902024, 91.61189241, 0.06321944, 9.16118924, 0.28181762, -89.54267739, -0.00923616, -107.52450408, -0.06554736, -10.75245041, -0.28414554, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2008991, 76.19409123, 0.00899038, 91.49527478, 0.06371919, 9.14952748, 0.27977729, -132.62637659, -0.00967156, -159.26020737, -0.07196444, -15.92602074, -0.28802254, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2008990, 33972544.7848095, 0.1125, 0.00189844, 0.00058594, 14155226.99367063, 0.00152995)
    ops.section('Aggregator', 2008991, 2008990, 'Mz')
    ops.section('Aggregator', 2008992, 2008991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2008, 2008991, 0.35783460174, 2008992, 0.35783460174, 2008990)
    # Create element
    ops.element('forceBeamColumn', 2008, 8, 18, 2008, 2008)

    # Create geometric transformation
    ops.geomTransf('Linear', 2108, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2108990, 79.92993067, 0.0088038, 96.00622559, 0.07917106, 9.60062256, 0.35495133, -119.38594492, -0.00929008, -143.39802204, -0.08659197, -14.3398022, -0.36237225, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2108991, 79.91115774, 0.00877986, 95.98367686, 0.07951588, 9.59836769, 0.35333124, -144.69804738, -0.00951771, -173.80114386, -0.09077307, -17.38011439, -0.36458843, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2108990, 33906572.59311686, 0.1125, 0.00189844, 0.00058594, 14127738.58046536, 0.00152995)
    ops.section('Aggregator', 2108991, 2108990, 'Mz')
    ops.section('Aggregator', 2108992, 2108991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2108, 2108991, 0.36012586721, 2108992, 0.36012586721, 2108990)
    # Create element
    ops.element('forceBeamColumn', 2108, 108, 118, 2108, 2108)

    # Create geometric transformation
    ops.geomTransf('Linear', 2208, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2208990, 77.8391355, 0.00883589, 93.51274261, 0.08171643, 9.35127426, 0.36089267, -116.28255895, -0.00931966, -139.69709369, -0.08938252, -13.96970937, -0.36855876, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2208991, 77.80077693, 0.0088152, 93.4666602, 0.08164229, 9.34666602, 0.36019775, -140.92174919, -0.0095487, -169.29760556, -0.09320609, -16.92976056, -0.37176155, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2208990, 33857844.89559699, 0.1125, 0.00189844, 0.00058594, 14107435.37316541, 0.00152995)
    ops.section('Aggregator', 2208991, 2208990, 'Mz')
    ops.section('Aggregator', 2208992, 2208991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2208, 2208991, 0.35819667133000005, 2208992, 0.35819667133000005, 2208990)
    # Create element
    ops.element('forceBeamColumn', 2208, 208, 218, 2208, 2208)

    # Create geometric transformation
    ops.geomTransf('Linear', 2308, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2308990, 79.20150982, 0.00895707, 95.45949965, 0.08099314, 9.54594997, 0.35553796, -137.86440881, -0.00965817, -166.1643511, -0.09165035, -16.61643511, -0.36619517, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2308991, 79.20150982, 0.00895707, 95.45949965, 0.0819914, 9.54594997, 0.35918204, -137.86440881, -0.00965817, -166.1643511, -0.09278657, -16.61643511, -0.36997721, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2308990, 33000205.29778179, 0.1125, 0.00189844, 0.00058594, 13750085.54074241, 0.00152995)
    ops.section('Aggregator', 2308991, 2308990, 'Mz')
    ops.section('Aggregator', 2308992, 2308991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2308, 2308991, 0.36076254466, 2308992, 0.36076254466, 2308990)
    # Create element
    ops.element('forceBeamColumn', 2308, 308, 318, 2308, 2308)

    # Create geometric transformation
    ops.geomTransf('Linear', 2408, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2408990, 77.21572943, 0.00914035, 92.73703621, 0.07914486, 9.27370362, 0.35363472, -115.32545607, -0.00963318, -138.50728438, -0.08653657, -13.85072844, -0.36102643, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2408991, 77.16141089, 0.00912412, 92.67179898, 0.08013434, 9.2671799, 0.35788686, -139.73062337, -0.00987045, -167.81818904, -0.09144079, -16.7818189, -0.36919331, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2408990, 33931526.51820623, 0.1125, 0.00189844, 0.00058594, 14138136.0492526, 0.00152995)
    ops.section('Aggregator', 2408991, 2408990, 'Mz')
    ops.section('Aggregator', 2408992, 2408991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2408, 2408991, 0.36003274389, 2408992, 0.36003274389, 2408990)
    # Create element
    ops.element('forceBeamColumn', 2408, 408, 418, 2408, 2408)

    # Create geometric transformation
    ops.geomTransf('Linear', 2508, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2508990, 77.83526549, 0.00876426, 94.28595903, 0.08455485, 9.4285959, 0.36437909, -116.23078753, -0.00926485, -140.79647834, -0.09252454, -14.07964783, -0.37234879, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2508991, 77.80908405, 0.00873968, 94.25424408, 0.08536889, 9.42542441, 0.36523557, -140.84899112, -0.00950018, -170.61780573, -0.09752512, -17.06178057, -0.3773918, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2508990, 31561505.92560957, 0.1125, 0.00189844, 0.00058594, 13150627.46900399, 0.00152995)
    ops.section('Aggregator', 2508991, 2508990, 'Mz')
    ops.section('Aggregator', 2508992, 2508991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2508, 2508991, 0.35731299036, 2508992, 0.35731299036, 2508990)
    # Create element
    ops.element('forceBeamColumn', 2508, 508, 518, 2508, 2508)

    # Create geometric transformation
    ops.geomTransf('Linear', 2608, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2608990, 79.89373839, 0.00903921, 95.93877005, 0.07897086, 9.593877, 0.35435136, -119.35295353, -0.00953371, -143.32256563, -0.08635708, -14.33225656, -0.36173757, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2608991, 79.85603328, 0.0090178, 95.89349264, 0.07925445, 9.58934926, 0.35210583, -144.64536224, -0.00976758, -173.69443997, -0.0904493, -17.369444, -0.36330069, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2608990, 33970187.86600412, 0.1125, 0.00189844, 0.00058594, 14154244.94416838, 0.00152995)
    ops.section('Aggregator', 2608991, 2608990, 'Mz')
    ops.section('Aggregator', 2608992, 2608991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2608, 2608991, 0.3621308266, 2608992, 0.3621308266, 2608990)
    # Create element
    ops.element('forceBeamColumn', 2608, 608, 618, 2608, 2608)

    # Create geometric transformation
    ops.geomTransf('Linear', 2708, 1, 0, 0, '-jntOffset', 0.0, 0.175, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2708990, 77.5881241, 0.00885257, 93.21989817, 0.06377401, 9.32198982, 0.28413575, -91.07076738, -0.00906644, -109.41890605, -0.06612803, -10.9418906, -0.28648976, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2708991, 77.51610661, 0.00881515, 93.13337123, 0.06436893, 9.31333712, 0.28306248, -134.95540128, -0.00949375, -162.14503071, -0.07272562, -16.21450307, -0.29141918, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2708990, 33833911.55120338, 0.1125, 0.00189844, 0.00058594, 14097463.14633474, 0.00152995)
    ops.section('Aggregator', 2708991, 2708990, 'Mz')
    ops.section('Aggregator', 2708992, 2708991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2708, 2708991, 0.3578403978, 2708992, 0.3578403978, 2708990)
    # Create element
    ops.element('forceBeamColumn', 2708, 708, 718, 2708, 2708)

    # Create geometric transformation
    ops.geomTransf('Linear', 2018, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2018990, 79.45379921, 0.0087717, 94.77127847, 0.06104321, 9.47712785, 0.27887739, -138.35029197, -0.00943409, -165.02211572, -0.06893005, -16.50221157, -0.28676423, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2018991, 79.50194113, 0.008811, 94.82870143, 0.06068658, 9.48287014, 0.28219318, -93.32363879, -0.00902003, -111.31501134, -0.06291706, -11.13150113, -0.28442366, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2018990, 35585680.3853791, 0.1125, 0.00189844, 0.00058594, 14827366.82724129, 0.00152995)
    ops.section('Aggregator', 2018991, 2018990, 'Mz')
    ops.section('Aggregator', 2018992, 2018991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2018, 2018991, 0.35970547868, 2018992, 0.35970547868, 2018990)
    # Create element
    ops.element('forceBeamColumn', 2018, 18, 28, 2018, 2018)

    # Create geometric transformation
    ops.geomTransf('Linear', 2118, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2118990, 77.56388692, 0.00867148, 92.88013248, 0.08040727, 9.28801325, 0.3606768, -140.50446416, -0.00938641, -168.24934597, -0.09179022, -16.8249346, -0.37205975, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2118991, 77.56388692, 0.00867148, 92.88013248, 0.08076428, 9.28801325, 0.36103381, -140.50446416, -0.00938641, -168.24934597, -0.09220033, -16.8249346, -0.37246986, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2118990, 34665708.38394807, 0.1125, 0.00189844, 0.00058594, 14444045.15997836, 0.00152995)
    ops.section('Aggregator', 2118991, 2118990, 'Mz')
    ops.section('Aggregator', 2118992, 2118991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2118, 2118991, 0.3567993979, 2118992, 0.3567993979, 2118990)
    # Create element
    ops.element('forceBeamColumn', 2118, 118, 128, 2118, 2118)

    # Create geometric transformation
    ops.geomTransf('Linear', 2218, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2218990, 76.94068548, 0.00887239, 92.68961085, 0.08433593, 9.26896108, 0.36392334, -139.3488605, -0.00961549, -167.87206367, -0.09630141, -16.78720637, -0.37588882, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2218991, 76.94068548, 0.00887239, 92.68961085, 0.08386117, 9.26896108, 0.36344858, -139.3488605, -0.00961549, -167.87206367, -0.09575605, -16.78720637, -0.37534346, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2218990, 33131405.38309356, 0.1125, 0.00189844, 0.00058594, 13804752.24295565, 0.00152995)
    ops.section('Aggregator', 2218991, 2218990, 'Mz')
    ops.section('Aggregator', 2218992, 2218991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2218, 2218991, 0.35766989838, 2218992, 0.35766989838, 2218990)
    # Create element
    ops.element('forceBeamColumn', 2218, 218, 228, 2218, 2218)

    # Create geometric transformation
    ops.geomTransf('Linear', 2318, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2318990, 76.18230245, 0.00891722, 91.30879999, 0.07935711, 9.13088, 0.35628149, -132.62494977, -0.00958938, -158.95850641, -0.08976477, -15.89585064, -0.36668916, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2318991, 76.18230245, 0.00891722, 91.30879999, 0.07923698, 9.13088, 0.35504244, -132.62494977, -0.00958938, -158.95850641, -0.08962804, -15.89585064, -0.3654335, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2318990, 34443596.58599067, 0.1125, 0.00189844, 0.00058594, 14351498.57749611, 0.00152995)
    ops.section('Aggregator', 2318991, 2318990, 'Mz')
    ops.section('Aggregator', 2318992, 2318991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2318, 2318991, 0.35727495247, 2318992, 0.35727495247, 2318990)
    # Create element
    ops.element('forceBeamColumn', 2318, 318, 328, 2318, 2318)

    # Create geometric transformation
    ops.geomTransf('Linear', 2418, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2418990, 77.46837534, 0.00880479, 93.33149575, 0.08328233, 9.33314958, 0.36286534, -140.30064062, -0.00954632, -169.02986007, -0.09509963, -16.90298601, -0.37468263, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2418991, 77.50661858, 0.00882606, 93.37757002, 0.08195525, 9.337757, 0.3581333, -115.77505339, -0.0093149, -139.4821933, -0.08965091, -13.94821933, -0.36582896, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2418990, 33113560.69680008, 0.1125, 0.00189844, 0.00058594, 13797316.95700003, 0.00152995)
    ops.section('Aggregator', 2418991, 2418990, 'Mz')
    ops.section('Aggregator', 2418992, 2418991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2418, 2418991, 0.35767553592, 2418992, 0.35767553592, 2418990)
    # Create element
    ops.element('forceBeamColumn', 2418, 418, 428, 2418, 2418)

    # Create geometric transformation
    ops.geomTransf('Linear', 2518, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2518990, 77.57306043, 0.00876843, 93.41615436, 0.08177114, 9.34161544, 0.35963967, -140.48916839, -0.00950677, -169.18190115, -0.09336591, -16.91819011, -0.37123444, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2518991, 77.57306043, 0.00876843, 93.41615436, 0.08239287, 9.34161544, 0.36211927, -140.48916839, -0.00950677, -169.18190115, -0.09408009, -16.91819011, -0.3738065, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2518990, 33232668.49735495, 0.1125, 0.00189844, 0.00058594, 13846945.20723123, 0.00152995)
    ops.section('Aggregator', 2518991, 2518990, 'Mz')
    ops.section('Aggregator', 2518992, 2518991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2518, 2518991, 0.35749217538, 2518992, 0.35749217538, 2518990)
    # Create element
    ops.element('forceBeamColumn', 2518, 518, 528, 2518, 2518)

    # Create geometric transformation
    ops.geomTransf('Linear', 2618, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2618990, 77.7226484, 0.00849483, 93.40116768, 0.08083347, 9.34011677, 0.35898994, -140.71683258, -0.00921158, -169.10278721, -0.09230789, -16.91027872, -0.37046436, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2618991, 77.7226484, 0.00849483, 93.40116768, 0.08109604, 9.34011677, 0.36165334, -140.71683258, -0.00921158, -169.10278721, -0.0926095, -16.91027872, -0.3731668, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2618990, 33779896.87464856, 0.1125, 0.00189844, 0.00058594, 14074957.03110357, 0.00152995)
    ops.section('Aggregator', 2618991, 2618990, 'Mz')
    ops.section('Aggregator', 2618992, 2618991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2618, 2618991, 0.35533358681, 2618992, 0.35533358681, 2618990)
    # Create element
    ops.element('forceBeamColumn', 2618, 618, 628, 2618, 2618)

    # Create geometric transformation
    ops.geomTransf('Linear', 2718, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2718990, 77.1460703, 0.00893074, 92.95444122, 0.06563202, 9.29544412, 0.28585914, -134.29379748, -0.009623, -161.81258301, -0.07416097, -16.1812583, -0.29438809, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2718991, 77.23132611, 0.00896669, 93.0571672, 0.06498772, 9.30571672, 0.28656765, -90.64747814, -0.00918488, -109.22248724, -0.06738891, -10.92224872, -0.28896884, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2718990, 33080903.71231097, 0.1125, 0.00189844, 0.00058594, 13783709.88012957, 0.00152995)
    ops.section('Aggregator', 2718991, 2718990, 'Mz')
    ops.section('Aggregator', 2718992, 2718991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2718, 2718991, 0.35832573431, 2718992, 0.35832573431, 2718990)
    # Create element
    ops.element('forceBeamColumn', 2718, 718, 728, 2718, 2718)

    # Create geometric transformation
    ops.geomTransf('Linear', 2028, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2028990, 76.46946957, 0.00874128, 91.99781912, 0.07886391, 9.19978191, 0.35596603, -89.75591497, -0.00895341, -107.98228989, -0.08180853, -10.79822899, -0.35891065, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2028991, 76.46946957, 0.00874128, 91.99781912, 0.07826384, 9.19978191, 0.34977404, -89.75591497, -0.00895341, -107.98228989, -0.08118508, -10.79822899, -0.35269528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2028990, 33489819.69920382, 0.1125, 0.00189844, 0.00058594, 13954091.54133492, 0.00152995)
    ops.section('Aggregator', 2028991, 2028990, 'Mz')
    ops.section('Aggregator', 2028992, 2028991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2028, 2028991, 0.28766312476, 2028992, 0.28766312476, 2028990)
    # Create element
    ops.element('forceBeamColumn', 2028, 28, 38, 2028, 2028)

    # Create geometric transformation
    ops.geomTransf('Linear', 2128, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2128990, 77.4980484, 0.00884834, 93.5124282, 0.07812564, 9.35124282, 0.34511262, -140.34507255, -0.00959808, -169.34630989, -0.08917778, -16.93463099, -0.35616476, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2128991, 77.4980484, 0.00884834, 93.5124282, 0.07911012, 9.35124282, 0.35518499, -140.34507255, -0.00959808, -169.34630989, -0.09030868, -16.93463099, -0.36638354, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2128990, 32688429.03909855, 0.1125, 0.00189844, 0.00058594, 13620178.76629106, 0.00152995)
    ops.section('Aggregator', 2128991, 2128990, 'Mz')
    ops.section('Aggregator', 2128992, 2128991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2128, 2128991, 0.29003029017, 2128992, 0.29003029017, 2128990)
    # Create element
    ops.element('forceBeamColumn', 2128, 128, 138, 2128, 2128)

    # Create geometric transformation
    ops.geomTransf('Linear', 2228, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2228990, 77.06929198, 0.00871831, 92.83523053, 0.08024822, 9.28352305, 0.35651742, -139.57531524, -0.00945321, -168.12800836, -0.09162052, -16.81280084, -0.36788972, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2228991, 77.06929198, 0.00871831, 92.83523053, 0.07964052, 9.28352305, 0.3503746, -139.57531524, -0.00945321, -168.12800836, -0.09092245, -16.81280084, -0.36165652, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2228990, 33158378.67381808, 0.1125, 0.00189844, 0.00058594, 13815991.11409087, 0.00152995)
    ops.section('Aggregator', 2228991, 2228990, 'Mz')
    ops.section('Aggregator', 2228992, 2228991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2228, 2228991, 0.28851972073000004, 2228992, 0.28851972073000004, 2228990)
    # Create element
    ops.element('forceBeamColumn', 2228, 228, 238, 2228, 2228)

    # Create geometric transformation
    ops.geomTransf('Linear', 2328, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2328990, 78.08682028, 0.00897105, 94.20079278, 0.07719571, 9.42007928, 0.34205679, -135.92576465, -0.00967246, -163.97536413, -0.08732645, -16.39753641, -0.35218753, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2328991, 78.08682028, 0.00897105, 94.20079278, 0.07741876, 9.42007928, 0.34433844, -135.92576465, -0.00967246, -163.97536413, -0.08758033, -16.39753641, -0.35450001, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2328990, 32753360.74150903, 0.1125, 0.00189844, 0.00058594, 13647233.64229543, 0.00152995)
    ops.section('Aggregator', 2328991, 2328990, 'Mz')
    ops.section('Aggregator', 2328992, 2328991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2328, 2328991, 0.29165367383, 2328992, 0.29165367383, 2328990)
    # Create element
    ops.element('forceBeamColumn', 2328, 328, 338, 2328, 2328)

    # Create geometric transformation
    ops.geomTransf('Linear', 2428, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.25, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2428990, 77.51306514, 0.00875987, 93.36103397, 0.07904184, 9.3361034, 0.35348229, -115.78327083, -0.00924565, -139.4557919, -0.08645385, -13.94557919, -0.36089431, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2428991, 77.51306514, 0.00875987, 93.36103397, 0.07878881, 9.3361034, 0.35089138, -115.78327083, -0.00924565, -139.4557919, -0.08617589, -13.94557919, -0.35827846, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2428990, 33183542.22255109, 0.1125, 0.00189844, 0.00058594, 13826475.92606295, 0.00152995)
    ops.section('Aggregator', 2428991, 2428990, 'Mz')
    ops.section('Aggregator', 2428992, 2428991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2428, 2428991, 0.28912757419, 2428992, 0.28912757419, 2428990)
    # Create element
    ops.element('forceBeamColumn', 2428, 428, 438, 2428, 2428)

    # Create geometric transformation
    ops.geomTransf('Linear', 2528, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2528990, 78.87943193, 0.00878925, 94.77066501, 0.07563859, 9.4770665, 0.34129474, -142.85592631, -0.0095252, -171.63601215, -0.08631589, -17.16360121, -0.35197204, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2528991, 78.87943193, 0.00878925, 94.77066501, 0.07558084, 9.4770665, 0.34069288, -142.85592631, -0.0095252, -171.63601215, -0.08624955, -17.16360121, -0.35136159, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2528990, 33835811.17767935, 0.1125, 0.00189844, 0.00058594, 14098254.65736639, 0.00152995)
    ops.section('Aggregator', 2528991, 2528990, 'Mz')
    ops.section('Aggregator', 2528992, 2528991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2528, 2528991, 0.29112095496, 2528992, 0.29112095496, 2528990)
    # Create element
    ops.element('forceBeamColumn', 2528, 528, 538, 2528, 2528)

    # Create geometric transformation
    ops.geomTransf('Linear', 2628, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.35, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2628990, 76.73085017, 0.00873704, 92.6034452, 0.07974379, 9.26034452, 0.35140624, -138.95244997, -0.00947874, -167.69624677, -0.09104509, -16.76962468, -0.36270755, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2628991, 76.73085017, 0.00873704, 92.6034452, 0.08011047, 9.26034452, 0.35511244, -138.95244997, -0.00947874, -167.69624677, -0.0914663, -16.76962468, -0.36646827, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2628990, 32638085.15020617, 0.1125, 0.00189844, 0.00058594, 13599202.14591924, 0.00152995)
    ops.section('Aggregator', 2628991, 2628990, 'Mz')
    ops.section('Aggregator', 2628992, 2628991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2628, 2628991, 0.28826102328000003, 2628992, 0.28826102328000003, 2628990)
    # Create element
    ops.element('forceBeamColumn', 2628, 628, 638, 2628, 2628)

    # Create geometric transformation
    ops.geomTransf('Linear', 2728, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2728990, 80.1398295, 0.00884701, 95.95523837, 0.07439371, 9.59552384, 0.34470822, -94.06501256, -0.0090596, -112.62852391, -0.07716047, -11.26285239, -0.34747499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2728991, 80.1398295, 0.00884701, 95.95523837, 0.07418931, 9.59552384, 0.34250862, -94.06501256, -0.0090596, -112.62852391, -0.07694811, -11.26285239, -0.34526742, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2728990, 34689663.93968502, 0.1125, 0.00189844, 0.00058594, 14454026.64153542, 0.00152995)
    ops.section('Aggregator', 2728991, 2728990, 'Mz')
    ops.section('Aggregator', 2728992, 2728991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2728, 2728991, 0.29257823893, 2728992, 0.29257823893, 2728990)
    # Create element
    ops.element('forceBeamColumn', 2728, 728, 738, 2728, 2728)

    # Create geometric transformation
    ops.geomTransf('Linear', 2038, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2038990, 78.37602821, 0.00898577, 94.61516174, 0.0655845, 9.46151617, 0.28626246, -91.98848493, -0.00920666, -111.04805358, -0.06801089, -11.10480536, -0.28868885, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2038991, 78.30394751, 0.00894561, 94.52814627, 0.06661563, 9.45281463, 0.28945013, -136.29724988, -0.00964887, -164.53738008, -0.07528947, -16.45373801, -0.29812396, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2038990, 32560613.0544524, 0.1125, 0.00189844, 0.00058594, 13566922.10602184, 0.00152995)
    ops.section('Aggregator', 2038991, 2038990, 'Mz')
    ops.section('Aggregator', 2038992, 2038991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2038, 2038991, 0.35965492274000005, 2038992, 0.35965492274000005, 2038990)
    # Create element
    ops.element('forceBeamColumn', 2038, 38, 48, 2038, 2038)

    # Create geometric transformation
    ops.geomTransf('Linear', 2138, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2138990, 78.77958742, 0.0088859, 94.95478009, 0.0827148, 9.49547801, 0.36068189, -142.66412741, -0.00963798, -171.95622988, -0.09444616, -17.19562299, -0.37241325, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2138991, 78.77958742, 0.0088859, 94.95478009, 0.0827381, 9.49547801, 0.36070519, -142.66412741, -0.00963798, -171.95622988, -0.09447292, -17.19562299, -0.37244002, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2138990, 32989291.98261952, 0.1125, 0.00189844, 0.00058594, 13745538.32609147, 0.00152995)
    ops.section('Aggregator', 2138991, 2138990, 'Mz')
    ops.section('Aggregator', 2138992, 2138991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2138, 2138991, 0.35975480980999996, 2138992, 0.35975480980999996, 2138990)
    # Create element
    ops.element('forceBeamColumn', 2138, 138, 148, 2138, 2138)

    # Create geometric transformation
    ops.geomTransf('Linear', 2238, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2238990, 75.23829046, 0.00906777, 90.3237274, 0.0801142, 9.03237274, 0.35601917, -136.19245644, -0.00980262, -163.49933303, -0.09141455, -16.3499333, -0.36731952, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2238991, 75.23829046, 0.00906777, 90.3237274, 0.08082658, 9.03237274, 0.36063076, -136.19245644, -0.00980262, -163.49933303, -0.09223288, -16.3499333, -0.37203706, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2238990, 34039297.43171103, 0.1125, 0.00189844, 0.00058594, 14183040.59654626, 0.00152995)
    ops.section('Aggregator', 2238991, 2238990, 'Mz')
    ops.section('Aggregator', 2238992, 2238991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2238, 2238991, 0.35739280221, 2238992, 0.35739280221, 2238990)
    # Create element
    ops.element('forceBeamColumn', 2238, 238, 248, 2238, 2238)

    # Create geometric transformation
    ops.geomTransf('Linear', 2338, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.275, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2338990, 76.2020562, 0.0089613, 92.07960877, 0.08429312, 9.20796088, 0.36405057, -132.62502251, -0.00966199, -160.25893256, -0.09540542, -16.02589326, -0.37516287, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2338991, 76.2020562, 0.0089613, 92.07960877, 0.08421005, 9.20796088, 0.3639675, -132.62502251, -0.00966199, -160.25893256, -0.09531086, -16.02589326, -0.37506832, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2338990, 32287290.60224377, 0.1125, 0.00189844, 0.00058594, 13453037.75093491, 0.00152995)
    ops.section('Aggregator', 2338991, 2338990, 'Mz')
    ops.section('Aggregator', 2338992, 2338991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2338, 2338991, 0.35745249657, 2338992, 0.35745249657, 2338990)
    # Create element
    ops.element('forceBeamColumn', 2338, 338, 348, 2338, 2338)

    # Create geometric transformation
    ops.geomTransf('Linear', 2438, 1, 0, 0, '-jntOffset', 0.0, 0.25, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2438990, 77.28264947, 0.00882301, 93.10772616, 0.08227585, 9.31077262, 0.36206685, -115.44092089, -0.00931127, -139.07962166, -0.09000283, -13.90796217, -0.36979383, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2438991, 77.24308307, 0.00880204, 93.0600578, 0.08308377, 9.30600578, 0.36287477, -139.89421557, -0.00954266, -168.54018856, -0.09487102, -16.85401886, -0.37466202, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2438990, 33113597.81660513, 0.1125, 0.00189844, 0.00058594, 13797332.42358547, 0.00152995)
    ops.section('Aggregator', 2438991, 2438990, 'Mz')
    ops.section('Aggregator', 2438992, 2438991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2438, 2438991, 0.35740963698, 2438992, 0.35740963698, 2438990)
    # Create element
    ops.element('forceBeamColumn', 2438, 438, 448, 2438, 2438)

    # Create geometric transformation
    ops.geomTransf('Linear', 2538, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2538990, 77.8174946, 0.0087998, 93.61653783, 0.08198527, 9.36165378, 0.36127767, -140.940268, -0.00953718, -169.55493104, -0.09360626, -16.9554931, -0.37289866, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2538991, 77.8174946, 0.0087998, 93.61653783, 0.08154091, 9.36165378, 0.35819909, -140.940268, -0.00953718, -169.55493104, -0.09309582, -16.9554931, -0.369754, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2538990, 33498354.29915057, 0.1125, 0.00189844, 0.00058594, 13957647.62464607, 0.00152995)
    ops.section('Aggregator', 2538991, 2538990, 'Mz')
    ops.section('Aggregator', 2538992, 2538991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2538, 2538991, 0.35804769633, 2538992, 0.35804769633, 2538990)
    # Create element
    ops.element('forceBeamColumn', 2538, 538, 548, 2538, 2538)

    # Create geometric transformation
    ops.geomTransf('Linear', 2638, 1, 0, 0, '-jntOffset', 0.0, 0.35, 0.0, 0.0, -0.375, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2638990, 77.85504851, 0.00869297, 93.31243179, 0.08028262, 9.33124318, 0.36018207, -141.02363252, -0.00941268, -169.02254051, -0.09164862, -16.90225405, -0.37154807, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2638991, 77.85504851, 0.00869297, 93.31243179, 0.07987041, 9.33124318, 0.35705234, -141.02363252, -0.00941268, -169.02254051, -0.09117511, -16.90225405, -0.36835703, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2638990, 34446887.29155669, 0.1125, 0.00189844, 0.00058594, 14352869.70481529, 0.00152995)
    ops.section('Aggregator', 2638991, 2638990, 'Mz')
    ops.section('Aggregator', 2638992, 2638991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2638, 2638991, 0.35727115312, 2638992, 0.35727115312, 2638990)
    # Create element
    ops.element('forceBeamColumn', 2638, 638, 648, 2638, 2638)

    # Create geometric transformation
    ops.geomTransf('Linear', 2738, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.325, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2738990, 77.79375996, 0.00903787, 93.52009382, 0.06440213, 9.35200938, 0.28604151, -91.31024433, -0.00925587, -109.76899204, -0.06677753, -10.9768992, -0.28841691, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2738991, 77.70572354, 0.0090033, 93.41426048, 0.06445931, 9.34142605, 0.27937049, -135.27856188, -0.00969351, -162.62568882, -0.0728141, -16.26256888, -0.28772528, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2738990, 33687502.8075505, 0.1125, 0.00189844, 0.00058594, 14036459.50314604, 0.00152995)
    ops.section('Aggregator', 2738991, 2738990, 'Mz')
    ops.section('Aggregator', 2738992, 2738991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2738, 2738991, 0.35959818313, 2738992, 0.35959818313, 2738990)
    # Create element
    ops.element('forceBeamColumn', 2738, 738, 748, 2738, 2738)

    # Create geometric transformation
    ops.geomTransf('Linear', 2048, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2048990, 76.45930656, 0.0089465, 91.84027173, 0.06436873, 9.18402717, 0.28399741, -133.10131225, -0.00962735, -159.87668781, -0.07270949, -15.98766878, -0.29233817, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2048991, 76.55261746, 0.00897821, 91.95235356, 0.06373803, 9.19523536, 0.28473967, -89.85208824, -0.00919371, -107.92721738, -0.06608737, -10.79272174, -0.28708902, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2048990, 33899026.6514497, 0.1125, 0.00189844, 0.00058594, 14124594.43810404, 0.00152995)
    ops.section('Aggregator', 2048991, 2048990, 'Mz')
    ops.section('Aggregator', 2048992, 2048991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2048, 2048991, 0.35777252519, 2048992, 0.35777252519, 2048990)
    # Create element
    ops.element('forceBeamColumn', 2048, 48, 58, 2048, 2048)

    # Create geometric transformation
    ops.geomTransf('Linear', 2148, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2148990, 78.78762194, 0.00897013, 94.66130477, 0.08211755, 9.46613048, 0.35946066, -142.7107983, -0.00971555, -171.46335983, -0.09374091, -17.14633598, -0.37108402, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2148991, 78.8290171, 0.00899066, 94.71103999, 0.08060488, 9.471104, 0.35613892, -117.76133281, -0.00948235, -141.48721766, -0.08815409, -14.14872177, -0.36368813, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2148990, 33833249.54619718, 0.1125, 0.00189844, 0.00058594, 14097187.31091549, 0.00152995)
    ops.section('Aggregator', 2148991, 2148990, 'Mz')
    ops.section('Aggregator', 2148992, 2148991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2148, 2148991, 0.36056421108000003, 2148992, 0.36056421108000003, 2148990)
    # Create element
    ops.element('forceBeamColumn', 2148, 148, 158, 2148, 2148)

    # Create geometric transformation
    ops.geomTransf('Linear', 2248, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2248990, 77.67318918, 0.00883625, 93.48350239, 0.08075782, 9.34835024, 0.35581931, -140.67980528, -0.00957661, -169.31506293, -0.09219382, -16.93150629, -0.36725531, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2248991, 77.71265556, 0.00885714, 93.53100213, 0.08044726, 9.35310021, 0.35788225, -116.08709502, -0.00934531, -139.71652691, -0.08799057, -13.97165269, -0.36542557, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2248990, 33384017.44348448, 0.1125, 0.00189844, 0.00058594, 13910007.26811853, 0.00152995)
    ops.section('Aggregator', 2248991, 2248990, 'Mz')
    ops.section('Aggregator', 2248992, 2248991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2248, 2248991, 0.35818916548, 2248992, 0.35818916548, 2248990)
    # Create element
    ops.element('forceBeamColumn', 2248, 248, 258, 2248, 2248)

    # Create geometric transformation
    ops.geomTransf('Linear', 2348, 1, 0, 0, '-jntOffset', 0.0, 0.275, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2348990, 77.37672495, 0.00875379, 92.98191745, 0.08243337, 9.29819175, 0.36241419, -134.70930337, -0.00942942, -161.87722257, -0.09329226, -16.18772226, -0.37327308, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2348991, 77.37672495, 0.00875379, 92.98191745, 0.08143055, 9.29819175, 0.35719303, -134.70930337, -0.00942942, -161.87722257, -0.09215085, -16.18772226, -0.36791332, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2348990, 33789704.97614706, 0.1125, 0.00189844, 0.00058594, 14079043.74006128, 0.00152995)
    ops.section('Aggregator', 2348991, 2348990, 'Mz')
    ops.section('Aggregator', 2348992, 2348991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2348, 2348991, 0.35716731917, 2348992, 0.35716731917, 2348990)
    # Create element
    ops.element('forceBeamColumn', 2348, 348, 358, 2348, 2348)

    # Create geometric transformation
    ops.geomTransf('Linear', 2448, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2448990, 77.65597278, 0.00892186, 93.38327873, 0.08154757, 9.33832787, 0.3601699, -140.6560612, -0.00966378, -169.14248444, -0.09308986, -16.91424844, -0.37171219, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2448991, 77.70079188, 0.00894153, 93.43717484, 0.08148533, 9.34371748, 0.36010766, -116.07164059, -0.00943093, -139.57909454, -0.08912387, -13.95790945, -0.3677462, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2448990, 33607334.57885375, 0.1125, 0.00189844, 0.00058594, 14003056.0745224, 0.00152995)
    ops.section('Aggregator', 2448991, 2448990, 'Mz')
    ops.section('Aggregator', 2448992, 2448991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2448, 2448991, 0.35890877884000005, 2448992, 0.35890877884000005, 2448990)
    # Create element
    ops.element('forceBeamColumn', 2448, 448, 458, 2448, 2448)

    # Create geometric transformation
    ops.geomTransf('Linear', 2548, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2548990, 78.89110296, 0.00877211, 95.00546893, 0.08355638, 9.50054689, 0.36217062, -142.85144068, -0.0095151, -172.03040139, -0.09542075, -17.20304014, -0.37403499, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2548991, 78.91617307, 0.0087956, 95.03565988, 0.08211004, 9.50356599, 0.35976825, -117.87017704, -0.00928517, -141.94644291, -0.08982469, -14.19464429, -0.3674829, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2548990, 33226808.86104904, 0.1125, 0.00189844, 0.00058594, 13844503.69210377, 0.00152995)
    ops.section('Aggregator', 2548991, 2548990, 'Mz')
    ops.section('Aggregator', 2548992, 2548991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2548, 2548991, 0.35891919793, 2548992, 0.35891919793, 2548990)
    # Create element
    ops.element('forceBeamColumn', 2548, 548, 558, 2548, 2548)

    # Create geometric transformation
    ops.geomTransf('Linear', 2648, 1, 0, 0, '-jntOffset', 0.0, 0.375, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2648990, 79.4026256, 0.00882369, 95.57808952, 0.08189993, 9.55780895, 0.3597418, -143.78099892, -0.00956961, -173.07126912, -0.0935132, -17.30712691, -0.37135507, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2648991, 79.42783308, 0.00884723, 95.60843212, 0.08183898, 9.56084321, 0.35968085, -118.63628974, -0.00933876, -142.80421881, -0.08952379, -14.28042188, -0.36736566, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2648990, 33347649.9474703, 0.1125, 0.00189844, 0.00058594, 13894854.14477929, 0.00152995)
    ops.section('Aggregator', 2648991, 2648990, 'Mz')
    ops.section('Aggregator', 2648992, 2648991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2648, 2648991, 0.35991695125, 2648992, 0.35991695125, 2648990)
    # Create element
    ops.element('forceBeamColumn', 2648, 648, 658, 2648, 2648)

    # Create geometric transformation
    ops.geomTransf('Linear', 2748, 1, 0, 0, '-jntOffset', 0.0, 0.325, 0.0, 0.0, -0.175, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2748990, 76.61807732, 0.00889171, 92.58340365, 0.06812038, 9.25834036, 0.2927131, -133.35803348, -0.00959034, -161.14657369, -0.07700501, -16.11465737, -0.30159773, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2748991, 76.70250486, 0.00892897, 92.68542381, 0.06732281, 9.26854238, 0.29215856, -90.02271387, -0.00914869, -108.78123737, -0.06981798, -10.87812374, -0.29465373, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2748990, 32283920.74574948, 0.1125, 0.00189844, 0.00058594, 13451633.64406229, 0.00152995)
    ops.section('Aggregator', 2748991, 2748990, 'Mz')
    ops.section('Aggregator', 2748992, 2748991, 'Mz')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2748, 2748991, 0.35734360597000003, 2748992, 0.35734360597000003, 2748990)
    # Create element
    ops.element('forceBeamColumn', 2748, 748, 758, 2748, 2748)
