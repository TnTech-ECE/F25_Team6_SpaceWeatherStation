# Experimental Analysis

As stated in the conceptual design, Team 6’s prototype objective is to design and implement a low cost, modular prototype system capable of directly measuring ionospheric TEC using dual signal GNSS-based signal observations. The prototype will emphasize accuracy, reliability, and field implementation. It will integrate essential functionality for signal acquisition, system control and processing, data logging, and power management. The system will be optimized for efficient operation in field environments and implemented at a total cost not exceeding $1,000.

This document is designed to define the measures of success for the Personal Space Weather Station, describe the methods of evaluation and verification, and assess how effectively the system meets its critical specifications and performance objectives. This process consists of three main stages: 

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

- **Measures of Success**:

  - __Dual-frequency Reception Performance__: Successful operation requires continuous reception and logging of both L1 and L5 signals for at least 95% of the test duration during each trial. 
  - __TEC Measurement Accuracy__: The system shall produce TEC estimates with a mean percent error less than or equal to 15% when compared to time-aligned reference TEC data.
  - __Signal Quality__: At least 70% of recorded carrier-to-noise density ratio values shall be greater than or equal to 30 dB-Hz during nominal operation.
  - __Continuous Operating Duration and System Reliability__: The system shall operate continuously for a minimum of 24 hours with no system crashes, resets, or data loss events.
  - __Power System Performance__:  The system shall maintain uninterrupted operation during transitions between power sources (battery, outlet, and solar input), with zero loss of functionality or data during switching events.
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

- **Procedure**
  - __Dual-frequency Reception Performance__: Position the dual tuned antenna in an open-sky environment. Monitor the receiver output for UBX data packets and verify that both L1 and L5 signals are present. Confirm that TEC values are consistently computed.  
  - __TEC Measurement Accuracy__: Extract L1 and L5 observations from a credible RINEX dataset corresponding to the same time interval. Compute reference vTEC values and compare them to system-generated vTEC. Calculate statistical metrics including mean error, standard deviation, and percentage error.
  - __Signal Quality__: Record the UBX data stream while tracking GNSS satellites. Extract and log carrier-to-noise density ratio values over the test period. 
  - __Continuous Operating Duration and System Reliability__: Operate the system continuously for a minimum of 24 hours while monitoring for system failures, resets, or interruptions. 
  - __Power System Performance__: Operate the system for a minimum of 24 hours using battery power. Transition between outlet power and solar input during operation and verify uninterrupted functionality. 
  - __Storage Capacity and Data Logging Reliability__: Operate the system continuously while recording GNSS data. Monitor storage usage and verify that all logged data is complete and timestamped correctly. 
  - __Modularity and Expandability__: Demonstrate removal and replacement of key system components. Integrate a non-essential component to verify system expandability. 
  - __Field Implementation__: Deploy and operate the system in multiple outdoor locations for a minimum of 24 hours per test.
  - __Cost Compliance__: Document all system component costs and verify total cost.
  - __Documentation/Replicability__: Compile all required documentation including schematics, software setup, and operating procedures.

- **Data Collection**: For the following categories, pass or fail results will be stored in a System Performance Evaluation Table [1].
   -  __Dual-frequency Reception Performance__: Confirm that L1 and L5 frequencies are occurring in the UBX data stream, and that TEC values are consistently computed. 
  - __TEC Measurement Accuracy__: Record time-aligned vTEC values from both the system and the reference dataset. Compute per-epoch error (TECU) and document statistical metrics including mean error and standard deviation.
  - __Signal Quality__: Record carrier-to-noise density ratio values in dB-Hz for each tracked satellite, along with timestamps and satellite identifiers. Data shall be logged at a consistent rate.
  - __Continuous Operating Duration and System Reliability__: Record total runtime and any system interruptions, failures, or resets.
  - __Power System Performance__: Record system operation duration, battery performance, and successful transitions between power sources.
  - __Storage Capacity and Data Logging Reliability__: Verify completeness and integrity of logged data, including timestamps and file consistency.  
  - __Modularity and Expandability__: Record results of component replacement and integration of additional modules. 
  - __Field Implementation__: Record deployment conditions and successful system operation in outdoor environments.
  - __Cost Compliance__: Record total system cost.
  - __Documentation/Replicability__: Record completeness and clarity of documentation.

- **Trials**: 
   -  __Dual-frequency Reception Performance__: Conduct at least three trials in an open-sky environment. In each trial, verify that both L1 and L5 signals are consistently received and logged over a continuous 30-minute interval.
  - __TEC Measurement Accuracy__: Perform a minimum of three trials using time-aligned system data and reference RINEX datasets. Each trial will span a minimum of 30 minutes, and computed vTEC values will be compared against reference values to evaluate accuracy.
  - __Signal Quality__: Record carrier-to-noise density ratio over at least three separate trials, each lasting a minimum of 30 minutes. Trials should be conducted at different times of day to account for satellite geometry variations.
  - __Continuous Operating Duration and System Reliability__: Conduct at least one full-duration trial of 24 hours. Additional trials may be performed if system instability is observed. Monitor for interruptions, resets, or data loss.
  - __Power System Performance__: Perform at least three trials involving transitions between power sources (battery, outlet, and solar input). Each trial should include a minimum of one complete transition cycle while the system remains operational. 
  - __Storage Capacity and Data Logging Reliability__: Conduct at least three trials involving continuous data logging for a minimum of 24 hours. Verify that no data corruption, loss, or timestamp inconsistencies occur. 
  - __Modularity and Expandability__: Perform at least three trials involving component replacement or system modification. Demonstrate successful operation after each modification without requiring major redesign. 
  - __Field Implementation__: Conduct at least three deployment trials in different outdoor locations. Each trial should include full system setup, operation for a minimum of 24 hours, and successful data collection.
  - __Cost Compliance__: Perform a single comprehensive cost evaluation by documenting all system components. Verify total cost remains within the $1,000 constraint.
  - __Documentation/Replicability__: Conduct at least one validation review of the project documentation to confirm that another user would have sufficient information to reproduce the system without requiring undocumented steps or assumptions.

