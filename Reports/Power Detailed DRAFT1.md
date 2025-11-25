# Detailed Design - Power Subsystem
The Power Subsystem is responsible for supplying stable, uninterrupted electrical energy to all operational components of the Total Electron Content (TEC) Measurement Device. Its primary function is to convert, regulate, distribute, and protect the electrical power required by all implemented components  and peripherals. This subsystem ensures that each load receives power at the correct voltage level with minimal electrical noise.

At a high level, the Power Subsystem accepts energy from a 12 V LiFePO₄ rechargeable battery serving as the primary energy reservoir with external charging capability. The charging input  will be able to accept either a 19.5 V DC power supply or a plug-in 12 V rated solar panel. A lithium-compatible charge controller manages these external inputs, maintaining proper charging profiles for the battery while preventing common electrical faults. Once stored in the battery, energy is delivered to the internal power distribution network, where it is converted into regulated 5 V and 3.3 V power rails through high-efficiency buck regulators. These rails power all necessary  components, ensuring that all experience stable voltage conditions even during high-load events.

The subsystem also integrates electrical protection mechanisms, including fuses, transient voltage suppressors, and reverse-polarity diodes. This is necessary in order to shield downstream components from input faults, wiring errors, and environmental disturbances.  Additional filtering elements, such as ferrite beads and low-noise post-regulation stages, maintain signal integrity by reducing switching noise and preventing electromagnetic interference from propagating into noise-sensitive RF circuits. These measures ensure that the GNSS receiver maintains high carrier-to-noise density (C/N₀) and mitigates degradation of measurement accuracy caused by unstable or noisy power rails.

Unlike the one implemented in the ScintPi project, this Power Subsystem enables full autonomy of the TEC measurement device by providing portable, extended runtime capabilities without dependence on fixed AC power [1]. When deployed in the field, the LiFePO₄ battery delivers the energy required for long-duration observation sessions, while the plug-in solar input allows the device to recharge during daylight hours and remain operational for extended or indefinite periods. In laboratory or residential settings, the subsystem seamlessly transitions to AC-powered charging via the 19.5 V DC converter while continuing to power the device in real time.

Overall, the Power Subsystem functions as the foundational infrastructure supporting the reliability, precision, and field portability of the TEC measurement instrument. By ensuring clean, stable, and protected power delivery, the subsystem enables the GNSS processing chain, data acquisition system, and storage module to perform at the accuracy and stability levels required for scientific ionospheric measurements.

## Specifications and Constraints
The Power Subsystem is governed by a set of design constraints that ensure safe, reliable, and continuous operation of the TEC measurement device across all intended environments. These constraints arise from electrical and physical limitations, interactions with other subsystems, battery chemistry requirements, international standards, and socio-economic factors. Together, they define the performance envelope within which this subsystem must operate.

The specifications and rational for each component for the power system are as follows:

1.  This power subsystem shall implement a battery of at least 190Wh of usable energy
> 1.1 - As discussed later in the document, the nominal power draw of all components will be ~8W total, with a theoretical max continuous power draw of 20W [2,  3, 4,  5]
> 1.2 - Assuming at least 230Wh of usable energy, this amount would give a nominal energy life of ~23-24 hours and ~12-13 hours at maximum load, which is within the specified constraints of the conceptual design of 15-hour average usage [6]

2.  This subsystem shall implement a charge controller capable of regulating all current flow to and from the energy storage solution
> 2.1 - As discussed later in this documentation, the use of a LiFePO4 will require a charge controller to be implemented to regulate charge current of the battery [6,  7]
> 2.2 - To follow applicable IEEE and IEC standards discussed in Team 6 conceptual design, a charge controller with appropriate specifications  is  necessary  when using a lithium-based battery [6, 8,  9]

3.  This subsystem shall be capable of recharging energy via 120 VAC adapter input or an optional solar panel input
> 3.1 - As discussed in Team 6’s conceptual design, to achieve mobility this subsystem will make our device capable of recharging in most reasonable conditions to extend operation [6]
> 3.2 - For this device to be modular, the ability to recharge with multiple solutions extend the flexibility and modularity of the device giving the user the ability to  customize their charging solution if desired [6]

