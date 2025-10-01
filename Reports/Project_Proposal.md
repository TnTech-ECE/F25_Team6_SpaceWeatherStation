<h1 style="font-size:40px;">F25_Team 6_SpaceWeatherStation</h1>

## **Introduction**
&nbsp; &nbsp; &nbsp; &nbsp; Global reliance on communication, navigation, and positioning systems makes society increasingly vulnerable to disturbances in the ionosphere, where total electron content (TEC) refracts, delays, and disrupts radio signals. These disturbances reduce the accuracy and effectiveness of global navigation satellite system (GNSS) services, disrupting critical infrastructure in aviation, maritime operations, telecommunications, and everyday devices. Although anticipation of TEC interference could be limited by large amounts of accurately observed data, existing monitoring systems are often costly, technically complex, stationary, and geographically limited. This creates a barrier to broader participation in ionospheric research and limits the availability of distributed TEC measurements needed for accurate modeling.  

&nbsp; &nbsp; &nbsp; &nbsp; To address this challenge, Team 6 is developing a low-cost, modular, and replicable prototype capable of measuring TEC from dual-frequency GNSS signals. The system integrates an antenna, receiver, processing unit, and expandable modules within a single housing compartment to support mobility, while remaining under $1,000. Propagation of the prototype is supported by thorough documentation for seamless hobbyist replication. By normalizing access to TEC measurement, the project expands opportunities for education, grassroots research, and innovation. Moreover, it contributes to a distributed global database of ionospheric conditions, enhancing collective understanding of space weather and its implications for modern infrastructure. 

## **Formulating the Problem**

### **Background**

&nbsp; &nbsp; &nbsp; &nbsp; Modern society depends heavily on reliable communication and navigation systems, ranging from critical infrastructure to everyday Global Navigation Satellite Systems (GNSS)-enabled devices. Yet, these systems are constantly influenced by the ionosphere, a dynamic region of Earth’s upper atmosphere that can refract, delay, or disrupt radio signals. The most important parameter used to describe ionospheric effects is TEC. TEC refers to the total number of electrons present along a path between a signal transmitter and receiver. By definition, TEC is the integral of the electron density $N(s)$ along a path $ds$ between points $A$ and $B$ [1]:

$$
\text{TEC} = \int_A^B N_e(s) \, ds \quad (1)
$$

&nbsp; &nbsp; &nbsp; &nbsp; TEC varies considerably with time of day, geographic location, season, solar cycle, solar activity, geomagnetic storms, and atmospheric disturbances. The free electrons that make up TEC are concentrated in the ionosphere, roughly 80–600 km above Earth’s surface. In the ionosphere, atoms are ionized primarily by extreme ultraviolet (EUV) and x-ray solar radiation. The resulting electron density changes continuously with solar radiation and geomagnetic conditions. Additional disturbances, such as atmospheric waves and scintillation, further contribute to its variability. This dynamic behavior can both enhance long-distance radio communication and cause impairments such as delays, fading, scintillation, and even data loss [2][3][4]. Consequently, there is a strong demand for consistent measurement of electron content globally.

&nbsp; &nbsp; &nbsp; &nbsp; Due to the ionosphere being a plasma medium, the refractive index affects radio wave propagation. At high radio frequencies (HF), refraction caused by electrons can allow a radio signal to propagate over the horizon of the earth, allowing for an increased range of communication. However, TEC can also cause distortion and fading in the signal at these frequencies, resulting in data loss. At very high radio frequencies (VHF) and above, including GNSS, ionospheric effects appear as signal delays, phase shifts, and scintillation [1]. These disruptions reduce the accuracy and reliability of positioning, navigation, and timing (PNT) services critical to aviation, maritime, and telecommunication systems.  

&nbsp; &nbsp; &nbsp; &nbsp; By convention, the measurement of a total electron content unit (TECU) is defined as follows:

