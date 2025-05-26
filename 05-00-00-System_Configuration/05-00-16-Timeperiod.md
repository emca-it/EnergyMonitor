# Timeperiods

In the host configuration menu there is a field called: "**check_period**". 

This field contains "**Timeperiods**" which are essentially calendars for notifications and service checks, they govern at which days and hours they should be active.

In the host configuration menu timeperiods are managed by these fields:

- Services and hosts are governed by 2 calendars.

![Timeperiod](/media/05_00_16_02_Timeperiod.png)

Or

- Services and hosts are governed by 1 calendar.

![Timeperiod](/media/05_00_16_01_Timeperiod.png)

## Configuring a timeperiod

Enter "**Manage**" -> "**Configure**" -> "**Timeperiods**"

![Timeperiod](/media/05_00_16_03_Timeperiod.png)

1. Insert mandatory data, such as name of the timeperiod, alias and the file in which it will be saved.
<br></br>
2. Each day can be set individually, syntax is as follows: 

<blockquote>

- HH:MM-HH:MM,HH:MM-HH:MM

- Entire day: 00:00-24:00

- Separate each range with a "<strong>,</strong>"

</blockquote>

<br>

![Timeperiod](/media/05_00_16_04_Timeperiod.png)

3. Intervals consisting of "**Single Dates**" and "**Date Ranges**" can be set.

![Timeperiod](/media/05_00_16_05_Timeperiod.png)
![Timeperiod](/media/05_00_16_06_Timeperiod.png)
![Timeperiod](/media/05_00_16_07_Timeperiod.png)
![Timeperiod](/media/05_00_16_08_Timeperiod.png)

4. After finishing, save the changes to the database. 



