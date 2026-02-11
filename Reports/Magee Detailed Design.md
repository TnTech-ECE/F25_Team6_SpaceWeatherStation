****Detailed Design****

***Function of the Subsystem***

The function of the subsystem is explained in the following shall statements

- The subsystem shall enclose and secure all other subsystems by providing protection and structure for easy accessibility and intuitive field implementation.
- The enclosure shall provide adequate heat dissipation, allowing the prototype to be properly cooled for consistent operation.
- The enclosure shall provide a robust waterproof case capable of withstanding insects and weather conditions within reason.
- The enclosure shall secure all components during transportation and implementation.
- The design shall provide accessibility for troubleshooting and repairing every component.

***Specifications and Constraints***

The following shall statements comprise the constraints and specifications of the enclosure.

- The enclosure shall be protected against splashing water from any angle for broad field applications (IPX-4 waterproof rating at a minimum). \[IEC 60529-2020\][1]
- The enclosure shall maintain appropriate temperatures to prevent the internal subsystems from overheating.
- The enclosure shall implement waterproof grommets or liquid sealtight fittings at every point of exterior penetration to create a consistent seal.
- The enclosure shall include a small drain hole through the bottom of the enclosure to prevent water from being trapped inside the enclosure.
- The enclosure shall hinder insects from accessing the interior by protecting any exterior penetration.
- The enclosure shall be made of a NEMA 4 rated enclosure ensuring proper protection for indoor and outdoor use. Resilient to weather, abrasions, and general deterioration. \[ANSI/NEMA 250-2020\][2]
- The enclosure shall have a transparent barrier for viewing all internal components for observation during operation.
- The enclosure shall allow for easy access for interchanging parts to promote modularity and flexibility in field and home applications.
- All components shall be secured using appropriately sized screws for sustainable mounting.
- All 3-D printed parts shall be made of PETG.

***Overview of Proposed Solution***

&nbsp;&nbsp;&nbsp;&nbsp;Team 6 proposes the Gratury 16.1" x 12.2" x 7.1" water-resistant outdoor enclosure box as the chosen enclosure. The box shall maintain a rating of IP55 and NEMA 4, exceeding the required waterproof rating and providing durability and protection in rugged environments. The system shall produce 20.65 W at max load (4 W/ft^2) and 8 W at nominal load (1.6 W/ft^2). Using the sealed enclosure temperature rise chart, the enclosure shall satisfy heat regulation requirements by passively removing heat from the enclosure through the Acrylonitrile Butadiene Styrene (ABS) enclosure. [3] The enclosure has a transparent front cover for internal observation during operation. The enclosure uses 304 stainless steel latches, enabling easy access to the internal components and providing a solution which will remain rust free through repeated outdoor exposure. All hardware and components shall be mounted using M4 screws, excluding the PCB (M2) and the GPS module (M3). The battery shall be secured by installing corner brackets (figure 2) above the top right and top left corners of the battery, creating a secure vertical fit. To secure the front and sides of the battery, a large u-bracket (figure 3) shall be installed.

