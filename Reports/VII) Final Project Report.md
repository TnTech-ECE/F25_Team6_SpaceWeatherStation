<h1 style="font-size:40px;">F25_Team 6_SpaceWeatherStation</h1>

## **Introduction**
&nbsp; &nbsp; &nbsp; &nbsp; Global reliance on communication, navigation, and positioning systems makes society increasingly vulnerable to disturbances in the ionosphere, where variations in electron density refract, delay, and disrupt radio signals. These effects are commonly quantified using total electron content (TEC). These disturbances reduce the accuracy and effectiveness of global navigation satellite system (GNSS) services, disrupting critical infrastructure in aviation, maritime operations, telecommunications, and everyday devices. Although anticipation of TEC interference could be limited by large amounts of accurately observed data, existing monitoring systems are often costly, technically complex, stationary, and geographically limited. This creates a barrier to broader participation in ionospheric research and limits the availability of distributed TEC measurements needed for accurate modeling.

&nbsp; &nbsp; &nbsp; &nbsp; To address this challenge, Team 6 is developing a low-cost, modular, and replicable prototype capable of measuring TEC from dual-frequency GNSS signals. The system integrates an antenna, receiver, processing unit, and expandable modules within a single housing compartment to support mobility, while remaining under \$1,000. Propagation of the prototype is supported by thorough documentation for seamless hobbyist replication. By normalizing access to TEC measurement, the project expands opportunities for education, grassroots research, and innovation. Moreover, it contributes to a distributed global database of ionospheric conditions, enhancing collective understanding of space weather and its implications for modern infrastructure.

&nbsp; &nbsp; &nbsp; &nbsp; The scope of this proposal outlines the background of TEC measurement and a thorough survey of existing solutions. This addresses the theoretical background and successful implementation of TEC measurement systems by others. This will clarify the need for the project, identify limiting factors, and inform the project specifications to maintain focus. The proposal will then define what constitutes a successful outcome, supported by details regarding budget, available and required expertise, and a timeline of key milestones. Finally, the proposal will conclude with a discussion of specific and broader implications of successfully completing the project.

## **Formulating the Problem**

### **Background**

&nbsp; &nbsp; &nbsp; &nbsp; Modern society depends heavily on reliable communication and navigation systems, ranging from critical infrastructure to everyday Global Navigation Satellite Systems (GNSS)-enabled devices. Yet, these systems are constantly influenced by the ionosphere, a dynamic region of Earth’s upper atmosphere that can refract, delay, or disrupt radio signals. The most important parameter used to describe ionospheric effects is TEC. TEC refers to the total number of free electrons present along a path between a signal transmitter and receiver. By definition, TEC is the integral of the electron density $N(s)$ along a path $ds$ between points $A$ and $B$ [1]:

$$
\text{TEC} = \int_A^B N_e(s) \ ds \quad (1)
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
S = \rho - \int_A^B (n - 1) \ ds = \rho - 40.3 \frac{1}{f^2} \int_A^B N_e(s) \ ds = \rho - 40.3 \frac{\text{TEC}}{f^2} \quad (3)
$$

&nbsp; &nbsp; &nbsp; &nbsp;Here, $\rho$ is the distance between the satellite and receiver excluding atmospheric delays and $f$ is the frequency of the delayed signal. From the derivations below, we can see the delay of ionospheric signals is entirely dependent on TEC. Knowing TEC and its characteristics enables more precise predictions of space-related phenomena such as solar activity. Additionally, the errors in radio wave propagation through the ionosphere can be better determined.

&nbsp; &nbsp; &nbsp; &nbsp;While the ionospheric delay is directly proportional to TEC, other sources of error can corrupt its estimation. These include tropospheric delay, satellite and receiver clock biases, multipath effects, and instrumental biases within the GNSS hardware. Additionally, noise and orbital uncertainties can introduce further inaccuracies. To isolate TEC, these effects must be modeled, minimized, or corrected through dual-frequency measurements and calibration techniques.

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
n = 1 - \frac{X}{2} = 1 - \frac{f_{N_e}^2}{2 f^2} = 1 - \frac{40.3 \ N_e}{f^2} \quad (5)
$$

Where $f_{N_e}^2 = 80.6 N \, (\text{Hz}^2)$ as a function of electron density $N_e$.

&nbsp; &nbsp; &nbsp; &nbsp; To facilitate the comparison of the electron concentration in satellite trajectories with different elevation angles, known as slant TEC (sTEC), it is sometimes necessary to convert the TEC values into their vertical equivalent (TECv). This parameter represents the total number of electrons in a column perpendicular to the ground. This transformation is performed under the assumption that the ionosphere can be approximated as a thin layer compressed at a maximum altitude of 350 km. Accurately converting TEC measurements from sTEC into TECv is essential for standardizing measurements. Ionospheric data models often utilize TECv data as an alternative to sTEC, enabling meaningful comparison and integration into ionospheric models.

&nbsp; &nbsp; &nbsp; &nbsp; It is important to note that the sampling rate of the receiver introduces a spatial averaging effect along the satellite-to-receiver path. As the GNSS signal traverses the ionosphere, both the satellite and ionospheric pierce point are in motion. A finite sampling interval therefore corresponds to a distance traveled through the ionosphere, effectively “blurring” fine-scale electron density variations. Higher sampling rates reduce this effect and improve the spatial resolution of TEC measurements.

&nbsp; &nbsp; &nbsp; &nbsp; The scope required to build a TEC measurement system encompasses many fields of learning within engineering. A single person interested in building said system has a high likelihood of becoming overwhelmed due to the complexity involved. This necessitates having a team of individuals to research and distill the information into a condensed process. By this, a hobbyist can mitigate the time and expertise needed to complete a system capable of measuring TEC. 

&nbsp; &nbsp; &nbsp; &nbsp;Another limiting factor to widespread involvement in measuring TEC is the expense of required equipment. Thus, the goal of this project is to create a replicable, open sourced, affordable system by which, hobbyists with some technical background, is enabled in their pursuit of observing TEC.


### **Specifications**

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 has consulted with the customer and developed preliminary system specifications and constraints to guide the design. These are outlined in the following sections. 

**System Capabilities**

- The system shall use a dual-tuned antenna to receive two signals from GNSS satellites simultaneously to obtain direct measurements of TEC.  
- The system shall feature a signal processing unit capable of converting received GNSS signals into meaningful measurements, such as TEC values. This may be implemented using a DSP module or equivalent hardware.  
- The system may include a signal monitoring capability that computes metrics such as signal-to-noise ratio (SNR), carrier-to-noise density (C/N), or equivalent measures to assess the reliability of received GNSS signals.  
- The system may have the capability to measure ionospheric scintillation events.  
- The system shall include a microcontroller or single-board computer to perform calculations, data logging, and interface management.  
- The system shall log data at a rate appropriate for capturing significant variations in TEC while remaining efficient for storage and analysis. Currently, a frequency of one measurement every three seconds per satellite is being considered.  
- The system shall have a storage system to record collected data from all applicable sensors for later analysis.  
- The system shall feature a reliable power source to enable continuous operation including battery and/or wall power.  

**Modularity and Expandability**

- The system shall enable easy component replacement.  
- The system shall offer multiple input ports to support user-driven expansions.  
- The system may include additional sensors to further demonstrate modularity.  

**Physical Reliability**

- The system shall be waterproof up to an IPx4 ingress protection rating, allowing it to withstand splashing water from any direction, though it is not designed to be submerged [5].  
- The system shall be securely mounted to a base to prevent displacement during severe weather.  

**Documentation and Replicability**

- Documentation of the design and build process shall be published, enabling enthusiasts to replicate the system.
- The system shall be replicable for a maximum cost of $1,000.  

### **Constraints**
**Regulatory Compliance**

- The system shall meet all applicable regulatory requirements in its deployment region, including spectrum allocations for passive GNSS reception as defined by the International Telecommunication Union (ITU) [6], and local regulations governing unlicensed ISM band operation.  
- The receiver shall conform to the signal structure specifications of the GNSS bands it supports to ensure compatibility and measurement reliability [7].  
- For short-range wireless communication, the system shall operate within approved ISM bands and comply with the applicable regional standards for those frequencies.  

**Operational Guidelines**

- The system shall be designed for passive reception of satellite signals to perform TEC calculations.  
- The system shall not transmit to any satellites.  
- The system may transmit collected data to a local host device, such as a personal computer at the deployment site, for storage or further processing.  

**Safety and Environmental Guidelines**

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

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 aims to measure the success of the TEC measurement system based on four factors: accuracy, reliability, usability and accessibility, and cost-effectiveness. Below are the definitions of these factors with respect to the system and specific success criteria within each factor. Additionally, a testing methodology section briefly describes how the prototype will be tested. 

#### Accuracy

- The system's ability to gather TEC data with minimal deviation from published TEC reference data. 

    - TEC measurements shall be validated against published ionospheric data, where the measured data demonstrates agreement to the reference data. 
    - Each set of TEC measurements taken shall be sufficiently large to confirm accuracy. Each set shall span at least 60 minutes of data.  
    - Team 6 is considering capturing a TEC measurement every 3 seconds per viewable satellite.
- The system’s ability to reliably and accurately gather repeated readings under similar conditions.
    - Each of Team 6’s measured datasets will be cross-referenced with datasets previously measured in similar conditions, with a deviation below 15%.  

#### Reliability

- The system’s resilience to faults, including emergency shutdown procedures and performance under various environmental conditions. 
    - The system shall be designed to withstand and operate during external temperature extremes (0 to 105 degrees Fahrenheit). 
    - The system shall automatically shut down when its core approaches an unsafe temperature, mitigating damage in the event of overheating and safely storing measured data. An interior thermal sensor shall initiate shutdown procedures. 
    - The system shall withstand and operate during moderate rainfall without damage.
- The system’s ability to operate over extended periods of time.
    - The system shall be designed to last a minimum of 24 hours on battery life alone.
    - For use with a battery and solar panel in conjunction, it shall operate perpetually (assuming adequate data storage), given it receives at least 6 hours of solar charging a day.
    - The system shall be able to run indefinitely when connected to a continuous power source (assuming adequate data storage).  

#### Usability and Accessibility

- The ease of replicability for hobbyists using reference materials provided by Team 6. 

    - All publications and open-sourced documentation shall be sufficiently detailed and up to supervisor's standards. 
    - Each component shall be easily accessible for purchase globally at the time of publication.
- The system’s capability to be transportable.
    - The system shall be able to fit within a one cubic foot enclosure, excluding a mounting system.
    - The system shall weigh under 25 lbs.
- The system’s modularity shall be for ease of adaptation, troubleshooting, and repairs.
    - The system shall consist of discrete components for streamlined repairs.
    - Team 6 is capable of demonstrating full modularity by exchanging components connected to the prototype.  

#### Cost-Effectiveness

- The sum of all the system’s components shall be under $1,000.  

#### Testing Methodology

- Accuracy
    - Each iteration of Team 6’s prototype shall record data for a minimum of one hour. 
    - To represent improvement in measurement accuracy, all datasets gathered throughout the project lifecycle shall be compiled in a single document.  

- Reliability
    - Before testing a prototype’s resilience to environmental factors, the housing of the system shall be tested thoroughly.  
    - Each component of the system shall be thoroughly stress tested to confirm full functionality prior to extended field use.  

- Usability
    - The prototype shall be fully assembled and disassembled. This will evaluate the system’s mobility and ease of deployment.  


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
| Processing Unit | 100  |
| Micro SD card | 10  |
| USB to Sata | 10  |
| 1 TB 2.5" SSD | 50  |
| (3x) ESP 32 | 20  |
| Misc. Fuses and temp sensors | 25  |
| Battery with solar panel | 150 |
| Magnetometer | 15  |
| Waterproofing material | 40  |
| **Total** | **930** |

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

&nbsp; &nbsp; &nbsp; &nbsp;Affordability is perhaps the most transformative aspect of this project, because cost is the single greatest barrier to widespread TEC monitoring. Commercial-grade systems often cost tens of thousands of dollars, restricting their deployment to government institutions and well-funded laboratories. By delivering a design that remains under $1,000, this project dramatically lowers the financial threshold for participation. Affordability directly enables scalability. Instead of a handful of centralized monitoring stations, hundreds of low-cost devices can be deployed across the globe. This normalization of TEC measurement ensures broader geographic coverage, critical for improving the accuracy of ionospheric models. Moreover, affordability aligns with educational and grassroots initiatives, allowing schools, universities, and hobbyists to contribute to scientific data collection in ways previously inaccessible. 

&nbsp; &nbsp; &nbsp; &nbsp; Unlike traditional rigid and specialized TEC measurement systems, Team 6’s prototype is intentionally structured for components to be exchanged or additional components included without redesigning the entire prototype. This modular architecture benefits both the scope and design process. From a development perspective, modularity allows individual subsystems, such as the dual-frequency receiver, processing unit, or auxiliary sensors. Components shall be chosen and tested independently, simplifying troubleshooting and iterative refinement. For a hobbyist, modularity ensures the system is adaptable to future needs, enabling the integration of additional sensors to broaden the scope of collected data. This adaptability positions the system to be more than a static design, paving the way for ongoing experimentation, innovation, and collaborative research. 

&nbsp; &nbsp; &nbsp; &nbsp; Making this system accessible ensures the device can be used and understood by a wide audience, not just specialists. Accessibility in this context includes clear documentation, open-source software, and the use of commonly available hardware. This empowers a diverse user base of university researchers, educators, and hobbyists alike to replicate, deploy, and contribute data with confidence. For customers and end users, accessibility means inclusion in advanced space weather research, removing technical barriers. They can meaningfully participate in a global scientific effort, with the device serving as both a research tool and educational platform. Emphasizing accessibility strengthens the project’s ability to generate widespread impact. As more people use the device, more geographically distributed data is collected, adding significant value to the global community. 

&nbsp; &nbsp; &nbsp; &nbsp; The uniqueness of this project lies in its ability to bridge the gap between high-end scientific instrumentation and practical, community-driven research tools. By simultaneously solving the challenges of modularity, accessibility, and affordability, the system invites an unprecedented level of participation in TEC measurement. This ensures ionospheric monitoring can evolve beyond a specialized, resource-limited activity into a globally distributed, collaborative effort. In turn, this may ultimately lead to better models, more accurate predictions, and greater resilience of the technologies that depend on reliable GNSS services.



## **Broader Implications, Ethics, and Responsibility as Engineers**

&nbsp; &nbsp; &nbsp; &nbsp; The deployment and use of TEC measurement systems carry broad implications across scientific, societal, and environmental contexts. In the scientific realm, accurate TEC data supports the study of ionospheric behavior, space weather phenomena, and their impact on systems dependent on satellite communication and navigation. These measurements aid researchers in understanding global atmospheric processes and support engineers in improving models capable of predicting disruptions in GPS and other critical services. Without reliable data, entire fields of research are limited in their ability to explain or mitigate natural events influencing everyday technologies. 

&nbsp; &nbsp; &nbsp; &nbsp; From a societal perspective, TEC data underpins technologies many people intuitively rely on. Reliable navigation for aviation, maritime travel, and emergency response services all depend on the stable functioning of GNSS signals. Accurate TEC monitoring can prevent accidents, optimize transportation, and ensure that first responders have trustworthy positioning data in critical situations. Conversely, misuse or misinterpretation of TEC data could lead to faulty predictions or misguided public communication. This has the potential to undermine trust in technology or cause financial and operational losses for dependent industries. 

&nbsp; &nbsp; &nbsp; &nbsp; Ethical responsibilities also play a role when deploying TEC systems. Engineers and researchers must ensure accuracy and integrity in the data they collect and distribute. This requires validating measurements, properly calibrating equipment, and transparently documenting methodologies. Upholding copyright and regulatory standards are equally important. TEC data often involves international collaboration and shared satellite infrastructure. Adhering to such regulations protects intellectual property rights and ensures global research efforts remain cooperative rather than competitive. 

&nbsp; &nbsp; &nbsp; &nbsp; Environmental considerations extend beyond scientific scope. The design and deployment of TEC systems should strive to minimize their environmental footprint through careful selection of energy-efficient components, sustainable materials, and responsible disposal of outdated hardware. Engineers should also consider the broader ecosystem of satellite launches, ground stations, and electronic waste, recognizing that every stage of system development carries environmental costs. 

&nbsp; &nbsp; &nbsp; &nbsp; Finally, public safety must remain a priority. TEC measurement systems, while highly technical, ultimately serve the purpose of safeguarding critical infrastructure and ensuring that society can operate smoothly even during ionospheric disturbances. Engineers must approach their work with honesty and diligence, acknowledging the outputs of their systems could influence decisions with global impact. A strong awareness of these societal responsibilities helps ensure technological progress contributes positively to the public good rather than introducing new risks.


## **References**
[1]  E. D. Lopez, R. E. Hidalgo, and M. J. Carrera, “Preliminary mapping of ionospheric total electron content (TEC) over Ecuador using global positioning system (GPS) data,” arXiv preprint arXiv:2403.19053, 2024. [Online]. Available: https://arxiv.org/abs/2403.19053. [Accessed: Sep. 20, 2025].  

[2]  NOAA / NWS Space Weather Prediction Center, “Space Weather and GPS Systems,” Space Weather Prediction Center, National Oceanic and Atmospheric Administration. [Online]. Available: https://www.swpc.noaa.gov/impacts/space-weather-and-gps-systems. [Accessed: Sep. 19, 2025].  

[3]  NOAA / NWS Space Weather Prediction Center, “Ionosphere,” Space Weather Prediction Center, National Oceanic and Atmospheric Administration. [Online]. Available: https://www.swpc.noaa.gov/phenomena/ionosphere. [Accessed: Sep. 23, 2025].  

[4]  A. Coster, “Using GNSS to Study Magnetosphere - Ionosphere Coupling,” PowerPoint slides, MIT Haystack Observatory. [Online]. [Accessed: Sep. 23, 2025].  

[5]  B. Fogg, “IP rating guide: IP66, IPX7? Water-resistance explained,” Reviews.org, Nov. 03, 2021. [Online]. Available: https://www.reviews.org/au/mobile/ip-rating-guide/. [Accessed: Sep. 23, 2025].  

[6]  “Radio Regulations – ITU,” International Telecommunication Union, 2024. [Online]. Available: https://www.itu.int/hub/publication/r-reg-rr-2024/. [Accessed: Sep. 21, 2025].  

[7]  “Understanding satellite frequencies and GNSS receiver channels,” Global GPS Systems. [Online]. Available: https://globalgpssystems.com/gnss/understanding-satellite-frequencies-and-gnss-receiver-channels/. [Accessed: Sep. 25, 2025].  

[8]  “Personal Space Weather Station (PSWS) — Overview,” HamSCI, 2025. [Online]. Available: https://hamsci.org/psws-overview. [Accessed: Sep. 23, 2025].  

[9]  U.S. Defense Technical Information Center, ADA256916. [Online]. Available: https://apps.dtic.mil/sti/tr/pdf/ADA256916.pdf. [Accessed: Sep. 30, 2025].  

[10]  P. Ward, Texas Instruments TI 4100 NAVSTAR Navigator, ION Museum. [Online]. Available: https://www.ion.org/museum/item_view.cfm?cid=3&scid=10&iid=22. [Accessed: Sep. 30, 2025].  

[11]  “Anthea Jane Coster,” MIT Haystack Observatory. [Online]. Available: https://www.haystack.mit.edu/researcher/anthea-coster/. [Accessed: Sep. 23, 2025].  

[12]  J. Gómez Socola and F. S. Rodrigues, “ScintPi 2.0 and 3.0: low-cost GNSS-based monitors of ionospheric scintillation and total electron content,” Earth, Planets and Space, vol. 74, art. no. 185, Dec. 2022. [Online]. Available: https://earth-planets-space.springeropen.com/articles/10.1186/s40623-022-01743-x. [Accessed: Sep. 23, 2025].  

[13]  “Septentrio PolaRx5TR RTK OEM Board GNSS GPS Module,” Alibaba, Product Detail. [Online]. Available: https://www.alibaba.com/product-detail/Septentrio-Polarx5tr-RTK-OEM-Board-Precision_1601231199008.html. [Accessed: Sep. 23, 2025].  

[14]  OpenAI, GPT-5, ChatGPT, San Francisco, CA, USA, 2025. [Online]. Available: https://chat.openai.com/. [Accessed: Sep. 20, 2025].  


## **Statement of Contributions**

- Jack Bender: Specifications and Constraints, Survey of Existing Solutions, Measures of Success, Final Review
- Kenny Creamer: Background, Specific Implications, References
- Blake Hudson: Broader Implications, Ethics, and Responsibility as Engineers, Resources, Specifications and Constraints
- Nolan Magee: Introduction, Budget, Personnel, Timeline, Final Review
- Jackson Taylor: Background, Measures of Success


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
  - IEEE Std 1657-2018 recommends procedures for battery handling and installation, such as fuse placement and connector design types in Section 4. In Section 7, it encourages labeling polarity, voltage, and capacity, making our modular system safe for the replication of others [4]. 
  - IEC 62509:2010 Clause 8 specific efficiency testing and current limiting varification relevant to the charge controllers rated output ensuring safe operation while charging [4]. 
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
  - Radio Regulations, Vol. I, Section 5: Frequency Allocations define the GNSS bands as space-to-Earth passive services, meaning no intentional radiation is allowed from user equipment [5]. 
- The chosen design shall operate for short-range wireless communication within approved ISM bands and comply with the applicable regional standards for chosen frequencies.
  - Constraint originates from customer specifications, including a server-based system to remotely analyze TEC data.
- The chosen design shall meet IPx4 splash resistant waterproofing standards, thermal protection guidelines, and have the capability to be safely mounted.
  - Environmental and safety constraints stem from engineering ethics and public safety standards, requiring IPx4 waterproofing, thermal protection, and secure mounting to prevent damage or injury during operation. \[10\]
  - IEC 60529:2021 specifies the IP rating system in Clause 4 for environmental protection. It lists test paremeters that involve splashing water from all directions for 5 minutes and the varification of sealed conectors [10]. 

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

&nbsp; &nbsp; &nbsp; &nbsp;The antenna selection was guided by metrics including gain, radiation pattern coverage, multi-frequency support, and cost, ensuring an optimal balance between performance and budget for accurate TEC measurements. Team 6 has considered several antenna options including the helical, choke-ring, and patch antennas. While Helical and Choke-ring antennas are available as options, cost constraints nullify their viability for low-cost TEC measurement.

- **Helical antennas** are directional and provide high gain, making them well suited for high-precision GNSS applications. However, their radiation and reception patterns limit simultaneous multi-satellite monitoring. With a slightly higher minimum cost of an estimated US $120 compared to the budgeted US $75, and the additional limitation of a narrow reception pattern, helical antennas are not an ideal choice for Team 6’s design.
- **Choke-ring antennas** provide near-hemispherical radiation and reception patterns, enabling observation of multiple satellites simultaneously. They also offer excellent multipath rejection and are capable of multi-frequency tuning. However, their cost starts in the low thousands of dollars, well above Team 6’s budget constraints.
- **Patch antennas**  are commonly used in handheld GNSS devices due to their compact form factor and affordability. [12] They are a usual choice for RF engineers when designing a GNSS application, featuring a fairly hemispherical radiation pattern. Most off-the-shelf dual-frequency GNSS antennas use patch elements. [13] These antennas are reasonably priced, typically ranging from US $30 to $100 depending on features and frequency coverage. Therefore, a dual-tuned, multi-element patch antenna has been selected for the prototype.

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

&nbsp; &nbsp; &nbsp; &nbsp;Utilizing an SDR is one approach for processing and digitizing GNSS signals. This method offers significant flexibility for the user while substantially increasing design complexity. Implementing an SDR requires extensive programming knowledge for handling IQ sampling, filtering, modulation, multipath rejection, and other digital signal processing tasks. Furthermore, these processes must be performed concurrently for multiple satellites, adding additional challenges. The primary goal of this prototype is to develop a simple yet functional system, enabling a hobbyist to measure TEC independently. While Team 6 will provide the necessary code regardless of the RF processing method chosen, using an SDR introduces unnecessary complexity, threatening the system’s user-friendly appeal to the user. A moderately capable SDR that supports L1 and L5 bands may cost approximately US $400, thereby ruling out any cost advantage over dedicated RF modules while adding complexity.

<div align="center">
  <img src="https://hackmd.io/_uploads/BJUc5I3Rxx.png" alt="Screenshot of System Layout" width="600">
  <p><strong>Figure 3:</strong> Example of an SDR Module</em></p> 
</div>

**RF Module Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An alternative solution for RF conditioning and digitization is using a dedicated dual-tuned GNSS signal processing unit. This approach was first introduced and recommended to Team 6 by Dr. Anthea Coster, a professor at MIT and expert in ionospheric studies. Supporting this recommendation, the ScintPi 3.0, discussed in the project proposal, also employs an RF module and produces data comparable to that of high-end TEC monitoring systems.

<div align="center">
  <img src="https://hackmd.io/_uploads/H1HpOEbJZe.png" alt="u-blox Module vs High-end System TEC Measurements" width="600">
  <p><strong>Figure 4:</strong> u-blox Module (red) vs High-end System (black) TEC Measurements</p>
</div>

&nbsp; &nbsp; &nbsp; &nbsp;Many of these modules feature fully integrated RF conditioning and digitization, receiving an RF signal and outputting structured data (E.g. RINEX, UBX). They include a complete RF chain with filters and low-noise amplifiers. Furthermore, additional breakout boards can be purchased to interface with the units, requiring minimal coding experience while being cost-friendly (~US $300). Dr. Coster specifically recommended a u-blox GNSS positioning chip as seen below. However, Team 6 is investigating alternative options to ensure the best RF module is implemented.

&nbsp; &nbsp; &nbsp; &nbsp;Based on industry recommendations, design simplicity, and cost considerations, Team 6 has elected to implement a dedicated RF module in the prototype.

<div align="center">
  <img src="https://hackmd.io/_uploads/S1Ni9IhRel.png" alt="Screenshot of PCB Hub" width="600">
  <p><strong>Figure 5:</strong> u-blox ZED-F9P Module w/sparkfun Breakout Board</em></p>
</div>


<div align="center">
  <img src="https://hackmd.io/_uploads/rkv25LnClx.png" alt="Screenshot of PCB Hub Detail" width="800">
  <p><strong>Figure 6:</strong> u-blox ZED-F9P Module Block Diagram for L1 and L2</em></p>
</div>


### **Computing and Control Platform**

&nbsp; &nbsp; &nbsp; &nbsp;After the RF module outputs processed GNSS data, it is handled by the central computing platform, which manages TEC computation, system coordination, and data logging. Team 6 has considered implementing the full system using either a single-board computer (SBC) or a microcontroller (MCU)-based approach.

**Microcontroller Unit (MCU) Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An MCU is essentially a small computer on a single chip. It is designed to manage specific tasks within an embedded system without requiring a complex operating system. MCUs integrate processing, memory and input/output (I/O) peripherals—including timers, counters and analog-to-digital converters (ADCs)—into one efficient and cost-effective standalone unit [3]. They are ideal for directly interfacing with sensors monitoring system health. Other advantages, including low power consumption (~0.08W), minimal heat generation, and immediate startup make MCUs well-suited for field-deployable systems and user interfacing.

&nbsp; &nbsp; &nbsp; &nbsp;Despite their advantages, MCUs have significant limitations. Their limited processing power and memory restrict their ability to perform complex tasks simultaneously, such as real-time TEC computation and rendering ionospheric models. Unlike SBCs capable of multi-core GHz processing and gigabytes of memory, MCUs typically provide only a few hundred MHz and kilobytes to megabytes of memory, limiting their suitability for concurrent numerical and graphical workloads. Running sensor monitoring, system control, data logging, and TEC computations can quickly exceed an MCU’s resources. Additionally, while MCUs excel at low-level interfacing, they generally lack the high-level software ecosystem and modular expansion options needed to support advanced user-driven expansions.  

