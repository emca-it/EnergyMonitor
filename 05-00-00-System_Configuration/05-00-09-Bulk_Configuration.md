# Configuring multiple hosts at the same time

Energy Monitor has few inbuilt ways to allow the administrator to set up several hosts at the same time.

Possible targets of the following operations are:

- Cloning:

    - Hosts
    - Hosts in the following hostgroups
    - Hostgroups

 - Propagate:

    - Hosts
    - Hosts in the following hostgroups
    - Services assigned to hosts in the following hostgroups
    - Services assigned to the following Hosts
    - Services in the following servicegroups
    - Services

- A note worthy mention is the **Copy** option, which creates a new host that is identical to the one being copied, same groups, same notificat ion settings but with removed hostname.

- Useful if you set up 1 host and simply want to create X more with the only things changing like IP address and hostname. 


## Method 1: Propagate

This method involves essentially copying/pasting an existing metric on a host and placing it on the hosts of choice. 

<blockquote>
<strong>Propagate overwrites existing field values on the target host</strong>, for instance:
<br></br>
- Propagating to services on a host, will result in every service's fild being replaced with the one from the source host.
<br></br>
- It is possible and advised to pick a particular service to overwrite.  
</blockquote>

<br>
1. From the host configuration menu choose "<strong>Propagate</strong>"button:
</br>
<br>

![downtime](/media/05_00_06_04_bulk_configuration.png)

2. Tick the the checkbox next to the field/fields you want to propagate:

![downtime](/media/05_00_06_05_bulk_configuration.png)

3. Confirm with "**Propagate Selected Settings**"

![downtime](/media/05_00_06_06_bulk_configuration.png)

4. Pick which entries you wish to modify

![downtime](/media/05_00_06_07_bulk_configuration.png)

5. Confirm with "**Submit**" button and then save the changes into the database.

## Method 2: Clone 

Cloning creates an 1:1 copy of a chosen service/services onto a target host.
<blockquote>
<strong> 
- If on the target host, exists a service with the same name, cloning will not occur. 
<br></br>
-  Therefore in case of changes, the administartor must first delete the services in the target hosts, which are meant ot be overwritten by services from the source host. 
</strong>
</blockquote>
<br>

1. From the host configuration menu choose "**Clone**" button:

![downtime](/media/05_00_06_08_bulk_configuration.png)

2. Pick the entries you wish to modify:

![downtime](/media/05_00_06_09_bulk_configuration.png)
![downtime](/media/05_00_06_10_bulk_configuration.png)

3. Confirm with the "**Clone**" button and save changes to the database. 

```
Keep in mind that a hostgroup can be a target as well, so you can easily copy multiple metrics/services onto multiple hosts, as explained in Method 3.
```


## Method 3: Combination of Cloning and Hostgroups

This method involves creating a hostgroup, adding hosts to it then cloning services onto the hostgroup itself. The hosts will inherit the services from the hostgroup.

The pros is that it requires setting up once, then as new hosts appear, they can be added simply to the hostgroup, no need to configure on the level of the host itself.

The caveat, however is that this works brlliantly for metrics/services that never change. Any change to the metric assigned to the hsotgroup, affects all hosts within it.

For instance: You monitor CPU_LOAD with a warning threshold of 50%. But you have 1 host where you would like to have it at 30%. You would need to add a separate entry for this metric, on the host itself, essentially leaving you with 2 metrics measuring the same thing but with different notification parameters. 

