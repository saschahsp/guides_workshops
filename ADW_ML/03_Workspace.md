# Workspace

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/2.PNG)

A project is a **container** for your **notebooks**, and a **workspace** is a container for your **projects**. You can own multiple projects in a workspace. 

The initial workspace and the **default project** is created by the Oracle Machine Learning service automatically when you log in to Oracle Machine Learning for the first time. To create a new project and a workspace: 

On the top right corner of Oracle Machine Learning home page, click the project workspace **drop-down list**. The project name and the workspace, in which the project resides, are displayed. The menu will also give you access to Recent Projects, New Project, Manage Workspaces and Workspace Permissions. 

**Note**: The **last project** that you have worked on is stored in the browser **cache** and is the default project. If you clear the cache, then no default exists and you must select a project.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/6.PNG)

A workspace is an area where you can **store** your projects, and share with other users to collaborate in your project.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/7.PNG)

In order to **create** a new **workspace** for a new project. Click on the plus sign to do so.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/8.PNG)

You can provide access to the workspace, **manage permissions** for users, and edit and delete a workspace

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/9.PNG)

For **collaborating with other** users, you can provide different levels of **permission** such as VIEWER, DEVELOPER, or Manager

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/10.PNG)

Oracle Machine Learning allows three types of permissions.

* Manager
* Developer
* Viewer

Permission Type | Action based on permission |
---------|----------|
 **Manager** | **Project:** Create, Update, Delete | 
 ..| **Workspace:** View only | 
 .. | **Notebooks:** Create, update, run, and delete, and Schedule jobs |
 **Developer** | **Project:** View only| 
 .. | **Workspace:** View only| 
 .. | **Notebooks:** Create , update, run, delete notebooks that a developer creates only| 
 .. | **Jobs:** View and run jobs of shared notebooks only. A developer cannot create jobs for notebooks that are shared| 
 **Viewer** |  **Project:** View only| 
 .. | **Workspace:** View only| 
 .. | **Notebooks:**  View only| 
 .. | **Jobs:** View jobs and job runs of shared notebooks only|

**Note:** A user with the Manager or Developer permission type can also drop tables and run any script at any time on the owner’s account

