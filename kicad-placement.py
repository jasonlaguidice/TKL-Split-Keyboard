from pcbnew import *
pcb = GetBoard()

switch = pcb.FindModule("SW1")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,-0.000))
diode = pcb.FindModule("D1")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW8")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,19.050))
diode = pcb.FindModule("D8")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW15")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,38.100))
diode = pcb.FindModule("D15")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW22")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,57.150))
diode = pcb.FindModule("D22")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,60.198))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW28")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,76.200))
diode = pcb.FindModule("D28")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,79.248))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW35")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,95.250))
diode = pcb.FindModule("D35")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,98.298))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW2")
if switch is not None:
    switch.SetPosition(wxPointMM(0.000,114.300))
diode = pcb.FindModule("D2")
if diode is not None:
    diode.SetPosition(wxPointMM(-7.620,117.348))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW9")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,-0.000))
diode = pcb.FindModule("D9")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW16")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,19.050))
diode = pcb.FindModule("D16")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW23")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,38.100))
diode = pcb.FindModule("D23")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW29")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,57.150))
diode = pcb.FindModule("D29")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,60.198))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW36")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,76.200))
diode = pcb.FindModule("D36")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,79.248))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW3")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,95.250))
diode = pcb.FindModule("D3")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,98.298))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW10")
if switch is not None:
    switch.SetPosition(wxPointMM(19.050,114.300))
diode = pcb.FindModule("D10")
if diode is not None:
    diode.SetPosition(wxPointMM(11.430,117.348))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW17")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,-0.000))
diode = pcb.FindModule("D17")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW24")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,19.050))
diode = pcb.FindModule("D24")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW30")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,38.100))
diode = pcb.FindModule("D30")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW37")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,57.150))
diode = pcb.FindModule("D37")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,60.198))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW4")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,76.200))
diode = pcb.FindModule("D4")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,79.248))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW11")
if switch is not None:
    switch.SetPosition(wxPointMM(38.100,95.250))
diode = pcb.FindModule("D11")
if diode is not None:
    diode.SetPosition(wxPointMM(30.480,98.298))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW18")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,-0.000))
diode = pcb.FindModule("D18")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW25")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,19.050))
diode = pcb.FindModule("D25")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW31")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,38.100))
diode = pcb.FindModule("D31")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW5")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,57.150))
diode = pcb.FindModule("D5")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,60.198))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW12")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,76.200))
diode = pcb.FindModule("D12")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,79.248))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW19")
if switch is not None:
    switch.SetPosition(wxPointMM(57.150,95.250))
diode = pcb.FindModule("D19")
if diode is not None:
    diode.SetPosition(wxPointMM(49.530,98.298))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW26")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,-0.000))
diode = pcb.FindModule("D26")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW32")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,19.050))
diode = pcb.FindModule("D32")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW6")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,38.100))
diode = pcb.FindModule("D6")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW13")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,57.150))
diode = pcb.FindModule("D13")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,60.198))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW20")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,76.200))
diode = pcb.FindModule("D20")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,79.248))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW27")
if switch is not None:
    switch.SetPosition(wxPointMM(76.200,95.250))
diode = pcb.FindModule("D27")
if diode is not None:
    diode.SetPosition(wxPointMM(68.580,98.298))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW33")
if switch is not None:
    switch.SetPosition(wxPointMM(95.250,-0.000))
diode = pcb.FindModule("D33")
if diode is not None:
    diode.SetPosition(wxPointMM(87.630,3.048))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW7")
if switch is not None:
    switch.SetPosition(wxPointMM(95.250,19.050))
diode = pcb.FindModule("D7")
if diode is not None:
    diode.SetPosition(wxPointMM(87.630,22.098))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW14")
if switch is not None:
    switch.SetPosition(wxPointMM(95.250,38.100))
diode = pcb.FindModule("D14")
if diode is not None:
    diode.SetPosition(wxPointMM(87.630,41.148))
    diode.SetOrientationDegrees(270)

switch = pcb.FindModule("SW21")
if switch is not None:
    switch.SetPosition(wxPointMM(95.250,57.150))
diode = pcb.FindModule("D21")
if diode is not None:
    diode.SetPosition(wxPointMM(87.630,60.198))
    diode.SetOrientationDegrees(270)

led = pcb.FindModule("LED1")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,5.080))

led = pcb.FindModule("LED8")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,24.130))

led = pcb.FindModule("LED15")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,43.180))

led = pcb.FindModule("LED22")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,62.230))

led = pcb.FindModule("LED28")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,81.280))

led = pcb.FindModule("LED35")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,100.330))

led = pcb.FindModule("LED2")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(0.000,119.380))

led = pcb.FindModule("LED9")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,5.080))

led = pcb.FindModule("LED16")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,24.130))

