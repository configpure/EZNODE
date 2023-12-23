
nodeip = str(input("Enter Your Node IP: "))
node_root_password = str(input("Enter Your Node Root Password: "))

config_return = """
SERVER_IP = '{0}'
SERVER_PORT = '22' # Default Port
SERVER_USER = 'root' # Default User
SERVER_PASSWORD = '{1}'
""".format(nodeip,node_root_password)

f = open("config.py", "a")
f.write(config_return)
f.close()