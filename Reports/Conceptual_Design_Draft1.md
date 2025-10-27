<h1 style="font-size:40px;">F25 Team 6 Space Weather Station Conceptual Design</h1>

# **Introduction**

&nbsp; &nbsp; &nbsp; &nbsp;Global reliance on communication, navigation, and positioning systems makes society increasingly vulnerable to disturbances in the ionosphere, where total electron content (TEC) refracts, delays, and disrupts radio signals. These disturbances reduce the accuracy and effectiveness of global navigation satellite system (GNSS) services, disrupting critical infrastructure in aviation, maritime operations, telecommunications, and everyday devices. Although anticipation of TEC interference could be limited by large amounts of accurately observed data, existing monitoring systems are often costly, technically complex, stationary, and geographically limited. This creates a barrier to broader participation in ionospheric research and limits the availability of distributed TEC measurements needed for accurate modeling.

&nbsp; &nbsp; &nbsp; &nbsp;To address this challenge, Team 6 is developing a low-cost, modular, and replicable prototype capable of measuring TEC from dual-frequency GNSS signals. The system integrates an antenna, receiver, processing unit, and expandable modules within a single housing compartment to support mobility, while remaining under \$1,000. Propagation of the prototype is supported by thorough documentation for seamless hobbyist replication. By normalizing access to TEC measurement, the project expands opportunities for education, grassroots research, and innovation. Moreover, it contributes to a distributed global database of ionospheric conditions, enhancing collective understanding of space weather and its implications for modern infrastructure.

&nbsp; &nbsp; &nbsp; &nbsp;This document provides a structured framework for developing and presenting a conceptual design. It begins by defining a clearly formulated problem, identifying constraints, and proposing a comprehensive high-level solution, balancing performance, cost, and feasibility. Through comparative analysis, the document ensures that each potential approach has been critically evaluated before selecting the most effective design method. 

&nbsp; &nbsp; &nbsp; &nbsp;The conceptual design emphasizes clarity, completeness, and professionalism. It requires detailed system representations, including hardware block diagrams, operational flowcharts, and well-defined subsystem specifications supported by “shall” statements. All of this is done with the intention of ensuring each part of the system is measurable, testable, and functionally independent. 

&nbsp; &nbsp; &nbsp; &nbsp;Additionally, this document integrates ethical, professional, and standards-based considerations into the design process, guaranteeing adherence and accountability to universal standards. It concludes with a refined resource plan encompassing the project budget, division of labor, and a Gantt chart representing the proposed timeline. This provides a solid foundation to successfully transition into the detailed design phase. 

# **Restating the Fully Formulated Problem**

&nbsp; &nbsp; &nbsp; &nbsp;As discussed in Team 6's project proposal, modern society's dependence on communication, navigation, and timing systems makes it increasingly vulnerable to disruptions in the ionosphere. Variations in TEC can delay or distort GNSS radio signals \[1\]. These ionospheric disturbances undermine the accuracy and reliability of GNSS-based services supporting aviation, maritime operations, telecommunications, and numerous critical infrastructures. Therefore, accurate measurement of TEC is essential for understanding, predicting, and minimizing these effects.

&nbsp; &nbsp; &nbsp; &nbsp;Existing TEC monitoring systems are largely cost-prohibitive, technically complex, and stationary, restricting participation to well-funded institutions and leaving broad geographic regions without adequate observation coverage. This gap limits the availability of distributed ionospheric data necessary to refine predictive models and improve the resilience of global navigation systems.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 proposes the design and development of a low-cost, modular, and portable TEC measurement device, capable of acquiring dual-frequency GNSS signals to compute TEC directly. The fully formulated objective is to deliver an affordable (< \$1,000) and replicable prototype that integrates a dual-tuned antenna, GNSS receiver, processing unit, storage system, and power subsystem. All of which will be contained within a compact, field-deployable enclosure. The system will support open-source documentation enabling replication by educators, researchers, and hobbyists, fostering widespread participation in ionospheric data collection.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has placed multiple specifications, requirements, and constraints on the solution due to customer standards, in-depth analysis of existing solutions, and regulatory compliance.

- The chosen design shall consist of a GNSS signal processing unit and a dual-tuned antenna capable of receiving L1/L2 or L1/L5 GNSS signals.
  - TEC values are computed by calculating the delay between two captured GNSS signals. These measurements require an RF module, essential for conditioning and digitizing the received signals after which the data can be used in TEC calculations. TEC can only be derived if raw pseudo range and carrier phase data are collected and processed at high precision. Without this module, the system would fail to meet its primary function as a scientific measurement instrument \[1, 2\].
  - Dual-frequency reception (GPS L1/L2 or L1/L5, Galileo E1/E5, etc.) is mandated by GNSS and ionospheric research standards for accurate differential delay computation. Supporting multiple constellations increases data density and temporal resolution of TEC measurements \[1\].
- The chosen design shall consist of readily available components, able to be replaced or substituted without an extensive system of redesign.
  - The requirement for readily available components stems from customer specifications, allowing for interchangeability and cost-effective repairs. \[1\]
  - Modularity is a primary objective for the entire design process, including additional free input ports for user-driven expansions. \[1\]
- The chosen design shall consist of a data storage device capable of reliably recording high-resolution TEC measurements. Along with system health metrics, additional sensor data, and any additional applications.
  - An appropriate storage system ensures sufficient space for long-term raw GNSS data logging (often several megabytes per minute). The storage requirement originates from customer specifications, research, and ethical engineering standards for continuous 24-hour (or multi-day) operation without manual data offload. It ensures data integrity and prevents loss due to insufficient storage capacity. Furthermore, maintaining complete, timestamped datasets supports scientific transparency and reproducibility \[1\].
- The chosen design shall consist of a single-board computer and/or microcontroller.
  - This requirement originates from customer needs for a programmable and modular system supporting future expansions. A processing platform is essential for data acquisition, timestamping, and device control. The choice between an SBC (e.g., Raspberry Pi 5, Raspberry Pi 02W) and a microcontroller (e.g., STM32) allows for either high-performance processing or low-power efficiency, depending on design preferences \[1, 3\].
- The chosen design shall consist of a battery capable of recharging via wall main or solar panel with necessary electrical fault protections.
  - A rechargeable battery is essential for field autonomy and continuous operation independent of grid power. The inclusion of a rechargeable battery reflects an ethical and environmental concern, promoting sustainability by reducing single-use power sources. The requirement for safe operation and overcharge protection arises from safety engineering standards (IEEE/IEC) \[4, 5, 6\].
- The chosen design may have the capability to measure ionospheric scintillation events.
  - This specification enhances the impact of the data collected and provides more insight for the scientific community concerning ionospheric conditions.
- The chosen design shall consist of components that have a combined cost not exceeding \$1,000.
  - Cost constraints arise from the customer's specification to maintain inexpensive total component costs, ensuring accessibility to educators and hobbyists. This also follows the HamSci Initiative of producing affordable space weather stations \[1\].
- The chosen design shall record data that is able to produce measurements within 15% of credible reference TEC data
  - This requirement is guided by academic benchmarking and comparison of previous solutions \[7\].
- The chosen design shall have a sufficient sample rate capable of producing measurements meeting all accuracy constraints
  - This constraint stems from customer and supervisor specifications. The sample rate shall log data at an appropriate rate for capturing significant variations in TEC, while maintaining efficient storage and analysis. \[1\]
- The chosen design may monitor the quality of GNSS signals being recorded, including signal-to-noise ratio (SNR) and carrier-to-noise density (C/N₀) for all tracked GNSS satellites
  - The customer specification for GNSS signal quality being recorded and evaluated originates from established GNSS performance monitoring standards used in geodesy and ionospheric research. SNR and C/N₀ are the quantitative measures of signal integrity that directly influence TEC accuracy. Monitoring these parameters ensures collected TEC data meets the minimum scientific fidelity required for meaningful comparison with reference datasets such as those from IGS or NOAA ionospheric monitoring stations. Implementing this requirement aligns the system with ITU and GNSS ICD standards, who specify signal quality parameters for professional-grade receivers. \[8\]
- The chosen design shall include necessary and detailed documentation for efficient and accurate replication.
  - Detailed documentation satisfies customer specifications and actively supports students, researchers, hobbyists, and the larger scientific community. Inclusion of comprehensive schematics, software and hardware manuals, and wiring diagrams ensures system replicability without the need for proprietary tools or specialized expertise. Comprehensive documentation moves the TEC measurement device beyond a prototype, becoming a replicable open-source platform for broader adoption. \[1, 9\]
- The chosen design shall meet all applicable ITU standards
  - Constraint originates from customer specification and compliance with ITU standards, which prohibit unauthorized transmission within GNSS bands. Therefore, the system shall operate exclusively as a passive receiver. \[1\]
- The chosen design shall operate for short-range wireless communication within approved ISM bands and comply with the applicable regional standards for chosen frequencies.
  - Constraint originates from customer specifications, including a server-based system to remotely analyze TEC data.
- The chosen design shall meet IPx4 waterproofing standards, thermal protection guidelines, and have the capability to be safely mounted.
  - Environmental and safety constraints stem from engineering ethics and public safety standards, requiring IPx4 waterproofing, thermal protection, and secure mounting to prevent damage or injury during operation. \[10\]

