# User Manual

Configuration tasks can be carried out either through the Energy Monitor user interface or via the command line. These tasks should only be performed by users with the necessary experience and permissions, particularly when using the command line.

## Configuration Page

Most of Energy Monitor's key configuration functions can be found on the configuration page, accessible by clicking **Manage -> Configure**.

![Configuration_page](/media/04_01_configuration_page.png)

From the configuration page, you can manage the following:

- **Monitoring objects**
- **Users, contacts, and permissions**
- **Reusable objects**: This includes templates, time periods, management packs, and commands. For more details, see [Reusable configuration](#reusable-configuration).
- **Graphs**

Additional tasks you can perform:

- Search for an existing host to configure.
- View a list of plugins along with their support details.

### Common Configuration Features

Different configuration functions share some common features:

- **Search field**: Enter an existing configuration object to edit, or click **New** for a new configuration.
- **Related items links**: Access related configuration items from the links on the right.
- **Object type menu**: Switch between configuration pages for different object types using the menu on the right.
- **File ID field**: Located at the bottom of the configuration values, this field specifies the system configuration file in the /etc directory where the configuration is stored, such as `/etc/hosts.cfg`.
  
<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: It is not recommended to update the system configuration file directly.
</blockquote>

#### Configuration Shortcuts

Energy Monitor provides several shortcuts to streamline the configuration process:

- Clone objects
- Copy objects
- Propagate settings from one object to other objects of the same type
- Delete objects
- Bulk delete objects

You can switch between object types using the **Object type menu** to view and configure related items. These shortcuts work consistently across all object types.

### Saving Configuration Changes and Viewing the Changelog

To save your configuration changes, click **Save** in the top bar of the configuration page. Energy Monitor usually saves most configuration objects to the configuration database, with some exceptions such as the Permissions section. Visual cues indicate when you need to save a configuration, as explained in the workflow below:

1. Click an object on the configuration page and make changes.
2. Click **Submit**.
3. Repeat steps 1 and 2 as needed.
4. Click **Save** in the top bar of the configuration page to save all your changes and those made by other users.

When there are unsaved changes, the number of unsaved changes appears next to the **Save** button, and details are displayed next to the objects with unsaved changes.

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Note</b>: Users need export permissions to save changes.
</blockquote><br>

Additional actions you can perform:

- **Undo**: To revert all user changes since the last save, click **Undo**. This action provides the option to perform a complete reimport by clicking the displayed link.
- **Changelog**: View the history of all configuration changes by clicking **Changelog**. Filter the list of changes by clicking **Toggle filter bar** and entering details of users, objects, and dates. Users with limited permissions will only see changes on hosts and services for which they are contacts.

### Reusable Configuration

You can set up the following reusable configurations for use with other objects:

- Time periods
- Templates
- Commands

Energy Monitor comes with default reusable configurations for each of these types. You can either use these default settings, modify them, or create your own custom configurations.

### View active config

To view the details of the current configuration, select **Manage > View active config** from the menu. Use the **Object type** drop-down list to choose the specific object you wish to view.

You can view configurations for the following types:

- Hosts
- Services
- Host groups
- Service groups
- Contacts
- Contact groups
- Time periods
- Commands

To filter the displayed objects, enter a term in the filter field and click **Filter**. Additionally, you can click on links within the view to access details of related object configurations. For example, clicking a link in the **Host Check Command** column will take you to the related commands view.

### Commands and custom variables

You can define command lines and create custom variables when setting up configuration objects, including templates, hosts, services, and contacts.

### Configuration synchronization in distributed environment

In a distributed or load-balanced monitoring environment, Energy Monitor’s Merlin back end manages the synchronization of configuration updates on the master server.

## Overseeing Hosts and Services

The following procedures outline how to add, update, and configure monitoring objects, including:

- Hosts and host groups
- Services and service groups

The sequence in which you create hosts, services, and their respective groups does not matter. For instance, you can add a host to an existing host group or create a new host group and then add a host to it. Additionally, a host can be added to multiple groups.

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: Configuration changes are not finalized until you click Save, which saves your changes to the Energy Monitor database. For more details, refer to Saving configuration changes and viewing the changelog in the Introduction to configuration.
</blockquote>

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Caution</b>: Using the user interface to configure Energy Monitor objects is the only supported method for updating object configurations in Energy Monitor. We do not support direct modifications to object configuration files. Energy Monitor uses Livestatus to parse configuration files, and manual changes to these files can cause conflicts with Livestatus data and API calls. However, advanced users can create custom configuration files.</blockquote>
<br>

For background information on hosts, services, host groups, and service groups, see Monitoring objects in [Overview of Energy Monitor](../01-00-00-About/01-00-02-Overview.md).

### Procedure for Adding Windows Hosts to the Energy Monitor System

Adding Windows hosts to the Energy Monitor system requires several steps, which include installing the necessary software, configuring the monitoring agent, and verifying the connection. Below is a detailed procedure:

#### Step 1: Prepare the Windows Host

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Ensure you have administrative access to the Windows host:
You need administrative privileges to install software on the Windows host.</b>
</blockquote><br>

Install the required tools:

- Download and install NSClient++ (a monitoring tool for Windows systems) from the [NSClient++ website](https://www.nsclient.org/download/).

#### Step 2: Install and Configure NSClient++

1. **Install NSClient++**:

    - Run the downloaded installer and follow the installation instructions. Choose options such as installing it as a Windows service.
    ![first_step](/media/04_01_nsc_1.png)
    - Provide atleast one ip of Energy Monitor instance.
    ![second_step](/media/04_01_nsc_2.png)
    - Confirm start of installation process.
    ![final_step](/media/04_01_nsc_3.png)

1. **Configure NSClient++**:

    - Open the configuration file nsclient.ini, typically located in the NSClient++ installation directory (e.g., C:\Program Files\NSClient++).
    - Edit the configuration file to allow communication with the Energy Monitor server. Ensure that the appropriate modules are enabled, such as NRPE and CheckExternalScripts.

    Example configuration:

    ```ini
    [/settings/default]

    ; Undocumented key
    allowed hosts = 192.168.3.5


    ; in flight - TODO
    [/settings/NRPE/server]

    ; Undocumented key
    ssl options = 

    ; Undocumented key
    verify mode = none

    ; Undocumented key
    insecure = true

    ; Allow Arguements
    allow arguments = true

    ; Allow nasty chars
    allow nasty characters = true


    ; in flight - TODO
    [/modules]

    ; Undocumented key
    CheckExternalScripts = enabled

    ; Undocumented key
    CheckHelpers = enabled

    ; Undocumented key
    CheckEventLog = enabled

    ; Undocumented key
    CheckNSCP = enabled

    ; Undocumented key
    CheckDisk = enabled

    ; Undocumented key
    CheckSystem = enabled

    ; Undocumented key
    NSClientServer = enabled

    ; Undocumented key
    NRPEServer = enabled
   ```

1. **Restart the NSClient++ service**:

    - After making changes to the configuration file, restart the NSClient++ service using the Windows Services Manager.

#### Step 3: Configure Energy Monitor

1. **Log in to the Energy Monitor web interface**:

    - Open a web browser and log in to the Energy Monitor admin panel.

1. **Add a new host**:

    - Navigate to Manage -> Configure -> Hosts.
    ![win_add_host](/media/04_01_win_em_1.png)

1. **Enter host details**:

    - Provide the hostname, IP address, and other required details.
    ![win_add_host2](/media/04_01_new_host.png)

1. **Save the configuration and perform a test**:

    - Save the new host configuration and perform a monitoring test to ensure that Energy Monitor can communicate with the Windows host correctly.
    ![save](/media/04_01_save.png)

#### Step 4: Add services

Add monitoring services such as availability checks, CPU usage, memory usage, disk usage, etc., using NSClient++ as the data source.

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Ensure that you use the appropriate NRPE commands or other commands defined in the nsclient.ini file.</b>
</blockquote><br>

1. **Search for added host**:

    - Use a search bar
    ![search_host](/media/04_01_win_search.png)

1. **Open configuration**:

    - Open configuration of freshly added host from listview:
    ![open_config](/media/04_01_win_conf.png)
    - After open host configuration got to it services configuration:
    ![open_service_config](/media/04_01_win_conf_serv.png)

1. **Add service**:

    - Fill service description(reuired)
    - Choose correct `check_command` to monitor required parameter
    - Fill `check_command_args` if required or create `Custom Variable`
    ![service_desc](/media/04_01_win_conf_serv_new.png)

1. **Test if configuration of new service is correct**:

    - After filled up necessary firlds you can check response of service by clicking in `Test This Check`:
    ![test_this_check](/media/04_01_win_conf_serv_test.png)

1. **Submit and Save**

    - All changes in configuration(like adding new object) need to be submited by clicking in submit button at the bottom of object configuration page.
    - Next you need to perform save like at "Add host" step.
    - Before perform save you can add as many services as you want.

#### Step 5: Verification and Monitoring

1. **Check the status of the host and services**:

    - Ensure that the newly added host and its services are visible in the Energy Monitor dashboard and that real-time data is being received.

1. **Configure notifications**:

    - Set up appropriate notifications to receive alerts in case of issues with the monitored Windows host.

### Procedure for Monitoring Linux Systems with Energy Monitor

This documentation provides a step-by-step guide on how to monitor Linux systems using Energy Monitor. By following these instructions, you will be able to set up monitoring for various aspects of your Linux hosts, such as system performance, availability, and resource usage.

##### Prerequisites

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Ensure that you have Energy Monitor installed and configured.</b>
</blockquote><br>
<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Ensure you have administrative access to both the Energy Monitor server and the Linux systems you want to monitor.</b>
</blockquote>

#### Step 1: Install NRPE and Nagios Plugins on Linux Host

1. **Update Package Repository**:

   ```bash
   sudo apt update  # For Debian/Ubuntu
   sudo yum update  # For CentOS/RHEL
   ```

2. **Install NRPE and Nagios Plugins**:

   ```bash
   sudo apt install nagios-nrpe-server nagios-plugins  # For Debian/Ubuntu
   sudo yum install nrpe nagios-plugins-all  # For CentOS/RHEL
   ```

3. **Configure NRPE**:
   - Open the NRPE configuration file:

     ```bash
     sudo vim /etc/nagios/nrpe.cfg  # Path may vary depending on distribution
     ```

   - Add the IP address of your Energy Monitor server to the `allowed_hosts` directive:

     ```ini
     allowed_hosts=127.0.0.1,ENERGY_MONITOR_SERVER_IP
     ```

4. **Define Commands in NRPE Configuration**:
   - Add or modify commands in the `nrpe.cfg` file to match your monitoring requirements. Here are some example command definitions:

     ```ini
     command[check_load]=/usr/lib/nagios/plugins/check_load -w 5,4,3 -c 10,8,6
     command[check_disk]=/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /
     command[check_procs]=/usr/lib/nagios/plugins/check_procs -w 150 -c 200
     ```

5. **Restart NRPE Service**:

   ```bash
   sudo systemctl restart nagios-nrpe-server  # For Debian/Ubuntu
   sudo systemctl restart nrpe  # For CentOS/RHEL
   ```

#### Step 2: Configure Energy Monitor

1. **Log in to the Energy Monitor web interface**:

    - Open a web browser and log in to the Energy Monitor admin panel.

1. **Add a new host**:

    - Navigate to Manage -> Configure -> Hosts.
    ![win_add_host](/media/04_01_win_em_1.png)

1. **Enter host details**:

    - Provide the hostname, IP address, and other required details.
    ![win_add_host2](/media/04_01_new_host_lin.png)

1. **Save the configuration and perform a test**:

    - Save the new host configuration and perform a monitoring test to ensure that Energy Monitor can communicate with the Windows host correctly.
    ![save](/media/04_01_save.png)

1. **Save Configuration and Apply Changes**:
   - Save your configuration changes and apply them. This will update the Energy Monitor system to start monitoring the new Linux host and its services.

#### Step 3: Add services

1. **Search for added host**:

    - Use a search bar
    ![search_host](/media/04_01_lin_search.png)

1. **Open configuration**:

    - Open configuration of freshly added host from listview:
    ![open_config](/media/04_01_lin_conf.png)
    - After open host configuration got to it services configuration:
    ![open_service_config](/media/04_01_lin_conf_serv.png)

1. **Add service**:

    - Fill service description(reuired)
    - Choose correct `check_command` to monitor required parameter
    - Fill `check_command_args` if required or create `Custom Variable`
    ![service_desc](/media/04_01_lin_conf_serv_new.png)

1. **Test if configuration of new service is correct**:

    - After filled up necessary firlds you can check response of service by clicking in `Test This Check`:
    ![test_this_check](/media/04_01_lin_conf_serv_test.png)

1. **Submit and Save**

    - All changes in configuration(like adding new object) need to be submited by clicking in submit button at the bottom of object configuration page.
    - Next you need to perform save like at "Add host" step.
    - Before perform save you can add as many services as you want.

#### Step 4: Verification and Monitoring

1. **Verify Host and Services Status**:
   - Check the Energy Monitor dashboard to ensure the newly added Linux host and its services are listed and being monitored.

2. **Set Up Notifications**:
   - Configure notifications to alert you in case of any issues with the monitored Linux host. Navigate to `Configuration` -> `Notifications` and set up your preferred notification methods (e.g., email, SMS).

### Benefits of Monitoring with Energy Monitor

- **Centralized Monitoring**: Ability to monitor all Linux systems from a single, central location.
- **Early Problem Detection**: Quickly identify performance and availability issues.
- **Compliance with Security Policies**: Maintain compliance with internal and external security requirements.
- **Automation of Management**: Automated data collection and reporting streamline IT infrastructure management.

By following this procedure, you can effectively monitor your Linux systems using Energy Monitor, ensuring high levels of system availability and performance.

## Business Intelligence (BI)

### Overview

Energy monitor integrates monitoring with Business Intelligence (BI) to provide an overview of the applications and services your organization offers, both to customers and internally. You can share the BI services you create with other business units and organizations, making them valuable in scenarios where an overview and state information are needed on a specific service, such as supporting non-technical staff in service delivery or fulfilling Service Level Agreement obligations.

#### Designing a Business Intelligence

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
