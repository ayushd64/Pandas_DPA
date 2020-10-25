# Abstract

The main focus of this paper is to showcase the soccer analysis done by leveraging two datasets. The most fan clubs are associated with soccer and there’s a huge revenue made in this area of sports. If a manager wants to buy out a European league team, within a given budget, we try to help this new manager invest his money with the best possible team along with five swaps at max to make the team even better. We filtered out teams having an overall average rating above 75% from the primary dataset [sofifa dataset](https://sofifa.com/), which is the qualifying criteria. We picked the best possible team in the given budget. To further make sure the team with the best overall ratings really has the best players, we use the remaining amount to swap our players with the better ones from the other teams. We consider a few features variables from the secondary data set to improve the model efficiency. 


### 1.1 Problem Statement:

The objective of our algorithm is to maximize the team’s overall statistics by accumulating players with the highest ‘Ratings’ within the constrained budget.<br>
1. The ‘sofifa’ dataset has extensive data. The first step includes gathering the required domain knowledge of the dataset<br>
2. Perform sanity checks to ensure the data falls in the expected range of values. These ranges will be defined by our knowledge about the sport.
3. We predict ‘Overall Rating’ of the players for the year 2020 based on 10 years of data from the primary dataset. 
4. Then we predict ‘Overall Rating’ for 2020 by Joining Date of Birth (Age) column from our secondary dataset with our Primary Dataset.
5. We compare the model in 4 and 5 based on Regression Algorithms: Decision Trees Regressor, SVM (SVR), Linear Regression and Random Forest Regressor. 
6. We use the best model with the minimum RMSE value to form our dataset for Optimization Algorithm.
7. We build a proprietary optimization algorithm to tackle our problem statement and predict the best team in the given budget.


### 1.2 Data Acquisition:

As we need to minimize the RMSE value of the model, hence we decided to use some supplementary source: [kaggle-soccer](https://www.kaggle.com/hugomathien/soccer).<br>

What Data Sources are we using?<br>
*Dataset:*<br>
- We identify the data from soFIFA(primary dataset) and Kaggle(secondary dataset) which includes more than 100,000 rows of players (before pre-processing) with 15 prediction   variables and a target variable of overall rating from years 2009-2019.<br>

*Web Scraping:* <br>
- We start by web scraping the data from html tables from our primary datasource, using-beautifulsoup4, BS4, HTML5lib, requests, URLlib3, web-encoddings.<br>
- Each predictor variable (columns) are then stored into an array.<br>
- This array is converted into a dataframe and the data frame is then pushed into the .csv files.<br>


### 1.3 Data Understanding, Cleaning and Preparation:

*Predictor Variables* <br>
Age <br>
Name <br>
Team <br>
Best Overall <br>
Position  <br>
Attacking stats <br>
Movement stats <br> 
Goalkeeper stats <br>
Power stats <br>
Defense stats <br>
Skill sets <br> 
Total potential <br> 
market value <br>
Wage <br>
Predicted overall rating <br>
Actual overall rating <br>
 <br>
Used for the model: [["Age", "Best Overall", "Attacking stats", "Movement stats", "Power stats", "Defense stats", "Skill sets", "Total potential", "Market_value", "Wage"]]
 <br>
Various approaches for data cleaning <br>
- We first read the CSV files consisting of all data from years, 2009-2019. <br>
- Duplicate Entries: Removing Duplicates by Key - Player ID. <br>
- Missing Values: Drop unnamed columns <br>
- Units- ‘Wage’, ‘market_value’ columns have units in M (10,00000) and K (1,000). We converted from alpha-numeric to numeric values. <br>
- Alpha Numeric Values: Remove Columns such as ‘Team’, ‘Name’, ‘Position’ <br>
- Table Joins (Primary and Secondary dataset)- By Player ID <br>
- We dropped the rows which had ‘market_value’=0 and ‘Wage’=0 <br>


### 1.4 Exploratory Data Analysis

#External data sources:

link[https://sofifa.com/?hl=en-US&r=190075&set=true]

link[https://www.kaggle.com/hugomathien/soccer]

Measures precisely in business terms the value of these data sets to their business problem.

#Secondary Data Set

#How did we leverage it?
We used the ‘player‘ table from the database present in the link: link[https://www.kaggle.com/hugomathien/soccer]
From the player table, we used the ‘birthday’ column to calculate the age.
We joined the primary and secondary data sets on the ‘id’ column using the inner join.
That’s how we leveraged the secondary data set in our problem statement. 


#Data Analysis:

This part includes plotting the data that we cleaned, before prediction, to analyse and make better predictions on our data.
Some of the plots include:



  ![Image of plot](https://github.com/ayushd64/Pandas_DPA/blob/master/before_prediction/Dashboard%201.png)
Fig 4: Age vs Avg. Power stats                                   Fig 5: Age vs Avg. Skill sets








Fig 6: Age vs Avg. Total potential                                   	Fig 7: Age vs Avg. Best Overall


               
      
Fig 8: Age vs Avg. Overall Rating                             Fig 9: Age vs Count of Age



 
Fig 10: Age vs Avg. Defense stats





CONCLUSION:

From the above plots, we observed that age can be an important factor for our model.