To always provide safe operation, the subsystem shall be designed with the following constraints:

1.  The power subsystem shall incorporate proper fusing between all critical components, including the battery, charge controller, and PCB power input
    

> 1.1 - To follow applicable IEEE/IEC standards, proper fusing is necessary for safe operation [8, 9, 10, 11]
> 1.2 - The charge controller manual gives instructions on proper use of the device, including proper fusing parameters of its defined connections [12]
    

2. This subsystem shall incorporate purchased components manufactured with built in fault protection protocols

> 2.1 - To follow applicable IEEE/IEC standards, component  selection will favor those that have built in fault protection protocols.
> 2.2 - The charge controller manages current flow to and from the battery. Therefore, the charge controller should have over voltage, current and reverse current protection protocols [12]
> 2.3 - With a lithium-based battery, the risks associated with them are thermal runaway and short circuit faults. Therefore, this component  should have a built in Battery Management System (BMS) that have over voltage, over current and temperature protections [7]
> 2.4 - The PCB manages all connections and interfaces to all device subsystems. Because of this, there should be components incorporated  to handle common faults such as over voltage, over current and reverse polarity [13]

To Interface with all required components, the power subsystem must follow the following applicable constraints:

1.  The power subsystem shall be capable of delivering at least 25 W continuous output across all rails with a peak capability of ≥ 30  W for transient events
> 1.1 - The nominal power draw of all chosen main components discussed in other subsystems is ~8W, where the max power draw is ~17W. This includes the Raspberry Pi4B, Raspberry Pi Pico, Ublox NEO F9P, Ublox dual tuned patch antenna, USB thumb drive and power dissipated over PCB components [2, 3, 4, 5]
> 1.2 - Due to component boot inrush and transient events, being able to support up to 25W of continuous power will provide enough headroom for these components to properly function
2.  The 5 V rail shall supply at least 3A continuous, supporting the Raspberry Pi 4B, RF module interface boards, USB peripherals, and any future 5 V accessories.
> 2.1 - According to the RaspBerry Pi 4B, in order to support all peripherals, it requires at least  a 3A input at 5V. Therefore, our system shall supply these specifications with enough headroom for additional devices if needed [2]
3.  The 3.3 V rail shall supply at least 1 A continuous, powering the Raspberry Pico, GNSS control logic, level shifters, and digital/analog sensors.
> 3.1 - According to their respective datasheets, all 3.3V based components must be fed proper power specifications due to their sensitive internal components [3, 4]
4.  Regulated rails (5 V, 3.3 V) shall remain within ±5% of nominal voltage under all normal operating load conditions.
> 4.1 - According to the Pi foundations hardware documentation, the Raspberry Pi4B requires a 5.0V input with a tolerance of ±5%. Therefore, this should be supplied to ensure proper functionality [2]
5.  The 5 V and 3.3 V rails shall maintain output ripple < 50 mVpp in the frequency bands that could interfere with GNSS reception, to prevent degradation of RF performance.
> 5.1 - The Raspberry Pi Pico uses the RP2040 MCU, whose recommended operating voltage is 3.3 V ±10%, however stable operation and peripheral accuracy rely on tighter regulation (< ±5%). The RP2040 datasheet notes I/O characteristics and ADC accuracy degrade when VDD exceeds recommended limits. Thus, ±5% ensures full ADC accuracy and digital timing integrity [3]
> 4.2 - The U-blox M8/M9 GNSS Hardware Integration Guide states that the ripple on the supply must be less than 50 mVpp. Switching power supplies must be carefully filtered to avoid degrading GNSS sensitivity [4]

