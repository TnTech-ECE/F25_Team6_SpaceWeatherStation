<h1 style="font-size:40px;">System Interconnections Subsystem Detailed Design</h1>

# **Function of the Subsystem**

&nbsp; &nbsp; &nbsp; &nbsp;The System Interconnections platform serves as the central hub for electrically linking all major modules and peripheral devices within the prototype. It balances high system integration with modular flexibility, enabling seamless configuration, testing, and replacement of system components.

&nbsp; &nbsp; &nbsp; &nbsp;The subsystem implements a multi-layer PCB-based hub that provides regulated power rails, standardized connectors, and optimized signal pathways. It routes power, data, and control signals while maintaining signal integrity and meeting the current and voltage requirements of all connected modules. Standardized connectors, including 1 mm JST, 2.54 mm headers, and screw terminals, ensure modularity and reliable interfacing with both the Raspberry Pi Pico and Raspberry Pi 4B, as well as peripherals such as the RF module, LoRa, OLED, and analog inputs.

&nbsp; &nbsp; &nbsp; &nbsp;The subsystem lead (Jack Bender) oversees the full lifecycle of the PCB, including schematic development, layout design, fabrication oversight, and functional validation. This role also includes selection of interconnection standards, signal protocols, and power delivery strategies, ensuring that the PCB fulfills the design specifications and constraints while supporting both current and future system expansions.

# **Specifications and Constraints**

&nbsp; &nbsp; &nbsp; &nbsp;The interconnections subsystem implements the PCB responsible for interconnecting modules, routing power and signals, providing physical interfaces, and selecting appropriate wiring to and from the board. The following specifications and constraints shape its design, each with the required rationale grounded in physics, system requirements, standards, ethics, and socio-economic considerations.

## **Specifications**

### **PCB Stackup Specification**

**Specification:** The subsystem shall use a 4-layer FR-4 stackup consisting of:

- Top signal layer
- Inner Ground plane
- Inner Power plane
- Bottom signal layer

**Rationale:** FR-4 provides cost-effective material for moderate-speed interfaces (e.g. SPI). A 4-layer stackup improves signal routing, offers a full layer dedicated to ground, and simplifies power distribution.

### **Power Regulation and Inputs Specification**

**Specification:** The subsystem shall provide on-board power regulation supporting two standardized input options:

- Wall adapter input
- Battery input

&nbsp; &nbsp; &nbsp; &nbsp;Power inputs shall include current protection, overvoltage protection, reverse polarity protection, and bulk capacitors. A power multiplexer (MUX) shall automatically prioritize the wall adapter when present. Both regulated 5V and 3.3V rails shall be distributed to all connectors and test points where necessary. Each IC shall include local decoupling capacitors placed near the power pin.

**Rationale:** Ensures safe and reliable operation while enabling flexible power options. Automatic preference for wall power reduces battery drain. 5V and 3.3V rails are industry-standard for embedded systems.

### **Expansion and Modularity Specification**

**Specification:** The subsystem shall provide expansion ports and optional module interfaces without interfering with primary board functions.

**Rationale:** Modularity reduces redesign costs and extends functionality, addressing socio-economic factors related to long-term maintainability.

### **SBC and MCU Expansion Headers Specification**

**Specification:** The subsystem shall provide parallel breakout headers exposing all GPIO pins of both the Raspberry Pi Pico and Raspberry Pi 4B directly on the PCB. Each header shall map one-to-one with the official Raspberry Pi Pico 40-pin pinout and the official Raspberry Pi 4B 40-pin GPIO pinout, maintaining numbering, orientation, and functionality.

**Rationale:** Providing local breakouts of all SBC and MCU pins increases hardware flexibility, simplifies debugging, and enables easier prototyping. Additionally, users gain direct access to every available signal for measurement.

### **1.0 mm JST Connector Specification**

**Specification:** The subsystem shall use standardized 1.0mm JST connectors (e.g., JST-SH/Qwiic/STEMMA QT) for digital interfaces where appropriate.

**Rationale:** Using these connectors for digital connection points maintains consistency and simplicity across the board and reduces mismatching of standardized connectors. This approach simplifies prototyping, minimizes wiring errors, and supports modular expansion and long-term maintainability.

### **Analog Input Specification**

**Specification:** The subsystem will provide direct access via screw terminals to analog-to-digital conversion (ADC) pins for easy interfacing with analog signals.

**Rationale:** Direct access to ADC pins enables users to interface with analog peripherals seamlessly.

## **Constraints**

### **Physical and Electrical Routing Constraint**

**Constraint:** The subsystem shall provide clear and optimized routing for power, data, and control traces, maintaining separation between digital, analog, and power signals. High speed connections will best avoid crossing breaks in power zones on lower layers.

**Rationale:** Minimizes crosstalk caused by capacitive and inductive coupling, as well as other forms of electrical noise. These constraints stem from electromagnetic coupling behavior and the system's signal integrity requirements.

### **Signal Integrity and EMI Constraint**

