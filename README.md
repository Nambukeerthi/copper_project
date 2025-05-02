
<h1> Industrial_Copper_Modeling </h1>


<h1 align="center">
  <br>
  <a href=""><img src="data/copper-wire-1.jpg" alt="" width="400"></a>
  
  <h2  align="center">
  Link: https://copperproject-wlksjkfyhnyhhbnsyhkued.streamlit.app/
  </h2>  
  <br>
 
  <br>
</h1>


<p align="center">
  <a href="#Introduction"></a> 
  <a href="#Technologies Applied"></a>  
</p>

Video Link: [Linked-IN Video](https://www.linkedin.com/posts/nambu-keerthi-r-9b8839283_project-name-industrial-copper-model-project-activity-7296603762872262657-FJoL?utm_source=share&utm_medium=member_android&rcm=ACoAABMFg5wB3AA0b9CHRbG1E_77kFaZB8cVz7c)

Portfolio: [Nambu Keerthi](https://portfolio-b5zieg8xn5nhwau5b4bhp8.streamlit.app/)

## Introduction 
This project aims to develop two machine learning models for the copper business:

1. Selling Price Prediction Model – To accurately forecast copper selling prices.
2. Lead Classification Model – To classify leads effectively.

Manually predicting prices and managing leads is time-consuming and may lead to poor decisions. These models will automate the process, improving accuracy and efficiency. These models will help in making better price decisions and efficient lead management. 

**Domain** : *Manufacturing* 

## Technologies Applied
* Python
* Streamlit 
* Pandas 
* Numpy
* Skikit- Learn


## Project Setup
1. Firstly install all the required extensions in the requirements.txt
```
pip install -r requirements.txt
```

2. Second get the Data from the Data source and Load the data for Data cleaning and Pre Processing. Then finding the outliers for removing then make it visible the dataset columns by using matplotlib and seaborn.
```
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(dataframe['column_name'])
plt.show()
```

3. After that should make heatmap visualization to knowning how data values are spreaded there. 
```
x=df_p[['quantity tons_log','application','thickness_log','width','selling_price_log','country','customer','product_ref']].corr()
sns.heatmap(x, annot=True, cmap="YlGnBu")

```
4. Then split the dataset as well as  train and test data for creating ML models. Save the models in ".pkl" file 
```
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

```
  

6. Last we can run the streamlit app
```
streamlit run copper.py
```

   
## Project Methodology

**Selling Price Prediction**

1. Select the "Predict Selling Price" tab. Fill in the following required informations.

2. Click the "Predict Selling Price" button. The app will display the predicted selling price based on the provided information.

**Status Prediction**

3. Select the "Predict Status" tab. Fill in the following required informations.


4. Click the "Predict Status" button. The app will display the predicted selling price based on the provided information.