## Overview of Proposed Solution
The power subsystem for Team 6’s TEC measurement device is implemented as a hybrid AC/Solar capable rechargeable architecture built around a 12 V-class LiFePO₄ battery, a 20A PWM charge controller, a 200W 19.5 V XT60 AC power supply, an optional 100 W 12 V solar panel. A central PCB is implemented that provides low-voltage rails for the Raspberry Pi 4B, Raspberry Pi Pico, u-blox NEO-F9P module, and supporting electronics. Below is the comprehensive power budget for all components this subsystem needs to provide.

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
1.  Energy is stored in a 12.8 V LiFePO₄ battery sized to provide ≥ 190 Wh usable capacity.
2.  Storage solution can recharge from either a 120 VAC to 19.5 V DC XT60 power supply or an optional 100 W 12 V solar panel.
3.  All charge and discharge currents are managed through a 20A rated  LiFePO₄-compatible PWM charge controller.
4.  Energy is distributed through the central PCB, which provides tightly regulated 5 V and 3.3 V rails with low ripple for the processing and RF components.
5.  Layered protection and fusing is implemented that satisfies IEEE/IEC safety expectations and mitigates hazards associated with lithium-based storage.

**Battery Component**: For Team 6’s functional prototype, we have chosen the ZapLitho 12 V 22 Ah with a 30 A BMS [7].The integrated Battery Management System (BMS) provides over-charge, over-discharge, over-current, and over-temperature protections, satisfying the constraint that lithium storage must include internal fault mitigation to reduce thermal-runaway and short-circuit risk.

Assuming 85–90 % usable depth-of-discharge to preserve cycle life, this component  advertises 240Wh of usable energy, which is  ≥ 190 Wh  satisfying the subsystem specification. At a nominal system draw of ≈ 8 W and a theoretical  maximum continuous draw of ≈17 W, the system runtime equates to  23.7 hours and 12.7 hours respectively. These values meet the conceptual design requirement for ~15 hours of average usage while still reserving margin to protect the battery from deep discharge.
**BATTERY IMG**
Figure 1: ZapLitho 12V 22Ah Battery with BMS

**Charge Controller Component**: For a charge controller, Team 6 has chosen to implement the Limu Solar LTB Series 20A PWM Solar Charge Controller for our functional prototype [12]. This device supports LiFePO₄, lithium  chemistries, uses a three-stage PWM charging algorithm, and accepts solar inputs up to 50 V while managing a 20 A battery charge and load current.

The controller’s battery terminals connect directly to the LiFePO₄ pack, and its load terminals feed the 12 V bus that supplies the PCB and any future 12 V accessories. The specific connector scheme and wiring gauge for these interfaces will be defined in a later section of the detailed design.
**CHARGE CONT IMG**
Figure 2: Charge Controller (20A, 12/24V)

**DC Power Supply Component**: For mains charging of Team 6’s functional prototype, we have decided to use the SUPULSE 200 W AC power adapter with 19.5 V, 10.3 A DC output and an XT60 connector  [14].  This supply is designed for RC LiPo charging, and its 19.5 V DC output falls directly within the PV input range of the solar charge controller, allowing it to be treated as a “synthetic solar panel” when plugged into the controller’s PV terminals.
**PSU IMG**
Figure 3: XT60 AC/DC Power Supply (19.5V, 10.3A, 200W)

**Solar Panel Component**: This subsystem gives the user the ability to charge the device through two means of charging. The ability to charge the device via solar panel is given by the selected PWM charge controller above.

For our functional prototype, Team 6 has selected the Rvpozwer 18BB 100-Watt Solar Panel [15]. This is a 12 V monocrystalline N-type panel with 18-busbar cells and claimed module efficiency up to 25%. The panel is mechanically compact at roughly 40 in × 18 in and weighs about 6 kg, with an anodized aluminum frame and tempered glass front. The components advertised specifications and price were among the best compared to other options offered by the distributor. This component is also within the specified price given in the conceptual design [6].
**SOLAR PANEL IMG**
Figure 4: N-Type Monocrystalline 18BB 100W 12V Solar Panel

**PCB Power Rail Components**: The PCB power section provides the final stage of regulated, protected, and selectable power for all digital and RF subsystems, using a combination of the TPS2121 Power Multiplexer, TPS62913 Buck Converters, board-level filtering components, and two user-selectable input connectors. This portion of the subsystem is designed to meet the system’s constraints on modularity, ripple performance, voltage stability, and safety, without requiring the reader to understand the low-level circuit mechanisms.
The board supports two power-entry options:

