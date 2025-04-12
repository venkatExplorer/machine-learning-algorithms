Machine Learning Models: Regression & Classification
Welcome to my machine learning practice repository! In this project, I've implemented and compared several ML models using scikit-learn in Python. It includes both regression (for salary prediction) and classification (for diabetes prediction) tasks.

Project Files
├── LinearRegression.py
├── LogisticRegression.py
├── DecisionTree.py
├── RandomForest.py
├── NavieBayes.py
└── README.md
Models Included
Regression:
Linear Regression: Predicts salary based on years of experience. I used the R² score to evaluate the model’s performance.

Classification:
Logistic Regression: Used for binary classification in the diabetes dataset. I evaluated it with accuracy and confusion matrix.

Decision Tree: Another model for classifying diabetes outcomes.

Random Forest: A more robust classifier for the diabetes dataset. It performs better than others!

Naive Bayes: A simple but effective classification algorithm, showing decent performance on the diabetes data.

Model Performance at a Glance
Model	Type	Accuracy / R²	Notes
Linear Regression	Regression	0.9553 (R²)	Excellent fit for salary prediction
Logistic Regression	Classification	73.59%	Solid starting point
Decision Tree	Classification	71.42%	Tends to overfit without pruning
Random Forest	Classification	75.32%	Best overall performance
Naive Bayes	Classification	74.46%	Simple but surprisingly effective
How to Get Started
Clone or download this repo to your local machine.

Install the required dependencies:

pip install pandas scikit-learn
Each Python file (e.g., LinearRegression.py, LogisticRegression.py) contains the implementation for each model. To run a model, simply execute the corresponding script in your terminal:

python LogisticRegression.py
Make sure the datasets (data (2).csv for salary prediction, and diabetes.csv for the diabetes prediction models) are correctly located or update the paths in the code accordingly.

Key Insights
Linear Regression gives a great fit for salary prediction.

Random Forest works really well for classification, outperforming other models.

Naive Bayes is a simple model but gets surprisingly good results.

Logistic Regression and Decision Trees provide solid benchmarks but could use improvements.

Need Help?
Feel free to reach out or open an issue if you have any questions or suggestions. I’m happy to help!

