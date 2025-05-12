# Saving the changes into the database

- In order to save any changes the user makes into the database for LogMonitor to recognize, after inputting changes, the user must enter "Save" menu on the right side of the UI, then press "write changes to the database" button.

- Data prior to being saved to the database is stored in a buffer, as an additional protection from inserting changes by mistake. All changes must be confirmed by the user.  

![help_in_line](/media/03-00-01_Saving_to_the_database_1.png)

- If the changes user makes, like renaming a host or a service, would result in affecting other data, EnergyMonitor will display an appropriate warning:

![database_historical_data_warning](/media/03-00-02_database_historical_data_warning.png)

- EnergyMonitor allows the user to see specifically what host or services are affected by the changes.

- Clicking on the entry will take the user to the particular host or service that is being changed.

![database_changes](/media/03-00-03_database_changes.png)

- After successful saving, the user will see the following confirmation.

![database_changes_saved](/media/03-00-04_database_changes_saved.png)

<blockquote style="border-left: 8px solid green; padding: 15px;"> <b>Note</b>: Keep in mind that a user needs <strong>"export permissions"</strong> to save changes.
</blockquote>





