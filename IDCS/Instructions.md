**User Management**

1.  Navigate to the User Management Interface (top right)

\1png

2. Navigate to the Identity Console (top right)

\2png

The Identity Cloud Console has multiple tabs (with the right access). 

\3

\4

The dashboard displays an overview about:

* Users
* Applications
* Groups
*  Passwords
* Logins
* Reports
* Directory Integration
* Single Sign-On
* Identity Providers

**User Tab**

3. Navigate to the Users Tab

\5

The user interface enables the following capabilities:
* Create a User (Add)
* Import and Export Users
* Activate and Deactivate Users
* Resend Invitation (More)
* Reset Password (More)
* Remove (More)
* Reset all Passwords (More)

**Groups Tab**

4. Navigate to the Groups Tab

\6

The user interface enables the following capabilities:
* Add Group
* Remove a Group
* Import and Export Groups

**Application Tab**

5. Navigate to the Applications Tab

\7

The user interface enables the following capabilities for applications:
* Add 
* Remove
* Activate
* Deactivate

**Jobs Tab**

6. Navigate to the Jobs tab

\8

The Jobs tab displays jobs that has been run, f.e. an Application Role Memberships Export

**Reports tab**

7. Navigate to the Reports tab

\9

The reports interface gives the capabilities to navigate to reports regarding users and applications.

8. Click on Successful Login Attempts

\10

Here you can see the Successful Login Attempts. It is also possible to change the Date Range and Download the Report. 

**IDCS Settings**

9. Click on Settings on the sidebar

\11

The top down menu enables the navigation to the following sections:
* Default Settings

Specify whether users can set their own password recovery email address, the default tenant locale, and the default tenant contact information for an identity domain

* Partner Settings

Add, manage, and use trusted partner certificates

* Notifications

Customize and use notifications

* Password Policy

Set, test, modify, and evaluate password policies

* Branding

Customize the Sign In page and brand the Identity Cloud Service console and notification templates by
adding logos to them

* Directory Integrations

Create, manage, and remove bridges, such as Microsoft Active Directory

* Session Settings

Specify the session expiration and the logout URL for an identity domain

* Self Registration

Create self-registration profiles to manage different sets of users, approval policies, and applications

* Downloads

Download software development kits (SDKs) to enable your mobile and Web applications to authenticate and integrate with Oracle Identity Cloud Service, the Oracle E-Business Suite (EBS) Asserter to integrate Oracle E-Business Suite with Oracle Identity Cloud Service, or the Secure Form

Fill Client to configure Secure Form Fill for your applications

* Schema Management

Manage schema for Identity Cloud Service user

**Security**

10. Click on Security

\12

The top down menu enables the navigation to the following sections:

* Administratiors

After you create or import user accounts, delegate administrative responsibilities for these accounts

* Adaptive Security

Activate adaptive security, and add, manage, and use risk providers

Adaptive Security is an advanced feature that provides strong authentication capabilities for your users, based on their behavior within Oracle Identity Cloud Service, and across multiple heterogeneous on-premises applications and cloud services.

When activated, the Adaptive Security feature can analyze a user’s risk profile within Oracle Identity Cloud Service based on their historical behavior, such as too many unsuccessful login attempts, too many unsuccessful MFA attempts, and real-time device context like logins from unknown devices, access from unknown locations, blacklisted IP addresses, and so on. 

* Identity Providers

Add, manage, and use identity providers

An identity provider, known as an Identity Assertion provider, provides identifiers for users who want to interact with Oracle Identity Cloud Service using a website that's external to Oracle Identity Cloud Service. A service provider is a website such as Oracle Identity Cloud Service that hosts applications. You can enable an identity provider and define one or more service providers. Your users can then access the applications hosted by the service providers directly from the identity provider.

* IDP Policies

Create, manage, and remove identity provider (IDP) policies

* Sign-On Policies

Create, manage, and remove sign-on policies

* Network Perimeters

Define network perimeters

* MFA (Mobile App, SMS, Security Questions, Email)

Enable and disable Multi-Factor Authentication (MFA), and configure MFA settings

* OAuth

Configure the OAuth settings. 

* Delegated Athentication

Configure delegated authentication for bridges associated with Microsoft Active Directory domains

11. Navigate to the users tab and click on Add to create a new user.

\13

12. Type in the ncessary information and click on next. It is also possible to finish the process already, but the next already enables group assignments. 

\14

13. Assign the user to the OCI_Administrators group

\15

In step 2 its possible to assign users to groups already. 

14. Navigate back to the user tab and click in the created user

\16

You can also assign the user to a group or application in the displayed interface. 

15. Click on your user on the top right corner and on My Home to navigate back to the home dashboard

\17

16. Click in Users to reach User Management

\18

**User Roles**

17. Click and the newly created user and then roles.

\19

For the user to have service entitlements and/or access to the instances, it is necessary to assign a role (admin or user. You can do it manually for each service / instance or add the role to all services / instances with one click.

18. Click on Add User Roles to assign the user role for all services / instances for the given user

**OCI Identity Management**

19. Navigate to the OCI Identiy management. One way would be to click on Atonomous Data Warehouse under services and then scroll down to Identity 

\20
\21

Some services require users in the OCI environment with an AuthT oken. One example would be a user than can access the Object Storage Buckets, f.e. for manual backups. 

20. Click on create user and fill out the necessary information

\22

21. Navigate to the Auth Tokens tab on the left-hand side. 

\23

22. Click on generate Auth Token, fill in a description and click generate Token

Make sure to copy and save the Auth Token somewhere in a safe and dedicated place, because it is not possible to see and copy it after you have closed the window.

**Compartments**

23. Scroll up and navigate back to the Identity tab. Then click on Compartments

\24

A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. The compartments are herarchisch, meaning it starts with the root and branches out to child compartments, which can have their own child compartments. 

**Policies**

24. Navigate to the Policies tab

\25

A document that specifies who can access which resources, and how. Access is granted at the group and compartment level, which means you can write a policy that gives a group a specific type of access within a specific compartment, or to the tenancy itself. If you give a group access to the tenancy, the group automatically gets the same type of access to all the compartments inside the tenancy. For more information, see Example Scenario and How Policies Work. The word "policy" is used by people in different ways: to mean an individual statement written in the policy language; to mean a collection of statements in a single, named "policy" document (which has an Oracle Cloud ID (OCID) assigned to it); and to mean the overall body of policies your organization uses to control access to resources.

