# User Manual

## Overview

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

### Configuration Shortcuts

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
