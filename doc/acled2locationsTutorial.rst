
========================================================
Automation for creating a locations .csv from ACLED Data
========================================================

| By using the ``fabsim process_acled`` command it is possible to construct a locations.csv file using data from `acleddata.com <https://www.acleddata.com>`_  for use in FabFlee simulations. The locations.csv will be in the following format:


+------+--------+---------+-----+------+---------------+---------------+---------------------+
| name | region | country | lat | long | location_type | conflict_date | population/capacity |
+======+========+=========+=====+======+===============+===============+=====================+
| A    |   AA   |   ABC   | xxx |  xxx |    conflict   |      xxx      |         xxx         |
+------+--------+---------+-----+------+---------------+---------------+---------------------+
| B    |   BB   |   ABC   | xxx |  xxx |    conflict   |      xxx      |         xxx         |
+------+--------+---------+-----+------+---------------+---------------+---------------------+
| C    |   CC   |   ABC   | xxx |  xxx |    conflict   |      xxx      |         xxx         |
+------+--------+---------+-----+------+---------------+---------------+---------------------+

|
| For more information on FabFlee Simulation Instance construction see the Simulation Instance Construction Tutorial `here <https://github.com/djgroen/FabFlee/blob/master/doc/TutorialConstuct.md>`_

Procedure
---------

Getting Conflict Data from ACLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The Armed Conflict Location and Event Data Project (ACLED) database provides conflict location data for forced displacement simulations. 
| To obtain data on chosen conflict situation, complete the ACLED data export tool fields (https://www.acleddata.com/data) as follows:

- Provide dates of interest for conflict situation (i.e. From and To).
- Select Event Type: Battles.
- Select Sub Event Type: Armed clash, Attack, Government regains territory and Non-state actor overtakes territory.
- Specify Region and Country of conflict situation choice.
- Accept Terms of Use and Attribution Policy.
- name.csv file exports to Downloads automatically.

| There are two options at this point:
|
|   1. Rename the file acled.csv and place it in the relevant config files directory. For example, if you collected data for Mali, you would place it in '/FabFlee/Config_Files/mali'
|
|   2. Keep it as it is, and use a path argument when issuing the process_acled command.
|

Using the Command
^^^^^^^^^^^^^^^^^
| The command uses the following syntax:
| ``fabsim localhost process_acled:country="country",start_date="dd-mm-yyyy",filter="[earliest/fatalities]"``
|
| If your .csv file is not stored in the country directory:
| ``fabsim localhost process_acled:``country="country",start_date="dd-mm-yyyy",filter="[earliest/fatalities]",path="\path\to\acled_csv"``

 - **country** is the name of the country directory the acled.csv is stored in.
 - **start_date** uses dd--mm-yyyy format and is the date which conflict_date will be calculated from.
 - **filter** takes earliest or fatalities. Earliest will keep the first occurring (using date) location and remove all occurrences that location after that date. Fatalities will keep highest fatalities of each location and remove all other occurences of that location.
 - **path** is the path to your acled csv file if it is not already stored in config_files. This argument is optional.

|
| The following example uses Mali as the country. 
|
| ``fabsim localhost process_acled: country=mali,start_date=20-01-2010,filter=earliest``     
| 
| This will output a locations.csv into the input_csv directory for the given country, so in this case the .csv can be found in /FabFlee/config_files/mali/input_csv/locations.csv. If there is not input_csv folder, one will be created.
| 
| Currently the population figures for each location will need to be collected and written to the "population/capacity" column manually using a resource such as `www.citypopulation.de <https://www.citypopulation.de>`_.