**Constraint:** The subsystem shall maintain a continuous nearby ground for all signal traces and minimize loop areas to limit EMI and noise, particularly on digital signals.

**Rationale:** Even at moderate speeds like SPI, proper return paths and grounded planes help prevent interference, reduce signal disturbances, and maintain reliable communication between modules. Among the most critical issues are electromagnetic interference (EMI) and signal integrity (SI). Poorly managed interconnects, inconsistent grounding, or inadequate shielding can lead to signal degradation, system instability, and even regulatory failures \[1\].

### **Trace, Via, and Wire Design Constraint**

**Constraint:** The subsystem shall select PCB trace widths, via diameters, and external wire gauges to accommodate expected current levels and shall use multiple parallel traces or wires when necessary to distribute current safely. These selections will be informed by IPC-2221 standards. IPC-2221 (Revision B effective 2012) is a generally accepted industry standard that defines a multitude of PCB design aspects \[2\]. Additionally, adequate copper areas will be used for thermal relief.

**Rationale:** Proper trace, via, and wire sizing prevents excessive heating and voltage drop while maintaining reliable current delivery. Using parallel traces or wires reduces the risk of overloading a single conductor.

### **Standards-Based Interface Constraint**

**Constraint:** The subsystem shall standardize electrical and physical interface connections using widely accepted header spacing, pin assignments, electrical circuits, and communication standards. I2C, SPI, and UART are commonly used as means for communication between devices within embedded systems due to their simplicity and ease of operation \[3\].

**Rationale:** Alignment with industry standards ensures interoperability with third-party modules and supports ethical engineering practices by reducing error, increasing accessibility, and lowering long-term replacement costs.

### **PCB and Schematic Labeling Constraint**

**Constraint:** All PCB components, headers, connectors and wire entry points shall be clearly labeled with interface designators, pin numbers, and signal names on both the PCB silkscreen and the schematic. The PCB silkscreen will include all relevant information for the current version of the project.

**Rationale:** Clear labeling improves assembly, debugging, testing, and maintenance. It reduces user error, simplifies documentation, and ensures consistency between the board and schematic. Proper labeling also facilitates modular expansion and long-term maintainability.

### **Form-Factor Constraint**

**Constraint:** The subsystem shall maintain a form-factor compatible with the enclosure and mounting requirements.

**Rationale:** Ensures physical compatibility and manufacturability. This constraint is based on physical limitations of the enclosure subsystem.

### **Manufacturability and Assembly Constraint**

**Constraint:** Component placement, footprints, and pad sizes shall comply with the capabilities and recommendations of the PCB manufacturer who will fabricate the PCB. These specifications come directly from PCBWay's PCB Capabilities \[4\]. The PCB design shall pass KiCad's design rules checker (DRC).

**Rationale:** Ensures the board can be reliably manufactured and assembled, reducing errors during soldering and inspection. Following manufacturer guidelines prevent issues such as solder bridging and component misalignment.

# **Overview of Proposed Solution**

&nbsp; &nbsp; &nbsp; &nbsp;The System Interconnections subsystem is designed to provide a centralized platform for connecting all peripheral modules and subsystems. It implements this functionality through a PCB that delivers regulated power rails, standardized connectors, optimized signal routing, and mechanical stability. Additionally, proper cables have been selected to interface with all peripheral modules, ensuring reliable electrical connections and compatibility with the system's connectors. The following section provides a detailed overview of the proposed solution.

**Substrate Material**

&nbsp; &nbsp; &nbsp; &nbsp;It is essential when designing a PCB to first consider the speed of the signals on the board, as signal frequency strongly influences material selection and stackup. For the Personal Space Weather System, the highest-frequency signals present on the PCB will be SPI communications, which typically operate in the tens of megahertz. FR-4 is an industry standard PCB material that has been used for decades due to its good balance of electrical, mechanical, and thermal properties at a relatively low cost. Importantly, FR-4 performs reliably for frequencies from DC through the low-GHz range \[5\], making it well suited for the signal speeds in this design. Therefore, FR-4 is selected as the substrate material for the PCB.

**Stackup**

&nbsp; &nbsp; &nbsp; &nbsp;Due to the complexity of connections being made between various modules in the prototype, a 4-layer board has been selected. The additional layers allow dense routing without signal congestion, provide uninterrupted ground and power planes, and improve the electrical performance and reliability of the interconnecting traces. A 4-layer configuration balances performance, cost, and space efficiency, making it ideal for applications that require moderate-to-high complexity, excellent signal integrity, and reliable power delivery \[6\].

&nbsp; &nbsp; &nbsp; &nbsp;The subsystem implements a 90x95mm 4-layer FR-4 PCB with the following stackup:

- Top Layer: Signal Layer
  - Includes all components and connection points for power, debugging, and interfacing with external modules.
- Second Layer: Ground Plane
  - Filled copper GND zone over the entire layer providing consistent current return paths.
- Third Layer: Power Plane
  - Includes regulated 5V and 3.3V copper zones oriented to simplify power routing on top and bottom layers.