$$
1~\text{TECU} = 10^{16}~\text{electrons/m}^2 \quad (2)
$$

&nbsp; &nbsp; &nbsp; &nbsp; To mitigate or take advantage of the effects of TEC, its levels must be accounted for during radio transmission. As more information becomes available for TEC analysis, accuracy and predictability will increase, leading to more effective ways of transmitting signals. In addition, a wealth of TEC data provides more opportunity and interest for innovation to occur within emerging fields related to ionospheric conditions. 

&nbsp; &nbsp; &nbsp; &nbsp; One way to measure TEC is to compute the time delay between two signals being transmitted through the atmosphere. Two GNSS signals transmitted concurrently are received by an antenna connected to a signal processing unit. The difference of delay between the two signals is identified as a result. The delay of a signal passing through the ionosphere can be expressed as the integral of the ionospheric refractive index $n$ along the path $ds$ extending from the satellite at point $A$ to the receiver at point $B$. Equivalently, it can also be expressed as an added term in the measured pseudo-range $S$ [2].

$$
S = \rho - \int_A^B (n - 1) \, ds = \rho - 40.3 \frac{1}{f^2} \int_A^B N_e(s) \, ds = \rho - 40.3 \frac{\text{TEC}}{f^2} \quad (3)
$$

&nbsp; &nbsp; &nbsp; &nbsp;Here, $\rho$ is the distance between the satellite and receiver excluding atmospheric delays and $f$ is the frequency of the delayed signal. From the derivations below, we can see the delay of ionospheric signals is entirely dependent on TEC. Knowing TEC and its characteristics enables more precise predictions of space-related phenomena such as solar activity. Additionally, the errors in radio wave propagation through the ionosphere can be better determined.

&nbsp; &nbsp; &nbsp; &nbsp; The following is a derivation of the ionospheric refractive index. If we assume a plane electromagnetic wave traveling along the $x$-axis of the orthogonal coordinate system in the presence of a uniform external magnetic field that makes an angle $\theta$ with the direction of wave propagation, we can find the ionospheric refractive index $n$ using the Appleton-Hartree equation [1].


$$
n^2 = 1 - 
\Bigg(
\frac{
    X
}{
    (1 - i Z) 
    - \dfrac{Y_T^2}{2 (1 - X - i Z)} 
    \pm \sqrt{ \dfrac{Y_T^4}{4 (1 - X - i Z)^2} + Y_L^2 } 
}
\Bigg) \quad (4)
$$

Where

$$
X = \frac{\omega_N^2}{\omega^2}, \quad
Y = \frac{\omega_H}{\omega}, \quad
Y_L = \frac{\omega_L}{\omega}, \quad
Y_T = \frac{\omega_T}{\omega}, \quad
Z = \frac{\omega_C}{\omega}
$$

&nbsp; &nbsp; &nbsp; &nbsp; Here, $\omega$ is the angular frequency of the carrier wave from the signal transmitter. Analogously, to the rest of the angular frequencies, $\omega_N$ is the angular frequency of the plasma, which is calculated by the formula $\omega_N^2 = \frac{N e^2}{\epsilon_0 m_e}$, with electron density $N$, electronic charge $e$, vacuum dielectric permittivity $\epsilon_0$, and electronic mass $m_e$, $\omega_H$ is the cyclotron angular frequency of free electrons, which is calculated by the formula $\omega_H = \frac{B_0 |e|}{m_e}$, with magnetic induction $B_0$, $\omega_T$ is the transverse component of $\omega_H$, and $\omega_L$ is the longitudinal component of $\omega_H$, defined as $\omega_T = \omega_H \sin \theta$ and $\omega_L = \omega_H \cos \theta$, and finally, $\omega_C$ is the angular frequency of collisions between electrons and heavy particles [1].