&nbsp; &nbsp; &nbsp; &nbsp;In summary, the specifications, requirements, and constraints established by Team 6 form a foundational design framework, ensuring the TEC measurement system achieves scientific credibility and practical implementation. Each requirement spanning GNSS signal processing and antenna choice to data storage, power autonomy, and environmental durability, has been developed through careful alignment with customer expectations, existing industry standards, and ethical engineering practices. Collectively, these constraints guarantee the device will operate as a scientifically valid, robust, and sustainable research instrument.

&nbsp; &nbsp; &nbsp; &nbsp;The inclusion of a dual-frequency GNSS receiver and high-capacity storage directly supports accurate and reproducible ionospheric data collection. Modular computing architecture and a 12V rechargeable power system promote flexibility and long-term field autonomy. Economic and regulatory considerations, such as a budget limit \$1,000 and adherence to ITU and safety standards, ensure that the project remains accessible, compliant, and environmentally responsible. Finally, by requiring the system's measured TEC values to remain within 15% of established reference data, the design establishes a clear benchmark for scientific validity and performance verification.

&nbsp; &nbsp; &nbsp; &nbsp;Together, these constraints define not only the engineering boundaries of the solution but also its broader mission, to deliver a reliable, affordable, and ethically engineered platform for advancing open ionospheric research.

# **Comparative Analysis of Potential Solutions**

&nbsp; &nbsp; &nbsp; &nbsp;The project proposal previously identified three established TEC measurement systems. Each system was developed to meet distinct objectives informing their respective designs. What follows is a comparative analysis of design methods and an evaluation of off-the-shelf components to determine the most suitable elements for Team 6's prototype.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6's stated prototype objective:

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 aims to design and implement a low cost, modular prototype system capable of directly measuring ionospheric TEC using dual signal GNSS-based signal observations. The prototype will emphasize accuracy, reliability, and deployability. It will integrate essential functionality for signal acquisition, system control and processing, data logging, and power management. The system will be optimized for efficient operation in field environments and implemented at a total cost not exceeding \$1,000.

&nbsp; &nbsp; &nbsp; &nbsp;The following sections examine design considerations for signal reception, central processing and control systems, storage, power, modularity, and enclosure. The goal being identification of components and design elements that support the prototype objective.

## **Signal Reception**

&nbsp; &nbsp; &nbsp; &nbsp;The prototype will utilize dual-frequency GNSS signal observations to directly measure TEC with high accuracy. To achieve this, a dual-tuned Right-Hand Circularly Polarized (RHCP) antenna is proposed. RHCP is predominantly used for GNSS applications. This preference stems from the fact that most GNSS satellites transmit signals in RHCP, optimizing the system for uninterrupted signal reception. \[11\] Additionally, the antenna should have a spatial reception pattern that is close to hemispherical, meaning it can receive signals from all skyward directions. This spatial pattern improves coverage by maximizing the number of visible satellites. The antenna chosen shall be tuned to L1 (1,559-1,610 MHz) and L5 (1,164-1,215 MHz) bands.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has considered several antenna options including the helical, choke-ring, and patch antennas. While Helical and Choke-ring antennas are available as options, cost constraints nullify their viability for low-cost TEC measurement.

- **Helical antennas** are directional and provide high gain, making them well suited for high-precision GNSS applications. However, their radiation and reception patterns limit simultaneous multi-satellite monitoring. Additionally, helical antennas are relatively expensive, making them unsuitable for Team 6's budget constraints.
- **Choke-ring antennas** provide near-hemispherical radiation and reception patterns, enabling observation of multiple satellites simultaneously. They also offer excellent multipath rejection and are capable of multi-frequency tuning. However, the cost surpasses Team 6's constraint of affordability.
- **Patch antennas** are commonly used in handheld GNSS devices due to their compact form factor and affordability. \[12\] They are a usual choice for RF engineers when designing a GNSS application, featuring a fairly hemispherical radiation pattern. Most off-the-shelf dual-frequency GNSS antennas use patch elements. \[13\] Therefore, a dual-tuned, multi-element patch antenna had been selected for the prototype.

<div align="center">
  <img src="https://hackmd.io/_uploads/S1JOqLnRll.jpg" alt="Dual Tuned Patch GNSS Antenna" width="600">
  <p><strong>Figure 1:</strong> Dual Patch Antenna Explodable View</em></p>
</div>

&nbsp; &nbsp; &nbsp; &nbsp;Reception of both signals will be achieved by a single antenna, minimizing phase alignment issues and system complexity. The dual-tuned patch antenna will interface with the processing module via an SMA connector and a low-loss coaxial cable. This configuration minimizes signal attenuation and maintains GNSS signal integrity, critical for high-accuracy TEC measurements.

<div align="center">
  <img src="https://hackmd.io/_uploads/Sy4Fq8hAlg.png" alt="Dual Tuned Patch GNSS Antenna Front" width="400">
  <p><strong>Figure 2:</strong> Dual-Tuned Patch Antenna w/Coaxial</em></p>
</div>

## **Central Processing and Control System (CPCS)**

&nbsp; &nbsp; &nbsp; &nbsp;The prototype's CPCS manages all computational and control functions essential to device operation. It is responsible for performing TEC-related calculations, managing data storage, and executing system-level control tasks such as sensor monitoring and safety management.

&nbsp; &nbsp; &nbsp; &nbsp;The CPCS consists of two distinct functional domains: **RF signal conditioning and digitization**, and **computing and control platform**. The RF module performs all signal conditioning and digitization, outputting structured data for further computation. The data is then received by the computing and control platform, executing higher-level computations and overseeing system coordination.

### **RF Signal Conditioning and Digitization**

**Software Defined Radio (SDR) Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Utilizing an SDR is one approach for processing and digitizing GNSS signals. This method offers significant flexibility for the user while substantially increasing design complexity. Implementing an SDR requires extensive programming knowledge for handling IQ sampling, filtering, modulation, multipath rejection, and other digital signal processing tasks. Furthermore, these processes must be performed concurrently for multiple satellites, adding additional challenges. The primary goal of this prototype is to develop a simple yet functional system, enabling a hobbyist to measure TEC independently. While Team 6 will provide the necessary code regardless of the RF processing method chosen, using an SDR introduces unnecessary complexity, threatening the system's user-friendly appeal to the user. Additionally, SDRs do not offer a significant cost advantage and may exceed Team 6's budget to meet the required measurement accuracy.

<div align="center">
  <img src="https://hackmd.io/_uploads/BJUc5I3Rxx.png" alt="Screenshot of System Layout" width="600">
  <p><strong>Figure 3:</strong> Example of an SDR Module</em></p> 
</div>

**RF Module Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An alternative solution for RF conditioning and digitization is using a dedicated dual-tuned GNSS signal processing unit. This approach was first introduced and recommended to Team 6 by Dr. Anthea Coster, a professor at MIT and expert in ionospheric studies. Supporting this recommendation, the ScintPi 3.0, discussed in the project proposal, also employs an RF module and produces data comparable to that of high-end TEC monitoring systems.

&nbsp; &nbsp; &nbsp; &nbsp;Many of these modules feature fully integrated RF conditioning and digitization, receiving an RF signal and outputting structured data (E.g. RINEX, UBX). They include a complete RF chain with filters and low-noise amplifiers. Furthermore, additional breakout boards can be purchased to interface with the units, requiring minimal coding experience while being cost-friendly. Dr. Coster specifically recommended a u-blox GNSS positioning chip as seen below. However, Team 6 is investigating alternative options to ensure the best RF module is implemented.

&nbsp; &nbsp; &nbsp; &nbsp;Based on industry recommendations, design simplicity, and cost considerations, Team 6 has elected to implement a dedicated RF module in the prototype.

<div align="center">
  <img src="https://hackmd.io/_uploads/S1Ni9IhRel.png" alt="Screenshot of PCB Hub" width="600">
  <p><strong>Figure 4:</strong> u-blox ZED-F9P Module w/sparkfun Breakout Board</em></p>
</div>


<div align="center">
  <img src="https://hackmd.io/_uploads/rkv25LnClx.png" alt="Screenshot of PCB Hub Detail" width="800">
  <p><strong>Figure 5:</strong> u-blox ZED-F9P Module Block Diagram for L1 and L2</em></p>
</div>


### **Computing and Control Platform**

&nbsp; &nbsp; &nbsp; &nbsp;After the RF module outputs processed GNSS data, it is handled by the central computing platform, which manages TEC computation, system coordination, and data logging. Team 6 has considered implementing the full system using either a single-board computer (SBC) or a microcontroller (MCU)-based approach.

**Microcontroller Unit (MCU) Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An MCU is essentially a small computer on a single chip. It is designed to manage specific tasks within an embedded system without requiring a complex operating system. MCUs integrate processing, memory and input/output (I/O) peripherals-including timers, counters and analog-to-digital converters (ADCs)-into one efficient and cost-effective standalone unit \[3\]. They are ideal for directly interfacing with sensors monitoring system health. Other advantages, including low power consumption, minimal heat generation, and immediate startup make MCUs well-suited for field-deployable systems and user interfacing.

&nbsp; &nbsp; &nbsp; &nbsp;Despite their advantages, MCUs have significant limitations. Their limited processing power and memory restrict their ability to perform complex tasks simultaneously, such as real-time TEC computation and rendering ionospheric models. Multi-tasking capabilities are also constrained. Running sensor monitoring, system control, data logging, and TEC computations can quickly exceed an MCU's resources. Additionally, while MCUs excel at low-level interfacing, they generally lack the high-level software ecosystem and modular expansion options needed to support advanced user-driven expansions.

