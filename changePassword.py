global AdminUtilities;
## modify JAAS authentication alias ##
def modifyJAASAuthenticationAlias( authAlias, uid, password):
	msgPrefix = "modifyJAASAuthenticationAlias("+`authAlias`+", "+`uid`+", "+`password`+" ): "
        try:
                #--------------------------------------------------------------------
                # modify JAAS authentication alias
                #--------------------------------------------------------------------
                print "---------------------------------------------------------------"
                print " Authentication alias:"
                print "    alias                "+authAlias
                print "    user ID              "+uid
                print "    password             "+password
                print " Usage: createJAASAuthenticationAlias(\""+authAlias+"\", \""+uid+"\", \""+password+"\")"
                print " Return: 0 - success, > 0 failure"
                print "---------------------------------------------------------------"
                print " "
                print " "

                # check  the required arguments
		if (authAlias == ""):
                   raise AttributeError(AdminUtilities._formatNLS(resourceBundle, "WASL6041E", ["authAlias", authAlias]))

		if (uid == ""):
                   raise AttributeError(AdminUtilities._formatNLS(resourceBundle, "WASL6041E", ["uid", uid]))

		if (password == ""):
                   raise AttributeError(AdminUtilities._formatNLS(resourceBundle, "WASL6041E", ["password", password]))

                # Get the config id for the cell's security object
                cell = AdminConfig.list("Cell")
                cellName = AdminConfig.showAttribute(cell, "name")
                sec = AdminConfig.getid("/Cell:"+cellName+"/Security:/")
                # Create a new JAASAuthData
                #attrs = "['-alias','" + authAlias+ "', '-user','" + uid + "', '-password', '" + password + "']"
		# http://www-01.ibm.com/support/knowledgecenter/SSEQTP_8.5.5/com.ibm.websphere.nd.doc/ae/rxml_7securityconfig.html
		AdminTask.modifyAuthDataEntry(["-alias",authAlias,"-user", uid,"-password",password]);
		print "Authentication Alias modified successfully!"
                AdminConfig.save()
		print "Config saved!"

                return 0;
        except:
                typ, val, tb = sys.exc_info()
                if (typ==SystemExit):  raise SystemExit,`val`
                print "Exception: %s %s " % (sys.exc_type, sys.exc_value)
                val = "%s %s" % (sys.exc_type, sys.exc_value)
                raise "ScriptLibraryException: ", `val`
		return 1;
                #endIf
        #endTry
        AdminUtilities.infoNotice(AdminUtilities._OK_+msgPrefix)
#endDef

modifyJAASAuthenticationAlias("WSRRDB_Auth_Alias","WSRRDB","j^K?N{'q]S1&S%Z^bOF]0__+ZFH%kl");
