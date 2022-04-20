import PySimpleGUI as sg
import subprocess
import sys
import os
import webbrowser as wb
import xmltodict
import csv
import shlex
import sqlite3
import sqlalchemy
import pandas as pd
import xml.etree.ElementTree as etree
from sqlalchemy import create_engine

print(sg.version)

help_text = """
    Scanning Options
      Nmap 7.80SVN ( https://nmap.org )
           Usage: nmap [Scan Type(s)] [Options] {target specification}
           TARGET SPECIFICATION:
             Can pass hostnames, IP addresses, networks, etc.
             Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
             -iL <inputfilename>: Input from list of hosts/networks
             -iR <num hosts>: Choose random targets
             --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
             --excludefile <exclude_file>: Exclude list from file
           HOST DISCOVERY:
             -sL: List Scan - simply list targets to scan
             -sn: Ping Scan - disable port scan
             -Pn: Treat all hosts as online -- skip host discovery
             -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
             -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
             -PO[protocol list]: IP Protocol Ping
             -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
             --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
             --system-dns: Use OS's DNS resolver
             --traceroute: Trace hop path to each host
           SCAN TECHNIQUES:
             -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
             -sU: UDP Scan
             -sN/sF/sX: TCP Null, FIN, and Xmas scans
             --scanflags <flags>: Customize TCP scan flags
             -sI <zombie host[:probeport]>: Idle scan
             -sY/sZ: SCTP INIT/COOKIE-ECHO scans
             -sO: IP protocol scan
             -b <FTP relay host>: FTP bounce scan
           PORT SPECIFICATION AND SCAN ORDER:
             -p <port ranges>: Only scan specified ports
               Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
             --exclude-ports <port ranges>: Exclude the specified ports from scanning
             -F: Fast mode - Scan fewer ports than the default scan
             -r: Scan ports consecutively - don't randomize
             --top-ports <number>: Scan <number> most common ports
             --port-ratio <ratio>: Scan ports more common than <ratio>
           SERVICE/VERSION DETECTION:
             -sV: Probe open ports to determine service/version info
             --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
             --version-light: Limit to most likely probes (intensity 2)
             --version-all: Try every single probe (intensity 9)
             --version-trace: Show detailed version scan activity (for debugging)
           SCRIPT SCAN:
             -sC: equivalent to --script=default
             --script=<Lua scripts>: <Lua scripts> is a comma separated list of
                      directories, script-files or script-categories
             --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
             --script-args-file=filename: provide NSE script args in a file
             --script-trace: Show all data sent and received
             --script-updatedb: Update the script database.
             --script-help=<Lua scripts>: Show help about scripts.
                      <Lua scripts> is a comma-separated list of script-files or
                      script-categories.
           OS DETECTION:
             -O: Enable OS detection
             --osscan-limit: Limit OS detection to promising targets
             --osscan-guess: Guess OS more aggressively
           TIMING AND PERFORMANCE:
             Options which take <time> are in seconds, or append 'ms' (milliseconds),
             's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
             -T<0-5>: Set timing template (higher is faster)
             --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
             --min-parallelism/max-parallelism <numprobes>: Probe parallelization
             --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
                 probe round trip time.
             --max-retries <tries>: Caps number of port scan probe retransmissions.
             --host-timeout <time>: Give up on target after this long
             --scan-delay/--max-scan-delay <time>: Adjust delay between probes
             --min-rate <number>: Send packets no slower than <number> per second
             --max-rate <number>: Send packets no faster than <number> per second
           FIREWALL/IDS EVASION AND SPOOFING:
             -f; --mtu <val>: fragment packets (optionally w/given MTU)
             -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
             -S <IP_Address>: Spoof source address
             -e <iface>: Use specified interface
             -g/--source-port <portnum>: Use given port number
             --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
             --data <hex string>: Append a custom payload to sent packets
             --data-string <string>: Append a custom ASCII string to sent packets
             --data-length <num>: Append random data to sent packets
             --ip-options <options>: Send packets with specified ip options
             --ttl <val>: Set IP time-to-live field
             --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
             --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
           OUTPUT:
             -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
                and Grepable format, respectively, to the given filename.
             -oA <basename>: Output in the three major formats at once
             -v: Increase verbosity level (use -vv or more for greater effect)
             -d: Increase debugging level (use -dd or more for greater effect)
             --reason: Display the reason a port is in a particular state
             --open: Only show open (or possibly open) ports
             --packet-trace: Show all packets sent and received
             --iflist: Print host interfaces and routes (for debugging)
             --append-output: Append to rather than clobber specified output files
             --resume <filename>: Resume an aborted scan
             --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
             --webxml: Reference stylesheet from Nmap.Org for more portable XML
             --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
           MISC:
             -6: Enable IPv6 scanning
             -A: Enable OS detection, version detection, script scanning, and traceroute
             --datadir <dirname>: Specify custom Nmap data file location
             --send-eth/--send-ip: Send using raw ethernet frames or IP packets
             --privileged: Assume that the user is fully privileged
             --unprivileged: Assume the user lacks raw socket privileges
             -V: Print version number
             -h: Print this help summary page.
           EXAMPLES:
             nmap -v -A scanme.nmap.org
             nmap -v -sn 192.168.0.0/16 10.0.0.0/8
             nmap -v -iR 10000 -Pn -p 80
"""

