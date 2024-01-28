# Loan Approval Predictor

**Problem Statement:**
The task is to develop a machine learning model to predict whether a loan application will be approved or rejected based on various features provided by the applicant.

**Introduction:**
This project aims to create a loan approval predictor using a dataset containing information about loan applicants. The goal is to build a model that can accurately predict whether a loan will be approved or rejected, thereby assisting in the decision-making process for loan approvals.

**Data Exploration:**
The initial step involves exploring the dataset to understand its structure and characteristics. The dataset includes features such as education level, employment status, income, loan amount, loan term, credit score, and various asset values.

**Data Preprocessing:**
1. Data Cleaning: The dataset is cleaned by removing unnecessary columns and handling missing values.
2. Feature Engineering: New features are created by combining asset values into a single 'assets' column.
3. Encoding Categorical Variables: Categorical variables like 'education' and 'self_employed' are encoded into numerical values for model compatibility.

**Exploratory Data Analysis (EDA):**
Visualizations such as bar plots, histograms, and box plots are used to gain insights into the data distribution and relationships between variables. This helps in understanding the impact of different features on the loan approval process.

**Model Building:**
1. Data Splitting: The dataset is split into training and testing sets.
2. Feature Scaling: Standard scaling is applied to normalize the numerical features.
3. Model Selection: A Random Forest Classifier is chosen for its ability to handle complex datasets and provide accurate predictions.
4. Model Training: The Random Forest model is trained using the training dataset.
5. Model Evaluation: The trained model is evaluated using the testing dataset, and performance metrics such as accuracy and classification report are generated.

**Results:**
The Random Forest Classifier achieves a high accuracy rate of over 95% in predicting loan approval status. The model provides valuable insights into the factors influencing loan approval decisions and can assist financial institutions in making informed lending decisions.

**Conclusion:**
The loan approval predictor developed in this project demonstrates the effectiveness of machine learning techniques in automating decision-making processes. By accurately predicting loan approval outcomes, the model can help financial institutions streamline their loan approval process and improve customer satisfaction.

**Technologies Used:**
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn (Random Forest Classifier, StandardScaler)
- Pickle (for model serialization)
