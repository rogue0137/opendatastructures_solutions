
### CHAPTER 1

_Steps to get this code to work_

1. Ensure that Python3 is installed

2. Create the virtual environment

```python3 -m venv data_structures```

3. Activate the virtual environment

```source data_structures/bin/activate```

4. Install necessary packages

```pip install ```

5. Call the file using the full file path. EX:

```python3 /Users/krystalflores/github/general/data_structures/classifying_iris_species.py```

6. Produce a beautifully colored output file. EX:

![Scatterplot: Chapter 1](/images/section_intromachinelearning_chapt1.jpg)

### CHAPTER 2

1. Activate the virtual environment previously created

```source data_structures/bin/activate```

_Synthetic two-classification dataset_

```python3 /Users/krystalflores/github/general/data_structures/forge_dataset.py```

_Synthetic regression dataset_

```python3 /Users/krystalflores/github/general/data_structures/wave_dataset.py```

_Real two-classification Wisconsin Breast Cancer Dataset_

```python3 /Users/krystalflores/github/general/data_structures/cancer_dataset.py```

_Real regression Boston Housing Dataset_

```python3 /Users/krystalflores/github/general/data_structures/boston_housing_dataset.py```


_k-NN "Nearest Neighbors"_

There are multiple exercise in the chapter. I have grouped them into:
- 1-NN
- 3-NN
- forge
- cancer

In order to call a specific exercise, you must supply it as an argument.

```python3 /Users/krystalflores/github/general/data_structures/k-NN_algorithm.py <<EXERCISE>> ```

Example:

```python3 /Users/krystalflores/github/general/data_structures/k-NN_algorithm.py "cancer"```