led = pcb.FindModule("LED23")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,43.180))

led = pcb.FindModule("LED29")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,62.230))

led = pcb.FindModule("LED36")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,81.280))

led = pcb.FindModule("LED3")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,100.330))

led = pcb.FindModule("LED10")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(19.050,119.380))

led = pcb.FindModule("LED17")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,5.080))

led = pcb.FindModule("LED24")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,24.130))

led = pcb.FindModule("LED30")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,43.180))

led = pcb.FindModule("LED37")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,62.230))

led = pcb.FindModule("LED4")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,81.280))

led = pcb.FindModule("LED11")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(38.100,100.330))

led = pcb.FindModule("LED18")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,5.080))

led = pcb.FindModule("LED25")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,24.130))

led = pcb.FindModule("LED31")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,43.180))

led = pcb.FindModule("LED5")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,62.230))

led = pcb.FindModule("LED12")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,81.280))

led = pcb.FindModule("LED19")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(57.150,100.330))

led = pcb.FindModule("LED26")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,5.080))

led = pcb.FindModule("LED32")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,24.130))

led = pcb.FindModule("LED6")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,43.180))

led = pcb.FindModule("LED13")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,62.230))

led = pcb.FindModule("LED20")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,81.280))

led = pcb.FindModule("LED27")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(76.200,100.330))

led = pcb.FindModule("LED33")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(95.250,5.080))

led = pcb.FindModule("LED7")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(95.250,24.130))

led = pcb.FindModule("LED14")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not False:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(0)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(95.250,43.180))

led = pcb.FindModule("LED21")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if False is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(0.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(95.250,62.230))

led = pcb.FindModule("LED43")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(360.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(198.239,-8.644))

led = pcb.FindModule("LED42")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(360.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(129.778,-8.644))

led = pcb.FindModule("LED41")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(360.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(61.317,-8.644))

led = pcb.FindModule("LED40")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(90.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(-8.644,39.291))

led = pcb.FindModule("LED39")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(90.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(-8.644,85.725))

led = pcb.FindModule("LED38")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(90.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(-8.644,132.159))

led = pcb.FindModule("LED37")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(180.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(61.317,180.094))

led = pcb.FindModule("LED36")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(180.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(129.778,180.094))

led = pcb.FindModule("LED35")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(180.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(198.239,180.094))

led = pcb.FindModule("LED34")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(270.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(268.200,116.681))

led = pcb.FindModule("LED33")
if led is not None:
    # Reset positioning
    if led.IsFlipped() is True:
        led.Flip(wxPointMM(0,0))
    led.SetOrientationDegrees(0)
    led.SetPosition(wxPointMM(0,0))

    # Apply flip if required
    if led.IsFlipped() is not True:
        led.Flip(wxPointMM(0,0))

    if True is True:
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,2.000))
        # Fixup rotation
        led.SetOrientationDegrees(270.000)
    else:
        # Fixup rotation
        led.SetOrientationDegrees(180)
        # Fixup silkscreen
        for item in led.GraphicalItems():
            if isinstance(item, TEXTE_MODULE) and item.GetText() != "HOLE":
                item.SetPosition(wxPointMM(-3.900,-2.000))

    # Fixup positioning
    led.SetPosition(wxPointMM(268.200,54.769))

drill = pcb.FindModule("DRILL1")
if drill is not None:
    drill.SetPosition(wxPointMM(266.700,-7.144))

drill = pcb.FindModule("DRILL2")
if drill is not None:
    drill.SetPosition(wxPointMM(-7.144,-7.144))

drill = pcb.FindModule("DRILL3")
if drill is not None:
    drill.SetPosition(wxPointMM(-7.144,178.594))

drill = pcb.FindModule("DRILL4")
if drill is not None:
    drill.SetPosition(wxPointMM(266.700,178.594))

lcd = pcb.FindModule("LCD1")
if lcd is not None:
    lcd.SetPosition(wxPointMM(144.780,51.435))
    lcd.SetOrientationDegrees(0.000)

encoder = pcb.FindModule("ENC1")
if encoder is not None:
    encoder.SetPosition(wxPointMM(145.733,76.200))

hat = pcb.FindModule("HAT1")
if hat is not None:
    hat.SetPosition(wxPointMM(102.394,104.775))

reset = pcb.FindModule("RESET1")
if reset is not None:
    reset.SetPosition(wxPointMM(164.306,64.294))

usb = pcb.FindModule("USB1")
if usb is not None:
    usb.SetPosition(wxPointMM(120.015,-19.759))
    usb.SetOrientationDegrees(180.000)

split = pcb.FindModule("SPLIT1")
if split is not None:
    split.SetPosition(wxPointMM(140.494,-13.840))
    split.SetOrientationDegrees(135.000)

Refresh()
