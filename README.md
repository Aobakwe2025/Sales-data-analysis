# Sales-data-analysis
📌 Project Overview

This project focuses on data collection, data management, data cleaning, and basic data analysis using a real-world sales dataset. The aim is to demonstrate how structured data is handled, transformed, and analyzed using Microsoft Excel.

The dataset was provided as part of Week 2: Data Collection & Management and is stored in CSV format.

🎯 Project Objectives

The objectives of this project are to:

Understand the data lifecycle and governance

Identify structured data within a real-world dataset

Work with common data file formats (CSV)

Clean and transform raw data for analysis

Extract meaningful insights using Excel functions

🗂️ Dataset Description

File name: Week-2-Sales-Data.csv

Data type: Structured data

Format: CSV (Comma-Separated Values)

Key Attributes in the Dataset

Product

Region

Units Sold

Unit Price

Revenue

Sales Representative

Order Date

Order ID

The dataset contains sales transactions recorded across different regions and products, making it suitable for time-based and performance analysis.

🛠️ Tools & Technologies Used

Microsoft Excel

CSV File Format

Excel Functions:

TEXT()

MONTH()

Sorting & filtering tools

🔄 Data Processing Steps
1️⃣ Data Import

Imported the CSV file into Microsoft Excel.

Verified column headers and data types.

2️⃣ Data Exploration

Identified the dataset as structured data because:

It follows a tabular format

Each column represents a specific attribute

Data entries are consistent and organized

3️⃣ Data Transformation

Created a new Month column from the Order_Date field using:

=TEXT(Order_Date,"mmmm")


This enabled monthly analysis of sales data.

4️⃣ Data Cleaning

Ensured dates were correctly formatted

Checked for missing or inconsistent values

Verified numerical columns for accuracy

📈 Analysis & Insights

Using the cleaned data, the dataset can be analyzed to:

Identify sales trends by month

Compare product performance across regions

Understand sales distribution by sales representatives

Support summary reporting and pivot table analysis

📚 Learning Outcomes

Through this project, the following skills were developed:

Understanding structured vs unstructured data

Working with CSV files

Data cleaning and transformation in Excel

Applying Excel formulas for data analysis

Preparing data for reporting and visualization

📂 Repository Structure
📁 Week-2-Sales-Data
│── 📄 Week-2-Sales-Data.csv
│── 📄 README.md

✅ Conclusion

This project demonstrates the importance of proper data collection and management before analysis. By transforming raw sales data into a structured and analyzable format, meaningful insights can be generated to support decision-making.
>>>>>>> 54cbaccc8c699e4a770ef7513fe7f92abf132101
