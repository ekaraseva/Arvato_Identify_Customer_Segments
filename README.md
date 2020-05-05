# Identify Customers for a Mailout Campaign. 
This project is a part of the Capstone project for Udacity Data Scientist nanodegree. 
The data is provided by Arvato Financial Solutions, a Bertelsmann subsidiary.

## 1. Project Description
A mail-order sales company is interested in identifying segments of the general population to target with their marketing campaign in order to grow. The goal is to identify which individuals are most likely to respond to the campaign and become customers.

Unsupervised learning techniques were used to analyze the attributes of established customers and the general population in order to create customer segments. Thereafter, supervised learning was used to build a model that predicts customers for Arvato Financial Solutions.

## 2. Installation
Clone or download the repository. 

**Prerequisites**
- pandas
- nupmy
- sklearn
- xgboost

For plotting:
- matplotlib
- seaborn

Extra function for oen hot encoding

## 3. Performed steps
The project has three major steps: the customer segmentation report, the supervised learning model, and the Kaggle Competition.

1. Customer Segmentation Report
By using unsupervised learning methods to analyze attributes of established customers and the general population in order to create customer segments.

2. Supervised Learning Model
Build a machine learning model that predicts whether or not each individual will respond to the campaign using the train dataset.

3. Kaggle Competition
Once  the model is chosen, predict response to the campaign and submit your results to a Kaggle Competition.

## 4. Conclusions
One of the main points for a good data science project is to perform a proper exploration of the data, data cleaning and transformation.

After the preparation of the data was completed, I was able to perform data clustering and identify overrepresented clusters of the general population data in the customer data. There is a clear pattern, which people are underrepresented in the customer data.

I advise the company to analyse if underrepresented clusters can be potential clients of the company and to add these individuals to its database. These are mainly younger and poorer people with low financial interest and a more mobile moving pattern.

Using the training data I was able to build a prediction model to predict which individuals are most likely to respond positively to the campaign and become customers. The Gradient Boosting Classification was chosen as the prediction model with the score on the training set of 0.8932.

The next step is to submit the predicted response on the test set to kaggle to see how good the model performs. However, I still have to figure out why I can’t get a connection with the kaggle server.

The link to article: https://medium.com/@lena.karaseva/identify-customers-for-a-mailout-campaign-94a09146444d

## 5. Improvements
At least the following improvements can be done:
- Try different subset of features to see the performance of the model, 
- Double check attribute types.

## 6. Acknowledgement
Thanks to Arvato Financial Solutions for teh provided data set.

Thanks to Udacity for interesting nanodegree content and projects.

Thanks to [Elena Ivanova](https://github.com/lenuel/Capstone-Arvato-Project/blob/master/etl/etl.py) for GetDummies function, as I was stuck with build-in OneHotEncoder and couldn't understand how to get rid of first column after encoding but really wanted to use pipelines for data transformation.