&nbsp; &nbsp; &nbsp; &nbsp;MCUs are excellent for analog sensor interfacing and low-level processing operations. However, MCUs alone are insufficient for handling the computationally intensive, modular, and expandable requirements of Team 6's prototype. Their limited number of I/O ports and communication interfaces restrict the ability to support multiple peripherals and expansion modules simultaneously. This makes them unsuitable as the primary processing platform.

<div align="center">
  <img src="https://hackmd.io/_uploads/HJNTcLhCgx.png" alt="Arduino MCU" width="600">
  <p><strong>Figure 6:</strong> Example of Two MCUs</em></p>
</div>

**Single Board Computer (SBC) Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An SBC provides the processing power and flexibility necessary to support Team 6's prototype. SBCs typically feature multiple GPIO pins, USB ports, HDMI ports, and other interfaces, enabling high modularity and straightforward integration of additional hardware modules. This flexibility allows the prototype to go beyond its primary objective of TEC measurement, supporting user-driven expansions such as software-defined radios and other telecommunication experiments.

&nbsp; &nbsp; &nbsp; &nbsp;The surplus computing power of an SBC enables real-time TEC calculations while simultaneously handling system control tasks, data logging, and additional processing requirements. For example, Team 6 aims to render models of ionospheric data directly from the prototype, demanding significant computational resources that an SBC can readily provide. Furthermore, widely supported development tools and a robust user community ensure that custom features and experiments can be efficiently implemented.

&nbsp; &nbsp; &nbsp; &nbsp;While an SBC can handle all tasks related to TEC measurement and provide a flexible platform for user expansion, there are some trade-offs. SBCs typically consume more power than MCUs, which warrants consideration for field-deployable systems. They also generate more heat, potentially necessitating cooling solutions, increasing the system's size. Running a full operating system adds to boot times and overall system complexity. Furthermore, most SBCs lack built-in analog-to-digital converters (ADCs). Thus, any analog input monitoring would require either external ADCs or a dedicated microcontroller to interface with the sensors.

&nbsp; &nbsp; &nbsp; &nbsp;Despite these trade-offs, the combination of modularity, high processing capability, and extensive interface support, substantiates an SBC as the optimal choice for the prototype. Team 6 has elected to implement an SBC to provide both the computational power and design flexibility needed to support the innovative user-driven nature of the system. To address the limited number of built-in ADCs, an MCU or an external ADC module (ADC hat) may be integrated to work in tandem with the SBC. This enables analog sensor monitoring for system health metrics and any additional analog inputs.


<div align="center">
  <img src="https://hackmd.io/_uploads/S1jj-D2Cgl.jpg" alt="PCB Hub Layout" width="500">
  <p><strong>Figure 7:</strong> Raspberry Pi 5 SBC</em></p>
</div>


## **Storage**

&nbsp; &nbsp; &nbsp; &nbsp;The prototype requires a storage solution capable of reliably recording high-resolution TEC measurements, system health metrics, and additional sensor data over extended periods. Storage must support continuous data logging, fast read/write operations, and seamless interfacing with the central computing platform. To ensure long-term reliability and simplicity, Team 6 conducted a throughput analysis and performed a storage estimation. This was followed by an evaluation of several options, including traditional hard disk drives (HDDs), solid-state drives (SSDs), and removable flash-based media such as SD cards and USB thumb drives.

### **Throughput Analysis**

&nbsp; &nbsp; &nbsp; &nbsp;The prototype periodically samples L1 and L5 signals for up to 20 satellites concurrently. The maximum sample rate of the u-blox ZED-F9P-05B module is 10 Hz (10 samples per second) across the constellations GPS, GLONASS, Galileo, and BeiDou \[2\]. Team 6 is using the ZED-F9P-05B as a reference module for all calculations made. Each sample is processed by the RF module and output as raw UBX packets. Relevant data, such as satellite pseudoranges, carrier phase, Doppler shifts, SNR, and other satellite-specific observables, are parsed from these packets by the SBC. This enables TEC and scintillation calculations to be performed, with the results stored as single-precision floating point numbers (8 bytes per pair of TEC and scintillation values).

&nbsp; &nbsp; &nbsp; &nbsp;The resulting throughput requirement for TEC and scintillation measurements is:

$$
\text{TEC + Scintillation Throughput (B/s)} = 8~\text{B/sample} \times 10~\text{samples/s} \times 20~\text{satellites} = 1.6~\text{kB/s}
$$

&nbsp; &nbsp; &nbsp; &nbsp;In addition to TEC and scintillation measurements, the prototype will generate RINEX files for archival and scientific use. RINEX is widely considered the standard format for satellite observation data, ensuring compatibility with established GNSS analysis tools. From the UBX stream of 10 Hz, a 1 Hz snapshot of the observables is taken and appended as an epoch to an existing RINEX file. To save space, the UBX stream is discarded. This RINEX file preserves TEC values but does not capture high-frequency scintillation events. 

&nbsp; &nbsp; &nbsp; &nbsp;RINEX file size varies based on multiple factors, most notably the number of satellites in view, the number of observation types recorded, and the sampling rate. Older versions, such as RINEX 2.0, used a fixed 80-byte line format [14]. Whereas modern versions, including RINEX 4.0, allow variable line lengths, typically shorter than 80 bytes. 

&nbsp; &nbsp; &nbsp; &nbsp;For conservative planning, Team 6 assumes each line consists of one epoch, one satellite, and one frequency. An epoch is a snapshot of the orbit and measurements of a satellite at a specific moment in time \[15\]. Essentially, it is a single sample taken across all tracked satellites at a specific instant. With 20 satellites, 2 signals per satellite, and 1 epoch per second (1 Hz RINEX generation), each RINEX file will contain roughly 40 lines. At 80 bytes per line, this corresponds to:

$$
\text{RINEX Throughput (B/s)} = 40~\text{lines/s} \times 80~\text{B/line} = 3.2~\text{kB/s}
$$

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 may choose to render TEC maps on a 100x100 grid, with each cell holding a single TEC value of 4 bytes. If Team 6 produces a map every second, this would yield a throughput of 40 kB/s.

Combining all data streams gives the total estimated throughput:

$$
\text{Total Throughput (B/s)} = 40~\text{kB/s (Map)} + 3.2~\text{kB/s (RINEX)} + 1.6~\text{kB/s (TEC + Scintillation)} = 44.8~\text{kB/s}
$$


&nbsp; &nbsp; &nbsp; &nbsp;The total throughput presented is an approximation due to the variable sizes of UBX and RINEX files. Team 6 has employed conservative calculations to account for a worst-case scenario across the three primary data streams. Additional contributions, including minor system metadata, housekeeping information, and occasional logging of auxiliary sensor measurements may slightly increase overall throughput. However, these effects are expected to be minimal. Incorporating a 20% buffer to account for the additional overhead creates an estimated total throughput of 53.8 kB/s.

### **Data Estimation**

A throughput of 53.8kB/s provides a basis for estimating daily storage requirements:

$$
\text{Storage per Day} = 53.8~\text{kB/s} \times 3600~\text{s} \times 24~\text{hours} = 4.65~\text{GB/day}
$$


&nbsp; &nbsp; &nbsp; &nbsp;Based on this calculation and Team 6's goal of a field-deployable system, the required storage capacity can be approximated. The system should be capable of storing at least one month of continuous operation, corresponding to roughly 139 GB per month. Accounting for additional software and applications, a 256 GB storage drive provides ample space, leaving an estimated 117 GB available for user-driven expansions and auxiliary data.

### **Storage Mediums Considered**

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 is considering various storage options for the prototype, with the goal of identifying the most suitable solution for meeting the project's specifications and operational constraints. Key considerations include reliability under field conditions, continuous data logging capability, throughput requirements, and sufficient storage capacity for at least one month of autonomous operation. Based on the previously estimated total throughput of 53.8 kB/s and a monthly storage requirement of approximately 139 GB, the following options were evaluated:

- **Hard Disk Drives (HDDs)**

&nbsp; &nbsp; &nbsp; &nbsp;HDDs are widely available and cost-effective, offering high storage capacity at a relatively low price per gigabyte. However, they rely on mechanical components, making them vulnerable to shock, vibration, and harsh environmental conditions. Their power consumption is higher than solid-state alternatives, and latency can limit performance while logging data continuously. This makes them less ideal for a battery-powered or field-deployable prototype.

- **Solid-State Drives (SSDs)**

&nbsp; &nbsp; &nbsp; &nbsp;SSDs offer advantages over HDDs, including static parts, high reliability, fast and consistent throughput, and compact form factors. Despite their benefits, SSDs are significantly more expensive than smaller flash-based media, which conflicts with Team 6's goal of developing a cost-effective prototype. Additionally, SSDs may consume more power and can be slightly more complex for software interfacing, requiring additional drivers or protocol management.

<div align="center">
  <img src="https://hackmd.io/_uploads/rJUyo8n0le.jpg" alt="HDD vs SSD Interior" width="600">
  <p><strong>Figure 8:</strong> HDD vs. SDD Interior</em></p>
</div>


- **SD Cards**

&nbsp; &nbsp; &nbsp; &nbsp;SD Cards provide a compact, removable storage solution and are widely available at low cost. However, their throughput and write endurance can be limited, and consumer-grade SD cards may struggle with sustained continuous logging over long periods of time. Industrial-grade SD cards offer higher endurance but are more costly, conflicting with the cost goals for the prototype.

