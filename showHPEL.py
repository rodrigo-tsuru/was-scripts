servers = "catalogServer1,catalogServer2,catalogServer3,containerServer1,containerServer2,containerServer3,containerServer4"
 
serverArray = servers.split(",")
for x in range(len(serverArray)):
	print "Configurações de log do servidor: " + serverArray[x];
	HPELService = AdminConfig.getid("/Cell:DES-SSWAS-01Cell01/Node:DES-SSWAS-01Node01/Server:"+serverArray[x]+"/HighPerformanceExtensibleLogging:/");
	HPELLog = AdminConfig.list("HPELLog", HPELService)
	print AdminConfig.showall(HPELLog);


