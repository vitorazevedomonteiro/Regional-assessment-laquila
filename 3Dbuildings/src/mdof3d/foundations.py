import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 3000
    ops.node(70000, 0.0, 0.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70000, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3010
    ops.node(70010, 0.0, 5.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70010, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3020
    ops.node(70020, 0.0, 10.0, 0.0, '-mass', 0.7148318042813455, 0.7148318042813455, 0.7148318042813455, 0.0, 0.0, 0.0)
    ops.fix(70020, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3030
    ops.node(70030, 0.0, 13.3, 0.0, '-mass', 0.7148318042813455, 0.7148318042813455, 0.7148318042813455, 0.0, 0.0, 0.0)
    ops.fix(70030, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3040
    ops.node(70040, 0.0, 18.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70040, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3050
    ops.node(70050, 0.0, 23.3, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70050, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3100
    ops.node(70100, 5.0, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70100, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3110
    ops.node(70110, 5.0, 5.0, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70110, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 4120
    ops.node(70120, 5.0, 10.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70120, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3130
    ops.node(70130, 5.0, 13.3, 0.0, '-mass', 1.0614169215086644, 1.0614169215086644, 1.0614169215086644, 0.0, 0.0, 0.0)
    ops.fix(70130, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3140
    ops.node(70140, 5.0, 18.3, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70140, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3150
    ops.node(70150, 5.0, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70150, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3200
    ops.node(70200, 8.3, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70200, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3210
    ops.node(70210, 8.3, 5.0, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70210, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 4220
    ops.node(70220, 8.3, 10.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70220, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3230
    ops.node(70230, 8.3, 13.3, 0.0, '-mass', 1.0614169215086644, 1.0614169215086644, 1.0614169215086644, 0.0, 0.0, 0.0)
    ops.fix(70230, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3240
    ops.node(70240, 8.3, 18.3, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70240, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3250
    ops.node(70250, 8.3, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70250, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3300
    ops.node(70300, 13.3, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70300, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3310
    ops.node(70310, 13.3, 5.0, 0.0, '-mass', 1.3105249745158003, 1.3105249745158003, 1.3105249745158003, 0.0, 0.0, 0.0)
    ops.fix(70310, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3320
    ops.node(70320, 13.3, 10.0, 0.0, '-mass', 1.083078491335372, 1.083078491335372, 1.083078491335372, 0.0, 0.0, 0.0)
    ops.fix(70320, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3330
    ops.node(70330, 13.3, 13.3, 0.0, '-mass', 1.083078491335372, 1.083078491335372, 1.083078491335372, 0.0, 0.0, 0.0)
    ops.fix(70330, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3340
    ops.node(70340, 13.3, 18.3, 0.0, '-mass', 1.3105249745158003, 1.3105249745158003, 1.3105249745158003, 0.0, 0.0, 0.0)
    ops.fix(70340, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3350
    ops.node(70350, 13.3, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70350, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3400
    ops.node(70400, 16.6, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70400, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3410
    ops.node(70410, 16.6, 5.0, 0.0, '-mass', 1.8304026503567792, 1.8304026503567792, 1.8304026503567792, 0.0, 0.0, 0.0)
    ops.fix(70410, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3420
    ops.node(70420, 16.6, 10.0, 0.0, '-mass', 1.083078491335372, 1.083078491335372, 1.083078491335372, 0.0, 0.0, 0.0)
    ops.fix(70420, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3430
    ops.node(70430, 16.6, 13.3, 0.0, '-mass', 1.083078491335372, 1.083078491335372, 1.083078491335372, 0.0, 0.0, 0.0)
    ops.fix(70430, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3440
    ops.node(70440, 16.6, 18.3, 0.0, '-mass', 1.8304026503567792, 1.8304026503567792, 1.8304026503567792, 0.0, 0.0, 0.0)
    ops.fix(70440, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3450
    ops.node(70450, 16.6, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70450, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3500
    ops.node(70500, 21.6, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70500, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3510
    ops.node(70510, 21.6, 5.0, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70510, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 4520
    ops.node(70520, 21.6, 10.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70520, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3530
    ops.node(70530, 21.6, 13.3, 0.0, '-mass', 1.0614169215086644, 1.0614169215086644, 1.0614169215086644, 0.0, 0.0, 0.0)
    ops.fix(70530, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3540
    ops.node(70540, 21.6, 18.3, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70540, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3550
    ops.node(70550, 21.6, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70550, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3600
    ops.node(70600, 24.9, 0.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70600, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3610
    ops.node(70610, 24.9, 5.0, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70610, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 4620
    ops.node(70620, 24.9, 10.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70620, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3630
    ops.node(70630, 24.9, 13.3, 0.0, '-mass', 1.0614169215086644, 1.0614169215086644, 1.0614169215086644, 0.0, 0.0, 0.0)
    ops.fix(70630, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3640
    ops.node(70640, 24.9, 18.3, 0.0, '-mass', 1.2996941896024465, 1.2996941896024465, 1.2996941896024465, 0.0, 0.0, 0.0)
    ops.fix(70640, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3650
    ops.node(70650, 24.9, 23.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70650, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3700
    ops.node(70700, 29.9, 0.0, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70700, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3710
    ops.node(70710, 29.9, 5.0, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70710, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3720
    ops.node(70720, 29.9, 10.0, 0.0, '-mass', 0.7148318042813455, 0.7148318042813455, 0.7148318042813455, 0.0, 0.0, 0.0)
    ops.fix(70720, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3730
    ops.node(70730, 29.9, 13.3, 0.0, '-mass', 0.7148318042813455, 0.7148318042813455, 0.7148318042813455, 0.0, 0.0, 0.0)
    ops.fix(70730, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3740
    ops.node(70740, 29.9, 18.3, 0.0, '-mass', 0.9856014271151883, 0.9856014271151883, 0.9856014271151883, 0.0, 0.0, 0.0)
    ops.fix(70740, 1, 1, 1, 1, 1, 1)

    # Foundation or support under the column 3750
    ops.node(70750, 29.9, 23.3, 0.0, '-mass', 0.5307084607543322, 0.5307084607543322, 0.5307084607543322, 0.0, 0.0, 0.0)
    ops.fix(70750, 1, 1, 1, 1, 1, 1)
