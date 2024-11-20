# ML Framework Example Repository

This repository demonstrates a modular and reproducible framework for machine learning workflows. It includes examples, utility functions, and tests to support data exploration, model development, and testing.

Directory Structure

```
.
├── examples/                     # Example scripts showcasing framework usage
├── notebooks/                    # Jupyter notebooks for experimentation
│   └── example_notebook.ipynb    # Toy example notebook
├── tests/                        # Unit tests for utility functions
│   └── test_math_ops.py          # Simple tests for math operations
├── utils/                        # Utility functions and helpers
│   └── math_ops.py               # Basic math operations
├── requirements.txt              # Python dependencies
├── lefthook.yml                  # Git hooks for linting and testing
├── setup.sh                      # Script to install and configure Lefthook
└── README.md                     # Project overview and instructions
```


## Features

1. Jupyter Notebooks
The notebooks/ directory contains examples for data exploration, transformation, and modeling.
Example: example_notebook.ipynb demonstrates basic math operations and data transformations.

2. Utility Functions
Reusable utilities are located in the utils/ directory.
Current utilities include:
add: Adds two numbers or lists element-wise.
multiply: Multiplies two numbers or lists element-wise.

3. Testing
Unit tests are located in the tests/ directory and ensure code reliability.
Example tests:
test_math_ops.py: Tests for add and multiply functions.

4. Git Hooks
Configured with Lefthook to automate linting and testing before commits and pushes.
Linting: Ensures code style with Black and nbqa.
Testing: Runs unit tests with pytest.

5. CI/CD Pipeline
A GitHub Actions workflow runs linting and testing on every push or pull request.
Includes:
Black and nbqa for linting and formatting.
pytest with pytest-cov for testing and coverage reporting.


# Getting Started

Prerequisites

Virtual environment (Anaconda, virtualenv, pipenv, etc)
Git

1. Clone the Repository

`git clone git@github.com:dtsukiyama/centralized-notebook-repository.git`

`cd centralized-notebook-repository`


2. Install Dependencies

Example:

```python
conda create --name myenv python=3.10
conda activate myenv
pip install -r requirements.txt
```

3. Set Up Lefthook
Run the provided script to install and configure Lefthook:

Run: `./setup.sh`

4. Run the Example Notebook
Launch Jupyter Notebook and open notebooks/example_notebook.ipynb:


5. Run Tests
Execute the tests to validate the utility functions:

`pytest --cov=utils tests/`

6. pre-commit hooks


# Contributing

Create a new branch:

`git checkout -b feature/your-feature-name`

Make your changes and commit:

`git commit -m "Add your feature"`

Push to your branch:

`git push origin feature/your-feature-name`

Submit a pull request.
