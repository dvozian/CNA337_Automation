# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Dorin Vozian")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results

    my_server_ip = "18.188.243.5"
    my_server = Server(my_server_ip)
    my_server.ping()
    ping_result = my_server.ping()

    print("**********")

    if ping_result == 0:
        print(ping_result)
        print("Pinging IP [%s] successful." % my_server_ip)
    else:
        print("Pinging IP [%s] Failed." % my_server_ip)

    print("**********")
