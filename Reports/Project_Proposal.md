<h1 style="font-size:40px;">F25_Team 6_SpaceWeatherStation</h1>

## **Introduction**
&nbsp; &nbsp; &nbsp; &nbsp; The goal of this project is to create a working prototype capable of measuring total electron content (TEC) in the ionosphere. The design shall be simple yet functional, affordable yet durable. The intention is to establish a foundational framework of hardware and software for hobbyists interested in measuring TEC. The project aims to create accessibility for the hobbyist both intellectually and financially, while maintaining flexibility for personal modifications. Team 6 seeks to develop a dynamic database that supports hobbyists worldwide in creating, innovating, and educating in regard to TEC. 

&nbsp; &nbsp; &nbsp; &nbsp; The scope of this proposal includes outlining the background of TEC by addressing what has been accomplished, what is currently underway, and what is planned. This will clarify the need for the project, identify limiting factors, and inform the project specifications to maintain focus. The proposal will then define what constitutes a successful outcome, supported by details regarding budget, available and required expertise, and a timeline of key milestones. Finally, the proposal will conclude with a discussion of the broader implications of successfully completing the project. 

## **Formulating the Problem**

### **Background**

Modern society depends heavily on reliable communication and navigation systems, ranging from critical infrastructure to everyday Global Navigation Satellite Systems (GNSS)-enabled devices. Yet, these systems are constantly influenced by the ionosphere, a dynamic region of Earth’s upper atmosphere that can refract, delay, or disrupt radio signals. The most important parameter used to describe ionospheric effects is TEC. TEC refers to the total number of electrons present along a path between a signal transmitter and receiver. By definition, TEC is the integral of the electron density $N(s)$ along a path $ds$ between points $A$ and $B$ [1]:

$$
\text{TEC} = \int_A^B N(s) \, ds
$$

By convention, the measurement of a total electron content unit (TECU) is defined as follows:

$$
1~\text{TECU} = 10^{16}~\text{electrons/m}^2
$$

TEC varies considerably with time of day, geographic location, season, solar cycle, solar activity, geomagnetic storms, and atmospheric disturbances. The free electrons that make up TEC are concentrated in the ionosphere, roughly 80–600 km above Earth’s surface. In the ionosphere, atoms are ionized primarily by extreme ultraviolet (EUV) and x-ray solar radiation. The resulting electron density changes continuously with solar radiation and geomagnetic conditions. Additional disturbances, such as atmospheric waves and scintillation, further contribute to its variability. This dynamic behavior can both enhance long-distance radio communication and cause impairments such as delays, fading, scintillation, and even data loss [2][3][4]. Consequently, there is a strong demand for consistent measurement of electron content globally.

Due to the ionosphere being a plasma medium, the refractive index affects radio wave propagation. At high radio frequencies (HF), refraction caused by electrons can allow a radio signal to propagate over the horizon of the Earth, increasing communication range. However, TEC can also cause distortion and fading, resulting in data loss. At very high radio frequencies (VHF) and above, including GNSS, ionospheric effects appear as signal delays, phase shifts, and scintillation [1]. These disruptions reduce the accuracy and reliability of positioning, navigation, and timing (PNT) services critical to aviation, maritime, and telecommunication systems. To mitigate or take advantage of the effects of TEC, its levels must be accounted for during radio transmission.

As more information becomes available for TEC analysis, accuracy and predictability will increase, leading to more effective ways of transmitting signals. In addition, a wealth of TEC data provides more opportunity for innovation within emerging fields related to ionospheric conditions.

The scope required to build a TEC measurement system encompasses many fields of learning within engineering. A single person interested in building such a system has a high likelihood of becoming overwhelmed due to the complexity involved. This necessitates having a team of individuals to research and distill the information into a condensed process, allowing hobbyists to mitigate the time and expertise needed to complete a functional TEC measurement system.

A major limiting factor to widespread involvement in measuring TEC is the expense of required equipment. Thus, the goal of this project is to create a replicable, open-source, affordable system that enables technically inclined hobbyists to observe TEC.

One way to measure TEC is to compute the time delay between two signals transmitted through the atmosphere. Two GNSS signals transmitted concurrently are received by an antenna connected to a signal processing unit. The difference of delay between the two signals is identified as a result. The delay of a signal passing through the ionosphere can be expressed as the integral of the ionospheric refractive index $N$ along the path $ds$ extending from the satellite at point $A$ to the receiver at point $B$ [1]. Equivalently, it can also be expressed as an added term in the measured pseudorange $S$:

$$
S = \rho - 40.31 f^2 \int_A^B N \, ds = \rho - 40.3 (\text{TEC}) f^2
$$

Here, $\rho$ is the distance between the satellite and receiver excluding atmospheric delays. From the derivations below, we can see that the delay of ionospheric signals is entirely dependent on TEC. Knowing TEC and its characteristics enables more precise predictions of space-related phenomena such as solar activity, and helps better determine errors in radio wave propagation through the ionosphere.

The following is a derivation of the ionospheric refractive index. If we assume a plane electromagnetic wave traveling along the x-axis of an orthogonal coordinate system in the presence of a uniform external magnetic field that makes an angle $\theta$ with the direction of wave propagation, we can find the ionospheric refractive index $n$ using the Appleton-Hartree equation [1]:

$$
n^2 = 1 - X(1 - i Z) - \frac{Y_T^2 (1 - X - i Z)^2}{2} 
\pm \frac{\sqrt{ Y_T^4 (1 - X - i Z)^4 + 4 Y_L^2 (1 - X - i Z)^2 }}{2}
$$

Where

$$
X = \frac{\omega_N^2}{\omega^2}, \quad
Y = \frac{\omega_H}{\omega}, \quad
Y_L = \frac{\omega_L}{\omega}, \quad
Y_T = \frac{\omega_T}{\omega}, \quad
Z = \frac{\omega_C}{\omega}
$$

Here, $\omega$ is the angular frequency of the carrier wave from the signal transmitter. Analogously, to the rest of the angular frequencies, $\omega_N$ is the angular frequency of the plasma, which is calculated by the formula $\omega_N^2 = \frac{N e^2}{\epsilon_0 m_e}$, with electron density $N$, electronic charge $e$, vacuum dielectric permittivity $\epsilon_0$, and electronic mass $m_e$, $\omega_H$ is the cyclotron angular frequency of free electrons, which is calculated by the formula $\omega_H = \frac{B_0 |e|}{m_e}$, with magnetic induction $B_0$, $\omega_T$ is the transverse component of $\omega_H$, and $\omega_L$ is the longitudinal component of $\omega_H$, defined as $\omega_T = \omega_H \sin \theta$ and $\omega_L = \omega_H \cos \theta$, and finally, $\omega_C$ is the angular frequency of collisions between electrons and heavy particles [1].

Under certain conditions, the collisions of heavy particles can be neglected ($Z \approx 0$). By expanding Equation (4) using a Taylor series and neglecting the influence of the magnetic field ($\theta \approx 0$), the ionospheric refractive index simplifies to:

$$
n = 1 - X^2 = 1 - \frac{f_N^2}{f^2}
$$

Where $f_N^2 = 80.6 N \, (\text{Hz}^2)$ as a function of electron density $N$.

To facilitate comparison of electron concentration in satellite trajectories with different elevation angles (slant TEC, sTEC), it is sometimes necessary to convert TEC values into their vertical equivalent (TECv). This represents the total number of electrons in a column perpendicular to the ground, under the thin-layer assumption of the ionosphere at a maximum altitude of 350 km. Accurate conversion from sTEC to TECv is essential for standardizing measurements, enabling meaningful integration into ionospheric models. Achieving this requires a robust, integrated system of hardware and software, and a dedicated team to research and implement the solution.


#### **Specifications**

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 aims to design and build a low-cost modular system with data logging to support continuous TEC data collection. The system will primarily use dual GNSS signals to gather TEC measurements in the ionosphere. These measurements will be validated against published ionospheric data. The system will log data at a rate appropriate for capturing significant variations in TEC while remaining efficient for storage and analysis. It will enable easy component replacement and offer multiple input ports to support user-driven expansions. Additional sensors may be included to further demonstrate modularity.

&nbsp; &nbsp; &nbsp; &nbsp; For safe operation in changing weather, the system will be waterproof up to an IPx4 ingress protection rating, allowing it to withstand splashing water from any direction, though it is not designed to be submerged \[5\]. The system shall also be securely mounted to a base to prevent displacement during severe weather.

&nbsp; &nbsp; &nbsp; &nbsp; The system will feature a reliable power source to enable continuous operation including battery and/or wall power. A dual-tuned antenna will receive signals from GNSS satellites simultaneously and a processing unit will perform calculations, converting the data into meaningful values. A storage system will record the collected data for later analysis. At minimum, the system will include a dual-tuned antenna, a processing unit, and a storage system.

&nbsp; &nbsp; &nbsp; &nbsp; All interior circuitry shall be simulated and tested thoroughly throughout the design and build process. Documentation of the design and build process will be published enabling enthusiasts to replicate the system at a cost below \$1,000.