- **USB Thumb Drives**

&nbsp; &nbsp; &nbsp; &nbsp;USB Thumb Drives combine portability, low cost, and ease of use. Many modern drives provide sufficient throughput to easily handle the estimated 53.8 kB/s of data with minimal risk of write bottlenecks. While not as fast or robust as industrial SSDs, USB thumb drives offer a practical balance of reliability, cost, and simplicity for field deployment. This supports continuous operation lasting up to one month, aligning with Team 6's expected maximum data generation of roughly 139 GB per month.

&nbsp; &nbsp; &nbsp; &nbsp;After evaluating these options Team 6 has elected to implement a USB thumb drive as the prototype storage medium. The USB drive will have 256 GB capacity and a storage format that can support files larger than 4 GB, such as exFAT or similar formats. This option offers true plug-and-play functionality, allowing easy insertion, removal, or replacement without additional hardware or system modifications. Modern USB 3.0 drives provide sufficient throughput for real-time TEC data logging and system monitoring. USB thumb drives are also cost-effective, providing ample storage capacity for continuous operation and additional user-driven experiments, while minimizing system complexity.


<div align="center">
  <img src="https://hackmd.io/_uploads/r1ySXDnAxx.jpg" alt="System Overview Diagram" width="600">
  <p><strong>Figure 9:</strong> Thumb Drive Example</em></p>
</div>


&nbsp; &nbsp; &nbsp; &nbsp;In addition to the USB thumb drive, the prototype will be capable of connecting to a local host server or workstation, enabling backup, visualization, and integration of logged GNSS measurements, system health metrics, and auxiliary data. The addition of the server provides supplementary storage and data analysis capabilities without affecting the prototype's on-device storage requirements. The choice to implement a USB thumb drive is based on throughput analysis, data estimation, and consideration of cost, reliability, and field deployability. The USB drive serves as the primary local storage for continuous TEC and system data logging. The prototype may also connect to the host server or workstation for centralized data aggregation.

## **Power**

&nbsp; &nbsp; &nbsp; &nbsp;Powering Team 6's prototype requires careful consideration of mobility, reliability, and operational environment. Various approaches, ranging from AC wall power to hybrid battery and solar configuration, offer different trade-offs in cost, complexity, and deployment flexibility. Team 6 evaluates these approaches to balance portability, autonomy, and modularity while ensuring continuous, safe operation of all subsystems, including the GNSS receiver, processing unit, and data storage.

### **AC Wall Power Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;A simple method for powering the prototype is through direct connection to a 120 V AC wall outlet. This approach provides a stable and continuous power source, ensuring reliable operation for all system components, including the GNSS receiver, processing unit, and data storage device. Wall-powered operation significantly reduces system complexity by eliminating the need for battery management circuitry, power conversion modules, and charge controllers.

&nbsp; &nbsp; &nbsp; &nbsp;No energy storage component is required, resulting in a lower-cost build. This creates margin in the budget for higher-performance electronics. However, this approach imposes significant spatial limitations. The device can only operate in proximity to a building or facility with available mains power. Consequently, deployment flexibility and geographic coverage are greatly reduced. The system would be constrained to controlled environments such as research laboratories, homes, schools, and other desired observatories, making it unsuitable for widespread or remote field measurements.

### **Standalone Rechargeable Battery Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Using a rechargeable battery system capable of supplying all required electrical loads greatly improves mobility, deployment, and versatility. This enables the prototype to operate in isolated locations without dependance on infrastructure. A well-designed battery subsystem, such as a 12.8 V LiFePO₄ pack paired with a battery management system (BMS), provides the necessary current for the device's power rails through appropriate buck converters or voltage dividers.

&nbsp; &nbsp; &nbsp; &nbsp;The advantages of a battery-only system include portability and operational independence critical for field experiments and distributed observation networks. However, this approach introduces engineering and safety challenges. The integration of rechargeable batteries necessitates protection circuits against overvoltage, short-circuit, and thermal runaway conditions. Without an external charging source, runtime is inherently limited by battery capacity, requiring careful energy budgeting and system shutdown protocols to prevent data corruption upon power depletion. This design also demands periodic maintenance and manual recharging, reducing long-term autonomy.

<div align="center">
  <img src="https://hackmd.io/_uploads/HJOoXwnCxl.png" alt="System Block Diagram" width="600">
  <p><strong>Figure 10:</strong> 12V 20Ah LiFePO4 Battery w/Built in BMS</em></p>
</div>

### **Standalone Rechargeable Battery + Solar Capable Recharge Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Incorporating a solar charging system alongside the onboard battery mitigates many limitations of the battery-only configuration. A solar panel coupled with a maximum power point tracking (MPPT) charge controller enables the device to operate for extended periods of time dependent on sunlight availability and energy demand. The use of the 12 V (nominal 12.8 V LiFePO₄) standard aligns with industry conventions for portable instrumentation and ensures compatibility with commonly available charge controllers and solar modules.

&nbsp; &nbsp; &nbsp; &nbsp;This configuration enhances the device's operational autonomy, making it ideal for remote monitoring networks or long-term unattended deployments. However, the addition of solar power introduces new physical and electrical complexities. The panel increases the system's physical footprint, potentially reducing portability. Wiring between the MPPT, battery, and system load must be carefully designed to prevent reverse current flow and cross-charging between power inputs. Furthermore, system cost and assembly time increase due to additional components and mounting considerations. Despite these drawbacks, the solar-assisted configuration offers the best endurance-to-cost ratio for long-duration field applications.


<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://hackmd.io/_uploads/ByuoQw2Clg.png" alt="12V Solar Panel" width="300"><br>
        <em>12V 20A MPPT Charge Controller</em> 
      </td>
      <td align="center">
        <img src="https://hackmd.io/_uploads/Sy_i7w2Cel.png" alt="12V 20A MPPT" width="300"><br>
        <em>12V Solar Panel</em>
      </td>
    </tr>
  </table>
  <p><strong>Figure 11:</strong> 12V Solar Panel and 20A MPPT</p>
</div>



### **Hybrid AC/DC Rechargeable Battery Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Team 6's proposed solution adopts a hybrid rechargeable battery architecture that can be powered or recharged from either a 120 V AC wall main (via DC adapter) or a solar panel. This configuration provides an optimal balance between mobility, flexibility, and simplicity. Under this approach, the prototype draws power primarily from its onboard battery, while external charging sources can be connected and disconnected as needed.

&nbsp; &nbsp; &nbsp; &nbsp;This dual-source design improves deployment versatility, allowing the device to function both as a stationary laboratory instrument (plugged into wall power) and as a portable field unit (running on battery). By using modular, standalone charge controllers, each power source remains electrically isolated, preventing simultaneous back-feeding between the AC adapter and the solar input. This simplifies protection of circuitry and reduces the likelihood of electrical faults. Moreover, excluding a permanently attached solar panel reduces the system's physical footprint and enhances portability, while still providing the option for renewable charging when required.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://hackmd.io/_uploads/B1YDrPh0lx.png" alt="19.5V 200W AC Power Adapter" width="300"><br>
        <em>Solar MC4 to XT60 Adapter</em>
      </td>
      <td align="center">
        <img src="https://hackmd.io/_uploads/SkKPHPnClg.png" alt="Solar MC4 to XT60 Adapter" width="300"><br>
        <em>19.5V 200W XT60 AC Power Adapter</em>
      </td>
    </tr>
  </table>
  <p><strong>Figure 12:</strong> AC and Solar Power Adapters</p>
</div>

&nbsp; &nbsp; &nbsp; &nbsp;The hybrid approach offers significant engineering and operational advantages. It ensures that the system remains functional during power interruptions, supports hot-swappable charging inputs, and eliminates the need for constant supervision. Using widely available power connectors such as the XT60, DC barrel jacks, or Anderson Powerpole allows for easy field servicing and replacement without compromising structural integrity. The architecture also promotes modularity, enabling future users to upgrade components without redesigning the core electronics.

&nbsp; &nbsp; &nbsp; &nbsp;The chosen approach maintains a good balance between power redundancy, safety, and cost efficiency. The inclusion of a BMS, MPPT, AC/DC, and DC/DC regulation circuitry ensures compliance with IEEE and IEC electrical safety standards while supporting continuous operation of the SBC, GNSS receiver, and storage subsystem. Overall, the hybrid rechargeable power design aligns with Team 6's objective of creating a robust, modular, and accessible prototype capable of deployment across both laboratory and remote field environments.

## **Modularity**

&nbsp; &nbsp; &nbsp; &nbsp;Robust modularity is a crucial specification for the prototype, enabling user-based servicing and expansion. Modularity ensures individual subsystems, such as the RF front end, computing platform, power management, and storage, can be upgraded, serviced, and replaced without a complete redesign. This approach supports long-term maintainability and aligns with the project's goal of enabling user-driven expansion and experimentation.

&nbsp; &nbsp; &nbsp; &nbsp;To achieve modularity, Team 6 evaluated two approaches for the PCB design:

- **Direct Footprint Approach:**  
    In this approach, the PCB includes dedicated footprints for the SBC and MCU, allowing the boards to be soldered or socketed directly onto the PCB. This provides a compact design with minimal wiring and straightforward signal routing. However, it limits flexibility to the specific boards for which the footprints were designed. Upgrading to a different SBC or MCU would require redesigning the PCB, making the prototype less adaptable for future hardware. This approach also constrains the prototype's plug-and-play capability. Users would need to modify or redesign the PCB layout to accommodate new boards, reintroducing PCB design software and adding complexity that the modular approach seeks to avoid.
