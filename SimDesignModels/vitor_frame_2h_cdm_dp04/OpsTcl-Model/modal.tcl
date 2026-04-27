proc do_modal { {numModes 3} } {
    # Perform modal analysis for built OpenSees model
    #
    # Parameters
    # ----------
    # num_modes : int, optional
    #     Number of modes considered for modal analysis.
    #     By default 3.#
    # Return
    # ------
    # dict
    #     Dictionary containing modal properties.

    # Set output directory
    set output_directory "Modal-Results"
    file mkdir $output_directory
    # Build the numerical model
    source model.tcl

    # Perform eigenvalue analysis
    set eigenVals [eigen $numModes]
    # Save eigen vectors for retained floor nodes
    set nodes [list 91000 92000]
    # Loop through eigenvectors
    for {set i 1} {$i <= $numModes} {incr i} {
        set modalDisps ""
        foreach node $nodes {
            # Get the eigenvector as a list of floats
            set eigenvector [nodeEigenvector $node $i]
            # Join the list into a comma-separated string
            set disps [join $eigenvector ", "]
            # Append the node tag and the comma-separated eigenvector string
            append modalDisps "$node, $disps\n"
        }
        # Write the eigenvector data for the mode to a file
        set report_file [open "$output_directory/EigenVectors_Mode${i}.txt" "w"]
        puts $report_file $modalDisps
        close $report_file
    }

    # Perform modal analysis and save results
    set report_file "$output_directory/ModalProperties.txt"
    set results [modalProperties -print -return -file $report_file -unorm]

    return $results
}