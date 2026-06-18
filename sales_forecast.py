import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
df = pd.read_csv("/Users/ashna/Desktop/Predictive Sales Forecast/Dataset/Sample - Superstore.csv", encoding='latin1')

print("=" * 50)
print("DATASET SHAPE")
print(df.shape)

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly Sales
monthly_sales = df.groupby(
    df['Order Date'].dt.to_period('M')
)['Sales'].sum().reset_index()

monthly_sales['Order Date'] = monthly_sales['Order Date'].astype(str)

# Create Month Number
monthly_sales['Month_Number'] = range(1, len(monthly_sales) + 1)

# Features and Target
X = monthly_sales[['Month_Number']]
y = monthly_sales['Sales']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predictions
monthly_sales['Predicted_Sales'] = model.predict(X)

# Accuracy Metrics
mae = mean_absolute_error(y, monthly_sales['Predicted_Sales'])
r2 = r2_score(y, monthly_sales['Predicted_Sales'])

print("\nMean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# Forecast Next 12 Months
future_months = pd.DataFrame({
    'Month_Number': range(
        len(monthly_sales) + 1,
        len(monthly_sales) + 13
    )
})

future_predictions = model.predict(future_months)

print("\nFORECAST FOR NEXT 12 MONTHS")

for i, value in enumerate(future_predictions, start=1):
    print(f"Month {i}: ${value:.2f}")

# Plot Actual vs Predicted
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales['Month_Number'],
         monthly_sales['Sales'],
         label='Actual Sales')

plt.plot(monthly_sales['Month_Number'],
         monthly_sales['Predicted_Sales'],
         label='Predicted Sales')

plt.title("Sales Forecast")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.legend()

plt.savefig("sales_forecast.png")
plt.close()

print("\nChart Saved: sales_forecast.png")
print("\nPROJECT COMPLETED SUCCESSFULLY")