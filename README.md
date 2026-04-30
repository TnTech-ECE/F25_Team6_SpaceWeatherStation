# What The TEC (Personal Space Weather Station)

## Executive Summary

Team 6 has developed a low-cost, modular, and replicable prototype capable of measuring total electron content (TEC) from dual-frequency GNSS signals. The system integrates an antenna, receiver, processing unit, and expandable modules within a single housing compartment to support mobility, while remaining under $1,000. Propagation of the prototype is supported by thorough documentation for seamless hobbyist replication. By normalizing access to TEC measurement, the project expands opportunities for education, grassroots research, and innovation. Moreover, it contributes to a distributed global database of ionospheric conditions, enhancing collective understanding of space weather and its implications for modern infrastructure.

## Capabilities

The version of the Personal Space Weather Station developed in this repository is capable of performing end-to-end ionospheric Total Electron Content (TEC) measurement using dual-frequency GNSS signals. At its core, the system receives L1 and L5 satellite signals through a dual-tuned patch antenna and processes them using a dedicated GNSS RF module. These signals are converted into structured data containing pseudorange and carrier phase measurements, which are then used to compute TEC values in real time.

The system supports continuous multi-satellite tracking, allowing it to collect data from up to ~20 GNSS satellites simultaneously. This enables consistent TEC monitoring with sufficient temporal resolution to observe ionospheric variations. The computed TEC values, along with raw GNSS observables and system health data, are logged to a local storage device and can also be accessed through a lightweight web-based interface for visualization and analysis.

A major capability of the system is its ability to operate autonomously in field environments. The hybrid power subsystem allows operation from battery, wall power, or solar input, enabling deployment in both laboratory and remote outdoor settings. The system can sustain continuous operation for at least 24 hours without interruption while maintaining stable data logging and processing.

The architecture is highly modular. A central PCB hub allows easy integration, removal, or replacement of subsystems such as the RF module, computing platform, sensors, and storage. This enables users to expand functionality beyond TEC measurement, including adding environmental sensors or experimenting with additional RF or signal processing modules.

Overall, this implementation delivers a complete, low-cost (~$1000), field-deployable platform capable of contributing meaningful ionospheric data while remaining accessible to students, researchers, and hobbyists.

## Salient Outcomes

Projects often have some outcomes that are more interesting than others. Here, highlight those things that you found interesting!


## Project Demonstration & Images

Give a link to a video of the project being demonstrated. The video should be hosted on the capstone youtube.

Below the video link show some well-taken, appropriately sized images of the project.


## About Us

### Team

Give a brief bio for each team member and their broad contribution to the project (no need to be terribly specifc).

### Faculty Supervisor

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
