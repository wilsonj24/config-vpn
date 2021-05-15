# VPN config file

# imports





def main():
    """The main driver function for the project."""

    print(
        "\n\n-------------------------------------------\n"
        + "| Welcome to the VPN config Program!                           |"
        + "\n|* Note if you want to create your own VPN you will need cloud instacnce|"
        + "\n-------------------------------------------\n\n"
    )  # print program welcome message

main()

print("You can use the user created VPN on phone, laptop, and desktop\n")


answer = input("Would you like to enable IPsec support? This will allow for more secure connections between devices as it uses encryption\n")
if answer == "yes":
   print("Great\n")
elif answer == "no":
   print("Okay\n")

answer = input("Would you like to enable dns adblocking? This will help block ads while using VPN\n")
if answer == "yes":
   print("Great!\n")
elif answer == "no":
   print("Okay!\n")

answer = input("Would you like to enable dns encrpytion? You cannot disable this if you enabled dns adblocking\n")
if answer == "yes":
   print("Great!\n")
elif answer == "no":
   print("Okay!\n")

answer = input("Would you like to block traffic between connected clients? If you don't other clients on the same server will be able to reach each other\n")
if answer == "yes":
   print("Great!\n")
elif answer == "no":
   print("Okay!\n")

answer = input("Would you like to enable unattended reboot? This will allow for your algo server to automatically install sercurity updates.\n")
if answer == "yes":
   print("Great!\n")
elif answer == "no":
   print("Okay!\n")

answer = input("Do you have a running cloud instance with: \n"
+ "azure\n"
+"digitalocean\n"
+"gce\n"
+"lightsail"
+"scaleway\n"
+"hetzner\n"
+"openstack\n"
+"cloudstack\n"
+"vultr\n"
+"linode?\n")
if answer == "yes":
   print("Congratulations! you now have the information to create your own algo server\n")
elif answer == "no":
   print("Sorry, but something went wrong!"
 +"Please check the troubleshooting guide."
 +"https://trailofbits.github.io/algo/troubleshooting.html\n")