- Bottom Layer: Signal Layer
  - Additional layer to ensure clean routing.

&nbsp; &nbsp; &nbsp; &nbsp;This layer arrangement not only optimizes electrical performance and signal integrity but also respects manufacturability constraints, ensuring that the board can be reliably fabricated and assembled according to the chosen manufacturer's specifications. The 90x95mm dimensions provide a compact form factor that fits the enclosure while allowing sufficient space for component placement, routing, and connector access.

**Manufacturability Specifications**

&nbsp; &nbsp; &nbsp; &nbsp;Based on the manufacturability and assembly constraints, the proposed PCB has passed KiCad's Design Rules Checker (DRC), which verifies that all board constraints are satisfied. These constraints follow the specifications provided by the manufacturer, PCBWay, including minimum trace width and spacing, via sizes, solder mask clearances, and silkscreen spacing. Adhering to these rules ensures reliable fabrication and reduces the risk of defects.

&nbsp; &nbsp; &nbsp; &nbsp;The following figure specifies the manufacturer's specifications used \[4\]:

PCBWay Design Specifications

**Tracing and Vias Constraints**

&nbsp; &nbsp; &nbsp; &nbsp;In addition to meeting the minimum manufacturability specifications, the PCB must be capable of handling the electrical throughput required by the system. All trace widths and via diameters are sized safely to carry the expected maximum continuous currents without overheating. These calculations assume an ambient temperature of 40 °C, a temperature rise of 10 °C, a copper thickness of 1 oz/ft², and a via wall copper thickness of 0.018 mm, as specified by the manufacturer.

&nbsp; &nbsp; &nbsp; &nbsp;The table below summarizes the expected maximum continuous currents along with the corresponding minimum trace widths and via diameters. Calculations were performed using the DigiKey Trace Width Calculator \[7\] and the Best Technology Via Current Calculator \[8\].

| Source | Expected Continuous Maximum Current (A) | Minimum Trace Width (mm) | Minimum Via Diameter (mm) |
| --- | --- | --- | --- |
| 12V Input | 1.6 | 0.57 | 0.35 |
| 5V Input | 3   | 1.37 | 0.84 |
| Data Lines | <0.005 | \*Below constraint | \*Below constraint |

\*This column shows minimum values; using traces and vias rated for more than needed is acceptable.

&nbsp; &nbsp; &nbsp; &nbsp;In many areas of the board, larger traces are intentionally used to act as heatsinks, improving thermal management. This is particularly evident near the full-bridge rectifier, where the traces near diode terminals are 1.2mm. Additionally, filled copper zones are used to distribute current and dissipate heat, such as those surrounding the TPS62913 buck converters. Trace lengths are kept as short as possible to minimize resistance, reduce voltage drops, and maintain clean return paths, enhancing electrical performance and thermal efficiency.

| Full Bridge Rectifier | TPS62913 Buck Converter |
| --- | --- |

&nbsp; &nbsp; &nbsp; &nbsp;By carefully sizing traces and vias to handle the maximum expected currents and optimizing copper fills and trace lengths for both thermal and electrical performance, the PCB ensures reliable power distribution throughout the system. With these constraints met, the next critical step is routing, where signal paths are laid out to connect all modules effectively.

**Routing**

&nbsp; &nbsp; &nbsp; &nbsp;The strategy for PCB routing is critical to ensure reliable signal transmission, proper power delivery, and modular connectivity between system components. Careful routing minimizes interference between traces and maintains signal integrity. Routing decisions were guided by four primary considerations: signal integrity, power distribution, trace management, and connection site access.

&nbsp; &nbsp; &nbsp; &nbsp;Data signal traces are kept on the top layer wherever possible, with the ground layer positioned between the signal traces and the power plane. This arrangement greatly reduces the likelihood of ground loops. By minimizing ground loop area, this strategy limits unwanted electromagnetic radiation, as a ground loop can otherwise act as an unintended antenna \[9\]. Additionally, the PCB incorporates a ground copper filled zone on the power plane at points where SPI connections cross, providing a low impedance return path and mitigating interference between signals. All ground fills are stitched to the main ground plane using vias, ensuring a continuous low impedance return path. Further reducing electromagnetic interference, routing is designed to combat crosstalk achieved by minimizing data signals crossing junctions on the power plane. Crosstalk occurs where there are rapid voltage and current transitions inducing voltages in adjacent traces due to inductive and capacitive coupling \[9\].

&nbsp; &nbsp; &nbsp; &nbsp;The use of a power plane greatly simplifies power distribution. Instead of routing individual traces for each voltage rail, entire planes are defined as filled copper zones regulated to their respective voltages. These zones are oriented to reduce EMI while spanning the board to deliver power efficiently to all components.