&nbsp; &nbsp; &nbsp; &nbsp; Under certain conditions, the collisions of heavy particles can be neglected ($Z \approx 0$). Likewise, by expanding Equation (4) using a Taylor series and neglecting the influence of the magnetic field ($\theta \approx 0$), the ionospheric refractive index can be simplified greatly into the following expression [1].

$$
n = 1 - X^2 = 1 - \frac{f_N_e^2}{2f^2} = 1 - \frac{40.3 \, N_e}{f^2} \quad (5)
$$

Where $f_N^2 = 80.6 N \, (\text{Hz}^2)$ as a function of electron density $N$.

&nbsp; &nbsp; &nbsp; &nbsp; To facilitate the comparison of the electron concentration in satellite trajectories with different elevation angles, known as slant TEC (sTEC), it is sometimes necessary to convert the TEC values into their vertical equivalent (TECv). This parameter represents the total number of electrons in a column perpendicular to the ground. This transformation is performed under the assumption that the ionosphere can be approximated as a thin layer compressed at a maximum altitude of 350 km. Accurately converting TEC measurements from sTEC into TECv is essential for standardizing measurements. Ionospheric data models often utilize TECv data as an alternative to sTEC, enabling meaningful comparison and integration into ionospheric models.  

&nbsp; &nbsp; &nbsp; &nbsp; The scope required to build a TEC measurement system encompasses many fields of learning within engineering. A single person interested in building said system has a high likelihood of becoming overwhelmed due to the complexity involved. This necessitates having a team of individuals to research and distill the information into a condensed process. By this, a hobbyist can mitigate the time and expertise needed to complete a system capable of measuring TEC. 

&nbsp; &nbsp; &nbsp; &nbsp;Another limiting factor to widespread involvement in measuring TEC is the expense of required equipment. Thus, the goal of this project is to create a replicable, open sourced, affordable system by which, hobbyists with some technical background, is enabled in their pursuit of observing TEC.


### **Specifications**

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has consulted with the customer and developed preliminary system specifications and constraints to guide the design. These are outlined in the following sections. 

##### System Capabilities

- The system shall use a dual-tuned antenna to receive two signals from GNSS satellites simultaneously to obtain direct measurements of TEC.  
- The system shall feature a signal processing unit capable of converting received GNSS signals into meaningful measurements, such as TEC values. This may be implemented using a DSP module or equivalent hardware.  
- The system may include a signal monitoring capability that computes metrics such as signal-to-noise ratio (SNR), carrier-to-noise density (C/N), or equivalent measures to assess the reliability of received GNSS signals.  
- The system may have the capability to measure ionospheric scintillation events.  
- The system shall include a microcontroller or single-board computer to perform calculations, data logging, and interface management.  
- The system shall log data at a rate appropriate for capturing significant variations in TEC while remaining efficient for storage and analysis. Currently, a frequency of one measurement every three seconds per satellite is being considered.  
- The system shall have a storage system to record collected data from all applicable sensors for later analysis.  
- The system shall feature a reliable power source to enable continuous operation including battery and/or wall power.  

##### Modularity and Expandability

- The system shall enable easy component replacement.  
- The system shall offer multiple input ports to support user-driven expansions.  
- The system may include additional sensors to further demonstrate modularity.  

##### Physical Reliability

- The system shall be waterproof up to an IPx4 ingress protection rating, allowing it to withstand splashing water from any direction, though it is not designed to be submerged [5].  
- The system shall be securely mounted to a base to prevent displacement during severe weather.  

##### Documentation and Replicability

- Documentation of the design and build process shall be published, enabling enthusiasts to replicate the system at a cost below $1,000.  

### **Constraints**
##### Regulatory Compliance

- The system shall meet all applicable regulatory requirements in its deployment region, including spectrum allocations for passive GNSS reception as defined by the International Telecommunication Union (ITU) [6], and local regulations governing unlicensed ISM band operation.  
- The receiver shall conform to the signal structure specifications of the GNSS bands it supports to ensure compatibility and measurement reliability [7].  
- For short-range wireless communication, the system shall operate within approved ISM bands and comply with the applicable regional standards for those frequencies.  

