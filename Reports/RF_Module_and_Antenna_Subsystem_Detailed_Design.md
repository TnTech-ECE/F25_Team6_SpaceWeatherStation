# **RF Module and Antenna Subsystem Detailed Design**

## **Function of the Subsystem**

The overall function of the Antenna and RF Module Subsystem is to use GNSS signals to compute Total Electron Content (TEC) measurements in the atmosphere. The calculated values and other recorded data is to then be sent to the Data Storage System to be further processed and stored. This subsystem shall meet several constraints given in the following section and shall align with the Conceptual Design description.

## **Specifications and Constraints**

The following is a list of constraints applicable to this subsystem. The proposed solution shall meet or exceed these requirements.

- The subsystem shall use L1 and L5 GNSS signals to compute the TEC measurements, as requested by the customer.
- The subsystem shall measure the pseudorange and carrier phase of the L1 and L5 signals from valid GNSS satellites, as well as the satellite's azimuth angle, as they are required to compute the TEC measurements along the signal path between the receiver and the transmitting satellite \[1\].
- The subsystem shall compute the TEC measurement from the above data on the Single Board Computer (SBC), a main component of the Data and Storage Subsystem.
- The computed TEC measurements shall fall within 15% of credible reference TEC data
- The subsystem shall record identifying information of each connected satellite and transfer that data along with the computed TEC measurement to the Data and Storage Subsystem.
- The subsystem shall comply with FCC Part 15 Class B (or applicable international equivalent) to ensure that it does not emit harmful RF interference, adhering to regulatory and ethical requirements for protecting GNSS spectrum and public safety \[2\].
- The subsystem shall remain under the \$375 budget limit.

## **Overview of Proposed Solution**

The proposed solution for this subsystem is to use a GNSS RF module with a dual-tuned patch antenna that can receive L1/L5 GNSS signals, extract the needed signal data, and transfer the data to the SBC of the Data and Storage Subsystem. The SBC will then compute the TEC computations, which will be stored by the Data and Storage Subsystem along with other satellite identification data.

__Figure 1:__ _Antenna and RF Module Hardware Diagram_

## **TEC Computation Method**

For more information on what TEC is and the physics behind it, refer to the Project Proposal Document.

Before TEC computation can be discussed, it is necessary to define what a signal's pseudorange is, as it is used in determining TEC. A signal's pseudorange, P, is the estimated distance between a transmitter and receiver, computed by multiplying the difference of the received and sent timestamps of the transmitted signal by the speed of light, c \[3\].

(1)

The difference between two signals' pseudoranges along the same path can be rewritten as the following formula, with respect to the TEC of the pseudorange \[3\]:

(2)

In the above formula, each frequency and pseudorange pair correspond to a signal that travels along the same path between the transmitter and receiver. The above equation can be rewritten as follows \[3\]:

(3)

Equation 3 clearly shows that if the pseudorange and frequency of two separate signals transmitted across the same path is known, then the straight-line TEC for that path can be calculated. This TEC value is referred to as the slant TEC, as in reference to GNSS transmitters and receivers on the earth, the path the transmissions taken are "slanted" with respect to a vertical path through the atmosphere \[3\].

Applying these principles, it is necessary to select an RF module that can determine the pseudoranges for two separate signal frequencies transmitted from GNSS satellites. The constraints of this subsystem, as discussed in the above section, require the module to receive the L1 and L5 GNSS frequencies specifically. Additionally, to record the location of the path of each TEC measurement, the module will need to be able to determine the position of the receiver, as well as the position of any measured satellites.

The RF module that has been selected to meet these constraints is the SparkFun GNSS-RTK L1/L5 NEO-F9P Breakout Board. This module contains a u-blox NEO-F9P chip, which is an L1/L5 GNSS receiver which boasts centimeter level accuracy, capable of connecting to four concurrent GNSS systems \[4\]. This module can easily measure the pseudorange and carrier phase of received GNSS signals, as well as determine satellite identification and positional data, making it ideal for gathering information for TEC measurements \[5\]. This module has configurable interfaces for UART, SPI, and I2C connections, allowing it to easily connect and communicate with a chosen SBC of the data storage system \[6\].