#### **Constraints**

&nbsp; &nbsp; &nbsp; &nbsp; The system shall comply with all applicable regulatory requirements in the regions where it could be deployed. At a minimum, this includes compliance with international spectrum allocations defined by the International Telecommunication Union (ITU) for passive GNSS reception, and adherence to local wireless communication regulations for unlicensed ISM band operation \[6\]. Safety and environmental requirements shall follow internationally recognized standards for electronic equipment to ensure global replicability.

&nbsp; &nbsp; &nbsp; &nbsp; The system shall be designed for the purpose of receiving satellite signals to perform TEC calculations. No transmissions are made to satellites or external systems during the process. Consequently, the collection of TEC data constitutes passive reception and is permitted by international regulations. The receiver shall conform to the defined signal structure specifications of the GNSS bands it supports to ensure compatibility and measurement reliability \[7\]. For short range wireless communication, the system shall operate within approved ISM bands and comply with the applicable regional standards for those frequencies.

&nbsp; &nbsp; &nbsp; &nbsp; Public health and safety are of utmost concern. The system shall incorporate protective circuitry and automatic shutdowns to prevent hazards from overcurrent, overvoltage, or overheating. Additionally, the system shall pose no risks to users from sharp edges, fire, or unstable mounting.

## **Survey of Existing Solutions**

&nbsp; &nbsp; &nbsp; &nbsp; Several existing solutions for TEC measurement have been developed in both the amateur radio and scientific communities. A notable initiative is the Personal Space Weather Station (PSWS), an active project coordinated through the Ham Radio Science Citizen Investigation (HamSCI) \[8\]. The PSWS is designed as a modular system with different teams responsible for developing and documenting specific modules. These modules include single-channel Doppler monitors for tracking ionospheric disturbances, as well as ground-based magnetometers for measuring variations in the Earth's magnetic field. At its core, the PSWS seeks to make space weather research accessible to both professional researchers and amateur radio operators. The broader goal is to understand how ionospheric activity influences radio wave propagation.

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 is in contact with Dr. Anthea Jane Coster, a principal research scientist at Massachusetts Institute of Technology (MIT). Dr. Coster specializes in the physics of the ionosphere, magnetosphere, thermosphere, space weather, GNSS positioning and measurement accuracy, and radio wave propagation. She and her colleagues developed the first real-time ionospheric monitoring system based on GPS \[9\]. She has recommended that Team 6 consider using u-blox positioning chips and modules, widely used in this area of research.

&nbsp; &nbsp; &nbsp; &nbsp; A pertinent example of a low-cost GNSS based TEC measurement system utilizing u-blox positioning chip and module is the ScintPi 3.0, developed by Dr. Fabiano S. Rodrigues and Josemaria Gomez Socola \[10\]. Dr. Rodrigues, a professor of physics at University of Texas at Dallas (UTD), has extensive expertise in upper atmospheric physics, ionospheric electrodynamics, remote sensing, and GNSS studies. The ScintPi 3.0, built for approximately \$564, employs a GNSS antenna, u-blox GPS breakout boards, and a Raspberry Pi 3 Model B+ to gather scintillation measurements in two frequencies and estimates of the ionospheric TEC. The ScintPi 3.0 was compared against the commercial grade ionospheric GNSS monitoring reference receiver, the Septentrio PolaRx5S, which sells for approximately \$29,000 \[11\]. Results showed that the ScintPi 3.0 phase TEC measurements align closely with the phase TEC measurements provided by PolaRx5S.

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 has done a thorough investigation into existing solutions for TEC measurement and has highlighted two significant projects in this research area. In addition, Team 6 will continue to utilize all resources available to adaptively develop the system throughout the plan, design, and build process.

## **Measures of Success**

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 aims to measure the success of the TEC measurement system based on four factors: accuracy, reliability, usability, and cost-effectiveness.

- Accuracy
  - The system's ability to gather TEC data that has minimal deviation from the published TEC reference data.
  - The system's ability to reliably and accurately gather repeated readings are under the same conditions.
- Reliability
  - The system's resilience to faults, including battery life tests when applicable, emergency shutdown procedures, and performance under various environmental conditions.
  - The system's durability in running continuously
- Usability
  - The ease of replicability for hobbyists using reference materials provided by Team 6.
  - The system's capability to be transportable.
  - The system's modularity shall be for ease of adaptation, troubleshooting, and repairs.
- Cost-Effectiveness
  - A monetary goal of providing the system for under \$1,000.

## **Resources**