&nbsp; &nbsp; &nbsp; &nbsp;MCUs are excellent for analog sensor interfacing and low-level processing operations. However, MCUs alone are insufficient for handling the computationally intensive, modular, and expandable requirements of Team 6's prototype. Their limited number of I/O ports and communication interfaces restrict the ability to support multiple peripherals and expansion modules simultaneously. This makes them unsuitable as the primary processing platform.

<div align="center">
  <img src="https://hackmd.io/_uploads/HJNTcLhCgx.png" alt="Arduino MCU" width="600">
  <p><strong>Figure 7:</strong> Example of Two MCUs</em></p>
</div>

**Single Board Computer (SBC) Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;An SBC provides the processing power and flexibility necessary to support Team 6’s prototype, featuring multi-core GHz processing and several gigabytes of RAM. SBCs typically feature multiple GPIO pins, USB ports, HDMI ports, and other interfaces, enabling high modularity and straightforward integration of additional hardware modules. This flexibility allows the prototype to go beyond its primary objective of TEC measurement, supporting user-driven expansions such as software-defined radios and other telecommunication experiments.

&nbsp; &nbsp; &nbsp; &nbsp;The surplus computing power of an SBC enables real-time TEC calculations while simultaneously handling system control tasks, data logging, and additional processing requirements. For example, Team 6 aims to render models of ionospheric data directly from the prototype, demanding significant computational resources that an SBC can readily provide. Furthermore, widely supported development tools and a robust user community ensure that custom features and experiments can be efficiently implemented.

&nbsp; &nbsp; &nbsp; &nbsp;While an SBC can handle all tasks related to TEC measurement and provide a flexible platform for user expansion, there are some trade-offs. SBCs typically consume more power than MCUs (~10 W), which warrants consideration for field-deployable systems. They also generate more heat due to increased power consumption, potentially necessitating cooling solutions, and increasing the system’s size. Running a full operating system adds to boot times and overall system complexity. Furthermore, most SBCs lack built-in analog-to-digital converters (ADCs). Thus, any analog input monitoring would require either external ADCs or a dedicated microcontroller to interface with the sensors. 

&nbsp; &nbsp; &nbsp; &nbsp;Despite these trade-offs, the combination of modularity, high processing capability, and extensive interface support, substantiates an SBC as the optimal choice for the prototype. Team 6 has elected to implement an SBC to provide both the computational power and design flexibility needed to support the innovative user-driven nature of the system. To address the limited number of built-in ADCs, an MCU or an external ADC module (ADC hat) may be integrated to work in tandem with the SBC. This enables analog sensor monitoring for system health metrics and any additional analog inputs.


<div align="center">
  <img src="https://hackmd.io/_uploads/S1jj-D2Cgl.jpg" alt="PCB Hub Layout" width="500">
  <p><strong>Figure 8:</strong> Raspberry Pi 5 SBC</em></p>
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

&nbsp; &nbsp; &nbsp; &nbsp;Team 6 is considering various storage options for the prototype, aiming to meet throughput, endurance, reliability, and cost requirements for field deployment. Key requirements include sustaining a total throughput of ~53.8kB/s, continuous logging for at least one month (~139 GB), reliable operation under potential environmental stresses, and affordability. The following options were evaluated: 

- **Hard Disk Drives (HDDs)**

  - **Throughput:** Typically hundreds of MB/s, sufficient for logging, but subject to latency during continuous writes.  
  - **Endurance:** Limited by mechanical wear and vulnerable to shock and vibration.  
  - **Reliability:** Mechanical components make them less suitable for portable, field-deployable systems.  
  - **Power Consumption:** ~2-6 W 
  - **Cost:** US $10-40 

- **Solid-State Drives (SSDs)**

  - **Throughput:** Hundreds of MB/s, consistent under continuous writes. 
  - **Endurance:** Moderate write endurance with consumer SSDs typically supporting several           hundred gigabytes to a few terabytes written over their lifetime.  
  - **Reliability:** No moving parts, robust under vibration and shock, compact form-factors,         slightly higher interface complexity. 
  - **Power Consumption:** ~2-4 W 
  - **Cost:** US $30-100 

<div align="center">
  <img src="https://hackmd.io/_uploads/rJUyo8n0le.jpg" alt="HDD vs SSD Interior" width="600">
  <p><strong>Figure 9:</strong> HDD vs. SDD Interior</em></p>
</div>


- **SD Cards**

  - **Throughput:** Consumer-grade cards may support ~10-100 MB/s, reasonably consistent under        continuous writes. 
  - **Endurance:** Moderate write endurance with a risk of degradation if subjected to                continuous high-volume writes over long periods.    
  - **Reliability:** Compact form factor and removable with performance and durability that           vary depending on the make and quality of the card. 
  - **Power Consumption:** ~ 0.02 - 0.1 W 
  - **Cost:** US $10-50 

- **USB Thumb Drives**
  
  - **Throughput:** Modern USB 3.0 thumb drives support sustained throughput of ~100MB/s,             consistent under continuous writes.  
  - **Endurance:** Moderate write endurance, typically sufficient for several hundreds of             gigabytes to a few terabytes over their lifetime.  
  - **Reliability:** Solid-state, no moving parts, plug-and-play, and easily replaceable in the       field.  
  - **Power Consumption:** ~0.05 - 0.5 W 
  - **Cost:** US $20-50 

&nbsp; &nbsp; &nbsp; &nbsp;After evaluating these options Team 6 has elected to implement a USB thumb drive as the prototype storage medium. The USB drive will have 256 GB capacity and a storage format that can support files larger than 4 GB, such as exFAT or similar formats. This option offers true plug-and-play functionality, allowing easy insertion, removal, or replacement without additional hardware or system modifications. Modern USB 3.0 drives provide sufficient throughput for real-time TEC data logging and system monitoring. USB thumb drives are also cost-effective, providing ample storage capacity for continuous operation and additional user-driven experiments, while minimizing system complexity.


<div align="center">
  <img src="https://hackmd.io/_uploads/r1ySXDnAxx.jpg" alt="System Overview Diagram" width="600">
  <p><strong>Figure 10:</strong> Thumb Drive Example</em></p>
</div>


&nbsp; &nbsp; &nbsp; &nbsp;In addition to the USB thumb drive, the prototype will be capable of connecting to a local host server or workstation, enabling backup, visualization, and integration of logged GNSS measurements, system health metrics, and auxiliary data. The addition of the server provides supplementary storage and data analysis capabilities without affecting the prototype's on-device storage requirements. The choice to implement a USB thumb drive is based on throughput analysis, data estimation, and consideration of cost, reliability, and field deployability. The USB drive serves as the primary local storage for continuous TEC and system data logging. The prototype may also connect to the host server or workstation for centralized data aggregation.

## **Power**

&nbsp; &nbsp; &nbsp; &nbsp;Powering Team 6's prototype requires careful consideration of mobility, reliability, and operational environment. Various approaches, ranging from AC wall power to hybrid battery and solar configuration, offer different trade-offs in cost, complexity, and deployment flexibility. Team 6 evaluates these approaches to balance portability, autonomy, and modularity while ensuring continuous, safe operation of all subsystems, including the GNSS receiver, processing unit, and data storage.

### **AC Wall Power Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;A simple method for powering the prototype is through direct connection to a 120 V AC wall outlet. This approach provides a stable and continuous power source, ensuring reliable operation for all system components, including the GNSS receiver, processing unit, and data storage device. Wall-powered operation significantly reduces system complexity by eliminating the need for battery management circuitry, power conversion modules, and charge controllers.

&nbsp; &nbsp; &nbsp; &nbsp;No energy storage component is required, resulting in a lower-cost build. This creates a margin in the budget for higher-performance electronics. However, this approach imposes significant spatial limitations. The device can only operate in proximity to a building or facility with available mains power. Consequently, deployment flexibility and geographic coverage are greatly reduced. The system would be constrained to controlled environments such as research laboratories, homes, schools, and other desired observatories, making it unsuitable for widespread or remote field measurements. Overall, the price for this subsystem is minimal at roughly $10-$30 since minimal componets would be used in this solution.

### **Standalone Rechargeable Battery Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Using a rechargeable battery system capable of supplying all required electrical loads greatly improves mobility, deployment, and versatility. This enables the prototype to operate in isolated locations without dependance on infrastructure. A well-designed battery subsystem, such as a 12.8 V LiFePO₄ pack paired with a battery management system (BMS), provides the necessary current for the device’s power rails through appropriate buck converters or voltage dividers. The battery itself would cost approximately US $60-$110, assuming the use of a 12.8 V LiFePO₄ 20Ah pack paired with a BMS. 

&nbsp; &nbsp; &nbsp; &nbsp;The advantages of a battery-only system include portability and operational independence critical for field experiments and distributed observation networks. However, this approach introduces engineering and safety challenges. The integration of rechargeable batteries necessitates protection circuits against overvoltage, short-circuit, and thermal runaway conditions. Because of these challenges, a cost esimate of US $10-$30 is added towards the cost of this subsystem to implement the necessary protection circuitry. Without an external charging source, runtime is inherently limited by battery capacity, requiring careful energy budgeting and system shutdown protocols to prevent data corruption upon power depletion. This design also demands periodic maintenance and manual recharging, reducing long-term autonomy. The overall cost of this subsystem would be approximately $150-$200 with the use of an affordable charge controller, battery, power supply and other supporting components. 

<div align="center">
  <img src="https://hackmd.io/_uploads/HJOoXwnCxl.png" alt="System Block Diagram" width="600">
  <p><strong>Figure 11:</strong> 12V 20Ah LiFePO4 Battery w/Built in BMS</em></p>
</div>

### **Standalone Rechargeable Battery + Solar Capable Recharge Approach:**

&nbsp; &nbsp; &nbsp; &nbsp;Incorporating a solar charging system alongside the onboard battery mitigates many limitations of the battery-only configuration. A solar panel coupled with a maximum power point tracking (MPPT), or a pulse width modulation (PWM) charge controller, enables the device to operate for extended periods of time dependent on sunlight availability and energy demand. Using this component would add a US $25-$90 addition to the overall cost of this subsystem, assuming the purchace of a 10A-20A rated charge controller. The use of the 12 V (nominal 12.8 V LiFePO₄) standard aligns with industry conventions for portable instrumentation and ensures compatibility with commonly available charge controllers and solar modules.

&nbsp; &nbsp; &nbsp; &nbsp;This configuration enhances the device’s operational autonomy, making it ideal for remote monitoring networks or long-term unattended deployments. However, the addition of solar power introduces new physical and electrical complexities. The panel increases the system’s physical footprint, potentially reducing portability. Wiring between the MPPT, battery, and system load must be carefully designed to prevent reverse current flow and cross-charging between power inputs. Furthermore, system cost and assembly time increase due to additional components and mounting considerations. Despite these drawbacks, the solar-assisted configuration offers the best endurance-to-cost ratio for long-duration field applications. The overall cost of this subsystem would be approximately US $200-$300 with the use of similar components found in the last solution. However, it adds additional costs for the solar panel and the adaptive cables for modular connections. 


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
  <p><strong>Figure 12:</strong> 12V Solar Panel and 20A MPPT</p>
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
  <p><strong>Figure 13:</strong> AC and Solar Power Adapters</p>
</div>

&nbsp; &nbsp; &nbsp; &nbsp;The hybrid approach offers significant engineering and operational advantages. It ensures that the system remains functional during power interruptions, supports hot-swappable charging inputs, and eliminates the need for constant supervision. Using widely available power connectors such as the XT60, DC barrel jacks, or Anderson Powerpole allows for easy field servicing and replacement without compromising structural integrity. The architecture also promotes modularity, enabling future users to upgrade components without redesigning the core electronics.

&nbsp; &nbsp; &nbsp; &nbsp;Assuming the use of defined components mentioned earlier in this proposal, a predicted power draw analysis can be anticipated.

| **Component** | **Nominal PD (Watts)** | **Peak PD (Watts)** | **Efficiency (%)** | **Max Loss (W)** |
| --- | --- | --- | --- | --- |
| Single-Board Computer (RasPi5) | 10.0 | 24.0 | &nbsp; | &nbsp; |
| Microcontroller (RasPiPico) | 0.08 | 0.2 | &nbsp; | &nbsp; |
| RF Module (u-blox ZED-F9P) | 0.7 | 1.0 | &nbsp; | &nbsp; |
| USB Thumb (256GB) | 0.10 | 0.50 | &nbsp; | &nbsp; |
| MPPT/PWM Controller | &nbsp; | &nbsp; | &nbsp; | 0.35 |
| 3.3V buck/LDO | &nbsp; | &nbsp; | 85 to 90 | 1.7 |
| 5V Buck Converter | &nbsp; | &nbsp; | 88 to 92 | 0.22 |
| **TOTAL** | **10.94** | **25.08** | **88-90%** | **1.93** |

&nbsp; &nbsp; &nbsp; &nbsp;With a 12 V 20 Ah LiFePO₄ battery, the system sustains operation for approximately 20 – 22 hours assuming normal draw (16 W) or 10 hours under peak conditions (25 W). When recharge via a 120 V AC adapter (19.5 V / 200 W), full recovery from 20% to 100% state-of-charge requires 1.5 – 2 hours. Solar recharging using a 12 V 100 W panel typically yields 5–6 A at midday, restoring full charge in 5 – 6 hours under optimal insolation. 

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
  <p><strong>Figure 14:</strong> 40 Pin Male to Female Ribbon Cable</p>
</div>

**Enclosure**

&nbsp; &nbsp; &nbsp; &nbsp;The system shall be housed in an enclosure designed for mobility, rapid deployment, and easy access in support of a variety of configurations. Team 6 draws inspiration from the ScintPi 3.0 design, exemplifying compact form factor, transportability, and user-friendly accessibility. The enclosure shall accommodate modular components, allowing for straightforward integration and replacement of the various modules and sensors within. This shall foster long-term serviceability and adaptability. Team 6 considered the following characteristics in deciding between 3D printing the enclosure compared to buying one prefabricated; such as ease of attaining, thermal resistance, and mechanical strength to ensure durability and field suitability. This shall foster long-term serviceability and adaptability.

**3D Printed Enclosure**

&nbsp; &nbsp; &nbsp; &nbsp;To achieve an IPx4 rating while maintaining ventilation, the enclosure design shall incorporate an enclosure nested within a larger enclosure. Interior walls are arranged to force any water entering the vent to travel upward along a convoluted path before reaching the internal cavity, effectively preventing water ingress while allowing passive airflow for thermal regulation. Additional airflow beneath the enclosure increases exposed surface area for heat dissipation, improving long-term thermal stability. The enclosure shall be 3D printed, enabling rapid prototyping and low-cost production while maintaining structural integrity suitable for repeated field deployment. The 3D print files will be made publicly available, allowing users to modify and adapt the design for each specific application and environmental condition.

Team 6 has identified three potential materials to use in creating the enclosure:

- **Polylactic Acid (PLA) Approach**

&nbsp; &nbsp; &nbsp; &nbsp;PLA is a widely used material known for its ease of printing, high dimensional accuracy, and smooth surface finish, making it ideal for rapid prototyping and aesthetic enclosures. However, PLA suffers from significant drawbacks in outdoor environments. It softens at low temperatures relative to other 3D printing materials (60-65 °C), is brittle under mechanical stress, and degrades over time when exposed to sunlight and moisture. While it provides affordable precision for early design iterations, its lack of toughness and long-term heat resistance makes it unsuitable for field applications requiring long-term durability.

- **Acrylonitrile Butadiene Styrene (ABS)** **Approach**

&nbsp; &nbsp; &nbsp; &nbsp;ABS provides excellent mechanical strength, impact resistance, and thermal stability. These properties make ABS a strong candidate for rugged outdoor enclosures. However, its high printing temperature, susceptibility to warping, and the requirement for a controlled printing environment make it difficult to fabricate with standard 3D printers. Additionally, ABS emits unpleasant and potentially harmful fumes during printing, eliminating it as an option at Tennessee Technological University.

- **Polyethylene Terephthalate Glycol (PETG)** **Approach**

&nbsp; &nbsp; &nbsp; &nbsp;PETG combines the advantages of both PLA and ABS, offering bond strength between layers, moderate flexibility, chemical resistance, and excellent impact durability. PETG withstands higher temperatures than PLA while maintaining lower printing difficulty than ABS. Its low warping tendency and moisture resistance make it ideal for producing large, dimensionally stable parts without requiring specialized equipment. PETG's balance of printability, mechanical performance, and environmental resilience make it particularly suited for outdoor or mobile applications.

**Prefabricated Enclosure**

&nbsp; &nbsp; &nbsp; &nbsp;The enclosure and protection subsystem serves as the structural backbone of the overall design, ensuring that all internal components remain secure, accessible, and protected during field use. Its primary function is to provide a robust, weather-resistant housing to support intuitive implementation. Effective airflow for thermal regulation will need to be taken into account, as well as user-friendly access for troubleshooting, repairs, and modular component interchange. To meet these goals, the prefabricated enclosure is governed by strict minimum requirements, including ventilation requirements, insect mitigation, waterproof sealing through grommets or sealtight fittings, and compliance with IPX-4 and NEMA 4 protection standards. 

&nbsp; &nbsp; &nbsp; &nbsp;In conclusion, team 6 has elected to use a prefabricated enclosure. This is justified by its ability to align with every functional requirement and constraint of the TEC measurement prototype. A custom-built enclosure would struggle to match the desired specifications without significant additional effort or cost and assumes the user has access to a 3D printer. Although team 6 will select a specific model, any model matching the desired criteria exemplified by the chosen enclosure shall adequately provide the most practical, efficient, and robust solution for both prototype development and future user adoption. 

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
  <img src="https://hackmd.io/_uploads/ByZS5VZJ-l.png" alt="Hardware Block Diagram" width="600">
  <p><strong>Figure 15:</strong> <em>Hardware Block Diagram</em></p>
</div>

# **Operational Flow Chart**

<div align="center">
  <img src="https://hackmd.io/_uploads/SkQP54WyWe.png" alt="Operation Flowchart" width="600">
  <p><strong>Figure 16:</strong> <em>Operation Flowchart</em></p>
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
  <img src="https://hackmd.io/_uploads/B1z0c4-1Ze.png" alt="Data Storage Flow Chart" width="600">
  <p><strong>Figure 17:</strong> <em>Data Storage Flow Chart</em></p>
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
  <img src="https://hackmd.io/_uploads/Sy4-j4ZkZe.png" alt="Antenna and RF Module Hardware Diagram" width="400">
  <p><strong>Figure 18:</strong> <em>Antenna and RF Module Hardware Diagram</em></p>
</div>


**Subsystem Flowchart**

<div align="center">
  <img src="https://hackmd.io/_uploads/H1gVsNZ1bx.png" alt="Antenna and RF Module Flowchart" width="400">
  <p><strong>Figure 19:</strong> <em>Antenna and RF Module Flowchart</em></p>
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
  <img src="https://hackmd.io/_uploads/BkJ5_YhW-x.png" alt="Connections Diagram" width="800">
  <p><strong>Figure 20:</strong> <em>System Interconnections Block Diagram</em></p>
</div>


&nbsp; &nbsp; &nbsp; &nbsp;The block diagram does not show the specific PCB trace connections other than general power buses. It instead highlights the use of a hub-based architecture for the prototype.

**Interface Connections**

| **Connected Subsystem** | **Signal Type** | **Signal Direction** | **Protocol** | **Notes** |
| --- | --- | --- | --- | --- |
| Power Supply/ Battery | DC Power | Input/Output | N/A | Provides regulated power rails to all connected devices |
| RF Module | Analog RF / Digital GNSS Data | Input: Analog RF from antenna / Output: GNSS data to SBC routed through PCB | UART/I2C | Receives RF signal via coaxial cable. Outputs GNSS data file (e.g., RINEX or UBX) to SBC through PCB traces |
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
  <img src="https://hackmd.io/_uploads/B109jVZyZl.png" alt="Detailed Power System Flowchart" width="800">
  <p><strong>Figure 21:</strong> <em>Power System Flowchart</em></p>
</div>


## **Enclosure and Protection System**

&nbsp; &nbsp; &nbsp; &nbsp;The enclosure and protection system serves as the structural and environmental safeguard for the entire prototype, ensuring reliable performance under diverse operating conditions. Its primary role is to shield all internal subsystems from external hazards such as moisture, dust, and temperature fluctuations, while also mitigating internal risks like heat buildup or mechanical stress. To achieve this, the enclosure shall be prefabricated from  NEMA 4 rated material for superior resistance to water, chemicals, and extreme temperatures. The chosen enclosure shall support modularity and accessibility for efficient maintenance and future upgrades.

- This subsystem shall be prefabricated, optimizing resilience against water, chemical, and heat interactions.
- This subsystem shall possess air vents for proper temperature regulation of the system.
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

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be made up of a storage drive and an SBC. The justification for selecting these components is detailed in the ‘Storage Mediums Considered’ and ‘Single Board Computer (SBC) Approach’ subsections of the Comparative Analysis. The SBC shall be used for data processing, and the thumb drive shall be used for data storage. The thumb drive has been chosen for its low cost and plug-and-play nature. The SBC approach has been chosen for its high processing capability and design flexibility. To keep options open for various specifications, the SBC and the storage drive shall not exceed US $120 for the SBC and $25 for the storage as shown below. 
| Subsystem | Item | Budget |
| --- | --- | --- |
| Data Storage System 
| | Storage Drive (Thumb Drive) | \$25 |
| | Single-Board Computer (SBC)\* | \$120\* |
| Total | | \$145 |

  \*SBC will be shared between Data Subsystem and RF Module Subsystem 
  
**Antenna and RF Module System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of an RF Module and Dual-Tuned Patch Antenna, which includes the required Coaxial Cable. The justification for selecting these components is detailed in the ‘RF Signal Conditioning and Digitization’ and ‘Signal Reception’ subsections of the Comparative Analysis. The antenna shall receive GNSS signals, and the RF module shall process those signals. A dual-tuned patch antenna has been chosen for its low relative cost compared to other options, and the RF module approach has been chosen due to its design simplicity, industry recommendations, and cost considerations. Given the large variation in cost for RF modules, the max budget for this component has been set at US $300.
| Subsystem | Item | Budget |
| --- | --- | --- |
| Antenna and RF Module System
| | RF Module | \$300 |
| | Dual-Tuned Patch Antenna | \$75 |
| Total | | \$375 |


**System Interconnections:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of a PCB board, a magnetometer, a microcontroller, and any miscellaneous cables connecting each subsystem together. The PCB board shall act as a hub to connect all components and any additional devices to the system, as discussed in the Modularity subsection of the Comparative Analysis. The magnetometer is included in this budget so that modularity of the system can be demonstrated, as it is a cheap peripheral that can be attached to the system. The microcontroller shall allow the system to have ADC connections, further enabling user-driven expansion of the prototype. This subsystem’s budget also covers cost for any cabling between subsystems, accounted for under the Miscellaneous Cables section. 

| Subsystem | Item | Budget |
| --- | --- | --- |
| System Interconnections
| | PCB | \$50 |
| | Miscellaneous Cables | \$25 |
| | Magnetometer | \$5 |
| | Microcontroller | \$20 |
| Total || \$100 |

**Power System:**

&nbsp; &nbsp; &nbsp; &nbsp;This system shall be composed of a power supply, MPPT charge controller, 12V 20Ah battery, transformer, miscellaneous cables, and as a demonstration of expandability, a solar panel shall be included.  The justification for selecting a solar panel, power supply, 12V battery, MPPT/PWM is discussed in the ‘Power’ subsection of the Comparative Analysis, as well as the ‘Power’ subsection of the Atomic Subsystem Analysis. The 12V battery provides all other electronic components with proper power input to function. The solar panel and power supply shall be used to charge and recharge the battery. Interfacing all the components requires voltage regulation. Therefore, the purchase of buck converters and voltage regulators is necessary. To interface all components, the use of miscellaneous adapters such as MC4/XT60 adapters, barrel jack or USB port wires is necessary, justifying the purchase of miscellaneous cables. To ensure protective integrity and a clean energy supply, the use of fuses, diodes, capacitors, and inductors prevents the risk of over/under voltage and current in an area where this is not present. This justifies the purchase of protection components. 

| Subsystem | Item | Budget |
| --- | --- | --- |
| Power System
| | Solar Panel | $75 |
| | Power Supply | $25 |
| | MPPT Charge Controller | $30   |
| | Battery (12V, 20Ah) |$50 |
| | Transformer/Converters | $20   |
| | Protection/Filtering Components |  $25  |
| | Miscellaneous Cables | $35   |
| Total | | $260 |

**Enclosure System:**

&nbsp; &nbsp; &nbsp; &nbsp;**This system shall be composed of the enclosure box, wire mesh vents, and a ½" liquid seal tight fitting with a matching ferrule. The justification for selecting a prefabricated box is to be more inclusive for those wanting to replicate the prototype and may not have access to a 3D printer.**

| **Enclosure** || |
| --- | --- | --- |
| **Enclosure Box** | **\$73.39** |
| **Wire Mesh Vents** | **\$33.61** |
| **½" Liquid Seal Tight Fitting** | **\$1.79** |
| **½" Liquid Seal Tight Ferrule** | **\$0.50** |
| **Total** | **\$109.29** |

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
|| Enclosure Box | \$73.39 |
|| Wire Mesh Vents | \$33.61 |
|| ½" Liquid Seal Tight Fitting | \$1.79 |
|| ½" Liquid Seal Tight Ferrule | \$0.50 |
| Total || \$109.29 |
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

Nolan Magee: Introduction, Division of Labor, Timeline, and Final Review.

Jackson Taylor: Budget, Atomic Subsystem Specifications \[Antenna and RF Module Subsystem\]


# Detailed Design — Data Storage Subsystem
*Team 6 — GNSS TEC Measurement System*  

---

## 1. Function of the Subsystem

The **Data Storage Subsystem** acts as the long-term memory and real-time visibility layer of the TEC instrument. Its primary responsibility is to ensure that all computed Total Electron Content (TEC) and scintillation measurements are **reliably recorded, monitored, preserved, and accessible** throughout system operation.

It gathers processed GNSS data from the antenna and RF module, formats it, and stores it in a structured, fault-tolerant manner for scientific use, field diagnostics, and post-mission analysis.

---

### 1.1 Core Responsibilities

#### **Continuous Data Logging**
- Records TEC and scintillation outputs at **10 Hz**.  
- Each entry includes:
  - Timestamp  
  - TEC value  
  - Scintillation index  
  - Temperature  
  - System-health metadata  
- Supports long-term scientific analysis.

#### **Automated File Management**
- Creates new log files every **24 hours** or when file size exceeds limits.  
- Automatically **compresses and archives** files older than 30 days.  
- Implements **first-in, first-out (FIFO)** deletion when storage is full.

#### **Data Integrity & Fault Tolerance**
- Performs CRC/hash checks on newly written logs.  
- Corrupted files are flagged for re-verification.  
- Logs integrity events in a diagnostics file.

#### **Fail-Safe Operation**
- Flushes buffers and closes files safely during shutdown.  
- Continues logging even if Wi-Fi or web server fails.  
- Ensures no TEC data is lost during transient faults.

#### **User Accessibility**
- Provides real-time visualization through a **Wi-Fi web dashboard**:
  - Recent TEC values  
  - Satellite tracking  
  - System temperature  
  - Battery level  
  - Storage usage  
- Raw logs stored locally in **CSV format** for MATLAB/Python.  
- LoRa telemetry provides long-range, low-bandwidth system summaries.

---

## 1.2 Role in the Overall System

The Data Storage Subsystem forms a **central integration point** among:

- GNSS computation  
- User interfaces  
- Long-range telemetry  
- System-health monitoring  