&nbsp; &nbsp; &nbsp; &nbsp;Beyond signal integrity, PCB trace routing is a careful balancing act to ensure all connections reach their intended components and connectors without congestion. The layout must navigate limited space and dense component placement, making design tools like KiCad's DRC particularly valuable. Mindful trace management ensures signals are routed efficiently, with minimal crossings and detours, while maintaining clear access to pads, vias, and connectors throughout the board.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the PCB routing strategy balances performance, power delivery, and accessibility. Careful attention to signal integrity, power distribution, trace management, and connection site access ensures an efficient board with straightforward access to all connection points for testing, debugging, and future expansion. These routing decisions directly satisfy the physical and electrical routing constraint by ensuring signal integrity, minimizing interference, and maintaining organized, electrically sound trace paths.

| SPI Signal Crossing w/ Ground Zone | Power Plane Routing |
| --- | --- |

**Power**

&nbsp; &nbsp; &nbsp; &nbsp;The PCB power design provides flexibility for the user by supporting two input sources: one for connection to mains power and another for portable operation via a battery system. This design involved a collaborative effort between the Power Subsystem lead (Kenneth Creamer) and the System Interconnections lead (Jack Bender) to achieve the proposed solution. Collaboration primarily focused on selecting surface-mount components with appropriate power ratings and form factors. The detailed signal path for both inputs is summarized in the Power Subsystem Detailed Design \[10\]. This document provides specifics regarding the PCB and a general overview of the power components used.

&nbsp; &nbsp; &nbsp; &nbsp;The PCB power design includes a thorough analysis of component specifications to properly manage thermal signatures and current ratings.

&nbsp; &nbsp; &nbsp; &nbsp;The wall mains input utilizes a USB-C connector, supporting up to 20VDC and 3A. All traces in this input power path have a width of at least 1.37mm, and via diameters are at least 0.84mm to accommodate the expected current. Critical singular vias in this path, such as the via that feeds the 5V plane from the MUX, are 1mm in diameter to ensure reliable current flow. In component-dense areas, filled copper regions are used to provide a low-resistance conduction path capable of handling the full 3 A.

&nbsp; &nbsp; &nbsp; &nbsp;The battery input uses a barrel jack connector rated for up to 24V and 8A, although the expected maximum current for this system is 1.6A. All traces in this input path have a width of at least 0.57mm, with via diameters of at least 0.35mm to handle the expected current safely. The battery input also incorporates a full-bridge rectifier using four SS32 Schottky diodes. Each diode has a forward voltage drop of approximately 0.5V, resulting in a power dissipation of roughly 0.8W per diode. This level of heat necessitates enlarged copper areas around the diode pads to aid in thermal dissipation.

&nbsp; &nbsp; &nbsp; &nbsp;The TPS2121RUXR voltage multiplexer and TPS62913RPUR buck converter were selected in part because of their compact surface-mount footprints, which optimize board space but necessitate precise soldering techniques. To ensure reliable solder joints, these components require reflow soldering, as hand-soldering is impractical for such small packages. The layout of the TPS62913RPUR closely follows the recommendations provided in the datasheet, including copper filled zones and proper placement of components specified. While both devices are highly efficient, the TPS62913RPUR may have a small thermal signature under continuous high-current operation. Proper copper pours and thermal reliefs are incorporated into the PCB layout to dissipate heat effectively and maintain safe operating temperatures.

| Current TPS62913RPUR Layout | Datasheet Recommended TPS62913RPUR Layout |
| --- | --- |

&nbsp; &nbsp; &nbsp; &nbsp;Decoupling and bypass capacitors are strategically positioned near both the USB-C and barrel jack input connectors as well as close to the TPS2121RUXR and TPS62913RPUR power pins. This placement helps stabilize the voltage at the entry points and at the devices themselves, minimizing ripple voltage and ensuring clean, reliable power under varying load conditions. Additional passive components for power conditioning are similarly arranged to optimize current paths and reduce localized thermal buildup. Thoughtful positioning of these components contributes to reliable operation and improved thermal performance.

&nbsp; &nbsp; &nbsp; &nbsp;The PCB has two status indicators directly connected to the 5V and 3.3V power rails, providing a visual confirmation of power presence on both supply lines. These LEDs allow users to quickly verify that the respective voltage rails are active and functioning correctly. Their inclusion supports troubleshooting, system validation, and general operational awareness.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the PCB power design balances flexibility, efficiency, and thermal management. By carefully selecting components, sizing traces and vias, following recommended layouts, and strategically positioning passive elements, the design delivers stable power to the system while maintaining safe operating temperatures and manufacturability.

**Component Selection and Labeling**

&nbsp; &nbsp; &nbsp; &nbsp;Component selection for the PCB was guided by considerations of electrical performance and form factor.

&nbsp; &nbsp; &nbsp; &nbsp;Edge connectors are standardized across the PCB to maintain consistency and ensure seamless compatibility among all subsystems. The following edge connectors are included on the board:

