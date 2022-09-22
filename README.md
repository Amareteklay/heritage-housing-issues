# HouPP: Housing Price Predictor

HouPP is a Machine Learning project that helps users predict the sales prices of houses taking the houses' attributes as inputs.
[HouPP is live on Heroku](https://houpp.herokuapp.com/).


## 1. Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





## 2. Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* 2 - The client is interested to predict the house sales price from her 4 inherited houses, and any other house in Ames, Iowa.

In order to address the business requirements, we have the following epics and user stories. Each user story is further broken down to manageable stasks, and the agile process was used to implement each task. 

### Epics

* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

### User Stories

* **US1:** As a client, I want to know which attributes of a house are most correlated with its sale price so that I can set the right price for each house.
* **US2:** As a client, I want to have reliable prediction of the sale price of houses I have inherritted so that I can sell them at the maximum total price possible.
* **US3:** As a technical user, I want to learn about the ML steps that were used to arrive at the sale price prediction so that I can understand the model employed.
* **US4:** As a technical user, I want to know the model performance so that I can ensure that the predictions are reliable.
* **US5:** As a client, I want to get a dashboard so that I can display the results of the prediction on a standalone app.
* **US6:** As a user, I want to have interactive input widgets so that I can provide real-time house data and predict the sale price.
* **US7:** As a user, I want to see relevant plots so that I can visualize the relationships between sale price and other features.
* **US8:** As a user, I want to have access to the data cleaning and preparation pipeline so that I can quickly predict sale price without reinventing the wheel.
* **US9:** As a user, I want to know the source and content of the data used in training the model so that I can be confident about the quality of the trained model.
* **US10:** As a user, I want to know the project hypotheses and how they were validated so that I understand 
### Tasks



## 3. Hypotheses and how to validate?
* Size matters. Variables that are associated with the size of the house are positively correlated to sale price.
  * We will examine correlations between attributes about the size of the house and the sale price.
* Ratings of the quality and condition of the house reflect its value and thus its sale price.
  * We will use the correlation between variables about the different ratings of the house and the sale price to validate this hypothesis.
* Age of the house is expected to have significant influence on the sale price of the house.
  * We study when the house was built and how expensive it is to test this hypothesis.


## 4. Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation study
  * We will inspect the sale price of the houses in the data and plot a histogram to understand its distribution.
  * We will study the magnitudes and directions of correlation between the attributes and sale price of the houses. We will compute both Peason and Spearman correlations.
  * We will plot the key variables against the sale price of the houses to illustrate the nature of relationship.

* **Business Requirement 2:** Regression Analysis
  * As the target variable we are interested to predict is continuous, we will do regression analysis. In case the performance of our regression model is poor, we may change this to a classification problem.
  * Not all attributes will have the same effect on the sale price. We want to identify variables that contribute to the lion's share of the price so that our customer can maximize price by leveraging these factors. We will use PCA to identify these variables.
## 5. ML Business Case
(**Note terminologies**)
* In the previous bullet, you potentially visualized a ML task to answer a business requirement. You should frame the business case using the method we covered in the course 
  * Note: a Business Case for each ML model considering the model objective, outcome, metrics, output, heuristic and training data, and the Dashboard Design.
### Predict price
##### Regression model
* The target variable is sale price of houses. Given the continuous-valued target, we want to create an ML model that predicts the sale price of a house with various attributes. We will use a regression model, and it is a supervised machine learning problem because we have sale prices of the houses in our dataset.
* Having caliberated the parameters of the ML model, we want to help users of this application to predict the sale prices of houses with different characteristics.
* As performance metrics for the model, we will use
  * an R2 score of at least 0.75.
* The model will not be accepted if R2 is below 0.75. 



## 6. Dashboard Design
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)
### Page 1: Quick project summary
In this page, we will provide a quick summary of
* the project's key terms
* the project dataset
* the business requirements
### Page 2: House prices


### Page 3: Key attributes 


### Page 4: Project hypotheses and validation
(**At least 3**)
* 1. One of the most important attributes that determine the sales price of a house is the property size. This can include the interior and exterior surface area of the property. 
  * We hypothesize that houses with a lot of space have higher prices.

* 2. The ages of a house and its sales price might be related. Specifically, recently built houses are likely to have modern facilities and thus higher sales prices.
  * We noted that modern houses have higher prices(**Edit later**).

### Page 5: Predict price

* The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.


## 7. Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## 8. Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## 9. Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.
* Numpy
* Pandas
* Scikit-learn
* Matplot-lib
* Seaborn
* Jupyter
* StreamLit



## 10. Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



### Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