1.  12 V Barrel Jack Input (CUI Devices PJ-063AH Barrel Jack) [16]
    

2.  5 V USB-C Input (Abra CON-USB-C-CL 5A Power Connector) [17]
    

The PCB includes a barrel-jack input rated for up to 24 VDC and 8 A. This input is protected by a bidirectional polyfuse with a 1.5 A hold and 3 A trip rating, satisfying the project requirement for upstream overcurrent protection between critical components [18]. A bidirectional TVS diode (SMBJ15CA) with a 15 V reverse standoff, 16.7 V breakdown voltage, and 24.4 V clamping voltage is placed across the input, and four SS32 Schottky diodes (20 V, 3 A) are arranged in a full-bridge configuration to ensure correct polarity regardless of how the barrel connector is wired. Together, these components protect the system by clamping surges, preventing reverse-polarity faults, and limiting over-voltage excursions at the input [19], while the Schottky diodes provide the advantage of low forward voltage and reduced thermal dissipation [20]. Additional smoothing capacitors filter the rectified input, enabling the barrel jack to operate as a universal DC plug-in interface.

The protected 12V input is stepped down to 5V using a TPS62913 synchronous buck converter. The TPS6291x family provides high efficiency, low output ripple, and low noise switching performance appropriate for RF-sensitive designs [21]. In this design, VIN is tied to EN and S-CONFIG, which selects a 2.2 MHz switching frequency; the recommended 470 nF capacitor sets up a 5ms soft-start timing. The PSNS pin is tied to ground to disable current-sense reporting. The PG pin is unused and left floating per datasheet guidance. A 2.2 µH inductor is selected as required for outputs above 3.3 V when switching at 2.2 MHz, and the SW node is routed with proper filtering to reduce switch-node ringing. Voltage regulation is achieved using the device’s 0.8 V reference via a resistive divider, designed per datasheet recommendations. All external components follow TI’s reference design values [21]. The resulting 5 V rail then supplies the Raspberry Pi 4B, RF modules, and USB storage devices.

The regulated 5 V output feeds the TPS2121 power multiplexer, which also receives the USB-C input through its independent channel. A resistive divider sets the CP2 pin to 2 V. The TPS212x family supports Dual-Input, Single-Output (DISO) multiplexing and provides automatic detection, prioritization, and seamless source transition between the available power inputs [22]. Prioritization is established by raising PR1 above CP2; in this design, PR1 receives 4 V from the USB-C path, ensuring that USB-C is selected whenever both sources are present. Section 7.5 of the TPS2121 datasheet specifies a 29.8 kΩ resistor on ILIM for a typical 3.5 A output limit. A 1 µF capacitor on the SS pin sets an 88 V/s output slew rate, defining a controlled soft start. OV pins are not used and tied to the ground. This configuration satisfies system modularity requirements by enabling automatic selection between LiFePO₄ battery power and USB-C external power.

A second TPS62913 buck converter then generates the regulated 3.3 V rail for the Raspberry Pi Pico, GNSS control logic, sensors, and level shifters. Both buck stages use TI-recommended LC networks and filtering, which reduces conducted noise, switching ripple, and high-frequency transients. This configuration ensures the design meets the system’s strict ripple constraints, particularly those required for GNSS receiver performance. A figure later in this document illustrates the expected ripple based on the manufacturer’s recommended filtering network [21].

**RIPPLE GRAPH IMG**
Figure 5: 5-3.3V Ripple and Ripple FFT after all filtering [21]

For users wishing to run the device directly from USB-C power, the PCB includes the Abra CON-USB-C-CL connector [17], capable of supporting 20 VDC at 3 A. Two 5.1 kΩ pull-down resistors on CC1 and CC2 establish proper sink-side CC negotiation. The VBUS path is protected with a 3 A/5 A-trip polyfuse, followed by a USB-side TVS diode (5 V standoff, 6.4 V breakdown, 9.2 V clamp). The smoothed VBUS feed is then routed into the TPS2121 multiplexer, with a local voltage divider providing the 4 V PR1 signal to establish USB-priority.