- JST 1mm pitch connectors are used for all peripheral digital connections, providing a consistent interface and supporting modular connectivity.
- Analog inputs are handled through screw-terminal connectors to provide a secure and reliable interface for the system. Each analog input includes a data line, a 3.3V supply, and a GND connection, duplicated for two separate channels. By using screw terminals for analog signals, the design prioritizes signal integrity and mechanical reliability, allowing ferrule-terminated wires to be securely connected while maintaining robust electrical contact.
- Female through-hole Pi Pico sockets are used to interface with the microcontroller, providing secure mechanical fastening and reliable electrical contact.
- Three 40-pin through-hole connectors with a standardized 2.54mm pitch are included on the board. One header is directly mapped to the MCU pins, allowing the user to access any pin as needed. The other two headers are connected in parallel: one is designed for a ribbon cable connection, and the other provides open access to the corresponding pins brought in by the ribbon.
- Dedicated 4-pin 2.54 mm connectors carry either 3.3 V or 5 V power lines, and an 8-pin 2.54 mm connector supplies multiple ground connections to ensure consistent power and reference distribution.
- The RF module's 5 V and ground connections are made via a JST HX connector, matching the module's design requirements.

&nbsp; &nbsp; &nbsp; &nbsp;Most components on the PCB use surface-mount technology (SMT) to achieve a clean, professional finish. The decision to use SMT was further reinforced by the voltage regulators and the voltage MUX, which require surface-mount packages. Adopting SMT for the majority of components ensures consistency in assembly and reliability across the board.

&nbsp; &nbsp; &nbsp; &nbsp;To help users with hand soldering, the selection of most components was determined by its form-factor, in which the 0805 (2012 Metric) package is ideal. Most resistors on the board are in this package, with a small number of exceptions required by electrical constraints. Capacitors follow the same standard, supporting consistent assembly and soldering practices. LEDs are standard red indicators in a 1206 (3216 Metric) package, which is easily hand solderable. They provide visual feedback for power and status signals on the board.

&nbsp; &nbsp; &nbsp; &nbsp;All components are clearly labeled with reference designators, which can be cross-referenced with the schematic for assembly and verification purposes. This ensures reliable assembly, simplifies testing and debugging, and supports maintainability over the life of the system. Thoughtful component selection and consistent labeling contribute to the overall usability, maintainability, and modularity of the System Interconnections PCB.

**Cable Selection**

&nbsp; &nbsp; &nbsp; &nbsp;To ensure reliable electrical connections and maintain modularity across the system, careful consideration was given to cable selection. Cables were chosen to match the standardized edge connectors on the PCB, support the required current, and provide secure mechanical fastening where applicable. The following outlines the cables used for digital connections and power distribution.

JST 1 mm Pitch Connectors

- 8-pin 1mm Pitch cable: Provides a standardized interface for power and digital connections. Includes locking mechanism for secure attachment.
- Four 4-pin 1mm Pitch cables: Used for peripheral digital connections. Locking tabs ensure reliable connections and prevent accidental disconnection.

Custom Ribbon Cable - 40-position IDC ribbon cable using 26 AWG wire

- Crimped to a 40-position rectangular receptacle connector.
- Powers the Raspberry Pi 4B via both 5V input pins in parallel, safely carrying the required current. 26 AWG wire has the capability of carrying 2.2A for chassis wiring \[11\].
- Supports mechanical fastening to ensure stable connection.

2-pin JST XH Cable - For RF module 5V and GND connection

- Locking connector ensures secure, reliable power delivery.
- Provides proper orientation to prevent misconnection.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the selected cables ensure that the System Interconnections PCB maintains electrical reliability, modularity, and safe current handling throughout the system. While not all edge connectors are actively used in the current configuration, they are included to demonstrate modularity and may be paired with the appropriate cables in future expansions or system modifications. Thoughtful cable selection and secure mechanical fastening support consistent performance, ease of assembly, and long-term maintainability of the system.

# **Interface with Other Subsystems**

&nbsp; &nbsp; &nbsp; &nbsp;The System Interconnections PCB provides a centralized platform for interfacing with power sources, the MCU, SBC, and peripheral modules. Detailed connectivity ensures reliable power delivery, standardized data transfer, and clear signal routing.

**Power Inputs**  
&nbsp; &nbsp; &nbsp; &nbsp;The PCB includes two primary power input terminals: a USB-C connector and a barrel jack. The USB-C connector is configured to accept up to 5V at 3A, with trace widths and CC pin configurations designed to safely handle this continuous current, as detailed in the Power Subsystem Detailed Design. The barrel jack supports 12V at 1.6A, with trace widths selected to accommodate continuous current without excessive voltage drop or heating.

**RF Module Interface**  
&nbsp; &nbsp; &nbsp; &nbsp;1mm pitch edge connectors are provided to interface with the RF module, supporting SPI, I2C, and UART communication protocols. These connections handle packets of data relating to Total Electron Content (TEC) and scintillation measurements. Additional pins are included for module state control. These are voltage-sensitive lines that allow the SBC to give or receive simple state information. A dedicated 5V power line and an extra 4-pin connector facilitate powering the module and accessing non-data signals.

**Raspberry Pi 4B GPIO Ribbon Connection**  
&nbsp; &nbsp; &nbsp; &nbsp;A 40-pin ribbon connector provides complete access to all GPIO pins of the Raspberry Pi 4B, including power and ground. The ribbon uses 26 AWG wire, capable of safely carrying the required current when supplying both 5V pins in parallel. The ribbon is kept as short as possible to minimize voltage drop and reduce signal noise.

