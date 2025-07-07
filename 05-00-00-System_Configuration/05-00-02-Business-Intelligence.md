# Business Intelligence (BI)

### Overview

Energy monitor integrates monitoring with Business Intelligence (BI) to provide an overview of the applications and services your organization offers, both to customers and internally. You can share the BI services you create with other business units and organizations, making them valuable in scenarios where an overview and state information are needed on a specific service, such as supporting non-technical staff in service delivery or fulfilling Service Level Agreement obligations.

### Designing a Business Intelligence

When setting up a new Business Intelligence, the initial task is to pinpoint the core service components within your organization, assess their features, and map out their network hierarchy. With this groundwork completed, you can formulate a design that aligns with your business objectives and outlines an effective service topology.

Key considerations for your design include:

- Determining if the service should track both availability and performance metrics.
- Deciding which applications and components, such as ticketing or CRM systems, should be integrated into the business service.
- Establishing the necessary level of availability to ensure the service fulfills its intended goals.

In Energy Monitor, a BI is organized as groups of sub-elements, accompanied by rule sets that dictate when state changes are reported.

### Rule sets

Below, you'll find a description of the various rule sets available. Keep in mind that each rule set applies solely to the sub-elements on the level immediately below.

#### Thresholds

In Business Inteligence, thresholds are pivotal in monitoring the health of BI groups by defining warning and critical limits.

Defining Thresholds:

- **Warning Threshold**: Specifies the number of issues after which the BI group's status changes to a warning.
- **Critical Threshold**: Specifies the number of issues after which the BI group's status changes to critical.

For example, if a group's warning threshold is set to 2 and the critical threshold to 4:

    When the number of issues reaches 2, the group's status changes to warning.
    When the number of issues reaches 4 or more, the group's status changes to critical.

These thresholds allow for flexible monitoring tailored to the infrastructure's specifics, enabling early detection of potential problems and the implementation of appropriate corrective actions.

The underlying logic behind the thresholds is as follows:

**"Best state"** is calculated by:

```
warning threshold = amount of members in a group -1
critical threshold = amount of members in a group -1
```
"**Worst state**" is calculated by:
```
warning threshold = 1
critical threshold = 1
```

To clarify with a example, let's assume we have 10 hosts and 1 of them experiences a malfunction of sorts.

-    Critical Threshold

    -   would occur if number of members with a critical state were to be bigger than a threshold.      

-    Warning Threshold

    -   would occur if number of members with a warning state were to be bigger than a threshold. 

-   Best State will take those 9 hosts working properly and display "Ok" status. 

-   Worst State will take that 1 host with a malfunction and display let's say "Critical" state. 

_Additional Information: Check [Essential Member](#essential-member)_

#### Scores

Calculates an overall state by summing the scores assigned to each sub-element (0 for OK, 1 for WARNING, 2 for CRITICAL) and then comparing that total against pre-set thresholds for a WARNING or OK condition.

Multiple sub-elements in a WARNING state are treated as equivalent to a mix of sub-elements in both OK and CRITICAL states.

    Scores(4,3,num) of {OK, OK, WARNING, CRITICAL} => WARNING
    Scores(4,3,num) of {OK, WARNING, WARNING, WARNING} => WARNING 
    Scores(4,3,num) of {WARNING, WARNING, WARNING, WARNING} => CRITICAL
    Scores(4,3,num) of {WARNING, WARNING, WARNING, WARNING} => CRITICAL

#### Essential Member

Essential members are critical sub-elements within a BI group that directly influence the overall health and state of a business process. By identifying and designating these indispensable components, the system ensures that their failure immediately reflects on the process status, regardless of the aggregate score calculated from non-essential elements.

The primary goal of marking essential members is to accurately identify and prioritize the health of components that are vital for business operations. This approach prevents scenarios where a majority of non-critical elements might mask the failure of a crucial service, thereby enabling operations teams to quickly pinpoint and address issues that have a high impact on the business process.

Furthermore, essential members simplify the overall monitoring logic. Instead of relying solely on the sum of individual scores (e.g., OK = 0, WARNING = 1, CRITICAL = 2) and pre-set thresholds, the failure of any essential member can trigger an immediate state change. This ensures that the integrity of critical business functions is maintained, and any deviation in their performance is promptly escalated for remediation.

    Consider a BI group that monitors a business process consisting of several services. Suppose one service, responsible for processing payments, is marked as an essential member:

    Non-Essential Members:
    These may include services like reporting, notifications, or logging, which contribute to the aggregate score but are not critical enough to override the process state on their own.

    Essential Member – Payment Processing:
    If the payment processing service transitions to a WARNING or CRITICAL state, the entire process is flagged as problematic immediately. This is done even if the overall score from non-essential members might otherwise fall within acceptable ranges.

#### Constant

This type of BI group is configured to always report a fixed status—OK, WARNING, or CRITICAL—regardless of the real-time conditions of its sub-elements.

- Fixed OK: The group always shows an OK status.
- Fixed WARNING: The group is permanently in a warning state.
- Fixed CRITICAL: The group continuously reports a critical status.
- Fixed UNKNOWN:  The group always returns an unknown status, indicating that the actual state cannot be determined or is not applicable.

This configuration is ideal for testing, overriding dynamic calculations, or maintaining consistent reporting in specific scenarios.


## Setup

In order to set up Business Intelligence the following must be done:

1. Enter "**Monitor**" -> "**Business Intelligence**":

![BI](/media/05_00_02_01_Business_Intelligence.png)

2. Create a group, consisting of objects of your preference with "**Create a New Group**" button

Available options include:

    -   Groups

    -   Hostgroups

    -   Servicegroups
    
    -   Hosts

    -   Services

Groups can be set as "**Primary Group**", this causes the group, as the name implies, to be the 1st in hierarchy. In the main window, such a group would be on the highest level. Although, there is no technical restriction to add 1 primary group under another primary one. 

In order to add 1 group into another, the following must be done:

-   Create the 2nd group, this one will be under the primary one. Pick objects of your preferrence, set up a name under "**Display Name**".

-   Create the 1st group and under "**Group Members**" pick your 2nd group.

-   Save the changes wit the "**Save**" button.


During creation of a group, few optional parameters can be chosen:

-  "**[Essential Member](#essential-member)**"

-   "**Deploy as a Service**"

    -   This option will create a service on the chosen host, specified under the "**Host**" field. 

    -   This service will be visible under the "**View**" button.

-   "**Primary Group**"    


![BI](/media/05_00_02_02_Business_Intelligence.png)

![BI](/media/05_00_02_03_Business_Intelligence.png)

![BI](/media/05_00_02_04_Business_Intelligence.png)

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
States in BI are the same as when using thresholds and notifications from the host main menu. The same logic applies. 
</blockquote>


![BI](/media/05_00_02_05_Business_Intelligence.png)

![BI](/media/05_00_02_06_Business_Intelligence.png)

Tick the "**checkboxes**" next to the menu You wish to hide, then save the settings with "**Save New Settings**" button.

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
It doesn't restrict access rights of the group in any capacity. 
</blockquote>
<br>


