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

- __TEC Measurement Accuracy__:- The TEC Measurement Accuracy criterion was classified as marginal, as shown in Table [1]. System performance was evaluated based on the agreement between calculated TEC values and time-aligned reference data using absolute error metrics in TEC units. Data collected was compared to measurements distributed by NOAA, recorded by station TN24 in Cookeville, TN.

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

  &nbsp; &nbsp; &nbsp; &nbsp;These additional trials confirm that the observed bias is consistent and therefore systematic in nature rather than the result of random noise. Because this bias remains stable across multiple 24-hour datasets, it can be treated as a fixed offset in the system. For practical use, particularly in hobbyist applications, this offset can be compensated for by subtracting the estimated bias (approximately 17–20 TECU) from the measured TEC values. Applying this correction significantly improves absolute accuracy while preserving the system’s ability to reliably track TEC variation.

- __Signal Quality__: The Signal Quality criterion was classified as a pass, as shown in Table [1]. The system was required to maintain sufficient signal strength for reliable TEC computation, defined as at least two GNSS signals with carrier-to-noise density ratio (C/N₀) ≥ 30 dB-Hz at each one-second interval.

  During the initial test, signal quality was inconsistent due to indoor placement of the system near a window. Carrier-to-noise density ratio values frequently dropped below the 30 dB-Hz threshold and exhibited significant variability. While some valid signals were observed, the requirement of maintaining at least two signals above the threshold at each epoch was not consistently met under these conditions.

  In the follow-up outdoor test, signal quality improved significantly. Carrier-to-noise density ratio values consistently exceeded 30 dB-Hz, with many signals reaching 40 dB-Hz or higher. For nearly all one-second intervals, at least two signals satisfied the required threshold, indicating reliable signal acquisition and improved measurement conditions.

  These results demonstrate that the system is capable of meeting signal quality requirements when deployed in an appropriate outdoor environment. The observed improvement between tests highlights the importance of antenna placement and signal visibility for achieving consistent and reliable GNSS measurements.

- __Continuous Operating Duration and System Reliability__: The Continuous Operating Duration and System Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to operate continuously for a minimum of 24 hours without interruption, failure, or data loss. During testing, the system operated for the full 24-hour interval without crashes, resets, or interruptions. All data was recorded successfully with no missing timestamps. These results confirm that the system is capable of stable, long-duration operation.

- __Power System Performance__: The Power System Performance criterion was classified as a pass, as shown in Table [1]. The system was required to support continuous operation for a minimum of 24 hours while maintaining stable power delivery and successfully transitioning between available power sources. During testing, the system operated continuously for the full 24-hour interval without interruption while powered by the battery and external sources. Transitions between power inputs, including outlet and solar power, were completed without system resets, loss of functionality, or interruption to data logging.

  A voltage ripple of less than 50 mVpp was recorded in both the 5V and 3.3V PCB rails, as shown in Figures 7 and 8. During AC charging, a brief 60 Hz voltage ripple can be detected at the barrel jack input and is successfully filtered before reaching downstream components. The 12V, 5V, and 3.3V rails all maintained stable voltage levels throughout operation, as shown in Figures 6–8, confirming effective regulation across the power distribution system.

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

  &nbsp; &nbsp; &nbsp; &nbsp;Over a multi-day period, the system demonstrated the ability to generate sufficient energy through solar and wall input to support operation. As shown in Figure 9, generated energy meets or exceeds system consumption during multiple intervals, indicating that the system can sustain operation and recharge the battery under typical outdoor conditions.

  &nbsp; &nbsp; &nbsp; &nbsp;The system maintained stable operation throughout the duration of testing, indicating that the power subsystem provided consistent and reliable energy delivery under varying conditions. The absence of power-related disruptions confirms that the system is capable of sustained operation in field environments requiring flexible and autonomous power management.

- __Storage Capacity and Data Logging Reliability__: The Storage Capacity and Data Logging Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to record continuous, timestamped data for a minimum of 24 hours without data loss, corruption, or storage overflow. During testing, the system successfully logged GNSS data continuously throughout the 24-hour interval. Each recorded entry includes both local and UTC timestamps, along with corresponding satellite and measurement parameters, demonstrating consistent and structured data collection. No missing timestamps, gaps in logging, or corrupted entries were observed within the dataset. Figure 6 shows a representative segment of the logged data, illustrating continuous recording across multiple satellites and signal parameters. The presence of sequential timestamps and complete measurement fields confirms that data was captured reliably at the intended rate. Additionally, storage capacity was sufficient to support the full duration of testing without reaching capacity limits or impacting system performance. Logged files remained accessible and properly formatted for post-processing, including TEC computation. These results confirm that the system meets the requirements for reliable data logging and storage and is capable of supporting extended data collection for TEC analysis.  

<div align="center">
  <img src="https://hackmd.io/_uploads/Syl340UaWx.png" alt="GNSS Logged Data" width="900">
  <p><strong>Figure 10:</strong> Example of Logged GNSS Data Showing Continuous Timestamped Measurements and Satellite Parameters</p>
</div>

- __Modularity and Expandability__: The Modularity and Expandability criterion was classified as a pass, as shown in Table [1]. The system was required to support component replacement or upgrade without major redesign. During testing, components were successfully removed and replaced without modifying the overall system architecture. The system remained fully operational after replacement, and additional components were integrated without affecting core functionality. These results confirm that the system supports modular design and future expansion.

- __Field Implementation__: The Field Implementation criterion was classified as a pass, as shown in Table [1]. The system was required to be deployable in an outdoor environment with minimal setup. During testing, the system was successfully deployed and operated outdoors under varying conditions, including partially clouded skies. Figure 7 shows the deployed system and antenna configuration. The system operated continuously without interruption, demonstrating its suitability for real-world field applications.

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

Jack Bender: Modularity and Expandability, Documentaion/Replicability, Report Preparation

Keneth Creamer-Harris: Power System Performance, Documentaion/Replicability

Blake Hudson: Storage Capacity and Data Logging Reliability, Documentaion/Replicability

Nolan Magee: Field Implementation, Cost Compliance, Documentaion/Replicability 

Jackson Taylor: Dual-Frequency Reception Performance, TEC Measurement Accuracy, Signal Quality, Documentaion/Replicability
