# Checks in Energy Monitor

Energy Monitor allows for various check types, to determine the state of the endpoints. 

There are 2 methods:

-   Active Checks
<br></br>
-   Passive Checks

## Active Checks

-   Those are the most popular method of checking hosts and services. 

-   They are initiated by Energy Monitor process

-   They are run regularly, accordingly to the system setup.


-   Active Checks are initiated when Energy Monitor when the process determines the need to verify the status of a host or a service.

    -   It executes a plugin, passing the instructions about what data to verify, the plugin checks the state of a host or service, then reports back to Energy Monitor. 

    -   Based on the returned data, Energy Monitor takes whatever action is required, for instance it will send notifications.

![CheckTypes](/media/05-00-30-Check_Types_01.png)

### Executing Active Checks

-   Active Checks are executed at:
<br></br>
    -   **Regular intervals**, those are defined by "**check_interval**" and "**retry_interval**" in your host and service definitions. 
<br></br>
        -   check_interval manages "**HARD**" state, endpoint in this state will be checked at intervals defined there, while retry_interval manages "**SOFT**" state and endpoint in this state will be checked accordingly to that parameter.   
<br></br>
    -   **On Demand**, such checks can be manually triggered in the GUI with "**Check Now**" option or when Energy Monitor determines the need to check the latest status information. 
<br></br>
        -   An example of this could be a case when Energy Monitor wants to determine the reachability of a particular network segment, it will check parent-child relations, so children hosts will be checked due to the parent host being checked. 
<br></br>
    -   **On Schedule**, by utilizing the "**Scan Schedule**" option.

### Executing Passive Checks
    
-   Passive Checks are host checks received from a remote source, for instance another Energy Monitor instance, like in a cluster environment.
In other words, Energy Monitor doesn't ask for the data, it only receives it periodically from another server.
<br></br>
-   Passive monitoring encourages building the topology with failover in mind, so hat if 1 monitoring server will suffer a failure, the others can pick up where it left off. Like aformentioned cluster set up.

We will illustrate with the following diagram:

![CheckTypes](/media/05-00-30-Check_Types_02.png)

Energy Monitor - A is the primary monitoring server, a master node, if you will, is monitoring the entire network infrastructure, all routers and switches. 2 other nodes, Energy Monitor - B and Energy Monitor - C, serve as backup servers. Those backup nodes, are receiving the results of passive checks from the master node, Energy Monitor - A. 

In our example, both Router - C and Router - D have suffered some sort of failure and are offline. 

However, it isn't so clear to the nodes. Because they have to take into account their own placement in the topology and where the failed host is. 

Hence from the perspective of:

-   Energy Monitor - A
<br></br>
    -   Router-D is "**DOWN**" while Router-C is "**Unreachable**"   
<br></br>
-   Energy Monitor - B
<br></br>
    -   Router-C is "**DOWN**" while Router-D is "**Unreachable**"
<br></br>
-   Energy Monitor - C 
<br></br>
    -   Both Router - C and Router - D are "**DOWN**"

Please keep in mind, that the idea of passive monitoring is built on the foundation of mutual trust across the nodes operating in the same network segment. So, when Energy Monitor - C reports Router - D as "**DOWN**", Energy Monitor - A and Energy Monitor - B will not question it. 

So if your infrastructure is spread across many network segments, with various different hops, different parent-child relations between the endpoints, depending where in the topology the monitoring server is, distributed passive monitoring setup might not be the most convenient or accurate method. 


