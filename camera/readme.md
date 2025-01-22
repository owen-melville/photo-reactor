<h1>Imaging Module:</h1>

![_Camera_cropped](https://github.com/user-attachments/assets/b398f27c-26b4-4100-98fb-fac003baddd9)

The following describes how to turn the photoreactor into an imaging reactor. 

<h2> Parts Needed: </h2>

[Camera](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/5733/21839820)

[USB Extender](https://www.amazon.ca/UGREEN-Extension-Extender-Transfer-Playstation/dp/B00P0ES0VC/ref=sr_1_5?crid=3N7RB1UZNDPM9&dib=eyJ2IjoiMSJ9.BhVm3nQeHf4O2F3fpluVa9MnVuqOXOqPzwndRqhN5wIk5KDBnGOyOacnbayJ5clOGYHaLHxdhKI6rnkZir4PwAJsOd09U1QD9qv1fTuxgMCQPkcKCM6-ybV8UKALXnw_wskcogvQg65o7bOX424w-_h-Qt9qaEt4mN6ElmxiGWEC7KLLOdewoQaJxE13Zu6O2pco-PesKyHwSwAnMI3XakVCboK7iKjdPY2Hb6xurQVthA3WPzighLCuuS8IEw0yXjPTXVnI_6q1riQLdB_S-qeTKg8rih4-pd0e4aAKv7cEObw2ZyZiPoslMgMZFGMUNWv4swpIfWzd6cllzPrXc40BNtEXacHGO-ZcmUbCqNeN4LvlyVmxF8kmsnndf9YWSJOVJwtSmoHuiI7UzX6fD9ZlHBly3g4CTy-M4vVkOYIF1IITzI5kdRMVn7tppYce.ysUtx2_TLXXK0cOXU83ke25pdNLNYkddpoul-cmYRAo&dib_tag=se&keywords=usb%2Bextender&qid=1737577841&sprefix=usb%2Bextender%2Caps%2C96&sr=8-5&th=1)

<i>Note: The USB extender does seem to create issues with the camera in some instances. It may be an issue with power that can be solved with a shorter cable or with an actively-powered USB hub. I am also looking into using other cameras that may work better for this application. </i>

<h2> 3D Printed Parts: </h2>

- <b>Camera_Module:</b> This holds the camera. Flip 180 degrees and print with supports.
- <b>Camera_Spacer:</b> This can be placed under the tunnel to prevent the reactor from tipping. No supports needed for printing.
- <b>Camera_Tunnel_Lower:</b> This distances the camera from the vial and slides into the side of the reactor. No supports needed for printing.
- <b>Camera_Tunnel_Upper:</b> This slides onto the top of the camera tunnel to block out light. The connection isn't that robust and could be improved. No supports needed for printing. 

<i>There are longer and shorter versions of the tunnel here. I'm not certain what the best length is for the tunnel for image quality.</i>

<h2> Assembly: </h2>
1. Attach the camera onto the camera module using the adhesive tape attached to the camera. 

![1000009149-removebg-preview (1)](https://github.com/user-attachments/assets/7b673660-3737-41a5-8add-989ca68c7560)

2. Slot the camera module in at the edge of the tunnel.

![1000009152-removebg-preview (1)](https://github.com/user-attachments/assets/b504daff-9025-457d-888d-95b74aafc5f6)

3. Slide the tunnel cover onto the top of the tunnel.

![1000009151-removebg-preview (1)](https://github.com/user-attachments/assets/386e88c9-ab17-4aef-96f9-409d8a998c05)

4. Slot the tunnel onto the photoreactor. Place the camera spacer below the tunnel if you want to provide counter support. 

<h2>Lighting: </h2>

I used white [LED stars](https://www.digikey.com/en/products/detail/new-energy/LST1-01H06-3080-01/10663115) in the photo-reactor, and slid in a 0.3 mm white sheet between the reactor and the module to diffuse the light. This does create some glare. This could be improved. If you want to save time, its totally possible to use another lighting source. 

![reactor_image](https://github.com/user-attachments/assets/3e3feba1-4f20-455a-8751-3d2f089892cb)

<h2> Operation & Code: </h2>
