# Software Requirements Specification
## For <project name>

Version 0.1  
Prepared by <author>  
<organization>  
<date created>  

## 1. Introduction
> This section should provide an overview of the entire document

### 1.1 Product Scope
Identify the product whose software requirements are specified in this document. Explain what the product will do. Provide a short description of the software being specified and its purpose, including relevant benefits, objectives, and goals.

Transaction data analysis and visualization in different ways in order to understand store revenue by a store manager and possibly increase revenue

### 1.2 Definitions and Abbreviations
List any technical terms, acronyms, or abbreviations that readers might not be familiar with.

data analyzing is that it reads data and finds correlations in said data

### 1.3 References
List any other documents or Web addresses to which this SRS refers. These may include user interface style guides, contracts, standards, or API documentation. Provide enough information so that the reader could access a copy of each reference, including title, author, version number, date, and source or location.

- scikit-learn: https://etc


## 2. Product Overview
> This section should describe the general factors that affect the product and its requirements. This section does not state specific requirements. Instead, it provides a background for those requirements, which are defined in detail in Section 3, and makes them easier to understand.

### 2.1 Product Description
Describe the context and origin of the product being specified in this SRS. For example, state whether this product is a replacement for certain existing systems, or a new, self-contained product. If the SRS defines a component of a larger system, relate the requirements of the larger system to the functionality of this software and identify interfaces between the two. A simple diagram that shows the major components of the overall system, subsystem interconnections, and external interfaces can be helpful.

Its an improvement upon the python file reader and editor, https://github.com/Bastheblackdachshund/Python-Backend-MK.1.

It will be a standalone product.

### 2.2 Product Functions
Summarize the major functions the product must perform or must let the user perform. Details will be provided in Section 3, so only a high level summary (such as a bullet list) is needed here. Organize the functions to make them understandable to any reader of the SRS. 

add your transaction data  the program reads the data puts it into a graph and a databsa sends it all back and then the program displays new data and the anlayses

### 2.3 User Characteristics
Identify the various user classes that you anticipate will use this product. User classes may be differentiated based on frequency of use, subset of product functions used, technical expertise, security or privilege levels, educational level, or experience. Describe the pertinent characteristics of each user class. Certain requirements may pertain only to certain user classes. 

business owners who want to view their transactions find the patterns and increase their profits

### 2.4 Constraints
This subsection should provide a general description of any other items that will limit the developer's options. These may include: 

it should display accurate data, because its supposed to be for business owners

* Interfaces to users, other applications or hardware.  
* Quality of service constraints.  
* Standards compliance.  
* Constraints around design or implementation.

### 2.5 Assumptions and Dependencies
List any assumed factors (as opposed to known facts) that could affect the requirements stated in the SRS. These could include third-party or commercial components that you plan to use, issues around the development or operating environment, or constraints. The project could be affected if these assumptions are incorrect, are not shared, or change. Also identify any dependencies the project has on external factors, such as software components that you intend to reuse from another project.

I use MariaDB and mySQL for the databases the rest is already in the software.

