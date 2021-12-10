import PySimpleGUI as sg
import subprocess
import sys
import os
print(sg.version)

help_text = \
    """
    Scanning Options
      Nmap 7.70SVN ( https://nmap.org )
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

version = 'December 8, 2021'

# This is a fixed-size text input. It returns a row with a text and an input element.
def FText(text, in_key=None, default=None, tooltip=None, input_size=None, text_size=None):
    if input_size is None:
        input_size = (20, 1)
    if text_size is None:
        text_size = (20, 1)
    return [sg.Text(text, size=text_size, justification='r', tooltip=tooltip),
            sg.Input(default_text=default, key=in_key, size=input_size, tooltip=tooltip)]

# This function is for saving the scan results in a folder called 'scans', and asks for the filename
# the user wishes to use.
def ask_for_filename(default_filename='', initial_folder='scans', size=None):
    if initial_folder is None:
        initial_folder = os.getcwd()


def main():
    # This GUI uses a large input dictionary to display the layout. It collects the parameters inputted to
    # display the projected command-line input. The tuple, input_definition, contains information about each
    # display element. The keys, used to differentiate between each input field, is defined as -(Input field name)-.
    input_definition = {
        '-USERNAME-': ('', 'Username', '', (40, 1), "the username for the database", []),
        '-PASSWORD-': ('', 'Password', '', (40, 1), "the password for the user and the database", []),
        '-DATABASE-': ('', 'Database', '', (40, 1), "the database to save scanning results to", []),
        '-FLAGS-': ('', 'Flags', '', (40, 1), "nmap flags to set scanning options", []),
        '-TARGETS-': ('', 'Target(s)', '', (40, 1), "the IP/URL(s) to scan", []),
        '-FILENAME-': ('', 'Filename (optional)', '', (40, 1), "the file to output scan results to", [])
    }

    # This command will be invoked with the parameters.
    command_to_run = r'nmap '

    # Find the longest input description which is at index 1 in the table.
    text_len = max([len(input_definition[key][1]) for key in input_definition])

    # This is the top part of the layout that does not pull from the table.
    layout = [[sg.Text('GUImap - Nmap with a GUI', font='Any 20')]]

    # This part of the layout is defined from the attributes listed in the table.
    for key in input_definition:
        layout_def = input_definition[key]
        line = FText(layout_def[1], in_key=key, default=layout_def[2],
                     tooltip=layout_def[4], input_size=layout_def[3], text_size=(text_len, 1))
        if layout_def[5] != []:
            line += layout_def[5]
        layout += [line]

    # The bottom part of the layout does not draw from the table, but does display what the command-line input will be.
    # It also displays various buttons that run the Start, Clear All, Help, and Exit commands.
    layout += [[sg.Text('Constructed Command Line:')],
               [sg.Text(size=(80, 3), key='-COMMAND LINE-',
                        text_color='yellow', font='Courier 8')],
               [sg.Text('Command Line Output:')],
               [sg.Multiline(size=(80, 10), reroute_stdout=True, reroute_stderr=False,
                             reroute_cprint=True,  write_only=True, font='Courier 8', autoscroll=True, key='-ML-')],
               [sg.Button('Start'), sg.Button('Clear All'), sg.Button('Help'), sg.Button(
                   'Exit'), sg.Checkbox('Output to an XML file?', key='-FILEOUT-', default=False)],
               [sg.Text(f'Version : {version}          PySimpleGUI Version {sg.version.split(" ")[0]}', font='Any 8', text_color='yellow')]]

    # This displays the entirety of the text fields, buttons, and command-line output text field.
    window = sg.Window('GUIMap', layout, icon=nmap_icon,
                       element_justification='c', finalize=True)

    # This reads the window for user input. When we read the window, keys will be stored in the values.
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Start':
            params = ''
            user = values['-USERNAME-']
            password = values['-PASSWORD-']
            database = values['-DATABASE-']
            flags = values['-FLAGS-']
            targets = values['-TARGETS-']
            fname = values['-FILENAME-']
            file_flag = '-oX'
            for key in values:
                if key not in input_definition:
                    continue
                if values[key] != '':
                    # This piece of code is for the export of scanning results to a file. It has yet to be implemented,
                    # due to a complete rework of the GUI.
                    if values["-FILEOUT-"] == True:
                        params = flags + ' ' + targets + ' ' + file_flag + ' ' + fname
                    else:
                        params = flags + ' ' + targets

            # The command to run, with the parameters pulled from the text fields.
            command = command_to_run + params

            # Displays the formed command-line.
            window['-COMMAND LINE-'].update(command)

            # Runs the command.
            runCommand(cmd=command, window=window)

            # When the scanning is done, the program alerts the user.
            sg.cprint('*'*20+'DONE'+'*'*20,
                      background_color='gray', text_color='white')
            sg.popup('*'*20+'DONE'+'*'*20, title='Completed scanning!',
                     background_color='gray', text_color='white', keep_on_top=True)

        if event == 'Clear All':
            # Will clear all text fields and command output.
            _ = [window[elem].update(
                '') for elem in values if window[elem].Type != sg.ELEM_TYPE_BUTTON]

        # Displays the help text (found in the comment at the top of the program).
        elif event == 'Help':
            sg.popup(help_text, line_width=len(
                max(help_text.split('\n'), key=len)))
    window.close()

# This code provides GUIMap with the capability to run nmap from the GUI, along with designated flags and targets.


def runCommand(cmd, timeout=None, window=None):
    # Runs the command in a shell.
    # cmd is the command to execute.
    # timeout is to watch for potential hanging of the command.
    # window is the PySimpleGUI window that the output is being displayed on. It refreshes to show updated output.
    # return is used to return the code from the command and command output.
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (
            3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.refresh() if window else None
    retval = p.wait(timeout)
    return (retval, output)


if __name__ == '__main__':
    sg.theme('Dark Grey 14')
    nmap_icon = '../media/logo.png'
    main()
