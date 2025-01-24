import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def plot_numerical_features_histograms(df, log_file=None):

  if log_file:
    logging.basicConfig(filename=log_file, level=logging.INFO) 

  numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
  logging.info(f"Selected numerical features: {numerical_columns}")

  plt.figure(figsize=(15, 20))  # Set figure size explicitly
  df[numerical_columns].hist(bins=30)
  plt.suptitle('Distribution of Numerical Features')
  plt.show()
  logging.info("Histograms plotted successfully.")

def plot_correlation_heatmap(df, log_file=None):
    if log_file: 
       logging.basicConfig(filename=log_file, level=logging.INFO)

    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    logging.info(f"Selected numerical features: {numerical_columns}")

    corr_matrix = df[numerical_columns].corr()
    logging.info("Correlation matrix computed.")

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()
    logging.info("Correlation heatmap plotted successfully.")

def plot_numerical_features_boxplots(df, log_file=None):

  if log_file:
    logging.basicConfig(filename=log_file, level=logging.INFO)

  numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
  logging.info(f"Selected numerical features: {numerical_columns}")

  n_plots = len(numerical_columns)
  rows, cols = 3, 3  # Adjust rows and cols based on number of features
  fig, axes = plt.subplots(rows, cols, figsize=(15, 10))  # Set figure size explicitly

  for i, col in enumerate(numerical_columns):
    ax = axes.flat[i]
    sns.boxplot(ax=ax, y=df[col])
    ax.set_title(col)
    ax.set_xlabel('')  # Remove x-axis label for better layout

  fig.tight_layout()
  plt.show()
  logging.info("Boxplots plotted successfully.")    
