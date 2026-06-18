# Predictive Sales Forecast using Machine Learning

## Project Overview

This project aims to predict future sales trends using historical sales data. A Linear Regression model is used to analyze past sales patterns and forecast sales for the next 12 months.

## Objective

The objective of this project is to:

- Analyze historical sales data
- Identify sales trends over time
- Build a predictive model for forecasting future sales
- Generate insights that can support business decision-making

## Dataset

- Dataset: Sample Superstore Dataset
- Records: 9,994
- Features: 21

The dataset contains information about orders, customers, products, sales, profit, and order dates.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Machine Learning Model

- Linear Regression

## Project Workflow

1. Data Loading and Preprocessing
2. Date Conversion and Time-Series Aggregation
3. Monthly Sales Analysis
4. Feature Engineering
5. Model Training using Linear Regression
6. Sales Forecast Generation
7. Visualization of Actual vs Predicted Sales

## Results

### Dataset Size

- Rows: 9,994
- Columns: 21

### Model Performance

- Mean Absolute Error (MAE): 17,457.73
- R² Score: 0.25

### Forecasted Sales for Next 12 Months

| Month | Predicted Sales |
|---------|-------------:|
| 1 | $69,957.54 |
| 2 | $70,859.54 |
| 3 | $71,761.55 |
| 4 | $72,663.56 |
| 5 | $73,565.57 |
| 6 | $74,467.57 |
| 7 | $75,369.58 |
| 8 | $76,271.59 |
| 9 | $77,173.60 |
| 10 | $78,075.60 |
| 11 | $78,977.61 |
| 12 | $79,879.62 |

## Output

The project generates:

- Sales forecast for the next 12 months
- Performance metrics
- Sales forecast visualization chart (`sales_forecast.png`)

## Conclusion

The Linear Regression model successfully identified sales trends and generated future sales forecasts. This project demonstrates the use of machine learning techniques for business forecasting and data-driven decision-making.

## Author

Ashna Fathima