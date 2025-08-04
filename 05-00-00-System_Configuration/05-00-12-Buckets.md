# Buckets

Buckets are a functionality in Energy Monitor that allows the administrator to set up predefined metrics/services in a **"Bucket"** object, which can be chosen during **"Network Autoscan"** Functionality.

## Configuring buckets

1. Enter "**Manage**" -> "**Configure**" -> "**Bucket Templates**"

2. Assign name of your bucket

3. Assign services/metrics you wish your bucket to contain. 

4. Save the changes into the database.

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
Metrics can be assigned from various hosts. 

It is recommended to create a "dummy host" which will house all such metrics, for ease and convenience of future modifications of the bucket. 
</blockquote>
<br>

![Buckets](/media/05_00_12_01_Buckets.png)


## Automatic buckets

Energy Monitor also has buckets which contain services with a suffix of "**(automatic)**".

The "**Automatic**" nature of these buckets comes do to the fact that they are pre-defined services that unlike a regular service, which points to 1 object, ie. a C drive on Windows and reads some sort of data on it, an automatic service points to all drives in that Windows system. 

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Note</b>: 
<b>These automatic metrics if modified, will stop working.</b> 
</blockquote>
<br></br>

![Buckets](/media/05_00_12_02_Buckets.png)

This is how such a bucket output looks like in the main host menu.

Under "**Bucket Templates**" You can look for these services in a particular bucket.

![Buckets](/media/05_00_12_03_Buckets.png)



<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
Buckets are added during the creation of host in Energy Monitor, therefore the initial scan wil pick up all the information at the time.
<br></br>
If for instance, a disk is added to the host later, a scan in scheduler needs to be planned and executed.
<br></br>
More details on how to set up the scans can be found in a section dedicated to the

[Scheduler](https://kb.monitor.energylogserver.com/en/latest/05-00-00-System_Configuration/05-00-11-Scheduler.html#scheduler)
</blockquote>