**Peripheral 1 mm Pitch Connectors**  
&nbsp; &nbsp; &nbsp; &nbsp;Several 1 mm pitch edge connectors are included for peripheral modules excluding the RF module:

- LoRa module: interfaces with the MCU via SPI.
- OLED display: interfaces via I2C.
- Magnetometer: interfaces via I2C.
- Additional UART option: allows optional serial communication.

&nbsp; &nbsp; &nbsp; &nbsp;These connectors are positioned close together to reduce routing complexity and improve accessibility while maintaining the board's compact form factor.

**Analog Inputs**  
&nbsp; &nbsp; &nbsp; &nbsp;Two analog inputs are provided for simple voltage measurements. Each input includes a data line, a 3.3V supply, and a GND line, allowing direct connection to the MCU's ADC pins. Screw terminals are used to enable secure, ferrule-terminated wiring while preserving signal integrity.

**Raspberry Pi Pico Female Header**  
&nbsp; &nbsp; &nbsp; &nbsp;A female through-hole header maps all 40 pins of the Raspberry Pi Pico MCU to the PCB, providing full input and output access to GPIOs, ADCs, and power rails. This mapping enables flexible interfacing for debugging, prototyping, and expansion.

**Form Factor and Subsystem Integration**  
&nbsp; &nbsp; &nbsp; &nbsp;The board layout facilitates straightforward placement of connectors and modules while maintaining a compact form factor compatible with the enclosure, including mounting holes designed for M1 screws. Signal assignment and protocol routing have been optimized to support the software subsystems, providing a standardized and modular platform for system development.

# **3D Model of Custom Mechanical Components**


# **Buildable Schematic**

&nbsp; &nbsp; &nbsp; &nbsp;All schematics were created in KiCad Schematic Editor. The power portion was designed collaboratively with the Power Subsystem lead. It is essential to include the power schematic within the Interconnections Subsystem documentation because it contains direct references to the PCB silkscreen. In addition to the power schematic, an SBC and MCU header-mapping schematic is provided, which uses bus structures to reduce visual clutter. This schematic also includes two status LEDs, enabling the user to send a signal to verify proper system functionality.

&nbsp; &nbsp; &nbsp; &nbsp;The external connector schematic outlines all access points on the board and details how each pin is powered. The RF connectors include a normally open solder jumper to ensure that only one power source can supply the RF module at a time, preventing potential damage. All pins are clearly identified using net labels, which automatically carry over into the PCB editor and support a streamlined workflow.

# **Printed Circuit Board Layout**


Routing Layers

# **BOM**

| **Component** | **Total Price (\$US)** | **Quantity** | **Manufacturer** | **Part No.** | **Distributor** | **Distributor Part No.** | **Schematic Reference** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Headers** |     |     |     |     |     |     |     |
| 40 Pin Header | \$3.63 | 3   | Sullins Connector Solutions | PRPC022DFBN-RC | DigiKey | S2221EC-22-ND | SBCR1, SBCO1, J2 |
| 01x04 Header | \$0.34 | 2   | Wurth Elektronik | 61300411121 | DigiKey | 732-5317-ND | 5V_Pinout1, 3V3_Pinout1 |
| 01x08 Header | \$0.36 | 1   | Wurth Elektronik | 61300811121 | DigiKey | 732-5321-ND | GND_Pinout1 |
| RPiPico Female Header | \$1.66 | 2   | Wurth Elektronik | 61302011821 | DigiKey | 732-61302011821-ND | A2  |
| **Edge Connects** |     |     |     |     |     |     |     |
| Screw Terminal | \$2.08 | 2   | Phoenix Contact | 1935174 | DigiKey | 277-1578-ND | Analog_1, Analog_2 |
| RF Power Connect | \$0.12 | 1   | JST Sales America Inc. | S2B-XH-A | DigiKey | 455-S2B-XH-A-ND | 5V_GND_RF1 |
| 4pin Data Connect | \$3.50 | 7   | JST Sales America Inc. | SM04B-SRSS-TB | DigiKey | SM04B-SRSS-TB | I2C_RF1, UART_RF1, Adds_RF, UART_Additional2, I2C_Mag1, I2C_OLED1 |
| 6pin Data Connect | \$1.34 | 2   | JST Sales America Inc. | SM06B-SRSS-TB | DigiKey | SM06B-SRSS-TB | SPI_RF1 |
| 8pin Data Connect | \$1.56 | 2   | JST Sales America Inc. | SM08B-SRSS-TB | DigiKey | SM08B-SRSS-TB | SPI_LoRa1 |
| **Cables** |     |     |     |     |     |     |     |
| Ribbon Terminal | \$5.00 | 2   | 3M  | 89140-0001 | DigiKey | MSC40A-ND | N/A |
| Ribbon Cable | \$4.26 | 1   | 3M  | 3811/40 300 | DigiKey | 3M157799-300-ND | N/A |
| 8pin Data Cable | \$1.98 | 1   | JST Sales America Inc. | A08SR08SR30K152 | DigiKey | 455-3016-ND | N/A |
| 4pin Data Cable | \$6.25 | 5   | Adafruit Industries LLC | 4401 | Adafruit Industries LLC | STEMMA QT / Qwiic JST SH 4-Pin Cable - 200mm Long | N/A |
| RF Power Cable | \$0.95 | 1   | Adafruit Industries LLC | 4872 | DigiKey | 1528-4872-ND | N/A |
| **Modules** |     |     |     |     |     |     |     |
| Magnetometer | \$5.95 | 1   | Adafruit Industries LLC | 5579 | Adafruit Industries LLC | Adafruit Triple-axis Magnetometer - MMC5603 - STEMMA QT / Qwiic | N/A |
| OLED Display | \$9.99 | 1   | ELEGOO | EL-SM-008 | Amazon | ELEGOO 3PCS 0.96 Inch OLED Display Screen Module Compact Self-Luminous SSD1306 I2C Display Mini Screens for Arduino Projects | N/A |
| Raspberry Pi Pico H Presoldered | \$5.00 | 1   | Raspberry Pi | SC0917 | DigiKey | 2648-SC0917-ND | N/A |
| **PCB Printing** |     |     |     |     |     |     |     |
| PCBWay Print | \$50.00 | 1   | PCBWay | N/A | PCBWay | N/A | N/A |
| **TOTALS** | **\$103.97** | **36** |     |     |     |     |     |