##### Operational Guidelines

- The system shall be designed for passive reception of satellite signals to perform TEC calculations.  
- The system shall not transmit to satellites or external systems.  
- The system may transmit collected data to a local host device, such as a personal computer at the deployment site, for storage or further processing.  

##### Safety and Environmental Guidelines

- The system shall include protective circuitry and automatic shutdowns to prevent hazards from overcurrent, overvoltage, or overheating.  
- The system shall pose no risks to users from sharp edges, fire, or unstable mounting.  
- Safety and environmental requirements shall comply with internationally recognized standards for electronic equipment.  


## **Survey of Existing Solutions**


&nbsp; &nbsp; &nbsp; &nbsp;Several existing solutions for TEC measurement have been developed in both the amateur radio and scientific communities. Team 6 has surveyed these solutions, identifying three systems that will particularly guide the design process.  

### HamSCI Personal Weather Station (PSWS)

&nbsp; &nbsp; &nbsp; &nbsp;The HamSCI PSWS is an active project coordinated through HamSCI, designed as a modular, low-cost system designed to enable ground-based measurements of the ionosphere [8]. Different teams develop specific modules, such as single-frequency Doppler monitors for ionospheric disturbances and ground magnetometers, which can be combined in multi-instrument setups. The data collected by individual PSWS units are aggregated into a central database for space science and space weather research. Each module is designed to be easily replicable by hobbyists, educators, and citizen scientists at a price between $100 and $1,000. The system fosters collaboration across several reputable institutions including MIT Haystack Observatory, National Science Foundation, and NASA, providing ionospheric data for research purposes. At its core, the PSWS seeks to make space weather research accessible to both professional researchers and amateur radio operators.  

**Pros**  

- **Accessible price point ($100-$1,000):** Affordable for citizen scientists, schools, and amateur radio operators.  
- **Community-driven development:** Strong institutional backing (MIT Haystack Observatory, National Science Foundation, NASA, etc.) and community support ensuring ongoing improvements and documentation.  
- **Modular architecture:** Allows users to start with a single instrument and expand it later.  
- **Established data network:** Data contributions are aggregated into a central repository for broader research impact.  

**Cons**  

- **No dual-frequency GPS capability:** None of the current modules implement dual-frequency GNSS signals for direct TEC measurement.  
- **No direct TEC measurement:** Modules do not directly measure TEC. Instead, they infer it with other observations such as Doppler shifts or variations in the Earth’s magnetic field.  
- **Single-purpose modules:** Each module performs only one specific measurement, requiring multiple devices to study various phenomena, increasing overall cost and complexity.  
- **No unified interface:** While individual module data can be uploaded to the central repository, users must manually submit each dataset. Data from different modules is not stored in the same location during capture.  

**Gaps**  

- **No dual frequency GNSS TEC sensing:** Current modules cannot directly measure TEC using dual-frequency GNSS signals, limiting the precision of ionospheric observations.  
- **Lack of integrated multi-sensor platforms:** Emphasizes modularity but does not offer a single apparatus that combines several sensors.  
- **Limited portability and deployment flexibility:** Some modules assume fixed positions, with minimal emphasis on mobility or rapid deployment configurations.  

**Takeaways**  

- **Cost-effective target:** Team 6 adopts the PSWS price target of $100-$1,000 to build an accessible system for hobbyists, educators, and researchers.  
- **Integrated multi-sensor platform:** Unlike PSWS, Team 6 will build a single apparatus capable of modular expansion of multiple sensors. This reduces hardware complexity and deployment efforts.  
- **Direct TEC measurement with dual-frequency GNSS signals:** Team 6 intends to gather direct measurements of TEC rather than inferring values from related observations, improving precision and scientific value.  
- **Unified interface:** Team 6 will aggregate all data into a single platform for streamlined access and analysis.  
- **Modular design:** Team 6 adopts the PSWS concept of modularity, but implements it within a single, integrated apparatus, combining multiple sensors while maintaining expandability.  
- **Collaboration with HamSCI:** Team 6 may engage with HamSCI to share the prototype and contribute collected data to the existing PSWS data repository, supporting broader space weather research.  

