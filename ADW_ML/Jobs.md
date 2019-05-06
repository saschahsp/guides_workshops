# Jobs

Jobs allow you to create schedules to run notebooks. In the Jobs page, you can create and schedule jobs, monitor job status, and view job logs as read-only notebooks.  

The Jobs page lists all the jobs created, along with the job name notebook, owner of the job, last start date, next run date, status, and schedule. 

You can perform the following tasks:  
• Edit jobs: You can edit the metadata of any job listed in the Jobs page. Click Edit to edit the 
selected job. 
• Create jobs: Click Create to create a new job to schedule your Notebook. 
• Duplicate jobs: You can create a copy of an existing job listed in the Jobs page. 
Click Duplicate to make a copy of the selected job. 
• Stop jobs: Click Stop to terminate a job that is currently running. 
• Delete jobs: Click Delete to delete any job listed in the Jobs page

You can reach the Job section via the side menu or the quick actions.

You can create jobs to schedule your notebook with preferred scheduling settings.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/c28.PNG)

Following **settings** are possible:

* **Start date and time** (be wary of timezone settings)
* **Frequency:** To set the repeat settings and frequency. You can set the frequency in minutes, hours, days, week, and month. 
* **Custom:** To customize the job settings 

**Advanced Settings**, select one or more of the following options: 
* **Maximum Number of Runs:** To specify the maximum number of times the job must run before it is stopped. When the job reaches the maximum run limit, it will stop. 
* **Maximum Failures Allowed:** To specify the maximum number of times a job can fail on consecutive scheduled runs. When the maximum number of failures is reached, the next run date column in the Jobs UI will show an empty value to indicate the job is 
no longer scheduled to run. The Status column may show the status as Failed. 
* **Timeout in Minutes**: To specify the maximum amount of time a job should be allowed to run.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/c29.PNG)

## Viewing Job Logs

* You can view the historical logs of any particular job in the Job Log interface.
* You can view a log in a read-only notebook.

To view job logs:
* To view the history of a job, select the job and click the view icon.
* To delete a particular job log, select it and click the delete icon

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/c30.PNG)

