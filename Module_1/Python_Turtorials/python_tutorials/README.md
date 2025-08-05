# How-to Guide

## Basic Scripts
We will walk you through all 
the Python basics, from basic data structures to `if else`, `for loop`, and programming with input arguments.

```bash
python argument_parser.py
```

## House Price Prediction

This is a `.ipynb` file called a Jupyer notebook. To open this, please activate the conda environment first by typing the following command:

```bash
# Create a first environment named `test`
# with Python 3.10 
conda create -n test python=3.9
# Activate the environment
conda activate test
# Now you are in the test environment, 
# you will install all the dependencies as follows
pip install -r requirements.txt
# Then open you Jupyter notebook by typing the following command
jupyter lab
# Then execute the notebook as in the lectures
```

The purpose of this notebook is to walk you through the most important steps of a Data Science workflow, from `EDA` to `Preprocess Data` to `training` and `evaluation`. You will need other steps to make your workflow more robust, but it will be on the module 3. For now, just keep it simple :).

## Linear Regression
This is another Jupyter notebook to code Linear Regression algorithm from scratch instead of using the available `clf.fit` from `sklearn` library. 