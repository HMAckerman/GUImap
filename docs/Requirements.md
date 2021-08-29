Requirements
============

1. Functional Requirements
--------------------------

-   **Requirement ID**: 01a

    -   **Requirement Type**: Functions

    -   **Description**: This product shall initiate scans from the Nmap engine
        per the user's instructions and record all data into a database.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall be able to easily (without external
        help) complete scans and view the results in a database.

    -   **Priority**: 5

-   **Requirement ID**: 01b

    -   **Requirement Type**: User Input

    -   **Description**: This product shall accept input from the user that will
        be parsed by the internal processes of the product.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall be able to input their data into the
        product and the product follows the user's instructions.

    -   **Priority**: 5

-   **Requirement ID**: 01c
  
    -   **Requirement Type**: Scan Options: Profiles

    -   **Description**: This product shall have a pre-defined list of
        scan intensities (how forceful the scan is).

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall be able to choose the "Intense scan" option
        and the scan will complete faster than the "Quick scan" option.

    -   **Priority**: 5    

-   **Requirement ID**: 01d

    -   **Requirement Type**: Scan Options: TCP

    -   **Description**: This product shall accept input from the user that designates
        the type of TCP scan to be used.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall put in one of the flags for the TCP scans and the scan
        will be completed with the user's parameters. 

    -   **Priority**: 5

-   **Requirement ID**: 01e

    -   **Requirement Type**: Scan Options: Special Scans

    -   **Description**: This product shall accept input from the user that will initiate
        one of the unique scans that Nmap is able to perform.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall put in a unique flag (as in, a specialized flag)
        and the scan will be completed with the user's parameters. 

    -   **Priority**: 5

-   **Requirement ID**: 01f
  
    -   **Requirement Type**: Scan Options: Timing

    -   **Description**: This product shall give the user an option to delay scanning probes
        via pre-defined intervals of time. 

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall select the "10-minute" option, and it will be
        10 minutes before the next probe is sent out. 

    -   **Priority**: 5

-   **Requirement ID**: 01g
  
    -   **Requirement Type**: Scan Options: Checkboxes

    -   **Description**: This product shall have several checkboxes with unique pre-defined 
        functions: a FTP bounce attack, an Idle Scan, Services version detection, Operating
        system detection, and Disable reverse DNS resolution. 
    
    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall check the checkboxes, and the current 
        Nmap command will reflect the user's choice.

    -   **Priority**: 5

-   **Requirement ID**: 01h
    
    -   **Requirement Type**: Scan Options: Target

    -   **Description**: This product shall have a text field that accepts either an IP address
        or a URL address from the user.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall put "www.google.com" into the text field, and the product
        shall scan "www.google.com".

    -   **Priority**: 5

-   **Requirement ID**: 01i

    -   **Requirement Type**: Exporting Data

    -   **Description**: This product shall allow the user to retrieve all of
        their data that the product has stored and created.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall run a scan and download the results
        from the product.

    -   **Priority**: 4

-   **Requirement ID**: 01j

    -   **Requirement Type**: Data Visualization

    -   **Description**: This product shall display the user's data in a format
        chosen by the user.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The user shall run a scan and view their data in a
        format they choose.

    -   **Priority**: 3

2. Look and Feel Requirements
-----------------------------

-   **Requirement ID**: 02

    -   **Requirement Type**: Appearance

    -   **Description**: This product's appearance shall be minimalistic and
        unobtrusive. It shall provide the user with complete control of the
        product.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: On a Likert scale of 1 to 5 (5 being most
        aesthetically pleasing), polled users will average a rating of 3 or
        above.

    -   **Priority**: 3

3. Ease of Use Requirements
---------------------------

-   **Requirement ID**: 03

    -   **Requirement Type**: Useability

    -   **Description**: This product shall be used by people with basic
        knowledge of operating a computer program.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: Someone unaware of the capabilities of the product
        shall be able to pick it up and use it to its full capabilities.

    -   **Priority**: 4

4. Performance Requirements
---------------------------

-   **Requirement ID**: 04a

    -   **Requirement Type**: Speed and Latency

    -   **Description**: This product will complete scans and upload data in a
        reasonable timeframe. Depending on the size of the network being scanned
        and the results being uploaded, a reasonable timeframe can be
        established to be \~\< 30 minutes.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The product shall complete scans and upload results
        in less than an hour.

    -   **Priority**: 3

-   **Requirement ID**: 04b

    -   **Requirement Type**: Precision or Accuracy

    -   **Description**: The scans from this product will depict network
        conditions with relative accuracy and the database will accurately
        record information.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: On a network with 10 devices, scans will show all 10
        devices and the database will show all information for each device.

    -   **Priority**: 3

-   **Requirement ID**: 04c

    -   **Requirement Type**: Reliability and Availability

    -   **Description**: This product shall be freely available to the user and
        will run until the user chooses to terminate the product.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: The product will run for 3 hours and will only
        terminate once the user presses the quit button.

    -   **Priority**: 2

-   **Requirement ID**: 04d

    -   **Requirement Type**: Scalability and Capacity

    -   **Description**: This product shall rely on dynamic scalability and
        capacity, defined by the user's parameters.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: Starting at 1 scan result, the product will scale up
        to 1000+ results and the database will show all results.

    -   **Priority**: 4

5. Maintainability and Support Requirements
-------------------------------------------

-   **Requirement ID**: 05

    -   **Requirement Type**: Maintenance Requirements

    -   **Description**: Bug fixes and performance improvements must be able to
        be applied to the project as soon as they are available.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: Bugs will be fixed and patches will be pushed out
        ASAP, and will be applied to the product.

    -   **Priority**: 1

6. Security Requirements
------------------------

-   **Requirement ID**: 06a

    -   **Requirement Type**: Access Requirements

    -   **Description**: This product shall provide users with the capability of
        locking their databases with passwords.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: All users are able to password-protect their
        information.

    -   **Priority**: 5

-   **Requirement ID**: 06b

    -   **Requirement Type**: Integrity Requirements

    -   **Description**: The product shall prevent incorrect or harmful data
        from being introduced into the database.

    -   **Originator**: Hayden Ackerman

    -   **Fit Criterion**: Incorrect scan results and garbage data will be
        entered into the database, and will be rejected or corrected.

    -   **Priority**: 5
