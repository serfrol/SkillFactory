# Amazon Toy Price Prediction  

Purpose of this project is to create a model that predicts toy's price based on it's description, customers' review, category, weight and other features.
The business puprose of this project could be buying toys that have lower price than it should be and then selling those toys for a higher price.  
  
Evaluation metric: **RMSE**

## Features
- **price** - Target feature
- **number_available_in_stock** - number of toys available
- **number_of_reviews** - number of reviews left buy customers
- **number_of_answered_questions** - number of answered questions
- **average_review_rating** - average rating of a toy
- **weight_g** - weight of a toy in grams
- **total_rank** - rank among all categories
- **sub_rank** - rank in subcategory
- **sellers_count** - count of people selling the toy
- **description** - technical description of a product
- **customer_reviews** - customer reviews (text)
- **category** - Amazon toy category
- **sub_category** - Amazon toy subcategory
- **manufacturer** - manufacturer name

## Stages
- ### Preprocessing
Modifying columns for ML, extracting valuable information
- ### Naive Model
Naive model to get first prediction
- ### EDA
Statistical analysis of all columns
- ### Text Analysis
Analysis of text columns, tokenization, lemmatization, sentiment analysis, text embeddings as features
- ### ML & DL
Usage of different ML models (RandomForestRegressor, CatBoost, ...), NLP for text columns, blending
