# Environmental and cultural predictors of Pacific islands deforestation 

## About

In this project I employ the methods of machine learning to build models predicting deforestation based on data from from [1] and [2]. Moreover I use various methods of estimation how individual variables contribute to the outcome, including the cutting-edge Shapley values analysis. The goal is not to reproduce the results of the mentioned papers and perform a meticulous statistical analysis but rather to see how the modern tools of data science can supplement statistical approaches of environmental science.

See the accompanying blog post: https://patryk-kubiczek.github.io/posts/pacific-deforestation/.

[1] Rolett, B. & Diamond, J. [Environmental predictors of pre-European deforestation on Pacific islands](https://www.nature.com/articles/nature02801). Nature 431, 443 (2004).

[2] Atkinson, Q. D., Coomber, T., Passmore, S., Greenhill, S. J. & Kushnick, G. [Cultural and Environmental Predictors of Pre-European Deforestation on Pacific Islands](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0156340). PLOS ONE 11, e0156340 (2016).

![Map of deforestation levels](/output/spatial-deforestation.png)

## Results

See the notebook `analyse.ipynb` in [nbviewer](https://nbviewer.jupyter.org/github/patryk-kubiczek/pacific-deforestation/blob/master/notebooks/analyse.ipynb).

## Reproducibility

1. Install the required Python modules from env.yaml. For example, if you use Anaconda:
```
conda env create --name pacific-deforestation -f env.yml
conda activate pacific-deforestation
```
2. Run the notebook `merge-data.ipynb` which calls scripts for downloading and cleaning the data, and eventually creates the final dataset.

3. Run the notebook `analysis.ipynb`. Execution of some cells may take a while.

## Acknowledgements

We acknowledge the usage of public datasets supplementing papers [1] and [2], as well the usage of a map from [Natural Earth](https://www.naturalearthdata.com/).

**Copyright (C) 2019 Patryk Kubiczek**
