# Administration

* Oracle Machine Learning is managed at the system level and at the application level by an administrator.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/33.PNG)

**Administrator:** 
* Creates, edits, and deletes Oracle Machine Learning user accounts. The Administrator reassigns user workspace.
**Developer:** 
* This is the default user role that allows you to create, and run notebooks, run SQL Statements, create SQL scripts, create jobs to schedule and run notebooks.

The tasks listed here can be performed by an administrator only.
**Administrative tasks:**
* User account and password creation
* Connection groups: View and reset
* Compute resource: View
* User data administration: Delete all users, all user-related objects such as workspace, projects and notebooks, and workspace reassignment.

## User Data

On the User Data page in Oracle Machine Learning, you can view existing user data, reassign, and delete it.
* The User Data page lists details of a Oracle Machine Learning user such as name, role, comments, and last updated date. 

You can perform the following tasks:
* **Delete User Data:** To delete a user, select the user to delete and click Delete User Data.
**Reassign:** Reassign workspace and templates from one user to another.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/31.PNG)

The Reassign option allows you to reassign workspaces, along with templates, from one user to another. 

To reassign workspaces: 
* On the User Data page, select the user from whom you want to reassign workspace and click Reassign. 
* You can reassign templates 
* Choose the workspaces to reassign
 
* After the templates and workspaces are reassigned successfully, a notification message is displayed on the User Data page with the number of templates and workspaces reassigned.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/c32.PNG)

## Compute Resource

* Compute resource refers to services such as a database, or any other back-end service to which a Zeppelin Interpreter connects.
* The Compute Resources page displays the list of compute resources along with the name of each resource, its type, comments, and last updated details. 

To view details of each compute resource, click the compute resource name. The following connection details are displayed:
* Name
* Comment
* Host
* Port

**Note: You must have the administrator role to access the Compute Resources page.**

## Creating User Accounts for Oracle Machine Learning

* The ADMINuser creates the user account and user credentials for Oracle Machine Learning (OML) in the User Management interface.
* You must have the administrator role to access the Oracle Machine Learning User Management interface.

A user must have the administrator role to access the Oracle Machine Learning User Management interface.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/34.PNG)

When choosing to have a temporary password generated for the user. The user has to reset the password on first sign in.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/35.PNG)