### Millstone Real-Time TEC Ionospheric Monitoring System

&nbsp; &nbsp; &nbsp; &nbsp;The Millstone Real-Time TEC Ionospheric Monitoring System, developed at MIT Lincoln Laboratory, uses dual-frequency GPS signals to measure TEC. The system was designed to support the Millstone Hill Observatory satellite-tracking radar by providing real-time TEC values. Measurements are gathered every three seconds for each satellite in view and are processed through a Kalman filter to account for ionospheric effects on the radar’s wave propagation [9]. The system utilizes a T14100 GPS receiver developed by Texas Instruments in the 1980s [10]. This receiver is capable of tracking four satellites, concurrently receiving L1 (1575.42 MHz) and L2 (1227.6 MHz) frequencies. The TEC along the path to each satellite is determined by combining both frequencies using the pseudo-range and the integrated phase data. At the Millstone radar frequency of 1295 MHz, implementing the dual-frequency GPS TEC correction reduced the standard deviation from 5.3m to 1.4m [9]. This implementation establishes the dual-frequency TEC correction as a state-of-the-art approach for reducing ionospheric range errors.  

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 is in contact with Dr. Anthea Jane Coster, a principal research scientist at Massachusetts Institute of Technology (MIT) and developer of the Millstone TEC monitoring system, the first system built for real-time TEC measurements. Dr. Coster specializes in the physics of the ionosphere, magnetosphere, thermosphere, space weather, GNSS positioning and measurement accuracy, and radio wave propagation [11]. Team 6 may consult her for guidance or to clarify technical questions. She has also recommended the use of u-blox positioning chips and modules, which are widely used in ionospheric research.  

**Pros**  

- **Real-time TEC measurements:** Provides direct ionospheric TEC values updated every three seconds.  
- **Dual-frequency GPS capability:** Uses L1 and L2 signals to directly measure ionospheric delays, improving TEC measurement accuracy.  
- **Proven performance:** Demonstrates highly accurate, reliable TEC measurements, establishing a benchmark for real-time TEC measurements.  
- **Concurrent satellite monitoring:** Capable of measuring TEC from four satellites simultaneously.  

**Cons**  

- **Outdated hardware:** The T14100 is an outdated piece of hardware no longer in production.  
- **Limited portability:** Designed for fixed positions, not suitable for field deployable or mobile setups.  
- **Limited satellite tracking:** The T14100 limits the user to tracking four satellites simultaneously.  

**Gaps**  

- **Single-purpose system:** The system only focuses on gathering TEC values, not integrating additional sensors for further space weather observations.  
- **Limited accessibility:** Designed for a particular solution to radar range errors and is therefore not easily replicable.  
- **Limited TEC measurement resolution:** Few satellites and sampling points make it harder to interpolate TEC across space and time, reducing the detail of ionospheric mapping.  

**Takeaways**  

- **Dual-frequency TEC benchmark:** Dr. Coster’s system demonstrates integration of the electron density along a satellite-receiver path reliably produces accurate TEC measurements, guiding Team 6’s design approach.  
- **Sample rate:** Team 6 may adopt the sample rate of measuring every three seconds per satellite in view.  
- **Concurrent satellite tracking:** Team 6 intends to track multiple satellites concurrently to increase sampling points in support of better accuracy for ionospheric models.  
- **Expert guidance available:** Team 6 may occasionally consult Dr. Coster, whose expertise provides valuable insight into the design and validation decisions.  

### ScintPi 3.0: Low Cost GNSS Ionospheric Monitor

