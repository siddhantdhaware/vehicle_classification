# Vehicle Classification

## CM3070 Computer Science Final Project

## BSc Computer Science - University of London

## Siddhant Dhaware (190305701)

------

### Project Description

This is a deep learning project that uses convolutional neural networks and the TensorFlow and Keras libraries to achieve the project objectives.

More specifically it is a multiclass single-label image classification project, which aims to accurately classify vehicles images based on their type.

The key objective is to create a small model that can rival larger models and various types of state-of-the-art models in terms of test accuracies. The main metric along with model accuracy, is the model size.

### Ensure the following libraries are installed before starting, or use the commands below to install them:

|    | Library        | Command to install              |
|----|----------------|---------------------------------|
| 1. | TensorFlow:    | ``` pip install tensorflow```   |
| 2. | Matplotlib:    | ``` pip install matplotlib```   |
| 3. | split-folders: | ``` pip install splitfolders``` |
| 4. | OpenCV:        | ``` pip install cv2 ```         |

> While these commands should run directly on most systems, instructions of installing the above packages may differ for different operating system environments. Kindly ensure the above four libraries are installed and working before proceeding.

### Datasets and Methodology

**Primary/Main dataset:** [https://zenodo.org/record/6634554](https://zenodo.org/record/6634554)

**Secondary dataset (only used for the transfer learning notebook):** [https://data.mendeley.com/datasets/htsngg9tpc](https://data.mendeley.com/datasets/htsngg9tpc)

The `datasets/dataset_sources.md` contains detailed information about both the datasets.

The `1_methodology_getDS.ipynb` notebook contains information about the problem, establishes the measure of success, evaluation protocol, and other parameters that will be used. It also contains a code cell which when ran, downloads the secondary dataset to the `datasets/data/raw` folder. The primary dataset is already in the repository and can be found in `datasets/data/raw`.

The `2_explore_split_datasets.ipynb` file explores the datasets and their various features, and also splits them in train, test, and validation sets.

### Deep Learning Workflow used in this project

**The six notebooks in the *notebooks/* folders run various models**:

The baseline and overfitting models can be found in the `notebooks/1_baseline_and_overfitting.ipynb` file.

In the `notebooks/2_replicate_paper.ipynb` file, I have tried to replicate a state-of-the-art model proposed by researchers.

The project then entails tuning model architectures and hyperparameters, along with experimenting with various advanced techniques like data augmentation, residuals and batch normalization, and image processing using TensorFlow. The `notebooks/3_tuning_model_parameters.ipynb` file contains a progressive history of the experimentation, and reaching the final models.

The `notebooks/4_test_final_models.ipynb` file contains the final test accuracies for the two best models.

The `notebooks/5_transfer_learning.ipynb` file details the experiment with using transfer learning, utilizing an already trained model (trained on the secondary dataset).

The `notebooks/5_transfer_learning.ipynb` file runs the state-of-the-art VGG16 model on the main dataset and gets the test accuracies.

### Results

|    | Model          | Test Accuracy |
|----|----------------|---------------|
| 1. | Proposed Model | 93.96%        |
| 2. | Best Model     | 95.83%        |

> The `helpers/plot_graphs.py` is a python script which plots training and validation accuracy and loss graphs, and it is used in all the models in the notebooks in the `notebooks/` folder.

> The `html_exports/` folder contains the **html** exports of the notebooks, and all the work can be viewed there.