## Analyzing Results and Drawing Conclusions

The results of system testing are summarized in the System Performance Evaluation Table, which evaluates each performance criterion against its defined success metric. This table serves as the primary reference for determining whether the Personal Space Weather Station meets its design objectives. 

Performance outcomes were categorized as pass, marginal, or fail based on how closely the system met the defined measures of success. A “pass” indicates that the system fully satisfied the success criteria, while a “fail” indicates that the criteria were not met. A “marginal” classification was used in cases where performance approached the required thresholds but did not fully satisfy all conditions. 

In cases where results were classified as marginal or failed to meet the success criteria, contributing factors such as environmental variability, signal quality limitations, or system constraints were considered during analysis. 

Overall system performance was evaluated by examining both individual criteria and the system as a whole. Particular emphasis was placed on TEC measurement accuracy, continuous operation, and data logging reliability, as these represent the core functional objectives of the system. 

Based on the results, conclusions were drawn regarding the effectiveness of the system design, its readiness for field deployment, and its ability to meet the intended performance requirements. Areas of strong performance and areas requiring improvement were identified to guide future development and refinement. 

| Evaluation Criterion | Description | Success Metric | Result |
|---------------------|------------|---------------|--------|
| Dual-Signal Reception Performance | Ability to receive and process both L1 and L5 signals | Continuous logging of both L1 and L5 signals for ≥95% of test duration | Pass |
| TEC Measurement Accuracy | Comparison of calculated TEC to reference data | Mean percent error ≤ 15% | Marginal |
| Signal Quality (Carrier-to-Noise Density Ratio) | Quality of GNSS signals received | ≥ 80% of carrier-to-noise density values ≥ 30 dB-Hz | Fail |
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

- __TEC Measurement Accuracy__: 
- __Signal Quality__: 
- __Continuous Operating Duration and System Reliability__: The Continuous Operating Duration and System Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to operate continuously for a minimum of 24 hours without interruption, failure, or data loss. During testing, the system operated for the full 24-hour interval without crashes, resets, or interruptions. All data was recorded successfully with no missing timestamps. These results confirm that the system is capable of stable, long-duration operation.

- __Power System Performance__: The Power System Performance criterion was classified as a pass, as shown in Table [1]. The system was required to maintain continuous operation while providing stable power and successfully transitioning between power sources. During testing, the system operated continuously for the full duration while powered by battery and external sources. Transitions between power inputs were completed without interruption, system reset, or data loss. These results confirm that the power subsystem provides reliable and stable operation under varying conditions.

- __Storage Capacity and Data Logging Reliability__: The Storage Capacity and Data Logging Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to record continuous, timestamped data for at least 24 hours without loss, corruption, or storage overflow. During testing, data was logged continuously with no missing timestamps or corrupted files. Figure [X] shows data storage over a representative two-hour interval, where a steady increase in storage indicates continuous logging with no interruptions. Storage capacity was sufficient for the full duration of testing, confirming reliable data collection.

- __Modularity and Expandability__: The Modularity and Expandability criterion was classified as a pass, as shown in Table [1]. The system was required to support component replacement or upgrade without major redesign. During testing, components were successfully removed and replaced without modifying the overall system architecture. The system remained fully operational after replacement, and additional components were integrated without affecting core functionality. These results confirm that the system supports modular design and future expansion.

- __Field Implementation__: The Field Implementation criterion was classified as a pass, as shown in Table [1]. The system was required to be deployable in an outdoor environment with minimal setup. During testing, the system was successfully deployed and operated outdoors under varying conditions, including partially clouded skies. Figures [3] and [4] show the deployed system and antenna configuration. The system operated continuously without interruption, demonstrating its suitability for real-world field applications.

<div style="display: flex; justify-content: space-between;">

<img src="https://hackmd.io/_uploads/Hy_R-8I6-l.jpg" alt="Left Image" width="48%">

<img src="RIGHT_IMAGE_URL_HERE" alt="Right Image" width="48%">

</div>

- __Cost Compliance__: The Cost Compliance criterion was classified as a pass, as shown in Table [1]. The system was required to maintain a total cost not exceeding $1,000. The total cost of the system was $991.31, including all major subsystems. This total includes components associated with stretch goals, indicating that a minimal implementation could be reproduced at a lower cost. These results confirm that the system meets cost requirements while remaining scalable and accessible.

- __Documentation/Replicability__: The Documentation and Replicability criterion was classified as a pass, as shown in Table [1]. The system was required to be supported by complete documentation sufficient for replication. All project materials were organized within a centralized GitHub repository, including design documentation, subsystem descriptions, and experimental analysis. A README file provides guidance for navigating the repository, and a dedicated software section documents all code written for the system. These materials ensure that the system can be replicated without requiring undocumented steps.


## Statement of Contributions

Each team member must contribute meaningfully to the experimental analysis and document their contributions clearly in this section. Contributions should be recorded individually, and one team member may not document contributions on behalf of another. Each team member must clearly outline their involvement in experiment design, execution, data analysis, and reporting. By submitting this report, the team collectively certifies the accuracy and completeness of each member's stated contributions.
