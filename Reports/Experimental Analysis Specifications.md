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

  - __Dual-frequency Reception Performance__: The Dual-Frequency Reception Performance criterion is classified as a pass, as shown in Table [1]. Successful operation requires continuous reception and processing of L1 and L5 GNSS signals, which are necessary for accurate TEC computation. Figure [1] shows a portion of the receiver output, where both L1 and L5 signals are clearly identified in the UBX data stream. The system consistently detected and logged both frequencies throughout the duration of testing, satisfying the requirement for dual-frequency operation.  

In addition, Figure [2] illustrates the computed TEC values over time, demonstrating that TEC calculations were continuously performed using the dual-frequency observations. The presence of stable and continuous TEC output further confirms that both signals were not only received but also successfully processed by the system.  

Overall, the system maintained dual-frequency signal reception for greater than 95% of the test duration, meeting the defined success metric. These results confirm that the system can support reliable TEC computation through consistent L1 and L5 signal acquisition and processing.  

  - __TEC Measurement Accuracy__:
  - __Signal Quality__:
  - __Continuous Operating Duration and System Reliability__: The Continuous Operating Duration and System Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to operate continuously for a minimum of 24 hours without interruption, system failure, or data loss. 

During testing, the system operated continuously for the full 24-hour interval without any observed crashes, resets, or interruptions in functionality. Additionally, all data was successfully recorded throughout the test duration, with no missing timestamps or evidence of data loss. 

These results demonstrate that the system is capable of stable, long-duration operation and is suitable for extended data collection in field environments. The absence of failures or interruptions indicates that the system design is robust and reliable under sustained operation. 
  - __Power System Performance__: 
  - __Storage Capacity and Data Logging Reliability__: The Storage Capacity and Data Logging Reliability criterion was classified as a pass, as shown in Table [1]. The system was required to record continuous, timestamped data for a minimum of 24 hours without data loss, corruption, or storage overflow. 

During testing, the system successfully logged data continuously throughout the 24-hour interval. All recorded data contained consistent timestamps with no missing entries, and no corrupted or incomplete files were observed. 

Figure X shows the total data storage over a representative two-hour interval during system operation. The steady and continuous increase in data storage, without abrupt changes, gaps, or irregularities, indicates that data was recorded consistently during this period. This behavior is representative of the system’s performance over the full test duration. 

Additionally, storage capacity was sufficient to support the entire 24-hour test without reaching capacity limits or impacting system performance. 

These results confirm that the system meets the requirements for reliable data logging and storage and can support extended data collection for TEC analysis. 
  - __Modularity and Expandability__: The Modularity and Expandability criterion was classified as a pass, as shown in Table [1]. The system was required to allow component replacement or upgrade without requiring major redesign, rewiring, or modification to the overall system architecture. 

During testing, system components were successfully removed and replaced without requiring changes to the overall system design. Following component replacement, the system remained fully operational and continued to perform all required functions without degradation in performance. 

Additionally, the system architecture supported integration of non-essential components without impacting core functionality. This demonstrates that the system design is modular and can be adapted or expanded to support future modifications or additional features. 

These results confirm that the system meets the requirement for modularity and can support maintenance, upgrades, and future development without significant redesign. 
  - __Field Implementation__: The Field Implementation criterion was classified as a pass, as shown in Table [1]. The system was required to be deployable in an outdoor environment with self-contained power and minimal setup. 

During testing, the system was successfully deployed and operated in outdoor environments under varying conditions. Setup was completed efficiently, and the system achieved operational status shortly after power-on. The system functioned as expected in real-world conditions, including periods of partially clouded sky. 

Figures 3 and 4 show the system deployed in the field, including antenna placement and overall system configuration. The setup demonstrates that the system is compact, portable, and suitable for practical use outside of a controlled laboratory environment. 

The system operated continuously during field deployment without interruption, confirming that it is capable of reliable performance in real-world environments. These results indicate that the system meets the requirements for field implementation and is suitable for portable space weather monitoring applications. 
  - __Cost Compliance__: The Cost Compliance criterion was classified as a pass, as shown in Table [1]. The system was required to maintain a total cost not exceeding $1,000. 

The total cost of the system was calculated by summing all major subsystem components, including data and storage, power, signal collection and processing, enclosure, and printed circuit board (PCB) fabrication. The cost breakdown is as follows: 

  - Data and Storage: $183.40  
  - Power: $327.48  
  - Signal Collection and Processing: $321.66  
  - Enclosure: $80.67  
  - PCB: $78.10  

The total system cost was $991.31, which falls within the $1,000 budget constraint. 

It is important to note that this total includes additional components and design features associated with stretch goals. A minimal implementation of the system, focused solely on core functionality, could be reproduced at a lower cost. This indicates that the system design is not only within budget but also scalable and accessible for future users with varying resource constraints. 

These results confirm that the system meets the cost compliance requirement while maintaining flexibility for cost optimization and broader usability. 
  - __Documentation/Replicability__: The Documentation and Replicability criterion was classified as a pass, as shown in Table [1]. The system was required to be supported by complete and clear documentation sufficient for replication without requiring undocumented steps. 

To support this requirement, all project materials were organized and maintained within a centralized GitHub repository. The repository includes structured documentation covering all aspects of the system design, implementation, and testing. Key documents include the project proposal, conceptual design, detailed subsystem designs (data and storage, power system, RF module and antenna, enclosure, and PCB interconnections), as well as experimental analysis. 

In addition to hardware and system design documentation, the repository contains a dedicated README file that provides an overview of the project and guidance for navigating the available resources. A separate software section is also included to document all code written for the system. 

The repository further includes supporting materials such as electrical design files, 3D models, and organized meeting records, providing a comprehensive record of system development. This level of organization ensures that all necessary information is accessible and logically structured for future users. 

The completeness and organization of the documentation indicate that the system can be replicated by another user without requiring additional clarification or undocumented assumptions. These results confirm that the project meets the requirements for documentation and replicability. 


## Statement of Contributions

Each team member must contribute meaningfully to the experimental analysis and document their contributions clearly in this section. Contributions should be recorded individually, and one team member may not document contributions on behalf of another. Each team member must clearly outline their involvement in experiment design, execution, data analysis, and reporting. By submitting this report, the team collectively certifies the accuracy and completeness of each member's stated contributions.
