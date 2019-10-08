## Project Outline

The project focuses on developing a framework which allows dynamic composition of workflows, facilitating massive Data Analytics (DA) tasks. 

Navigate to **“How to run the framework”**

## Problem Definition

Although humans have gathered data since the beginning of time, the acquisition rate of data has surged significantly during the recent years, with no end in sight.  Institutions in every industry are racing to gather each and every piece of data available. 

The benefits of Data Analytics are evident from applications in numerous fields such as, financial data analysis, retail, telecommunication, science and engineering. The domain is widespread and commercial, governmental and educational sectors stand to gain much from proper implementation of data mining, in the form of increased efficiency, reduced cost and insight to previously unknown relationships. 

#### High Performance Data Analytics  (HPDA)

High Performance Data Analytics unites High Performance Computing (HPC) with Data Analytics. The primary forces driving the use of HPDA are, the organic growth of data-intensive simulation and the need to process data analytics workloads that are too complex and time critical for enterprise IT technology to handle using traditional systems. The HPDA process leverages HPC’s use of parallel processing to run analytics tasks at previously unprecedented speeds, providing entities with the ability to quickly examine large data sets and draw meaningful conclusions. 

#### Talent management 

With the increase in data availability, the complements of Data Analytics has become more valuable. The most crucial of these are, data scientists and other professionals skilled at working with large amounts of information.  

Many key techniques for using, cleaning and organizing large amounts of structured and unstructured data are rarely taught in traditional statistics courses. A major barrier in harvesting knowledge from Data Analytics exists in this talent gap. Human capital with  high levels of technical skill is essential in order to leverage knowledge through Data Analytics techniques. Not surprisingly, individuals possessing such a skill set are difficult to find and are in great demand. Notably, it is difficult to come across data scientists with domain-specific knowledge, relating to the Data Analytics application. 

As previously discussed, the Data Analytics domain stands to gain a great deal from the convergence with High Performance Computing. However, in addition to domain experts, even data scientists sometimes lack the specialized skills needed to make use of complex computational platforms such as HPC clusters to implement these tasks. Therefore, it could be correctly inferred that the requirement for a convenient paradigm for performing High Performance Data Analytics tasks exist. Such a programming model could decrease the talent gap in the industry, by encouraging more individuals to enter the field, reducing the effort put in to performing analytics tasks and enabling technological advancement.  

#### Large Amounts of Data

Another evident issue in the data analytics field is the large amount of structured and unstructured data generated through various systems, processes and actions within and outside of companies on a daily basis. This abundance of data, coupled with a growing need for powerful data analysis tools creates a *“data rich but information poor”* situation. The escalating need to perform advanced analytics tasks on massive data sets in near-real time is a modern day requirement that is causing a new wave of commercial firms to adopt HPC for analytics tasks.

## Project Description

From the many existing methodologies for performing Data Analytics, the team selected **workflows** as the focal concept of the project.    

In modern Data Analytics applications, the concept of static workflows are no longer tenable due to the fact that it is beneficial to be able to perform reconfiguration **dynamically**. 

The project takes the concept of static workflows, one step further and develops the capability of dynamically composing workflows for data analytics. This would build another level of abstraction on top of static workflow composition and enable domain experts to define a thread of control dynamically, through means of a script or using a graphical user interface; providing much needed convenience and ease of use.  

The project utilizes the notion of control driven coordination to dynamically compose interacting software modules during execution through means of orchestration. Workflow orchestration is performed using Golang, by utilizing one of the most exciting aspects of the language; its concurrency model. 

Furthermore, the team proposes extracting the computational power of an HPC cluster with the help of Swift, the parallel scripting language to carry out this task effectively and efficiently.

## Project Goal and Objectives 

### Goal

Enhancing programming expressiveness and convenience for Data Scientists and Domain Experts in performing Massive Data Analytics tasks.

### Objectives

+ Provide an efficient layer of **abstraction** for convenient  manipulation of  workflows to perform massive Data Analytics

+ Implement **dynamic orchestration of workflows** to perform data analytics tasks

+ Enable users to fully **exploit the power of cloud infrastructure** to greatly improve the efficiency of performing analytics tasks

+ Enable domain experts to efficiently carry out data analytics tasks by providing a **convenient programming paradigm** for HPC

## High level Architecture


Figure : The High level Architecture of the system

The end user would access the dynamic workflow system for data analytics using either the web application or through means of a script. 

Thereafter, through the AWS management console, the data set would be migrated to an S3 bucket. The framework would be implemented in an AWS EC2 instance, connected with the mentioned S3 bucket, in order to transfer the data set to the DA modules of the workflow. 

We can run different Swift-Python modules, parallely, in other EC2 instances. 


Figure : The Proposed Data Analytics Process

This is the proposed data analytics process in our framework. 

Dynamic composition of workflows would initially be applied to the data mining phase of the data analytics process. The connectivity between modules is generated at runtime of each phase. 

Once the output of the data transformation stage is generated, the Go control thread of the data mining stage would capture this information and see what are the user selected data mining algorithms (Swift-Python script(s)).

From the user-determined candidate algorithms, the control thread would choose the most suitable Swift-Python script according to the nature of the problem under consideration and generate the final output. Thereafter, that output would be inputted to the next stage, which is knowledge presentation. 

## Data Analytics Workflow
	
The following figure depicts the Data Analytics static workflow as opposed to the dynamic workflow proposed.

Figure : Static and Dynamic Data Analytics workflows

While the static workflow follows data cleaning through to knowledge presentation in a deterministic manner, the dynamic workflow provides flexibility of runtime orchestration; the most appropriate next step of the workflow is determined by the output of the previous step, as determined by the domain expert.

## Implemented Data Analytics Workflow Modules


Figure : DA Workflow Modules

## Technologies

* **Swift** is a parallel scripting language, which would abstract the complexities of performing Data Analytics tasks on HPC platforms    
* **GoLang** is used as a coordination language to provide concurrency. 
* **Python3.6** would be used to program logic of Data Analytic modules.
* Python libraries such as, **TensorFlow, Pandas, scikit-learn, Matplotlib and NumPy** in order to facilitate Data Analytics.
* **Angular 6** would be used for the front-end of the web application, with the back-end developed using GoLang.

## How to run the framework

Set necessary parameters in userScript.py by modifying the file.

Navigate to the framework folder from the Linux terminal. 

Run the command : **go run main.go**