version = "April 11, 2022"

# This is a fixed-size text input. It returns a row with a text and an input element.
def FText(
    text, in_key = None, default = None, tooltip = None, input_size = None, text_size = None
):
    if input_size is None:
        input_size = (20, 1)
    if text_size is None:
        text_size = (20, 1)
    return [
        sg.Text(text, size = text_size, justification = "r", tooltip = tooltip),
        sg.Input(default_text = default, key = in_key, size = input_size, tooltip = tooltip),
    ]

# Will be added at a later date.
# # This function is for saving the scan results in a folder called 'scans', and asks for the filename
# # the user wishes to use.
# def ask_for_filename(default_filename = "", initial_folder = "scans", size=None):
#     if initial_folder is None:
#         initial_folder = os.getcwd()


def main():
    # This GUI uses a large input dictionary to display the layout. It collects the parameters inputted to
    # display the projected command-line input. The tuple, input_definition, contains information about each
    # display element. The keys, used to differentiate between each input field, is defined as -(Input field name)-.
    input_definition = {
        '-DATABASE-': ('', 'Database', '', (40, 1), "the database to save scanning results to", []),
        '-TABLE-': ('', 'Database Table', '', (40, 1), "the database table to save scanning results to", []),
        '-FLAGS-': ('', 'Flags', '', (40, 1), "nmap flags to set scanning options", []),
        '-TARGETS-': ('', 'Target(s)', '', (40, 1), "the IP/URL(s) to scan", []),
        '-FILENAME-': ('', 'Filename (optional)', '', (40, 1), "the file to output scan results to", [])
    }

    # This command will be invoked with the parameters.
    command_to_run = r"nmap "

    # Find the longest input description which is at index 1 in the table.
    text_len = max([len(input_definition[key][1]) for key in input_definition])

    # This is the top part of the layout that does not pull from the table.
    layout = [[sg.Text("GUImap - Nmap with a GUI", font = "Any 20")]]

    # This part of the layout is defined from the attributes listed in the table.
    for key in input_definition:
        layout_def = input_definition[key]
        line = FText(
            layout_def[1],
            in_key = key,
            default = layout_def[2],
            tooltip = layout_def[4],
            input_size = layout_def[3],
            text_size = (text_len, 1),
        )
        if layout_def[5] != []:
            line += layout_def[5]
        layout += [line]

    # The bottom part of the layout does not draw from the table, but does display what the command-line input will be.
    # It also displays various buttons that run the Start, Clear All, Help, and Exit commands.
    layout += [
        [sg.Text("Constructed Command Line:")],
        [
            sg.Text(
                size = (80, 3),
                key = "-COMMAND LINE-",
                text_color = "yellow",
                font = "Courier 8",
            )
        ],
        [sg.Text("Command Line Output:")],
        [
            sg.Multiline(
                size = (90, 10),
                reroute_stdout = True,
                reroute_stderr = False,
                reroute_cprint = True,
                write_only = True,
                font = "Courier 8",
                autoscroll = True,
                key = "-ML-",
            )
        ],
        [
            sg.Button("Start"),
            sg.Button("Clear All"),
            sg.Button("Help"),
            sg.Button("Exit"),
            sg.Checkbox("Output to an XML file?", key = "-FILEOUT-", default = False),
            sg.Checkbox("Upload to a database?", key = "-UPLOAD-", default = False),
            sg.Checkbox("Visualize results?", key = "-XSLT-", default = False),
            sg.Checkbox(
                "Give nmap elevated privileges?", key = "-PRIVILEGE-", default = False
            ),
        ],
        [
            sg.Text(
                f'Version : {version}          PySimpleGUI Version {sg.version.split(" ")[0]}',
                font = "Any 8",
                text_color = "yellow",
            )
        ],
    ]

    # This displays the entirety of the text fields, buttons, and command-line output text field.
    window = sg.Window(
        "GUIMap", layout, icon = nmap_icon, element_justification = "c", finalize = True
    )

    # This reads the window for user input. When we read the window, keys will be stored in the values.
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Start":
            sub_timeout = 5
            params = ""
            database = values["-DATABASE-"]
            table_name = values["-TABLE-"]
            flags = values["-FLAGS-"]
            targets = values["-TARGETS-"]
            file_flag = "-oX "
            file_name = values["-FILENAME-"]
            xml_ext = ".xml"
            csv_ext = ".csv"
            priv_command = [
                "gnome-terminal",
                "--",
                "bash",
                "-c",
                'echo "Please enter your system password to give nmap elevated privileges."; sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip $(which nmap); exec bash'
            ]
            file_to_save = file_name + xml_ext
            csv_name = file_name + csv_ext
            for key in values:
                if key not in input_definition:
                    continue
                if values[key] != "":
                    # This piece of code is for the export of scanning results to a file. The user ticks
                    # a checkbox if they wish to output their scanning results to an XML file. This is necessary
                    # if the user intends to use a database. 
                    # Nmap has some scans that require elevated privileges. Rather than giving the nmap program root as a whole, I set Linux file capabilities for it.
                    # When the user chooses to do a privileged scan, a new bash prompt will pop up and ask for the root password.
                    # However, the problem is that the current implementation is non-blocking, as in, when the bash terminal pops up
                    # it does not block program execution. The bash prompt will pop up, but nmap will continue to run in the background.
                    # This can be fixed with an implementation of subprocess.call (which is blocking), but tinkering is required to ensure
                    # that it actually works. Subprocess.run is non-blocking, and is being used as a placeholder until a successful subprocess.call
                    # implementation can be found.
                    # The user has 5 seconds to enter the root password before the subprocess times out.
                    try:
                        if values["-FILEOUT-"] and values["-PRIVILEGE-"]:
                            subprocess.run(priv_command, timeout = sub_timeout)
                            params = (
                                flags
                                + " --privileged "
                                + targets
                                + " "
                                + file_flag
                                + file_to_save
                            )
                            break
                        elif values["-FILEOUT-"]:
                            params = (
                                flags 
                                + " " 
                                + targets 
                                + " " 
                                + file_flag 
                                + file_to_save
                            )
                            break
                        elif values["-PRIVILEGE-"]: 
                            subprocess.run(priv_command, timeout=sub_timeout)
                            params = (
                                flags
                                + " --privileged "
                                + targets
                            )
                            break
                        else:
                            params = flags + " " + targets
                    except subprocess.TimeoutExpired:
                        print('Time for setting nmap capabilities expired')

            # The command to run, with the parameters pulled from the text fields.
            command = command_to_run + params

            # Displays the formed command-line.
            window["-COMMAND LINE-"].update(command)

            # Runs the command.
            runCommand(cmd = command, window = window)

            # If the user ticks both checkboxes, a database and table is created.
            if values["-FILEOUT-"] == True and values["-UPLOAD-"] == True:
                data = xml_parse(file_to_save)
                csv_parse(data, csv_name)
                create_database(file_name, database, table_name)
            
            # If only the upload checkbox is ticked, upload an already existing file. 
            if values["-UPLOAD-"] == True:
                data = xml_parse(file_to_save)
                csv_parse(data, csv_name)
                create_database(file_name, database, table_name)

            # This command runs the xsltproc engine, and opens up a web browser with the xml turned html file.
            if values["-XSLT-"]:
                xsltproc(file_to_save, file_name)


            # When the scanning is done, the program alerts the user.
            sg.cprint(
                "=" * 43 + "DONE" + "=" * 43,
                background_color = "gray",
                text_color = "white",
                justification = "c"
            )

        if event == "Clear All":
            # Will clear all text fields and command output.
            _ = [
                window[elem].update("")
                for elem in values
                if window[elem].Type != sg.ELEM_TYPE_BUTTON
            ]

        # Displays the help text (found in the comment at the top of the program).
        elif event == "Help":
            sg.popup_scrolled(help_text, size = (100, 100))
    window.close()