- **Hub/Interconnect Approach:**  
    In this approach, the PCB acts primarily as a central hub that routes power, data, and control signals between modules without requiring the SBC or MCU to be connected directly onto the board. The hub will be designed to work seamlessly with the chosen SBC, allowing plug-and-play functionality via standardized connectors, such as ribbon cables or pin headers. All pins on the hub will be clearly marked, simplifying connections and reducing the chance of miswiring. Other SBCs may require manual wiring to match the hub's signal layout. Future iterations of similar SBCs are likely to maintain the same pinout, ensuring that the hub design remains adaptable and compatible with upcoming boards. This approach preserves modularity, simplifies assembly, and enables straightforward integration of additional peripherals, sensors, or expansion modules via dedicated headers. By decoupling the computing board from the PCB, the hub maximizes flexibility of the prototype for future experimentation, collaboration, and incremental upgrades.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has elected to use the hub approach, maintaining flexibility for new sensors, communication interfaces, and auxiliary modules, preserving organized routing and reliable connections. Headers and expansion ports reduce wiring complexity, simplify assembly, and make it easier to replace modules or test new configurations.


<div align="center">
  <img src="https://hackmd.io/_uploads/BkKlLP30gg.jpg" alt="40 Pin Ribbon Cable Connector" width="600">
  <p><strong>Figure 13:</strong> 40 Pin Male to Female Ribbon Cable</p>
</div>


## **Enclosure**

&nbsp; &nbsp; &nbsp; &nbsp;The system shall be housed in an enclosure designed for mobility, rapid deployment, and easy access in support of a variety of configurations. Team 6 draws inspiration from the ScintPi 3.0 design, exemplifying compact form factor, transportability, and user-friendly accessibility. The enclosure shall accommodate modular components, allowing for straightforward integration and replacement of the various modules and sensors within. This shall foster long-term serviceability and adaptability.

&nbsp; &nbsp; &nbsp; &nbsp;To achieve an IPx4 rating while maintaining ventilation, the enclosure design shall incorporate an enclosure nested within a larger enclosure. Interior walls are arranged to force any water entering the vent to travel upward along a convoluted path before reaching the internal cavity, effectively preventing water ingress while allowing passive airflow for thermal regulation. Additional airflow beneath the enclosure increases exposed surface area for heat dissipation, improving long-term thermal stability. The enclosure will be 3D printed, enabling rapid prototyping and low-cost production while maintaining structural integrity suitable for repeated field deployment. The 3D print files will be made publicly available, allowing users to modify and adapt the design for each specific application and environmental condition.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has identified three potential materials to use in creating the enclosure:

- **Polylactic Acid (PLA) Approach**

    PLA is a widely used material known for its ease of printing, high dimensional accuracy, and smooth surface finish, making it ideal for rapid prototyping and aesthetic enclosures. However, PLA suffers from significant drawbacks in outdoor environments. It softens at low temperatures, is brittle under mechanical stress, and degrades over time when exposed to sunlight and moisture. While it provides affordable precision for early design iterations, its lack of toughness and heat resistance makes it unsuitable for field applications requiring long-term durability.

- **Acrylonitrile Butadiene Styrene (ABS)** **Approach**

    ABS provides excellent mechanical strength, impact resistance, and thermal stability. These properties make ABS a strong candidate for rugged outdoor enclosures. However, its high printing temperature, susceptibility to warping, and the requirement for a controlled printing environment make it difficult to fabricate with standard 3D printers. Additionally, ABS emits unpleasant and potentially harmful fumes during printing, eliminating it as an option at Tennessee Technological University.

- **Polyethylene Terephthalate Glycol (PETG)** **Approach**

    PETG combines the advantages of both PLA and ABS, offering bond strength between layers, moderate flexibility, chemical resistance, and excellent impact durability. PETG withstands higher temperatures than PLA while maintaining lower printing difficulty than ABS. Its low warping tendency and moisture resistance make it ideal for producing large, dimensionally stable parts without requiring specialized equipment. PETG's balance of printability, mechanical performance, and environmental resilience make it particularly suited for outdoor or mobile applications.

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has elected to use PETG due to its superior mechanical strength, environmental stability, and manufacturability using readily available printers. Its resistance to cracking, warping, and degradation under a large range of temperatures directly supports the system's IPx4 weather resistance requirement and ensures long-term enclosure integrity. PETG therefore represents the most practical and reliable material for the project's mobile, modular, and field-deployable design objectives.

# **High-Level Solution**

&nbsp; &nbsp; &nbsp; &nbsp;The high-level solution fulfills all specified system capabilities, constraints, and stakeholder objectives through a cost-effective, modular, and reliable architecture designed for ionospheric TEC measurement. The system integrates proven commercial components to ensure operational efficiency, environmental robustness, and expandability while maintaining a total cost not exceeding \$1,000. Each design decision is justified through comparative evaluation of alternative approaches to ensure the final configuration optimally balances accuracy, affordability, reliability, and regulatory compliance.

## **System Overview**

- The proposed system directly measures ionospheric TEC using simultaneous dual-frequency observations from GNSS signals. A dual-tuned patch antenna receives signals in the L1 and L5 frequency bands, providing broad coverage for multi-satellite tracking while maintaining low cost and compactness.
- The L1 and L5 signals are processed by a u-blox dual-frequency GNSS receiver, which performs signal conditioning, filtering, and digitization. This approach is more suited to team 6's needs than SDR alternatives, offering a simpler, lower-power, and more accessible implementation for hobbyist replication and long-term deployment.
- Processed GNSS UBX files are transmitted to an SBC that serves as the system's primary computing platform. The SBC computes TEC values from signal delay measurements, logs data locally as RINEX files, and supports a web-based interface for real-time visualization.
- To enhance modularity and expandability, an MCU monitors system health parameters such as power levels, temperature, and component status, and manages optional user expansion sensors. This secondary control layer enables integration of auxiliary environmental or experimental modules without interfering with core TEC operations.
- All components interface through a centralized PCB hub, standardizing power, data, RF, and control connections. This hub-based design simplifies assembly, supports modular attachment and removal of system modules, ensuring electrical integrity across all subsystems.
- A rechargeable 12V battery with solar charging capabilities powers the device, allowing continuous autonomous operation in both laboratory and remote field environments.

&nbsp; &nbsp; &nbsp; &nbsp;The complete architecture satisfies all functional, operational, and regulatory constraints while emphasizing low cost, replicability, and modular expandability. The encapsulation of these requirements encourages broad adoption and community-driven development.

## **Design Justification and Alignment with Specifications**

**Signal Reception**

&nbsp; &nbsp; &nbsp; &nbsp;After evaluating helical, choke-ring, and patch antenna designs, a dual-tuned patch antenna was selected. Helical antennas, while offering high gain, were excluded due to their cost and directional limitations, conflicting with the system's requirement for hemispherical coverage. Choke-ring antennas, although providing excellent multipath rejection, were also rejected because they exceed budget constraints. In contrast, the dual-tuned patch antenna meets the necessary L1 and L5 frequency operation, provides broad sky coverage for simultaneous multi-satellite observation, and remains affordable. This directly satisfies both the System capabilities for dual-frequency reception and does not exceed the cost constraint of \$1,000.

**Signal Processing**

&nbsp; &nbsp; &nbsp; &nbsp;Comparative analysis between SDR-based and dedicated GNSS module approaches showed that while SDRs provide flexibility, they impose unnecessary complexity, cost, and power draw for the intended educational and research adoption. The RF module GNSS receiver integrates dual-frequency reception, filtering, and analog-to-digital conversion in a compact, low-power design. This satisfies the operational guidelines for passive GNSS signal reception and the regulatory compliance requirements for ITU-defined GNSS frequency allocations.

**Computation and Data Management**

&nbsp; &nbsp; &nbsp; &nbsp;A combination of an SBC and an MCU was selected as the CPCS due to its robust computational performance, modular I/O support, and open-source ecosystem. This configuration enables real-time TEC calculation at a 10 Hz logging rate, concurrent data logging with web-based visualization, modular expansion through USB and GPIO interfaces, and continuous monitoring of system health metrics and auxiliary analog sensors. Compared to designs utilizing microcontrollers alone, the inclusion of an SBC provides the necessary processing capabilities and flexibility to meet the system's data logging, analysis, and control requirements while maintaining energy efficiency suitable for continuous field deployment.

**Storage**

&nbsp; &nbsp; &nbsp; &nbsp;The storage system is designed to use a 256 GB USB thumb drive, which records TEC and scintillation data at the full 10 Hz sampling rate. In addition to the high-frequency measurements, the system also generates and stores RINEX files at a 1 Hz rate, ensuring compatibility with standard GNSS analysis tools, providing both detailed and archival data for long-term monitoring and post-processing. This design was chosen to balance high-resolution data capture, long-term storage capacity, and cost-effectiveness, meeting both operational requirements and budget constraints.  

**Power System**

&nbsp; &nbsp; &nbsp; &nbsp;The power subsystem combines a 12V rechargeable battery with wall and solar charging capability, enabling both off-grid and wall-powered operation. The inclusion of overcurrent and thermal protection circuits satisfies safety and environmental constraints, enabling continuous operation during field deployment in remote locations. This fulfills operational guidelines for autonomous functionality.

**Modularity and Expandability**

