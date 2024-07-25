# Overseeing Hosts and Services

The following procedures outline how to add, update, and configure monitoring objects, including:

- Hosts and host groups
- Services and service groups

The sequence in which you create hosts, services, and their respective groups does not matter. For instance, you can add a host to an existing host group or create a new host group and then add a host to it. Additionally, a host can be added to multiple groups.

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: Configuration changes are not finalized until you click Save, which saves your changes to the Energy Monitor database. For more details, refer to Saving configuration changes and viewing the changelog in the Introduction to configuration.
</blockquote>

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Caution</b>: Using the user interface to configure Energy Monitor objects is the only supported method for updating object configurations in Energy Monitor. We do not support direct modifications to object configuration files. Energy Monitor uses Livestatus to parse configuration files, and manual changes to these files can cause conflicts with Livestatus data and API calls. However, advanced users can create custom configuration files.</blockquote>
<br>

For background information on hosts, services, host groups, and service groups, see Monitoring objects in [Overview of Energy Monitor](../01-00-00-About/01-00-02-Overview.md).
