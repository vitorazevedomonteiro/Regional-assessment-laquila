import openseespy.opensees as ops


def add_beams() -> None:
    """Add components of all beams to ops domain
    """
    # Create geometric transformation
    ops.geomTransf('Linear', 1001, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1001990, 31.07899346, 0.00987771, 37.8851638, 0.05589071, 3.78851638, 0.29150403, -31.07899346, -0.00987771, -37.8851638, -0.05589071, -3.78851638, -0.29150403, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1001991, 31.03393052, 0.00984957, 37.83023227, 0.0566823, 3.78302323, 0.29477518, -45.9922262, -0.01034843, -56.0643325, -0.06165464, -5.60643325, -0.29974753, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1001990, 29514820.12562636, 0.07, 0.00071458, 0.00023333, 12297841.71901098, 0.00060032)
    ops.section('Aggregator', 1001991, 1001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1001992, 1001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1001, 1001991, 0.32794480327000003, 1001992, 0.32794480327000003, 1001990)
    # Create element
    ops.element('forceBeamColumn', 1001, 1, 101, 1001, 1001)

    # Create geometric transformation
    ops.geomTransf('Linear', 1101, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1101990, 31.63016565, 0.00965172, 38.48663948, 0.06753407, 3.84866395, 0.36408007, -46.90978214, -0.01014281, -57.0784198, -0.07355411, -5.70784198, -0.37010011, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1101991, 31.63016565, 0.00965172, 38.48663948, 0.06826684, 3.84866395, 0.3737955, -46.90978214, -0.01014281, -57.0784198, -0.07435687, -5.70784198, -0.37988553, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1101990, 30143345.33710517, 0.07, 0.00071458, 0.00023333, 12559727.22379382, 0.00060032)
    ops.section('Aggregator', 1101991, 1101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1101992, 1101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1101, 1101991, 0.26017228945, 1101992, 0.26017228945, 1101990)
    # Create element
    ops.element('forceBeamColumn', 1101, 101, 201, 1101, 1101)

    # Create geometric transformation
    ops.geomTransf('Linear', 1201, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1201990, 31.21845109, 0.00950563, 38.07091295, 0.05807277, 3.8070913, 0.29883239, -46.29942769, -0.00999794, -56.46216964, -0.06320425, -5.64621696, -0.30396387, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1201991, 31.25887638, 0.00954273, 38.12021161, 0.05750162, 3.81202116, 0.29862805, -31.25887638, -0.00954273, -38.12021161, -0.05750162, -3.81202116, -0.29862805, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1201990, 29368086.04237188, 0.07, 0.00071458, 0.00023333, 12236702.51765495, 0.00060032)
    ops.section('Aggregator', 1201991, 1201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1201992, 1201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1201, 1201991, 0.32630573931, 1201992, 0.32630573931, 1201990)
    # Create element
    ops.element('forceBeamColumn', 1201, 201, 301, 1201, 1201)

    # Create geometric transformation
    ops.geomTransf('Linear', 1011, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1011990, 53.45694953, 0.0101479, 65.31518063, 0.07873144, 6.53151806, 0.29376239, -81.67917678, -0.01107495, -99.79787909, -0.08690291, -9.97978791, -0.30193386, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1011991, 53.45694953, 0.0101479, 65.31518063, 0.07879466, 6.53151806, 0.29429609, -81.67917678, -0.01107495, -99.79787909, -0.08697281, -9.97978791, -0.30247424, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1011990, 28668857.4272938, 0.07, 0.00071458, 0.00023333, 11945357.26137242, 0.00060032)
    ops.section('Aggregator', 1011991, 1011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1011992, 1011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1011, 1011991, 0.36756135016, 1011992, 0.36756135016, 1011990)
    # Create element
    ops.element('forceBeamColumn', 1011, 11, 111, 1011, 1011)

    # Create geometric transformation
    ops.geomTransf('Linear', 1111, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1111990, 52.4534051, 0.01057591, 63.78669471, 0.09238948, 6.37866947, 0.35740878, -80.13820358, -0.0114924, -97.45317995, -0.10194787, -9.745318, -0.36696717, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1111991, 52.4534051, 0.01057591, 63.78669471, 0.09130536, 6.37866947, 0.34806999, -80.13820358, -0.0114924, -97.45317995, -0.10074924, -9.745318, -0.35751386, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1111990, 30336728.89118892, 0.07, 0.00071458, 0.00023333, 12640303.70466205, 0.00060032)
    ops.section('Aggregator', 1111991, 1111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1111992, 1111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1111, 1111991, 0.30123752621, 1111992, 0.30123752621, 1111990)
    # Create element
    ops.element('forceBeamColumn', 1111, 111, 211, 1111, 1111)

    # Create geometric transformation
    ops.geomTransf('Linear', 1211, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1211990, 52.99670445, 0.01032198, 64.87116336, 0.07878968, 6.48711634, 0.29133837, -80.97426738, -0.01127192, -99.11738819, -0.08697181, -9.91173882, -0.2995205, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1211991, 52.99670445, 0.01032198, 64.87116336, 0.07907516, 6.48711634, 0.29373203, -80.97426738, -0.01127192, -99.11738819, -0.08728744, -9.91173882, -0.30194431, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1211990, 27959825.4989416, 0.07, 0.00071458, 0.00023333, 11649927.29122567, 0.00060032)
    ops.section('Aggregator', 1211991, 1211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1211992, 1211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1211, 1211991, 0.36798676419, 1211992, 0.36798676419, 1211990)
    # Create element
    ops.element('forceBeamColumn', 1211, 211, 311, 1211, 1211)

    # Create geometric transformation
    ops.geomTransf('Linear', 1021, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1021990, 31.10398316, 0.00984662, 38.07482889, 0.05809607, 3.80748289, 0.29656408, -31.10398316, -0.00984662, -38.07482889, -0.05809607, -3.80748289, -0.29656408, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1021991, 31.05725832, 0.00981226, 38.01763235, 0.05863888, 3.80176323, 0.29634239, -46.03601125, -0.0103284, -56.3533372, -0.06381897, -5.63533372, -0.30152248, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1021990, 27942193.34156752, 0.07, 0.00071458, 0.00023333, 11642580.55898647, 0.00060032)
    ops.section('Aggregator', 1021991, 1021990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1021992, 1021991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1021, 1021991, 0.32764013731, 1021992, 0.32764013731, 1021990)
    # Create element
    ops.element('forceBeamColumn', 1021, 21, 121, 1021, 1021)

    # Create geometric transformation
    ops.geomTransf('Linear', 1121, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1121990, 31.33046106, 0.009474, 38.19969633, 0.07281784, 3.81996963, 0.38347404, -46.46858384, -0.0099654, -56.65686783, -0.07935987, -5.66568678, -0.39001608, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1121991, 31.33046106, 0.009474, 38.19969633, 0.07200123, 3.81996963, 0.37324144, -46.46858384, -0.0099654, -56.65686783, -0.07846527, -5.66568678, -0.37970547, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1121990, 29440815.2721719, 0.07, 0.00071458, 0.00023333, 12267006.36340496, 0.00060032)
    ops.section('Aggregator', 1121991, 1121990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1121992, 1121991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1121, 1121991, 0.258362971, 1121992, 0.258362971, 1121990)
    # Create element
    ops.element('forceBeamColumn', 1121, 121, 221, 1121, 1121)

    # Create geometric transformation
    ops.geomTransf('Linear', 1221, 0, -1, 0, '-jntOffset', 0.125, 0.0, 0.0, -0.125, 0.0, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 1221990, 30.73491409, 0.00985123, 37.64112807, 0.06107378, 3.76411281, 0.30599938, -45.54491693, -0.0103683, -55.77897652, -0.06648366, -5.57789765, -0.31140926, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 1221991, 30.78234819, 0.00988288, 37.69922074, 0.06030838, 3.76992207, 0.30382175, -30.78234819, -0.00988288, -37.69922074, -0.06030838, -3.76992207, -0.30382175, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 1221990, 27748148.388981, 0.07, 0.00071458, 0.00023333, 11561728.49540875, 0.00060032)
    ops.section('Aggregator', 1221991, 1221990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 1221992, 1221991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 1221, 1221991, 0.32711163293, 1221992, 0.32711163293, 1221990)
    # Create element
    ops.element('forceBeamColumn', 1221, 221, 321, 1221, 1221)

    # Create geometric transformation
    ops.geomTransf('Linear', 2001, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2001990, 35.83250161, 0.00791305, 43.76066445, 0.0986298, 4.37606645, 0.40602155, -145.22429013, -0.01024963, -177.3560635, -0.13646984, -17.73560635, -0.44386159, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2001991, 53.24814402, 0.00820514, 65.02962558, 0.1001989, 6.50296256, 0.40759066, -145.3531475, -0.01017344, -177.51343135, -0.12701014, -17.75134313, -0.4344019, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2001990, 28844117.41574328, 0.08, 0.00106667, 0.00026667, 12018382.2565597, 0.00073242)
    ops.section('Aggregator', 2001991, 2001990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2001992, 2001991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2001, 2001991, 0.32531776803999995, 2001992, 0.32531776803999995, 2001990)
    # Create element
    ops.element('forceBeamColumn', 2001, 1, 11, 2001, 2001)

    # Create geometric transformation
    ops.geomTransf('Linear', 2101, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2101990, 80.08185893, 0.00644088, 97.95741203, 0.07999121, 9.7957412, 0.33021496, -188.03181358, -0.00744865, -230.00352495, -0.09735775, -23.0003525, -0.34758149, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2101991, 118.82070909, 0.00664536, 145.3433938, 0.08340028, 14.53433938, 0.33200822, -277.58737155, -0.00796078, -339.54931733, -0.10178723, -33.95493173, -0.35039517, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2101990, 28232703.92307172, 0.125, 0.00260417, 0.00065104, 11763626.63461322, 0.00178813)
    ops.section('Aggregator', 2101991, 2101990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2101992, 2101991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2101, 2101991, 0.36740095577, 2101992, 0.36740095577, 2101990)
    # Create element
    ops.element('forceBeamColumn', 2101, 101, 111, 2101, 2101)

    # Create geometric transformation
    ops.geomTransf('Linear', 2201, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2201990, 80.81838531, 0.00632964, 98.15120618, 0.07429938, 9.81512062, 0.31709612, -189.87477688, -0.00727824, -230.59651962, -0.09036553, -23.05965196, -0.33316227, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2201991, 120.0034636, 0.00652434, 145.74016361, 0.0778442, 14.57401636, 0.32222036, -280.45618042, -0.00775944, -340.60458252, -0.09494197, -34.06045825, -0.33931814, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2201990, 30764345.08517599, 0.125, 0.00260417, 0.00065104, 12818477.11882333, 0.00178813)
    ops.section('Aggregator', 2201991, 2201990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2201992, 2201991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2201, 2201991, 0.36713177725999996, 2201992, 0.36713177725999996, 2201990)
    # Create element
    ops.element('forceBeamColumn', 2201, 201, 211, 2201, 2201)

    # Create geometric transformation
    ops.geomTransf('Linear', 2301, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2301990, 35.44984224, 0.00802877, 43.11127812, 0.09534769, 4.31112781, 0.4026742, -143.74855278, -0.01030629, -174.81555479, -0.13179889, -17.48155548, -0.4391254, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2301991, 52.59887504, 0.00831641, 63.96656762, 0.09696597, 6.39665676, 0.40429247, -143.79250782, -0.0102378, -174.86900941, -0.1228272, -17.48690094, -0.43015371, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2301990, 30321355.80345242, 0.08, 0.00106667, 0.00026667, 12633898.25143851, 0.00073242)
    ops.section('Aggregator', 2301991, 2301990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2301992, 2301991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2301, 2301991, 0.3253868371, 2301992, 0.3253868371, 2301990)
    # Create element
    ops.element('forceBeamColumn', 2301, 301, 311, 2301, 2301)

    # Create geometric transformation
    ops.geomTransf('Linear', 2011, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2011990, 53.231303, 0.00881755, 65.07387513, 0.09754642, 6.50738751, 0.40108639, -145.4444863, -0.01090564, -177.80207897, -0.12359576, -17.7802079, -0.42713573, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2011991, 35.95081709, 0.00850774, 43.94893325, 0.09692287, 4.39489332, 0.40046284, -145.46296726, -0.01097974, -177.82467145, -0.13399757, -17.78246715, -0.43753754, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2011990, 28467740.69158626, 0.08, 0.00106667, 0.00026667, 11861558.62149427, 0.00073242)
    ops.section('Aggregator', 2011991, 2011990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2011992, 2011991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2011, 2011991, 0.32944590371, 2011992, 0.32944590371, 2011990)
    # Create element
    ops.element('forceBeamColumn', 2011, 11, 21, 2011, 2011)

    # Create geometric transformation
    ops.geomTransf('Linear', 2111, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2111990, 119.77907483, 0.0067062, 146.11822553, 0.08201547, 14.61182255, 0.33184482, -280.01674519, -0.0080045, -341.59180128, -0.10006376, -34.15918013, -0.34989311, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2111991, 80.75182513, 0.00650015, 98.5089709, 0.07761922, 9.85089709, 0.32051289, -189.68850969, -0.00749536, -231.40058879, -0.09443244, -23.14005888, -0.33732611, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2111990, 29251342.5356373, 0.125, 0.00260417, 0.00065104, 12188059.38984888, 0.00178813)
    ops.section('Aggregator', 2111991, 2111990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2111992, 2111991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2111, 2111991, 0.36898493142, 2111992, 0.36898493142, 2111990)
    # Create element
    ops.element('forceBeamColumn', 2111, 111, 121, 2111, 2111)

    # Create geometric transformation
    ops.geomTransf('Linear', 2211, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2211990, 119.46248335, 0.00671553, 146.1199549, 0.08340399, 14.61199549, 0.33332636, -279.14957173, -0.0080422, -341.44043963, -0.1017874, -34.14404396, -0.35170977, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2211991, 80.53462161, 0.00650799, 98.50553034, 0.07933264, 9.85055303, 0.32553741, -189.1113551, -0.0075242, -231.31063331, -0.09654622, -23.13106333, -0.34275098, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2211990, 28255341.88537145, 0.125, 0.00260417, 0.00065104, 11773059.11890477, 0.00178813)
    ops.section('Aggregator', 2211991, 2211990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2211992, 2211991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2211, 2211991, 0.36872244525000003, 2211992, 0.36872244525000003, 2211990)
    # Create element
    ops.element('forceBeamColumn', 2211, 211, 221, 2211, 2211)

    # Create geometric transformation
    ops.geomTransf('Linear', 2311, 1, 0, 0, '-jntOffset', 0.0, 0.125, 0.0, 0.0, -0.125, 0.0)
    # Create uniaxial materials
    ops.uniaxialMaterial('Hysteretic', 2311990, 54.09698844, 0.00855956, 66.23215393, 0.0993143, 6.62321539, 0.40343798, -147.69806294, -0.01064057, -180.83004473, -0.12590365, -18.08300447, -0.43002732, 0.8, 0.2, 0.0, 0.0, 0.85)
    ops.uniaxialMaterial('Hysteretic', 2311991, 36.43641573, 0.0082524, 44.60991942, 0.09776171, 4.46099194, 0.40188538, -147.60679998, -0.01072102, -180.71830945, -0.13526124, -18.07183094, -0.43938492, 0.8, 0.2, 0.0, 0.0, 0.85)
    # Create element sections
    ops.section('Elastic', 2311990, 27873891.96220495, 0.08, 0.00106667, 0.00026667, 11614121.65091873, 0.00073242)
    ops.section('Aggregator', 2311991, 2311990, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    ops.section('Aggregator', 2311992, 2311991, 'Mz', 99999, 'Vy', 99999, 'My', 99999, 'Vz', 99999, 'P', 99999, 'T')
    # Create integration scheme
    ops.beamIntegration('HingeRadau', 2311, 2311991, 0.32881359533, 2311992, 0.32881359533, 2311990)
    # Create element
    ops.element('forceBeamColumn', 2311, 311, 321, 2311, 2311)