The TPS2121 automatically switches between the 5 V derived from the 12 V battery and the 5 V supplied via USB-C, ensuring seamless transitions and maximizing battery longevity. This behavior aligns with system requirements for reliability, modularity, and field flexibility. Together, the PCB power architecture acts as the final regulated interface between the energy subsystem and the low-voltage electronics, providing stable 5 V and 3.3 V rails with low ripple, integrated protection against surges and reverse polarity, and compliance with IEEE/IEC expectations for safe power delivery. Overall, this stage ensures robust, low-noise, and reliable power for all downstream subsystems.

The PCB power section acts as the final interface between the main battery/charger system and all low-voltage electronics, ensuring devices receive clean, stable power. The two buck converters generate low-noise 5 V and 3.3 V rails required by the Pi, Pico, and GNSS module, meeting the system’s voltage-regulation and ripple constraints. Integrated protection elements provide overcurrent, surge, and reverse-polarity safety consistent with IEEE/IEC constraints. Overall, this design stage ensures reliable, low-ripple power delivery to all subsystems.

**For more information on the PCB  component configuration  and topology within this subsystem, see Team 6’s detailed design of the PCB interconnections  by Jack Bender** [13].

## High-Level Flowchart & Buildable Schematic
Below is a rough schematic of the PCB layout for the distribution of power rails, filtering, and external input. A table of all devices below clarifies specific components within this schematic, to a reference to their specific datasheet.
**PCB SCHEMATIC IMG**
Figure 6: PCB Power Schematic [13]

| Component | Schematic Symbol | Datasheet Link |
| --- | --- | --- |
| PJ-063AH Barrel Jack | J3 | https://www.sameskydevices.com/product/resource/pj-063ah.pdf |
| UJC-HP2-3-SMT-TR USBC | J1 | https://www.sameskydevices.com/product/resource/ujc-hp2-3-smt-tr.pdf |
| Bel Fuse 0ZCG0150BF2C 3A, 5A Hold, 3A Trip PTC Fuse | F2 | https://www.belfuse.com/media/datasheets/products/circuit-protection/ds-cp-0zcg-series.pdf |
| YEGEO SMD2920B300TF/15 3A Hold, 5A trip PTC Fuse | F1 | https://www.yageogroup.com/content/Resource%20Library/Datasheet/SMD2920_1.pdf |
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

**HIGH LEVEL FLOWCHART IMG**
Figure 5: High Level Power Subsystem Flowchart

## Bill Of Materials
Below is a comprehensive list of all necessary  components apart  of this subsystem. All components are listed with their manufacturer, part number, quantity, price, and purchasing URL. Note that the nature of the power subsystem specifically extends into the Interfacing/PCB subsystem [13].

Therefore, some components may also be reflected in that respective detailed design document. Therefore, the price of these components shall be obviously reflected in the bill of materials as Total price of MAIN components and total price of ALL components, which include the main components plus components used for the PCB integration. At the end of this table, both main and all components of pre-tax and post-tax total cost are reflected respectively. The United States of Tennessee average state and federal tax rates in the year of 2025  were taken into consideration for post-tax calculations. Delivery and packaging costs were not reflected in this bill of materials.

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
| PWM Charge Controller (20A, 12/24V) | https://www.amazon.com/gp/product/B08L39D2NY/ |
| LiFePO4 Battery (22Ah, 12V) | www.amazon.com/gp/product/B0F1FRBMG3/ |
| MC4 to XT60 FEMALE Adapter | https://www.amazon.com/gp/product/B08L39D2NY/ |
| 12 AWG Black/Red Wire | www.amazon.com/gp/product/B0D12VYLGV/ |
| 10 Pair XT60H Bullet Connectors | https://www.amazon.com/gp/product/B07Q2SJSZ1/ |
| 2Pack 16AWG Barrel Jack Connectors | https://www.amazon.com/gp/product/B0BLYMVWNP/ |
| 4 Pack 12AWG Inline Fuse Holder w/ Fuses | https://www.amazon.com/Anyongora-Inline-Waterproof-Automotive-Standard/dp/B0CL7MLY6T/ |
| XT60 to O ring Connector | www.amazon.com/gp/product/B0F1FRBMG3/ |
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