It ensures that the TEC instrument remains:

- **Observable** — real-time web dashboard  
- **Diagnosable** — LoRa status packets  
- **Scientifically valid** — accurate, verified logs  
- **Reliable** — uninterrupted long-term data collection  

---

## 1.3 Summary

The Data Storage Subsystem is the backbone of the TEC instrument’s data lifecycle, ensuring:

- High-quality scientific data capture  
- Long-duration operation  
- Fault-tolerant behavior  
- Real-time visibility  
- Long-range status reporting  

It connects raw GNSS processing to field users, researchers, and remote operators, forming one of the system’s most critical subsystems.

---

## 2. Specifications and Constraints

The **Data Storage Subsystem** must continuously record TEC, scintillation, and system-health data with high reliability.  
This section defines all performance specifications, constraints, and derived requirements guiding the subsystem’s design.

---

## 2.1 Performance Specifications

### **Storage Capacity**
- Minimum **256 GB** non-volatile storage
- Supports ≥ **30 days** of continuous operation  
- Estimated data generation: **~139 GB/month**

### **Sustained Write Throughput**
- Required: **≥ 53.8 kB/s**  
  (Supports TEC logs, scintillation values, RINEX files, TEC maps, metadata)

### **Logging Frequencies**
- **TEC / Scintillation:** 10 Hz  
- **RINEX:** 1 Hz (per UBX → RINEX conversion requirements)  
- Maintains scientific resolution for ionospheric modeling

### **File System Requirements**
- Must use **exFAT** to:
  - support files > 4 GB  
  - ensure cross-platform compatibility  
  - align with ISO/IEC 20933

---

## 2.2 Wi-Fi Server Requirements

### **Server Latency**
- Dashboard updates within **1 second**  
- Enables near-real-time TEC and health visualization

### **Concurrent Access**
- Supports **two simultaneous clients**

### **Range**
- Stable operation at **≥ 10 meters line-of-sight**

---

## 2.3 LoRa Telemetry Requirements

### **Telemetry Throughput**
- Minimum: **30 bps**

### **Packet Size**
- Must reliably handle **40-byte packets**

### **Range**
- Required minimum: **500 meters**  
- Typical LoRa ranges (1–5 km) exceed needs

---

## 2.4 System-Level Constraints

### **Power Constraints**
- Must operate within Raspberry Pi 4B USB power budget:
  - **5V at 1.2A**, shared across ports  
- Storage device must be low-power (<0.5W typical)

### **Interface Constraints**
- Must use **USB 3.0**:
  - Ensures high throughput  
  - Enables field-replaceable storage  
  - Provides hot-swap capability  

### **Data Integrity**
- Must support:
  - Write verification  
  - Automatic file rotation  
  - Graceful shutdown logging  

### **Software Compatibility**
- Automatically mounts under Linux  
- Requires no kernel modifications  
- Must support exFAT/FAT drivers

---

## 2.5 Standards-Based Constraints

- **exFAT File System Specification** (ISO/IEC 20933)  
- **RINEX 4.00 Standard** for GNSS data formatting  
- **USB 3.0 Specification** for interface compliance  
- Aligns with open scientific standards and non-proprietary formats

---

## 2.6 Ethical & Socio-Economic Constraints

### **Affordability**
- Total subsystem cost **≤ $200**  
- Supports educational and citizen-science missions

### **Sustainability**
- Preference for **solid-state**, low-power storage  
- Avoids spinning disks, reducing wear and power consumption

### **Data Privacy**
- Logged data must contain **no personally identifiable information**

---

## 2.7 Reliability & Maintainability Constraints

### **Fault Tolerance**
- Logging must continue uninterrupted during:
  - Wi-Fi failures  
  - Server crashes  
  - LoRa outages  

### **File Management**
- Automatically:
  - Compresses files older than **30 days**  
  - Overwrites oldest archives when storage fills  

### **Field Replaceability**
- USB drive must be:
  - Hot-swappable  
  - Replaceable without reconfiguration  
  - Recognized immediately by the OS  

---

## 2.8 Derived Technical Specifications (Summary Table)

| Requirement | Value |
|------------|-------|
| Minimum storage capacity | **256 GB** |
| Sustained write rate | **≥ 53.8 kB/s** |
| Logging duration | **≥ 30 days** |
| File format | **exFAT** |
| Replaceability | **Hot-swappable USB** |
| Subsystem cost | **≤ $200** |

---

## 2.9 Summary

The subsystem is engineered to balance:

- **Performance:** high-throughput, continuous logging  
- **Reliability:** file rotation, CRC checks, fault tolerance  
- **Accessibility:** USB-based modular storage  
- **Standards compliance:** exFAT + RINEX 4.00 + USB 3.0  
- **Affordability:** remains within project budget  

It provides a robust foundation for long-term TEC data preservation compatible with scientific workflows and field operations.

---

## 3. Overview of Proposed Solution

The Data Storage Subsystem is implemented using a **256 GB USB 3.0 solid-state thumb drive** mounted to the Raspberry Pi 4B.  
This solution meets all capacity, throughput, power, and cost constraints while maintaining field modularity and long-term reliability.

The subsystem enables continuous high-rate logging of TEC and scintillation measurements, system-health data, RINEX records, and auxiliary sensor outputs.  
All data is timestamped, buffered, and written sequentially to ensure fault-tolerant and scientifically valid operation.

---

## 3.1 Key Features of the Proposed Solution

### **High Throughput & Continuous Logging**
- USB 3.0 thumb drives support **20–100+ MB/s** sustained writes  
  (far above the required **53.8 kB/s**)
- Provides ample overhead for simultaneous:
  - TEC logs  
  - Scintillation values  
  - RINEX 4.0 archival files  
  - TEC map outputs  
  - System metadata  
- Ensures no bottlenecks during peak load or multitasking.

---

### **Data Integrity & Fault Tolerance**
The subsystem includes multiple safeguards:

- Periodic write verification  
- Automatic file rotation every 24 hours or size threshold  
- FIFO deletion of oldest archives when storage reaches limit  
- Independent logging even during:
  - Server failures  
  - Wi-Fi outages  
  - LoRa dropouts  
- Graceful handling of shutdown events to prevent corruption  

This guarantees uninterrupted long-term data collection.

---

### **Modularity & Replaceability**
The USB thumb drive is:
- **Plug-and-play**  
- **Hot-swappable**  
- **Field-replaceable** without tools  
- Upgradable to larger capacities (e.g., 512 GB, 1 TB)  
- Compatible across Windows, Linux, and macOS  

This is essential for field deployments and maintenance simplicity.

---

### **Power Efficiency**
- Typical USB 3.0 flash drive consumption: **0.05–0.3 W**  
- Fits comfortably within the Raspberry Pi’s USB power budget  
- Supports extended field deployment on:
  - Solar + battery subsystems  
  - Low-power operation cycles  

Its low consumption enhances system sustainability.

---

### **Standards Compliance & Scientific Compatibility**
The subsystem adheres to core international standards:

- **RINEX 4.00** for GNSS archival data  
- **exFAT file system (ISO/IEC 20933)** for large-file support  
- **USB 3.0** interface for high-speed access  

These standards ensure:

- Interoperability with GNSS analysis software  
- Long-term archival compatibility  
- Non-proprietary data formats  

---

## 3.2 Why a USB 3.0 Thumb Drive Is the Optimal Solution

### **1. It exceeds the throughput requirements by over 500×.**
No risk of overflow, delays, or data loss during peak computation.

### **2. It is field-replaceable.**
Technicians can replace or upgrade drives instantly.

### **3. It supports exFAT.**
Essential for long files and cross-platform transfers.

### **4. It is extremely low power.**
Ideal for remote, solar-powered, or battery-constrained missions.

### **5. It is inexpensive and widely available.**
Typical cost: **$20–$40** — well within subsystem budget.

### **6. It is solid-state and durable.**
No moving parts, resistant to vibration, weather, and outdoor conditions.

---

## 3.3 Conclusion

The selected **256 GB USB 3.0 thumb drive** fully satisfies the subsystem’s technical, environmental, and operational requirements. It supports:

- High-rate TEC and scintillation logging  
- Long-duration scientific deployments  
- Real-time monitoring  
- Fault-tolerant operation  
- Standards-based data handling  
- Low-power, low-cost field deployment  

This implementation balances modularity, reliability, and scientific rigor, forming the foundation for the TEC instrument’s complete data lifecycle.

---

## 4. Interface With Other Subsystems

The Data Storage Subsystem acts as the **central data endpoint** of the TEC measurement instrument.  
It receives processed scientific data, logs all relevant system-health information, archives standardized files, and enables multiple avenues for user access (USB storage, Wi-Fi dashboard, and LoRa telemetry).

This section details how the subsystem interacts with each major component of the overall system.

---

## 4.1 Interface With the Antenna & RF Module System

### **Inputs Received**
- Standardized GNSS observables
- Satellite tracking information  
- L1/L5 frequency timestamps  
- Receiver position data  
- UBX-format raw GNSS data forwarded from SBC  

### **Communication Method**

### **Function in the Interface**
- The SBC computes TEC and scintillation values.  
- The Data Storage Subsystem logs:
  - Computed TEC  
  - Scintillation indices  
  - RINEX-formatted data  
  - System metadata  

This completes the GNSS-to-storage data pipeline.

---

## 4.2 Interface With the System Interconnections Subsystem

### **Inputs / Outputs**
- Power routed through PCB hub  
- Control/status signals routed between subsystems  
- USB data lines maintained through routed traces  

### **Communication Method**
- Hardware PCB traces for:
  - 5V/3.3V power  
  - Control signals  
  - USB routing  

### **Function in the Interface**
- Maintains clean, stable USB connectivity  
- Ensures EMC/EMI minimization to prevent file corruption  
- Distributes power paths to the SBC and storage device  

Reliable electrical interface = reliable long-term data logging.

---

## 4.3 Interface With the Power Subsystem

### **Inputs Received**
- Battery telemetry:
  - Voltage  
  - Current  
  - State of Charge (SoC)  
  - Protection flags  
- Low-voltage shutdown warnings

### **Communication Method**

### **Function in the Interface**
- Allows the system to:
  - Flush logs  
  - Close files safely  
  - Enter safe shutdown mode  
- Prevents data corruption during brownouts  
- Ensures mission continuity during low-power events  

---

## 4.4 Interface With the Enclosure & Protection Subsystem

### **Inputs / Physical Support**
- Mechanical mounting  
- Environmental protection (IP-rated enclosure)  
- Heat dissipation paths  
- Cable routing and strain relief  

### **Function in the Interface**
- Protects the USB drive and SBC  
- Controls temperature to extend flash memory lifespan  
- Ensures survivability in outdoor deployments  

---

## 4.5 Interface With User Access Subsystems

### **Wi-Fi Web Server Interface**
- Exposes dashboard for:
  - TEC trends  
  - Satellite information  
  - Temperature readings  
  - Battery level  
  - Storage availability  
- Allows file downloads through local web interface  
- Uses SBC’s built-in Wi-Fi AP mode

### **LoRa Telemetry Interface**
- Sends minimal, long-range data packets:
  - TEC summary  
  - Battery percentage  
  - Temperature  
  - Error flags  
  - Timestamp  
- Ensures system observability at >500m range

### **USB Physical Interface**
- User can remove the USB storage drive to:
  - Retrieve datasets  
  - Perform system-level backups  
  - Replace or upgrade the storage module  

Allows redundancy and data transport flexibility.

---

## 4.6 Summary

The Data Storage Subsystem integrates tightly with every major subsystem:

- **RF Module:** Receives GNSS observables → logs TEC  
- **System Interconnections:** Power and routing → ensures stability  
- **Power System:** Safe shutdowns → preserves data integrity  
- **Enclosure:** Protects hardware → ensures longevity  
- **User Access:** Provides Wi-Fi dashboard & LoRa telemetry  

This makes it a **central, mission-critical** component that ties together computation, logging, monitoring, and remote diagnostics.

---

## 5. Data Storage Subsystem Flowchart

The following flowchart describes the internal logic of the Data Storage Subsystem, including
data ingestion, logging, file rotation, integrity checks, and system-health transmission.

---

<img width="895" height="659" alt="image" src="https://github.com/user-attachments/assets/2d4c815d-ffe3-4fd8-98d7-65f1170af194" />


---

## 6. Bill of Materials (BOM)

The BOM is organized into two major components:

1. **Base System** — Required hardware that keeps the system under the HamSCI-required **$1,000 core system cost limit**.  
2. **Stretch Goals (Add-Ons)** — Optional components added on top of the base system.

All prices are shown in USD and reflect current market estimates.

---

## 6.1 Base System Components

| Component | Total Price | Qty | Manufacturer | Part Number | Distributor | Distributor Part No. |
|----------|-------------|-----|--------------|-------------|-------------|------------------------|
| Raspberry Pi 4B (4 GB RAM) | $55.00 | 1 | Raspberry Pi | SC0194(9) | DigiKey | 2648-SC0194(9)-ND |
| Pi 4B Power Supply | $8.00 | 1 | Raspberry Pi | SC0445 | DigiKey | 2648-SC0445-ND |
| 128 GB Micro SD Card | $13.91 | 1 | Amazon Basics | B08TJRVWV1 | Amazon | B08TJRVWV1 |
| 256 GB USB 3.0 Flash Drive | $22.99 | 1 | SanDisk | SDCZ73-256G-G46 | Amazon | SanDisk Ultra Flair USB 3.0 256GB |

### **Base System Total**
- **Subtotal:** $99.90  
- **Total with 9.75% tax:** **$109.64**

---

## 6.2 Stretch Goal Components (Add-On Hardware)

These components extend telemetry capabilities, enable long-range communication, or expand user functionality, but are **not required** for base system operation.

| Component | Total Price | Qty | Manufacturer | Part Number | Distributor | Distributor Part No. |
|----------|-------------|-----|--------------|-------------|-------------|------------------------|
| ESP32 LoRa V3 Board Kit | $23.89 | 1 | Heltec Automation | WiFi LoRa 32 (V3/V3.2) | Amazon | ESP32 LoRa V3 Dev Kit |
| LoRa Radio Transceiver Breakout | $19.95 | 1 | Adafruit Industries | 3072 | Mouser | 485-3072 |
| 915 MHz LoRa Antenna (2-pack) | $9.99 | 1 set | Nelawya | 915 MHz LoRa Kit | Amazon | B0CSZ14MNY |
| SMA Connector for Thick PCBs | $2.50 | 1 | Adafruit | 1865 | Mouser | 485-1865 |

### **Stretch Goals Total**
- **Subtotal:** $56.33  
- **Total with 9.75% tax:** **$61.82**

---

## 6.3 Combined Total Cost

| Category | Cost |
|----------|-------|
| Base System (with tax) | $109.64 |
| Stretch Goals (with tax) | $61.82 |
| **Grand Total** | **$171.46** |

---

## 6.4 Component Purchase Links

### **Base System Links**
- Raspberry Pi 4B (4 GB RAM):  
  https://www.digikey.com/en/products/detail/raspberry-pi/SC0194-9/10258781  

- Raspberry Pi Power Supply:  
  https://www.digikey.com/en/products/detail/raspberry-pi/SC0445/10258760  

- 128 GB Micro SD Card:  
  https://www.amazon.com/dp/B08TJRVWV1  

- SanDisk 256 GB USB 3.0 Flash Drive:  
  https://www.amazon.com/dp/B06XG9XP49  

---

### **Stretch Goal Links**
- ESP32 LoRa V3 Development Kit:  
  https://www.amazon.com/dp/B0D2DBRR6T  

- Adafruit RFM95W LoRa Transceiver Breakout:  
  https://www.mouser.com/c/?q=LoRa%20Radio%20Transceiver%20Breakout  

- 915 MHz LoRa Antenna (2-pack):  
  https://www.amazon.com/dp/B0CSZ14MNY  

- SMA Connector (Edge Launch):  
  https://www.mouser.com/c/tools-supplies/accessories/adafruit-accessories/?q=Edge-Launch%20SMA%20Connector  

---

## 6.5 Summary

- The **base system** remains under the required cost ceiling, enabling compliance with HamSCI's Personal Space Weather Station standards.  
- **Stretch components** enhance telemetry and user experience without affecting core data-logging reliability.  
- The BOM prioritizes affordability, modularity, field serviceability, and long-term scientific sustainability.

---

## 7. Analysis

This section evaluates the throughput requirements, computational demands, and architectural decisions supporting the Data Storage Subsystem. It also explains why the Raspberry Pi 4B is the optimal computing platform for the TEC measurement system.

---

## 7.1 Throughput Analysis

The TEC instrument requires a computing platform capable of:

- Parsing GNSS UBX data at **10 Hz**  
- Computing TEC and scintillation values in real time  
- Generating RINEX 4.0 files at **1 Hz**  
- Logging TEC/scintillation values to storage  
- Generating optional TEC maps  
- Hosting a Wi-Fi dashboard  
- Operating a LoRa transmitter  
- Running background health monitoring

The central computing platform must support **multitasking**, **high I/O throughput**, and **robust memory allocation**.

---

## 7.2 Why a Single-Board Computer (SBC) Is Required

The TEC measurement pipeline performs several computationally intensive tasks:

1. **Real-time GNSS processing**  
   - Parses 10 Hz UBX observables  
   - Extracts pseudoranges, Doppler, SNR, carrier phase  

2. **Scientific computation**  
   - TEC computation  
   - Scintillation index extraction  
   - Real-time filtering  

3. **Standardized data generation**  
   - RINEX 4.0 file creation  
   - Epoch formatting  
   - Multi-constellation support (GPS, GLONASS, Galileo, BeiDou)

4. **Data storage pipeline**  
   - Sequential writes to USB 3.0  
   - File rotation  
   - Error checking  

5. **Networking and telemetry**  
   - Onboard Wi-Fi server (local dashboard)  
   - LoRa telemetry (long-range status packets)  

6. **System monitoring**  
   - Temperature  
   - Battery voltage and current  
   - Storage utilization  
   - Fault conditions  

These tasks require an SBC with:

- High processing throughput  
- ≥ 4 GB RAM  
- USB 3.0 interfaces  
- SPI and UART access  
- Embedded Wi-Fi  
- Linux OS with multi-threading  
- Scientific libraries (Python, C/C++)  

An MCU alone cannot meet these demands.

---

## 7.3 Rationale for Selecting the Raspberry Pi 4B

Team 6 selected the Raspberry Pi 4B due to its balance of performance, reliability, and accessibility.

### **Key Advantages**

#### **1. Processing Power**
- Quad-core 1.5 GHz ARM Cortex-A72 CPU  
- Capable of real-time TEC & scintillation computation  
- Supports concurrent web server + GNSS processing + storage

#### **2. Sufficient Memory**
- **4 GB RAM** allows:
  - TEC computation buffers  
  - File I/O caching  
  - Multi-threaded web services  
  - Future expansion (mapping, SDR experiments)

#### **3. Required Hardware Interfaces**
- **USB 3.0** for high-speed storage  
- **SPI** for LoRa transmitter  
- **UART** for GNSS receiver  
- **GPIO** for sensors, control signals  

#### **4. Built-in Networking**
- Dual-band Wi-Fi for:
  - Standalone Access Point mode  
  - Real-time dashboard  

#### **5. Full Linux OS**
- Native exFAT support  
- RINEX generation tools  
- Python/C computing environments  
- Systemd service management  
- LoRa/UBX parsing libraries

#### **6. Power and Budget Compatibility**
- Consumes **4–6 W**, suitable for:
  - Solar-powered operation  
  - Field deployment  

- Affordable and widely available

---

## 7.4 Summary

The Raspberry Pi 4B is uniquely suited for the TEC instrument:

- Real-time GNSS computation  
- High-rate data logging  
- Onboard Wi-Fi dashboard  
- LoRa communication  
- Standards-based data handling  
- Low-power field operation  
- Affordable and modular  

Its performance ensures the system can run GNSS processing, storage management, telemetry, and diagnostics **simultaneously and reliably**, making it the ideal choice for the TEC project architecture.


<p align="center">
  <img width="794" height="606" alt="image" src="https://github.com/user-attachments/assets/0df0b6a0-2266-4210-a38f-c2b783205d7d" />
</p>

<p align="center"><strong>Figure 1: Raspberry Pi 4B SBC</strong></p>

---

## 8. Storage

The storage subsystem must reliably record high-resolution TEC measurements, system health data, and auxiliary sensor readings over extended periods. This section presents the throughput analysis, storage estimation, and justification for selecting a USB 3.0 thumb drive as the core storage medium.

---

## 8.1 Storage Requirements

The storage system must support continuous logging of:

- TEC and scintillation values (10 Hz)  
- RINEX archival data (1 Hz)  
- TEC map outputs (optional)  
- System-health metrics  
- Diagnostic logs  

It must also:

- Handle large files → **requires exFAT**  
- Maintain high write speed  
- Be reliable in field deployments  
- Operate at low power  
- Be easy to replace in remote conditions  

---

## 8.2 GNSS Sampling Throughput

The u-blox NEO-F9P module samples:

- **Up to 20 satellites simultaneously**  
- At a maximum of **10 Hz** across:
  - GPS  
  - GLONASS  
  - Galileo  
  - BeiDou  

Each UBX packet contains:

- Pseudoranges  
- Carrier phase  
- Doppler  
- Signal-to-noise ratio (SNR)  
- Satellite metadata  

These data are processed by the SBC to compute TEC and scintillation indices.

---

## 8.3 Computed TEC & Scintillation Throughput

Each TEC + scintillation record is stored as:

- **8 bytes per pair** (two 4-byte floats)

Given 10 Hz sampling:

$$
\begin{aligned}
\text{TEC Throughput} &= 8\ \text{bytes} \times 10\ \text{samples/s} \\
                      &= 80\ \text{bytes/s} \\
                      &= 0.08\ \text{kB/s}
\end{aligned}
$$


Actual throughput increases when including metadata.

---

## 8.4 RINEX Throughput

RINEX files store standardized GNSS data at **1 Hz**.

Assumptions:

- 20 satellites  
- 2 signals per satellite  
- 40 lines per epoch  
- 80 bytes per line (conservative)

$$
\begin{aligned}
\text{RINEX Throughput} &= 40\ \text{lines/s} \times 80\ \text{bytes} \\
                        &= 3200\ \text{bytes/s} \\
                        &= 3.2\ \text{kB/s}
\end{aligned}
$$


---

## 8.5 TEC Map Throughput (Optional)

TEC maps may be generated at:

- **100 × 100 grid**  
- Each cell = one 4-byte TEC value  
- Updated once per second

$$
\begin{aligned}
\text{Map Throughput} &= 10{,}000\ \text{cells} \times 4\ \text{bytes} \\
                      &= 40{,}000\ \text{bytes/s} \\
                      &= 40\ \text{kB/s}
\end{aligned}
$$


---

## 8.6 Total Estimated Throughput

Combined streams:

$$
\begin{aligned}
\text{Total Throughput} &= 40\ \text{kB/s (maps)} \\
                        &\quad + 3.2\ \text{kB/s (RINEX)} \\
                        &\quad + 1.6\ \text{kB/s (TEC + scintillation + metadata)} \\
                        &= 44.8\ \text{kB/s}
\end{aligned}
$$


Adding **20% safety margin**:

$$
\text{Final Throughput Requirement} \approx 53.8\ \text{kB/s}
$$


This defines the minimum sustained write performance needed.

---

## 8.7 Daily Storage Requirement

$$
\begin{aligned}
\text{Daily Storage} &= 53.8\ \text{kB/s} \times 3600\ \text{s/hr} \times 24\ \text{hr} \\
                     &\approx 4.65\ \text{GB per day}
\end{aligned}
$$

One month (30 days):

$$
\begin{aligned}
\text{Monthly Storage} &= 4.65\ \text{GB/day} \times 30 \\
                       &\approx 139\ \text{GB/month}
\end{aligned}
$$

To maintain reserve capacity, a **256 GB drive** is required.

---

## 8.8 Why a USB 3.0 Thumb Drive Is the Correct Storage Choice

### **1. Meets Throughput Requirements Easily**
- Typical USB 3.0 write speeds: **20–100+ MB/s**  
- Required throughput: **0.0538 MB/s**

Provides **500× margin**.

---

### **2. Plug-and-Play Field Replaceability**
USB thumb drives are:

- Hot-swappable  
- Replacable without tools  
- Easily upgraded  
- Immediately recognized by Linux  

Essential for remote field deployments.

---

### **3. Compatible With exFAT**
Required for:

- Files > 4 GB  
- Cross-platform data sharing  
- Compliance with ISO/IEC 20933  

USB drives universally support exFAT.

---

### **4. Low Power Consumption**
Typical USB 3.0 drive: **0.05–0.3 W**  
Fits within SBC’s power budget and enables solar-powered field operation.

---

### **5. Durable & Reliable**
- Solid-state  
- No moving parts  
- Resistant to shock/vibration/weather  

---

### **6. Cost Effective**
- 256 GB drives: **$20–$40**  
- Supports project affordability goals.

---

## 8.9 Conclusion

A **256 GB USB 3.0 thumb drive** is the optimal storage medium for the TEC measurement system because:

- It meets and far exceeds write-speed requirements  
- Provides sufficient capacity for ≥ 30 days of data  
- Ensures low power consumption  
- Is simple to replace in the field  
- Supports the exFAT file system standard  
- Is affordable and highly reliable for long-term deployments  

This choice aligns perfectly with the goals of modularity, scientific integrity, and field durability.

<p align="center">
  <img width="722" height="525" alt="image" src="https://github.com/user-attachments/assets/8e8b9d4f-b971-48ce-a1df-011883ed6334" />
</p>

<p align="center"><strong>Figure 2: Thumb Drive Example</strong></p>

---

## 9. Long Range Data Transfer

The TEC measurement system requires a low-power, long-range communication method capable of transmitting essential system-health data, condensed TEC summaries, and diagnostic information far beyond the range of local Wi-Fi. This ensures that users can monitor the system even when deployed in remote or inaccessible locations.

Team 6 evaluated several options including cellular, long-range Wi-Fi, satellite messaging, and LPWAN technologies. After throughput and power analysis, **LoRa** was selected as the optimal method.

---

## 9.1 Data Characteristics

The system must send compact telemetry packets that include:

| Field | Size |
|-------|------|
| TEC Summary | 4 bytes |
| Satellite Count | 1 byte |
| Battery Percentage | 2 bytes |
| Temperature | 1 byte |
| Error Flags | 1 byte |
| Timestamp | 4 bytes |
| Protocol Overhead | 12 bytes |
| Buffer | 15 bytes |

### **Total Packet Size:**  

$$
40\ \text{bytes per transmission}
$$

### **Update Interval:**  
The system transmits **one packet every 15 seconds**.

---

## 9.2 Telemetry Throughput Requirement

Using the maximum packet size: 

$$
\text{Required Throughput} =
\frac{40\ \text{Bytes}}{15\ \text{s}} =
2.67\ \text{bytes/s} \approx 21.4\ \text{bps}
$$

With overhead and retransmissions:

$$
\text{Required Telemetry Throughput} \approx 30\ \text{bps}
$$


This low data rate makes LoRa ideal.

$$
\text{LoRa Throughput} \approx 300\ \text{bps}
$$

---

## 9.3 Why LoRa Was Selected

### **Meets and exceeds telemetry needs**
Even in the *lowest* speed configuration:


This is **10× above** the required 30 bps.

### **Minimal power consumption**
Ideal for solar + battery field operation.

### **Excellent range**
- Typical: **1–5 km**
- With line of sight: 10+ km
- Indoor/urban: 300–800 meters

### **No dependency on external networks**
No cell towers, no Wi-Fi bridges, no fees.

### **Works anywhere**
Forests, mountaintops, deserts, rural fields, research stations.

