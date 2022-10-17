# Technical Analysis

if you want to read this same document but in [Spanish](https://github.com/yeriel/technical_analysis/blob/main/Spanish.md)

## Context
Work performed in this repository corresponds to a technical test for the company Comunidad Feliz. The test is designed to perform an analysis of a set of available products, retrieving information from an endpoint designed for this test.

## Getting Started
To run the code present in this repository you must clone the repository and install the required dependencies as follows
``` 
git clone https://github.com/yeriel/technical_analysis.git
cd technical_analysis
pip install -r requirements.txt
```
## Repository structure
This repository is structured in two parts in the scripts that allow the extraction of the information from the endpoit prepared for this test and in the data analysis.

### Information extraction
To perform the extraction of information, the files extract_clients.py and extract_sales.py must be executed using Python by means of the command

```
python extract_clients.py 
python extract_sales.py
```

### Analysis
The data analysis was performed using jupyter notebook for them you must run your conda environment or your virtual environment of choice and execute the following command

```
jupyter notebook analysis.ipynb
```