Team 6 also realized that the need for a LiFePO4 battery is needed for our design, since energy  efficiency, charge rate, and weight to energy storage ratio are essential variables to choosing  a battery. This also required us to get a larger battery than we originally planned to implement, since we originally did not account for energy storage headroom to not discharge the battery fully. This decision finally snowballed into needing to purchase a more capable power supply than originally intended for which increased cost. Team 6 also does not account for sales taxation when budgeting all components.

Therefore, the total price for ALL COMPONENTS is estimated to be $316.83. This puts this subsystem over budget by $54.87. Analyzing this price point, by eliminating the optional solar panel and adapter, this would put this subsystem withing Team 6’s allocated budget.

## Analysis of Solution
**Energy Storage**: The energy storage component has been chosen to be a nominal 12.8 V LiFePO₄ pack with 22Ah capacity providing roughly 240-280  Wh nameplate capacity and > 4,000 charge cycles. The reasoning behind the choice of a lithium-based battery chemistry is the following.

1.  High cycle life providing an average of 3,000+ deep cycles
    

2.  Stable voltage plateau around 12.8–13.2 V, which is ideal for 12 V-class DC/DC converters
    

3.  Inherently safer behavior and better thermal stability than other lithium chemistries, which aligns with IEEE/IEC safety considerations discussed in the conceptual design.
    

LiFePO₄ chemistry provides better cycle life capacity that other battery chemistries such as lead acid. It also provides great energy to weight ratio which is ideal for a portable device solution. Phosphate-based chemistry does make this choice worse than Lithium-Ion or LiPo based batteries. However, it is less prone to dangerous reactions in the event of electrical failure. Since this system will run for prolonged periods of time unattended, this is an important consideration when choosing between battery chemistries.

**Charge Controller**: As discussed earlier in this document, all current flowing into or out of the battery is routed through an acceptable 20A 12V PWM charge controller. This device supports LiFePO₄, lithium chemistries, uses a three-stage PWM charging algorithm, and accepts solar inputs while managing a 20A maximum battery charge and load current. Below is an overview of the charge controller's functionality.

1.  Regulates current to and from the battery based on measured battery conditions
    

2.  Switches between Bulk / absorption / float stages tailored to LiFePO₄ charge voltages
    

3.  Detects system voltage automatically and constant monitoring of charge and load currents
    

4.  Provides integrated protections such as over-voltage, over-current, short-circuit, reverse connection, and reverse current blocking
    

By interposing this controller between both charging sources and the battery, the subsystem enforces the constraint that all current flow to and from the energy storage solution shall be regulated. It also aligns with conceptual-design guidance that a LiFePO₄-based system must incorporate a dedicated charge controller to meet IEEE/IEC safety practices. Providing integrated fault protections, this device satisfies applicable constraints.

**DC Power Supply (AC Adapter)**: The AC-to-DC power supply serves as the primary charging option for the subsystem, enabling users to recharge the LiFePO₄ battery in situations where solar availability is limited or when fast turnaround is needed. By converting 120 VAC mains into a regulated 19.5 V DC output, the adapter provides an electrical input that behaves similarly to a fixed-voltage 12 V-class solar panel when connected to the PWM charge controller. The adapter remains a power source  only, the charge controller continues to regulate all charging behavior. This ensures full compatibility with LiFePO₄ charging requirements and maintains compliance with subsystem constraints regarding regulated current flow into the battery.

Below is an overview of how the AC adapter meets functional and safety requirements:

1.  Provides a stable 19.5 V DC output within the acceptable PV-input voltage range of the 20 A PWM controller
    

2.  Behaves electrically like a fixed-voltage DC source, which PWM controllers are designed to accept without requiring solar-specific I–V curve characteristics
    

3.  Delivers up to ~200 W, remaining safely below the charge controller's input power rating
    

4.  Chosen component is designed for pulsed, rapid-load environments (RC battery chargers), making it tolerant of PWM switching behavior
    

5.  Implementation commonly used in industry and laboratory environments as a stand-in for solar panels during testing, system evaluation, or indoor charging scenarios
    

