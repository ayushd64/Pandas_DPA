1.1 Problem Statement:

 	The objective of our algorithm is to maximize the team’s overall statistics by accumulating players with the highest ‘Ratings’ within the constrained budget. 
The ‘sofifa’ dataset has extensive data. The first step includes gathering the required domain knowledge of the dataset
Perform sanity checks to ensure the data falls in the expected range of values. These ranges will be defined by our knowledge about the sport.
We predict ‘Overall Rating’ of the players for the year 2020 based on 10 years of data from the primary dataset. 
Then we predict ‘Overall Rating’ for 2020 by Joining Date of Birth (Age) column from our secondary dataset with our Primary Dataset.
We compare the model in 4 and 5 based on Regression Algorithms: Decision Trees Regressor, SVM (SVR), Linear Regression and Random Forest Regressor. 
We use the best model with the minimum RMSE value to form our dataset for Optimization Algorithm[8].
We build a proprietary optimization algorithm to tackle our problem statement and predict the best team in the given budget.

