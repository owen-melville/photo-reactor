<img src="https://github.com/user-attachments/assets/ff46246e-549c-4888-8031-985b907012fd" width="600"/>

<b><h1>Overview:</b></h1>
This repository contains the instructions/code/files for the assembly and operation of the LEDbyXample photoreactor. LEDbyXample is designed for automation and self-driving labs (SDLs), like those at the Acceleration Consortium in Toronto. Although it is designed for 8 mL (2 dram) vials that can be placed inside by a robotic arm with gripper, the 3d-printed design files are easily altered for use with larger vials. Most components, including for the LEDs (~1W to be suitable for photochemistry) are modular and easy to swap.

<b><h2>Authors:</b></h2>

Owen Alfred Melville, Staff Scientist <br>
Monique Ngan, Automation Technician <br>
Jeffrey Watchorn, Staff Scientist <br>
[Acceleration Consortium](https://acceleration.utoronto.ca/) <br>
Last Updated 2024-10-22 <br>

<b><h2>Why LEDbyXample? </b></h2>
<b> Low Cost: </b> Existing photoreactors on the market are quite expensive. One of the cheapest, the [Pioreactor](https://pioreactor.com/en-ca/products/pioreactor-20ml?variant=46984254554168), costs about $340 USD ($460 CAD). There is no need for such a large price. The main parts for the LEDbyXample photoreactor cost about $80 USD, with additional electronic components from kits costing another $80 USD. Many of these additional parts are small electronic components that users may already have, and the kits provide more parts than are required by the reactor. Many of the components could also likely be sourced for cheaper as long as the builders are able to perform their own quality control checks. 

<b> Automation Friendly: </b> LEDbyXample is designed to work with automation and self-driving labs. Vials can be release inside the reactor by a robotic arm with a gripper. Automation of the stirring rpm and LED intensity is controlled through a custom python script and uses a Raspberry Pi Pico which can be commanded through a USB cable. Wireless support for the Pico is available but not documented in this project. 

<b> Skill Development: </b> LEDbyXample is made largely from scratch. This allows builders to develop their DIY skills (3D printing, electronics prototyping, microcontroller use). It contains clear build instructions with photos, links to videos, and clear part lists with links. The Python code used to communicate with the microcontroller is designed to be clear and easily modified. 

<b> Modular / Customizable: </b> LEDbyXample is designed to be modular, with components (LEDs, fans, bases) that can be easily removed or swapped. The 3D printed parts that comprise the physical reactor can be modified to accomodate for different vial sizes. 

<b><h2>Summary of Steps:</b></h2>
  1. Order the required items
  2. 3D Print the required parts
  3. Assemble the photo-reactor
  4. Operate the photo-reactor

<b><h2>Tools Required For This Project:</b></h2>
- [Soldering Iron (for electrical connections)](https://www.amazon.ca/Weller-Soldering-Station-WLACCBSH-02-Silicone/dp/B08MC4HVTR?th=1)
- [Heat Gun (for heat-shrink electrical connections)](https://www.amazon.ca/Mini-Heat-Shrink-Gun-Dual-Temp-dp-B09TYM45BH/dp/B09TYM45BH/ref=dp_ob_title_hi)
- [Wire cutters](https://www.amazon.ca/BOOSDEN-Crafting-Spring-Loaded-Plastics-Clippers/dp/B08ZCHYGN7/?th=1)
- [3D printer](https://ca.store.bambulab.com/products/p1s?srsltid=AfmBOorLX7Ki2ZaYaFx6AWRBcr8wJq_0mTlmHkm-IWXz0sfFRXeNtMNX)

<b><h2>Skills required For This Project: </b></h2>
- Soldering
- Basic Python coding

<b><h1>Step 1: Order the Required Items: </b></h1>

The majority of the components for this project are electronic. 

<b><h2>Materials Required:</b></h2>

These materials are required for the photoreactor. You would need to purchase more to make additional photoreactors. Note, only 1x Fan and 1x Fan Board are strictly needed for stirring. The active cooling Fan and Fan Board are optional. The total cost with 2 LED modules and 1 active cooling (fan) module is $82.80 USD. 

| Item                             | Supplier | Part number                   |Number | Cost (USD) | Total Cost (USD) |
| -------------------------------- | -------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| [Raspberry Pi Pico WH](https://www.pishop.ca/product/raspberry-pi-pico-wh-pre-soldered-headers/  )            | PiShop   | 402-1               |           1      | 9.8   | 9.8        |
| [Grove Shield for Pico](https://www.digikey.ca/en/products/detail/seeed-technology-co-ltd/103100142/13688265?s=N4IgTCBcDaIIwFYCcB2AtHADAZi5uALGGgHIAiIAugL5A)            | Digikey  | 1597-103100142-ND              | 1      | 6.25  | 6.25       |
| [Fan Control Board](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4808/13590573?s=N4IgTCBcDaIIwFYwA4C0AWZAGNA5AIiALoC%2BQA )               | Digikey  | 1528-4808-ND                   | 2      | 7.99  | 15.98      |
| [Square Fan (20mm Diameter)](https://www.digikey.ca/en/products/detail/cui-devices/CFM-2006CF-060-078-22/19524716?s=N4IgTCBcDa5mBmAtAYQGIFkkAIwAY8A2dJIvHPAdgA4l4kA5AERAF0BfIA)       | Digikey  | 2223-CFM-2006CF-060-078-22-ND |  2      | 11.06 | 22.12      |
| [Grove to Fan Board Connectors](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4528/11627737?s=N4IgTCBcDaIIwFYwA4C0AWJaByAREAugL5A)   | Digikey  | 1528-4528-ND                  | 2      | 2.83  | 5.66       |
| [Power Barrel Connector](https://www.digikey.ca/en/products/detail/same-sky-formerly-cui-devices/PJ-102AH/408448)     | Digikey  | PJ-102AH                  |  1      | 1.02  | 1.02       |
| [Power Supply](https://www.digikey.ca/en/products/detail/tri-mag-llc/L6R06H-050/7682614)    | Digikey  | L6R06H-050           |  1      | 5.31  | 5.31       |
| [LED Stars (Green)](https://www.digikey.ca/en/products/detail/new-energy/LST1-01H06-GRN1-01/10663110?s=N4IgTCBcDaIDIGUAqBGAtABhQCQwNjQHEAlAOXSxAF0BfIA)               | Digikey  | LST1-01H06-GRN1-01            |  2      | 6.41  | 12.82      |
| [NPN Transistor](https://www.digikey.ca/en/products/detail/nexperia-usa-inc/PZT2222A-115/1158011?s=N4IgTCBcDaIIwHYwILQBYwFYwrigBAHIAiIAugL5A )                  | Digikey  | 1727-4252-1-ND                |  2      | 0.56  | 1.12       |
| [USB Cable for Pico](https://www.digikey.com/en/products/detail/cvilux-usa/DH-20M50056/13177301) |  Digikey | DH-20M50056 | 1 | 2.72 | 2.72 |
| Total Cost (USD) | | | | | <b> $82.80 </b> |
| Total Cost (CAD) | | | | |<b> $115.53 </b> |

<b><h2>Materials Required - Kits:</b></h2>

These materials come in kits, so you may not need them if you already have similar materials. They can be used for multiple reactors or other projects. 

| Item                             | Supplier |  Cost (CAD) |
| -------------------------------- | -------- |  ----- |
| [Prototype PCB Board](https://www.amazon.ca/BOJACK-6-Prototype-Soldering-Compatible-Arduino/dp/B091PZQ4W7/    )              | Amazon Canada        | 21.99 |
| [Nyodenium Magnets 6mm x 2mm](https://www.amazon.ca/Magnets-Refrigertor-Whiteboard-Durable-Multi-Use/dp/B07BJFD6FL/)      | Amazon Canada     | 9.99  |
| [Heat Sinks](https://www.amazon.ca/Awxlumv-Heatsink-25-x25-x10/dp/B08CMK8BMT/ )                       | Amazon Canada   |  10.99 |
| [Resistors](https://www.amazon.ca/Resistor-Assorted-Resistors-Assortment-Experiments/dp/B07L851T3V/?th=1 )                        | Amazon Canada   | 17.99 |
| [Solder Seal Connectors](https://www.amazon.ca/Kuject-Connectors-Waterproof-Electrical-Automotive/dp/B073RMRCC3/) | Amazon Canada   | 16.99 |
| [4-Pin Connectors](https://www.amazon.ca/1-25mm-Connectors-Pre-Crimped-Pixhawk-Silicone/dp/B07S18D3RN/ )  | Amazon Canada           | 21.99 |
| [2-Pin Connectors](https://www.amazon.ca/dp/B00T2U76V0/ref=olp-opf-redir?aod=1&th=1) | Amazon Canada | 10.77 |
| Total Cost (USD) | | <b> $79.29  </b>| 
| Total Cost (CAD) | | <b> $110.71 </b> |

<b><h2>Generic Materials Required</b></h2>
  - Wires (at least red, black, blue, and yellow)
  - Solder
  - Filament for 3D printing (eg [PLA](https://ca.store.bambulab.com/products/pla-basic-filament?gad_source=1&gclid=Cj0KCQjwpP63BhDYARIsAOQkATYc5jM-nciSOOw8pbxHA_WIkh3n5OJYfMMvQm4q8-BjsxyQY5-RIlQaAhdqEALw_wcB) and [ASA](https://ca.store.bambulab.com/products/asa-filament?srsltid=AfmBOor0TaklWc8wcPPxX6YhTCeVZ4l1UiV82qqBd3xhd9iYvP6Alb0c))

<b><h2>Photo of Materials </b></h2>
<img src="https://github.com/user-attachments/assets/755f7d33-3f28-4b20-b5f1-a5f32581dd48" width="800"/> <br>

<b><h1>Step 2: 3D Print the Parts: </b></h1>

All the 3D printed parts can be printed with 0.2 mm layer height and a 0.4 mm nozzle. For prototyping or low-temperature reactors, PLA filament can be used. For higher temperatures or shorter wavelength (blue,violet,UV), ASA can be used. Since ASA tends to warp, I recommend using glue stick on the print bed. 

| File Name          | Purpose                  | Printing Considerations      | Number Required         | Customization Potential                 |
| ------------------ | ------------------------ | ---------------------------- | ----------------------- | --------------------------------------- |
| LED_holder.stl     | Holds LED + Heat Sink    | None                         | 1 per LED               |                                         |
| blank_holder.stl   | Blocks Window            | None                         | 1 per unblocked window  |                                         |
| fan_base.stl       | Holds Fan + Magnets      | Tree Supports from base only | 1                       | Change inset for larger fan             |
| fan_holder.stl     | Holds Cooling Fan        | Tree supports from base only | Only if cooling desired |                                         |
| reactor_shield.stl | Holds Vial               | Tree supports from base only | 1                       | Change circle diameter for larger vial  |
| screw_base.stl     | Connects reactor to base | None                         | 1                       | Change screw pattern for different base |

<img src="https://github.com/user-attachments/assets/62d1e7ee-361d-46b5-8baa-6726d720cf07" width="800"/>

<b><h1>Step 3: Assemble the Photoreactor: </b></h1>

The 3D printed parts are modular. When assembled, they should look like this:

<img src="https://github.com/user-attachments/assets/46840458-0334-4217-876d-ce14d960154b" width="200"/>

<b><h2> Step 3a: Assemble the LED Holders </b></h2>

The LED Holder takes the 3D printed insert, and adds in a heat sink and a ~1W LED with attached wires to be controlled by the microcontroller. 

<b>Parts Required:</b>
- LED star
- Wires
- 2-Pin Connectors (or alternative)
- 3D Printed LED Holder
- Solder seal connectors
- Heat sinks

<b>Steps:</b>
  1. Take your LED star, it should have two large soldering pads labelled + and -

<img src="https://github.com/user-attachments/assets/f5ad7750-d359-4cf4-9f4c-2d04c2cf09ac" width="200"/>
 
  2. Clean the LED star pads using rubbing alcohol (isopropanol) and a tissue
  3. ***Tricky step Alert*** Attach a red wire to the + labelled pad on the right of the star, and tape it down away from the pad to keep it in place. Heat up your soldering iron in a well ventilated area, then place it over the wire. Using your non-dominant hand, feed solder to the pad from different directions, allowing it to flow onto the pad. Once the solder has covered the whole pad, carefully remove the soldering iron and replace it in its holder. The wire should be encased in solder that has made a strong bind with the pad. If after 2 minutes, gentle pressure on the solder pushes it off the pad, you may need to clean the pad and repeat the process. For tips on this process, see this video (Time Stamp 4:30) https://www.youtube.com/watch?v=H-82av4zQKY&ab_channel=MrTroutDT


https://github.com/user-attachments/assets/7bd34561-cb51-4cb3-8f49-8e8b69328b1f


  4. Repeat the last process using a black wire and the - labelled pad on the right of the star. Ensure the contact has been well made after completion

<img src="https://github.com/user-attachments/assets/32c3599f-7942-4f20-a431-ed609db9fcdc" width="400"/>
 
  5. Remove the adhesive from the heat sink, and slide it into the 3D printed LED holder. Note that the spikes of the heat sink point outwards, towards the thinner side. The flat side of the heat sink should point inwards towards the thinner side.
     
<img src="https://github.com/user-attachments/assets/7e2b9ade-fd8d-4ce7-9e17-7f89670c8fbd" width="200"/>

  6. Carefully feed the red and black wire through the hole at the bottom of the LED holder. If your wires will not fit, you can use a sharp knife to cut open the channel. As you feed the wires through, you may need to bend them so you can position the LED in a central location on the heat sink.

<img src="https://github.com/user-attachments/assets/7373ccb2-6cda-42ff-8504-7082727b10d2" width="200"/>
 
  7. If you wanted a permanent setup, you could wire these red and black ends straight to your LED board (Step 3c). However, to make them removable/swappable, the wires need connectors. I recommend getting a set of pre-wired connectors with red and black wires at the non-connector end. Take the red wire from your LED and the red wire from the connector, and place them in a solder seal connector so that the bare ends of the wires are touching and under the "solder" of the connector. Use your heat gun to carefully heat up the solder seal connector from different angles. First the plastic will melt, sealing the wires together, then you will see the solder spreading from the central area, which should create a proper connection between the two wires. Let the connection cool. To check that the wiring has been made correctly, you can use a multimeter, comparing the LED pad to the appropriate pin in the connector. Use this youtube video for guidance: https://www.youtube.com/watch?v=bvDk3HzS7lM&ab_channel=SkillBuilder

<img src="https://github.com/user-attachments/assets/74cff052-b6ad-41a6-8cfc-0ee9209b1246" width="200"/>
  
  8. Repeat the last step to connect the black wires.

<i>Congratulations, you have created your LED holder, which can slide in and out of the photoreactor! You can create as many of these as you have LEDs that you want to use </i>

<img src="https://github.com/user-attachments/assets/1358ff0c-9712-4247-9423-5027ea5965c2" width="200"/>
 
<b><h2> Step 3b: Assemble the Fan Base </b></h2>

The fan base holds a fan with magnets to allow for magnetic stirring.

<b>Parts Required:</b>
- 3D Printed Fan Base
- Fan
- Wires
- Super glue / double-sided tape
- Magnets (x2)
- 4-Pin Connectors (or alternative)

<b>Steps:</b>
  1. Thread the wires through the hole near the center of the fan base, with the black side of the fan facing up.

<img src="https://github.com/user-attachments/assets/4cb23316-80ef-4810-b8c4-0a2b49eafe8f" width="200"/>

  2. Carefully pull on the wires and wiggle the fan into the center square.

<img src="https://github.com/user-attachments/assets/d990a419-c216-41bc-89c8-05daa266d34b" width="200"/>

  3. Using super glue or double-sided tape, carefully place the magnets on the top of the fan.

<img src="https://github.com/user-attachments/assets/e3d64590-094e-4241-b5e5-eb869c47dd86" width="200"/>

  4. <b>Attach the connectors:</b> You can wire the fan to a 4-pin connector using the optional kit or an alternative. 
  
  <i>Using Optional Kit:</i> Using the same technique as in Step 3a - 7, use solder seal connectors to extend the length of the fan wires by attaching them to pre-crimped wires from the electrical connector kit. Then, connect each wire to the connector head. When inserted correctly, the ends of the wire should be fully contained inside the plastic connectors, and fit snugly in place.

<img src="https://github.com/user-attachments/assets/1c7ae419-4b70-4708-9fc9-78c2f4f0db90" width="300"/><img src="https://github.com/user-attachments/assets/3e2fc185-a7a7-454d-abe7-26f17d035467" width="300"/><img src="https://github.com/user-attachments/assets/0d30857c-bc3d-4d44-adf1-b6a340a8582b" width="300"/>

  <i>Using Other Connectors:</i> If you have a pre-wired connector with 4 wire leads, you can use that instead of the connector kit. Using the same technique as in Step 3a - 7, use solder seal connectors to connect the fan wires to your pre-wired 4-pin connector. 

<img src="https://github.com/user-attachments/assets/72303172-57d6-4a45-badc-7784df92e15e" width="400"/>

<i>Congratulations, you have created your Fan Base which is used to stir a magnetic rod in the reactor </i>

<b><h2> Step 3c: (Optional) Assemble the Fan Holder </b></h2>

The fan holder holds a fan to actively cool the reactor vial. The cooling capacity of the current setup is unknown, and it is possible a larger or a stronger fan is required. This will be investigated for future versions of the photoreactor. 

<b>Parts Required:</b>
- 3D Printed Fan Holder
- Fan
- Wires
- 4-Pin Connectors (or alternative)

<b>Steps:</b>
  1. Thread the wires through the hole near the bottom of the fan holder, with the black side of the fan facing out.

<img src="https://github.com/user-attachments/assets/f0f54a80-086c-4ea3-97b7-6a5aff1c70cd" width="200"/>

  2. Carefully pull on the wires and pull the fan into its slot.

<img src="https://github.com/user-attachments/assets/530b5e00-fb60-4061-bba2-5d57997112f3" width="200"/>

  3. Using the same technique as in Step 3a - 7, use solder seal connectors to extend the length of the fan wires by attaching them to pre-crimped wires, then carefully insert the pre-crimped wires into the connector head. Alternatively, if you have a pre-wired connector with 4 wire leads, you can use that instead.

<img src="https://github.com/user-attachments/assets/ca9832b9-e13d-449d-b706-0cea9f68d433" width="400"/>

<i>Congratulations, you have created your Fan Holder which is used to cool the reactor </i>

<b><h2> Step 3d: Assemble the LED Board </b></h2>

The LED Board uses transistors to control the on/off status of the LEDs, with the signal to the transistor coming from the Rasperry pi. It also has a power inlet port to power the LEDs separately from the Pi, as they draw quite a bit of current. In the future, an LED board could be purchased to directly control the LED, including its intensity, something not currently possible with this design. The design described here controls 2 LEDs at a time, but it could be extended to control more LEDs at once. 

<b>Parts Required:</b>
- PCB board from Kit (60x40 mm)
- Wires
- 1x 1000 Ohm resistor
- 2x 5.6 Ohm resistor
- 2x 390 Ohm resistor
- 2x NPN Transistors
- 4-Pin Connectors (or alternative)
- 2-Pin Connectors (or alternative)
- 1x Power Barrel Connector

<b>Steps:</b>

<img src="https://github.com/user-attachments/assets/4a819eb4-cefc-4ced-982f-17caf310d74d" width="400"/>

  1. Mount the power board and solder in a 1000 Ohm resistor between the power and ground sides. This creates a power port. The GND side represents your ground, and 5V your high voltage.
  2. Solder the circuit diagram above. For now, leave the open circles with text labels. The power supply and 1000 Ohm resistor are already completed in step 1. For the NPN transistors, the drawing below shows the schematic. Pin 1 (base) goes to the 330 Ohm resistor, and eventually to the RPi GPIO Pin. This acts like a switch for this LED. Pin 2 (collector) goes towards the LED and the power supply. Pin 3 (emitter) goes to ground.

<img src="https://github.com/user-attachments/assets/5954095a-d3c8-4d65-bc8e-a652bc8a053b" width="200"/>

  3. Solder wires into the open circles that connect to the RPi GPIO pins. The other end of the wire can be bare or an open pin. We will connect these to the RPi in a later step.
  4. Solder wires into the open circles that connect to the LED. For clarity, you can use red wires to go towards the power supply, and black wires towards the transistors. These wires should be at their other end connected to the complementary connectors that you used in Steps 3a-7 and 3a-8. These are meant to connect and disconnect the LED holders so you can change them.
  5. Solder a black wire from the ground/- terminal. The other end of the wire can be bare or an open pin. We will connect this wire to the RPi Ground Pin in a later step, to ensure a common ground.
  
<img src="https://github.com/user-attachments/assets/9afe2258-821c-457f-b0fd-84a86cb2db12" width="400"/>
  
  6. (Optional): To add more LED outputs, add more of this section of the circuit diagram, connected in the same way. If you add many more LEDs, you may require a power supply that is rated for higher current. 

<img src="https://github.com/user-attachments/assets/3d178e2d-80eb-4003-b73c-21f0d1d6c7ba" width="400"/>

<i>Congratulations, you have created your LED Board which is used to control the reactor LEDs</i>

<b><h2> Step 3e: Assemble the Fan Board </b></h2>

The Fan Board uses pre-made fan control boards to control the RPM of the fans. It connects to the Rasperry pi and to a separate power supply. The current design is for 2 fans (1 cooling, 1 stirring) but could be easily be extended for use with more fans. 

<b>Parts Required:</b>
- PCB board (60x40 mm)
- Wires
- 1x 1000 Ohm resistor
- 2x Fan Control Board
- 2x Grove to Fan Board Connectors
- 1x Power Barrel Connector (Optional)

<b>Steps:</b>

<img src="https://github.com/user-attachments/assets/cb81da7f-3da0-43e1-a4db-d8c14636db3a" width="200"/>

  1a. (Optional) Mount the power board and solder in a 1000 Ohm resistor between the power and ground sides. This creates a power port. The GND side represents your ground, and 5V your high voltage.
  1b. Alternatively, you can connect the 5V using a wire to the 5V section of the LED board or to the 5V Pin in the Pico. This means one less power supply, but will draw power either from the LED power supply or from the Pico (which you don't want to draw too much from). 
  2. Solder the circuit diagram above. Solder wires into the open circles for the fan power (red) and ground (black). These will go to the 4-pin connector to the fan.
  3. For each Fan Control Board, solder wires into the "FAN" (blue) and "TACH" (yellow) ports, the other ends will go to the 4-pin connector to the fan.
  4. For each Fan Control Board, attach a Grove to Fan Board Connector. This will connect to the RPi.
  5. Take the power (red), ground (black), tach (yellow), and fan (blue) wires and connect them to a 4-pin connector that complements the one you created for your fans in step 3b-4. 

<img src="https://github.com/user-attachments/assets/24645da1-c7f1-4156-a71e-eaadc0973199" width="400"/>

<i>Congratulations, you have created your Fan Board which is used to control the reactor Fans</i>

<b><h2> Step 3f: Combine the Electronics </b></h2>

We need to connect the boards to the raspberry pi, which controls them. Optionally, you can choose to house them in the 3D printed holder, the parts of which you would need to print. This housing is only to keep the electronics tidy, and is not needed. 

<b>Parts Required:</b>
- Assembled Fan Board (Step 3e)
- Assembled LED Board (Step 3d)
- Raspberry Pi Pico WH
- Grove Shield for Pico
- USB Cable for Pico (USB-A to micro-USB)
- Power Supply (for LED Board)
- (Optional): Power Supply (for Fan Board)
- (Optional): 3D Printed electronics housing

<b>Steps:</b>
  1. Place the Raspberry Pi into the Grove Shield. This requires some force so that it goes in all the way.
  2. Common ground: Take the wires directed towards "RPi Ground" from the Fan and LED Boards and connect them to any open pin on the Raspberry Pi Pico labelled GND.
  3. Signal wires (LEDs): Take the wires directed towards "RPi GPIO Pin 0" and "RPi GPIO Pin 1" from the LED board and connect them to the Raspberry Pi Pico in the corresponding Pins ("GP0" and "GP1")
  4. Signal wires (Fans): Take the Grove-to-stemma connectors from the fan boards and connect them to the top-right corner slots on the Raspberry Pi Pico (with the USB connector oriented up).

<img src="https://github.com/user-attachments/assets/de60fa9d-b3a7-4d3d-9422-c25d8a3d01f0" width="400"/> <br>

<b> Optional: Add the electronics to a housing </b>

The electronics housing can be used to house the Raspberry Pi Pico and auxillary electronics. The holders for the auxillary electronics will fit the 60x40 mm PCB boards. They can be printed according to the instructions below. For the material you can use PLA but the snapping mechanism on the snap lid may work better with PETG. 

| File Name                            | Purpose                     | Printing Considerations | Number Required | Customization Potential                  |
| ------------------------------------ | --------------------------- | ----------------------- | --------------- | ---------------------------------------- |
| Pico Holder_MainBody.stl             | Holds the Pico              | Flat side down          | 1               |                                          |
| Pico Holder_Main_Lid.stl             | Lid for Main Unit           | Flat side down          | 1               |                                          |
| Aux_Module.stl                       | Holds LED/Fan Board         | Flat side down          | 2               | Could change to hold different sized PCB |
| Pico Holder_Port_Door_Default.stl    | Blank door for Aux Unit     | Flat side down          | 0               | Can add ports                            |
| Pico Holder_Port_Door_Open_Ports.stl | Custom door for Aux Unit    | Flat side down          | 2               |                                          |
| Pico_Aux_Lid_Snap.stl                | Lid for Aux Unit            | Flat side down          | 2               |                                          |
| Pico Holder_Port_Door_Honeycomb      | Honeycomb door for Aux Unit | Flat side down          | 2               |                                          |

Instructions:
- Print the pieces for the housing
- Place the boards in their respective holders with any connecting wires detached
  
<img src="https://github.com/user-attachments/assets/65af9733-7747-49fc-8726-cbd7fad284da" width="600"/> <br>

- Thread any connecting wires through the honeycomb in the sides
- Attach the side pieces and lids

<img src="https://github.com/user-attachments/assets/dd8e2990-4d99-45c2-99e0-43a468e77be5" width="600"/> <br>

<i> Congratulations, you have finished assembling the electronics! </i>

<b><h2> Step 3g: Assemble the Reactor </b></h2>

<b>Parts Required:</b>
  - Assembled Electronics (Step 3f)
  - Assembled Fan Base (Step 3b)
  - Assembled LED Holder (Step 3a)
  - Assembled Fan Holder (Optional, Step 3c)
  - Reactor Shield
  - Blank Holders (for open unfilled slots)
  - Screw Base (Optional)

<b>Steps:</b>
  1. Connect the electrical connectors for each LED and fan to the electrical setup.

<img src="https://github.com/user-attachments/assets/62df0b9c-4685-476f-ac98-35a04919de7a" width="400"/> <br>

  2. Assemble the reactor parts. The LED holder, blank holders, and fan holders should slot easily into the 4 slots on the sides of the reactor shield. The reactor shield slots onto the fan base, which slots onto the screw base. The screw base has slots for fastening the base of the reactor. These could be modified to attach the reactor to a different base or with different screws.

<img src="https://github.com/user-attachments/assets/a8aeecdd-5958-4516-b0fa-05f81ab622aa" width="400"/> </br>

<i> Congratulations, you have fully assembled the LEDbyXAmple photoreactor! </i>

<b><h1>Step 4: Operate the Photoreactor: </b></h1>

To operate the photoreactor, we will need to use a Python script that connects to the RPi Pico. The script can be used to control the RPM of the fan (with some constraints) and to turn the LEDs on and off as needed. 

<b><h2> Step 4a: Installations </b></h2>

<b>Steps:</b>
  1. Install a code editor, we recommend VSCode. 
  2. Install Python on your computer if it is not already installed.
  3. Install Micropico extension in VScode
  4. Connect the RPi Pico to your computer using the Usb B Micro B to Usb A Cable, while pressing the BOOTSEL button on the Pico. A file directory for the Pico should show up in your file explorer.
  5. Flash the Raspberry Pi  by downloading the [MicroPython UF2 file for Pico W](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) into your computer and moving the file to the directory of the Raspberry Pi. The file directory should disappear after this and disconnect it from your computer.
  6. Open a new “micropico vPERL” terminal in VS code
  7. When the Raspberry Pi is connected it should show a success message in green text.

![VS Code - Raspberry Pi Connected](https://github.com/user-attachments/assets/98e207d4-47e1-4f2b-a559-222c2ae830b2)

<b><h2> Step 4b: Python Scripts </b></h2>

<b>Steps:</b>
  1. Download the python scripts from this github repository, including photo_reactor.py and reactor_test.py and the "lib" folder with the drivers for the fan boards
  2. In VSCode, “Configure project” for the folder that contains the lib folder, photo_reactor.py & reactor_test.py files
  3. Upload the project to Raspberry Pi by right clicking on folder containing all the project files & select  “Upload project to Pico”
  4. To run the test code, select reactor_test.py file & right click to choose “Run current file on Pico”

<b> NOTE: Do not look directly at your LEDs! We recommend using blue-light blocking glasses and never looking directly at the emitted light </b>
	
<b><h2> Step 4b: Operation </h2></b>

The LEDbyXample photoreactor currently has two functions: Switch on/off the LEDs (could have up to 4 in one reactor) and initialize/set the rpm of the fans (both for stirring and cooling). 

<b>Functions:</b>
  1. <b> add_fan ( fan ) </b> takes in the SoftI2C address with two pins that are associated with controlling the fan, these numbers will change depending on which slot you put your fans in on the pico board
  2. <b> add_led ( pin ) </b> takes in the GPIO pin number for a specific LED to set it up for operation
  3. <b> turn_on_led ( index ) </b> turns on the LED with the specified index
  4. <b> turn_off_led ( index ) </b> turns off the LED with the specified index
  5. <b> set_led_brightness (index, duty_cycle) </b> Set the brightness of an LED to between 0 and 100 (duty_cycle) using pulse width modulation.
  6. <b> initialize_fan ( index, starting_duty_cycle) </b> attempts to turn on fan with specific index, it will try different duty cycles until it is able to measure an rpm (sometimes the initial duty cycle is insufficient when there is a load like a stir bar in a thick liquid. Note that the fan may not initialize if the stir bar is too close or too far away from the magnets. This matters more if you are using a different vial than the 2 dram (8 mL) vial this reactor was designed for. This function returns the duty cycle that was sufficient to activate the fan. 
  7. <b> set_fan_rpm (index, target_rpm, duty_cycle) </b> This attempts to get the specified fan to reach a specific rpm, starting with the specified duty cycle. It may not maintain that rpm, but will keep the same duty cycle, which is returned by the function.
  8. <b> hold_fan_rpm (index, target_rpm, target_time, duty cycle) </b> This attempts to adjust the input duty cycle to maintain a target rpm for a specific time period. This means adjusting the duty cycle up and down slightly as needed. 


<b><h1> Future Steps </b></h1>

1. Increase the physical robustnest of the design, preventing the pieces from falling over when wires are tugged.
2. Measure the temperature of the reactor using a thermocouple or an IR probe/camera.
3. Measure the spatial uniformity of the LED emission in the reactor.
4. Use feedback control to increase cooling fan speed when temperature rises. This might require a stronger cooling fan.
