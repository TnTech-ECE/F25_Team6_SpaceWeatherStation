# Personal Space Weather Station  
## What The TEC  
**April 30, 2026**

---

## Team Members
- Jack Bender (System Interconnection)  
- Kenneth Creamer-Harris (Power)  
- Blake Hudson (Data and Storage)  
- Nolan Magee (Enclosure)  
- Jackson Taylor (RF Module)  

### Major Contributors
- Owen O'Connor (Advisor)  
- Dr. Jeffrey Austen (Customer)  
- Dr. Christopher Storm Johnson (Instructor)  

---

## Live Demonstration
http://10.122.135.238:5000

---

## What is TEC and Why Measure It?
- Total Electron Content (TEC) = number of electrons along path between satellite and receiver  
- Current problem: **unpredictability**  
- Root issue: **lack of observed data**  
- Impact: instability in GNSS communications  
- Solution: increase observed data collection  

---

## Survey of Existing Solutions

| Product | Cost | Drawbacks |
|--------|------|----------|
| HamSci Personal Space Weather Station | $100–1000 | No dual-frequency GNSS |
| Millstone Real-Time TEC Monitor | N/A | Outdated, not flexible, not mobile |
| ScintPi 3.0 | $564 | No storage, no wireless, not purchasable |
| Septentrio PolaRx5TR | $29,000 | Too expensive |

---

## Customer Specifications

### Core Function
- Measure TEC directly  
- Store data reliably  

### Design Requirements
- Affordable (< $1000)  
- Reproducible  
- Fully documented  
- Open-source hardware & software  

---

## Our Solution
A low-cost, self-contained GNSS TEC measurement system with:
- Data storage  
- Remote monitoring  
- Continuous power  
- Expandability  

---

## System Design Tradeoffs

| Component | Options | Final Selection | Reason |
|----------|--------|----------------|-------|
| Antenna | Helical, Choke-ring, Patch | Dual-frequency Patch | Low cost, good coverage |
| RF Processing | SDR, GNSS Module | GNSS Module (u-blox) | Simpler, reliable |
| Processing | MCU, SBC | Raspberry Pi | Handles computation |
| Storage | HDD, SSD, SD, USB | USB Drive (256GB) | Portable |
| Power | AC, Battery, Solar | Hybrid | Flexible |
| Enclosure | 3D Printed, Prefab | Prefab | Durable |

---

## How We Measure TEC (GNSS)
- TEC causes **signal delay**
- Delay affects **pseudo-range**
- Compute TEC from dual-frequency signals  

---

## TEC Calculation (Concept)
- Signals at different frequencies → different delays  
- Difference used to calculate TEC  
- Slant TEC → mapped to vertical TEC (vTEC)  

---

## Data Collection Hardware
- Antenna → receives GNSS signals  
- RF Module → interprets signals  
- SBC → computes TEC  
- USB Drive → stores data  

---

## Data Collection Software

### Data Collection
- UART communication with RF module  
- Collects UBX packets  
- Stores data as CSV  
- Sends to server  

### Packet Types
| Packet | Data |
|--------|------|
| NAV-POSLLH | Position |
| NAV-SAT | Satellite info |
| RXM-RAWX | Raw signal |

---

## Server Software
- Flask-based Wi-Fi server  
- Real-time plots  
- HTML dashboard  

---

## Hardware Design

### System Interconnections
- Central PCB  
- 4-layer board  
- SPI, I2C, UART  
- 5V & 3.3V rails  

---

## Power System
- AC + Battery + Solar  
- LiFePO4 (290Wh)  
- PWM charge controller  
- Continuous operation capable  

---

## Enclosure
Requirements:
- IPX-4 / NEMA 4  
- Thermal dissipation  
- Modular  
- Accessible  

---

## Hardware Implementation

### Enclosure
- PETG used (better heat resistance than PLA)

### PCB
- Mixed assembly  
- Issue: fine-pitch regulator  
- Workaround: buck converter  

### Power
- XT60 connections  
- Stress tested with PSU and load  

---

## Experimental Analysis

### Carrier-to-Noise Ratio
- Avg: **41 dB-Hz**  
- Data below 30 dB-Hz omitted  

---

## Measurement Accuracy

| Metric | Value (TECU) |
|--------|-------------|
| MAE | 18.445 |
| MBE | 18.441 |
| RMS | 18.772 |

- Error is **systematic**  
- Likely due to receiver bias  

---

## Data Logging
- Timestamped TEC values  
- Logs satellite metadata  
- Stores sTEC and vTEC  

---

## Power Performance
- Stable rails  
- Continuous operation  
- Solar can sustain indefinitely  

---

## Field Deployment
- 48-hour continuous operation achieved  
- Tested:
  - Outdoor (no solar)  
  - Car setup  
  - Outdoor (with solar)  

---

## Budget Overview

| Category | Cost |
|---------|------|
| Data & Storage | $183.40 |
| Enclosure | $80.67 |
| Power System | $327.48 |
| PCB | $78.10 |
| Signal Processing | $321.66 |
| **Total** | **$991.31** |

---

## Project Overview
- Successful prototype  
- Accurate trend vs reference data  
- Low cost  
- Portable & replicable  

### Future Work
- Fix bias error  
- Add scintillation measurements  
- Add sensors (LoRa, magnetometer)  

---

## Lessons Learned
- Collaboration matters  
- Avoid overdesign  
- Don’t lock in decisions early  
- Proper testing is critical  
- External factors (tariffs) matter  

---

## Works Cited
[1]–[11] (See original slides for full references)

---

## Statement of Contributions
- Jack Bender – System Interconnections  
- Kenneth Creamer – Power  
- Blake Hudson – Data & Storage  
- Nolan Magee – Introduction & Enclosure  
- Jackson Taylor – RF Module  

---

## Questions?