&nbsp; &nbsp; &nbsp; &nbsp;Following HamSCI design principles, the system emphasizes modularity and expandability through a standardized PCB hub design. This hub provides consistent SMA, USB, and GPIO interfaces, allowing the antenna, receiver, and computing modules to connect in a uniform and easily reconfigurable manner. The standardized PCB hub simplifies wiring, improves system reliability, and includes expansion headers to accommodate future sensors or additional processing modules. This approach ensures straightforward replacement or upgrades of individual components, fully satisfying the Modularity and Expandability Specifications while supporting the platform's long-term adaptability.

**Physical Reliability and Enclosure**

&nbsp; &nbsp; &nbsp; &nbsp;The system is housed in a weather-resistant IPx4-rated enclosure, providing protection against splashing water and dust. A stable mounting base ensures the system remains securely in place during adverse weather conditions, fully satisfying the physical reliability constraint.

**Documentation and Replicability**

&nbsp; &nbsp; &nbsp; &nbsp;Comprehensive open-source documentation will include hardware schematics, PCB layouts, assembly instructions, and programming scripts. This ensures enthusiasts and researchers can replicate and expand the system independently at a total cost not exceeding \$1,000. This satisfies documentation and replicability specifications.

**Regulatory and Safety Compliance**

&nbsp; &nbsp; &nbsp; &nbsp;The device operates solely as a GNSS receiver, transmitting no signals. Thus, adhering to ITU and regional ISM spectrum regulations, protective power, and thermal safeguards, ensuring safe operation, satisfying regulatory compliance, and safety constraints.

**Achievement of Objectives**

&nbsp; &nbsp; &nbsp; &nbsp;This design meets all stakeholder and customer objectives through the following outcomes:

- **Accuracy:** Dual-frequency GNSS observation and low-noise RF path enable precise TEC computation.
- **Reliability:** Environmental sealing, robust components, and integrated safety protections ensure continuous operation.
- **Modularity:** Replaceable modules, standard interfaces, and open documentation promote long-term expandability.
- **Affordability:** Use of off-the-shelf components and open-source software keeps total system cost below \$1,000.
- **Replicability:** Public design documentation supports community-driven replication and enhancement.
- **Compliance:** Fully operation and adherence to GNSS and ISM regulations ensure legal and safe use.

## **Summary**

&nbsp; &nbsp; &nbsp; &nbsp;The proposed TEC measurement system represents a balanced integration of accuracy, affordability, and modularity. The design incorporates a dual-tuned GNSS antenna, RF receiver, and a computing subsystem composed of both an SBC and an additional MCU. The SBC handles high-speed TEC and scintillation computation, data logging, and visualization, while the MCU monitors system health and auxiliary sensors. All modules are connected through a standardized PCB hub that provides power distribution, modular expansion ports, and support for future sensors or processing modules. This architecture meets all functional, safety, and regulatory specifications, delivering a low-cost, replicable, and environmentally resilient GNSS-based ionospheric monitoring system optimized for research, educational deployment, and long-term adaptability.

# **Hardware Block Diagram**
<div align="center">
  <img src="https://hackmd.io/_uploads/S1PtFvnCxl.png" alt="Hardware Block Diagram" width="600">
  <p><strong>Figure 14:</strong> <em>Hardware Block Diagram</em></p>
</div>

# **Operational Flow Chart**

<div align="center">
  <img src="https://hackmd.io/_uploads/rJz6KwhCee.png" alt="Operation Flowchart" width="600">
  <p><strong>Figure 15:</strong> <em>Operation Flowchart</em></p>
</div>


# **Atomic Subsystem Specifications**

## **Data Storage System**

**Overview**

&nbsp; &nbsp; &nbsp; &nbsp;The Data Storage Subsystem provides persistent, reliable logging of all processed ionospheric TEC data by the CPCS. It ensures the prototype maintains a continuous record of timestamps for calculated TEC and scintillation values for analysis and visualization. The design emphasizes modularity, durability, and ease of data retrieval while maintaining compatibility with the SBCs limited power and memory resources.

**Functional Description**

&nbsp; &nbsp; &nbsp; &nbsp;The subsystem's core function is to store TEC computation outputs on a non-volatile solid-state thumb drive. It fulfills the secondary requirement of scintillation computations, storing them in the same location.  
It enables:

- Sequential data logging of all processed observations at fixed time intervals (e.g., 10 Hz UBX file sample rate).
- The system implements automatic file management, creating new log files daily or upon reaching a predefined size threshold. All files are stored on an exFAT-formatted storage device, ensuring compatibility across platforms while supporting large file sizes and efficient data access.
- Data accessibility, allowing users to retrieve stored data either locally (via USB) or access real-time data remotely (via network interface).
- Error detection, ensuring data integrity through periodic write verification.  

&nbsp; &nbsp; &nbsp; &nbsp;In addition, the storage drive functions as a black box component within the system. It  
operates independently from visualization and network layers, continuously recording every TEC measurement and timestamp in the event of web server failure. This fault-tolerant design ensures no data is lost during outages or reboots. By serving as a digital black box, the subsystem preserves long-term data integrity and supports reliable post-event analysis, ensuring consistent performance across both lab and field conditions.

**Subsystem Interfaces**

- **Power Input**
  - Connected To: Power Subsystem
  - Description: Supplies power to the SBC and attached storage device
- **Data Input**
  - Connected To: CPCS (SBC)
  - Description: Receives processed TEC data, timestamps, and system diagnostics
- **Data Output**
  - Connected To: CPCS / Web Interface
  - Description: Provides stored TEC data for visualization and download
- **User Interface**
  - Connected To: Web Dashboard
  - Description: Displays recent TEC trends and storage status

**Subsystem Operation**

- **Initialization Phase**
  - On system startup, the SBC verifies the presence of the attached storage device.
  - If absent, a system log error is generated and will only use the server to show recent TEC data and trends.
- **Logging Phase**
  - After each TEC computation cycle, the CPCS writes new entries (timestamp, TEC value).
  - Data is added to the server showing recent trends and the last few entries.
- **Archival and Maintenance Phase**
  - Files older than a set duration (e.g., 30 days) are compressed or archived.
  - If the storage drive is completely full, the oldest entries will be written over by the newest entries.
- **Access and Visualization Phase**
  - Logged data can be accessed directly with the storage drive.
  - The SBC operates a lightweight server to render visual summaries (TEC vs. time) using stored logs.  

**Expected User Interaction**

&nbsp; &nbsp; &nbsp; &nbsp;From a user's perspective, the subsystem operates transparently. The user can:

- Connect to the system's web interface to view recent TEC data trends.
- Export raw data files for post-analysis.
- Check available storage space and system logging health from the dashboard.

No direct user control of logging frequency or file management is required, though these parameters may be configurable via the software interface.

**Conceptual Functional Flow**

<div align="center">
  <img src="https://hackmd.io/_uploads/ByVp5v3Cxx.png" alt="Data Storage Flow Chart" width="600">
  <p><strong>Figure 16:</strong> <em>Data Storage Flow Chart</em></p>
</div>


**Shall Statements**

- The Data Storage Subsystem shall continuously record all TEC computation results at the system's defined logging rate.
- The subsystem shall utilize a non-volatile solid-state thumb drive to preserve data during power loss.
- The subsystem shall automatically manage log file rotation and archival to prevent data loss or overflow.
- The subsystem shall interface directly with the CPCS via internal file I/O, requiring no external communication link for operation.
- The subsystem shall remain modular, allowing replacement and enabling expansion (e.g., switching to larger-capacity storage) without major redesign.
- The subsystem shall consume minimal power, remaining within the limits provided by the power subsystem.

## **Antenna and RF Module System**

&nbsp; &nbsp; &nbsp; &nbsp;The Antenna and RF Module System shall be responsible for receiving GNSS data for computation of TEC and scintillation measurements. The resulting measurements and other generated data shall then be sent to the data and storage subsystem for further analysis and processing.

**Subsystem Description**

- This subsystem shall use a dual-tuned patch antenna to receive L1 and L5 GNSS signals as an analog input.
- This subsystem shall use an RF module to interpret the GNSS signals from the antenna.
- The RF module shall extract the timestamps of each received L1 and L5 signal, as well as the location of the GNSS satellite(s), and the location of the module.
- This data shall be passed to a separate SBC via a serial UART connection to compute TEC measurements.
- The measurements computed by the SBC, as well as the standardized data extracted by the RF module, shall be sent to the data and storage subsystem to be further analyzed and saved.
- This subsystem shall be powered by the power subsystem, connected by the system interconnections subsystem, and contained within the enclosure subsystem.

**Subsystem Hardware Diagram**


<div align="center">
  <img src="https://hackmd.io/_uploads/rkdwev6Rlg.png" alt="Antenna and RF Module Hardware Diagram" width="400">
  <p><strong>Figure 17:</strong> <em>Antenna and RF Module Hardware Diagram</em></p>
</div>

**Subsystem Flowchart**

<div align="center">
  <img src="https://hackmd.io/_uploads/rJOvlDTRxl.png" alt="Antenna and RF Module Flowchart" width="400">
  <p><strong>Figure 18:</strong> <em>Antenna and RF Module Flowchart</em></p>
</div>


## **System Interconnections**

&nbsp; &nbsp; &nbsp; &nbsp;The system interconnections platform is responsible for providing a central connection site for all major modules and peripheral devices. This subsystem ensures the prototype remains modular, maintainable, and expandable, supporting user-driven experimentation. To achieve this, the system will implement a PCB hub approach, serving as a unified interface for routing power, data, control, and RF signals between modules. This maintains electrical integrity and ease of reconfiguration.

