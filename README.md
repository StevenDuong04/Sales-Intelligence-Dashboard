# Sales-Intelligence-Dashboard

A self-service analytics platform built with Python and Streamlit that enables small businesses to analyze their sales data without requiring SQL or data analytics experience.

Users can upload their sales data, automatically generate key business metrics, visualize trends, and gain actionable insights through an intuitive dashboard.

## Overview

Many small businesses collect valuable sales data but lack the technical knowledge to analyze it effectively. This application bridges the gap by transforming raw sales data into interactive dashboards and meaningful business insights.

The goal is to make sales analytics accessible to non-technical users through a simple upload-and-analyze workflow.

## Features
### Data Upload
- Upload CSV or Excel sales datasets
- Automatic file validation
- Automatic data type detection
- Support for common sales data formats

### Data Cleaning
- Missing value handling
- Duplicate removal
- Date conversion
- Numeric conversion
- Column standardization

### Sales KPIs
- Total revenue
- Total orders
- Average order value
- Total customers
- Total units sold
- Revenue growth
- Top performing product/service

### Sales Analytics
- Revenue over time
- Revenue by category
- Product performance
- Customer analysis
- Sales trends
- Monthly comparisons

### Interactive Dashboard
- Dynamic filters
- Interactive charts
- Executive summary
- Download cleaned dataset
- Export reports

## Workflow
Upload Sales Data \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Load Dataset \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Validate Data \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Clean & Prepare Data \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Calculate Business Metrics \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Generate Interactive Charts \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&darr; \
Display Sales Dashboard

## Techstack
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib

## Expected Dataset
The application expects sales transaction data containing columns similar to:

<table>
  <tr>
    <td>
      <h3>Column</h3>
      <p>transaction_id</p>
      <p>order_date</p>
      <p>customer_id</p>
      <p>product_name</p>
      <p>category</p>
      <p>quantity</p>
      <p>unit_price</p>
      <p>revenue</p>
    </td>
    <td>
      <h3>Description</h3>
      <p>Unique transaction identifier</p>
      <p>Date of purchase</p>
      <p>Customer identifier</p>
      <p>Product/Service sold</p>
      <p>Product/Service category</p>
      <p>Quantity sold</p>
      <p>Price per unit</p>
      <p>Total revenue</p>
    </td>
  </tr>
</table>
Additional columns will be supported when available.

## Dashboard Modules
### Executive Summary
Overview of business performance, including:
- Total Revenue
- Total Orders
- Average Order Value
- Total Customers
- Revenue Growth

### Revenue Analysis
Analyze business performance through:
- Revenue over time
- Revenue by month
- Revenue by category

### Product Analysis
Evaluate product performance with:
- Top-selling products
- Highest revenue products
- Product category comparison

### Customer Analysis
Understand customer behaviour through:
- Top customers
- Customer spendings
- Purchase frequency
- Customer segmentation

### Trend Analysis
Monitor long-term business performance by identifying:
- Monthly trends
- Seasonal patterns
- Revenue growth
- Sales distribution

## Getting Started
### Clone the repository
```
git clone <repository-url> 
cd sales-intelligence-dashboard
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run the application
```
streamlit run app.py
```

## Project Goals
This project was developed to demonstrate practical data analytics and software engineering skills, including:
- Data preprocessing
- Data validation
- Business intelligence
- Dashboard development
- Data visualization
- Modular software architecture
- Python application development

## Target Users
This application is designed for:
- Small business owners
- Entrepreneurs
- Retail businesses
- E-commerce sellers
- Sales managers
- Users with little or no technical background

No SQL or programming knowledge is required to use the dashboard.

## License
This project is intended for educational and portfolio purposes.