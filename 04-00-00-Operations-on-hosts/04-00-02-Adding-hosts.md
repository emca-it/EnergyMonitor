# Adding hosts to the database

Energy Monitor supports 2 methods of adding hosts to it's database:

1. Autoscan of the network

2. Manual addition of hosts

## Autoscan of the network

**Enter "Manage" -> Configure -> Hosts**

![Adding_hosts](/media/03-00-03_Adding_hosts.png)
![Adding_hosts](/media/03-00-04_Adding_hosts.png)

The administrator can specify the IP range to search from, domain and buckets to be applied to any host found.

## Manual addition

### 1. **Enter "Manage" -> Configure -> Hosts**

![Adding_hosts](/media/03-00-02_Adding_hosts.png)

### 2. **Fill mandatory fields:**

![Adding_hosts](/media/03-00-02_Adding_hosts_2.png)
![Adding_hosts](/media/03-00-02_Adding_hosts_3.png)

    - Default Template (For regular, non-server endpoints generic-host will suffice)

    - Ip Address

    - Hostname

    - File where this entry is meant to be saved

### 3. **Confirm with "Add Services"**

![Adding_hosts](/media/03-00-02_Adding_hosts_4.png)

### 4. **Confirm adding host with "Finish"**

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: Buckets give the user a capacity of adding multiple services at once, during the creation of a host. So if many identical services are used on multiple hosts, setting a bucket up can make setting up a host much easier. One should of it as several metrics/services bundled together.
</blockquote>
