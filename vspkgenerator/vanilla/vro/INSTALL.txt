VSPK Plug-In for VMWare vRealize Orchestrator (vRO) README

1. Install VSPK plug-in for vRO 7.0.x:

   a. In a web browser, go to the IP address of your Orchestrator Appliance virtual machine: http://orchestrator_appliance_ip
   b. Click the "Orchestrator Control Center" link
   c. Login to Control Center
   d. Click the "Manage Plug-Ins" icon
   e. Click the "Browse..." button
   f. Select the plug-in installer file to install:
       i) For a VSD 3.2.x compatible plug-in, use o11nplugin-3.2.x.vmoapp
      ii) For a VSD 4.0.x compatible plug-in, use o11nplugin-4.0.x.vmoapp
   g. Click "Open"
   h. Put a check mark beside "Accept EULA"
   i. Click the "Install" button. The plug-in version information should be displayed
   j. Click the "Install" button
   k. Click the "Statup Options" link
   l. Click the "Restart" button

2. Start the Orchestrator Client:

   a. In a web browser, go to the IP address of your Orchestrator Appliance virtual machine: http://orchestrator_appliance_ip
   b. Click "Start Orchestrator Client" link
   c. The IP address of the Orchestrator Appliance should be displayed in the "Host Name" text box
   d. Log in by using the Orchestrator client user name and password
   e. If a Security Warning window pops up, select "Install this certificate and do not display any security warnings for it anymore." and click "Ignore" to install the certificate

3. Verify that VSPK plug-in is properly installed in vRO:

   a. In the Orchestrator Client main window, select Help->Installed plug-ins...
   b. Check that VSPK (version 3.2.x or 4.0.x) shows up in the list of installed plug-ins

5. Enable context menus in Orchestrator Client:

   a. In the Orchestrator Client main window, select Tools->User preferences...
   b. Click "Inventory" on the left
   c. Put a check mark beside "Use contextual menu in inventory"
   d. Click "Save & Close"

4. Create a session to a VSD:

   a. In the Orchestrator Client main window, click the "Workflows" icon
   b. Expand the following folders: Library->VSPK->Basic->Session
   c. Right click "Add Session" workflow
   d. Select "Start Workflow..." from the context menu
   e. Fill in the following fields:
         - apiUrl: The URL of the VSD to connect to, ex: http://135.121.118.83:8443
         - username, ex: csproot
         - password, ex: csproot
         - enterprise, ex: csp
   f. Click the "Submit" button
   e. Ensure that the workflow executed successfully, otherwise correct errors and click "Submit" again

5. Verify that the newly created session is available in the VSPK plug-in's Inventory:

   a. In the Orchestrator Client main window, click the "Inventory" icon
   b. Expand the VSPK plug-in folder
   c. Check that the VSD URL entered at #4 is displayed
   d. Expand the VSD URL
   e. Expand the "Enterprises" folder. Make sure the enterprises listed below are the same as in the VSD GUI.

6. Create a new Enterprise:

   a. In the VSPK plug-in Inventory, right click on the "Enterprises" folder
   b. From the context menu select the "Add Enterprise" workflow
   c. Enter a name for the new enterprise, ex: testEnterprise
   d. Click submit
   e. Verify that the newly created enterprise shows up in both VSPK plug-in's Inventory as well as the VSD GUI

7. Delete the newly created Enterprise:

   a. In the VSPK plug-in Inventory, right click on the enterprise node
   b. From the context menu select the "Remove Enterprise" workflow
   e. Verify that the enterprise is removed from both VSPK plug-in's Inventory as well as from the VSD GUI

General notes:

   - In all the creation related workflows (i.e. the workflows which names start with "Add ..."), 
     the first input parameter requires a "fetcher". A fetcher is the parent folder to which the new object 
     (that is going to be created as a result of the workflow execution) is going to be attached to. 
     For example, when creating a new enterprise like we did in step #6, the fetcher field was pre-populated 
     with "Enterprises" which is the folder from which we started the "Add Enterprise" workflow.

For support and feature requests, please contact:
nuage-oss-support@alcatel-lucent.com