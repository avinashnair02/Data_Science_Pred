<!-- # Data Science Salary Estimator: Project Overview 


* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2



## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 

 

 -->


# Data-Science-Salary-Estimator
>> `BEST WITH LIGHT-MODE`
>> `FORK & STAR THIS PROJECT. USE IT AS YOUR BEGINNERS DATA SCIENCE PROJECT`

## Project Synopsis

* Created a tool that estimates Data Science salaries *{Mean Absolute Error(MAE) ~ $ 11K}* to help rookie Data Scientists negotiate their income with correct stats when they get a job.
* Using **Python & Selenium**, created an automated scraper which scraped over 1000+ job descriptions from *GlassDoor*
* Introspected features from the text inputs provided in each job description to quantify what values/skills MNCs put on **Python, MS-Excel, AWS, & Spark**.
* Optimized **Linear, Lasso, & Random Forest Regressors** using **GridsearchCV & Scikit-Learn** to reach the best model.
* Built a client facing Representational State Transfer API using Flask.

-------------------------------
## Project Walk-through

### Data Collection {Web Scraping}


Desgined an automated Web scraper with selenium to scrape 1000+ job postings from [GlassDoor](https://www.glassdoor.co.in/). 
With each job; attributes to be focused were:

    Job title
    Salary Estimate
    Job Description
    Rating
    Company
    Location
    Company Headquarters
    Company Size
    Company Founded Date
    Type of Ownership
    Industry
    Sector
    Revenue
    Competitors
    
    --------------------------
    Pre-requisites at this stage are: 
    Selenium WebDriver for FireFox (or Chrome)
    Selenium Automation Documentation

*For other resources scroll at last*

#### Click **.py** file-icon Below to redirect to Web Scraper Code & Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/blob/master/glassdoor_scraper.py">
<img src="https://img.icons8.com/ios-glyphs/2x/python.png" width="5%" height="5%">
</a>

------------------------------


## Data Cleaning

After scraping the data, I cleaned the cluttering data for it to be usable/readable for the model. Changes I made and what all variables & scripts I wrote:

    * Parsed numeric data out of salary
    * Made seperate columns for employer for given dataset of salary and hourly wages
    * Removed rows without salary
    * Parsed rating out of company_text
    * Made a new column for company_state
    * Added a column for if: job was at the company’s headquarters
    * Calculated age of the company by transforming Company founded/established year data
    * Made columns for if different skills were listed in the job description:
        -> Python
        -> R
        -> Excel
        -> AWS
        -> Spark
    * Column for simplified job title and Seniority
    * Column for description length


#### Click Git-Branch Icon Below to redirect to Data-Cleaning Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/data_cleaning">
  <img src="https://img.icons8.com/ios-filled/2x/compare-git.png" width="5%" height="5%">
</a>

-------------------------------
## EDA {Exploratory Data Analysis}

* All the imported distributions from data cleaning data-set, I looked at the distributions of the data and the value counts for the various categorical variables.
* Using **Matplotlib & Seaborn**, categorised and crafted a beautiful data visualisation charts & plots
* Below are a few highlights from the *Pivot tables, Barplots & HeatMaps*.

![alt text](https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/salary_by_job_title.PNG) ![alt text](https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/positions_by_state.png)

![alt text](https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/correlation_visual.png)

![alt text](https://github.com/VivanVatsa/Data-Science-Salary-Estimator/blob/master/assets/Screenshot%202020-12-21%20211042.png)


#### Click Line-Graph Icon Below to redirect to EDA Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/data_eda">
  <img src="https://img.icons8.com/pastel-glyph/2x/increase-profits.png" width="5%" height="5%">
</a>

-----------------------------


## Model Building

* First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.
* I tried three different models and evaluated them using *Mean Absolute Error*. 
* Chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Using **Matplotlib, Pandas, Numpy, Sklearn-Models,  GridSearchCV** 
Designed **three different Models** for this Data-Set:

* **Multiple Linear Regression** –> Baseline for the model
* **Lasso Regression** –> Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* **Random Forest** –> Again, with the sparsity associated with the data, I thought that this would be a good fit.

#### Click Model-Building Icon Below to redirect to Model_Building Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/model_building">
  <img src="https://img.icons8.com/windows/2x/settings--v2.gif" width="5%" height="5%">
</a>

--------------------------------


## Model performance

The **Random Forest model** far outperformed the other approaches on the test and validation sets.

* **Random Forest : *MAE* = 11.06711409395973**
* **Linear Regression: *MAE* = 18.855189990211073**
* **Ridge Regression: *MAE* = 19.665303712749914**

#### Click Performance-Meter Icon Below to redirect to Model_Building Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/model_building">
  <img src="https://img.icons8.com/ios/2x/speed.png" width="5%" height="5%">
</a>

-------------------------------


## Model Productionization

* The last step in this Project was to build a **Flask API** endpoint that was hosted on a *local webserver.*
* Several Articles helped in Deployment of the Model on a local server (*all resources linked at last*)
* The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

#### Click Flask API Icon Below to redirect to flask_API Branch Workspace
<a href="https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/flask_API">
  <img src="https://img.icons8.com/ios/2x/api-settings.png" width="5%" height="5%">
</a>

------------------------------


## Resources Consumed for this project & where you can find them:

    Python Ver: 3.9.0
    Packages Used: Pandas, Numpy, Sklearn, Matplotlib, Seaborn, Selenium, Flask, Json, Pickle
    For Web Framework Requirements type in console >> pip install -r requirements.txt
* Selenium WebDrivers: 
    * [FireFox - GeckoDriver](https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/master/drivers) 
    * [Chrome - ChromeDriver](https://github.com/VivanVatsa/Data-Science-Salary-Estimator/tree/master/drivers)
* Scikit-learn Documentation: [Click here](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
* Matplotlib Documentation: [Click here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html?highlight=boxplot#matplotlib.pyplot.boxplot)
* Seaborn Documentation: [Click here](http://seaborn.pydata.org/examples/many_pairwise_correlations.html)
* Scraper Github: [Click Here](https://github.com/arapfaik/scraping-glassdoor-selenium)
* Flask Model-Productionization: [Click Here](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)
* Ken Jee Data Science Tutorials: [Ken Jee YouTube Channel](https://www.youtube.com/c/KenJee1)

-----------------------------
