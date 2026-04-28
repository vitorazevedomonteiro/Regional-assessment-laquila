# Add components of all infills to ops domain

# Create the material for diagonal struts
uniaxialMaterial Concrete01 2000 -1157.25129027 -0.0013 -11.5725129 -0.0045
# Create the elements for diagonal struts
element Truss 2000001 70000 11 0.13300886377971516 2000
element Truss 2000002 1 70010 0.13300886377971516 2000

# Create the material for diagonal struts
uniaxialMaterial Concrete01 2010 -1157.25129027 -0.0013 -11.5725129 -0.0045
# Create the elements for diagonal struts
element Truss 2010001 70010 21 0.13300886377971516 2010
element Truss 2010002 11 70020 0.13300886377971516 2010

# Create the material for diagonal struts
uniaxialMaterial Concrete01 2300 -1157.25129027 -0.0013 -11.5725129 -0.0045
# Create the elements for diagonal struts
element Truss 2300001 70300 311 0.13300886377971516 2300
element Truss 2300002 301 70310 0.13300886377971516 2300

# Create the material for diagonal struts
uniaxialMaterial Concrete01 2310 -1157.25129027 -0.0013 -11.5725129 -0.0045
# Create the elements for diagonal struts
element Truss 2310001 70310 321 0.13300886377971516 2310
element Truss 2310002 311 70320 0.13300886377971516 2310

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3000 -1157.24467666 -0.0013 -11.57244677 -0.0045
# Create the elements for diagonal struts
element Truss 3000001 70000 101 0.13301060201382886 3000
element Truss 3000002 1 70100 0.13301060201382886 3000

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3100 -1403.72422825 -0.0013 -14.03724228 -0.0045
# Create the elements for diagonal struts
element Truss 3100001 70100 201 0.08386831646140677 3100
element Truss 3100002 101 70200 0.08386831646140677 3100

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3200 -1157.24467666 -0.0013 -11.57244677 -0.0045
# Create the elements for diagonal struts
element Truss 3200001 70200 301 0.13301060201382886 3200
element Truss 3200002 201 70300 0.13301060201382886 3200

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3020 -1157.24467666 -0.0013 -11.57244677 -0.0045
# Create the elements for diagonal struts
element Truss 3020001 70020 121 0.13301060201382886 3020
element Truss 3020002 21 70120 0.13301060201382886 3020

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3120 -1403.72422825 -0.0013 -14.03724228 -0.0045
# Create the elements for diagonal struts
element Truss 3120001 70120 221 0.08386831646140677 3120
element Truss 3120002 121 70220 0.08386831646140677 3120

# Create the material for diagonal struts
uniaxialMaterial Concrete01 3220 -1157.24467666 -0.0013 -11.57244677 -0.0045
# Create the elements for diagonal struts
element Truss 3220001 70220 321 0.13301060201382886 3220
element Truss 3220002 221 70320 0.13301060201382886 3220
