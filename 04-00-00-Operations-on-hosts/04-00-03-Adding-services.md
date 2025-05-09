# Adding services to a host

In order to add a service to a host: 

1. Pick the host from the "**Monitor**" -> "**Hosts**" -> "**All Hosts**" menu and access it's configuration page through the "**Gear**" icon.
<br></br>

![Adding_hosts](/media/04_00_03_main_menu.png)

2. Enter the service menu either through the link under the search bar or through a shortcut bar on the right side of the screen.
<br></br>

![Adding_hosts](/media/04_00_03_main_menu_1.png)
![Adding_hosts](/media/04_00_03_main_menu_2.png)

3. Specify the service parameters
<br></br>
Parameters include:
````
- Service description

- Check command

    - this is the metric that will be monitored.

- Check command arguments:

    - this determines the parameters of the metric

- File

    - Where the metric will be saved. 
````


![Adding_hosts](/media/04_00_03_main_menu_3.png)

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: If You are uncertain about the syntax of the metric yo uare trying to use, you can use <strong>Syntax Help</strong> button which will show you the documentation for the plugin, including available options. 

<br>
Later, you can check your syntax with <strong>Test This Check</strong> button and see if the metric returns proper data. You will be informed about any errors with their specifc details, as the plugin logs them.
<br></br>
Example:

> The administrator might define the metric paraemters with a custom named variables. As shown in the following images, supplying raw parameters or custom variables yields the same results. Additional help regarding custom variables can be found under "**?**" sign next to the "**Custom variable**" field.

![Adding_hosts](/media/04_00_03_main_menu_4.png)
![Adding_hosts](/media/04_00_03_main_menu_5.png)
![Adding_hosts](/media/04_00_03_main_menu_6.png)
</blockquote>