### **Simple integration**
Works with:
- RFM95W transmitter (on SBC)
- SX1262-based ESP32 LoRa handheld receiver

---

## 9.4 Conclusion

After evaluating alternatives, LoRa clearly provides the best combination of:

- **Range**
- **Low power usage**
- **Reliability**
- **Cost-effectiveness**
- **Robustness**
- **Ease of integration**
- **Telemetry capability**

It ensures the TEC instrument remains verifiable and observable at long distances, even when Wi-Fi is unavailable, making it a critical component of the system’s remote-monitoring design.

---

## 10. LoRa Hardware Selected

LoRa provides the system’s long-range telemetry capability. Team 6 selected a pairing of the Adafruit RFM95W transmitter and an ESP32 LoRa V3 (SX1262) receiver to achieve a balance of long-distance performance, low power consumption, and straightforward integration.

---

## 10.1 Transmitter — RFM95W (Installed in TEC Device)

### **Hardware**
- **Model:** Adafruit RFM95W – 915 MHz  
- **Chipset:** Semtech SX127x-family LoRa modem  
- **Interface:** SPI  
- **Operating Frequency:** 915 MHz (US ISM band)

### **Advantages**
- Proven long-range stability  
- Excellent sensitivity and link budget  
- Strong library support for Linux SBCs  
- Highly reliable in obstructed and multipath environments  
- Compact and low-power, ideal for a solar-battery system

The RFM95W is used as the **primary transmitter** mounted to the SBC to send summarized telemetry packets.

---

## 10.2 Receiver — ESP32 LoRa V3 (Handheld Device)

### **Hardware**
- **Model:** Heltec ESP32 LoRa V3 Board  
- **Chipset:** Semtech SX1262  
- **Display:** Integrated 0.96" OLED  
- **Features:** Wi-Fi, BLE, LoRa, onboard antenna connector

### **Advantages**
- SX1262 chipset offers:
  - Lower power consumption  
  - Higher sensitivity  
  - Better blocking performance than SX127x  
- Integrated OLED:
  - Displays TEC summary  
  - Battery level  
  - Satellite count  
  - Temperature  
  - Error flags  
- No need for external equipment (phones, laptops, etc.)

The handheld receiver provides **portable field visibility**, allowing users to verify system status instantly.

---

## 10.3 Compatibility Between RFM95W (SX127x) and ESP32 LoRa V3 (SX1262)

The two devices are fully compatible when configured with matching:

- **Frequency:** 915 MHz (required)  
- **Bandwidth:** Typically 125 kHz  
- **Spreading Factor:** SF7–SF12  
- **Coding Rate:** 4/5, 4/6, etc.  

Setting these ensures seamless interoperability between transmitter and receiver.

---

## 10.4 Summary

The selected LoRa components were chosen because they are:

- Low-power  
- Long-range  
- Cost-effective  
- Highly reliable  
- Easy to integrate  
- Fully compatible  

Together, the RFM95W transmitter and SX1262-based ESP32 LoRa receiver create a robust telemetry chain that ensures mission-critical system-health and TEC-summary data are always accessible, even at long distances and in remote field environments.

---

## 11. References

[1] u-blox AG, *NEO-F9P GNSS Module Integration Manual (UBX-21031704)*, 2022.

[2] SparkFun Electronics, *SparkFun GNSS-RTK L1/L5 Breakout – NEO-F9P (Qwiic), Product Documentation*, 2023.

[3] International GNSS Service (IGS), *RINEX 4.00: Receiver Independent Exchange Format*, 2021.

[4] ISO/IEC 20933:2014, *exFAT File System Specification*.

[5] USB Implementers Forum, *Universal Serial Bus 3.0 Specification*.

[6] Raspberry Pi Foundation, *Raspberry Pi 4 Model B: Product Brief & Technical Specifications*, 2020.

[7] SanDisk, *Ultra Flair USB 3.0 Flash Drive – Product Specifications*, 2022.

[8] Semtech Corp., *SX1276/77/78/79 LoRa Modem Datasheet*, 2019.

[9] Semtech Corp., *SX1262 LoRa Transceiver Datasheet*, 2021.

[10] Adafruit Industries, “RFM95W LoRa Radio Transceiver Breakout (PID 3072),” Product Page, 2023.

[11] Heltec Automation, *ESP32 LoRa V3 Technical Manual (SX1262)*, 2023.

[12] NASA Space Weather Program, “Understanding Ionospheric Total Electron Content (TEC).”

[13] HamSCI, *Personal Space Weather Station (PSWS) Technical Requirements*, 2022.

[14] M. Hernández-Pajares et al., “The GNSS Ionospheric Mapping Techniques and Models,” *Journal of Geodesy*, vol. 85, no. 12, pp. 1–17, 2011.

[15] National Institute of Standards and Technology (NIST), *Special Publication 800-57: Guidelines for Key Management*, 2019.

[16] IEEE, *IEEE Code of Ethics*, 2020.

---


****Detailed Design****

***Function of the Subsystem***

The function of the subsystem is explained in the following shall statements

- The subsystem shall enclose and secure all other subsystems by providing protection and structure for easy accessibility and intuitive field implementation.
- The enclosure shall provide adequate heat dissipation, allowing the prototype to be properly cooled for consistent operation.
- The enclosure shall provide a robust waterproof case capable of withstanding insects and weather conditions within reason.
- The enclosure shall secure all components during transportation and implementation.
- The design shall provide accessibility for troubleshooting and repairing every component.

***Specifications and Constraints***

The following shall statements comprise the constraints and specifications of the enclosure.

- The enclosure shall be protected against splashing water from any angle for broad field applications (IPX-4 waterproof rating at a minimum). \[IEC 60529-2020\][1]
- The enclosure shall maintain appropriate temperatures to prevent the internal subsystems from overheating.
- The enclosure shall implement waterproof grommets or liquid sealtight fittings at every point of exterior penetration to create a consistent seal.
- The enclosure shall include a small drain hole through the bottom of the enclosure to prevent water from being trapped inside the enclosure.
- The enclosure shall hinder insects from accessing the interior by protecting any exterior penetration.
- The enclosure shall be made of a NEMA 4 rated enclosure ensuring proper protection for indoor and outdoor use. Resilient to weather, abrasions, and general deterioration. \[ANSI/NEMA 250-2020\][2]
- The enclosure shall have a transparent barrier for viewing all internal components for observation during operation.
- The enclosure shall allow for easy access for interchanging parts to promote modularity and flexibility in field and home applications.
- All components shall be secured using appropriately sized screws for sustainable mounting.
- All 3-D printed parts shall be made of PETG.

***Overview of Proposed Solution***

&nbsp;&nbsp;&nbsp;&nbsp;Team 6 proposes the Gratury 16.1" x 12.2" x 7.1" water-resistant outdoor enclosure box as the chosen enclosure. The box shall maintain a rating of IP55 and NEMA 4, exceeding the required waterproof rating and providing durability and protection in rugged environments. The system shall produce 20.65 W at max load (4 W/ft^2) and 8 W at nominal load (1.6 W/ft^2). Using the sealed enclosure temperature rise chart, the enclosure shall satisfy heat regulation requirements by passively removing heat from the enclosure through the Acrylonitrile Butadiene Styrene (ABS) enclosure. [3] The enclosure has a transparent front cover for internal observation during operation. The enclosure uses 304 stainless steel latches, enabling easy access to the internal components and providing a solution which will remain rust free through repeated outdoor exposure. All hardware and components shall be mounted using M4 screws, excluding the PCB (M2) and the GPS module (M3). The battery shall be secured by installing corner brackets (figure 2) above the top right and top left corners of the battery, creating a secure vertical fit. To secure the front and sides of the battery, a large u-bracket (figure 3) shall be installed.