Because a PWM controller regulates charging by rapidly connecting and disconnecting the PV input, it does not rely on the non-linear solar I–V curve that MPPT controllers require. Thus, a constant-voltage adapter is fully compatible as long as it remains within PV-input specifications. The charge controller continues to manage bulk, absorption, and float stages according to LiFePO₄ requirements, while the adapter simply provides the DC energy needed.

Safety concerns are mitigated through several layers of protection. The charge controller includes PV-side and battery-side protections such as reverse-polarity, over-voltage, over-current, and short-circuit safeguarding. The LiFePO₄ battery’s integrated BMS provides cell-level protections including over-charge, over-discharge, over-current, and thermal limits. At the system level, additional fusing protects both the adapter path and battery path. Together, these measures ensure that no unregulated or unsafe current path exists from the AC mains to the battery.

Finally, the adapter’s XT60 output integrates cleanly into the subsystem’s modular design. The XT60 interface allows users to easily swap between solar input, the AC adapter, or laboratory bench supplies without modifying internal electronics. With its 19.5 V, 10.3 A output, the adapter can recharge the system rapidly, typically within 1.5–2 hours, while fully aligning with all design constraints for safe, efficient battery charging.

**Solar Panel**:  The chosen panel construction also offers advantages over competing low-cost alternatives. The monocrystalline N-type cells and multi-bus-bar structure used in this model are typically associated with higher conversion efficiencies and improved shade tolerance compared to older polycrystalline or 5-bus-bar panels. This improves energy yield per unit area and enhances real-world performance when irradiance is variable in conditions that directly affect GNSS measurements. The panel’s physical design, including a tempered-glass front and aluminum frame, aligns with outdoor durability expectations while remaining light enough to be carried, mounted, or stowed easily. It also uses standard MC4 connectors, which simplifies integration with the rest of the power subsystem and supports modular field setup with extension cables, folding configurations, or parallel/series arrangements for future scalability.

A more exotic panel such as flexible copper-indium-gallium selenide structures, foldable camping panels, or bifacial glass modules could increase cost or complexity without delivering proportional benefit to the system’s energy budget. The chosen monocrystalline panel has a tradeoff giving us high enough power to reliably recharge the system, physically manageable for field deployments, electrically compatible with the selected controller and battery, robust enough for repeated use, and economically appropriate for both academia and future replication outside the lab environment.

Because this component is a functional option of Team 6’s design, this component has been placed as least priority, since the core operation of this subsystem can still function without this component. AC wall charging is also more convenient than Solar charging and therefore will be implemented first in the case that team 6 is unable to implement this component.

**PCB Implementation**: The PCB power stage successfully implements the project’s requirements by providing clean, protected, and modular low-voltage power distribution. The design meets all electrical specifications by delivering regulated 5 V and 3.3 V rails within ±5% tolerance and maintaining ripple well below the <50 mVpp constraint using low-noise buck converters and appropriate LC filtering. Each rail is sized with a comfortable current margin, exceeding the required continuous and peak loads for all implemented devices.

The PCB also satisfies protection requirements through layered safeguarding: polyfuses, TVS diodes, and Schottky rectification at the input; current-limited power multiplexing; and the inherent protections within the voltage regulators. This ensures compliance with constraints calling for safe operation, prevention of reverse-polarity faults, and adherence to IEEE/IEC-aligned practices  mentioned in the conceptual design. Modularity constraints are equally fulfilled through the TPS2121 power MUX, which enables seamless source selection between USB-C and battery-derived 5 V, supporting a transparent and user-friendly operating model.

Overall, the PCB implementation provides stable, low-noise, fault-tolerant power routing that satisfies the subsystem’s performance, safety, and modularity constraints without unnecessary complexity.

**High Level Solution**: At the broader system level, the power architecture meets all functional requirements for runtime, flexibility, and safe battery management. The selected LiFePO₄ pack provides ≥190 Wh of usable energy, exceeding the 15-hour operational requirement under the nominal 8–9 W load and still meeting conservative expectations under peak demand. All charging and discharging activity is routed through the 20 A PWM charge controller, satisfying the constraint that all battery current must be regulated and that lithium chemistries must use a dedicated management device.

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