**Subsystem functions**

- The subsystem shall implement a PCB to interconnect all modules and peripheral devices.
- The subsystem shall provide organized routing for power, data, RF signals, and control lines between modules.
- The subsystem shall maintain electrical integrity, minimizing coupling, noise, and interference on critical signal paths.
- The subsystem shall standardize interface connections for auxiliary processing modules, external sensors, and communication devices.
- The subsystem shall include clearly marked headers, expansion ports for modular attachment, and removable components while maintaining system integrity.
- The subsystem shall accommodate all necessary electrical and signal pathways, including power distribution rails, RF signal lines, data buses, and control interfaces, ensuring full system integration.


<div align="center">
  <img src="https://hackmd.io/_uploads/ry81xbpRgx.svg" alt="Connections Diagram" width="800">
  <p><strong>Figure 19:</strong> <em>Connections Diagram</em></p>
</div>


&nbsp; &nbsp; &nbsp; &nbsp;The block diagram does not show the specific PCB trace connections other than general power buses. It instead highlights the use of a hub-based architecture for the prototype.

**Interface Connections**

| **Connected Subsystem** | **Signal Type** | **Signal Direction** | **Protocol** | **Notes** |
| --- | --- | --- | --- | --- |
| Power Supply/ Battery | DC Power | Input/Output | N/A | Provides regulated power rails to all connected devices |
| RF Module | Analog RF / Digital GNSS Data | Input: Analog RF from antenna / Output: GNSS data to SBC routed through PCB | UART | Receives RF signal via coaxial cable. Outputs GNSS data file (e.g., RINEX or UBX) to SBC through PCB traces |
| SBC | GNSS Data / MCU Sensor Status / TEC Measurements / Peripheral Commands | Input: Data from RF module and MCU / Output: Commands to peripherals and logging devices | GPIO/UART/I2C/SPI/Power | Receives GNSS data and sensor status. Sends configuration commands, peripheral control signals, and processed TEC data |
| MCU | Sensor GPIO | Input/Output | GPIO/UART/I2C/SPI/Power | Provides the system data as the control platform |
| Storage | Digital Data / Power from SBC | Input: Commands from SBC / Output: Data to SBC | USB connected to SBC | Read/write operations for logged GNSS data, system health metrics, and user applications |

## **Power System**

&nbsp; &nbsp; &nbsp; &nbsp;The Power Subsystem is responsible for supplying all other subsystems with the necessary electrical parameters for them to function properly without fault. This subsystem also includes internal protection, preventing electrical faults from damaging other components.

- This subsystem shall supply stable DC power to all other subsystems
- This subsystem shall manage charging operations.
- This subsystem shall supply the necessary DC voltage to all components requiring specific voltage levels for proper operation.
- This subsystem shall implement circuit protection components preventing over-charge, discharge, and all other types of well-defined electrical faults with the use of physical circuit protection components.
- This subsystem shall report electrical parameters such as battery capacity to the MCU, ensuring proper shutdown procedures. These values will also be readily available for user observation.
- This subsystem shall use components that are readily available for purchase and can be exchanged easily without physically altering any other component.

<div align="center">
  <img src="https://hackmd.io/_uploads/rJEkHITCex.png" alt="Detailed Power System Flowchart" width="800">
  <p><strong>Figure 20:</strong> <em>Power System Flowchart</em></p>
</div>


## **Enclosure and Protection System**

&nbsp; &nbsp; &nbsp; &nbsp;The enclosure and protection system serves as the structural and environmental safeguard for the entire prototype, ensuring reliable performance under diverse operating conditions. Its primary role is to shield all internal subsystems from external hazards such as moisture, dust, and temperature fluctuations, while also mitigating internal risks like heat buildup or mechanical stress. To achieve this, the enclosure will be 3-D printed using PETG, a material and method selected for superior resistance to water, chemicals, and extreme temperatures. The design will incorporate precision-engineered mounts to securely position both internal and external components, provide multiple stable mounting configurations, and support modularity for efficient maintenance and future upgrades.

- This subsystem shall be 3-D printed using PETG, optimizing resilience against water, chemical, and heat interactions.
- This subsystem shall contain mounts to securely hold all internal and external components.
- This subsystem shall provide stability for a variety of mounting options.
- This subsystem shall promote modularity of internal components.
- The subsystem shall provide ease of access to all internal components.

## **Publication**

&nbsp; &nbsp; &nbsp; &nbsp;The Publication Subsystem is responsible for comprehensive documentation of all activities throughout the system's lifecycle, including planning, design, prototyping, and testing. This ensures the project processes, milestones, and results are clearly recorded and accessible, providing the necessary resources for replication and scientific dissemination.

**Subsystem Requirements**

- The subsystem shall document all project planning activities, including objectives, schedules, and milestone definitions.
- The subsystem shall record all design decisions, schematics, and system configurations in sufficient detail for replication.
- The subsystem shall log all construction and assembly procedures, including materials, components, and pinouts.
- The subsystem shall document testing and validation procedures, capturing experimental setups, results, and analysis.
- The subsystem shall produce a final comprehensive paper detailing each milestone, prototype development, and experimental outcomes.
- The subsystem shall ensure that all documentation is clear, structured, and accessible to both internal team members and external researchers.
- The subsystem shall provide all necessary materials for system replication, including manuals, diagrams, and procedural guides.
- The subsystem shall facilitate knowledge transfer to the scientific community, supporting further research and discovery in ionospheric science.

&nbsp; &nbsp; &nbsp; &nbsp;By adhering to these requirements, the publication subsystem ensures that the project is thoroughly documented and reproducible, providing meaningful contributions to the scientific community and enabling continued research and innovation in ionospheric monitoring.

# **Ethical, Professional, and Standards Considerations**

&nbsp; &nbsp; &nbsp; &nbsp;The deployment and use of TEC measurement systems carry broad implications across scientific, societal, and environmental contexts. In the scientific realm, accurate TEC data supports the study of ionospheric behavior, space weather phenomena, and their impact on systems dependent on satellite communication and navigation. These measurements aid researchers in understanding global atmospheric processes and support engineers in improving models capable of predicting disruptions in GPS and other critical services. Without reliable data, entire fields of research are limited in their ability to explain or mitigate natural events influencing everyday technologies.

&nbsp; &nbsp; &nbsp; &nbsp;From a societal perspective, TEC data underpins technologies many people intuitively rely on. Reliable navigation for aviation, maritime travel, and emergency response services all depend on the stable functioning of GNSS signals. Accurate TEC monitoring can prevent accidents, optimize transportation, and ensure that first responders have trustworthy positioning data in critical situations. Conversely, misuse or misinterpretation of TEC data could lead to faulty predictions or misguided public communication. This has the potential to undermine trust in technology or cause financial and operational losses for dependent industries.

&nbsp; &nbsp; &nbsp; &nbsp;Ethical responsibilities also play a role when deploying TEC systems. Engineers and researchers must ensure accuracy and integrity in the data they collect and distribute. This requires validating measurements, properly calibrating equipment, and transparently documenting methodologies. Upholding copyright and regulatory standards are equally important. TEC data often involves international collaboration and shared satellite infrastructure. Adhering to such regulations protects intellectual property rights and ensures global research efforts remain cooperative rather than competitive.

&nbsp; &nbsp; &nbsp; &nbsp;Environmental considerations extend beyond scientific scope. The design and deployment of TEC systems should strive to minimize their environmental footprint through careful selection of energy-efficient components, sustainable materials, and responsible disposal of outdated hardware. Engineers should also consider the broader ecosystem of satellite launches, ground stations, and electronic waste, recognizing that every stage of system development carries environmental costs.

&nbsp; &nbsp; &nbsp; &nbsp;Finally, public safety must remain a priority. TEC measurement systems, while highly technical, ultimately serve the purpose of safeguarding critical infrastructure and ensuring that society can operate smoothly even during ionospheric disturbances. Engineers must approach their work with honesty and diligence, acknowledging the outputs of their systems could influence decisions with global impact. A strong awareness of these societal responsibilities helps ensure technological progress contributes positively to the public good rather than introducing new risks.

# **Resources**

&nbsp; &nbsp; &nbsp; &nbsp;Project resources are allocated across three primary categories: budget, labor, and timeline. The budget ensures cost-effective component selection and material procurement within the project's \$1,000 constraint. The division of labor assigns specific subsystem responsibilities to team members based on technical expertise, while the timeline coordinates design, fabrication, testing, and documentation milestones to maintain steady project progress and accountability to guarantee on-time delivery.

## **Budget**

**Data Storage System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be made up of a storage drive and an SBC. To keep options open for various specs for the SBC and the storage drive, a maximum expenditure of \$150 for the SBC and \$75 for the storage has been set as follows.

| Subsystem | Item | Budget |
| --- | --- | --- |
| Data Storage System 
| | Storage Drive (Thumb Drive) | \$25 |
| | Single-Board Computer (SBC)\* | \$120\* |
| Total | | \$145 |

**Antenna and RF Module System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of an RF Module and Dual-Tuned Patch Antenna, which includes the required Coaxial Cable. Given the large variation in cost for RF modules, the max budget for this component has been set at \$300.

| Subsystem | Item | Budget |
| --- | --- | --- |
| Antenna and RF Module System
| | RF Module | \$300 |
| | Dual-Tuned Patch Antenna | \$75 |
| Total | | \$375 |