&nbsp; &nbsp; &nbsp; &nbsp;A pertinent example of a low-cost GNSS based TEC measurement system utilizing u-blox positioning chip and module is the ScintPi 3.0, developed by Dr. Fabiano S. Rodrigues and Josemaria Gomez Socola [12]. Dr. Rodrigues, a professor of physics at University of Texas at Dallas (UTD), has extensive expertise in upper atmospheric physics, ionospheric electrodynamics, remote sensing, and GNSS studies. The ScintPi 3.0, built for approximately $564, employs a GNSS antenna, u-blox SparkFun GPS Breakout-ZED-F9P ($275.00), and a Raspberry Pi 3 Model B+ to gather scintillation measurements in two frequencies and estimates of the ionospheric TEC. While not intended to fully replace commercial-grade ionospheric monitors, it proves a low-cost alternative for distributed observation, educational purposes, and citizen science initiatives [12].  

&nbsp; &nbsp; &nbsp; &nbsp;The ScintPi has been validated against the commercial-grade Septentrio PolaRx5S, which sells for approximately $29,000 [13]. Results showed that the ScintPi 3.0 phase TEC measurements align closely with those from the PolaRx5S, demonstrating its reliability and accuracy. The system has been deployed in Brazil, where it successfully detected scintillation events and TEC depletions, such as those associated with equatorial plasma bubbles [12]. These measurements illustrate how an easily deployable, low-cost TEC monitoring system can quickly be set up to observe and study ionospheric irregularities, making it accessible to hobbyists, educators, and citizen scientists alike.  

**Pros**  

- **Low-cost design:** Built for approximately $564, making it highly affordable compared to commercial systems like the Septentrio PolaRx5S.  
- **Dual-frequency TEC measurements:** Uses u-blox GPS breakout boards (ZED-F9P) to compute TEC from the difference in carrier phase between two GNSS signals, providing direct ionospheric observations.  
- **Validated performance:** Phase TEC measurements closely match those of a commercial reference receiver, demonstrating reliability and accuracy.  
- **Multi-constellation support:** The system has the capability of receiving signals from several GNSS constellations such as GPS, GLONASS, GALILEO, and BeiDou.  
- **Easily deployable:** The system can be easily set up in the field, allowing for flexible monitoring and rapid data collection.  
- **Supports citizen science and education:** Designed for use by hobbyists, educators, and citizen scientists. The system’s low cost enables broader participation and makes establishing multi-site observation networks more feasible.  

**Cons**  

- **Single-purpose design:** Focuses on TEC and scintillation measurements, not including additional sensors for broader space weather monitoring.  
- **Hardware dependency:** Relies on off-the-shelf components that may have limited processing power compared to a research-grade system.  
- **Limited runtime:** Due to size constraints, the system has a runtime limited to the power supply of the Raspberry Pi.  
- **Data redundancy:** Continuous long-term data logging may require frequent data offload or larger SD card.  

**Gaps**  

- **Limited time resolution:** Continuous monitoring over long-time frames may require additional hardware such as power supplies or storage mediums.  
- **Data redundancy:** SD card failure or corruption could result in data loss. The system lacks cloud or remote storage integration.  

**Takeaways**  

- **Affordable benchmark:** The ScintPi 3.0 demonstrates that low-cost hardware can reliably measure TEC and detect scintillation events, guiding Team 6 in a budget-conscious system design.  
- **Rapid deployment:** Shows the benefits of field-deployable systems capturing certain ionospheric events quickly.  
- **Multi-constellation capability:** The system can receive signals from various satellites, demonstrating that Team 6’s design can be replicated globally.  

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has conducted a thorough investigation of existing TEC measurement solutions, highlighting three significant projects in this research area. The team will continue to leverage all available resources to adaptively develop the system throughout the planning, design, and build process. Insights from the survey have strongly influenced the project’s specifications and constraints, confirming feasibility, clarifying limitations, and defining key design priorities and preferences.



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





























