# Bati Bank Credit Scoring Model

This repository contains the code for building a credit scoring model for Bati Bank's buy-now-pay-later (BNPL) service. The model aims to assess the creditworthiness of customers and predict optimal loan terms.

**Business Need**

Bati Bank is partnering with an eCommerce company to offer a BNPL service. To mitigate risk, a robust credit scoring model is crucial to:

- **Identify high-risk customers:** Minimize potential losses due to defaults.
- **Offer personalized loan terms:** Provide appropriate credit limits and repayment durations for each customer.
- **Enhance customer experience:** Offer a seamless and efficient application process.

**Data**

The dataset used for this project can be found here: [Xente Challenge | Kaggle](https://www.kaggle.com/competitions) 

**Data Fields**

- `TransactionId`: Unique transaction identifier
- `BatchId`: Unique number assigned to a batch of transactions
- `AccountId`: Unique customer identifier
- `SubscriptionId`: Unique customer subscription identifier
- `CustomerId`: Unique customer identifier
- `CurrencyCode`: Country currency
- `CountryCode`: Numerical geographical code of country
- `ProviderId`: Source provider of the item bought
- `ProductId`: Item name being bought
- `ProductCategory`: Product category
- `ChannelId`: Customer's purchase channel (web, Android, iOS, etc.)
- `Amount`: Transaction amount
- `Value`: Absolute value of the transaction amount
- `TransactionStartTime`: Transaction start time
- `PricingStrategy`: Xente's pricing structure for merchants
- `FraudResult`: Fraud status of the transaction (1 - yes, 0 - no)

**Methodology**

1. **Data Preprocessing:**
   - Handle missing values (imputation, removal).
   - Clean and transform data (e.g., feature scaling, encoding categorical variables).
   - Explore data distribution and identify potential outliers.

2. **Feature Engineering:**
   - Create new features based on existing data (e.g., customer lifetime value, purchase frequency, recency).
   - Select features with high correlation to the target variable (default probability).

3. **Model Development:**
   - **Define Target Variable:** Define a proxy variable to categorize users as high-risk or low-risk (e.g., 90-day delinquency rate).
   - **Train Models:** Experiment with various machine learning models (e.g., Logistic Regression, Random Forest, XGBoost).
   - **Evaluate Model Performance:** Assess model accuracy using metrics like AUC, precision, recall, F1-score.

4. **Credit Score Calculation:**
   - Convert predicted probabilities into credit scores using a scoring function (e.g., logistic transformation).

5. **Loan Term Prediction:**
   - Develop a separate model to predict optimal loan amount and duration based on credit score and other relevant factors.

**Model Deployment**

- Deploy the trained models into a production environment for real-time credit risk assessment.
- Monitor model performance and retrain periodically to adapt to changing customer behavior and market conditions.
