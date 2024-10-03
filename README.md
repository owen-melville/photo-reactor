<b><h1>Overview:</b></h1>
This repository contains the STL files and instructions for the assembly of the LEDbyEXAMPLE photoreactor. 

![image](https://github.com/user-attachments/assets/329264f6-ba9a-4603-b425-6119a54de8dd)

Last Updated 2024-10-03 By Owen Melville

<b><h2>Summary of Steps:</b></h2>
  1. Order the required items
  2. 3D Print the required parts
  3. Assemble the photo-reactor

<b><h2>Tools Required For This Project:</b></h2>
- Soldering Iron (for electrical connections)
- Heat Gun (for heat-shrink electrical connections)
- Wire cutters
- 3D printer

<b><h2>Skills required For This Project: </b></h2>
- Soldering
- Basic Python coding

<b><h1>Step 1: Order the Required Items: </b></h1>

The majority of the components for this project are electronic. In order to obtain 

<b><h2>Materials Required:</b></h2>

These materials are required for the photoreactor. You would need to purchase more to make additional photoreactors. 

| Item                             | Supplier | Part number                   | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Number | Cost  | Total Cost |
| -------------------------------- | -------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- | ---------- |
| Raspberry Pi Pico WH             | PiShop   | 402-1                         | https://www.pishop.ca/product/raspberry-pi-pico-wh-pre-soldered-headers/                                                                                                                                                                                                                                                                                                                                                                                                                             | 1      | 9.8   | 9.8        |
| Grove Shield for Pico            | Digikey  | 1597-103100142-ND             | https://www.digikey.ca/en/products/detail/seeed-technology-co-ltd/103100142/13688265?s=N4IgTCBcDaIIwFYCcB2AtHADAZi5uALGGgHIAiIAugL5A | 1      | 6.25  | 6.25       |
| Fan Control Board                | Digikey  | 1528-4808-ND                  | https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4808/13590573?s=N4IgTCBcDaIIwFYwA4C0AWZAGNA5AIiALoC%2BQA                                                                                                                                                                                                                                                                                        | 2      | 7.99  | 15.98      |
| Square Fan (20mm Diameter)       | Digikey  | 2223-CFM-2006CF-060-078-22-ND | https://www.digikey.ca/en/products/detail/cui-devices/CFM-2006CF-060-078-22/19524716?s=N4IgTCBcDa5mBmAtAYQGIFkkAIwAY8A2dJIvHPAdgA4l4kA5AERAF0BfIA                                                                                                                                                                                                                                                                                                                                                    | 2      | 11.06 | 22.12      |
| Grove to Fan Board Connectors    | Digikey  | 1528-4528-ND                  | [https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4528/11627737?s=N4IgTCBcDaIIwFYwA4C0AWJaByAREAugL5A](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4528/11627737?s=N4IgTCBcDaIIwFYwA4C0AWJaByAREAugL5A)                                                                                                                                                                                                                                                       | 2      | 2.83  | 5.66       |
| Usb B Micro B Circuit board      | Digikey  | 1528-1383-ND                  | https://www.digikey.ca/en/products/detail/adafruit-industries-llc/1833/5629431?s=N4IgTCBcDaIK4GcBGACVBbAlgYwE4Hs018BDXAExRPJIDNc5MAXEAXQF8g                                                                                                                                                                                                                                                                                                                                                          | 1      | 2.83  | 2.83       |
| Usb B Micro B to Usb A cable     | Digikey  | 2987-DH-20M50057-ND           | https://www.digikey.ca/en/products/detail/cvilux-usa/DH-20M50057/13177527                                                                                                                                                                                                                                                                                                                                                                                                                            | 2      | 1.78  | 3.56       |
| LED Stars (Green)                | Digikey  | LST1-01H06-GRN1-01            | https://www.digikey.ca/en/products/detail/new-energy/LST1-01H06-GRN1-01/10663110?s=N4IgTCBcDaIDIGUAqBGAtABhQCQwNjQHEAlAOXSxAF0BfIA                                                                                                                                                                                                                                                                                                                                                                   | 2      | 6.41  | 12.82      |
| NPN Transistor                   | Digikey  | 1727-4252-1-ND                | https://www.digikey.ca/en/products/detail/nexperia-usa-inc/PZT2222A-115/1158011?s=N4IgTCBcDaIIwHYwILQBYwFYwrigBAHIAiIAugL5A                                                                                                                                                                                                                                                                                                                                                                          | 2      | 0.56  | 1.12       |
| Total Cost (CAD) | $80.14

<b><h2>Materials Required - Kits:</b></h2>

These materials come in kits, so you may not need them if you already have similar materials. They can be used for multiple reactors or other projects. 

| Item                             | Supplier | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Cost  |
| -------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Prototype PCB Board              | Amazon   | https://www.amazon.ca/BOJACK-6-Prototype-Soldering-Compatible-Arduino/dp/B091PZQ4W7/                                          | 21.99 |
| Nyodenium Magnets 6mm x 2mm      | Amazon   | https://www.amazon.ca/Magnets-Refrigertor-Whiteboard-Durable-Multi-Use/dp/B07BJFD6FL/ | 9.99  |
| Heat Sinks                       | Amazon   | https://www.amazon.ca/Awxlumv-Heatsink-25-x25-x10/dp/B08CMK8BMT/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10.99 |
| Resistors                        | Amazon   | https://www.amazon.ca/Resistor-Assorted-Resistors-Assortment-Experiments/dp/B07L851T3V/?th=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 17.99 |
| Optional: Solder Seal Connectors | Amazon   | https://www.amazon.ca/Kuject-Connectors-Waterproof-Electrical-Automotive/dp/B073RMRCC3/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 16.99 |
| Optional: Electrical Connectors  | Amazon   | https://www.amazon.ca/1-25mm-Connectors-Pre-Crimped-Pixhawk-Silicone/dp/B07S18D3RN/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 21.99 |
| Total Cost (CAD) | $99.94 |

<b><h2>Generic Materials Required</b></h2>
  - Wires
  - Solder
  - Filament for 3D printing

<b><h1>Step 2: 3D Print the Parts: </b></h1>