&nbsp; &nbsp; &nbsp; &nbsp; The proposed TEC measurement system requires a combination of specialized hardware and supporting components to achieve accurate data collection and long-term autonomous operation. A dual-band GNSS signal receiver will serve as the core of the system. The receiver will be connected to a processing unit, which will perform the necessary TEC calculations and interface with an external storage drive to create a dedicated data logging device.

&nbsp; &nbsp; &nbsp; &nbsp; The GNSS receiver will provide precise positioning and signal data necessary for TEC calculations as measured by the delay of two signals. To demonstrate modularity, including measurements of the Earth's magnetic field and solar light intensity, a magnetometer and light sensor may be integrated. Data processing and transmission will be handled by a dedicated processing unit capable of managing both the GNSS and sensor data streams.

&nbsp; &nbsp; &nbsp; &nbsp; Finally, mounting hardware and structural materials will be required to assemble the device into a robust and field-deployable apparatus. Additionally, a custom PCB may be developed to simplify assembly and enable quick interchange of components for repairs or future upgrades. To ensure complete safety for the public, Team 6 will also incorporate the proper protective devices.

### **Budget Document**

| Item | Price (\$) |
| --- | --- |
| Signal Receiver | 300 |
| Light Sensor | 20  |
| Dual Tuned Antenna | 75  |
| Mounting Material | 50  |
| PCB | 25  |
| Coaxial Cable | 40  |
| Raspberry Pi 5 | 80  |
| Raspberry Pi 5 heatsink | 10  |
| Micro SD card | 10  |
| USB to Sata | 10  |
| 1 TB 2.5" SSD | 50  |
| (3x) ESP 32 | 20  |
| Misc. Fuses and temp sensors | 25  |
| Battery with solar panel | 150 |
| Magnetometer | 15  |
| Waterproofing material | 40  |
| **Total** | **920** |

### **Personnel**

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 consists of members whose experience and expertise covers signal processing, programming, hardware construction, and technical writing. Individual skills as follows:

- Jack Bender: C/C++, MATLAB, Python, Assembly, LTSpice, KiCad, Soldering
- Kenneth Creamer: C/C++, Python, AutoCAD, SolidWorks, Soldering, MATLAB
- Blake Hudson: C/C++, Python/MicroPython, Assembly, VHDL, SolidWorks, AutoCAD, LTSpice, Soldering, Linux systems
- Nolan Magee: Solidworks, Technical writing, AutoCad, Revit, C++, Excel, Managment, Soldering
- Jackson Taylor: C/C++, MATLAB, VHDL, Telecommunications, Control Systems

&nbsp; &nbsp; &nbsp; &nbsp; These combined qualifications should be sufficient to successfully construct an apparatus capable of measuring, processing, and presenting TEC in the ionosphere. Team 6 shall work hard to diligently fill any gaps in understanding and expertise, as they are made aware, to provide the most optimal prototype possible.

&nbsp; &nbsp; &nbsp; &nbsp; The team has chosen Owen O'Connor as the supervisor for the project. He has extensive experience in embedded systems and shall be vital if the team experiences issues bridging the gap between hardware and software this project shall require. He is also one of the most qualified personnel at Tennessee Tech to provide feedback and support regarding signal processing.

&nbsp; &nbsp; &nbsp; &nbsp; The instructor is Dr. Christopher Johnson. The team's expectation for him is to function as quality assurance and quality control (QAQC) for the duration of the project. All major submittals will be vetted and approved by Dr. Johnson with the intention of refining the team's technical writing ability. He will also function as oversight in the case of interpersonal issues occurring within the group that are unable to be resolved by the team.

&nbsp; &nbsp; &nbsp; &nbsp; Team 6 has chosen Dr. Jeffery Austen as the customer. He has extensive experience with telecommunications and signal processing. He is extremely interested in measuring TEC and exciting the hobbyist community's desire to become more involved in TEC measurement. Dr. Austen's awareness of the field of study provides clarity for the direction of this project.

### **Timeline**

