# Perform linear static analysis under gravity loads

# Add gravity time-series and load pattern to ops domain
timeSeries Linear 1
pattern Plain 1 1 {

    # Add beam gravity loads to ops domain
    eleLoad -ele 1001 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1101 -type -beamUniform -3.6369 0.0
    eleLoad -ele 1201 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1011 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1111 -type -beamUniform -23.85125 0.0
    eleLoad -ele 1211 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1021 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1121 -type -beamUniform -11.64 0.0
    eleLoad -ele 1221 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1031 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1131 -type -beamUniform -8.87505 0.0
    eleLoad -ele 1231 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1002 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1102 -type -beamUniform -3.6369 0.0
    eleLoad -ele 1202 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1012 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1112 -type -beamUniform -23.85125 0.0
    eleLoad -ele 1212 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1022 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1122 -type -beamUniform -11.64 0.0
    eleLoad -ele 1222 -type -beamUniform -19.9375 0.0
    eleLoad -ele 1032 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1132 -type -beamUniform -8.87505 0.0
    eleLoad -ele 1232 -type -beamUniform -13.0238 0.0
    eleLoad -ele 1003 -type -beamUniform -10.625 0.0
    eleLoad -ele 1103 -type -beamUniform -2.8125 0.0
    eleLoad -ele 1203 -type -beamUniform -10.625 0.0
    eleLoad -ele 1013 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1113 -type -beamUniform -23.35625 0.0
    eleLoad -ele 1213 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1023 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1123 -type -beamUniform -10.65 0.0
    eleLoad -ele 1223 -type -beamUniform -18.4375 0.0
    eleLoad -ele 1033 -type -beamUniform -10.625 0.0
    eleLoad -ele 1133 -type -beamUniform -6.73125 0.0
    eleLoad -ele 1233 -type -beamUniform -10.625 0.0
    eleLoad -ele 6200 -type -beamUniform -19.6369 0.0
    eleLoad -ele 6201 -type -beamUniform -19.3244 0.0
    eleLoad -ele 6202 -type -beamUniform -19.3244 0.0
    eleLoad -ele 2001 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2101 -type -beamUniform -20.25 0.0
    eleLoad -ele 2201 -type -beamUniform -20.25 0.0
    eleLoad -ele 2301 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2011 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2111 -type -beamUniform -32.07885 0.0
    eleLoad -ele 2211 -type -beamUniform -32.07885 0.0
    eleLoad -ele 2311 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2021 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2121 -type -beamUniform -32.07885 0.0
    eleLoad -ele 2221 -type -beamUniform -32.07885 0.0
    eleLoad -ele 2321 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2002 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2102 -type -beamUniform -19.9375 0.0
    eleLoad -ele 2202 -type -beamUniform -19.9375 0.0
    eleLoad -ele 2302 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2012 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2112 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2212 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2312 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2022 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2122 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2222 -type -beamUniform -31.76635 0.0
    eleLoad -ele 2322 -type -beamUniform -21.5863 0.0
    eleLoad -ele 2003 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2103 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2203 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2303 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2013 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2113 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2213 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2313 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2023 -type -beamUniform -18.4375 0.0
    eleLoad -ele 2123 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2223 -type -beamUniform -28.93975 0.0
    eleLoad -ele 2323 -type -beamUniform -18.4375 0.0

    # Add column gravity loads to ops domain
    load 70000 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 1 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70300 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 301 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70010 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 11 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70110 0.0 0.0 -3.375 0.0 0.0 0.0
    load 111 0.0 0.0 -3.375 0.0 0.0 0.0
    load 70210 0.0 0.0 -3.375 0.0 0.0 0.0
    load 211 0.0 0.0 -3.375 0.0 0.0 0.0
    load 70310 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 311 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70020 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 21 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70120 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 121 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 70220 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 221 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 70320 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 321 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70030 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 31 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70130 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 131 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70230 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 231 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70330 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 331 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 1 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 2 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 301 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 302 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 11 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 12 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 111 0.0 0.0 -3.375 0.0 0.0 0.0
    load 112 0.0 0.0 -3.375 0.0 0.0 0.0
    load 211 0.0 0.0 -3.375 0.0 0.0 0.0
    load 212 0.0 0.0 -3.375 0.0 0.0 0.0
    load 311 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 312 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 21 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 22 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 121 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 122 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 221 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 222 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 321 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 322 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 31 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 32 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 131 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 132 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 231 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 232 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 331 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 332 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 2 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 3 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 302 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 303 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 12 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 13 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 112 0.0 0.0 -3.375 0.0 0.0 0.0
    load 113 0.0 0.0 -3.375 0.0 0.0 0.0
    load 212 0.0 0.0 -3.375 0.0 0.0 0.0
    load 213 0.0 0.0 -3.375 0.0 0.0 0.0
    load 312 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 313 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 22 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 23 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 122 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 123 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 222 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 223 0.0 0.0 -4.59375 0.0 0.0 0.0
    load 322 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 323 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 32 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 33 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 132 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 133 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 232 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 233 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 332 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 333 0.0 0.0 -2.34375 0.0 0.0 0.0
    load 70100 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 70200 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 101 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 201 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 102 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1103 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1103 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 103 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 202 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1203 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 1203 0.0 0.0 -1.171875 0.0 0.0 0.0
    load 203 0.0 0.0 -1.171875 0.0 0.0 0.0
}

# Perform gravity analysis and save the model state
system UmfPack
numberer RCM
constraints Transformation
test NormDispIncr 1e-08 10 3
integrator LoadControl 0.1
algorithm Newton
analysis Static
analyze 10
loadConst -time 0.0
wipeAnalysis
