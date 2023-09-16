# IDS 706 Data Engineering Mini Project 3

## Overview
This repository is created using my Mini Project 1 template. It uses several Pandas as well as Polars library functions and returns descriptive statistics for a given cereal data. 

Dataset used: [Cereal Dataset]([https://www.kaggle.com/datasets/crawford/1000-cameras-dataset](https://www.kaggle.com/datasets/crawford/80-cereals))

## Key components in the repository are:
- `cereal.csv`
- `Makefile`
- `requirements.txt`
- `Dockerfile`
- `.devcontainer`
- `main.py`
- `test_main.py`
- `Summary_Report`
- `GitHub Actions`

## Result
- **make lint** : Check poorly structured code and stylistic errors. 
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/878442a5-27a3-4bb2-8076-d255f9b812fc)

- **make test** : It passed tests on all the functions I defined.
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/06dbcd6f-41dc-4ffc-a908-35766c273169)

- **make format**: Apply formatting checks 
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/42462fe3-ad70-4d12-a4ba-736a9c2232a4)

## Output from test_main.py
This shows top five columns of dataframe with head function, summary statistics of a 'Price' column, and a scatter plot. Summary statistics used Pandas describe() function and it includes mean, median, and standard deviation of Price feature. 
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/36daec02-a433-4053-afca-9219b35d2767)
![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/aaf08908-49dd-4575-bc5f-5b332c17515d)

## Data Visualization (Storage vs. Weights of cameras) 
It used Pandas plot function with matplotlib library and explains no relationship between cameras' storage and weights. 

![image](https://github.com/nogibjj/IDS706-Mini-Project2-/assets/141780408/44cff96e-5eef-469f-8fa9-e6d4da628446)
