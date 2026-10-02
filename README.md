# House Price Prediction & Housing Crash Simulator

## Project Overview

This project was developed as part of the AI/ML Engineering Virtual Internship Program.

The project uses Linear Regression to predict house sale prices based on property characteristics. It also includes an interactive Streamlit Housing Crash Simulator that demonstrates how increasing interest rates could affect the displayed predicted house price.

## Dataset

The project uses the House Prices: Advanced Regression Techniques dataset from Kaggle.

The training dataset contains 1,460 houses and includes information about property characteristics and their final sale prices.

Target variable:
- `SalePrice`

## Features Used

Seven numerical features were selected for the regression model:

- `OverallQual` - Overall material and finish quality
- `GrLivArea` - Above-ground living area
- `GarageCars` - Garage capacity
- `TotalBsmtSF` - Total basement area
- `FullBath` - Number of full bathrooms
- `BedroomAbvGr` - Number of bedrooms above ground
- `YearBuilt` - Original construction year

## Data Preprocessing

The dataset was explored for missing values before model training.

The selected seven numerical features contained no missing values, so no missing-value imputation or row removal was required for the model.

The dataset was divided into:

- 80% training data
- 20% testing data

A `random_state` of 42 was used to make the split reproducible.

## Model

A Linear Regression model was trained using Scikit-learn.

The model learns the relationship between the selected property characteristics and `SalePrice`.

## Model Performance

The model was evaluated using unseen testing data.

- RMSE: **$38,998.66**
- R² Score: **0.802**

The project also includes a residual plot and 10 sample predictions compared with their actual sale prices.

## Housing Crash Simulator

The Streamlit application allows users to enter property characteristics and receive a predicted house price.

An Interest Rate Simulator allows the interest rate to be increased from 3% to 8% and displays the simulated effect on the predicted house price in real time.

### Simulation Assumption

Interest rates are not included as a feature in the Kaggle training dataset.

Therefore, the interest-rate effect is implemented as a separate simulation layer and was not learned by the Linear Regression model.

For demonstration purposes, the simulator assumes that each 1 percentage-point increase in the interest rate above 3% reduces the displayed predicted house price by 5%.

This assumption is used only to demonstrate the interactive Housing Crash Simulator.

## Project Structure

```text
HousePricePrediction/
├── data/
│   └── train.csv
├── examples/
│   └── sample_predictions.csv
├── images/
│   └── residual_plot.png
├── models/
│   └── house_price_model.pkl
├── app.py
├── house_price_prediction.ipynb
├── README.md
├── requirements.txt
└── .gitignore