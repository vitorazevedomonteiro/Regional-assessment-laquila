proc _set_algorithm { tol ctrl_node ctrl_dof dincr {iter 100} } {
    # Sets the solution algorithm for NSPA in OpenSees.
    #
    # Parameters
    # ----------
    # tol : float
    #     The tolerance criteria used to check for convergence.
    # ctrl_node : int
    #     Tag of control node.
    # ctrl_dof : int
    #     Tag of control degrees of freedom, i.e., 1 or 2.
    # dincr : float
    #     The displacement increment considered during analysis.
    # iter : float
    #     The max number of iterations to check before returning failure.
    #     By default 100.
    #
    # Return
    # ------
    # int
    #     Result of the new analysis step in OpenSees.

    # Set testing and control procedures
    test NormDispIncr $tol $iter
    integrator DisplacementControl $ctrl_node $ctrl_dof $dincr
    # Try KrylovNewton
    algorithm KrylovNewton
    set ok [analyze 1]
    # Try NewtonLineSearch algorithm
    if { $ok != 0 } {
        algorithm NewtonLineSearch -InitialInterpolated 0.8
        set ok [analyze 1]
    }
    # Try Broyden algorithm
    if { $ok != 0 } {
        algorithm Broyden 50
        set ok [analyze 1]
    }
    # Try Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm
    if { $ok != 0 } {
        algorithm BFGS
        set ok [analyze 1]
    }
    # Return the analysis result
    return $ok
}


proc do_nspa_x { { max_drift 0.1 } { dincr 0.001 } } { 
    # Performs nonlinear static pushover analysis (NSPA) in x direction.
    #
    # Parameters
    # ----------
    # max_drift : float, optional.
    #    Maximum considered drift value for the control node.
    #    By default 0.1
    # dincr : float, optional.
    #    First displacement increment considered during the analysis.
    #    By default 0.001.
    #
    # Return
    # ------
    # ctrl_disp : List[float]
    #    Displacement values of control node.
    # base_shear : List[float]
    #    Base shear value obtained as sum of the reaction forces.

    # Set output directory
    set output_directory "NSPA-Results"
    file mkdir $output_directory
    set reaction_file_path "$output_directory/support_reactions_x.out"
    set disp_file_path "$output_directory/storey_displacements_x.out"
    set storey_heights_file_path "$output_directory/storey_heights.out"

    # Build the numerical model
    source model.tcl

    # Add NSPA time-series and load pattern to ops domain
    timeSeries Linear 2
    pattern Plain 2 2 {
        load 91000 0.18035668637941396 0 0 0 0 0
        load 92000 0.3597163138857157 0 0 0 0 0
        load 93000 0.45992699973487045 0 0 0 0 0
    }

    # Set recorders
    set ctrl_node 93000
    set ctrl_dof 1
    set supports [list 70000 70010 70020 70030 70100 70110 70120 70130 70200 70210 70220 70230 70300 70310 70320 70330]
    set floors [list 91000 92000 93000]
    recorder Node -file $disp_file_path -node {*}$floors -dof $ctrl_dof disp
    recorder Node -file $reaction_file_path -node {*}$supports -dof $ctrl_dof reaction

    # Base level coordinate
    set base_level 1.0e12
    foreach node $supports {
        set zCoord [nodeCoord $node 3]
        if {$zCoord < $base_level} {
            set base_level $zCoord
        }
    }
    # Save storey heights
    set file [open $storey_heights_file_path "w"]
    foreach node $floors {
        puts $file [expr {[nodeCoord $node 3] - $base_level}]
    }
    close $file

    # Set analysis parameters
    set max_disp [expr {$max_drift * [nodeCoord $ctrl_node 3] - $base_level}]
    set tol_init 1.0e-6
    set iter_init 20
    wipeAnalysis
    system UmfPack
    numberer RCM
    constraints Penalty 1.0e12 1.0e12
    test EnergyIncr $tol_init $iter_init
    integrator DisplacementControl $ctrl_node $ctrl_dof $dincr
    algorithm Newton -initialThenCurrent
    analysis Static

    # Start performing the analysis
    set max_base_shear 0
    set ok 0
    set cont 1
    set base_shear [list 0.0]
    set ctrl_disp [list 0.0]
    while { $ok == 0 && $cont == 1 } {
        # Perform the analysis for a single step with current settings
        set ok [analyze 1]
        # try other algorithms
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof $dincr]
        }
        # reduce dincr to an half
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof [expr 0.5 * $dincr]]
        }
        # reduce dincr to a quarter
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }
        # increase tolerance by factor of 10
        if { $ok != 0 } {
            set ok [_set_algorithm [expr 10 * $tol_init] $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }
        # increase tolerance by factor of 100
        if { $ok != 0 } {
            set ok [_set_algorithm [expr 100 * $tol_init] $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }

        # Get the base shear force
        reactions
        set current_disp [nodeDisp $ctrl_node $ctrl_dof]
        set current_shear 0
        foreach foundation_node $supports {
            set reaction [nodeReaction $foundation_node $ctrl_dof]
            set current_shear [expr $current_shear + abs($reaction)]
        }
        # Calculate the maximum encountered shear value
        set max_base_shear [expr {max($max_base_shear, $current_shear)}]
        # Set continue flag
        set cont [expr {($current_disp < $max_disp) && ($current_shear >= 0.4 * $max_base_shear)}]
        # Append base shear and control node displacement
        if { $ok == 0 && $cont == 1 } {
            lappend base_shear $current_shear
            lappend ctrl_disp $current_disp
        }
    }

    # Wipe the model
    wipe
    # Return base shear and control node displacement history
    return [list $ctrl_disp $base_shear]
}


