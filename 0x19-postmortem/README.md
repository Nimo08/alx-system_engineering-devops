# THE ARCHIVE CRASH INCIDENT REPORT 
	
![image](postmortem-img.png)

## Issue summary
At 11:27 AM, user reports to the Archive’s social media support handle stated that requests from users’ attempts at logging into the archive resulted in a 500 error response message. The issue affected all the users logged out of the archive portal at the time and therefore restricted access to the archive.

## Timelines (UTC+3)
- 11:20 AM: An update to a configuration file is pushed
- 11:27 AM: User reports of 500 error message flow in
- 12:34 PM: Pagers alerted the incident response team
- 1:05 PM: Issue is traced to a recent configuration update, using a new module not present in dependent scripts
- 1:45 PM: Successful update of dependent scripts with integration of the new module
- 1:53 PM: The servers are restarted
- 2:00 PM: Users are notified of the fix and requested to retry logging in
- 2:05 PM: User reports of successful login as well as access to their archive account

## Root Cause
At 11:20 AM, a configuration script was updated and among the updates was the addition of an upgraded version of one of the imported modules. This led to an error caused by the incompatibility of the updated configuration script with other configuration scripts due to the outdated versions of the module existing in the other configuration scripts. This resulted in an internal server error, which in turn, caused a failure in user access to the archive.

## Resolution and Recovery
At 1:05 PM the issue is traced to the recently updated script containing the new module. At 1:45 PM the scripts dependent on the update are modified to allow compatibility with the new module and at 1:53 PM the servers are restarted. The users are notified of the reload at 2:00 PM and advised to retry logging in to the library accounts. At 2:05 PM, users notify the archive's team that the website is up and running through the archive’s social media support handle.

## Corrective and Preventative Measures
An internal review of the website crash has been initiated with focus on the issues below:
- Introduction of a review process when making changes to configuration files i.e., a questionnaire provided to the engineers before pushing changes to ensure dependent scripts are not affected.
- Integration of a quarterly analysis of the current modules and dependencies in use to ensure updates to the software are made every quarter.

## Conclusion
The Archive is committed to improving our technology and operational processes to prevent site crashes. We appreciate your patience and apologize for the impact the crash had on our users. We thank you for your continued support.

Sincerely, 
The Archive’s Incident Response Team
