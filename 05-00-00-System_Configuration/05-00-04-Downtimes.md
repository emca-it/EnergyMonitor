# Downtimes

Dowtimes can be set up in 2 different ways: 

```
- 1 time downtime
- periodically occuring downtime
```

Downtimes can be accessed from the main bar: "**Monitor**" -> "**Downtimes**"

![downtime](/media/05_00_04_01_Downtime.png)

<blockquote style="border-left: 8px solid green; padding: 15px;"> 
<strong>All Downtimes </strong> sub-menu shows all regular downtimes currently active in Energy Monitor
<br></br>
<strong>Recurring Downtimes</strong> sub-menu shows all recurring downtimes currently active in Energy Monitor
</blockquote>

## Regular Downtimes

These downtimes are set from the host itself, from the it's main menu. 

They are visible under "**All Downtimes**" sub-menu.

![downtime](/media/05_00_04_02_Downtime.png)



### Setting up a regular downtime

1. Enter the hosts main menu either through "**Monitor**" -> "**All Hosts**" or the search bar.  

2. Click "**Schedule Downtime**"

![downtime](/media/05_00_04_03_Downtime.png)

3. Enter preferred parameters and save with "**Submit**"

![downtime](/media/05_00_04_04_Downtime.png)

Parameters include:

```
- Start Time

- End Time 

- Flexible

    - Determine how long the downtime should last after the host becomes unreachable.

- Duration (of flexible downtime) 

- Triggering downtime 

    - an existing downtime can trigger another one

- Propagate to children

    - If the host is a parent, all children under him will also receive the     downtime, either right away with a regular downtime, or when the host becomes unreachable, with flexible downtime.

- Comment 
```
Your downtime is now visible on the list and the host status on it's main page will change to "**Scheduled Downtime**" 

<blockquote style="border-left: 8px solid green; padding: 15px;"> A regular downtime can be changed into a recurring one at any time with the use of the <strong>"Actions"</strong> icon, in the "<strong>All Downtime</strong>" menu.

<br></br>
![downtime](/media/05_00_04_05_Downtime.png)
</blockquote>




## Recurring Downtimes

### Setting up a recuring downtime

1. Enter the cofiguratio meu through "**Monitor**" -> "**Downtimes**" -> "**Recurring Downtimes**"

2. Add a new downtime with the "**New**" button at the right side of the screen.

3. Enter the parameters of Your choice and confirm with "**Add Schedule**" button.

![downtime](/media/05_00_04_06_Downtime.png)
![downtime](/media/05_00_04_07_Downtime.png)

<blockquote style="border-left: 8px solid orange; padding: 15px;"> Objects in bulk, can be chosen, <strong>but only from the same type</strong>, ie. the user cannot add a single host and an entire hostgroup, it has to be either only host or only hostgroup.
</blockquote>
<br></br>

<blockquote style="border-left: 8px solid grey; padding: 15px;"> <strong> Flexible starttime </strong> similarly to it's equivalent in regular downtimes, allows the user to set an amount of time that the downtime should last, if a service gets into a <strong>problem</strong> state. This works in addition to a defined recurrence pattern, so ie. Downtime is set to 2 hours, from 8:00 to 10:00, Flexible is set to 2 hours. Metric has an issue at 9:45, so the total downtime, will be from 9:45 to 11:45. 
</blockquote>
<br></br>