__Figure 2:__ _SparkFun DNSS-RTK L1/L5 Breakout NEO-F9P_

The antenna that has been selected for this subsystem is the u-blox ANN-MB1 L1/L5 multi-band high precision GNSS antenna. This antenna is tuned to the L1 and L5 GNSS frequencies, allowing the subsystem to receive both signals concurrently. It is also a patch antenna, which allows for affordability and quality of the signal. This antenna is also fully compatible with the NEO-F9P module, making it ideal for this solution \[7\].

__Figure 3:__ _ANN-MB1 u-blox antenna_

## **Interface with Other Subsystems**

The RF Module and Antenna Subsystem shall connect to the Power subsystem and the Data and Storage Subsystem via the System Interconnections Subsystem, all whilst being housed within the Enclosure Subsystem. Below is a diagram of the connections between the hardware of the RF Module and Antenna Subsystem and the other subsystems.


__Figure 4:__ _Subsystem Connections_

All the connections between the subsystems of this project run through the System Interconnections Subsystem via a central PCB. The signals that shall connect the RF Module and Antenna Subsystem to the rest of the project and the nature of the data contained within are given below.

### **UART Serial Connection**

The RF Module of the RF Module and Antenna Subsystem shall connect to the Data and Storage Subsystem's SBC with a serial UART connection. This connection shall be used to transmit the pseudorange, carrier phase, and other GNSS positional data from the NEO-F9P module to the SBC. Additionally, the SBC shall send commands to the NEO-F9P module through this same connection.

For the UART connection to work properly, both devices must have their baud rates set to within 10% of each other \[8\]. The NEO-F9P documentation recommends the baud rate for the module to be set not less than 38400 baud and no larger than 921600 baud \[5\]. Therefore, the selected baud rate for the connection shall be between these values.

**UART Serial Connection: UBX Protocol**

The NEO-F9P uses the UBX protocol to communicate with host computers. This is a proprietary protocol designed by u-blox, the manufacturers of the NEO-F9P. This protocol sends frames consisting of two sync characters, a message class, a message ID, the length of the payload, the said payload, and a checksum. Each frame is formatted as in the following diagram from the NEO-F9P documentation \[5\]:



__Figure 5:__ _UBX Frame Structure_

The first section of the frame, the preamble, consists of two synch characters. These signify the beginning of the frame. The next segment, the message class and ID, signify what kind of message is contained in the frame. The message class identifies what group of messages the contained payload aligns with. The message ID defines what specific message is in the payload. Finally, the frame ends with a checksum, which is used to verify that the received data is valid \[5\].

The messages that can be sent over the UBX protocol range in function, from configuration commands to information transmission requests \[5\]. Messages of this protocol shall be sent between the NEO-F9P and the SBC through the UART connection to configure the NEO-F9P and to transmit required data to the SBC for TEC computation.

### **GPIO Control Pins**

The NEO-F9P's control pins shall also be connected to some of the Data and Storage Subsystem's SBC GPIO pins to allow for more control over the NEO-F9P by the project. The only control pin that will be connected to the SBC is the RESET pin. This pin will trigger a cold start if held low for at least 100ms \[6\].

### **Power Signal**

The NEO-F9P module shall be powered by a 5V connection provided by the Power System. The NEO-F9P board supplies the attached active antenna with power when supplied with a 5V power source, so the antenna will not need a separate power connection.

## **Buildable Schematic**

The buildable schematic of this subsystem can be found in the Detailed Design Specifications of the System Interconnections Subsystem, as the specific PCB connections fall under the envelope of that subsystem.

## **Flowchart**

The general operational flow of the RF Module and Antenna Subsystem is as follows.

