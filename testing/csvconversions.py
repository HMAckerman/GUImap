import xml.etree.ElementTree as etree
import os
import csv

def get_data(root):
    host_data = []
    hosts = root.findall('host')
    for host in hosts:
        address_info = []

        if not host.findall('status')[0].attrib['state'] == 'up':
            continue

        ip_address = host.findall('address')[0].attrib['addr']
        host_name_search = host.findall('hostnames')
        try:
            host_name = host_name_search[0].findall('hostname')[0].attrib['name']
        except IndexError:
            host_name = ''

        try:
            os_search = host.findall('os')
            os_name = os_search[0].findall('osmatch')[0].attrib['name']
        except IndexError:
            os_name = ''

        try:
            port_search = host.findall('ports')
            ports = port_search[0].findall('port')
            for port in ports:
                port_data = []
                protocol = port.attrib['protocol']
                port_id = port.attrib['portid']
                service = port.findall('service')[0].attrib['name']
                try:
                    product = port.findall('service')[0].attrib['product']
                except(IndexError, KeyError):
                    product = ''
                try:
                    servicefp = port.findall('service')[0].attrib['servicefp']
                except(IndexError, KeyError):
                    servicefp = ''
                try:
                    script_id = port.findall('script')[0].attrib['id']
                except(IndexError, KeyError):
                    script_id = ''
                try:
                    script_results = port.findall('script')[0].attrib['results']
                except(IndexError, KeyError):
                    script_results = ''

                port_data.extend((ip_address, host_name, os_name, protocol,
                                  port_id, service, product, servicefp,
                                  script_id, script_results))
                
                host_data.append(port_data)
        except IndexError:
            address_info.extend((ip_address, host_name))
            host_data.append(address_info)
    return host_data

def xml_parse(xml_file):
    try:
        tree = etree.parse(xml_file)
    except Exception as error:
        print("There was an error processing the XML file. Please try again: {}".format(error))
        exit()
    root = tree.getroot()
    scan_results = get_data(root)
    return scan_results

def csv_parse(data):
    if not os.path.isfile(csv_name):
        csv_file = open(csv_name, 'w', newline = '')
        csv_writer = csv.writer(csv_file)
        top_row = [
            'IP', 'Host', 'OS', 'Protocol', 'Port', 'Service',
            'Product', 'Service Fingerprint', 'NSE Script ID',
            'NSE Script Results', 'Notes'
        ]
        csv_writer.writerow(top_row)
    else:
        try:
            csv_file = open(csv_name, 'a', newline = '')
        except PermissionError as e:
            print("There was an error with opening the file. Please check to make sure you have the proper permissions.")
            for item in data:
                print(' '.join(item))
            exit()
        csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow(item)
    csv_file.close()