![Screenshot 2025-09-22 114404](https://hackmd.io/_uploads/B1Wrswvngx.png)

## **Specific Implications**

&nbsp; &nbsp; &nbsp; &nbsp; By developing a low-cost TEC measurement device, the project makes measuring TEC more accessible. Currently, large-scale ionospheric monitoring systems can be cost prohibitive, limiting widespread development. A system built under \$1,000 drastically reduces expense. By making it more affordable, researchers, universities, and others alike can replicate and contribute to space weather research and monitoring more easily. Making this method of data collection increasingly accessible means more geographically distributed measurements, expanding the availability of ionospheric data for increased accuracy in modeling.


## **Broader Implications, Ethics, and Responsibility as Engineers**

&nbsp; &nbsp; &nbsp; &nbsp; The deployment and use of TEC measurement systems have broader implications across scientific, societal, and environmental contexts. Accurate TEC measurements contribute to research on space weather and its effects on communication and navigation systems, but misuse or misinterpretation of data could negatively impact public or commercial applications. Ethical responsibilities include ensuring data integrity, adhering to regulations and copyright laws, minimizing environmental impact, and prioritizing public safety. Each engineer is responsible for conducting work with honesty, diligence, and awareness of the potential global and societal impacts of the system.

## **References**

\[1\] E. D. Lopez, R. E. Hidalgo, and M. J. Carrera, "Preliminary mapping of ionospheric total electron content (TEC) over Ecuador using global positioning system (GPS) data," arXiv preprint arXiv:2403.19053, 2024. \[Online\]. Available: <https://arxiv.org/abs/2403.19053> . \[Accessed: Sep. 20, 2025\].

\[2\] NOAA / NWS Space Weather Prediction Center, "Space Weather and GPS Systems," Space Weather Prediction Center, National Oceanic and Atmospheric Administration \[Online\]. Available: <https://www.swpc.noaa.gov/impacts/space-weather-and-gps-systems> . \[Accessed: Sep. 19, 2025\].

\[3\] NOAA / NWS Space Weather Prediction Center, "Ionosphere," Space Weather Prediction Center, National Oceanic and Atmospheric Administration, \[Online\]. Available: <https://www.swpc.noaa.gov/phenomena/ionosphere> . \[Accessed: Sep. 23, 2025\].

\[4\] A. Coster, "Using GNSS to Study Magnetosphere - Ionosphere Coupling," PowerPoint slides, MIT Haystack Observatory. \[Online\]. \[Accessed: Sep. 23, 2025\].

\[5\] B. Fogg, "IP rating guide: IP66, IPX7? Water-resistance explained," Reviews.org, Nov. 03, 2021. \[Online\]. Available: <https://www.reviews.org/au/mobile/ip-rating-guide/>. \[Accessed: Sep. 23, 2025\].

\[6\] "Radio Regulations - ITU," International Telecommunication Union, 2024. Accessed: Sep. 25, 2025. \[Online\]. Available: <https://www.itu.int/hub/publication/r-reg-rr-2024/> . \[Accessed: Sep. 21, 2025\].

\[7\] "Understanding satellite frequencies and GNSS receiver channels," Global GPS Systems. \[Online\]. Available: <https://globalgpssystems.com/gnss/understanding-satellite-frequencies-and-gnss-receiver-channels/> \[Accessed: Sep. 25, 2025\].

\[8\] "Personal Space Weather Station (PSWS) - Overview," HamSCI, 2025. \[Online\]. Available: <https://hamsci.org/psws-overview>. \[Accessed: Sep. 23, 2025\].

\[9\] "Anthea Jane Coster," MIT Haystack Observatory. \[Online\]. Available: <https://www.haystack.mit.edu/researcher/anthea-coster/>. \[Accessed: Sep. 23, 2025\].

\[10\] J. Gómez Socola and F. S. Rodrigues, "ScintPi 2.0 and 3.0: low-cost GNSS-based monitors of ionospheric scintillation and total electron content," Earth, Planets and Space, vol. 74, art. no. 185, Dec. 2022. \[Online\]. Available: <https://earth-planets-space.springeropen.com/articles/10.1186/s40623-022-01743-x>. \[Accessed: Sep. 23, 2025\].

\[11\] "Septentrio PolaRx5TR RTK OEM Board GNSS GPS Module," Alibaba, Product Detail. \[Online\]. Available: <https://www.alibaba.com/product-detail/Septentrio-Polarx5tr-RTK-OEM-Board-Precision_1601231199008.html>. \[Accessed: Sep. 23, 2025\].

\[12\] OpenAI, GPT-5, ChatGPT, San Francisco, CA, USA, 2025. \[Online\]. Available: <https://chat.openai.com/>. \[Accessed: Sep. 20, 2025\].

## **Statement of Contributions**

- Jack Bender: Specifications and Constraints, Survey of Existing Solutions, and Measures of Success, Final Review
- Kenny Creamer: Background, Specific Implications, References
- Blake Hudson: Broader Implications, Ethics, and Responsibility as Engineers, Resources, Specifications and Constraints
- Nolan Magee: Introduction, Budget, Personnel, Timeline, Final Review

- Jackson Taylor: Background



