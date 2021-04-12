Requirements
============

**Note**: User input functions, how they get their data back out/viewing, visualization and/or statistics, 

1. Functional Requirements

--------------------------

- **Requirement ID**: 01

  - **Requirement Type**: Functions

  - **Description**: This product shall initiate scans from the Nmap engine
        per the user's instructions and record all data into a database.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: The user shall be able to easily (without external
        help) complete scans and view the results in a database.

  - **Priority**: 5

2. Look and Feel Requirements

-----------------------------

- **Requirement ID**: 02

  - **Requirement Type**: Appearance

  - **Description**: This product's appearance shall be minimalistic and
        unobtrusive. It shall provide the user with complete control of the
        product.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: On a Likert scale of 1 to 5 (5 being most aesthetically pleasing), polled users will average a rating of 3 or above.

  - **Priority**: 3

1. Ease of Use Requirements

---------------------------

- **Requirement ID**: 03

  - **Requirement Type**: Useability

  - **Description**: This product shall be used by people with basic
        knowledge of operating a computer program.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: Someone unaware of the capabilities of the product
        shall be able to pick it up and use it to its full capabilities.

  - **Priority**: 4

4. Performance Requirements

---------------------------

- **Requirement ID**: 04a

  - **Requirement Type**: Speed and Latency

  - **Description**: This product will complete scans and upload data in a
        reasonable timeframe. Depending on the size of the network being scanned
        and the results being uploaded, a reasonable timeframe can be
        established to be \~\< 30 minutes.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: The product shall complete scans and upload results
        in less than an hour.

  - **Priority**: 3

- **Requirement ID**: 04b

  - **Requirement Type**: Precision or Accuracy

  - **Description**: The scans from this product will depict network
        conditions with relative accuracy and the database will accurately
        record information.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: On a network with 10 devices, scans will show all 10 devices and the database will show all information for each device.  

  - **Priority**: 3

- **Requirement ID**: 04c

  - **Requirement Type**: Reliability and Availability

  - **Description**: This product shall be freely available to the user and
        will run until the user chooses to terminate the product.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: The product will run for 3 hours and will only terminate once the user presses the quit button.

  - **Priority**: 2

- **Requirement ID**: 04d

  - **Requirement Type**: Scalability and Capacity

  - **Description**: This product shall rely on dynamic scalability and
        capacity, defined by the user's parameters.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: Starting at 1 scan result, the product will scale up to 1000+ results and the database will show all results.

  - **Priority**: 4

1. Maintainability and Support Requirements

-------------------------------------------

- **Requirement ID**: 05

  - **Requirement Type**: Maintenance Requirements

  - **Description**: Bug fixes and performance improvements must be able to
        be applied to the project as soon as they are available.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: Bugs will be fixed and patches will be pushed out ASAP, and will be applied to the product.

  - **Priority**: 1

6. Security Requirements

------------------------

- **Requirement ID**: 06a

- **Requirement Type**: Access Requirements

  - **Description**: This product shall provide users with the capability of
        locking their databases with passwords.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: All users are able to password-protect their
        information.

  - **Priority**: 5

- **Requirement ID**: 06b

  - **Requirement Type**: Integrity Requirements

  - **Description**: The product shall prevent incorrect or harmful data
        from being introduced into the database.

  - **Originator**: Hayden Ackerman

  - **Fit Criterion**: Incorrect scan results and garbage data will be entered into the database, and will be rejected or corrected.

  - **Priority**: 5
