See the documentation [Readme](https://github.com/TnTech-ECE/StarterRepo/blob/4acf2722f47a9d7eadf164df901ab597b25184e5/Documentation/ReadMe.md) for information about what should be in this directory
# TEC Prototype PCB Connection Hub

This directory contains the PCB design files for the TEC Prototype Personal Space Weather Station.

## Contents
- KiCad project files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`)
- Symbol and footprint libraries required for the design
- Gerber files for PCB fabrication
- Archived project zip (portable version with all dependencies)

## Getting Started
1. Download or extract the archived project `.zip` file in this directory.
2. Open the `.kicad_pro` file using KiCad (version 6 or later recommended).
3. All required symbols and footprints are included locally in the project.

## Manufacturing
- Use the Gerber files located in the `/gerbers` folder.
- Upload the Gerber `.zip` to a PCB manufacturer such as JLCPCB or PCBWay.
- Verify the board preview before ordering.

## Important Notes
- 3D footprint models were removed to reduce file size and are not required for fabrication or operation.
- Ensure correct polarity and voltage levels when powering the board.

## Replicability
This project is intended to be fully reproducible. All required design files and dependencies are included. No external libraries are required to open or manufacture the PCB.

## Future Improvements
- Increase use of through-hole components for easier assembly
- Add additional status LEDs for debugging and monitoring
- Simplify power stage for hobbyist accessibility