**System Interconnections:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of a PCB board, a magnetometer, a microcontroller, and any miscellaneous cables connecting each subsystem together.

| Subsystem | Item | Budget |
| --- | --- | --- |
| System Interconnections
| | PCB | \$50 |
| | Miscellaneous Cables | \$25 |
| | Magnetometer | \$5 |
| | Microcontroller | \$20 |
| Total || \$100 |

**Power System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of a power supply, MPPT charge controller, 12V 50Ah battery, transformer, miscellaneous cables, and as a demonstration of expandability, a solar panel shall be included.

| Subsystem | Item | Budget |
| --- | --- | --- |
| Power System
| | Solar Panel | $75 |
| | Power Supply | $25 |
| | MPPT Charge Controller | $30   |
| | Battery (12V, 20Ah) |$50 |
| | Transformer/Converters | $20   |
| | Protection Components |  $25  |
| | Miscellaneous Cables | $35   |
| Total | | $260 |

**Enclosure System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of waterproofing material and PETG filament.

| Subysystem | Item | Budget |
| --- | --- | --- |
| Enclosure
|| Waterproofing Material | \$40 |
|| PETG Filament | \$50 |
| Total || \$90 |

**Overall Budget:**

&nbsp; &nbsp; &nbsp; &nbsp;Below is the overall budget of the project. Most component prices are overestimated to allow for some wiggle room for part selections. However, the final design must be below \$1,000, so all subsystems should strive to be as under budget as possible.

| Subsystem | Item | Budget |
| --- | --- | --- |
| Data and Storage System 
|| Storage Drive (Thumb Drive) | \$25 |
|| Single-Board Computer (SBC)\* | \$120\* |
| Total || \$145 |
| Antenna and RF Module System 
|| RF Module | \$300 |
|| Dual-Tuned Patch Antenna | \$75 |
| Total || \$375 |
| System Interconnections 
|| PCB | \$50 |
|| Miscellaneous Cables | \$25 |
|| Magnetometer | \$5 |
|| Microcontroller | \$20 |
| Total || \$100 |
| Power System 
|| Solar Panel | \$75 |
|| Power Supply | \$25 |
|| MPPT Charge Controller | \$30 |
|| Battery (12V, 20Ah) | \$50 |
|| Transformer/Converters | \$20 |
|| Protection Components | \$25 |
|| Miscellaneous Cables | \$35 |
| Total || \$260 |
| Enclosure 
|| Waterproofing Material | \$40 |
|| Mounting Material | \$50 |
| Total || \$90 |
| Project Total |     | \$970 |

\*SBC will be shared between Data Subsystem and RF Module Subsystem

## **Division of Labor**

- Power Supply Subsystem - Kenneth Creamer
  - Requirements: A thorough understanding of power systems and solar panels.
  - Responsible team member and rationale: Kenneth is the only member of the group who has completed intro to power systems and is currently taking power systems analysis. He also has previous experience with solar panels and renewable energy systems.
- Storage and Server Subsystem - Blake Hudson
  - Requirements: knowledge of networking and server experience. Computer knowledge when using storage drives and memory allocation.
  - Responsible team member and rationale: Blake has previous experience creating servers and working with storage drives. He has worked with pi pico and esp 32 and built computers.
- Antenna and RF Module Subsystem - Jackson Taylor
  - Requirements: knowledge of embedded systems and communication between the u-blox and the computer and outputting received data. Computing the measurement of TEC
  - Responsible team member and rationale: Jackson is currently taking embedded system design and has completed intro to telecommunications.
- System Interconnection Subsystem - Jack Bender
  - Requirements: PCB design and a general understanding of each other subsystem to effectively integrate all subsystems.
  - Responsible team member and rationale: Jack has previous experience using RF chains, system engineering, and block diagrams.
- Enclosure and Thermal Load - Nolan Magee
  - Requirements: Competent in AutoCad design for creating housing for the prototype.
  - Responsible team member and rationale: Nolan has previous experience using AutoCad.
- Research Paper Subsystem - Team Effort
  - Requirements: Technical writing ability.
  - Responsible team member and rationale: Every member of the group shall contribute to the completion of the paper as documentation is completed.

## **Timeline**

<div align="center">
  <img src="https://hackmd.io/_uploads/S1mxF_2Reg.png" alt="Screenshot B" width="1400"><br><br>
  <img src="https://hackmd.io/_uploads/r1mxKdnRlg.png" alt="Screenshot A" width="1400">
</div>



# **References**

\[1\] TnTech ECE F25 Team 6, "Project Proposal," GitHub repository, 15 Oct. 2025. \[Online\]. Available: <https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/main/Reports/Project_Proposal.md>. \[Accessed: Oct. 21 2025\].

\[2\] u-blox AG, "ZED-F9P DataSheet UBX-DOC-963802114-12824," 2024. \[Online\]. Available: <https://content.u-blox.com/sites/default/files/documents/ZED-F9P-05B_DataSheet_UBXDOC-963802114-12824.pdf>. \[Accessed: Oct. 21 2025\].

\[3\] u-blox AG, "ZED-F9P DataSheet UBX-DOC-963802114-12824," 2024. \[Online\]. Available: <https://content.u-blox.com/sites/default/files/documents/ZED-F9P-05B_DataSheet_UBXDOC-963802114-12824.pdf>. \[Accessed: Oct. 21 2025\].

\[4\] IEC, "IEC 62133-2:2021 - Secondary cells and batteries containing alkaline or other non-acid electrolytes - Safety requirements for portable sealed secondary lithium cells, and for batteries made from them, for use in portable applications," International Electrotechnical Commission, 2021. \[Online\]. Available: <https://webstore.iec.ch/en/publication/32662>. \[Accessed: Oct. 21 2025\].

\[5\] IEEE Std 1657-2018, _IEEE Recommended Practice for Personnel Qualifications for Installation and Maintenance of Stationary Batteries and Battery Systems_, IEEE Standards Association, 2018. \[Accessed: Oct. 21 2025\].

\[6\] IEC 62509:2010, Battery charge controllers for photovoltaic systems - Performance and safety requirements, IEC, 2010. \[Accessed: Oct. 21 2025\].

\[7\] P. Kenpankho, "Comparison of GPS TEC measurements with IRI TEC over an equatorial station," Earth, Planets & Space, vol. 63, pp. 393-401, 2011. Available: <https://earth-planets-space.springeropen.com/articles/10.5047/eps.2011.01.010>. \[Accessed: Oct. 21, 2025\].

\[8\] "Measuring GNSS Signal Strength," Inside GNSS, Dec. 2010. \[Online\]. Available: <https://insidegnss.com/measuring-gnss-signal-strength/>. \[Accessed: Oct. 21 2025\].

\[9\] Open Source Initiative, "OSI approved licenses," Open Source Initiative, 2025. \[Online\]. Available: <https://opensource.org/licenses> . \[Accessed: Oct. 21 2025\].

\[10\] IEC 60529:2021, Degrees of protection provided by enclosures (IP Code), International Electrotechnical Commission, Geneva, 2021. \[Online\]. Available: <https://webstore.iec.ch/en/publication/32662>. \[Accessed: Oct. 21 2025\].

\[11\] Novotech Corp., "Circular Polarization," Technology webpage. \[Online\]. Available: <https://novotech.com/pages/circular-polarization>. \[Accessed: Oct. 21 2025\].

\[12\] V. Navarro, "Antennas," Navipedia - The GNSS Wiki, European Space Agency, JUL. 14 2011. \[Online\]. Available: <https://gssc.esa.int/navipedia/index.php/Antennas>. \[Accessed: Oct. 21 2025\].

\[13\] Ignion, "Chip vs Patch Antenna for GNSS," White Paper, 2024. \[Online\]. Available: <https://ignion.io/files/AN_Chip-vs-patch-antenna-for-GNSS.pdf>. \[Accessed: Oct. 21 2025\].

\[14\] J. Whitehead, "Unriddling the Elements of RINEX," Spatial Source, Geospatial Media Pty Ltd., 2015. \[Online\]. Available: <https://www.spatialsource.com.au/unriddling-the-elements-of-rinex/>. \[Accessed: Oct. 22 2025\].

\[15\] Taitus Software, "Orbital Elements Explained," Knowledge Base Article, Taitus Software S.L., 2023. \[Online\]. Available: <https://taitussoftware.com/kb/orbital-elements/>. \[Accessed: Oct. 22 2025\].

\[16\] OpenAI, GPT-5, ChatGPT, San Francisco, CA, USA, 2025. \[Online\]. Available: <https://chat.openai.com/>. \[Accessed: Sept. 20, 2025\].

# **Statement of Contributions**

Jack Bender: Comparative Analysis of Potential Solutions \[Signal Reception, CPCS, Storage, Modularity\], Atomic Subsystem Specifications \[System Interconnections\], Final Review

Kenneth Creamer-Harris: Restating the Problem, Comparative Analysis of Potential Solutions \[Power\], Atomic Subsystem Specifications \[Power Sub-System\], References

Blake Hudson: Atomic Subsystem Specifications \[Data Storage Subsystem\], High-Level Solution, Hardware Block Diagram, Operational Flow Chart.

Nolan Magee: Introduction, division of labor, Timeline, and Final Review.

Jackson Taylor: Budget, Atomic Subsystem Specifications \[Antenna and RF Module Subsystem\]