![81I+3fD0CeL._AC_SL1500_](https://hackmd.io/_uploads/Hy4GOCeWbe.jpg)
**Figure 1. Full View of Proposed Enclosure**


<img width="800" height="600" alt="Corner_Supports_V02" src="https://github.com/user-attachments/assets/691652df-bdd7-48bb-b9d9-4769b91831ca" />

**Figure 2. 31x22x19mm Corner Bracket**

<img width="1180" height="568" alt="Screenshot 2026-02-02 141046" src="https://github.com/user-attachments/assets/54e23df9-0cf9-4238-aa52-f65842566deb" />

**Figure 3. 7.1"x3"x3" U-Bracket**

***Buildable Schematic***

![710B15JyV2L._AC_SL1500_](https://hackmd.io/_uploads/rJNC9QW-bl.jpg)
**Figure 5. Exterior Dimensional View**

![Screenshot 2025-11-23 185257](https://hackmd.io/_uploads/Hkqdhm-W-g.png)

**Figure 6. Internal Component Layout**

***BOM***

| **Component** | **Enclosure Box** | **Liquid Seal Tight ½" fitting** | **1/2" Liquid Seal Tight Ferrule** | **Fastener Kit** |
| --- | --- | --- | --- | --- |
| **Manufacturer** | **Gratury** | **Phoenix Contact** | **Phoenix Contact** | **Hilitchi** |
| **Part Number** | **772467660195** | **1411153-ND** | **1411233-ND** | **‎H-M345-510** |
| **Distributor** | **Amazon** | **DigiKey** | **DigiKey** | **Amazon** |
| **Distributor Part Number** | **B0BCVGHF1J** | **1411153** | **1411233** | **‎B073SW4S6C** |
| **Quantity** | **1** | **1** | **1** | **1** | **1** |
| **Purchasing Website URL** | [4] | [5] | [6] | [7] |
| **Total** | **66.99** | **1.63** | **0.46** | **11.59** |
| **Grand Total** | **80.67** |

***Analysis***

&nbsp;&nbsp;&nbsp;&nbsp;Team 6 has concluded the Gratury 16.1" x 12.2" x 7.1" water-resistant outdoor enclosure box is the optimal solution for the needs of the TEC measurement prototype. This enclosure exceeds the minimum required IPX-4 waterproof rating. As stated above, the enclosure shall also the prototype's thermal load requirements. The enclosure is large enough to properly space components for ease of physical access, while leaving room for additional components, encouraging adaptability and modularity (as shown in figure 6). The orientation and spacing has been chosen to allow room for proper heat dissipation and creating the shortest distance for wire connections between devices. The internal back plate is removable, allowing the user to easily transfer the entire component platform in and out of the box, facilitating speed and convenience. The grid design of the backplate accepts a large size variation in fasteners, removing the annoyance of requiring uniform hardware. This will also encourage experimentation and additions to the minimal function of the prototype. Team 6 had the intention of mounting a small transparent faceplate to the chosen enclosure. However, this enclosure's entire latched door is transparent, allowing viewing of the complete interior of the enclosure. The door utilizing stainless steel latches satisfied the requirement for easy access to the internal components without sacrificing sturdiness. Overall, this enclosure exceeds expectations in every regard, and while this specific box may not be accessible anywhere in the world, it exemplifies the characteristics of any enclosure a hobbyist may want to use in their own application.

***References***

\[1\] <https://www.nema.org/docs/default-source/about-us-document-library/ansi-iec_60529-2020-contents-and-scopef0908377-f8db-4395-8aaa-97331d276fef.pdf?sfvrsn=29c118a6_3>

\[2\] <https://www.nema.org/docs/default-source/standards-document-library/ansi_nema_250-2020-contents-and-scope76f809d7-afad-4aa1-80cd-e1d09b60f2e5.pdf?sfvrsn=cb4086bd_3>

\[3\] <https://www.polycase.com/techtalk/aluminum-enclosures/how-to-calculate-temperature-rise-inside-enclosures-2.html>

\[4\]  <[<https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B08282VRXW/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1>](https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B0BCVGHF1J/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1)](https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B0BCVGHF1J/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1)>

\[5\] <https://www.digikey.com/en/products/detail/phoenix-contact/1411153/5188749?gclsrc=aw.ds&gad_source=1&gad_campaignid=17336967819&gbraid=0AAAAADrbLlioVAEPkwSrWuIyQJqISDpQu&gclid=CjwKCAiAuIDJBhBoEiwAxhgyFogJXM6Pct3Bt6_00QRIS_GeVxmJupNwJiNd-5xfBqYYcaVc0cQjCRoCi-MQAvD_BwE>

\[6\] <https://www.digikey.com/en/products/detail/phoenix-contact/1411233/5186528>

\[7\] <https://www.amazon.com/Hilitchi-510pcs-Stainless-Socket-Assortment/dp/B073SW4S6C/ref=asc_df_B073SW4S6C?tag=bingshoppinga-20&linkCode=df0&hvadid=80539418193264&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=84181&hvtargid=pla-4584138888772003&msclkid=f9ab892a8825176c7cf5e057986c6775&th=1>


# Detailed Design - Power Subsystem
The Power Subsystem is responsible for supplying stable, uninterrupted electrical energy to all operational components of the Total Electron Content (TEC) Measurement Device. Its primary function is to convert, regulate, distribute, and protect the electrical power required by all implemented components  and peripherals. This subsystem ensures that each load receives power at the correct voltage level with minimal electrical noise.

At a high level, the Power Subsystem accepts energy from a 12 V LiFePO₄ rechargeable battery serving as the primary energy reservoir with external charging capability. The charging input  will be able to accept either a 19.5 V DC power supply or a plug-in 12 V rated solar panel. A lithium-compatible charge controller manages these external inputs, maintaining proper charging profiles for the battery while preventing common electrical faults. Once stored in the battery, energy is delivered to the internal power distribution network, where it is converted into regulated 5 V and 3.3 V power rails through high-efficiency buck regulators. These rails power all necessary  components, ensuring that all experience stable voltage conditions even during high-load events.

The subsystem also integrates electrical protection mechanisms, including fuses, transient voltage suppressors, and reverse-polarity diodes. This is necessary in order to shield downstream components from input faults, wiring errors, and environmental disturbances.  Additional filtering elements, such as ferrite beads and low-noise post-regulation stages, maintain signal integrity by reducing switching noise and preventing electromagnetic interference from propagating into noise-sensitive RF circuits. These measures ensure that the GNSS receiver maintains high carrier-to-noise density (C/N₀) and mitigates degradation of measurement accuracy caused by unstable or noisy power rails.

Unlike the one implemented in the ScintPi project, this Power Subsystem enables full autonomy of the TEC measurement device by providing portable, extended runtime capabilities without dependence on fixed AC power [1]. When deployed in the field, the LiFePO₄ battery delivers the energy required for long-duration observation sessions, while the plug-in solar input allows the device to recharge during daylight hours and remain operational for extended or indefinite periods. In laboratory or residential settings, the subsystem seamlessly transitions to AC-powered charging via the 19.5 V DC converter while continuing to power the device in real time.

Overall, the Power Subsystem functions as the foundational infrastructure supporting the reliability, precision, and field portability of the TEC measurement instrument. By ensuring clean, stable, and protected power delivery, the subsystem enables the GNSS processing chain, data acquisition system, and storage module to perform at the accuracy and stability levels required for scientific ionospheric measurements.

## Specifications and Constraints
The Power Subsystem is governed by a set of design constraints that ensure safe, reliable, and continuous operation of the TEC measurement device across all intended environments. These constraints arise from electrical and physical limitations, interactions with other subsystems, battery chemistry requirements, international standards, and socio-economic factors. Together, they define the performance envelope within which this subsystem must operate.

The specifications and rational for each component for the power system are as follows:

1.  This power subsystem shall implement a battery of at least 235Wh of usable energy
- As discussed later in the document, the nominal power draw of all components will be ~8W total, with a theoretical max continuous power draw of 21W [2, 3, 4, 5]. 
- Assuming at least 235Wh of usable energy, this amount would give a nominal energy life of ~30-32 hours and ~9-11 hours at maximum load, which is within the specified constraints of the conceptual design of 15-hour average usage [6]

2.  This subsystem shall implement a charge controller capable of regulating all current flow to and from the energy storage solution
- As discussed later in this documentation, the use of a LiFePO4 will require a charge controller to be implemented to regulate charge current of the battery [6,  7]
- To follow applicable IEEE and IEC standards discussed in Team 6 conceptual design, a charge controller with appropriate specifications  is  necessary  when using a lithium-based battery [6, 8,  9]

3.  This subsystem shall be capable of recharging energy via 120 VAC adapter input or an optional solar panel input
- As discussed in Team 6’s conceptual design, to achieve mobility this subsystem will make our device capable of recharging in most reasonable conditions to extend operation [6]
- For this device to be modular, the ability to recharge with multiple solutions extend the flexibility and modularity of the device giving the user the ability to  customize their charging solution if desired [6]

To always provide safe operation, the subsystem shall be designed with the following constraints:

1.  The power subsystem shall incorporate proper fusing between all critical components, including the battery, charge controller, and PCB power input
- To follow applicable IEEE/IEC standards, proper fusing is necessary for safe operation [8, 9, 10, 11]
- The charge controller manual gives instructions on proper use of the device, including proper fusing parameters of its defined connections [12]
    

2. This subsystem shall incorporate purchased components manufactured with built in fault protection protocols
- To follow applicable IEEE/IEC standards, component  selection will favor those that have built in fault protection protocols.
- The charge controller manages current flow to and from the battery. Therefore, the charge controller should have over voltage, current and reverse current protection protocols [12]
- With a lithium-based battery, the risks associated with them are thermal runaway and short circuit faults. Therefore, this component  should have a built in Battery Management System (BMS) that have over voltage, over current and temperature protections [7]
- The PCB manages all connections and interfaces to all device subsystems. Because of this, there should be components incorporated  to handle common faults such as over voltage, over current and reverse polarity [13]

To Interface with all required components, the power subsystem must follow the following applicable constraints:

1.  The power subsystem shall be capable of delivering at least 25 W continuous output across all rails with a peak capability of ≥ 30  W for transient events
- The nominal power draw of all chosen main components discussed in other subsystems is ~8W, where the maximum power draw is ~21W. This includes the Raspberry Pi4B, Raspberry Pi Pico, Ublox NEO F9P, Ublox dual-tuned patch antenna, USB thumb drive, and power dissipated over PCB components [2, 3, 4, 5].
- Due to component boot inrush and transient events, being able to support up to 25W of continuous power will provide enough headroom for these components to properly function. 

2.  The 5V rail shall supply at least 3A continuous, supporting the Raspberry Pi 4B, RF module interface boards, USB peripherals, and any future 5V accessories 
- According to the Raspberry Pi 4B, in order to support all peripherals, it requires at least a 3A input at 5V. Therefore, our system shall supply these specifications with enough headroom for additional devices if needed [2].

3.  The 3.3V rail shall supply at least 1A continuous, powering the Raspberry Pi Pico, GNSS control logic, level shifters, and digital/analog sensors 
- According to their respective datasheets, all 3.3V-based components must be fed proper power specifications due to their sensitive internal components [3, 4].

4.  Regulated rails (5 V, 3.3 V) shall remain within ±5% of nominal voltage under all normal operating load conditions.
- According to the Pi foundations hardware documentation, the Raspberry Pi4B requires a 5.0V input with a tolerance of ±5%. Therefore, this should be supplied to ensure proper functionality [2]

5.  The 5V and 3.3V rails shall maintain output ripple < 50mVpp in the frequency bands that could interfere with GNSS reception, to prevent degradation of RF performance.
- The Raspberry Pi Pico uses the RP2040 MCU, whose recommended operating voltage is 3.3V ±10%, however stable operation and peripheral accuracy rely on tighter regulation (< ±5%). The RP2040 datasheet notes I/O characteristics and ADC accuracy degrade when VDD exceeds recommended limits. Thus, ±5% ensures full ADC accuracy and digital timing integrity [3]
- The U-blox M8/M9 GNSS Hardware Integration Guide states that the ripple on the supply must be less than 50 mVpp. Switching power supplies must be carefully filtered to avoid degrading GNSS sensitivity [4]

## Overview of Proposed Solution
The power subsystem for Team 6’s TEC measurement device is implemented as a hybrid AC/Solar capable rechargeable architecture built around a 12 V-class LiFePO₄ battery, a 20A PWM charge controller, a 200W 19.5V XT60 AC power supply, an optional 100W 12V solar panel. A central PCB is implemented that provides low-voltage rails for the Raspberry Pi 4B, Raspberry Pi Pico, u-blox NEO-F9P module, and supporting electronics. Below is the comprehensive power budget for all components this subsystem needs to provide.

**Power Budget (Nominal Operation)**
| Input Voltage | Component | Quantity | Current (A) | Power (W) | Regulator Type | Efficiency (%) |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | TPS62913 Buck 12-5V | 1 | 0.6 | 0.7 | Buck | 96 |
|  | Bel Fuse PTC Fuse 3A Trip | 1 | 0.6 | 0.11 |  |  |
|  | SS32 Schottky Diode | 2 | 0.6 | 0.75 |  |  |
|  | PWM Charge Controller | 1 | 0.6 | 0.1 |  |  |
| 5 | TPS62913 Buck 5-3.3V | 1 | 0.4 | 0.1 | Buck | 96 |
|  | TPS2121 Power MUX | 1 | 1.5 | 0.1 |  |  |
|  | YAGEO PTC Fuse 5A Trip | 1 | 1.5 | 0.05 |  |  |
|  | Raspberry Pi 4B SBC | 1 | 1.0 | 5.0 |  |  |
|  | 256GB USB Thumb drive | 1 | 0.1 | 0.5 |  |  |
|  | TVS Diode | 1 | Negligible | Negligible |  |  |
|  | Indicator LED | 1 | Negligible | Negligible |  |  |
| 3.3 | Ublox NEO F9P | 1 | 0.12 | 0.4 |  |  |
|  | Raspberry Pi PICO MCU | 1 | 0.05 | 0.16 |  |  |
|  | Indicator LED | 1 | Negligible | Negligible |  |  |
|  | (Optional) LoRa Module | 1 | 0.01 | 0.03 |  |  |
|  | (Optional) Magnetometer | 1 | Negligible | Negligible |  |  |
|  |  |  | **TOTALS** | **8.0W** |  | **92.2%** |

**Power Budget (Theoretical Maximum Operation)**
| Input Voltage | Component | Quantity | Current (A) | Power (W) | Regulator Type | Efficiency (%) |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | TPS62913 Buck 12-5V | 1 | 1.6 | 2.0 | Buck | 92 |
|  | Bel Fuse PTC Fuse 3A Trip | 1 | 1.6 | 1.1 |  |  |
|  | SS32 Schottky Diode (x2) | 2 | 1.6 | 1.2 |  |  |
|  | PWM Charge Controller | 1 | 1.6 | 0.15 |  |  |
| 5 | TPS62913 Buck 5-3.3V | 1 | 0.5 | 0.45 | Buck | 92 |
|  | TPS2121 Power MUX | 1 | 3.0 | 0.36 |  |  |
|  | YAGEO PTC Fuse 5A Trip | 1 | 3.0 | 0.12 |  |  |
|  | 256GB USB Thumb drive | 1 | 0.25 | 1.25 |  |  |
|  | Raspberry Pi 4B SBC | 1 | 2.5 | 12.5 |  |  |
|  | TVS Diode | 1 | Negligible | Negligible |  |  |
|  | Indicator LED | 1 | Negligible | Negligible |  |  |
| 3.3 | Ublox NEO F9P | 1 | 0.2 | 0.66 |  |  |
|  | Raspberry Pi PICO MCU | 1 | 0.1 | 0.33 |  |  |
|  | Indicator LED | 1 | Negligible | Negligible |  |  |
|  | (Optional) LoRa Module | 1 | 0.15 | 0.5 |  |  |
|  | (Optional) Magnetometer | 1 | Negligible | Negligible |  |  |
|  |  |  | **TOTALS** | **20.65W** |  | **84.7%** |

## System Architecture
The overall architecture of the system is defined as follows.
1.  Energy is stored in a 12.8V LiFePO₄ battery sized to provide ≥ 235Wh usable energy capacity.
2.  Storage solution can recharge from either a 120 VAC to 19.5V DC XT60 power supply or an optional 100W 12V solar panel.
3.  All charge and discharge currents are managed through a 20A rated  LiFePO₄-compatible PWM charge controller.
4.  Energy is distributed through the central PCB, which provides tightly regulated 5V and 3.3V rails with low ripple for the processing and RF components.
5.  Layered protection and fusing is implemented that satisfies IEEE/IEC safety expectations and mitigates hazards associated with lithium-based storage.

**Battery Component**: For Team 6’s functional prototype, we have chosen the ZapLitho 12V 22Ah with a 30A BMS [7].The integrated Battery Management System (BMS) provides over-charge, over-discharge, over-current, and over-temperature protections, satisfying the constraint that lithium storage must include internal fault mitigation to reduce thermal-runaway and short-circuit risk.

Assuming 85–90% usable depth-of-discharge to preserve cycle life, this component  advertises 240Wh of usable energy, satisfying the subsystem specification of ≥235Wh of usable energy. Because of the lack of raw computation needed for TEC measurements, a power draw near the theoretical maximum rated power draw for all components is not expected under any circumstances unless the user chooses to add features beyond the main scope of this device. Because of this, a powerdraw around the nominal rated usage would be a more accurate representation to compute expected runtime. At a nominal system power draw of ≈8W at 92.2% efficiency, the estimated system runtime equates to roughly 27.65 hours. These values meet the conceptual design requirement for ~15 hours of average usage while still reserving margin to protect the battery from deep discharge. An XT60 to O-Ring Adapter purchased from amazon will be used to connect this battery to the charge controller. A 30A inline fuse will be connected to this device to protect the charge controller from electrical faults, and add a layer of protection in addition to the battery management system.

<div align="center">
    <img width="712" height="735" alt="Screenshot 2025-11-24 205510" src="https://github.com/user-attachments/assets/3c99c4da-1631-43a0-a4ad-c0e22737c993" />
    <p><strong>Figure 1:</strong> ZapLitho 12V 22Ah Battery with BMS</em></p>
</div>

<div align="center">
    <img width="688" height="753" alt="image" src="https://github.com/user-attachments/assets/0857110a-3b7f-4cfd-9b34-d1845dade4ee" />
    <p><strong>Figure 2:</strong> XT60 to O-Ring Adapter</em></p>
</div>

**Charge Controller Component**: For a charge controller, Team 6 has chosen to implement the Limu Solar LTB Series 20A PWM Solar Charge Controller for our functional prototype [12]. This device supports LiFePO₄, lithium  chemistries, uses a three-stage PWM charging algorithm, and accepts solar inputs up to 50V while managing a 20A battery charge and load current.

The controller’s battery terminals connect directly to the LiFePO₄ pack, and its load terminals feed the 12V bus that supplies the PCB and any future 12 V accessories. The specific connector scheme and wiring gauge for these interfaces will be defined in a later section of the detailed design. 12AWG wire will be implemented to all connected components in order to be able to handle the charge contollers 20A rated max current draw. These wires will be black and red in order to differentiate positive and negative terminals within the system. In line fuses will be connected between critical components such as the battery and charge controller, and the charge source and controller. This will add extra fault protections in order to protect all connected components. These connections will be soldered and heatshrunk to provide stability. In the case of the charge source and battery inputs, XT60 connectors will be used to terminate wires. This will provide quick disconnects between components such as the battery and charging source to provide modularity and compatability with chosen components. A MALE barrel jack cable will be connected to the output terminal of the charge controller, giving this device the ability to connect with the PCB and provide power.

<div align="center">
    <img width="840" height="656" alt="Screenshot 2025-11-24 210257" src="https://github.com/user-attachments/assets/9e2252d1-cb16-491f-8abf-df5d0ca4614c" />
    <p><strong>Figure 3:</strong> Charge Controller (20A, 12/24V)</em></p>
</div>

<div align="center">
    <img width="860" height="821" alt="image" src="https://github.com/user-attachments/assets/db38af1c-99be-45bd-8350-21c276defd15" />
    <p><strong>Figure 4:</strong> XT60 Male and Female Wire Terminals</em></p>
</div>

<div align="center">
    <img width="748" height="846" alt="image" src="https://github.com/user-attachments/assets/25d90f6e-c7d0-461b-8eb6-89f155fd0db0" />
    <p><strong>Figure 5:</strong> 16AWG Barrel Jack Connectors</em></p>
</div>

<div align="center">
    <img width="838" height="801" alt="image" src="https://github.com/user-attachments/assets/f41964af-de7b-4212-bbb0-d16f6a5067a7" />
    <p><strong>Figure 6:</strong> 12AWG Inlne Fuse Holder</em></p>
</div>

<div align="center">
    <img width="796" height="795" alt="image" src="https://github.com/user-attachments/assets/97f3c4fa-fd8e-413f-99a8-6eec9b447ec1" />
    <p><strong>Figure 7:</strong> Black and Red 12AWG Wire</em></p>
</div>

**DC Power Supply Component**: For mains charging of Team 6’s functional prototype, we have decided to use the SUPULSE 200W AC power adapter with 19.5V, 10.3A DC output and an XT60 connector [14]. This supply is designed for RC LiPo charging, and its 19.5V DC output falls directly within the PV input range of the solar charge controller, allowing it to be treated as a “synthetic solar panel” when plugged into the controller’s PV terminals. A 25A inline fuse will be connected to this device to protect the charge controller from electrical faults from the charging source.
<div align="center">
    <img width="838" height="703" alt="Screenshot 2025-11-24 205510" src="https://github.com/user-attachments/assets/11fac487-ae81-48df-b2f9-73f8b71a5af3" />
    <p><strong>Figure 8:</strong> XT60 AC/DC Power Supply (19.5V, 10.3A, 200W)</em></p>
</div>

**Solar Panel Component**: This subsystem gives the user the ability to charge the device through two means of charging. The ability to charge the device via solar panel is given by the selected PWM charge controller above.

For our functional prototype, Team 6 has selected the Rvpozwer 18BB 100-Watt Solar Panel [15]. This is a 12V monocrystalline N-type panel with 18-busbar cells and claimed module efficiency up to 25%. The panel is mechanically compact at roughly 40 in × 18 in and weighs about 6 kg, with an anodized aluminum frame and tempered glass front. The components' advertised specifications and price were among the best compared to other options offered by the distributor. This component is also within the specified price given in the conceptual design [6].  
<div align="center">
    <img width="632" height="675" alt="Screenshot 2025-11-24 210809" src="https://github.com/user-attachments/assets/6d3a8fc3-b4a4-44ea-877b-cc3f3b4e50de" />
    <p><strong>Figure 9:</strong> N-Type Monocrystalline 18BB 100W 12V Solar Panel)</em></p>
</div>

<div align="center">
    <img width="894" height="833" alt="image" src="https://github.com/user-attachments/assets/3e0d9243-82d8-4109-8b54-d36af35e4963" />
    <p><strong>Figure 10:</strong> MC4 to XT60 Adapter </em></p>
</div>

**PCB Power Rail Components**: The PCB power section provides the final stage of regulated, protected, and selectable power for all digital and RF subsystems, using a combination of the TPS2121 Power Multiplexer, TPS62913 Buck Converters, board-level filtering components, and two user-selectable input connectors. This portion of the subsystem is designed to meet the system’s constraints on modularity, ripple performance, voltage stability, and safety, without requiring the reader to understand the low-level circuit mechanisms. 
The board supports two power-entry options:
1.  12 V Barrel Jack Input (CUI Devices PJ-063AH Barrel Jack) [16] 
2.  5 V USB-C Input (Abra CON-USB-C-CL 5A Power Connector) [17]
    
The PCB includes a barrel-jack input rated for up to 24VDC and 8A. This input is protected by a bidirectional polyfuse with a 1.5A hold and 3A trip rating, satisfying the project requirement for upstream overcurrent protection between critical components [18]. A bidirectional TVS diode (SMBJ15CA) with a 15V reverse standoff, 16.7V breakdown voltage, and 24.4V clamping voltage is placed across the input, and four SS32 Schottky diodes (20V, 3A) are arranged in a full-bridge configuration to ensure correct polarity regardless of how the barrel connector is wired. Together, these components protect the system by clamping surges, preventing reverse-polarity faults, and limiting over-voltage excursions at the input [19], while the Schottky diodes provide the advantage of low forward voltage and reduced thermal dissipation [20]. Additional smoothing capacitors filter the rectified input, enabling the barrel jack to operate as a universal DC plug-in interface. 

The protected 12V input is stepped down to 5V using a TPS62913 synchronous buck converter. The TPS6291x family provides high efficiency, low output ripple, and low noise switching performance appropriate for RF-sensitive designs [21]. In this design, VIN is tied to EN and S-CONFIG, which selects a 2.2 MHz switching frequency; the recommended 470 nF capacitor sets up a 5ms soft-start timing. The PSNS pin is tied to ground to disable current-sense reporting. The PG pin is unused and left floating per datasheet guidance. A 2.2 µH inductor is selected as required for outputs above 3.3V when switching at 2.2 MHz, and the SW node is routed with proper filtering to reduce switch-node ringing. Voltage regulation is achieved using the device’s 0.8V reference via a resistive divider, designed per datasheet recommendations. All external components follow TI’s reference design values [21]. The resulting 5V rail then supplies the Raspberry Pi 4B, RF modules, and USB storage devices. 

The regulated 5V output feeds the TPS2121 power multiplexer, which also receives the USB-C input through its independent channel. A resistive divider sets the CP2 pin to 2V. The TPS212x family supports Dual-Input, Single-Output (DISO) multiplexing and provides automatic detection, prioritization, and seamless source transition between the available power inputs [22]. Prioritization is established by raising PR1 above CP2; in this design, PR1 receives 4V from the USB-C path, ensuring that USB-C is selected whenever both sources are present. Section 7.5 of the TPS2121 datasheet specifies a 29.8 kΩ resistor on ILIM for a typical 3.5A output limit. A 1 µF capacitor on the SS pin sets an 88 V/s output slew rate, defining a controlled soft start. OV pins are not used and tied to the ground. This configuration satisfies system modularity requirements by enabling automatic selection between LiFePO₄ battery power and USB-C external power. 

A second TPS62913 buck converter then generates the regulated 3.3V rail for the Raspberry Pi Pico, GNSS control logic, sensors, and level shifters. Both buck stages use TI-recommended LC networks and filtering, which reduces conducted noise, switching ripple, and high-frequency transients. This configuration ensures the design meets the system’s strict ripple constraints, particularly those required for GNSS receiver performance. A figure later in this document illustrates the expected ripple based on the manufacturer’s recommended filtering network [21]. 

<div align="center">
    <img width="795" height="323" alt="Screenshot 2025-11-24 211904" src="https://github.com/user-attachments/assets/21f408bd-5921-4a15-bb84-73294a03945b" />
    <p><strong>Figure 11:</strong> 5-3.3V Ripple and Ripple FFT after all filtering [21]</em></p>
</div>

For users wishing to run the device directly from USB-C power, the PCB includes the Abra CON-USB-C-CL connector [17], capable of supporting 20VDC at 3A. Two 5.1 kΩ pull-down resistors on CC1 and CC2 establish proper sink-side CC negotiation. The VBUS path is protected with a 3A/5A-trip polyfuse, followed by a USB-side TVS diode (5V standoff, 6.4V breakdown, 9.2V clamp). The smoothed VBUS feed is then routed into the TPS2121 multiplexer, with a local voltage divider providing the 4V PR1 signal to establish USB-priority. 

The TPS2121 automatically switches between the 5V derived from the 12V battery and the 5V supplied via USB-C, ensuring seamless transitions and maximizing battery longevity. This behavior aligns with system requirements for reliability, modularity, and field flexibility. Together, the PCB power architecture acts as the final regulated interface between the energy subsystem and the low-voltage electronics, providing stable 5V and 3.3V rails with low ripple, integrated protection against surges and reverse polarity, and compliance with IEEE/IEC expectations for safe power delivery. Overall, this stage ensures robust, low-noise, and reliable power for all downstream subsystems. 

The PCB power section acts as the final interface between the main battery/charger system and all low-voltage electronics, ensuring devices receive clean, stable power. The two buck converters generate low-noise 5V and 3.3V rails required by the Pi, Pico, and GNSS module, meeting the system’s voltage-regulation and ripple constraints. Integrated protection elements provide overcurrent, surge, and reverse-polarity safety consistent with IEEE/IEC constraints. Overall, this design stage ensures reliable, low-ripple power delivery to all subsystems. 

**For more information on the PCB  component configuration  and topology within this subsystem, see Team 6’s detailed design of the PCB interconnections  by Jack Bender** [13].

## High-Level Flowchart & Buildable Schematic
Below is a rough schematic of the PCB layout for the distribution of power rails, filtering, and external input. A table of all devices below clarifies specific components within this schematic, to a reference to their specific datasheet.
<div align="center">
    <img width="3123" height="913" alt="Screenshot_2025-11-23_at_6 42 16_AM" src="https://github.com/user-attachments/assets/7e519f87-c389-4c1c-95ed-9470138b61fa" />
    <p><strong>Figure 12:</strong> PCB Power Schematic [13]</em></p>
</div>

| Component | Schematic Symbol | Datasheet Link |
| --- | --- | --- |
| PJ-063AH Barrel Jack | J3 | https://www.sameskydevices.com/product/resource/pj-063ah.pdf |
| UJC-HP2-3-SMT-TR USBC | J1 | https://www.sameskydevices.com/product/resource/ujc-hp2-3-smt-tr.pdf |
| Bel Fuse 0ZCG0150BF2C 3A, 5A Hold, 3A Trip PTC Fuse | F1 | https://www.belfuse.com/media/datasheets/products/circuit-protection/ds-cp-0zcg-series.pdf |
| YEGEO SMD2920B300TF/15 3A Hold, 5A trip PTC Fuse | F2 | https://www.yageogroup.com/content/Resource%20Library/Datasheet/SMD2920_1.pdf |
| SMB15.0A-13-F TVS Diode | CR1 | https://www.littelfuse.com/assetdocs/tvs-diodes-smbj-series-datasheet?assetguid=ba555e99-a12d-4f72-a0b6-86b06c67171e |
| SMB15CA TVS Diode | D5 | https://www.littelfuse.com/assetdocs/tvs-diodes-smbj-series-datasheet?assetguid=ba555e99-a12d-4f72-a0b6-86b06c67171e |
| SS32 Schottky Diode | D1, D2, D3, D4, D7 | https://www.onsemi.com/pdf/datasheet/ss39-d.pdf |
| Buck Converter | U5, U6 | https://www.ti.com/lit/ds/symlink/tps62913.pdf |
| Power MUX | U4 | https://www.ti.com/lit/ds/symlink/tps2120.pdf?HQS=dis-dk-null-digikeymode-dsf-pf-null-wwe&ts=1764003844946 |
| 22uF Electrolytic Capacitor | C36, C38, C44, C45, C46, C47, C48 C53, C54, C55, C56, C57 | https://www.niccomp.com/pdf/NACE.pdf |
| 10uF Ceramic Capacitor | C1, C40, C41, C42, C49, C50 | https://product.tdk.com/info/en/documents/catalog/mlcc_commercial_general_en. |
| 0.1uF Ceramic Capacitor | C37, C39 | https://www.kyocera-avx.com/wp-content/uploads/2021/03/KGM-Series.pdf |
| 2.2nF Ceramic Capacitor | C42, C51 | https://datasheet.murata.com/GRM155R71H222KA01.pdf |
| 22uF Ceramic Capacitor |  | https://product.tdk.com/info/en/documents/catalog/mlcc_commercial_general_en. |
| 470nF Ceramic Capacitor | C43, C52 | https://content.kemet.com/datasheets/KEM_C1002_X7R_SMD.pdf |
| 1uF Ceramic Capacitor | C3 | https://datasheet.samsungsem.com/mlcc.pdf |
| Ferrite Bead | FB4, FB5 | https://datasheet.murata.com/BLE18PS.pdf |
| 2.2mH Inductor | L4, L5 | https://www.coilcraft.com/en-us/products/power/xgl4030/xgl4030.pdf |
| 4.87kOhm Resistor | R30, R32 | https://www.seielect.com/catalog/sei-rmcf.pdf |
| 25.5kOhm Resistor | R29 | https://www.seielect.com/catalog/sei-rmcf.pdf |
| 1.2kOhm Resistor | R22 | https://www.seielect.com/catalog/sei-rmcf.pdf |
| 7.15kOhm Resistor | R26 | https://www.seielect.com/catalog/sei-rmcf.pdf |
| 5.0kOhm Resistor | R23, R27 | https://www.vishay.com/docs/20035/crcw.pdf |
| 29.8kOhm Resistor | R28 | https://www.koaspeer.com/pdfs/RN73.pdf |
| 5.1kOhm Resistor | R1, R2 | https://www.yageo.com/upload/media/product/productseries/datasheet/rchip/yc/rc0805.pdf |
| 270Ohm Resistor | R34 | https://www.yageo.com/upload/media/product/productseries/datasheet/rchip/yc/rc0805.pdf |
| 620Ohm Resistor | R33 | https://www.yageo.com/upload/media/product/productseries/datasheet/rchip/yc/rc0805.pdf |

<div align="center">
    <img width="688" height="567" alt="image" src="https://github.com/user-attachments/assets/af7b6fd5-aa83-4abe-8408-4252fe88514b" />
    <p><strong>Figure 13:</strong> High Level Power Subsystem Flowchart</em></p> 
</div>

## Bill Of Materials
Below is a comprehensive list of all necessary components that are a part of this subsystem. All components are listed with their manufacturer, part number, quantity, price, and purchasing URL. Note that the nature of the power subsystem specifically extends into the Interfacing/PCB subsystem [13].  

Therefore, some components may also be reflected in that respective detailed design document. Therefore, the price of these components shall be obviously reflected in the bill of materials as Total price of MAIN components and total price of ALL components, which include the main components plus components used for the PCB integration. At the end of this table, both the main and all components of pre-tax and post-tax total cost are reflected, respectively. The United States of Tennessee's average state and federal tax rates in the year 2025 were taken into consideration for post-tax calculations. Delivery and packaging costs were not reflected in this bill of materials.

**BOM: Material Specifications**
| Component | Total Cost(US$) | Quantity | Manufacturer | Part No. | Distributor | Distributor Part No. |
| --- | --- | --- | --- | --- | --- | --- |
| XT60 AC/DC Power Supply (19.5V, 10.3A, 200W) | 49.99 | 1 | Supulse | EXAC00591 | Amazon | ASIN B08L39D2NY |
| PWM Charge Controller (20A, 12/24V) | 21.99 | 1 | SOGTICPS | N/A | Amazon | ASIN B0FN7Q2X3L |
| LiFePO4 Battery (22Ah, 12V) | 53.99 | 1 | ZapLitho | YD1222/ZYD1222 | Amazon | ASIN B0F1FRBMG3 |
| 12 AWG Black/Red Wire | 8.99 | 1 | Zhongwang | N/A | Amazon | ASIN B0D12VYLGV |
| 10 Pair XT60H Bullet Connectors | 7.99 | 1 | MCIGICM | 727040387006 | Amazon | ASIN B07Q2SJSZ1 |
| 2Pack 16AWG Barrel Jack Connectors | 10.99 | 1 | Mandyyan | DC5521 | Amazon | ASIN B0BLYMVWNP |
| 4 Pack 12AWG Inline Fuse Holder w/ Fuses | 7.99 | 1 | Cooclensportey | CS011 | Amazon | ASIN B0FDJYRGB7 |
| XT60 to O ring Connector | 8.99 | 1 | ELFCULB | ELFCULB-XT60-2FT | Amazon | ASIN B0C9D74XP3 |
| *Solar Panel (12V, 100W) | 59.99 | 1 | Rvpozwer | N/A | Amazon | ASIN B0DSHPR3KH |
| *MC4 to XT60 FEMALE Adapter | 7.99 | 1 | MENTBERY | XT60-12AWG-2ft | Amazon | ASIN B0DPZRXLYN |
| USBC Power Connector | 0.51 | 1 | ABRA | UJC-HP2-3-SMT-TR | DigiKey | 2223-UJC-HP2-3-SMT-TRCT-ND |
| Barrel Jack | 1.50 | 1 | Same Sky | PJ-063AH | DigiKey | CP-063AH-ND |
| 22uF Electrolytic Capacitor | 1.32 | 4 | NIC Components | 4988-NACE220M35V6.3X5.5TR13FCT-ND | DigiKey | 4988-NACE220M35V6.3X5.5TR13FCT-ND |
| 10uF Ceramic Capacitor | 3.30 | 10 | TDK Corp. | C2012X7S1E106K125AC | DigiKey | 445-181600-1-ND |
| 0.1uF Ceramic Capacitor | 0.32 | 4 | KYOCERA AVX | KGM21NR71H104KT | DigiKey | 478-KGM21NR71H104KTCT-ND |
| 2.2nF Ceramic Capacitor | 0.60 | 6 | Murata Electronics | GRM155R71H222KA01D | DigiKey | 490-1305-1-ND |
| 22uF Ceramic Capacitor | 6.98 | 20 | TDK Corp. | C2012X7S1A226M125AC | DigiKey | 445-14560-1-ND |
| 470nF Ceramic Capacitor | 1.08 | 4 | KEMET | C0805C474K5RACTU | DigiKey | 399-C0805C474K5RACTUCT-ND |
| 1uF Ceramic Capacitor | 0.16 | 2 | Samsung | CL21B105KBFNNNE | DigiKey | 1276-1029-1-ND |
| Ferrite Bead | 1.16 | 4 | Murata Electronics | BLE18PS080SN1D | DigiKey | 490-BLE18PS080SN1DCT-ND |
| 2.2mH Inductor | 6.30 | 2 | Coil Craft | XGL4030-222MEC | DigiKey | 2457-XGL4030-222MEC-ND |
| 4.87kOhm Resistor | 0.40 | 4 | Stackpole Electronics | RMCF0805FT4K87 | DigiKey | RMCF0805FT4K87CT-ND |
| 25.5kOhm Resistor | 0.20 | 4 | Stackpole Electronics | RMCF0805FT25K5 | DigiKey | RMCF0805FT25K5CT-ND |
| 5.1kOhm Resistor | 0.56 | 4 | Vishay Dale | CRCW08055K00JNTA | DigiKey | 541-CRCW08055K00JNTACT-ND |
| 1.2kOhm Resistor | 0.20 | 2 | Stackpole Electronics | RMCF0805FT1K20 | DigiKey | RMCF0805FT1K20CT-ND |
| 7.15kOhm Resistor | 0.20 | 2 | Stackpole Electronics | RMCF0805FT7K15 | DigiKey | RMCF0805FT7K15CT-ND |
| 29.8kOhm Resistor | 0.28 | 2 | KOA Speer Electronics | RN73R2ATTD2982B50 | DigiKey | 2019-RN73R2ATTD2982B50CT-ND |
| 5.1kOhm Resistor | 0.60 | 6 | YAGEO | RC0805JR-075K1L | DigiKey | 311-5.1KARCT-ND |
| 270Ohm Resistor | 0.09 | 10 | YAGEO | RC0805JR-07270RL | DigiKey | 311-270ARCT-ND |
| 620Ohm Resistor | 0.11 | 10 | YAGEO | RC0805FR-07620RL | DigiKey | 311-620CRCT-ND |
| Schottky Diode | 4.14 | 10 | Onsemi | SS32 | DigiKey | SS32CT-ND |
| TVS Diode USB | 0.42 | 2 | Littelfuse Inc. | SMBJ15A | DigiKey | SMBJ15ALFCT-ND |
| TVS Diode Barrel | 0.64 | 2 | Littelfuse Inc. | SMBJ15CA | DigiKey | SMBJ15CALFCT-ND |
| Indicator LED | 1.80 | 10 | King Bright | AP3216EC | Digikey | 754-AP3216ECCT-ND |
| PTC RESET FUSE 24V 3A Hold, 5A Trip (USBC) | 0.78 | 2 | YEGEO | SMD2920B300TF/15 | DigiKey | 13-SMD2920B300TF/15CT-ND |
| PTC RESET FUSE 15V, 1.5A Hold, 3A Trip (Barrel) | 0.54 | 2 | Bel Fuse Inc. | 0ZCG0150BF2C | DigiKey | 5923-0ZCG0150BF2CCT-ND |
| Buck Converter | 10.00 | 4 | Texas Instrument | TPS62913RPUR | DigiKey | 296-TPS62913RPURCT-ND |
| Power MUX | 4.74 | 2 | Texas Instrument | TPS2121RUXR | DigiKey | 296-53410-1-ND |
| Total [Main] | $238.90 ($261.86) |  | Total [Main +PBC] | $287.23 ($314.83) |  |  |


**BOM: Material Purchase URL List**
| Component | Purchase URL |
| --- | --- |
| Solar Panel (12V, 100W) | www.amazon.com/gp/product/B0DSHPR3KH/ |
| XT60 AC/DC Power Supply (19.5V, 10.3A, 200W) | https://www.amazon.com/gp/product/B08L39D2NY/ |
| PWM Charge Controller (20A, 12/24V) | https://www.amazon.com/Controller-Monitoring-Regulator-Lead-Acid-Protections/dp/B0FN7Q2X3L |
| LiFePO4 Battery (22Ah, 12V) | www.amazon.com/gp/product/B0F1FRBMG3/ |
| MC4 to XT60 FEMALE Adapter | www.amazon.com/MENTBERY-Connector-Extension-Charging-Cable/dp/B0DPZRXLYN/ |
| 12 AWG Black/Red Wire | www.amazon.com/gp/product/B0D12VYLGV/ |
| 10 Pair XT60H Bullet Connectors | https://www.amazon.com/gp/product/B07Q2SJSZ1/ |
| 2Pack 16AWG Barrel Jack Connectors | https://www.amazon.com/gp/product/B0BLYMVWNP/ |
| 4 Pack 12AWG Inline Fuse Holder w/ Fuses | https://www.amazon.com/Anyongora-Inline-Waterproof-Automotive-Standard/dp/B0CL7MLY6T/ |
| XT60 to O ring Connector | https://www.amazon.com/ELFCULB-Terminal-Connector-Battery-Portable/dp/B0C9DDVM8P/ |
| USBC Power Connector | https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/UJC-HP2-3-SMT-TR/21555847 |
| Barrel Jack | https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-063AH/2161208 |
| 22uF Electrolytic Capacitor | https://www.digikey.com/en/products/detail/nic-components-corp/NACE220M35V6-3X5-5TR13F/2232043 |
| 10uF Ceramic Capacitor | https://www.digikey.com/en/products/detail/tdk-corporation/C2012X7S1E106K125AC/9991385 |
| 0.1uF Ceramic Capacitor | https://www.digikey.com/en/products/detail/kyocera-avx/KGM21NR71H104KT/563505 |
| 2.2nF Ceramic Capacitor | https://www.digikey.com/en/products/detail/murata-electronics/GRM155R71H222KA01D/587945 |
| 22uF Ceramic Capacitor | https://www.digikey.com/en/products/detail/tdk-corporation/C2012X7S1A226M125AC/3951796 |
| 470nF Ceramic Capacitor | https://www.digikey.com/en/products/detail/kemet/C0805C474K5RACTU/2212887 |
| 1uF Ceramic Capacitor | https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL21B105KBFNNNE/3886687 |
| Ferrite Bead | https://www.digikey.com/en/products/detail/murata-electronics/BLE18PS080SN1D/13904803 |
| 2.2mH Inductor | https://www.digikey.com/en/products/detail/coilcraft/XGL4030-222MEC/12714567 |
| 4.87kOhm Resistor | https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT4K87/1760656 |
| 25.5kOhm Resistor | https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT25K5/1712905 |
| 5kOhm Resistor | https://www.digikey.com/en/products/detail/vishay-dale/CRCW08055K00JNTA/5075662 |
| 1.2kOhm Resistor | https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT1K20/1760625 |
| 7.15kOhm Resistor | https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT7K15/1713329 |
| 29.8kOhm Resistor | https://www.digikey.com/en/products/detail/koa-speer-electronics-inc/RN73R2ATTD2982B50/10030137 |
| 5.1kOhm Resistor | https://www.digikey.com/en/products/detail/yageo/RC0805JR-075K1L/728338 |
| 270Ohm Resistor | https://www.digikey.com/en/products/detail/yageo/RC0805JR-07270RL/728291 |
| 620Ohm Resistor | https://www.digikey.com/en/products/detail/yageo/RC0805FR-07620RL/728083 |
| Shotkey Diode | https://www.digikey.com/en/products/detail/onsemi/SS32/1052379 |
| TVS Diode USBC | https://www.digikey.com/en/products/detail/littelfuse-inc/SMBJ15A/285980 |
| TVS Diode BARREL JACK | https://www.digikey.com/en/products/detail/littelfuse-inc/SMBJ15CA/285982 |
| Indicator LED | https://www.digikey.com/en/products/detail/kingbright/AP3216EC/25807552 |
| (USBC) PTC RESET FUSE 24V 3A Hold, 5A Trip | https://www.digikey.com/en/products/detail/yageo/smd2920b300tf-15/15212946 |
| (BARREL JACK) PTC RESET FUSE 15V 1.5A Hold, 3A Trip | https://www.digikey.com/en/products/detail/bel-fuse-inc/0ZCG0150BF2C/4156109 |
| Buck Converter | https://www.digikey.com/en/products/detail/texas-instruments/TPS62913RPUR/14004311 |
| Power MUX | https://www.digikey.com/en/products/detail/texas-instruments/TPS2121RUXR/9859001 |

As discussed in Team 5’s conceptual design, the allocated budget for the power subsystem was a total of $260. This price point did not include components needed for the PCB and was originally going to be a part of the PCB interconnections subsystem. However, after careful consideration, Team 6 has decided to incorporate these components into the Power subsystem, since this document goes into detail about the choice of components. 

Team 6 also realized that the need for a LiFePO4 battery is needed for our design, since energy efficiency, charge rate, and weight-to-energy-storage ratio are essential variables to choosing a battery. This also required us to get a larger battery than we originally planned to implement, since we originally did not account for energy storage headroom to not discharge the battery fully. This decision finally snowballed into needing to purchase a more capable power supply than originally intended for which increased the cost. Team 6 also does not account for sales taxation when budgeting all components. 

Therefore, the total price for ALL COMPONENTS is estimated to be $316.83. This puts this subsystem over budget by $54.87. Analyzing this price point, by eliminating the optional solar panel and adapter, this would put this subsystem within Team 6’s allocated budget. 

## Analysis of Solution
**Energy Storage**: The energy storage component has been chosen to be a nominal 12.8V LiFePO₄ pack with 22Ah capacity, providing roughly 240Wh capacity and > 4,000 charge cycles. The reasoning behind the choice of a lithium-based battery chemistry is the following. 

1.  High cycle life providing an average of 3,000+ deep cycles
    

2.  Stable voltage plateau around 12.8–13.2 V, which is ideal for 12 V-class DC/DC converters

   
4.  Provides energy for an estimated runtime of 27.65 hours assuming nominal load
    

5.  Inherently safer behavior and better thermal stability than other lithium chemistries, which aligns with IEEE/IEC safety considerations discussed in the conceptual design.
    

LiFePO₄ chemistry provides better cycle life capacity than other battery chemistries, such as lead acid. It also provides a great energy-to-weight ratio, which is ideal for a portable device solution. Phosphate-based chemistry does make this choice worse than Lithium-Ion or LiPo-based batteries. However, it is less prone to dangerous reactions in the event of electrical failure. Since this system will run for prolonged periods of time unattended, this is an important consideration when choosing between battery chemistries. 

Charge Controller: As discussed earlier in this document, all current flowing into or out of the battery is routed through an acceptable 20A 12V PWM charge controller. This device supports LiFePO₄, lithium chemistries, uses a three-stage PWM charging algorithm, and accepts solar inputs while managing a 20A maximum battery charge and load current. Below is an overview of the charge controller's functionality. 
1.  Regulates current to and from the battery based on measured battery conditions
    

2.  Switches between Bulk / absorption / float stages tailored to LiFePO₄ charge voltages
    

3.  Detects system voltage automatically and constant monitoring of charge and load currents
    

4.  Provides integrated protections such as over-voltage, over-current, short-circuit, reverse connection, and reverse current blocking
    

By interposing this controller between both charging sources and the battery, the subsystem enforces the constraint that all current flow to and from the energy storage solution shall be regulated. It also aligns with conceptual-design guidance that a LiFePO₄-based system must incorporate a dedicated charge controller to meet IEEE/IEC safety practices. Providing integrated fault protections, this device satisfies applicable constraints.

**DC Power Supply (AC Adapter)**: The AC-to-DC power supply serves as the primary charging option for the subsystem, enabling users to recharge the LiFePO₄ battery in situations where solar availability is limited or when fast turnaround is needed. By converting 120VAC mains into a regulated 19.5V DC output, the adapter provides an electrical input that behaves similarly to a fixed-voltage 12V-class solar panel when connected to the PWM charge controller. The adapter remains a power source only, the charge controller continues to regulate all charging behavior. This ensures full compatibility with LiFePO₄ charging requirements and maintains compliance with subsystem constraints regarding regulated current flow into the battery.

Below is an overview of how the AC adapter meets functional and safety requirements:

1.  Provides a stable 19.5V DC output within the acceptable PV-input voltage range of the 20A PWM controller
    

2.  Behaves electrically like a fixed-voltage DC source, which PWM controllers are designed to accept without requiring solar-specific I–V curve characteristics
    

3.  Delivers up to ~200W, remaining safely below the charge controller's input power rating
    

4.  Chosen component is designed for pulsed, rapid-load environments (RC battery chargers), making it tolerant of PWM switching behavior
    

5.  Implementation commonly used in industry and laboratory environments as a stand-in for solar panels during testing, system evaluation, or indoor charging scenarios
    

Because a PWM controller regulates charging by rapidly connecting and disconnecting the PV input, it does not rely on the non-linear solar I–V curve that MPPT controllers require. Thus, a constant-voltage adapter is fully compatible as long as it remains within PV-input specifications. The charge controller continues to manage bulk, absorption, and float stages according to LiFePO₄ requirements, while the adapter simply provides the DC energy needed. 

Safety concerns are mitigated through several layers of protection. The charge controller includes PV-side and battery-side protections such as reverse-polarity, over-voltage, over-current, and short-circuit safeguarding. The LiFePO₄ battery’s integrated BMS provides cell-level protections including over-charge, over-discharge, over-current, and thermal limits. At the system level, additional fusing protects both the adapter path and battery path. Together, these measures ensure that no unregulated or unsafe current path exists from the AC mains to the battery. 

Finally, the adapter’s XT60 output integrates cleanly into the subsystem’s modular design. The XT60 interface allows users to easily swap between solar input, the AC adapter, or laboratory bench supplies without modifying internal electronics. With its 19.5V, 10.3A output, the adapter can recharge the system rapidly, typically within 1.5–2 hours, while fully aligning with all design constraints for safe, efficient battery charging. 

**Solar Panel**:  The chosen panel construction also offers advantages over competing low-cost alternatives. The monocrystalline N-type cells and multi-bus-bar structure used in this model are typically associated with higher conversion efficiencies and improved shade tolerance compared to older polycrystalline or 5-bus-bar panels. This improves energy yield per unit area and enhances real-world performance when irradiance is variable in conditions that directly affect GNSS measurements. The panel’s physical design, including a tempered-glass front and aluminum frame, aligns with outdoor durability expectations while remaining light enough to be carried, mounted, or stowed easily. It also uses standard MC4 connectors, which simplifies integration with the rest of the power subsystem and supports modular field setup with extension cables, folding configurations, or parallel/series arrangements for future scalability.

A more exotic panel such as flexible copper-indium-gallium selenide structures, foldable camping panels, or bifacial glass modules could increase cost or complexity without delivering proportional benefit to the system’s energy budget. The chosen monocrystalline panel has a tradeoff giving us high enough power to reliably recharge the system, physically manageable for field deployments, electrically compatible with the selected controller and battery, robust enough for repeated use, and economically appropriate for both academia and future replication outside the lab environment.

Because this component is a functional option of Team 6’s design, this component has been placed as least priority, since the core operation of this subsystem can still function without this component. AC wall charging is also more convenient than Solar charging and therefore will be implemented first in the case that team 6 is unable to implement this component.

**PCB Implementation**: The PCB power stage successfully implements the project’s requirements by providing clean, protected, and modular low-voltage power distribution. The design meets all electrical specifications by delivering regulated 5 V and 3.3 V rails within ±5% tolerance and maintaining ripple well below the <50 mVpp constraint using low-noise buck converters and appropriate LC filtering. Each rail is sized with a comfortable current margin, exceeding the required continuous and peak loads for all implemented devices.

The PCB also satisfies protection requirements through layered safeguarding: polyfuses, TVS diodes, and Schottky rectification at the input; current-limited power multiplexing; and the inherent protections within the voltage regulators. This ensures compliance with constraints calling for safe operation, prevention of reverse-polarity faults, and adherence to IEEE/IEC-aligned practices  mentioned in the conceptual design. Modularity constraints are equally fulfilled through the TPS2121 power MUX, which enables seamless source selection between USB-C and battery-derived 5 V, supporting a transparent and user-friendly operating model.

Overall, the PCB implementation provides stable, low-noise, fault-tolerant power routing that satisfies the subsystem’s performance, safety, and modularity constraints without unnecessary complexity.

**High Level Solution**: At the broader system level, the power architecture meets all functional requirements for runtime, flexibility, and safe battery management. The selected LiFePO₄ pack provides ≥235 Wh of usable energy, exceeding the 15-hour operational requirement under the nominal 8W load and still meeting conservative expectations under peak demand. All charging and discharging activity is routed through the 20 A PWM charge controller, satisfying the constraint that all battery current must be regulated and that lithium chemistries must use a dedicated management device.

The AC adapter and solar input both fall within the controller’s defined PV voltage and power limits, fulfilling the requirement for multiple charging pathways while maintaining electrical equivalence and system safety. The battery’s internal BMS, the charge controller’s protections, and external PCB-level fusing ensure that no unprotected fault path exists from any source to the battery or low-voltage electronics. This directly satisfies the constraints concerning over-current protection, reverse-polarity protection, and safe fault handling.

From an integration standpoint, the system delivers stable and ripple-controlled power to all critical loads, maintains compatibility with RF-sensitive GNSS hardware, and aligns with the project’s modularity goals through swappable charging solutions and universal connector standards (USB-C, XT60, barrel). All components operate well within their rated electrical and thermal limits, demonstrating that the design not only satisfies the constraints on paper but is robust and reliable for field deployment.

## References
[1]  J. Gómez Socola and F. S. Rodrigues, “ScintPi 2.0 and 3.0: low-cost GNSS-based monitors of ionospheric scintillation and total electron content,” Earth, Planets and Space, vol. 74, art. no. 185, Dec. 2022. [Online]. Available: [https://earth-planets-space.springeropen.com/articles/10.1186/s40623-022-01743-x](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-022-01743-x). Accessed: Sep. 23, 2025.

[2]  Pidora.ca, “Raspberry Pi 4 Power Drain: Real Numbers and Smart Solutions.” Pidora, 2020. [Online]. Available: https://pidora.ca/raspberry-pi-4-power-drain-real-numbers-and-smart-solutions. Accessed: Nov. 20, 2025.

[3]  Raspberry Pi Ltd., Raspberry Pi Pico Datasheet, 2023. [Online]. Available: https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf. Accessed: Nov. 20, 2025.

[4]  u-blox AG, “NEO-F9P-15B Data Sheet (UBX-22021920),” 2022. [Online]. Available: /mnt/data/NEO-F9P-15B_DataSheet_UBX-22021920.pdf. Accessed: Nov. 24, 2025.

[5]  STMicroelectronics, LIS3MDL: Ultra-low-power High-Performance Magnetometer, 2015. [Online]. Available: https://docs.rs-online.com/1eae/0900766b815d5ab0.pdf. Accessed: Feb. 5, 2025.

[6]  TnTech ECE, “Team 6 Space Weather Station – Conceptual Design,” GitHub Repository, 2024. [Online]. Available: https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/main/Reports/Conceptual_Design.md. Accessed: Nov. 20, 2025.

[7]  ZapLitho, “LiFePO4 12V 20Ah Lithium Battery,” Amazon Product Listing, 2024. [Online]. Available: https://www.amazon.com/ZapLitho-LiFePO4-Lithium-Lightweight-Phosphate/dp/B0F1FRBMG3. Accessed: Nov. 20, 2025.

[8]  IEC, “IEC 62133-2:2021 – Secondary cells and batteries containing alkaline or other non-acid electrolytes – Safety requirements for portable sealed secondary lithium cells, and for batteries made from them, for use in portable applications,” International Electrotechnical Commission, 2021. [Online]. Available: [https://webstore.iec.ch/en/publication/32662](https://webstore.iec.ch/en/publication/32662). Accessed: Nov. 20, 2025.

[9]  IEEE Std 1657-2018, IEEE Recommended Practice for Personnel Qualifications for Installation and Maintenance of Stationary Batteries and Battery Systems, IEEE Standards Association, 2018. Accessed: Nov. 20, 2025.

[10]  IEC 62509:2010, Battery charge controllers for photovoltaic systems – Performance and safety requirements, IEC, 2010. Accessed: Nov. 20, 2025.

[11]  IEC 60529:2021, Degrees of protection provided by enclosures (IP Code), International Electrotechnical Commission, Geneva, 2021. [Online]. Available: [https://webstore.iec.ch/en/publication/32662](https://webstore.iec.ch/en/publication/32662). Accessed: Nov. 20, 2025.

[12]  Manuals+, “20A PWM Solar Charge Controller User Manual,” 2024. [Online]. Available: https://manuals.plus/m/dd7b8737fb967b4d5fe32fc89edac28ab765d71de89fff2da27e3c64563a618b. Accessed: Nov. 20, 2025.


[13]  TnTech ECE, “F25 _Team6_SpaceWeatherStation – System Interconnections Subsystem Detailed Design,” GitHub Repository, 2025. [Online]. Available: [https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/Bender_Detailed_Design/Reports/System%20Interconnections%20Subsystem%20Detailed%20Design.md](https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/Bender_Detailed_Design/Reports/System%20Interconnections%20Subsystem%20Detailed%20Design.md). Accessed: Nov. 24, 2025.

[14]  Supulse, “19.5V XT60 Power Adapter,” Amazon Product Listing, 2024. [Online]. Available: https://www.amazon.com/gp/product/B08L39D2NY. Accessed: Nov. 20, 2025.

[15]  Rvpozwer, “18BB 100 W Solar Panel, N-Type 12 V Module,” Amazon Product Listing, 2025. [Online]. Available: [https://www.amazon.com/Rvpozwer-Efficiency-Monocrystalline-Modules-Off-Grid/dp/B0DSHPR3KH](https://www.amazon.com/Rvpozwer-Efficiency-Monocrystalline-Modules-Off-Grid/dp/B0DSHPR3KH?utm_source=chatgpt.com). Accessed: Nov. 24, 2025.

[16]  Same Sky Devices, “PJ-063AH 5.5×2.1 mm DC Power Jack,” Official Datasheet, 2021. [Online]. Available: https://www.sameskydevices.com/product/resource/pj-063ah.pdf.Accessed: Nov. 20, 2025.

[17]  Same Sky (CUI Devices), “UJC-HP2-3-SMT-TR USB Type-C Receptacle,” Digi-Key Product Page, 2024. [Online]. Available: https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/UJC-HP2-3-SMT-TR/21555847. Accessed: Nov. 20, 2025.

[18]  Bel Fuse Inc., “0ZCG0150BF2C Resettable Fuse,” Digi-Key, 2023. [Online]. Available: https://www.digikey.com/en/products/detail/bel-fuse-inc/0ZCG0150BF2C/4156109. Accessed: Nov. 20, 2025.

[19]  Littelfuse Inc., “SMBJ15A Transient Voltage Suppression Diode,” Digi-Key, 2023. [Online]. Available: https://www.digikey.com/en/products/detail/littelfuse-inc/SMBJ15A/285980. Accessed: Nov. 20, 2025.

[20]  onsemi, “SS32 Schottky Rectifier,” Digi-Key, 2023. [Online]. Available: https://www.digikey.com/en/products/detail/onsemi/SS32/1052379. Accessed: Nov. 20, 2025.

[21]  Texas Instruments, TPS62913 2A Low-Noise Buck Converter Datasheet, 2023. [Online]. Available: https://www.ti.com/lit/ds/symlink/tps62913.pdf. Accessed: Nov. 20, 2025.

[22]  Texas Instruments, TPS2121 4.5A Power Multiplexer Datasheet, 2020. [Online]. Available: https://www.ti.com/lit/ds/symlink/tps2121.pdf. Accessed: Nov. 20, 2025.


# **RF Module and Antenna Subsystem Detailed Design**

## **Function of the Subsystem**

The overall function of the Antenna and RF Module Subsystem is to use GNSS signals to compute Total Electron Content (TEC) measurements in the atmosphere. The calculated values and other recorded data are to then be sent to the Data Storage System to be further processed and stored. This subsystem shall meet several constraints given in the following section and shall align with the Conceptual Design description.

## **Specifications and Constraints**

The following is a list of constraints applicable to this subsystem. The proposed solution shall meet or exceed these requirements.

- The subsystem shall use L1 and L5 GNSS signals to compute the TEC measurements, as requested by the customer.
- The subsystem shall measure the pseudorange and carrier phase of the L1 and L5 signals from valid GNSS satellites, as well as the satellite's azimuth angle, as they are used to compute the TEC measurements along the signal path between the receiver and the transmitting satellite \[1\].
- The subsystem shall compute the TEC measurement from the above data on the Single Board Computer (SBC), a main component of the Data and Storage Subsystem.
- The computed TEC measurements shall fall within 15% of credible reference TEC data.
- The subsystem shall record identifying information of each connected satellite and transfer that data along with the computed TEC measurement to the Data and Storage Subsystem.
- The subsystem shall comply with FCC Part 15 Class B (or applicable international equivalent) to ensure that it does not emit harmful RF interference, adhering to regulatory and ethical requirements for protecting GNSS spectrum and public safety \[2\].
- The subsystem shall remain under the \$375 budget limit.

## **Overview of Proposed Solution**

The proposed solution for this subsystem is to use a GNSS RF module with a dual-tuned patch antenna that can receive L1/L5 GNSS signals, extract the needed signal data, and transfer the data to the SBC of the Data and Storage Subsystem. The SBC will then compute the TEC computations, which will be stored by the Data and Storage Subsystem along with other satellite identification data.

<p align="center"><img width="609" height="790" alt="image" src="https://github.com/user-attachments/assets/2b1621a9-241f-4d85-83bc-46f6d212090b" /></p>

<p align="center"><b>Figure 1:</b> <i>Antenna and RF Module Hardware Diagram</i></p>

## **TEC Computation Method**

For more information on what TEC is and the physics behind it, refer to the Project Proposal Document.

Before TEC computation can be discussed, it is necessary to define what a signal's pseudorange is, as it is used in determining TEC. A signal's pseudorange, P, is the estimated distance between a transmitter and receiver, computed by multiplying the difference of the received and sent timestamps of the transmitted signal by the speed of light, c. \[3\].

<p align="center">$$P = c(t_s-t_r)$$ (1)</p>

This value is an estimation of distance because it contains an added time delay. This time delay is caused by the electrons along the signal's path (TEC), as well as instrumental noise and time delay. Compared to the time delay caused by the TEC along the path, the instrumental time delay is negligible, so the added time delay of the pseudorange can be estimated as being completely caused by the TEC \[3\].

The difference between two signals' pseudoranges along the same path can be rewritten as the following formula. The distance traveled by each signal cancels, leaving only the TEC delay components \[3\].

<p align="center">$$P_1-P_2=40.3\frac{TEC_p}{f_1^2}-40.3\frac{TEC_p}{f_2^2}$$ (2)</p>

In the above formula, each frequency and pseudorange pair correspond to a signal that travels along the same path between the transmitter and receiver. The above equation can be rewritten as follows, solving for the TEC along the path between the transmitter and receiver \[3\]:

<p align="center">$$TEC_p=\frac{1}{40.3}(\frac{f_1^2f_2^2}{f_2^2-f_1^2})(P_1-P_2)$$ (3)</p>

Equation 3 clearly shows that if the pseudorange and frequency of two separate signals transmitted across the same path are known, then the straight-line TEC for that path can be calculated. This TEC value is referred to as the slant TEC, because it is the TEC value of the "slanted" beam path of the signal through the atmosphere from the satellite to the receiver. \[3\].

## **Alternative TEC Computation Method and Noise Reduction**

Alternatively, the carrier phase of the signal can be used to compute TEC as well. Carrier phase provides more accurate measurements than pseudorange measurements. However, carrier phase measurements are ambiguous in nature, as the initial number of cycles between the transmitter and receiver is unknown. As such, TEC measurements are often processed using a least-squares model to match the smooth, ambiguous carrier phase measurements to the relatively noisy, clear pseudorange measurements. This arrives at a set of very accurate, unambiguous TEC values \[4\]. 

The primary method of TEC computation this system will use is the pseudorange computation, as this measurement method can be done with each measurement frame quickly without the ambiguity of carrier phase measurements. Pseudorange measurements may be relatively noisy, but the resulting values are reasonable. However, carrier phase measurements will still be collected to allow for the user to refine the stored data from the measurement device later. As a stretch goal, the designed device may include a post-processing function to take a set of collected pseudorange TEC data and apply carrier phase measurements as described to arrive at a smoother set of refined TEC data.

Applying these principles, it is necessary to select an RF module that can determine the pseudoranges for two separate signal frequencies transmitted from GNSS satellites, as well as their carrier phase. The constraints of this subsystem, as discussed in the above section, require the module to receive the L1 and L5 GNSS frequencies specifically. Additionally, to record the location of the path of each TEC measurement, the module will need to be able to determine the position of the receiver, as well as the position of any measured satellites.

The RF module that has been selected to meet these constraints is the SparkFun GNSS-RTK L1/L5 NEO-F9P Breakout Board. This module contains a u-blox NEO-F9P chip, which is an L1/L5 GNSS receiver which boasts centimeter level accuracy, capable of connecting to four concurrent GNSS systems \[5\]. This module can easily measure the pseudorange and carrier phase of received GNSS signals, as well as determine satellite identification and positional data, making it ideal for gathering information for TEC measurements \[6\]. This module has configurable interfaces for UART, SPI, and I2C connections, allowing it to easily connect and communicate with a chosen SBC of the data storage system \[7\].

<p align="center"><img width="513" height="513" alt="image" src="https://github.com/user-attachments/assets/598f23a6-2dcf-45af-9a3e-f2c93a63ec00" /></p>

<p align="center"><b>Figure 2:</b> <i>SparkFun GNSS-RTK L1/L5 Breakout NEO-F9P</i></p>

The antenna that has been selected for this subsystem is the u-blox ANN-MB1 L1/L5 multi-band high precision GNSS antenna. This antenna is tuned to the L1 and L5 GNSS frequencies, allowing the subsystem to receive both signals concurrently. It is also a patch antenna, which allows for affordability and quality of the signal. This antenna is also fully compatible with the NEO-F9P module, making it ideal for this solution \[8\].

<p align="center"><img width="386" height="386" alt="image" src="https://github.com/user-attachments/assets/20c46f6a-b1c6-44c3-b6f9-4ba43f5d1ac8" /></p>

<p align="center"><b>Figure 3:</b> <i>ANN-MB1 u-blox antenna</i></p>

## **Interface with Other Subsystems**

The RF Module and Antenna Subsystem shall connect to the Power subsystem and the Data and Storage Subsystem via the System Interconnections Subsystem, all whilst being housed within the Enclosure Subsystem. Below is a diagram of the connections between the hardware of the RF Module and Antenna Subsystem and the other subsystems.

<p align="center"><img width="814" height="461" alt="image" src="https://github.com/user-attachments/assets/9617886f-bf1c-4fb9-8164-4aa8d777ea70" /></p>

<p align="center"><b>Figure 4:</b> <i>Subsystem Connections</i></p>

All the connections between the subsystems of this project run through the System Interconnections Subsystem via a central PCB. The signals that shall connect the RF Module and Antenna Subsystem to the rest of the project and the nature of the data contained within are given below.

### **UART Serial Connection**

The RF Module of the RF Module and Antenna Subsystem shall connect to the Data and Storage Subsystem's SBC with a serial UART connection. This connection shall be used to transmit the pseudorange, carrier phase, and other GNSS positional data from the NEO-F9P module to the SBC. Additionally, the SBC shall send commands to the NEO-F9P module through this same connection.

For the UART connection to work properly, both devices must have their baud rates set to within 10% of each other \[9\]. The NEO-F9P documentation recommends the baud rate for the module to be set not less than 38400 baud and no larger than 921600 baud \[6\]. Therefore, the selected baud rate for the connection shall be between these values.

**UART Serial Connection: UBX Protocol**

The NEO-F9P uses the UBX protocol to communicate with host computers. This is a proprietary protocol designed by u-blox, the manufacturers of the NEO-F9P. This protocol sends frames consisting of two sync characters, a message class, a message ID, the length of the payload, the said payload, and a checksum. Each frame is formatted as in the following diagram from the NEO-F9P documentation \[6\]:


<p align="center"><img width="975" height="390" alt="image" src="https://github.com/user-attachments/assets/bfc7fb8f-c5e6-4259-98ff-62d34aba22e1" /></p>

<p align="center"><b>Figure 5:</b> <i>UBX Frame Structure</i></p>

The first section of the frame, the preamble, consists of two synch characters. These signify the beginning of the frame. The next segment, the message class and ID, signify what kind of message is contained in the frame. The message class identifies what group of messages the contained payload aligns with. The message ID defines what specific message is in the payload. Finally, the frame ends with a checksum, which is used to verify that the received data is valid \[6\].

The messages that can be sent over the UBX protocol range in function, from configuration commands to information transmission requests \[6\]. Messages of this protocol shall be sent between the NEO-F9P and the SBC through the UART connection to configure the NEO-F9P and to transmit required data to the SBC for TEC computation.

### **GPIO Control Pins**

The NEO-F9P's control pins shall also be connected to some of the Data and Storage Subsystem's SBC GPIO pins to allow for more control over the NEO-F9P by the project. The only control pin that will be connected to the SBC is the RESET pin. This pin will trigger a cold start if held low for at least 100ms \[7\].

### **Power Signal**

The NEO-F9P module shall be powered by a 5V connection provided by the Power System. The NEO-F9P board supplies the attached active antenna with power when supplied with a 5V power source, so the antenna will not need a separate power connection.

## **Buildable Schematic**

The buildable schematic of this subsystem can be found in the Detailed Design Specifications of the System Interconnections Subsystem, as the specific PCB connections fall under the envelope of that subsystem.

## **Flowchart**

This subsystem shall have three separate programmed functions to operate within the overall system that can be called by the system when needed. Those functions are the NEO-F9P Initialization Function, the Receiver Location Data Acquisition Function, and the TEC Computation and Satellite Data Acquisition Function. Any of these functions can be called by the system when needed.

The NEO-F9P Initialization Function shall likely only be called on bootup of the device. This function shall send initial configuration commands using the UBX protocol over the UART connection between the SBC and NEO-F9P to set up the NEO-F9P device for operation.

The Receiver Location Data Acquisition Function shall poll the NEO-F9P using the UBX protocol to obtain the locational data of the receiver. This function will likely only be called by the device during initial bootup, as the device is not intended to be moved when it has been set up in a location to measure TEC values.

The TEC Computation and Satellite Data Acquisition Function shall poll the NEO-F9P using the UBX protocol to get the identification, position, signal type, pseudoranges, and carrier phases of all acquired satellites. This data shall then be analyzed by the SBC to determine which satellites have both an L1 and L5 signal. The valid satellites shall then have TEC measurements computed using equation 3, which shall then be passed on to the rest of the system for further analysis and storage. This function shall be called every time the system wishes to make a TEC measurement.

<p align="center"><img width="975" height="726" alt="image" src="https://github.com/user-attachments/assets/a91a7b81-5b9f-43d4-b2ad-c7da7481bfeb" /></p>

<p align="center"><b>Figure 6:</b> <i>Operational Flowchart</i></p>

**Bill of Materials**

A comprehensive list of all expenses required for this subsystem is provided below. The total cost is $53.34 less than the allocated $375 budget. Note that the cost of any connective wires for this subsystem is covered by the System Interconnections Subsystem.

| Component | SparkFun GNSS-RTK L1/L5 Breakout - NEO-F9P (Qwiic) | ANN-MB1 L1/L5 Multi-Band GNSS Antenna |
| --- | --- | --- |
| Manufacturer | SparkFun Electronics | u-blox |
| Part # | GPS-23288 | ANN-MB1-00 |
| Distributor | SparkFun Electronics | DigiKey |
| Dist. Part # | GPS-23288 | 672-ANN-MB1-00-ND |
| Quantity | x1  | x1  |
| Price | \$259.95 | \$61.71 |
| URL | <https://www.sparkfun.com/sparkfun-gnss-rtk-l1-l5-breakout-neo-f9p-qwiic.html?gad_source=1&gad_campaignid=17479024039&gclid=Cj0KCQiAoZDJBhC0ARIsAERP-F_VOQB7xlmAha4Z4P-1NanVYHGOM7iVvMnycKp83FkyJxqAhj6OTCcaAqU6EALw_wcB> | <https://www.digikey.com/en/products/detail/u-blox-america-inc/ANN-MB1-00/14835875?curr=usd&utm_campaign=buynow&utm_medium=aggregator&utm_source=octopart> |
| Total Cost: |     | \$321.66 |

<p align="center"><b>Table 1:</b> <i>Bill of Materials</i></p>

## **Analysis**

The RF Module and Antenna Subsystem's function is to acquire GNSS signals and compute Total Electron Content (TEC) measurements of the ionosphere. The subsystem must meet functional requirements and operate within defined constraints, including measurement accuracy, signal compatibility for L1/L5 GNSS frequency bands, and a budget ceiling of \$375. The following analysis will show the proposed solution and its components meet the subsystem's objectives.

### **Functional Requirements**

The subsystem must:

1. Receive L1 and L5 GNSS signals
2. Measure pseudorange and carrier phase for L1 and L5 signals
3. Record satellite identification and position
4. Compute TEC accurately using the received signal data
5. Transfer computed TEC and associated data to the Data and Storage Subsystem
6. Comply with FCC Part 15 Class B (Or an international equivalent) to ensure that it does not emit harmful RF interference
7. Operate within a budget of \$375

Requirements 1, 2, 3, 5, and 7 are satisfied by the chosen RF module and antenna. They can receive L1 and L5 signals, measure pseudorange and carrier phase, and record satellite positional and identification data. The UART interface supported by the RF module, as well as the UBX protocol, allow for fast and easy communication of the required data to the SBC. As shown in the BOM section of this document, these components are also well within the budget.

Requirement 6 is not expressly covered by the NEO-F9P module, as it is designed with European standards in mind. However, its documentation lists it as compliant with the Radio Equipment Directive (RED) 2014/53/EU \[11\]. This European directive requires radio equipment to effectively use the RF spectrum without producing harmful interference, which would imply that the NEO-F9P does not produce harmful radio interference, thus fulfilling requirement 6 \[12\].

Requirement 4 is satisfied by the methodology described in the TEC Computation Method subsection of this document, as well as the operational flow description in Flow section of this document. The proposed TEC computation in equation 3 is easily performed with the pseudorange data measured by the RF module, and the associated satellite data is easily received by the Data and Storage Subsystem along with the TEC computation.

| Constraint | Design Fulfillment | Evidence / Justification |
| --- | --- | --- |
| Use of L1/L5 signals | ANN-MB1 antenna + NEO-F9P supports both L1 and L5 frequencies | NEO-F9P datasheet confirms dual-frequency GNSS reception \[5\]; ANN-MB1 is tuned for L1/L5 \[8\] |
| Measure pseudorange & carrier phase | NEO-F9P provides both measurements for all visible satellites | Verified in NEO-F9P Interface Description and Integration Manual \[7\] |
| Compute TEC on SBC | Subsystem sends raw pseudorange & phase data to SBC | Data transfer via UART ensures SBC receives all required inputs |
| Record satellite ID & positional data | NEO-F9P outputs satellite ID, elevation, and azimuth | UBX messages include this data; operational flow captures this before TEC computation |
| Budget ≤ \$375 | NEO-F9P \$259.95 + ANN-MB1 \$60 = \$319.95 | Total cost is \$55.05 below budget limit |

<p align="center"><b>Table 2:</b> <i>Design Analysis with respect to Constraints</i></p>

The proposed Antenna and RF Module Subsystem design fully meets the functional requirements and constraints. Therefore, the proposed design is highly likely to accomplish its intended function within the overall system.

## **References**

\[1\] M. A. S. R. A. Zaini, "Determination of Ionospheric Total Electron Content (TEC): Phase Measurement Based on Levelling Technique," Faculty of Electrical Engineering, Universiti Teknologi MARA, Shah Alam, Selangor, Malaysia. \[Online\]. Available: <https://ir.uitm.edu.my/id/eprint/40459/1/40459.pdf>. \[Accessed: Dec. 2, 2025\].

\[2\] Federal Communications Commission. _Title 47, Code of Federal Regulations, Part 15 - Radio Frequency Devices, Subpart B: Unintentional Radiators_. Washington, DC: U.S. Government Publishing Office, 54 FR 17714 (Apr. 25, 1989), as amended.

\[3\] E. D. Lopez, R. E. Hidalgo, and M. J. Carrera, "Preliminary mapping of ionospheric total electron content (TEC) over Ecuador using global positioning system (GPS) data," arXiv preprint arXiv:2403.19053, 2024. \[Online\]. Available: <https://arxiv.org/abs/2403.19053>. \[Accessed: Dec. 2, 2025\].

\[4\] L. Dyrud, A. Jovancevic, A. Brown, D. Wilson, and S. Ganguly, “Ionospheric measurement with GPS: Receiver techniques and methods,” Radio Science, vol. 43, no. 6, p. n/a-n/a, Nov. 2008. \[Online\]. Available:  <https://doi.org/10.1029/2007rs003770>. \[Accessed: Feb. 8, 2026\].

\[5\] u-blox AG, "NEO-F9P Product Summary," UBX-21043595-R05. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P//assets/component_documentation/NEO-F9P_ProductSummary_UBX-21043595.pdf>. \[Accessed: Dec. 2, 2025\].

\[6\] u-blox AG, "u-blox F9 HPG L1L5 1.40 - Interface Description," Interface Description UBX-23006991-R02. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P/assets/component_documentation/u-blox-F9-HPG-L1L5-1.40_InterfaceDescription_UBX-23006991.pdf>. \[Accessed: Dec. 2, 2025\].

\[7\] u-blox AG, "NEO-F9P - High Precision GNSS Module: Integration Manual," Document UBX-22028362-R03. \[Online\]. Available: <https://docs.sparkfun.com/SparkFun_u-blox_NEO-F9P/assets/component_documentation/NEO-F9P_IntegrationManual_UBX-22028362.pdf>. \[Accessed: Dec. 2, 2025\].

\[8\] u‑blox AG, "ANN‑MB1: L1/L5 Multi‑band High Precision GNSS Antenna - Data sheet," Document UBX‑21005551-R04. \[Online\]. Available: <https://content.u-blox.com/sites/default/files/ANN-MB1_DataSheet_UBX-21005551.pdf>. Accessed: Dec. 2, 2025.

\[9\] "Basics of UART Communication," CircuitBasics. \[Online\]. Available: <https://www.circuitbasics.com/basics-uart-communication/>. \[Accessed Dec. 2, 2025\].

\[10\] OpenAI, "ChatGPT (GPT-5-mini) \[Large language model\]," OpenAI, San Francisco, CA, USA, Dec. 2, 2025. \[Online\]. Available: <https://chat.openai.com/>. \[Accessed Dec. 2, 2025\].

\[11\] u-blox AG, "NEO-F9 - Declaration of Conformity," UBX-23004247-R02. \[Online\]. Available: <https://content.u-blox.com/sites/default/files/documents/NEO-F9-EU-RED_Conformity_UBX-23004247.pdf>. \[Accessed Feb. 8, 2026\].

\[12\] “Directive 2014/53/EU of the European Parliament and of the Council of 16 April 2014 on the harmonisation of the laws of the Member States relating to the making available on the market of radio equipment and repealing Directive 1999/5/EC Text with EEA relevance,” May 22, 2014. <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0053>


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

### **1.0mm JST Connector Specification**

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

### **Substrate Material**

&nbsp; &nbsp; &nbsp; &nbsp;It is essential when designing a PCB to first consider the speed of the signals on the board, as signal frequency strongly influences material selection and stackup. For the Personal Space Weather System, the highest-frequency signals present on the PCB will be SPI communications, which typically operate in the tens of megahertz. FR-4 is an industry standard PCB material that has been used for decades due to its good balance of electrical, mechanical, and thermal properties at a relatively low cost. Importantly, FR-4 performs reliably for frequencies from DC through the low-GHz range \[5\], making it well suited for the signal speeds in this design. Therefore, FR-4 is selected as the substrate material for the PCB.

### **Stackup**

&nbsp; &nbsp; &nbsp; &nbsp;Due to the complexity of connections being made between various modules in the prototype, a 4-layer board has been selected. The additional layers allow dense routing without signal congestion, provide uninterrupted ground and power planes, and improve the electrical performance and reliability of the interconnecting traces. A 4-layer configuration balances performance, cost, and space efficiency, making it ideal for applications that require moderate-to-high complexity, excellent signal integrity, and reliable power delivery \[6\].

&nbsp; &nbsp; &nbsp; &nbsp;The subsystem implements a 90x95mm, 1.6mm thick, 4-layer FR-4 PCB with the following stackup:

- Top Layer: Signal Layer
  - Includes all components and connection points for power, debugging, and interfacing with external modules.
- Second Layer: Ground Plane
  - Filled copper GND zone over the entire layer providing consistent current return paths.
- Third Layer: Power Plane
  - Includes regulated 5V and 3.3V copper zones oriented to simplify power routing on top and bottom layers.
- Bottom Layer: Signal Layer
  - Additional layer to ensure clean routing.

&nbsp; &nbsp; &nbsp; &nbsp;This layer arrangement not only optimizes electrical performance and signal integrity but also respects manufacturability constraints, ensuring that the board can be reliably fabricated and assembled according to the chosen manufacturer's specifications. The 90x95mm dimensions provide a compact form factor that fits the enclosure while allowing sufficient space for component placement, routing, and connector access.

### **Manufacturability Specifications**

&nbsp; &nbsp; &nbsp; &nbsp;Based on the manufacturability and assembly constraints, the proposed PCB has passed KiCad's Design Rules Checker (DRC), which verifies that all board constraints are satisfied. These constraints follow the specifications provided by the manufacturer, PCBWay, including minimum trace width and spacing, via sizes, solder mask clearances, and silkscreen spacing. Adhering to these rules ensures reliable fabrication and reduces the risk of defects.

&nbsp; &nbsp; &nbsp; &nbsp;The following figure specifies the manufacturer's specifications used \[4\]:

<p align="center">
  <img src="https://hackmd.io/_uploads/r145XI7bbg.png" alt="KiCad and PCBWay Constraints" width="600" />
  <br />
  <strong>Figure 1:</strong> KiCad and PCBWay Constraints
</p>


### **Tracing and Vias Constraints**

&nbsp; &nbsp; &nbsp; &nbsp;In addition to meeting the minimum manufacturability specifications, the PCB must be capable of handling the electrical throughput required by the system. All trace widths and via diameters are sized safely to carry the expected maximum continuous currents without overheating. These calculations assume an ambient temperature of 40 °C, a temperature rise of 10 °C, a copper thickness of 1 oz/ft², and a via wall copper thickness of 0.018 mm, as specified by the manufacturer.

&nbsp; &nbsp; &nbsp; &nbsp;The table below summarizes the expected maximum continuous currents along with the corresponding minimum trace widths and via diameters. Calculations were performed using the DigiKey Trace Width Calculator \[7\] and the Best Technology Via Current Calculator \[8\].

| Source | Expected Continuous Maximum Current (A) | Minimum Trace Width (mm) | Minimum Via Diameter (mm) |
| --- | --- | --- | --- |
| 12V Input | 1.6 | 0.57 | 0.35 |
| 5V Input | 3   | 1.37 | 0.84 |
| Data Lines | <0.005 | \*Below constraint | \*Below constraint |

\*This column shows minimum values; using traces and vias rated for more than needed is acceptable.

&nbsp; &nbsp; &nbsp; &nbsp;In many areas of the board, larger traces are intentionally used to act as heatsinks, improving thermal management. This is particularly evident near the full-bridge rectifier, where the traces near diode terminals are 1.2mm. Additionally, filled copper zones are used to distribute current and dissipate heat, such as those surrounding the TPS62913 buck converters. Trace lengths are kept as short as possible to minimize resistance, reduce voltage drops, and maintain clean return paths, enhancing electrical performance and thermal efficiency.

<p align="center">
  <!-- Swapped order: Full Bridge Rectifier on LEFT, Buck Converter on RIGHT -->
  <img src="https://hackmd.io/_uploads/BJim8OMW-g.png" alt="Full Bridge Rectifier" height="250" />
  <img src="https://hackmd.io/_uploads/S12EL_fWWg.png" alt="TPS62913 Buck Converter" height="250" />
  <br />
  <strong>Figure 2:</strong> Full Bridge Rectifier (Left) and TPS62913 Buck Converter (Right)
</p>


&nbsp; &nbsp; &nbsp; &nbsp;By carefully sizing traces and vias to handle the maximum expected currents and optimizing copper fills and trace lengths for both thermal and electrical performance, the PCB ensures reliable power distribution throughout the system. With these constraints met, the next critical step is routing, where signal paths are laid out to connect all modules effectively.

### **Routing**

&nbsp; &nbsp; &nbsp; &nbsp;The strategy for PCB routing is critical to ensure reliable signal transmission, proper power delivery, and modular connectivity between system components. Careful routing minimizes interference between traces and maintains signal integrity. Routing decisions were guided by four primary considerations: signal integrity, power distribution, trace management, and connection site access.

&nbsp; &nbsp; &nbsp; &nbsp;Data signal traces are kept on the top layer wherever possible, with the ground layer positioned between the signal traces and the power plane. This arrangement greatly reduces the likelihood of ground loops. By minimizing ground loop area, this strategy limits unwanted electromagnetic radiation, as a ground loop can otherwise act as an unintended antenna \[9\]. Additionally, the PCB incorporates a ground copper filled zone on the power plane at points where SPI connections cross, providing a low impedance return path and mitigating interference between signals. All ground fills are stitched to the main ground plane using vias, ensuring a continuous low impedance return path. Further reducing electromagnetic interference, routing is designed to combat crosstalk achieved by minimizing data signals crossing junctions on the power plane. Crosstalk occurs where there are rapid voltage and current transitions inducing voltages in adjacent traces due to inductive and capacitive coupling \[9\].

&nbsp; &nbsp; &nbsp; &nbsp;The use of a power plane greatly simplifies power distribution. Instead of routing individual traces for each voltage rail, entire planes are defined as filled copper zones regulated to their respective voltages. These zones are oriented to reduce EMI while spanning the board to deliver power efficiently to all components.

&nbsp; &nbsp; &nbsp; &nbsp;Beyond signal integrity, PCB trace routing is a careful balancing act to ensure all connections reach their intended components and connectors without congestion. The layout must navigate limited space and dense component placement, making design tools like KiCad's DRC particularly valuable. Mindful trace management ensures signals are routed efficiently, with minimal crossings and detours, while maintaining clear access to pads, vias, and connectors throughout the board.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the PCB routing strategy balances performance, power delivery, and accessibility. Careful attention to signal integrity, power distribution, trace management, and connection site access ensures an efficient board with straightforward access to all connection points for testing, debugging, and future expansion. These routing decisions directly satisfy the physical and electrical routing constraint by ensuring signal integrity, minimizing interference, and maintaining organized, electrically sound trace paths.

<p align="center">
  <!-- Swapped order: SPI Signal Crossing on LEFT, Power Plane Routing on RIGHT -->
  <img src="https://hackmd.io/_uploads/rybJ_OzbWx.png" alt="SPI Signal Crossing w/ Ground Zone" height="250" />
  <img src="https://hackmd.io/_uploads/rkTyOuMbZe.png" alt="Power Plane Routing" height="250" />
  <br />
  <strong>Figure 3:</strong> SPI Signal Crossing w/ Ground Zone (Left) and Power Plane Routing (Right)
</p>


### **Power**

&nbsp; &nbsp; &nbsp; &nbsp;The PCB power design provides flexibility for the user by supporting two input sources: one for connection to mains power and another for portable operation via a battery system. This design involved a collaborative effort between the Power Subsystem lead (Kenneth Creamer) and the System Interconnections lead (Jack Bender) to achieve the proposed solution. Collaboration primarily focused on selecting surface-mount components with appropriate power ratings and form factors. The detailed signal path for both inputs is summarized in the Power Subsystem Detailed Design \[10\]. This document provides specifics regarding the PCB and a general overview of the power components used.

&nbsp; &nbsp; &nbsp; &nbsp;The PCB power design includes a thorough analysis of component specifications to properly manage thermal signatures and current ratings.

&nbsp; &nbsp; &nbsp; &nbsp;The wall mains input utilizes a USB-C connector, supporting up to 20VDC and 3A. All traces in this input power path have a width of at least 1.37mm, and via diameters are at least 0.84mm to accommodate the expected current. Critical singular vias in this path, such as the via that feeds the 5V plane from the MUX, are 1mm in diameter to ensure reliable current flow. In component-dense areas, filled copper regions are used to provide a low-resistance conduction path capable of handling the full 3 A.

&nbsp; &nbsp; &nbsp; &nbsp;The battery input uses a barrel jack connector rated for up to 24V and 8A, although the expected maximum current for this system is 1.6A. All traces in this input path have a width of at least 0.57mm, with via diameters of at least 0.35mm to handle the expected current safely. The battery input also incorporates a full-bridge rectifier using four SS32 Schottky diodes. Each diode has a forward voltage drop of approximately 0.5V, resulting in a power dissipation of roughly 0.8W per diode. This level of heat necessitates enlarged copper areas around the diode pads to aid in thermal dissipation.

&nbsp; &nbsp; &nbsp; &nbsp;The TPS2121RUXR voltage multiplexer and TPS62913RPUR buck converter were selected in part because of their compact surface-mount footprints, which optimize board space but necessitate precise soldering techniques. To ensure reliable solder joints, these components require reflow soldering, as hand-soldering is impractical for such small packages. The layout of the TPS62913RPUR closely follows the recommendations provided in the datasheet, including copper filled zones and proper placement of components specified. While both devices are highly efficient, the TPS62913RPUR may have a small thermal signature under continuous high-current operation. Proper copper pours and thermal reliefs are incorporated into the PCB layout to dissipate heat effectively and maintain safe operating temperatures.

<p align="center">
  <img src="https://hackmd.io/_uploads/BJNKuOMWWx.png" alt="Datasheet Recommended TPS62913RPUR Layout" width="600" />
  <br />
  <img src="https://hackmd.io/_uploads/rkkm9uGZZl.png" alt="Detailed Design TPS62913RPUR Layout" width="600" />
  <br />
  <strong>Figure 4:</strong> Datasheet Recommended TPS62913RPUR Layout (Top) and Detailed Design TPS62913RPUR Layout (Bottom)
</p>



&nbsp; &nbsp; &nbsp; &nbsp;Decoupling and bypass capacitors are strategically positioned near both the USB-C and barrel jack input connectors as well as close to the TPS2121RUXR and TPS62913RPUR power pins. This placement helps stabilize the voltage at the entry points and at the devices themselves, minimizing ripple voltage and ensuring clean, reliable power under varying load conditions. Additional passive components for power conditioning are similarly arranged to optimize current paths and reduce localized thermal buildup. Thoughtful positioning of these components contributes to reliable operation and improved thermal performance.

&nbsp; &nbsp; &nbsp; &nbsp;The PCB has two status indicators directly connected to the 5V and 3.3V power rails, providing a visual confirmation of power presence on both supply lines. These LEDs allow users to quickly verify that the respective voltage rails are active and functioning correctly. Their inclusion supports troubleshooting, system validation, and general operational awareness.

&nbsp; &nbsp; &nbsp; &nbsp;Overall, the PCB power design balances flexibility, efficiency, and thermal management. By carefully selecting components, sizing traces and vias, following recommended layouts, and strategically positioning passive elements, the design delivers stable power to the system while maintaining safe operating temperatures and manufacturability.

### **Component Selection and Labeling**

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

### **Cable Selection**

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

### **Power Inputs**  
&nbsp; &nbsp; &nbsp; &nbsp;The PCB includes two primary power input terminals: a USB-C connector and a barrel jack. The USB-C connector is configured to accept up to 5V at 3A, with trace widths and CC pin configurations designed to safely handle this continuous current, as detailed in the Power Subsystem Detailed Design. The barrel jack supports 12V at 1.6A, with trace widths selected to accommodate continuous current without excessive voltage drop or heating.

### **RF Module Interface**  
&nbsp; &nbsp; &nbsp; &nbsp;1mm pitch edge connectors are provided to interface with the RF module, supporting SPI, I2C, and UART communication protocols. These connections handle packets of data relating to Total Electron Content (TEC) and scintillation measurements. Additional pins are included for module state control. These are voltage-sensitive lines that allow the SBC to give or receive simple state information. A dedicated 5V power line and an extra 4-pin connector facilitate powering the module and accessing non-data signals.

### **Raspberry Pi 4B GPIO Ribbon Connection**  
&nbsp; &nbsp; &nbsp; &nbsp;A 40-pin ribbon connector provides complete access to all GPIO pins of the Raspberry Pi 4B, including power and ground. The ribbon uses 26 AWG wire, capable of safely carrying the required current when supplying both 5V pins in parallel. The ribbon is kept as short as possible to minimize voltage drop and reduce signal noise.

### **Peripheral 1 mm Pitch Connectors**  
&nbsp; &nbsp; &nbsp; &nbsp;Several 1 mm pitch edge connectors are included for peripheral modules excluding the RF module:

- LoRa module: interfaces with the MCU via SPI.
- OLED display: interfaces via I2C.
- Magnetometer: interfaces via I2C.
- Additional UART option: allows optional serial communication.

&nbsp; &nbsp; &nbsp; &nbsp;These connectors are positioned close together to reduce routing complexity and improve accessibility while maintaining the board's compact form factor.

### **Analog Inputs**  
&nbsp; &nbsp; &nbsp; &nbsp;Two analog inputs are provided for simple voltage measurements. Each input includes a data line, a 3.3V supply, and a GND line, allowing direct connection to the MCU's ADC pins. Screw terminals are used to enable secure, ferrule-terminated wiring while preserving signal integrity.

### **Raspberry Pi Pico Female Header**  
&nbsp; &nbsp; &nbsp; &nbsp;A female through-hole header maps all 40 pins of the Raspberry Pi Pico MCU to the PCB, providing full input and output access to GPIOs, ADCs, and power rails. This mapping enables flexible interfacing for debugging, prototyping, and expansion.

### **Form Factor and Subsystem Integration**  
&nbsp; &nbsp; &nbsp; &nbsp;The board layout facilitates straightforward placement of connectors and modules while maintaining a compact form factor compatible with the enclosure, including mounting holes designed for M1 screws. Signal assignment and protocol routing have been optimized to support the software subsystems, providing a standardized and modular platform for system development.

# **3D Model of Custom Mechanical Components**
<p align="center">
  <img src="https://hackmd.io/_uploads/rkEFjuzZZl.png" alt="Top View of 3D Rendered PCB" width="600" />
  <br />
  <strong>Figure 5:</strong> Top View of 3D Rendered PCB
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/HJoJ3Oz-Zx.png" alt="Bottom View of 3D Rendered PCB" width="600" />
  <br />
  <strong>Figure 6:</strong> Bottom View of 3D Rendered PCB
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/SJOzh_MW-e.png" alt="Power Input Side View" width="600" />
  <br />
  <strong>Figure 7:</strong> Power input side view of 3D Rendered PCB
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/B1ovhOfbZe.png" alt="Connector Side View" width="600" />
  <br />
  <strong>Figure 8:</strong> Connector side view of 3D Rendered PCB
</p>


# **Buildable Schematic**

&nbsp; &nbsp; &nbsp; &nbsp;All schematics were created in KiCad Schematic Editor. The power portion was designed collaboratively with the Power Subsystem lead. It is essential to include the power schematic within the Interconnections Subsystem documentation because it contains direct references to the PCB silkscreen. In addition to the power schematic, an SBC and MCU header-mapping schematic is provided, which uses bus structures to reduce visual clutter. This schematic also includes two status LEDs, enabling the user to send a signal to verify proper system functionality.

&nbsp; &nbsp; &nbsp; &nbsp;The external connector schematic outlines all access points on the board and details how each pin is powered. The RF connectors include a normally open solder jumper to ensure that only one power source can supply the RF module at a time, preventing potential damage. All pins are clearly identified using net labels, which automatically carry over into the PCB editor and support a streamlined workflow.

<p align="center">
  <img src="https://hackmd.io/_uploads/rJ063_MZZl.png" alt="PCB Power Schematic" width="900" />
  <br />
  <strong>Figure 9:</strong> PCB Power Schematic
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/Sy0TndzW-l.png" alt="SBC and MCU Headers Schematic" width="900" />
  <br />
  <strong>Figure 10:</strong> SBC and MCU Headers Schematic
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/BJCp3uMbWg.png" alt="Edge Connector Schematic" width="900" />
  <br />
  <strong>Figure 11:</strong> Edge Connector Schematic
</p>


# **Printed Circuit Board Layout**
<p align="center">
  <img src="https://hackmd.io/_uploads/Hyel0_MW-l.png" alt="PCB Layout w/ All Layers Visible" width="900" />
  <br />
  <strong>Figure 12:</strong> PCB Layout w/ All Layers Visible
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/Hy9eRdz--e.png" alt="PCB Layout w/ Only Signal Layers Visible" width="900" />
  <br />
  <strong>Figure 13:</strong> PCB Layout w/ Only Signal Layers Visible
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/ByX-0OfZbl.png" alt="PCB Layout w/ Only Ground Layer Visible" width="900" />
  <br />
  <strong>Figure 14:</strong> PCB Layout w/ Only Ground Layer Visible
</p>

<p align="center">
  <img src="https://hackmd.io/_uploads/HyjzRuG-bx.png" alt="PCB Layout w/ Only Power Layer Visible" width="900" />
  <br />
  <strong>Figure 15:</strong> PCB Layout w/ Only Power Layer Visible
</p>

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
# Experimental Analysis

&nbsp; &nbsp; &nbsp; &nbsp;As stated in the conceptual design, Team 6’s prototype objective is to design and implement a low cost, modular prototype system capable of directly measuring ionospheric TEC using dual signal GNSS-based signal observations. The prototype will emphasize accuracy, reliability, and field implementation. It will integrate essential functionality for signal acquisition, system control and processing, data logging, and power management. The system will be optimized for efficient operation in field environments and implemented at a total cost not exceeding $1,000.

&nbsp; &nbsp; &nbsp; &nbsp;This document is designed to define the measures of success for the Personal Space Weather Station, describe the methods of evaluation and verification, and assess how effectively the system meets its critical specifications and performance objectives. This process consists of three main stages: 

1. **Designing Experiments**
2. **Conducting Experiments**
3. **Analyzing Results and Drawing Conclusions**

## Designing Experiments

- **Purpose**: Below is a comprehensive list of criteria for defining a successful project and evaluating the effectiveness of the Personal Space Weather Station prototype.  

  - __Dual-frequency Reception Performance__: Ability of the system to consistently receive and process both L1 and L5 GNSS signals required for TEC calculation.
  - __TEC Measurement Accuracy__: Agreement between the system’s calculated TEC values and a credible reference dataset.
  - __Signal Quality__: Quality of received GNSS signals, measured using carrier-to-noise density ratio, sufficient for reliable TEC computation.
  - __Continuous Operating Duration and System Reliability__: Ability of the system to operate continuously for extended durations without crashes, resets, or data loss.
  - __Power System Performance__: Ability of the power subsystem to provide sufficient runtime, maintain stable operation, and safe transition between power sources.
  - __Storage Capacity and Data Logging Reliability__: Ability to store high-rate GNSS data without running out of space and to record complete, timestamped data without corruption or loss.
  - __Modularity and Expandability__: Ease with which system components can be replaced, upgraded, or expanded without requiring major redesign.
  - __Field Implementation__: Ability to deploy, operate, and maintain the system in real-world outdoor environments with minimal setup.
  - __Cost Compliance__: Total system cost remaining within the $1,000 budget constraint.
  - __Documentation/Replicability__: Completeness and clarity of documentation such that the system can be reproduced by another user. 

- **Measures of Success**: The following criteria establish the key performance metrics used to evaluate the effectiveness of the prototype.

  - __Dual-frequency Reception Performance__: Successful operation requires continuous reception and logging of both L1 and L5 signals for at least 95% of the test duration during each trial. 
  - __TEC Measurement Accuracy__: The system shall demonstrate agreement with time-aligned reference TEC data by maintaining mean absolute TEC error within a prototype-appropriate TECU range and consistently follows the same overall TEC trend as the reference dataset
  - __Signal Quality__: For each one-second interval, at least two GNSS signals shall have a carrier-to-noise density ratio greater than or equal to 30 dB-Hz
  - __Continuous Operating Duration and System Reliability__: The system shall operate continuously for a minimum of 24 hours with no system crashes, resets, or data loss events.
  - __Power System Performance__: The system shall maintain uninterrupted operation during transitions between power sources (battery, outlet, and solar input), with zero loss of functionality or data during switching events. It shall also maintain stable regulated voltage rails and effectively filter input power fluctuations. 
  - __Storage Capacity and Data Logging Reliability__: The system shall record continuous, timestamped data for at least 24 hours with no missing timestamps, corrupted files, or storage overflow.
  - __Modularity and Expandability__: System components shall be replaceable or upgradable without requiring major redesign, rewiring, or modification to the overall system architecture.
  - __Field Implementation__: The system shall be deployable by one person in under 15 minutes and achieve operational status within 5 minutes of power-on in an outdoor environment.
  - __Cost Compliance__: The total cost of all system components shall not exceed $1,000. 
  - __Documentation/Replicability__: All required documentation (schematics, bill of materials, software setup, and operating procedures) shall be complete and organized such that no critical steps are missing or ambiguous.

- **Potential Biases**: Below is a list of potential sources of bias that impact the accuracy and reliability of the experimental results.

  - __Environmental Variability__: Changes in weather, obstructions, and atmospheric conditions that affect GNSS signal reception and TEC measurements.
      - __Mitigation Strategy__: Conduct testing under clear sky conditions when possible. Document environmental conditions during each trial and compare results collected under similar conditions.
  - __Satellite Geometry Differences__: Variations in the number and position of visible satellites that influence signal quality and measurement accuracy.
      - __Mitigation Strategy__: Record the number and general position of tracked satellites during each trial and perform multiple trials at different times to account for variations in satellite availability.
  - __Receiver Signal Quality Limitations__: Variations in carrier to noise values or signal loss that reduce measurement reliability and impact TEC accuracy
      - __Mitigation Strategy__: Monitor carrier to noise values during operation; flag data collected below a defined threshold and exclude this data from analysis while retaining it for record-keeping.
  - __Setup Differences__: Inconsistencies in antenna placement, orientation, or system setup that may influence signal reception and results. 
      - __Mitigation Strategy__: Maintain consistent antenna placement and orientation across trials whenever possible. Additionally, perform controlled variations in antenna placement to evaluate the system’s sensitivity to setup differences and ensure consistent comparison between trials.
  

## Conducting Experiments

- **Procedure**: The following steps outline how each performance criterion was tested and evaluated.
  - __Dual-frequency Reception Performance__: Position the dual tuned antenna in an open-sky environment. Monitor the receiver output for UBX data packets and verify that both L1 and L5 signals are present. Confirm that TEC values are consistently computed.  
  - __TEC Measurement Accuracy__: Extract L1 and L5 observations from a credible RINEX dataset corresponding to the same time interval. Compute reference vTEC values and compare them to system-generated vTEC. Calculate statistical metrics including mean absolute error (TECU), root mean squared error (TECU), and mean bias error (TECU).
  - __Signal Quality__: Record the UBX data stream while tracking GNSS satellites. Extract and log carrier-to-noise density ratio values for each satellite at a 1 Hz rate. For each one-second interval, identify and record whether at least two signals have carrier-to-noise density ratio ≥ 30 dB-Hz. 
  - __Continuous Operating Duration and System Reliability__: Operate the system continuously for a minimum of 24 hours while monitoring for system failures, resets, or interruptions. 
  - __Power System Performance__: Operate the system for a minimum of 24 hours using battery power. Transition between outlet power and solar input during operation and verify uninterrupted functionality. Observe and record voltage behavior across regulated power rails during operation and power source transitions. 
  - __Storage Capacity and Data Logging Reliability__: Operate the system continuously while recording GNSS data. Monitor storage usage and verify that all logged data is complete and timestamped correctly. 
  - __Modularity and Expandability__: Demonstrate removal and replacement of key system components. Integrate a non-essential component to verify system expandability. 
  - __Field Implementation__: Deploy and operate the system in multiple outdoor locations for a minimum of 24 hours per test.
  - __Cost Compliance__: Document all system component costs and verify total cost.
  - __Documentation/Replicability__: Compile all required documentation including schematics, software setup, and operating procedures.

- **Data Collection**: For the following categories, pass or fail results will be stored in a System Performance Evaluation Table [1].
   -  __Dual-frequency Reception Performance__: Confirm that L1 and L5 frequencies are occurring in the UBX data stream, and that TEC values are consistently computed. 
  - __TEC Measurement Accuracy__: Record time-aligned vTEC values from both the system and the reference dataset. Compute per-epoch error (TECU) and document statistical metrics including mean absolute error (TECU), root mean squared error (TECU), and mean bias error (TECU).
  - __Signal Quality__: Record carrier-to-noise density ratio values in dB-Hz for each tracked satellite, along with timestamps and satellite identifiers. Data shall be logged at a consistent rate.
  - __Continuous Operating Duration and System Reliability__: Record total runtime and any system interruptions, failures, or resets.
  - __Power System Performance__: Record system operation duration, battery performance, and successful transitions between power sources. Additionally, monitor voltage stability across regulated rails.
  - __Storage Capacity and Data Logging Reliability__: Verify completeness and integrity of logged data, including timestamps and file consistency.  
  - __Modularity and Expandability__: Record results of component replacement and integration of additional modules. 
  - __Field Implementation__: Record deployment conditions and successful system operation in outdoor environments.
  - __Cost Compliance__: Record total system cost.
  - __Documentation/Replicability__: Record completeness and clarity of documentation.

- **Trials**: The following outlines the frequency and number of trials conducted for each test category to ensure consistent and repeatable results.
   -  __Dual-frequency Reception Performance__: Conduct at least three trials in an open-sky environment. In each trial, verify that both L1 and L5 signals are consistently received and logged over a continuous 30-minute interval.
  - __TEC Measurement Accuracy__: Perform a minimum of three trials using time-aligned system data and reference RINEX datasets. Each trial will span a minimum of 6 hours, and computed vTEC values will be compared against reference values to evaluate accuracy.
  - __Signal Quality__: Record carrier-to-noise density ratio over at least three separate trials, each lasting a minimum of 30 minutes. Trials should be conducted at different times of day to account for satellite geometry variations.
  - __Continuous Operating Duration and System Reliability__: Conduct at least one full-duration trial of 24 hours. Additional trials may be performed if system instability is observed. Monitor for interruptions, resets, or data loss.
  - __Power System Performance__: Perform at least three trials involving transitions between power sources (battery, outlet, and solar input). Each trial should include a minimum of one complete transition cycle while the system remains operational. 
  - __Storage Capacity and Data Logging Reliability__: Conduct at least three trials involving continuous data logging for a minimum of 24 hours. Verify that no data corruption, loss, or timestamp inconsistencies occur. 
  - __Modularity and Expandability__: Perform at least three trials involving component replacement or system modification. Demonstrate successful operation after each modification without requiring major redesign. 
  - __Field Implementation__: Conduct at least three deployment trials in different outdoor locations. Each trial should include full system setup, operation for a minimum of 24 hours, and successful data collection.
  - __Cost Compliance__: Perform a single comprehensive cost evaluation by documenting all system components. Verify total cost remains within the $1,000 constraint.
  - __Documentation/Replicability__: Conduct at least one validation review of the project documentation to confirm that another user would have sufficient information to reproduce the system without requiring undocumented steps or assumptions.

## Analyzing Results and Drawing Conclusions

&nbsp; &nbsp; &nbsp; &nbsp;The results of system testing are summarized in the System Performance Evaluation Table, which evaluates each performance criterion against its defined success metric. This table serves as the primary reference for determining whether the Personal Space Weather Station meets its design objectives. 

&nbsp; &nbsp; &nbsp; &nbsp;Performance outcomes were categorized as pass, marginal, or fail based on how closely the system met the defined measures of success. A “pass” indicates that the system fully satisfied the success criteria, while a “fail” indicates that the criteria were not met. A “marginal” classification was used in cases where performance approached the required thresholds but did not fully satisfy all conditions. 

&nbsp; &nbsp; &nbsp; &nbsp;In cases where results were classified as marginal or failed to meet the success criteria, contributing factors such as environmental variability, signal quality limitations, or system constraints were considered during analysis. 

&nbsp; &nbsp; &nbsp; &nbsp;Overall system performance was evaluated by examining both individual criteria and the system as a whole. Particular emphasis was placed on TEC measurement accuracy, continuous operation, and data logging reliability, as these represent the core functional objectives of the system. 

&nbsp; &nbsp; &nbsp; &nbsp;Based on the results, conclusions were drawn regarding the effectiveness of the system design, its readiness for field deployment, and its ability to meet the intended performance requirements. Areas of strong performance and areas requiring improvement were identified to guide future development and refinement. 


**[1]System Performance Evaluation Table**
| Evaluation Criterion | Description | Success Metric | Result |
|---------------------|------------|---------------|--------|
| Dual-Signal Reception Performance | Ability to receive and process both L1 and L5 signals | Continuous logging of both L1 and L5 signals for ≥95% of test duration | Pass |
| TEC Measurement Accuracy | Comparison of calculated TEC to reference data | Mean absolute TEC error (TECU) and agreement with time-aligned reference TEC trend| Marginal |
| Signal Quality (Carrier-to-Noise Density Ratio) | Quality of GNSS signals received | For each one-second interval, at least two GNSS signals shall have carrier-to-noise density ratio ≥ 30 dB-Hz  | Pass |
| Continuous Operating Duration and System Reliability | Ability to operate without interruption | Continuous operation ≥ 24 hours with no failure or data loss | Pass |
| Power System Performance | Battery runtime stability | Continuous operation with stable power and successful switching between power sources without interruption | Pass |
| Storage Capacity and Data Logging Reliability | Ability to store and log data correctly | No missing timestamps, corrupted files, or storage overflow during ≥ 24-hour operation | Pass |
| Modularity and Expandability | Ease of component replacement or upgrade | Components can be replaced or upgraded without major redesign, and system remains operational after replacement | Pass |
| Field Implementation | Ease of setup and outdoor operation | Successful setup and operation outdoors and grid independent | Pass |
| Cost Compliance | Total prototype cost | Total cost ≤ $1,000 | Pass |
| Documentation and Replicability | Ability to reproduce system | Documentation is complete, clear, and contains no missing or ambiguous steps | Pass |

- __Dual-frequency Reception Performance__: The Dual-Frequency Reception Performance criterion was classified as a pass, as shown in Table [1]. The system was required to continuously receive and process GNSS signals necessary for dual-frequency TEC computation. Figure 1 shows a portion of the receiver output, including raw GNSS measurement packets (RXM-RAWX) and satellite tracking data (NAV-SAT). The presence of these packets indicates that the system is successfully acquiring and processing the measurements required for TEC computation. The displayed data includes computed slant TEC (sTEC) and vertical TEC (vTEC) values for multiple satellites, demonstrating that the system is actively performing TEC calculations based on received GNSS signals. Although individual frequency bands are not explicitly labeled in the output, the successful computation of TEC requires dual-frequency observations. The continuous generation of TEC values therefore confirms that both required frequency measurements are being received and processed by the system. Overall, the system maintained continuous GNSS data acquisition and TEC computation throughout testing, satisfying the requirement for dual-frequency reception performance.

<div align="center">
  <img src="https://hackmd.io/_uploads/H1IpqvLTWx.png" alt="GNSS Receiver Output" width="900">
  <p><strong>Figure 1:</strong> GNSS Receiver Output Showing Raw Measurements and TEC Computation</p>
</div>

- __TEC Measurement Accuracy__: The TEC Measurement Accuracy criterion was classified as marginal, as shown in Table [1]. System performance was evaluated based on the agreement between calculated TEC values and time-aligned reference data using absolute error metrics in TEC units. Data collected was compared to measurements distributed by NOAA, recorded by station TN24 in Cookeville, TN.

  &nbsp; &nbsp; &nbsp; &nbsp;An initial test was conducted with the system positioned indoors near a window. Comparison of the system-generated TEC values with reference data showed that the overall trend was captured; however, significant variability and large deviations in magnitude were observed. Quantitative analysis resulted in a mean absolute error of approximately 16.45 TECU, a root mean squared error of 23.82 TECU, and a mean bias error of 7.25 TECU. The error plot for this test shows large spikes and irregular fluctuations, indicating the presence of noise and instability in the measurements. These results suggest that while the system was able to detect general TEC variation, measurement accuracy was significantly degraded under these conditions.

  <div align="center">
    <img width="900" alt="TEC Comparison and Error Plots" src="https://github.com/user-attachments/assets/ff475db8-e5b8-44f8-885d-193fc0a70eef" />
    <p><strong>Figure 2:</strong> Comparison of System and Reference TEC with Corresponding Error Analysis (Test 1)</p>
  </div>

  &nbsp; &nbsp; &nbsp; &nbsp;A follow-up test was conducted in an improved outdoor environment to reduce signal attenuation and multipath interference. In this test, the system demonstrated strong agreement with the overall TEC trend of the reference dataset, with significantly improved stability and reduced variability in the error signal. Quantitative analysis resulted in a mean absolute error of approximately 18.45 TECU, a root mean squared error of 18.77 TECU, and a mean bias error of 18.44 TECU. While the error magnitude remained elevated, the error distribution was more consistent, indicating a reduction in random noise and the presence of a systematic bias.

  <div align="center">
    <img src="https://hackmd.io/_uploads/rkN49OtTZg.png" alt="Outdoor TEC Comparison and Error Plots" width="900">
    <p><strong>Figure 3:</strong> Outdoor TEC Comparison and Error Analysis (Test 2)</p>
  </div>

  &nbsp; &nbsp; &nbsp; &nbsp;These results indicate that the system is capable of reliably capturing TEC trends, but currently exhibits a consistent positive bias that limits absolute measurement accuracy. The improvement in stability between tests suggests that measurement setup plays a significant role in system performance, and that remaining error is primarily systematic rather than random.

  &nbsp; &nbsp; &nbsp; &nbsp;To further evaluate system consistency and characterize long-term performance, two additional 24-hour outdoor data collection experiments were conducted under similar environmental conditions.

  &nbsp; &nbsp; &nbsp; &nbsp;Results from these extended trials demonstrated strong repeatability in both the TEC trend tracking and error characteristics observed in Test 2. Across both datasets, the system continued to closely follow the changes in TEC over time from the NOAA reference values while maintaining improved signal stability compared to indoor measurements.

<div align="center">
    <img src="https://hackmd.io/_uploads/Sk5xSRCTWl.png" alt="TEC Comparison and Error Plots Test 3" width="900">
    <p><strong>Figure 4:</strong> TEC Comparison and Error Analysis (Test 3)</p>
</div>

<div align="center">
    <img src="https://hackmd.io/_uploads/rJcxrCCpZg.png" alt="TEC Comparison and Error Plots Test 4" width="900">
    <p><strong>Figure 5:</strong> TEC Comparison and Error Analysis (Test 4)</p>
</div>

  &nbsp; &nbsp; &nbsp; &nbsp;These additional trials confirm that the observed bias is consistent and therefore systematic in nature rather than the result of random noise. A slight downward trend observed in the error over time may be influenced by changing atmospheric conditions, such as variations in humidity throughout the day, which can affect signal propagation and introduce additional delay components. Because the bias remains stable across multiple 24-hour datasets, it can be treated as a fixed offset in the system. For practical use, particularly in hobbyist applications, this offset can be compensated for by subtracting the estimated bias (approximately 17–20 TECU) from the measured TEC values. Applying this correction significantly improves absolute accuracy while preserving the system’s ability to reliably track TEC variation.

- __Signal Quality__: The Signal Quality criterion was classified as a pass, as shown in Table [1]. The system was required to maintain sufficient signal strength for reliable TEC computation, defined as at least two GNSS signals with carrier-to-noise density ratio (C/N₀) ≥ 30 dB-Hz at each one-second interval.

  During the initial test, signal quality was inconsistent due to indoor placement of the system near a window. Carrier-to-noise density ratio values frequently dropped below the 30 dB-Hz threshold and exhibited significant variability. While some valid signals were observed, the requirement of maintaining at least two signals above the threshold at each epoch was not consistently met under these conditions.

  In the follow-up outdoor test, signal quality improved significantly. Carrier-to-noise density ratio values consistently exceeded 30 dB-Hz, with many signals reaching 40 dB-Hz or higher. For nearly all one-second intervals, at least two signals satisfied the required threshold, indicating reliable signal acquisition and improved measurement conditions.

  These results demonstrate that the system is capable of meeting signal quality requirements when deployed in an appropriate outdoor environment. The observed improvement between tests highlights the importance of antenna placement and signal visibility for achieving consistent and reliable GNSS measurements.

- __Continuous Operating Duration and System Reliability__: The Continuous Operating Duration and System Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to operate continuously for a minimum of 24 hours without interruption, failure, or data loss. During testing, the system operated for the full 24-hour interval without crashes, resets, or interruptions. All data was recorded successfully with no missing timestamps. These results confirm that the system is capable of stable, long-duration operation.

- __Power System Performance__: The Power System Performance criterion was classified as a pass, as shown in Table [1]. The system was required to support continuous operation for a minimum of 24 hours while maintaining stable power delivery and successfully transitioning between available power sources. During testing, the system operated continuously for the full 24-hour interval without interruption while powered by the battery and external sources. Transitions between power inputs, including outlet and solar power, were completed without system resets, loss of functionality, or interruption to data logging.

  &nbsp; &nbsp; &nbsp; &nbsp;A voltage ripple of less than 50 mVpp was recorded in both the 5V and 3.3V PCB rails, as shown in Figures 7 and 8. During AC charging, a brief 60 Hz voltage ripple can be detected at the barrel jack input and is successfully filtered before reaching downstream components. The 12V, 5V, and 3.3V rails all maintained stable voltage levels throughout operation, as shown in Figures 6–8, confirming effective regulation across the power distribution system. It should be noted that the 12V rail does not directly power any system components, but instead serves as an intermediate supply that feeds the 5V regulation stage.

  <div align="center">
    <img src="https://hackmd.io/_uploads/H1xR3OLTbe.png" width="700">
    <p><strong>Figure 6:</strong> 12V Rail Voltage During Operation</p>
  </div>

  <div align="center">
    <img src="https://hackmd.io/_uploads/B1xC2dITZl.png" width="700"> 
    <p><strong>Figure 7:</strong> 5V Rail Voltage During Operation</p>
  </div>

  <div align="center">
    <img src="https://hackmd.io/_uploads/S1l02OITWx.png" width="700">
    <p><strong>Figure 8:</strong> 3.3V Rail Voltage During Operation</p>
  </div>

  <div align="center">
    <img src="https://hackmd.io/_uploads/SJXGgtFa-e.jpg" alt="Solar Power Generation and Consumption Over 7 Days" width="900">
    <p><strong>Figure 9:</strong> Solar Power Generation and Consumption Over a 7-Day Period</p>
  </div>

  &nbsp; &nbsp; &nbsp; &nbsp;Over a multi-day period, the system demonstrated the ability to generate sufficient energy through solar and wall input to support operation. As shown in Figure 9, generated energy meets or exceeds system consumption during multiple intervals, indicating that the system can sustain operation and recharge the battery under typical outdoor conditions. It should be noted that energy generation was not continuous, as the solar panel was not always connected and external power was not consistently supplied, resulting in periods where the system operated solely on stored battery energy or the device was charged with the DC wall power supply for a few hours. Also, power consumption varies in this figure due to testing and periods where the device was frequently turned off and on for undefined periods of time. As seen in figure [9], the average daily usage is 60-100Wh a day. Therefore, our team is confident that a solar generation of 100Wh a day is enough to run this device indefinitly, which is equivalent to a 100W solar panel with 1 hour of sufficient sunlight.

  &nbsp; &nbsp; &nbsp; &nbsp;The system maintained stable operation throughout the duration of testing, indicating that the power subsystem provided consistent and reliable energy delivery under varying conditions. The absence of power-related disruptions confirms that the system is capable of sustained operation in field environments requiring flexible and autonomous power management.

- __Storage Capacity and Data Logging Reliability__: The Storage Capacity and Data Logging Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to record continuous, timestamped data for a minimum of 24 hours without data loss, corruption, or storage overflow. During testing, the system successfully logged GNSS data continuously throughout the 24-hour interval. Each recorded entry includes both local and UTC timestamps, along with corresponding satellite and measurement parameters, demonstrating consistent and structured data collection. No missing timestamps, gaps in logging, or corrupted entries were observed within the dataset. Figure 10 shows a representative segment of the logged data, illustrating continuous recording across multiple satellites and signal parameters. The presence of sequential timestamps and complete measurement fields confirms that data was captured reliably at the intended rate. Additionally, storage capacity was sufficient to support the full duration of testing without reaching capacity limits or impacting system performance. Logged files remained accessible and properly formatted for post-processing, including TEC computation. These results confirm that the system meets the requirements for reliable data logging and storage and is capable of supporting extended data collection for TEC analysis.  

<div align="center">
  <img src="https://hackmd.io/_uploads/Syl340UaWx.png" alt="GNSS Logged Data" width="900">
  <p><strong>Figure 10:</strong> Example of Logged GNSS Data Showing Continuous Timestamped Measurements and Satellite Parameters</p>
</div>

- __Modularity and Expandability__: The Modularity and Expandability criterion was classified as a pass, as shown in Table [1]. The system was required to support component replacement or upgrade without major redesign. During testing, components were successfully removed and replaced without modifying the overall system architecture. The system remained fully operational after replacement, and additional components were integrated without affecting core functionality. These results confirm that the system supports modular design and future expansion.

- __Field Implementation__: The Field Implementation criterion was classified as a pass, as shown in Table [1]. The system was required to be deployable in an outdoor environment with minimal setup. During testing, the system was successfully deployed and operated outdoors under varying conditions, including partially clouded skies. Figure 11 shows the deployed system and antenna configuration. The system operated continuously without interruption, demonstrating its suitability for real-world field applications.

<div align="center">

  <div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="https://hackmd.io/_uploads/Hy_R-8I6-l.jpg" alt="Field Setup 1" style="height: 400px; object-fit: cover;">
    <img src="https://hackmd.io/_uploads/SJlPrCIa-e.jpg" alt="Field Setup 2" style="height: 400px; object-fit: cover;">
  </div>

  <p><strong>Figure 11:</strong> Two Examples of Field Implementation</p>

</div>

- __Cost Compliance__: The Cost Compliance criterion was classified as a pass, as shown in Table [1]. The system was required to maintain a total cost not exceeding $1,000. The total cost of the system was $991.31, including all major subsystems. This total includes components associated with stretch goals, indicating that a minimal implementation could be reproduced at a lower cost. These results confirm that the system meets cost requirements while remaining scalable and accessible.

- __Documentation/Replicability__: The Documentation and Replicability criterion was classified as a pass, as shown in Table [1]. The system was required to be supported by complete documentation sufficient for replication. All project materials were organized within a centralized GitHub repository, including design documentation, subsystem descriptions, and experimental analysis. A README file provides guidance for navigating the repository, and a dedicated software section documents all code written for the system. These materials ensure that the system can be replicated without requiring undocumented steps.

## Conclusion

&nbsp; &nbsp; &nbsp; &nbsp;The Personal Space Weather Station prototype successfully demonstrated core system functionality, including dual-frequency GNSS reception, continuous operation, reliable data logging, and effective field deployment. The system met all performance criteria related to reliability, modularity, cost, and implementation, confirming that the overall design is robust and suitable for real-world use.

&nbsp; &nbsp; &nbsp; &nbsp;However, TEC measurement accuracy did not fully meet the desired performance level. While the system was able to consistently capture the overall TEC trend when compared to NOAA reference data from station TN24, a significant positive bias was observed in the measured values. Error analysis indicates that this discrepancy is primarily systematic rather than random, suggesting that calibration of receiver and hardware delays is required to improve absolute TEC accuracy.

&nbsp; &nbsp; &nbsp; &nbsp;Initial testing conditions, particularly indoor placement near a window, negatively impacted signal reception and contributed to measurement variability. Subsequent outdoor testing demonstrated improved signal quality and stability, reinforcing the importance of proper deployment conditions for accurate TEC measurement.

&nbsp; &nbsp; &nbsp; &nbsp;Future work will focus on refining system calibration, improving signal reception through optimized antenna placement, and conducting extended outdoor testing under consistent conditions. With these improvements, the system is expected to achieve greater measurement accuracy while maintaining its strengths as a low-cost, modular, and deployable platform for ionospheric monitoring.

## Statement of Contributions

Jack Bender: Modularity and Expandability, Documentation/Replicability, Report Preparation

Keneth Creamer-Harris: Power System Performance, Documentation/Replicability

Blake Hudson: Storage Capacity and Data Logging Reliability, Documentation/Replicability

Nolan Magee: Field Implementation, Cost Compliance, Documentation/Replicability 

Jackson Taylor: Dual-Frequency Reception Performance, TEC Measurement Accuracy, Signal Quality, Documentation/Replicability




<h1 style="font-size:40px;">Future Directions and Lessons Learned</h1>

This section summarizes key lessons learned during the design, implementation, and testing of the Personal Space Weather Station. It is intended to support future development efforts and enable other users to successfully replicate, modify, and extend the system. The following insights highlight practical considerations, design improvements, and recommendations based on observed system performance.

## PCB Design and Assembly

- Redesign the PCB to improve ease of assembly for hobbyists and reduce overall complexity.
- Utilize preexisting through-hole buck converter modules where possible to simplify power design.
- Increase component footprint sizes to make soldering more accessible and reduce assembly errors.
- Minimize or eliminate surface-mount (SMD) components, or alternatively provide pre-soldered boards.
- Include clearly visible on-board status LEDs for power, system state, and debugging.
- Consider tariffs, availability, and sourcing constraints when selecting components and manufacturing vendors.

## Power System

- The use of a charge controller supporting both solar input and wall (mains) power was validated and performed reliably.
- Battery selection should be tailored to the user’s needs, with consideration for:
  - Weight
  - Runtime requirements
  - Deployment environment
- Future designs may benefit from modular battery configurations to support different use cases.

## Data Storage and Networking

- Configure the system with a static IP address for the onboard server to improve reliability and simplify remote access.
- Ensure that network configuration steps are clearly documented for ease of replication.

## Data Acquisition and Processing

- Elevation angles for reference vTEC computation were derived from interpolated satellite positions using SP3 ephemeris data (CODE, via NASA CDDIS), as the reference rinex navigation files did not include elevation angles.
- All testing should be conducted outdoors with adequate exposure to the sky. Indoor testing (e.g., near windows) significantly degrades signal quality and measurement accuracy.
- Reference data in this project was obtained from NOAA station TN24 in Cookeville, TN.
- Future implementations should include robust processing of raw RINEX files to generate reference TEC values, as preprocessed external datasets may not be readily available for all locations or time periods.

## Measurement Considerations

- Measurement accuracy is highly sensitive to environmental conditions, antenna placement, and satellite visibility.
- Sampling rate should be selected with consideration of satellite motion and ionospheric traversal, as low sampling rates can introduce spatial averaging (“blurring”) of TEC measurements.
- A consistent systematic bias was observed in TEC measurements, indicating the need for calibration of hardware and receiver delays.
- vTEC is not a measurement of the TEC directly above the receiver as initally assumed. It is instead a measurement of TEC in a line through the atmospheric pierce point, where the line is perpendicular to the ground. Thus, averaging all observed vTEC values at a given timestamp from every satellite is not a valid way to compute the TEC in a straight line above the receiver. However, this metric could be used to describe the relative "activeness" of the visible ionosphere at a given time.

## Future Work

- Develop and implement calibration methods to correct for systematic TEC bias, including satellite bias and receiver bias.
- Improve antenna placement strategies and potentially antenna design to enhance signal quality.
- Expand software capabilities to support automated processing of raw GNSS data (e.g., RINEX workflows).
- Conduct additional long-duration outdoor testing under controlled and varying environmental conditions.
- Further simplify system assembly to improve accessibility for hobbyists, educators, and researchers.
- Currently, the rate of satellite measurements for the system is ~1 epoch per second. To increase this rate, the data collection program would need to be modified from the polling based method it currently employs to a data stream method. Instead of polling the RF module for every epoch of data, the RF module can be configured to output the required data messages at a set rate, possibly increasing the epoch per second rate above 1 Hz. This may allow the device to measure scintillation events in the atmosphere.
- Using the set of vTEC measurements collected, an added functionality of the device could be added to map the vTEC values in the atmosphere at a given timestamp, effectively creating a heat map of TEC in the visible atmosphere. A python script that could be modified for this purpose is included [here](https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/main/Software/Miscellaneous/satGraph.py). This program maps slant TEC values to a compass graph, but can easily be modified to graph vTEC values.


## Conclusion

The development of the Personal Space Weather Station succesfully demonstrated a low-cost, modular system for TEC measurement is both feasible and effective. While the system successfully met most performance objectives, several areas for improvement were identified, particularly in measurement accuracy, system calibration, and ease of replication. Addressing these areas in future iterations will enhance both the performance and accessibility of the system, enabling broader participation in ionospheric research and space weather monitoring.


