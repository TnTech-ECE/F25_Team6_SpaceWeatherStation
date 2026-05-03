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