| **Component** | **Purchasing URL** |
| --- | --- |
| **Headers** |     |
| 40 Pin Header | <https://www.digikey.com/en/products/detail/sullins-connector-solutions/PRPC022DFBN-RC/2775472?gclsrc=aw.ds&gad_source=1&gad_campaignid=17336967819&gbraid=0AAAAADrbLliY04271c8edlK7l9l_11HhJ&gclid=CjwKCAiA24XJBhBXEiwAXElO30QyIcSJV-FWfXQw7-eRvBJV-lLtoMTNtQWI8imqFnSzpjX7xPhSzRoCI30QAvD_BwE> |
| 01x04 Header | <https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/61300411121/4846827> |
| 01x08 Header | <https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/61300811121/4846839> |
| RPiPico Female Header | <https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/61302011821/16608603> |
| **Edge Connects** |     |
| Screw Terminal | <https://www.digikey.com/en/products/detail/phoenix-contact/1935174/568615> |
| RF Power Connect | <https://www.digikey.com/en/products/detail/jst-sales-america-inc/S2B-XH-A/1651055?gclsrc=aw.ds&gad_source=1&gad_campaignid=20470400566&gbraid=0AAAAADrbLliI2dNrkApeOglQsNs-J2tBO&gclid=Cj0KCQiAiebIBhDmARIsAE8PGNIb3jJudNuc1iXC2Z0QA5yOkA52DsRw1ld4gJulXVZiXKgrhLT5OooaAuKYEALw_wcB> |
| 4pin Data Connect | <https://www.digikey.com/en/products/detail/jst-sales-america-inc/SM04B-SRSS-TB/926710> |
| 6pin Data Connect | <https://www.digikey.com/en/products/detail/jst-sales-america-inc/SM06B-SRSS-TB/926712> |
| 8pin Data Connect | <https://www.digikey.com/en/products/detail/jst-sales-america-inc/SM08B-SRSS-TB/926714> |
| **Cables** |     |
| Ribbon Terminal | <https://www.digikey.com/en/products/detail/3m/89140-0001/229687?utm_source=chatgpt.com> |
| Ribbon Cable | <https://www.digikey.com/en/products/detail/3m/3811-40-300/1107544?utm_source=chatgpt.com> |
| 8pin Data Cable | <https://www.digikey.com/en/products/detail/jst-sales-america-inc/A08SR08SR30K152B/6009392> |
| 4pin Data Cable | <https://www.adafruit.com/product/4401> |
| RF Power Cable | <https://www.digikey.com/en/products/detail/adafruit-industries-llc/4872/13922052?utm_source=chatgpt.com> |
| **Modules** |     |
| Magnetometer | <https://www.adafruit.com/product/5579?gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvRTrY9zAG_e4utlMFfn0IrB5&gclid=Cj0KCQiAiebIBhDmARIsAE8PGNIaka8AI4I5PPEjeb8TQ8A6f_uAWlyQIzea-UpTVdZvFxQfw-mDhxIaAoCmEALw_wcB> |
| OLED Display | <https://www.amazon.com/ELEGOO-Display-Compact-Self-Luminous-Projects/dp/B0D2RMQQHR> |
| Raspberry Pi Pico H Presoldered | <https://www.digikey.com/en/products/detail/raspberry-pi/SC0917/16608257?gclsrc=aw.ds&gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlgeclh4LX6MHsytZH7fu5_1S&gclid=CjwKCAiA24XJBhBXEiwAXElO37mx-2zfPY0xFvAhZIXexCOY7H_v260vNOi58iN0q4uwZs4vJ6cSIhoCCQQQAvD_BwE> |
| **PCB Printing** |     |
| PCBWay Print | <https://www.pcbway.com/orderonline.aspx> |

