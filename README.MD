# tkreload

## Introduction

### The Problem

Developers often spend a significant amount of time restarting or reloading applications, especially when working with terminal-based scripts. Each reload can add up to valuable minutes, or even hours, lost during development. Manually restarting terminal programs every time a change is made, or debugging with constant reloads, can become a major source of inefficiency.

### Time-Saving Analysis

Let’s assume that a developer restarts their terminal application approximately 15 times per day, and each reload takes 30 seconds. This adds up to 7.5 minutes daily or around 3.12 hours per month. Multiply that by the number of developers working on a project, and you quickly see how terminal reloading becomes a significant bottleneck in development productivity.

### The Solution: tkreload

**tkreload** aims to solve this issue by providing developers with an automatic reload mechanism for terminal-based Python applications. With tkreload, you no longer need to manually restart your applications, saving hours of development time and making debugging much more efficient. The tool is designed for seamless integration with Tkinter-based applications or any terminal-based Python script, ensuring smooth reloading after every code change.

---

## Installation

Follow these steps to set up and install **tkreload**:

1. **Create a Python Virtual Environment**  
   Open your terminal and run:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**

- On Windows:

```bash
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

3. **Install Dependencies**
   Inside the activated virtual environment, install the required libraries listed in requirements.txt:

```bash
cd src # if not in /src
pip install -r requirements.txt
```

4. **Install tkreload**
   Once the environment is set up and dependencies are installed, you can install the tkreload library via pip:

```bash
cd src # if not in /src
pip install .
```

---

## Running Tests

Tests are critical to ensuring that the functionality and reliability of tkreload are maintained. Here’s how you can run the test suite for the project:

### 1. Install Testing Dependencies

To run the tests, you will need to install the testing dependencies (e.g., `pytest` if it’s being used). Make sure to install the dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 2. Running Tests with `pytest`

After installing the dependencies, you can run all tests using `pytest`. From the root directory of the project, execute the following command:

```bash
pytest
```

This will automatically discover and run all tests in the `tests/` folder.

### 3. Running Tests with `unittest`

If the project is using Python's built-in `unittest` framework, you can run the tests using:

```bash
python -m unittest discover tests
```

### 4. Checking Test Coverage

To ensure the project has good test coverage, you can use the `pytest-cov` plugin. If you're using `pytest`, install the coverage package:

```bash
pip install pytest-cov
```

Then run:

```bash
pytest --cov=src
```

This will display the test coverage for the `tkreload` library.

---

## Contributing

I believe that tkreload can significantly improve developer efficiency, but I can't do it alone. So, I invite you to contribute to this project to help it reach its full potential.

---

![alt text](.github\images\COMMUNISM.png)