# This code provides GUIMap with the capability to run nmap from the GUI, along with designated flags and targets.
def runCommand(cmd, timeout = None, window = None):
    # Runs the command in a shell.
    # shlex is used to break up the command, which prevents shell injections.
    # What shlex does is breaks the command up into a list. Take for example the command "echo Hello World".
    # What does it do? It just echos hello world. Now take "echo Hello World; rm -r /*". First it echos hello world,
    # and then recursively deletes all files on your system. With shlex, the commmand is interpreted as "echo, Hello World, ;, rm, -r, /, *".
    # This just throws up an error, which makes this a lot safer.
    # cmd is the command to execute.
    # timeout is to watch for potential hanging of the command.
    # window is the PySimpleGUI window that the output is being displayed on. It refreshes to show updated output.
    # return is used to return the code from the command and command output.
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    output = ""
    for line in p.stdout:
        line = line.decode(
            errors = "replace" if (sys.version_info) < (3, 5) else "backslashreplace"
        ).rstrip()
        output += line
        print(line)
        window.refresh() if window else None
    retval = p.wait(timeout)
    return (retval, output)

# This code is meant to traverse an XML tree (read in from a file), and 
# builds a list of scanning information. The value it returns is a list of lists.
def get_data(root):
    host_data = []
    hosts = root.findall("host")
    for host in hosts:
        address_info = []

        # This ignores hosts that are not 'up'.
        if not host.findall("status")[0].attrib["state"] == "up":
            continue
        
        # This scrapes the IP address and host info from the XML file. If no hostname
        # is found, a blank space is entered instead.
        ip_address = host.findall("address")[0].attrib["addr"]
        host_name_search = host.findall("hostnames")
        try:
            host_name = host_name_search[0].findall("hostname")[0].attrib["name"]
        except IndexError:
            host_name = ""

        # Get the operating system information. If no information is found,
        # a blank space is entered.
        try:
            os_search = host.findall("os")
            os_name = os_search[0].findall("osmatch")[0].attrib["name"]
        except IndexError:
            os_name = ""

        # Get the port results and all services listening on those ports.
        try:
            port_search = host.findall("ports")
            ports = port_search[0].findall("port")
            for port in ports:
                port_data = []
                protocol = port.attrib["protocol"]
                port_id = port.attrib["portid"]
                service = port.findall("service")[0].attrib["name"]
                # These try-except statements iterate through the "XML tree", and assigns
                # relevant data to variables. If no data is found on that "branch" of the tree, it's just an empty space.
                try:
                    product = port.findall("service")[0].attrib["product"]
                except (IndexError, KeyError):
                    product = ""
                try:
                    servicefp = port.findall("service")[0].attrib["servicefp"]
                except (IndexError, KeyError):
                    servicefp = ""
                try:
                    script_id = port.findall("script")[0].attrib["id"]
                except (IndexError, KeyError):
                    script_id = ""
                try:
                    script_output = port.findall("script")[0].attrib["output"]
                except (IndexError, KeyError):
                    script_output = ""

                # Create a list of the port data for further manipulation.
                port_data.extend(
                    (
                        ip_address,
                        host_name,
                        os_name,
                        protocol,
                        port_id,
                        service,
                        product,
                        servicefp,
                        script_id,
                        script_output,
                    )
                )
                # Add the port data to the host data.
                host_data.append(port_data)

        # If no port information is found, just a list of host information is created.        
        except IndexError:
            address_info.extend((ip_address, host_name))
            host_data.append(address_info)
    return host_data

