import streamlit as st

st.markdown("\n")
st.header("Algorithm Analysis")
data = ""
st.markdown(''' ### 1) Decision Tree:\n
##### Advantages:\n
• ***Simplicity***: Easy to understand and interpret.\n
• ***Adaptability***: Can be used with limited data.\n
• ***Scenario analysis***: Helps evaluate different outcomes.\n
• ***Transparency***: Decision-making process is clear.\n
• ***Combinability***: Can be combined with other techniques.\n
##### Disadvantages:\n
• ***Sensitivity***: Small changes in data can significantly impact the tree structure.\n
• ***Accuracy***: May be less accurate than other predictors for large datasets.\n
• ***Bias***: Can be biased towards attributes with more levels.\n
• ***Complexity***: Calculations can become complex with uncertainty and multiple 
linked outcomes.\n
### 2) K-Nearest Neighbors:\n
##### Advantages:\n
• ***Robustness***: KNN is relatively robust to noisy training data, especially when 
using inverse square weighted distance.\n
• ***Effectiveness with large datasets***: It can be effective even with large 
amounts of training data.\n
##### Disadvantages:\n
• ***Parameter tuning***: Determining the optimal value of K (the number of nearest 
neighbors) can be challenging.\n
• ***Distance metric selection***: Choosing the appropriate distance metric and 
attributes can significantly impact performance.\n
• ***Computational cost***: Calculating distances between a query instance and all 
training samples can be computationally expensive. Techniques like K-D trees 
can help reduce this cost.\n
### 3) Logistic Regression:\n
##### Advantages:\n
• ***Efficiency***: Logistic regression is computationally efficient, making it suitable for 
large datasets.\n
• ***Interpretability***: The model's coefficients can be interpreted to understand the 
relationship between features and the outcome.\n
• ***Scalability***: It doesn't require scaling of input features.\n
• ***Simplicity***: Logistic regression is easy to implement and train.\n
• ***Regularization***: It's straightforward to apply regularization techniques to prevent 
overfitting.\n
• ***Well-calibrated probabilities***: The predicted probabilities are well-calibrated, 
meaning they accurately reflect the likelihood of the outcome.\n
##### Disadvantages:\n
• ***Linearity assumption***: Logistic regression assumes a linear relationship between 
the features and the log odds of the outcome. This can limit its applicability to non-linear problems.\n
### 4) Random Forest Classifier:\n
##### Advantages:\n
• ***Overfitting prevention***: Combining multiple decision trees helps reduce 
overfitting, a common problem in decision trees.\n
• ***Lower variance***: Random forests generally have lower variance than a single 
decision tree, making them more robust to variations in the data.\n
• ***High accuracy***: Random forests often achieve high accuracy due to their 
ensemble nature.\n
• ***Flexibility***: They can handle various types of data and don't require extensive data 
preparation.\n
• ***Missing data tolerance***: Random forests can maintain accuracy even with 
missing data.\n
##### Disadvantages:\n
• ***Complexity***: Constructing random forests is more complex and time-consuming 
than building a single decision tree.\n
• ***Computational resources***: They require more computational resources 
compared to decision trees.\n
• ***Interpretability***: Understanding the relationships within a large collection of 
decision trees can be challenging.\n
• ***Prediction time***: Predictions using random forests can be slower than some other 
algorithms.''')
