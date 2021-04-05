Senior Project Proposal
=======================

- **Student Name**: Hayden Ackerman

- **Advisor Name**: Dr. Sean Hayes

- **Expected Graduation Date**: Spring 2022

Problem Statement
-----------------

The [Nmap scanning engine](https://en.wikipedia.org/wiki/Nmap) is a valuable
tool for anyone who wants to find out more about their own network, perform
reconnaissance against a target, or learn more about networking in general.
Ideally, Nmap supports the ability to upload to various database schemas. Users
would be able to retrieve current and past information about scans, using an
intuitive graphical user interface (GUI). However, Nmap itself possesses no such
functionality. The developer of Nmap even states on [his
website](https://nmap.org/), "Nmap offers no direct database output
functionality. Not only are there too many different database types for me to
support them all, but users' needs vary so dramatically that no single database
schema is suitable." Yet, there is a cross-platform GUI for Nmap called "Zenmap"
that possesses the capability to upload results to a local database. However,
the database is...functional at best, and the GUI is completely unintuitive. How
is an individual user or even an international enterprise supposed to easily
store their scan results? I propose a tool that utilizes an intuitive GUI and an
easily extensible database library/framework to complement the Nmap scanning
engine. This tool would be a valuable addition to anyone's toolkit.

Description of Project
----------------------

My project will be a graphical user interface (GUI)-focused implementation of
the Nmap "Network Mapper" scanning tool. It will receive input (e.g., flags,
IPs/URLs, and so forth) from the GUI and pass it to the Nmap engine. Output can
either be displayed immediately or directly submitted to a database of the
user's choosing for future examination. If a database does not exist yet, the
tool also supports the capability of creating a database for the user. If a
database already exists, the tool can pull down previous scanning results and
convert them into a comma separated values (CSV) file. Additionally, the user will be able to interact with the database itself. The user will be able to sort the data
in the database, delete data in the database, edit data,
and potentially merge data in the database. Furthermore, all
data that the database
possesses will be visualized using Grafana, an open-source analytics platform.

Proposed Implementation Language(s)
-----------------------------------

My project will use Python 3 for most of the heavy lifting. Python 3 is a
powerful, yet easily modifiable and implementable language. It has numerous
libraries and can easily interact with other programming languages. The backend,
i.e., the database, will be communicated with via SQL queries using SQLite as a
medium. SQL is a standard language for storing, manipulating, and retrieving
data in databases. SQLite is a C-language library that is a small, fast,
self-contained, high-reliability, full-featured, SQL database engine, according
to their [website](https://www.sqlite.org/index.html).

Libraries, Packages, Development Kits
-------------------------------------

1. **tkinter** ("Tk interface")

    - a Python framework meant to build GUIs with pure code.

2. **SQLite**

    - a C-language library that is a small, fast, self-contained,
        high-reliability, full-featured, SQL database engine.

3. **SQLalchemy**

    - a Python SQL toolkit and Object Relational Mapper, allowing for
        efficient and high-performance database access.

4. **Grafana SQLite Datasource**

   - a Grafana backend plugin to allow using a SQLite database as a data source.

Software/Equipment Needed
-------------------------

1. **Nmap**

    - The tool my project is interacting with.

2. **Text Editor**

    - Needs to have the capability to display a CSV file, also required to
        display scanning reports.

3. **Oracle's VirtualBox**

    - Needed for development inside Linux.

4. **Ubuntu Linux** *(potentially Windows 10 with Windows Subsystem for Linux
    (WSL) 2)*

    - Needed for development and testing purposes.

5. **Python 3**

    - Needed to develop and run the application.

6. **Visual Studio Code**

   - IDE needed to code the project.

7. **Grafana**

   - Needed to observe and visualize data from the database.

Motivation
----------

I decided to take on this project for several reasons:

1. I wanted to delve deep into the Python programming language. My first
    experience with Python was with making basic scripts for games when I was
    younger. My first collegiate experience with Python was in Survey of
    Scripting. In that class, I appreciated the raw power yet simplicity of the
    language as a whole. By taking on this project, I would like to be able to
    call myself a Python "guru".

2. I am a Cybersecurity major. In whatever profession I choose, I will most
    likely use Nmap at some point or another. It has been an invaluable boon to
    the Information Security (InfoSec) field. I would like to find out the sheer
    capabilities of the tool and doing so would only increase my appreciation
    for the InfoSec field. Additionally, I would like to be able to use my own
    tool in my profession.

3. The Nmap tool needs to be able to upload information to various database
    schemas/schemaless databases. Nmap would benefit from the capabilities and
    general uniformity that a powerful database engine, such as SQLite,
    possesses.

Outline of Future Research Efforts
----------------------------------

I will complete my project by completing the GUI first, then ensuring that input
from the GUI can be passed to the Nmap engine. The GUI will also handle creation
and/or modification of a database. I will ensure that the GUI will be clean and
intuitive with minimal instructions. I intend for the user to have a good
experience. I don't intend to clutter their whole screen with "tips & tricks".
The next step will be to create an easily modifiable database schema. I want my tool to
be capable of pulling down from/uploading to a database quickly. I will research into ways to
optimize performance. The main issue is that no database will be "one size fits all".
Due to the advanced nature of the Nmap engine, there can potentially be *numerous* columns and rows depending on the
flags used. However, from some brief research into the SQLite database engine,
it seems like it is easily modifiable to support larger sets of information.
Finally, I will implement file input and output, and conversion into CSV files.
I anticipate that the main problem will be getting different file formats to
cooperate nicely. However, Python 3 has numerous libraries dedicated to various
file formats, so this problem might easily be mitigated.

Schedule
--------

| Task                                                 | Start Date         | Completion Date (Estimated) |
|------------------------------------------------------|--------------------|-----------------------------|
| Create Project                                       | August 28, 2020    | August 28, 2020             |
| Install Necessary Software/Libraries                 | August 28, 2020    | August 28, 2020             |
| Graphical User Interface (GUI)                       | August 28, 2020    | March 5, 2021               |
| Final Draft of Requirements                          | March 19, 2021     | April 6, 2021               |
| User Input                                           | April 20, 2021     | April 30, 2021              |
| Create Database Schema/Implement Schemaless Database | September 24, 2021 | October 13, 2021            |
| File Input/Output & File Conversion                  | October 29, 2021   | November 10, 2021           |
| Create a Test Plan                                   | November 17, 2021  | December 5, 2021            |
| Testing Project for Bugs/Issues/Etc.                 | February 20, 2022  | March 2, 2022               |
| Compile Results & Analyze/Fix Bugs                   | March 2, 2022      | March 15, 2022              |
| Complete Project & Defend Project                    | April 15, 2022     | April 15, 2022              |
