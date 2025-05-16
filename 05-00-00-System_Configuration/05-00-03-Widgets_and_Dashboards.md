# Widgets and Dashboards

## Dashboards

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> Dashboards allow the user to easily see the current state of the host and associated services, without the need to manually enter host's entry in EnergyMonitor.
</blockquote>

<br></br>
![dashboard_first_view](/media/05_00_03_01_Dashboard.png)

### Adding Dashboards

1. Enter "**Dashboards**" -> "**New Dashboards**"

![dashboard_first_view](/media/05_00_03_06_Widget.png)

2. Pick the preferred layout and specify a name for your dashboard

![dashboard_first_view](/media/05_00_03_02_Dashboard.png)

## Widgets

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> Widgets are predefined, components that allow the user to easily display a particular aspect of current state of EnergyMonitor on a larger interface, ie. a dashboard.
</blockquote>


### Adding a widget

![dashboard_first_view](/media/05_00_03_03_Widget.png)

### Editing a widget

By clicking the gear icon the user can specify various parameters of the widget.

![dashboard_first_view](/media/05_00_03_04_Widget.png)

![dashboard_first_view](/media/05_00_03_05_Widget.png)

### Logserver widget

Logserver widget is worthy of a special mention, because it aggregates data from your Logserver instance and displays it in the form of a dashboard in Energy Monitor. 

After adding the widget the administrator must log into Energy Logserver as he normally would. 

<blockquote style="border-left: 8px solid purple; padding: 15px;"> <b>Note</b>: 

Keep in mind that if the widget is too small for your preference, you can increase it's height using the menu under the  "**Gear**" icon.
</blockquote> 

![dashboard_first_view](/media/05_00_03_07_Widget.png)
![dashboard_first_view](/media/05_00_03_08_Widget.png)



Additional Configuration Required:

1. On your LogServer host, under /etc/kibana/kibana.yml

Replace https://192.168.3.166 with IP of your Energy Monitor.

Add the following line:


<blockquote style="border-left: 8px solid purple; padding: 15px;"><strong>login.isSameSite: "None"</strong></blockquote>
<br>

This is neccessary to tell Kibana to allow placing elements from different sites. 


2. Restart Kibana service with 

<blockquote style="border-left: 8px solid purple; padding: 15px;"><strong> systemctl restart Kibana </strong></blockquote>
<br>


![dashboard_first_view](/media/05_00_03_09_Widget.png)
