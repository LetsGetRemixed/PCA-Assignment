[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/VgGk4WR1)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12431398)
# CS 4337 - Assignment 7 - PCA

To complete this assignment you will need to implement the following functions:
- `get_eigenvectors()` - Task 1
- `pca_detect_digit()` - Task 2

Read the detailed assignment description on Canvas for more information about the functions.

## File list
- `README.md` - This file
- `.gitignore`: This file tells git which files to ignore.
- `get_eigenvectors.py`: This file contains the function `get_eigenvectors()` that you need to implement.
- `pca_detect_digit.py`: This file contains the function `pca_detect_digit()` that you need to implement.
- `main.py`: This file contains the code that you can use to test your functions.
- `requirements.txt`: This file contains the list of Python packages required to run the code in this repository.
- `data/` - Directory containing the digits dataset for computing the eigenvectors and images to test your functions on.
- `tests/` - Directory containing the unit tests for your functions.
- `output/` - Directory where the test output images will be saved.
- `.github/workflows`: This folder contains the GitHub Actions workflow file that is used to run the unit tests on every commit.

## Setting up the environment

If you are running the code on your own machine, and you followed the tutorial posted on Canvas for setting up your environment for running computer vision applications, your environment should be ready to run the code. If you use Github Codespaces the environment will need to be set up by installing the packages listed in the `requirements.txt` file. You can do this by running the following command in the terminal:

```bash
pip install -r requirements.txt
```

**Note:** If on Github Codespaces, after installing the required packages, you get the error `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`, you will need to run the following command in the terminal:

```bash
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx
```

## Running the code

You can modify the `main.py` file to test your functions. You can run your code using the following command:

```bash
python main.py
```
## Running the tests

To run the unit tests, you will need to run the following command:

```bash
pytest
```

