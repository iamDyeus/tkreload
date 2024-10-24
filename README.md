<div align="center">

<!-- # `tkreload` -->
![TkReload-Logo](https://github.com/iamDyeus/tkreload/blob/main/.assets/logo/svg/logo_light.svg?raw=true)

![Static Badge](https://img.shields.io/badge/pip_install-tkreload-purple)
<br />
![Static Badge](https://img.shields.io/badge/Language-Python-red)
![GitHub last commit](https://img.shields.io/github/last-commit/iamDyeus/tkreload)

<p class="align center">
<h4><code>tkreload</code> is an open-source tool for automatically reloading terminal-based Python applications, saving developers valuable time.</h4>
</p>

[Installation](#installation) •
[Usage](#usage) •
[Contributing](#contributing) •
[Testing](#testing) •
[License](#license)

</div>

# Problem Statement
Developers often lose significant time manually restarting terminal applications during development. This process can be tedious and time-consuming, especially when working on complex projects that require frequent updates and testing.

# Time-Saving Analysis
Let’s assume that a developer restarts their terminal application approximately 15 times per day, and each reload takes 30 seconds. This adds up to 7.5 minutes daily or around 3.12 hours per month. Multiply that by the number of developers working on a project, and you quickly see how terminal reloading becomes a significant bottleneck in development productivity.

# Solution: tkreload
tkreload solves this issue by providing an automatic reload mechanism for terminal-based Python applications, particularly those using Tkinter. It eliminates the need for manual restarts, saving developers hours of time and streamlining the debugging process.

## Without tkreload
![Without tkreload](https://github.com/iamDyeus/tkreload/blob/main/.assets/without.gif?raw=true)

## With tkreload
![With tkreload](https://github.com/iamDyeus/tkreload/blob/main/.assets/with.gif?raw=true)

# Getting Started

## Prerequisites
- Python 3.9+
- pip

## Installation

1. Clone the repository:
```sh
git clone https://github.com/iamDyeus/tkreload.git
cd tkreload
```

2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

4. Install tkreload:
```sh
pip install .
```

# Usage

To run the app with `tkreload`, use the following command in your terminal:

```bash
tkreload your_app.py
```

Now, whenever you save changes to your script, tkreload will automatically reload your application.

## Testing
Ensuring the functionality and reliability of tkreload is crucial. Follow these steps to run the test suite for the project:
1. Install Testing Dependencies
Before running the tests, install the required dependencies (e.g., pytest). You can do this by installing the packages listed in the requirements.txt file.
2. Running Tests
Navigate to the root directory of the project (`tkreload`) and run the tests using `pytest` with the following command:
```bash
pytest .
```

# Contributing

Contributions are welcome and greatly appreciated! Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

![COMMUNISM](https://github.com/iamDyeus/tkreload/blob/main/.assets/communism.png?raw=true)

# License

Distributed under the Apache-2.0 License. See [`LICENSE`](LICENSE) for more information.

# Acknowledgments
- Inspired by the need for efficient development workflows
- Thanks to all contributors and supporters of this project

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=iamDyeus/tkreload&type=Date)](https://star-history.com/#iamDyeus/tkreload&Date)
