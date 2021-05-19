


def main():

	# open file in write mode
	fo = open("config.txt","wt")
	# Input the user data
	print("\n |Welcome to the VPN Config Program!\n"
	+ "\n|Note if you want to create your own VPN you will need a running cloud instacnce|\n")
	print("Press 1 for yes and 0 for no\n")
	print ("Would you like to enable IPsec support? This will allow for more secure connections between devices as it uses encryption\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("ipsec_enabled:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to enable dns adblocking? This will help block ads while using VPN\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("adblock_list:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to enable dns encrpytion? You cannot disable this if you enabled dns adblocking\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("dns_encryption:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to block traffic between connected clients? If you don't other clients on the same server will be able to reach each other\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("BetweenClients_DROP:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to enable unattended reboot? This will allow for your algo server to automatically install sercurity updates.\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("unattended_reboot:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to store the pki (primary key infrastructure) in a ram disk? This will allow for easier access to login. *Only supports MACOS and Linux.\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("pki_in_tmpfs:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to clean all of your primary keys? This will make it so ALL users will need to get new certificates, not just new users.\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("keys_clean_all:")
	fo.write(data)
	fo.write("\n")
	print ("Would you like to hide sensitive data?\n")
	data = input("Option: ")
	# write data to the file
	if int(data) == 1:
		data = "True";
	else:
		data = "False";
	fo.write("no_log:")
	fo.write(data)
	fo.write("\n")
	# close the file
	fo.close()

	# open file again in read mode
	fo = open("config.txt","rt")
	# read the data from the file
	str=fo.read()
	# print the read data
	print("\nYour new config file is:\n")
	print(str)
	print("Change to these settings in the algo folder:\n")
	# close the file
	fo.close()
if __name__=="__main__":main()
