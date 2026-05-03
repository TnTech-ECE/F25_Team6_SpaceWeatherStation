

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