# This code is passed an XML filename, and then reads and parses the XML file.
# It takes the root node of the XML ElementTree, and passes the root node to get_data.
# The get_data function will perform further data manipulation, and returns a list of lists
# containing the scan data.
def xml_parse(file_to_save):
    try:
        tree = etree.parse(file_to_save)
    except Exception as error:
        print(
            "There was an error processing the XML file. Please try again: {}".format(
                error
            )
        )
        exit()
    root = tree.getroot()
    scan_results = get_data(root)
    return scan_results

# This code takes a list of data, and adds the items to an already-existing CSV file,
# or creates a new file.
def csv_parse(data, csv_name):
    if not os.path.isfile(csv_name):
        csv_file = open(csv_name, "w", newline="")
        csv_writer = csv.writer(csv_file)
        top_row = [
            "IP",
            "Host",
            "OS",
            "Protocol",
            "Port",
            "Service",
            "Product",
            "Service FP",
            "NSE Script ID",
            "NSE Script Output",
            "Notes",
        ]
        # This sets up the columns for the database.
        csv_writer.writerow(top_row)
    # If the file already exists, we will write data into the currently existing file.
    else:
        try:
            csv_file = open(csv_name, "a", newline = "")
        # If the current user does not have the proper permissions, the program will throw an error.
        except PermissionError as e:
            print(
                "There was an error with opening the file. Please check to make sure you have the proper permissions."
            )
            for item in data:
                print(" ".join(item))
            exit()
        csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow(item)
    csv_file.close()

# This code provides GUImap with the capability to transform a xml file into a html file.
# Then, it opens a browser window using the webbrowser library to display the html file.
def xsltproc(file_to_save, file_name):
    html_file = file_name + ".html"
    subprocess.run(["xsltproc", file_to_save, "-o", html_file])
    url = 'file://' + os.getcwd() + '/' + html_file
    wb.open(url, new = 0, autoraise = True)

# This code provides GUImap the capability to create a database, and upload scan results to the database. It uses
# SQLAlchemy to create the database, and SQLite3 to create a connection to it. It loads the CSV file (created when the user selects
# the option to upload to a database) into a pandas dataframe. The dataframe converts it into a SQL statement, and passes it to the database.
# The connection to the database is then closed.
def create_database(file_name, database, table_name):
    db_ext = ".db"
    csv_ext = ".csv"
    scan_database = database + db_ext
    csv_file = file_name + csv_ext

    engine = create_engine(f"sqlite:///{scan_database}", echo=True)
    conn = sqlite3.connect(scan_database)

    scan_data = pd.read_csv(csv_file)
    scan_data.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()


if __name__ == "__main__":
    sg.theme("Dark Grey 14")
    nmap_icon = "../media/logo.png"
    main()
