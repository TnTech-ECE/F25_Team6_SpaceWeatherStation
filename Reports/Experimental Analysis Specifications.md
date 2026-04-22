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

- **Potential Biases**:

  - Identify potential sources of bias or errors that may impact experimental results.
  - Develop clear strategies to mitigate or control these biases (e.g., randomized trials, controlled environments, calibration of instruments).



## Conducting Experiments

When carrying out experiments:

- Carefully adhere to the established experimental procedures.
- Conduct each trial consistently to ensure reliable and comparable results.
- Record all data accurately and methodically.
- Organize your data clearly, using appropriate formats such as tables, charts, or graphs for ease of analysis.



## Analyzing Results and Drawing Conclusions

After completing experiments:

- Thoroughly analyze all collected data, paying close attention to consistency and patterns.
- Evaluate your data to identify potential sources of error, bias, or abnormalities, and address their implications.
- Clearly articulate conclusions derived from the data, emphasizing evidence-based insights and interpretations.
- Identify correlations or suggest causal relationships, if supported by data.

If analysis uncovers questions or uncertainties, consider designing and executing additional targeted experiments to refine your understanding.



## Writing the Report

Your deliverable should be a comprehensive markdown document, clearly organized, and uploaded to your project's GitHub repository.



For each documented experiment, you must include:

1. **Purpose and Justification**:

   - Explain why the experiment was designed, and how it relates to your critical success criteria.

2. **Detailed Procedure**:

   - Outline clearly the methods used, ensuring another team could reproduce your experiment.

3. **Expected Results**:

   - State your initial hypothesis or expectations clearly before conducting experiments.

4. **Actual Results**:

   - Present data collected during the experiments in an organized, easy-to-interpret format (tables, graphs, charts).

5. **Interpretation and Conclusions**:

   - Provide a detailed analysis explaining the significance of the results.
   - State whether results matched your expectations and explain any discrepancies.



When you have complete all of the experiments: clearly summarize whether your experiments demonstrated that your project meets the original success criteria outlined in your conceptual design. If success criteria were not met, discuss the reasons and outline steps for improvement.



## Statement of Contributions

Each team member must contribute meaningfully to the experimental analysis and document their contributions clearly in this section. Contributions should be recorded individually, and one team member may not document contributions on behalf of another. Each team member must clearly outline their involvement in experiment design, execution, data analysis, and reporting. By submitting this report, the team collectively certifies the accuracy and completeness of each member's stated contributions.
