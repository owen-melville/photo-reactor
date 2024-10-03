<b><h1>Overview:</b></h1>
This repository contains the STL files and instructions for the assembly of the LEDbyEXAMPLE photoreactor. 

![image](https://github.com/user-attachments/assets/329264f6-ba9a-4603-b425-6119a54de8dd)

Last Updated 2024-10-03 By Owen Alfred Melville, Staff Scientist at the Acceleration Consortium in Toronto. 

<b><h2>Summary of Steps:</b></h2>
  1. Order the required items
  2. 3D Print the required parts
  3. Assemble the photo-reactor
  4. Operate the photo-reactor

<b><h2>Tools Required For This Project:</b></h2>
- Soldering Iron (for electrical connections)
- Heat Gun (for heat-shrink electrical connections)
- Wire cutters
- 3D printer

<b><h2>Skills required For This Project: </b></h2>
- Soldering
- Basic Python coding

<b><h1>Step 1: Order the Required Items: </b></h1>

The majority of the components for this project are electronic. 

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

All the 3D printed parts can be printed with 0.2 mm layer height and a 0.4 mm nozzle. For prototyping or low-temperature reactors, PLA filament can be used. For higher temperatures or shorter wavelength (blue,violet,UV), ASA can be used. Since ASA tends to warp, I recommend using glue stick on the print bed. 

| File Name          | Purpose                  | Printing Considerations      | Number Required         | Customization Potential                 |
| ------------------ | ------------------------ | ---------------------------- | ----------------------- | --------------------------------------- |
| LED_holder.stl     | Holds LED + Heat Sink    | None                         | 1 per LED               |                                         |
| blank_holder.stl   | Blocks Window            | None                         | 1 per unblocked window  |                                         |
| fan_base.stl       | Holds Fan + Magnets      | Supports                     | 1                       | Change inset for larger fan             |
| fan_holder.stl     | Holds Cooling Fan        | Tree supports from base only | Only if cooling desired |                                         |
| reactor_shield.stl | Holds Vial               | Tree supports from base only | 1                       | Change circle diameter for larger vial  |
| screw_base.stl     | Connects reactor to base | None                         | 1                       | Change screw pattern for different base |

![Rotated_Pieces](https://github.com/user-attachments/assets/62d1e7ee-361d-46b5-8baa-6726d720cf07)

<b><h1>Step 3: Assemble the Photoreactor: </b></h1>

The 3D printed parts are modular. When assembled, they should look like this:
![Crop_Reactor](https://github.com/user-attachments/assets/46840458-0334-4217-876d-ce14d960154b)

<b><h2> Step 3a: Assemble the LED Holders </b></h2>

The LED Holder takes the 3D printed insert, and adds in a heat sink and a ~1W LED with attached wires to be controlled by the microcontroller. 

<b>Parts Required:</b>
- LED star
- Wires
- Wire connectors
- 3D Printed LED Holder
- Optional: Solder seal connectors
- Heat sinks

<b>Steps:</b>
  1. Take your LED star, it should have two large soldering pads labelled + and -
  2. Clean the LED star pads using rubbing alcohol (isopropanol) and a tissue
  3. ***Tricky step Alert*** Attach a red wire to the + labelled pad on the right of the star. Wearing temperature resistant gloves, heat up your soldering iron in a well ventilated area. Hold the wire down on the soldering pad carefully with the soldering iron for a few seconds with your dominant hand. Using your non-dominant hand, feed solder to the pad from different directions, allowing it to flow onto the pad. Put away the solder quickly, then use your non-dominant hand to hold down the wire as you carefully remove the soldering iron and replace it in its holder. Allow the solder to cool before you remove your hand. The wire should be encased in solder that has made a strong bind with the pad. If after 2 minutes, gentle pressure on the solder pushes it off the pad, you may need to clean the pad and repeat the process. For tips on this process, see this video (Time Stamp 4:30) https://www.youtube.com/watch?v=H-82av4zQKY&ab_channel=MrTroutDT
  4. Repeat the last process using a black wire and the - labelled pad on the right of the star. Ensure the contact has been well made after completion
***Insert image here of properly soldered wires on LED star***
  5. Remove the adhesive from the heat sink, and slide it into the 3D printed LED holder. Note that the spikes of the heat sink point outwards, towards the thinner side. The flat side of the heat sink should point inwards towards the thinner side.
![crop_heat_sink](https://github.com/user-attachments/assets/7e2b9ade-fd8d-4ce7-9e17-7f89670c8fbd)
  6. Carefully feed the red and black wire through the hole at the bottom of the LED holder. If your wires will not fit, you can use a sharp knife to cut open the channel. As you feed the wires through, you may need to bend them so you can position the LED in a central location on the heat sink.
![crop_star](https://github.com/user-attachments/assets/7373ccb2-6cda-42ff-8504-7082727b10d2)
  7. If you wanted a permanent setup, you could wire these red and black ends straight to your LED board (Step 3c). However, to make them removable/swappable, the wires need connectors. I recommend getting a set of pre-wired connectors with red and black wires at the non-connector end. Take the red wire from your LED and the red wire from the connector, and place them in a solder seal connector so that the bare ends of the wires are touching and under the "solder" of the connector. Use your heat gun to carefully heat up the solder seal connector from different angles. First the plastic will melt, sealing the wires together, then you will see the solder spreading from the central area, which should create a proper connection between the two wires. Let the connection cool. To check that the wiring has been made correctly, you can use a multimeter, comparing the LED pad to the appropriate pin in the connector. Use this youtube video for guidance: https://www.youtube.com/watch?v=bvDk3HzS7lM&ab_channel=SkillBuilder
  8. Repeat the last step to connect the black wires.

<i>Congratulations, you have created your LED holder, which can slide in and out of the photoreactor! You can create as many of these as you have LEDs that you want to use </i>

 
<b><h2> Step 3b: Assemble the Fan Base </b></h2>

<b><h2> Step 3c: (Optional) Assemble the Fan Holder </b></h2>

<b><h2> Step 3c: Assemble the LED Board </b></h2>

<b><h2> Step 3d: Assemble the Fan Board </b></h2>

<b><h2> Step 3e: Combine the Electronics </b></h2>

<b><h1>Step 4: Operate the Photoreactor: </b></h1>