- On bootup, the SBC shall send required configuration commands to the RF module. It is assumed that certain settings, such as baud rate, have already been configured correctly on the NEO-F9P.
- When the overall system is ready, the SBC will poll the NEO-F9P via a UBX message for the locational data of the measurement device.
- Once the locational data of the receiver has been acquired, the SBC will poll the NEO-F9P via UBX for connected satellites' identification, position, signal type, pseudoranges, and carrier phases. The received data shall then be stored in a vector of variable structures and analyzed by the SBC to determine what satellites have both L1 and L5 signal data.
- The data for each measured satellite which includes L1 and L5 signal data shall then be used to compute TEC measurements for those select satellites, following formula 3.
- Finally, the data shall be passed to the Data and Storage Subsystem section of the operational program to be further processed and stored.
- The RF Module and Antenna Subsystem shall repeat step 3 of this operational flow onward when requested to by the rest of the system.

Figure 6: _Operational Flowchart_

**Bill of Materials**

| Component | SparkFun GNSS-RTK L1/L5 Breakout - NEO-F9P (Qwiic) | ANN-MB1 L1/L5 Multi-Band GNSS antenna |
| --- | --- | --- |
| Manufacturer | SparkFun Electronics | u-blox |
| Part # | GPS-23288 | ANN-MB1-00 |
| Distributor | SparkFun Electronics | DigiKey |
| Dist. Part # | GPS-23288 | 672-ANN-MB1-00-ND |
| Quantity | x1  | x1  |
| Price | \$259.95 | \$60.00 |
| URL | <https://www.sparkfun.com/sparkfun-gnss-rtk-l1-l5-breakout-neo-f9p-qwiic.html?gad_source=1&gad_campaignid=17479024039&gclid=Cj0KCQiAoZDJBhC0ARIsAERP-F_VOQB7xlmAha4Z4P-1NanVYHGOM7iVvMnycKp83FkyJxqAhj6OTCcaAqU6EALw_wcB> | <https://www.digikey.com/en/products/detail/u-blox-america-inc/ANN-MB1-00/14835875?curr=usd&utm_campaign=buynow&utm_medium=aggregator&utm_source=octopart> |
| Total Cost: |     | \$319.95 |

Table 1: _Bill of Materials_

## **Analysis**

The RF Module and Antenna Subsystem's function is to acquire GNSS signals and compute Total Electron Content (TEC) measurements of the ionosphere. The subsystem must meet functional requirements and operate within defined constraints, including measurement accuracy, signal compatibility for L1/L5 GNSS frequency bands, and a budget ceiling of \$375. The following analysis will show the proposed solution and its components meet the subsystem's objectives.

### **Functional Requirements**

The subsystem must:

- Receive L1 and L5 GNSS signals
- Measure pseudorange and carrier phase for L1 and L5 signals
- Record satellite identification and position
- Compute TEC accurately using the received signal data
- Transfer computed TEC and associated data to the Data and Storage Subsystem
- Comply with FCC Part 15 Class B to ensure that it does not emit harmful RF interference
- Operate within a budget of \$375

Requirements 1, 2, 3, 5, 6, and 7 are satisfied by the chosen RF module and antenna. They can receive L1 and L5 signals, measure pseudorange and carrier phase, and record satellite positional and identification data. The UART interface supported by the RF module, as well as the UBX protocol, allow for fast and easy communication of the required data to the SBC. As shown in the BOM section of this document, these components are also well within the budget.

Requirement 4 is satisfied by the methodology described in the TEC Computation Method subsection of this document, as well as the operational flow description in Flow section of this document. The proposed TEC computation in equation 3 is easily performed with the pseudorange data measured by the RF module, and the associated satellite data is easily received by the Data and Storage Subsystem along with the TEC computation.