proc do_nspa_y { { max_drift 0.1 } { dincr 0.001 } } { 
    # Performs nonlinear static pushover analysis (NSPA) in y direction.
    #
    # Parameters
    # ----------
    # max_drift : float, optional.
    #    Maximum considered drift value for the control node.
    #    By default 0.1
    # dincr : float, optional.
    #    First displacement increment considered during the analysis.
    #    By default 0.001.
    #
    # Return
    # ------
    # ctrl_disp : List[float]
    #    Displacement values of control node.
    # base_shear : List[float]
    #    Base shear value obtained as sum of the reaction forces.

    # Set output directory
    set output_directory "NSPA-Results"
    file mkdir $output_directory
    set reaction_file_path "$output_directory/support_reactions_y.out"
    set disp_file_path "$output_directory/storey_displacements_y.out"
    set storey_heights_file_path "$output_directory/storey_heights.out"

    # Build the numerical model
    source model.tcl

    # Add NSPA time-series and load pattern to ops domain
    timeSeries Linear 2
    pattern Plain 2 2 {
        load 91000 0 0.18035668637941396 0 0 0 0
        load 92000 0 0.3597163138857157 0 0 0 0
        load 93000 0 0.45992699973487045 0 0 0 0
    }

    # Set recorders
    set ctrl_node 93000
    set ctrl_dof 2
    set supports [list 70000 70010 70020 70030 70100 70110 70120 70130 70200 70210 70220 70230 70300 70310 70320 70330]
    set floors [list 91000 92000 93000]
    recorder Node -file $disp_file_path -node {*}$floors -dof $ctrl_dof disp
    recorder Node -file $reaction_file_path -node {*}$supports -dof $ctrl_dof reaction

    # Base level coordinate
    set base_level 1.0e12
    foreach node $supports {
        set zCoord [nodeCoord $node 3]
        if {$zCoord < $base_level} {
            set base_level $zCoord
        }
    }
    # Save storey heights
    set file [open $storey_heights_file_path "w"]
    foreach node $floors {
        puts $file [expr {[nodeCoord $node 3] - $base_level}]
    }
    close $file

    # Set analysis parameters
    set max_disp [expr {$max_drift * [nodeCoord $ctrl_node 3] - $base_level}]
    set tol_init 1.0e-6
    set iter_init 20
    wipeAnalysis
    system UmfPack
    numberer RCM
    constraints Penalty 1.0e12 1.0e12
    test EnergyIncr $tol_init $iter_init
    integrator DisplacementControl $ctrl_node $ctrl_dof $dincr
    algorithm Newton -initialThenCurrent
    analysis Static

    # Start performing the analysis
    set max_base_shear 0
    set ok 0
    set cont 1
    set base_shear [list 0.0]
    set ctrl_disp [list 0.0]
    while { $ok == 0 && $cont == 1 } {
        # Perform the analysis for a single step with current settings
        set ok [analyze 1]
        # try other algorithms
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof $dincr]
        }
        # reduce dincr to an half
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof [expr 0.5 * $dincr]]
        }
        # reduce dincr to a quarter
        if { $ok != 0 } {
            set ok [_set_algorithm $tol_init $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }
        # increase tolerance by factor of 10
        if { $ok != 0 } {
            set ok [_set_algorithm [expr 10 * $tol_init] $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }
        # increase tolerance by factor of 100
        if { $ok != 0 } {
            set ok [_set_algorithm [expr 100 * $tol_init] $ctrl_node $ctrl_dof [expr 0.25 * $dincr]]
        }

        # Get the base shear force
        reactions
        set current_disp [nodeDisp $ctrl_node $ctrl_dof]
        set current_shear 0
        foreach foundation_node $supports {
            set reaction [nodeReaction $foundation_node $ctrl_dof]
            set current_shear [expr $current_shear + abs($reaction)]
        }
        # Calculate the maximum encountered shear value
        set max_base_shear [expr {max($max_base_shear, $current_shear)}]
        # Set continue flag
        set cont [expr {($current_disp < $max_disp) && ($current_shear >= 0.4 * $max_base_shear)}]
        # Append base shear and control node displacement
        if { $ok == 0 && $cont == 1 } {
            lappend base_shear $current_shear
            lappend ctrl_disp $current_disp
        }
    }

    # Wipe the model
    wipe
    # Return base shear and control node displacement history
    return [list $ctrl_disp $base_shear]
}
