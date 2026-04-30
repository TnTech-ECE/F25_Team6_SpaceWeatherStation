# What The TEC (Personal Space Weather Station)

## Executive Summary

Team 6 has developed a low-cost, modular, and replicable prototype capable of measuring total electron content (TEC) from dual-frequency GNSS signals. The system integrates an antenna, receiver, processing unit, and expandable modules within a single housing compartment to support mobility, while remaining under $1,000. Propagation of the prototype is supported by thorough documentation for seamless hobbyist replication. By normalizing access to TEC measurement, the project expands opportunities for education, grassroots research, and innovation. Moreover, it contributes to a distributed global database of ionospheric conditions, enhancing collective understanding of space weather and its implications for modern infrastructure.

## Capabilities

The version of the Personal Space Weather Station developed in this repository is capable of performing end-to-end ionospheric Total Electron Content (TEC) measurement using dual-frequency GNSS signals. At its core, the system receives L1 and L5 satellite signals through a dual-tuned patch antenna and processes them using a dedicated GNSS RF module. These signals are converted into structured data containing pseudorange and carrier phase measurements, which are then used to compute TEC values in real time.

The system supports continuous multi-satellite tracking, allowing it to collect data from up to ~50 GNSS satellites simultaneously. This enables consistent TEC monitoring with sufficient temporal resolution to observe ionospheric variations. The computed TEC values, along with raw GNSS observables and system health data, are logged to a local storage device and can also be accessed through a lightweight web-based interface for visualization and analysis.

A major capability of the system is its ability to operate autonomously in field environments. The hybrid power subsystem allows operation from battery, wall power, or solar input, enabling deployment in both laboratory and remote outdoor settings. The system can sustain continuous operation for at least 24 hours without interruption while maintaining stable data logging and processing.

The architecture is highly modular. A central PCB hub allows easy integration, removal, or replacement of subsystems such as the RF module, computing platform, sensors, and storage. This enables users to expand functionality beyond TEC measurement, including adding environmental sensors or experimenting with additional RF or signal processing modules.

Overall, this implementation delivers a complete, low-cost (~$1000), field-deployable platform capable of contributing meaningful ionospheric data while remaining accessible to students, researchers, and hobbyists.

## Salient Outcomes

Several outcomes of this project stand out as particularly impactful and insightful.

One of the most significant results is that the system successfully demonstrated reliable dual-frequency GNSS reception and continuous TEC computation. The system consistently tracked multiple satellites and maintained uninterrupted operation for extended periods (>24 hours), confirming that a low-cost architecture can achieve performance comparable to more expensive research systems in terms of functionality and reliability.

Another key outcome is the system’s ability to accurately capture TEC trends over time. While absolute accuracy showed a consistent bias, the system closely followed the variation and behavior of reference TEC datasets. This is important because it demonstrates that meaningful ionospheric observations can still be made even when calibration is not perfect. The identification of this bias as systematic rather than random is especially valuable, as it suggests that future calibration can significantly improve performance without requiring major hardware changes.

Another interesting outcome is the success of the modular architecture. The system allowed components to be removed, replaced, and expanded without redesigning the overall system. This validates the design philosophy and shows that the platform can evolve over time, supporting future experimentation and upgrades.

From a systems engineering perspective, the power subsystem performance was also notable. The system maintained stable voltage rails and transitioned seamlessly between battery, AC, and solar inputs without interruption. This demonstrates that the design is robust enough for real-world, long-duration field deployments.

Finally, one of the most important outcomes is that the entire system was implemented within the $1000 budget while still meeting nearly all performance requirements. This confirms that high-value scientific instrumentation can be made accessible, supporting the broader goal of distributed, community-driven ionospheric research.


## Project Demonstration & Images

More pictures and video demonstration to come...

![IMG_0876 Large](https://hackmd.io/_uploads/BJzX61-0Ze.jpg)

## About Us

### Team

Jack Bender – Systems Interconnections Subsystem
Responsible for the design and implementation of the system interconnections architecture. This includes developing the PCB hub and ensuring proper routing of power, data, RF, and control signals between all subsystems. Responsibilities also include standardizing interfaces and connections to maintain modularity, reliability, and ease of expansion.

Kenneth Creamer-Harris – Power Subsystem
Lead the design and implementation of the power subsystem. Responsibilities include developing a stable and efficient power architecture, integrating battery management, voltage regulation, and AC/solar charging capabilities. This work ensures safe, continuous operation in both laboratory and field environments.

Blake Hudson – Data and Storage Subsystem
Responsible for the data and storage subsystem. This includes receiving processed GNSS data, implementing accurate timestamping, and ensuring reliable long-term storage. Additional responsibilities include designing and managing the system’s server interface for data visualization, access, and user interaction.

Nolan Magee – Enclosure Subsystem
Responsible for the design and implementation of the enclosure subsystem. This work focuses on selecting and configuring a protective housing that meets environmental requirements while maintaining accessibility, thermal management, and structural integrity for field deployment.

Jackson Taylor – Signal Acquisition and Processing
Responsible for GNSS signal acquisition and processing. Responsibilities include interfacing with the RF module, extracting GNSS measurements, and supporting TEC computation. This role ensures reliable signal reception and contributes to overall system performance and measurement accuracy.

### Faculty Advisor

Mr. Owen O'Connor

### Stakeholders

Tell a bit about the customer for the project. Also discuss any other groups (specific or general) that are expected to be impacted by the project.

### Recognitions

Use this space to recognize anyone that you feel has had an impact on the project. Be sure to recognize the work of previous teams if you referenced it for style or content. 

## Repo Organization

Give the layout of the repo and what can be found where. Make it easy on those who are interested by making the headings of the various things in this section clickable links to the relevant folder or file in the repo.


### Reports

In the reports section of this repository information about the individual expectations for the reports and how they should be housed is provided.

### Documentation

In the documentaion section information regarding the documentation that is required and how it should be organized is given.

### Software

In the software directory of the repo information regarding how each team is expected to document software can be found.