![81I+3fD0CeL._AC_SL1500_](https://hackmd.io/_uploads/Hy4GOCeWbe.jpg)
**Figure 1. Full View of Proposed Enclosure**


<img width="800" height="600" alt="Corner_Supports_V02" src="https://github.com/user-attachments/assets/691652df-bdd7-48bb-b9d9-4769b91831ca" />

**Figure 2. 31x22x19mm Corner Bracket**

<img width="1180" height="568" alt="Screenshot 2026-02-02 141046" src="https://github.com/user-attachments/assets/54e23df9-0cf9-4238-aa52-f65842566deb" />

**Figure 3. 7.1"x3"x3" U-Bracket**

***Buildable Schematic***

![710B15JyV2L._AC_SL1500_](https://hackmd.io/_uploads/rJNC9QW-bl.jpg)
**Figure 5. Exterior Dimensional View**

![Screenshot 2025-11-23 185257](https://hackmd.io/_uploads/Hkqdhm-W-g.png)

**Figure 6. Internal Component Layout**

***BOM***

| **Component** | **Enclosure Box** | **Wire Mesh Vents** | **Liquid Seal Tight ½" fitting** | **1/2" Liquid Seal Tight Ferrule** | **Fastener Kit** |
| --- | --- | --- | --- | --- | --- |
| **Manufacturer** | **Gratury** | **Phoenix Contact** | **Phoenix Contact** | **Hilitchi** |
| **Part Number** | **772467660195** | **1411153-ND** | **1411233-ND** | **‎H-M345-510** |
| **Distributor** | **Amazon** | **DigiKey** | **DigiKey** | **Amazon** |
| **Distributor Part Number** | **B0BCVGHF1J** | **1411153** | **1411233** | **‎B073SW4S6C** |
| **Quantity** | **1** | **1** | **1** | **1** | **1** |
| **Purchasing Website URL** | [4] | [6] | [7] | [8] |
| **Total** | **66.99** | **1.63** | **0.46** | **11.59** |
| **Grand Total** | **80.67** |

***Analysis***

&nbsp;&nbsp;&nbsp;&nbsp;Team 6 has concluded the Gratury 16.1" x 12.2" x 7.1" water-resistant outdoor enclosure box is the optimal solution for the needs of the TEC measurement prototype. This enclosure exceeds the minimum required IPX-4 waterproof rating. Air vents will need to be added to meet the system's ventilation needs, which will decrease the waterproof rating to IP54 and NEMA 3R. The vents included will be 4" x 4" with slats covering the exterior to deter water entry into the enclosure. The vents being a perfect square allow for the enclosure to be set up in a vertical or horizontal orientation, allowing users the flexibility of mounting to a wall, strapping to a tree, or simply lying flat on the ground. The enclosure is large enough to properly space components for ease of physical access, while leaving room for additional components, encouraging adaptability and modularity (as shown in figure 6). The orientation and spacing has been chosen to allow room for proper heat dissipation and creating the shortest distance for wire connections between devices. The internal back plate is removable, allowing the user to easily transfer the entire component platform in and out of the box, facilitating speed and convenience. The grid design of the backplate accepts a large size variation in fasteners, removing the annoyance of requiring uniform hardware. This will also encourage experimentation and additions to the minimal function of the prototype. Team 6 had the intention of mounting a small transparent faceplate to the chosen enclosure. However, this enclosure's entire latched door is transparent, allowing viewing of the complete interior of the enclosure. The door utilizing stainless steel latches satisfied the requirement for easy access to the internal components without sacrificing sturdiness. Overall, this enclosure exceeds expectations in every regard, and while this specific box may not be accessible anywhere in the world, it exemplifies the characteristics of any enclosure a hobbyist may want to use in their own application.

***References***

\[1\] <https://www.nema.org/docs/default-source/about-us-document-library/ansi-iec_60529-2020-contents-and-scopef0908377-f8db-4395-8aaa-97331d276fef.pdf?sfvrsn=29c118a6_3>

\[2\] <https://www.nema.org/docs/default-source/standards-document-library/ansi_nema_250-2020-contents-and-scope76f809d7-afad-4aa1-80cd-e1d09b60f2e5.pdf?sfvrsn=cb4086bd_3>

\[3\] <https://www.polycase.com/techtalk/aluminum-enclosures/how-to-calculate-temperature-rise-inside-enclosures-2.html>

\[4\]  <[<https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B08282VRXW/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1>](https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B0BCVGHF1J/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1)](https://www.amazon.com/Gratury-Transparent-Waterproof-Electrical-290%C3%97190%C3%97140mm/dp/B0BCVGHF1J/ref=sr_1_32?crid=2AIQZLKKD6YO2&dib=eyJ2IjoiMSJ9.5yFO9ykv_jtUwHfG9E-ClJoPNtKzNKLnhCSUHgm0RCwWiDU8nU5PfSYJsAad4dnjqMME9QKA0E33tPX7sHr7KUIIhV23ihhWDIYhTeLSZTqMnIJ1sVyavnSMrqpOnNoCJP44ckrF24ZifCbY80OvjskAQksd3M51foSfKY9pdMN9HBfCu-Xo4lL_1yaD9UNCE_lG4uGlp-aGB6imXn_5cSfQhR0E1XsmTkEHw1lvN2MqiYZ4ud8f0aAc-ruMJ6w0Ees8lgQIMX39ri3Kyp1IIHkqKowMHdap-KHpsj0Kvzg.2z8UVhXIVgwiyfXMLGwNaK7EvuCaY6AN3g6fdFEA4Q8&dib_tag=se&keywords=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvented&nsdOptOutParam=true&qid=1763677894&sprefix=joinfworld%2Boutdoor%2Bwifi%2Benclosure%2Bwith%2Btransparent%2Bcover%2Bvente%2Caps%2C90&sr=8-32&th=1)>

\[5\] <https://www.digikey.com/en/products/detail/phoenix-contact/1411153/5188749?gclsrc=aw.ds&gad_source=1&gad_campaignid=17336967819&gbraid=0AAAAADrbLlioVAEPkwSrWuIyQJqISDpQu&gclid=CjwKCAiAuIDJBhBoEiwAxhgyFogJXM6Pct3Bt6_00QRIS_GeVxmJupNwJiNd-5xfBqYYcaVc0cQjCRoCi-MQAvD_BwE>

\[6\] <https://www.digikey.com/en/products/detail/phoenix-contact/1411233/5186528>

\[7\] <https://www.amazon.com/Hilitchi-510pcs-Stainless-Socket-Assortment/dp/B073SW4S6C/ref=asc_df_B073SW4S6C?tag=bingshoppinga-20&linkCode=df0&hvadid=80539418193264&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=84181&hvtargid=pla-4584138888772003&msclkid=f9ab892a8825176c7cf5e057986c6775&th=1>