| Constraint | Design Fulfillment | Evidence / Justification |
| --- | --- | --- |
| Use of L1/L5 signals | ANN-MB1 antenna + NEO-F9P supports both L1 and L5 frequencies | NEO-F9P datasheet confirms dual-frequency GNSS reception \[4\]; ANN-MB1 is tuned for L1/L5 \[7\] |
| Measure pseudorange & carrier phase | NEO-F9P provides both measurements for all visible satellites | Verified in NEO-F9P Interface Description and Integration Manual \[6\] |
| Compute TEC on SBC | Subsystem sends raw pseudorange & phase data to SBC | Data transfer via UART ensures SBC receives all required inputs |
| Record satellite ID & positional data | NEO-F9P outputs satellite ID, elevation, and azimuth | UBX messages include this data; operational flow captures this before TEC computation |
| Budget ≤ \$375 | NEO-F9P \$259.95 + ANN-MB1 \$60 = \$319.95 | Total cost is \$55.05 below budget limit |

Table 2: _Design Analysis with respect to Constraints_

The proposed Antenna and RF Module Subsystem design fully meets the functional requirements and constraints. Therefore, the proposed design is highly likely to accomplish its intended function within the overall system.

## **References**

\[1\] M. A. S. R. A. Zaini, "Determination of Ionospheric Total Electron Content (TEC): Phase Measurement Based on Levelling Technique," Faculty of Electrical Engineering, Universiti Teknologi MARA, Shah Alam, Selangor, Malaysia. \[Online\]. Available: <https://ir.uitm.edu.my/id/eprint/40459/1/40459.pdf>. \[Accessed: Dec. 2, 2025\].

\[2\] Federal Communications Commission. _Title 47, Code of Federal Regulations, Part 15 - Radio Frequency Devices, Subpart B: Unintentional Radiators_. Washington, DC: U.S. Government Publishing Office, 54 FR 17714 (Apr. 25, 1989), as amended.

\[3\] E. D. Lopez, R. E. Hidalgo, and M. J. Carrera, "Preliminary mapping of ionospheric total electron content (TEC) over Ecuador using global positioning system (GPS) data," arXiv preprint arXiv:2403.19053, 2024. \[Online\]. Available: <https://arxiv.org/abs/2403.19053>. \[Accessed: Dec. 2, 2025\].

\[4\] u-blox AG, "NEO-F9P Product Summary," UBX-21043595-R05. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P//assets/component_documentation/NEO-F9P_ProductSummary_UBX-21043595.pdf>. \[Accessed: Dec. 2, 2025\].

\[5\] u-blox AG, "u-blox F9 HPG L1L5 1.40 - Interface Description," Interface Description UBX-23006991-R02. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P/assets/component_documentation/u-blox-F9-HPG-L1L5-1.40_InterfaceDescription_UBX-23006991.pdf>. \[Accessed: Dec. 2, 2025\].

\[6\] u-blox AG, "NEO-F9P - High Precision GNSS Module: Integration Manual," Document UBX-22028362-R03. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P/assets/component_documentation/NEO-F9P_IntegrationManual_UBX-22028362.pdf>. \[Accessed: Dec. 2, 2025\].

\[7\] u‑blox AG, "ANN‑MB1: L1/L5 Multi‑band High Precision GNSS Antenna - Data sheet," Document UBX‑21005551-R04. \[Online\]. Available: <https://content.u-blox.com/sites/default/files/ANN-MB1_DataSheet_UBX-21005551.pdf>. Accessed: Dec. 2, 2025.

\[8\] "Basics of UART Communication," CircuitBasics. \[Online\]. Available: <https://www.circuitbasics.com/basics-uart-communication/>. \[Accessed Dec. 2, 2025\].

\[9\] OpenAI, "ChatGPT (GPT-5-mini) \[Large language model\]," OpenAI, San Francisco, CA, USA, Dec. 2, 2025. \[Online\]. Available: <https://chat.openai.com/>. \[Accessed Dec. 2, 2025\].
