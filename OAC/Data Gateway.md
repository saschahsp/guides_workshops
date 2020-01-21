# About Connecting to On-premises Data Sources

You connect to on-premises data sources using Oracle Analytics Cloud Data Gateway. Data Gateway enables you to deploy Oracle Analytics Cloud with large on-premises data sets **without migrating the data to the cloud**. Users can analyze the data in data visualizations, and in reporting dashboards and analyses.

You can install Data Gateway agents on Linux, MacOS, or Windows operating systems.

**Data Gateway agents poll Oracle Analytics Cloud for queries to run against your on-premises data sources. The results of these queries are returned to Oracle Analytics Cloud.**

Data Gateway replaces the Remote Data Connector utility that was used in earlier releases. Although you can still use Remote Data Connector, it's deprecated starting with Oracle Analytics Cloud 105.3 and will be removed in future releases no sooner than six months from the release of 105.3. Oracle recommends moving to Data Gateway within six months of the release of version 105.3 in order to avoid loss of functionality. See Install the Legacy Remote Data Connector.

Functionality and Limitations

You can either use Data Gateway or Remote Data Connector but not both.
Data flows can source data from remote connections. However, data flows can't save data to data sets that use remote connections.

Supported Data Sources

Look for databases with a "Yes" in the "Remote Connection for Data Sets" column or in the "Remote Connection for Data Models" column in Supported Data Sources.

Deploying Multiple Data Gateway Agents

You can deploy multiple Data Gateway agents so that there's no single point of failure. Deploying multiple Data Gateway agents might also improve performance. When you register an agent using the Data Gateway Agent Configuration dialog, note the following:

Each agent must be able to serve all remote queries. You can't target specific queries at specific agents.
If you leave the Allowed Hosts field blank, the agent tries to reach a data source on any host based on the connection information it retrieves from a connection in Oracle Analytics Cloud. If you specify hosts in the Allowed Hosts field, only those hosts can be addressed by the agent.
You can leave the Allowed SQL Statements blank. By default, the current release of Data Gateway only supports select statements. This restriction also applies to Data Model on-connect and on-query scripts.



## Requirements



- Credentials and Privileges to install software on the RDG host
- Database connection information and credentials for validating the installation
- The IP address or host name where RDG is to be installed
- Routing rules allowing user access to Identity Cloud Service (IDCS) and OAC via the Internet
- Routing rules allowing user access to the Dynamic Routing Gateway (DRG) described below; and to IDCS via the internet, if it is in a different region




## Steps


1. Install DataGateway on Linux Server
2. 