# **Analysis**

&nbsp; &nbsp; &nbsp; &nbsp;The System Interconnections subsystem fulfills all specifications and constraints defined for the design. The selected 4-layer FR-4 stackup, with dedicated ground and power planes, satisfies the PCB stackup specification by supporting clean routing and reliable performance. The power design meets all requirements for dual-input operation, incorporating overvoltage protection, reverse-polarity protection through the full-bridge rectifier, proper decoupling, and automatic source prioritization via the TPS2121 power multiplexer. Both regulated 5V and 3.3V rails are distributed across the PCB with appropriately sized traces, vias, and copper fills.

&nbsp; &nbsp; &nbsp; &nbsp;Modularity and expansion requirements are addressed through standardized JST 1.0mm digital connectors, screw-terminal analog inputs, three 40-pin headers for parallel SBC/MCU expansion, and additional unused connectors included for future system growth. Routing constraints are satisfied through the use of a continuous ground plane, minimized loop areas, ground stitching vias, and careful separation of digital, analog, and power paths to ensure signal integrity and minimize EMI.

&nbsp; &nbsp; &nbsp; &nbsp;Trace, via, and external wire gauges are selected based on calculated current requirements, supported by thermal considerations and manufacturer-validated calculators. All connectors, components, and signal entry points are clearly labeled on the schematic and PCB silkscreen to support assembly, debugging, and long-term maintainability. The board footprint of 90x95mm meets the Enclosure subsystem's mechanical constraints, and all footprints, clearances, and pad sizes comply with PCBWay's manufacturability guidelines, verified through KiCad's DRC.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the design satisfies all specifications and constraints through careful material selection, rigorous power and routing strategy, standardization of interfaces, and attention to manufacturability and system modularity.

# **References**

\[1\] "Eliminate EMI and Signal Integrity Issues in Multi-Board PCB Designs," _Altium_, Apr. 11, 2025. <https://resources.altium.com/p/emi-and-signal-integrity-multi-board-pcb-designs> (accessed Nov. 24, 2025).

\[2\] "Using an IPC-2221 PCB Clearance Calculator for High Voltage Design," _Altium_, Jan. 17, 2020. <https://resources.altium.com/p/using-an-ipc-2221-calculator-for-high-voltage-design>

\[3\] "I2C vs SPI vs UART - Introduction and Comparison of their Similarities and Differences," _Total Phase Blog_, Dec. 2021. <https://www.totalphase.com/blog/2021/12/i2c-vs-spi-vs-uart-introduction-and-comparison-similarities-differences/?srsltid=AfmBOoo_TYHNvEx6r0LQJao635syI8aqLDuQDlpBfUg-8FmeE7A8CSDh> (accessed Nov. 24, 2025).

\[4\] "PCB Capabilities - Custom PCB Prototype the Easy Way - PCBWay," [_www.pcbway.com_](https://www.pcbway.com). <https://www.pcbway.com/capabilities.html>

\[5\] U. Waseem, "PCB Material: A Comprehensive Guide to Understanding and Choosing the Right Materials," [_www.wevolver.com_](https://www.wevolver.com). <https://www.wevolver.com/article/pcb-material>

\[6\] "Introduction to 4-Layer PCB," _Allpcb.com_, 2024. <https://www.allpcb.com/blog/pcb-knowledge/4-layer-pcb.html>

\[7\] "PCB Trace Width Conversion Calculator | DigiKey," [_www.digikey.com_](https://www.digikey.com). <https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-pcb-trace-width>

\[8\] Best Technology, "PCB Via Current Calculator," _PCB & MCPCB - Best Technology | More Technical Details & News on PCB, MCPCB & Ceramic PCB from Best Technology_, Aug. 20, 2024. <https://www.bestpcbs.com/tools/PCB-Via-Current-Calculator.html> (accessed Nov. 24, 2025).

\[9\] T. S. Team, "Understanding Signal Integrity in PCBs," _Sierra Circuits_, Aug. 11, 2020. <https://www.protoexpress.com/blog/understanding-signal-integrity/> (accessed Nov. 24, 2025)

\[10\] TnTech-ECE, "F25_Team6_SpaceWeatherStation/Reports at main · TnTech-ECE/F25_Team6_SpaceWeatherStation," _GitHub_, 2025. <https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/tree/main/Reports> (accessed Nov. 24, 2025).

‌\[11\] "American Wire Gauge Chart and AWG Electrical Current Load Limits table with ampacities, wire sizes, skin depth frequencies and wire breaking strength," _Powerstream.com_, 2019. <https://www.powerstream.com/Wire_Size.htm>

\[12\] OpenAI, "ChatGPT," _ChatGPT_, 2025. <https://chatgpt.com/>

‌
