# Airflow-ETL-Data-Pipeline-project


## Project Overview:
The pipeline involves extracting data from PostgreSQL is securely staged in an AWS S3 bucket, transformed using Pandas, integrated with a Snowflake data warehouse, and undergoes type two slow change dimension.

## Project Details:
![airflow desc](https://github.com/islamyounis/Airflow-ETL-Pipeline-Data-project/assets/83661639/3b712ba6-6228-460b-babb-6ee78f184d4a)

We have developed a project that leverages the power of AirFlow DAGs to efficiently extract employees' data from the HR and Finance PostgreSQL schemas. This data is then seamlessly loaded into a cutting-edge Snowflake data warehouse, ensuring optimal storage and preserving the complete salary change history.

Our AirFlow DAG is designed to run hourly, diligently checking for any new data within the PostgreSQL source. Upon identification, it efficiently extracts this fresh information and loads it into dedicated AWS S3 buckets, serving as a comprehensive Data Lake that houses all the raw data in CSV file format.

To ensure data integrity and accuracy, we employ a set of sophisticated Python functions. These functions meticulously extract the new records that require insertion, as well as identify the existing records that necessitate updates. By employing the Slowly Changing Dimension (SCD) concept, we diligently maintain a comprehensive historical record of employees' salary changes within the Snowflake Data warehouse.

Through this robust and streamlined process, we empower organizations to effortlessly manage their employees' data, harnessing the power of AirFlow, PostgreSQL, Snowflake, and AWS to optimize data storage, accessibility, and historical record-keeping

## Project Steps:

- 1- Implement an AirFlow DAG that runs on an hourly basis, utilizing the TaskFlow approach to seamlessly pass outputs from one task to another.

-  2- Create two tasks that leverage the power of the SqlToS3Operator operation to extract data from the PostgreSQL schema and store it in AWS S3 buckets in CSV file format. One task is dedicated to extracting HR data, while the other focuses on extracting Finance data.

-  3- Introduce two additional tasks that incorporate Python functions to process the extracted data. These functions will efficiently retrieve the IDs of new records, enabling their insertion into the Data warehouse. Moreover, they will identify records with salary changes, allowing for updates and the insertion of new records with updated values, adhering to the Slowly Changing Dimension (SCD) type 2 concept.

- 4- Load the processed data into the designated table within the Snowflake Data warehouse, ensuring its seamless integration into the existing database structure.

- 5- To ensure smooth execution and prevent potential errors, the Airflow DAG incorporates Python functions implemented using the BranchPythonOperator operation. These functions effectively check for the presence of new records requiring insertion or records requiring updates before proceeding with the respective tasks.

## Tools and Technologies:
- Apache Airflow
- Python
- Pandas
- PostgreSQL
- Snowflake
- AWS S3
- ETL
- Data Warehouse Concepts
- SCD

## Project Files:

- ```Dags```: Contains the AirFlow Dag.
- ```Includes```: Contains the SQL and Python scripts that uses in the AirFlow Dag.
- ```Output```: Contains screenshots from the AirFlow Dag Output. 

## Project Output:
![airflow](https://github.com/islamyounis/Airflow-ETL-Pipeline-Data-project/assets/83661639/20a7012e-e64e-43e3-9665-b6d4a3c62914)


