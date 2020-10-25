**Abstract**

The main focus of this paper is to showcase the soccer analysis done by leveraging two datasets. The most fan clubs are associated with soccer and there’s a huge revenue made in this area of sports. If a manager wants to buy out a European league team, within a given budget, we try to help this new manager invest his money with the best possible team along with five swaps at max to make the team even better. We filtered out teams having an overall average rating above 75% from the primary dataset [sofifa dataset](https://sofifa.com/), which is the qualifying criteria. We picked the best possible team in the given budget. To further make sure the team with the best overall ratings really has the best players, we use the remaining amount to swap our players with the better ones from the other teams. We consider a few features variables from the secondary data set to improve the model efficiency. 


**1.1 Problem Statement:**

The objective of our algorithm is to maximize the team’s overall statistics by accumulating players with the highest ‘Ratings’ within the constrained budget.<br>
1. The ‘sofifa’ dataset has extensive data. The first step includes gathering the required domain knowledge of the dataset<br>
2. Perform sanity checks to ensure the data falls in the expected range of values. These ranges will be defined by our knowledge about the sport.
3. We predict ‘Overall Rating’ of the players for the year 2020 based on 10 years of data from the primary dataset. 
4. Then we predict ‘Overall Rating’ for 2020 by Joining Date of Birth (Age) column from our secondary dataset with our Primary Dataset.
5. We compare the model in 4 and 5 based on Regression Algorithms: Decision Trees Regressor, SVM (SVR), Linear Regression and Random Forest Regressor. 
6. We use the best model with the minimum RMSE value to form our dataset for Optimization Algorithm.
7. We build a proprietary optimization algorithm to tackle our problem statement and predict the best team in the given budget.


**1.2 Data Acquisition:**

As we need to minimize the RMSE value of the model, hence we decided to use some supplementary source: [kaggle-soccer](https://www.kaggle.com/hugomathien/soccer).<br>

What Data Sources are we using?<br>
*Dataset:*<br>
- We identify the data from soFIFA(primary dataset) and Kaggle(secondary dataset) which includes more than 100,000 rows of players (before pre-processing) with 15 prediction   variables and a target variable of overall rating from years 2009-2019.<br>

*Web Scraping:* <br>
- We start by web scraping the data from html tables from our primary datasource, using-beautifulsoup4, BS4, HTML5lib, requests, URLlib3, webencoddings.<br>
- Each predictor variable (columns) are then stored into an array.<br>
- This array is converted into a dataframe and the data frame is then pushed into the .csv files.<br>


