servers = "catalogServer1,catalogServer2,catalogServer3,containerServer1,containerServer2,containerServer3,containerServer4"
 
serverArray = servers.split(",")
for x in range(len(serverArray)):
	print serverArray[x];
	HPELService = AdminConfig.getid("/Cell:DES-SSWAS-01Cell01/Node:DES-SSWAS-01Node01/Server:"+serverArray[x]+"/HighPerformanceExtensibleLogging:/");
	print AdminConfig.showall(HPELService);

