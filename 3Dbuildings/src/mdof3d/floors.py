import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(91000, 14.95349539, 11.66932979, 3.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 1, 101, 201, 301, 401, 501, 601, 701, 11, 111, 211, 311, 411, 511, 611, 711, 21, 121, 221, 321, 421, 521, 621, 721, 31, 131, 231, 331, 431, 531, 631, 731, 41, 141, 241, 341, 441, 541, 641, 741, 51, 151, 251, 351, 451, 551, 651, 751)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(92000, 14.95326847, 11.68524623, 6.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 2, 102, 202, 302, 402, 502, 602, 702, 12, 112, 212, 312, 412, 512, 612, 712, 22, 122, 222, 322, 422, 522, 622, 722, 32, 132, 232, 332, 432, 532, 632, 732, 42, 142, 242, 342, 442, 542, 642, 742, 52, 152, 252, 352, 452, 552, 652, 752)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Retained floor node
    ops.node(93000, 14.95598474, 11.66906432, 9.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 3, 103, 203, 303, 403, 503, 603, 703, 13, 113, 213, 313, 413, 513, 613, 713, 23, 123, 223, 323, 423, 523, 623, 723, 33, 133, 233, 333, 433, 533, 633, 733, 43, 143, 243, 343, 443, 543, 643, 743, 53, 153, 253, 353, 453, 553, 653, 753)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Retained floor node
    ops.node(94000, 14.95334291, 11.66926399, 12.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 4, 104, 204, 304, 404, 504, 604, 704, 14, 114, 214, 314, 414, 514, 614, 714, 24, 124, 224, 324, 424, 524, 624, 724, 34, 134, 234, 334, 434, 534, 634, 734, 44, 144, 244, 344, 444, 544, 644, 744, 54, 154, 254, 354, 454, 554, 654, 754)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)

    # Floor no. 5
    # Retained floor node
    ops.node(95000, 14.95340505, 11.66962205, 15.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 95000, 5, 105, 205, 305, 405, 505, 605, 705, 15, 115, 215, 315, 415, 515, 615, 715, 25, 125, 225, 325, 425, 525, 625, 725, 35, 135, 235, 335, 435, 535, 635, 735, 45, 145, 245, 345, 445, 545, 645, 745, 55, 155, 255, 355, 455, 555, 655, 755)
    # Fix the floating dofs of the retained node
    ops.fix(95000, 0, 0, 1, 1, 1, 0)

    # Floor no. 6
    # Retained floor node
    ops.node(96000, 14.95341646, 11.66968779, 18.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 96000, 6, 106, 206, 306, 406, 506, 606, 706, 16, 116, 216, 316, 416, 516, 616, 716, 26, 126, 226, 326, 426, 526, 626, 726, 36, 136, 236, 336, 436, 536, 636, 736, 46, 146, 246, 346, 446, 546, 646, 746, 56, 156, 256, 356, 456, 556, 656, 756)
    # Fix the floating dofs of the retained node
    ops.fix(96000, 0, 0, 1, 1, 1, 0)

    # Floor no. 7
    # Retained floor node
    ops.node(97000, 14.95341646, 11.66968779, 21.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 97000, 7, 107, 207, 307, 407, 507, 607, 707, 17, 117, 217, 317, 417, 517, 617, 717, 27, 127, 227, 327, 427, 527, 627, 727, 37, 137, 237, 337, 437, 537, 637, 737, 47, 147, 247, 347, 447, 547, 647, 747, 57, 157, 257, 357, 457, 557, 657, 757)
    # Fix the floating dofs of the retained node
    ops.fix(97000, 0, 0, 1, 1, 1, 0)

    # Floor no. 8
    # Retained floor node
    ops.node(98000, 14.95199607, 11.67013666, 24.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 98000, 8, 108, 208, 308, 408, 508, 608, 708, 18, 118, 218, 318, 418, 518, 618, 718, 28, 128, 228, 328, 428, 528, 628, 728, 38, 138, 238, 338, 438, 538, 638, 738, 48, 148, 248, 348, 448, 548, 648, 748, 58, 158, 258, 358, 458, 558, 658, 758)
    # Fix the floating dofs of the retained node
    ops.fix(98000, 0, 0, 1, 1, 1, 0)
