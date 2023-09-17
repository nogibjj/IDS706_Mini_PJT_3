[![Python CI](https://github.com/nogibjj/IDS706_Mini_PJT_3/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_Mini_PJT_3/actions/workflows/cicd.yml)

# IDS 706 Data Engineering Mini Project 3

## Overview
This repository is created using my Mini Project 1 template. It uses several Pandas as well as Polars library functions and returns descriptive statistics for a given cereal data. It prints a histogram of a selected column, calories. It also generates Summary_Report file containing summary statistics.  

Dataset used: [80 Cereals](https://www.kaggle.com/datasets/crawford/80-cereals)

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

## Result from test_main.py
- **make lint, test, format**
    -  `make lint` : Check poorly structured code and stylistic errors.
    -  `make test` : It passed tests on function I defined in main.py
    -  `make format` : Apply formatting checks 
![image](https://github.com/nogibjj/IDS706_Mini_PJT_3/assets/141780408/d347a525-c746-4933-80d9-ca486d916ab2)

## Output 
This shows summary statistics of the given cereal dataframe. The below table displays continuous variables' statistics like mean, max, mean, median, average.   
![image](https://github.com/nogibjj/IDS706_Mini_PJT_3/assets/141780408/1ba51b75-8e19-401f-942a-d5a1d2329b15)


## Data Visualization (Histogram of Calories of Cereals)  
It used Pandas plot histogram function with matplotlib library and represents calories distribution. 
![image](https://github.com/nogibjj/IDS706_Mini_PJT_3/assets/141780408/d9fd47d9-2551-4545-81fc-c1a6df478f1a)