## 3. Requirements
> This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.
>
> The specific requirements should:
> * Be uniquely identifiable. This means they should have a number code. When there is a discussion about a certain requirement, we can refer to this number.
> * State what shall be done.
> * Be verifiable (e.g., it's written so that somebody could check that this requirement is completed)
> * Be clear and unambiguous.

1. it needs a database and in python it needs to be able to upload and read data to said database
2. in python it must be able to read the database data and extract the data and turn it into a graph using scikit-learn
3. it must be able to send the graphs from python to the frontend and be displayed there
4. the user must be able to choose a type of graph they want from line graph, or bar chart.

### 3.1 Functional Requirements
> This section specifies the requirements of functional effects that the software is to have
> 
> List what the system must do. Organize by feature or user class. Use clear, numbered statements.
> 
> Each requirement should specify a single, testable capability. If you find yourself using "and" to connect different functionalities, or if different parts could be implemented and tested independently, split them into separate requirements. This makes requirements easier to track, implement, test, and manage changes to individual features.

1. the system shall verify that all the information is filled in
2. the system shall also use the database to get a bigger graph

#### Example Functional Requirements (ATM machine):

##### FR1: Balance Verification
The system shall verify that the requested withdrawal amount does not exceed the customer's available account balance before processing a withdrawal transaction.

##### FR2: ATM Cash Availability Check
The system shall verify that sufficient cash is available in the ATM to fulfill the requested withdrawal amount before processing a withdrawal transaction.

##### FR3: Account Debit Processing
The system shall debit the customer's account by the exact withdrawal amount only after all verifications have passed successfully.

##### FR4: Cash Dispensing
The system shall dispense the requested cash amount after successfully debiting the customer's account.

##### FR5: Transaction Error Handling
The system shall display a specific error message and cancel the transaction without debiting the account if any verification fails (insufficient balance, exceeds limit, or insufficient ATM cash).

### 3.2 User Interface
Describe the screens/pages, what they are for, and what UI components need to be there. Describe any requirements about the layout or how the interface looks.

there are going to be 2 pages one for uploading the transaction logs and selecting which type of graphs you want and one for seeing the graph as an end result.

### 3.3 Non-Functional Requirements
> This section states additional, quality-related property requirements that the functional effects of the software should present.

#### 3.3.1 Performance
If there are performance requirements for the product under various circumstances, state them here and explain their rationale, to help the developers understand the intent and make suitable design choices. Make such requirements as specific as possible. You may need to state performance requirements for individual functional requirements or features.

it should just not have any major bugs that change the outcome of the graphs.

#### 3.3.2 Security
Specify any requirements regarding security or privacy issues surrounding use of the product or protection of the data used or created by the product. Define any user identity authentication requirements. Refer to any external policies or regulations containing security issues that affect the product.

it uses corsmiddleware to protect any info between the two ports

#### 3.3.3 Reliability
Specify the factors required to establish the required reliability of the software system at time of delivery. This could include requirements for uptime, error handling, or data integrity.

it should function without problems. does not need to be optimised just needs to do what is said it will do.

### 3.4 Technical Constraints
Specify technical implementation constraints such as:
i will use javascript, html, python and SQL
i will use mariaDB
i run it on windows
the basics browsers will all work
the third party librarys are, Express, handlebars, mariaDB, fastAPI.
i use VScode

* Programming languages or frameworks to be used
* Database systems
* Operating systems and platforms
* Browser compatibility requirements
* Third-party components or libraries
* Development tools or environments

## 4. Use Case Specifications
> Use cases describe how users will interact with the system to accomplish specific goals. They help ensure that the system will support the actual workflows users need. Each use case should tell a complete story of how a user achieves a particular objective using the system.
>
> Use cases are particularly valuable because they:
> * Help identify functional requirements you might have missed
> * Provide concrete scenarios for testing
> * Serve as a communication tool between stakeholders and developers
> * Help estimate the complexity and scope of the system
> 
> Below is the template for documenting use cases. Create one specification for each major user interaction with the system.

### Use Case Template

| **Use Case Specification** |                                                                                            |
|---|--------------------------------------------------------------------------------------------|
| **Use Case Name:** | upload forum                                                                               |
| **Actor(s):** | business owner                                                                             |
| **Summary Description:** | it is used to upload the transaction log and answer what type of graph the user wants back |
| **Priority:** | must/should have                                                                           |
| **Status:** | medium detail                                                                              |
| **Pre-Condition:** | nothing its the first step                                                                 |
| **Post-Condition(s):** | the program will run becuase it has the needed information                                 |
| **Basic Path:** | the user inputs the infromation and graph type<br>the program sends that to python         |
| **Alternative Paths:** | an error if not all the information was filled in                                          |

| **Use Case Specification** |                                                                                             |
|---|---------------------------------------------------------------------------------------------|
| **Use Case Name:** | read and write file                                                                         |
| **Actor(s):** | the program itself after the user pressed upload                                            |
| **Summary Description:** | the program reads the transaction log and adds the information to the database              |
| **Priority:** | must have                                                                                   |
| **Status:** | high detail                                                                                 |
| **Pre-Condition:** | the user must have put all the information in and have pressed upload                       |
| **Post-Condition(s):** | the program will have the info to run the analyses                                          |
| **Basic Path:** | it reads th given information by the user<br>then it pust that information into the databse |
| **Alternative Paths:** | it will give an error if it cant find the databse, or read the file                         |

| **Use Case Specification** |                                                                                                                                                                                                                                                               |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Use Case Name:** | sent graph                                                                                                                                                                                                                                                    |
| **Actor(s):** | the program, the user                                                                                                                                                                                                                                         |
| **Summary Description:** | it sent the anylsed transaction log and atabse and puts it into a graph and sents all that to the front end en the second page                                                                                                                                |
| **Priority:** | must have/should have                                                                                                                                                                                                                                         |
| **Status:** | medium level                                                                                                                                                                                                                                                  |
| **Pre-Condition:** | the programs must have run the analyses                                                                                                                                                                                                                       |
| **Post-Condition(s):** | the program is done running                                                                                                                                                                                                                                   |
| **Basic Path:** | it retrives the info from the database and the transaction log<br>it puts the info into a graph chosen by the user<br>gives both to the frontend<br>the frontend displays the graph on the second page<br>it displays all the information on this page aswell |
| **Alternative Paths:** | it throws an error if it misses anything to send back                                                                                                                                                                                                         |

### Example Use Case

| **Use Case Specification** |  |
|---|---|
| **Use Case Name:** | Withdraw Cash |
| **Actor(s):** | Customer (primary), Banking System (secondary) |
| **Summary Description:** | Allows any bank customer to withdraw cash from their bank account. |
| **Priority:** | Must Have |
| **Status:** | Medium Level of details |
| **Pre-Condition:** | • The bank customer has a card to insert into the ATM<br>• The ATM is online properly |
| **Post-Condition(s):** | • The bank customer has received their cash (and optionally a receipt)<br>• The bank has debited the customer's bank account and recorded details of the transaction |
| **Basic Path:** | 1. The customer enters their card into the ATM<br>2. The ATM verifies that the card is a valid bank card<br>3. The ATM requests a PIN code<br>4. The customer enters their PIN code<br>5. The ATM validates the bank card against the PIN code<br>6. The ATM presents service options including "Withdraw"<br>7. The customer chooses "Withdraw"<br>8. The ATM presents options for amounts<br>9. The customer selects an amount or enters an amount<br>10. The ATM verifies that it has enough cash in its hopper<br>11. The ATM verifies that the customer is below withdraw limits<br>12. The ATM verifies sufficient funds in the customer's bank account<br>13. The ATM debits the customer's bank account<br>14. The ATM returns the customer's bank card<br>15. The customer takes their bank card<br>16. The ATM issues the customer's cash<br>17. The customer takes their cash |
| **Alternative Paths:** | 2a. Invalid card<br>2b. Card upside down<br>5a. Stolen card<br>5b. PIN invalid<br>10a. Insufficient cash in the hopper<br>10b. Wrong denomination of cash in the hopper<br>11a. Withdrawal above withdraw limits<br>12a. Insufficient funds in customer's bank account<br>14a. Bank card stuck in machine<br>15a. Customer fails to take their bank card<br>16a. Cash stuck in machine<br>17a. Customer fails to take their cash<br>*a. ATM cannot communicate with Banking System<br>*b. Customer does not respond to ATM prompt |

## 5. Technical Design

### 5.1 System Components and Architecture
> This section provides a high-level technical view of how the system will be structured. It should give developers and technical stakeholders an understanding of the major components and how they interact.
> 
> Include in this section:
* **Architecture Diagram**: A visual representation of the system's major components and their relationships. This could be a simple block diagram showing:
  - Main system components (e.g., frontend, backend, database)
  - External systems or services the system interacts with
  - Data flow between components
  - Key interfaces or APIs

* **Component Descriptions**: For each major component shown in the diagram, provide:
  - Purpose and responsibilities of the component
  - Key technologies or frameworks to be used (if known)
  - Major interfaces it exposes or consumes
  - Data it manages or processes

* **Integration Points**: Document any external systems or services:
  - Third-party (External) APIs or services
  - Legacy systems to integrate with
  - Data import/export requirements


![img_1.png](img_1.png)