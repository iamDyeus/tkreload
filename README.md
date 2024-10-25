<div align="center">

# ![TkReload-Logo](https://github.com/iamDyeus/tkreload/blob/main/.assets/logo/svg/logo_light.svg?raw=true)

![Static Badge](https://img.shields.io/badge/pip_install-tkreload-purple)
![Static Badge](https://img.shields.io/badge/Language-Python-red)
![GitHub last commit](https://img.shields.io/github/last-commit/iamDyeus/tkreload)

<h3>
<code>tkreload</code> | Automated Tkinter App Reloading for a Smoother Development Workflow
</h3>

<p align="center">
Effortlessly reload Tkinter-based Python applications in the terminal, saving valuable development time.
</p>

[Installation](#installation) • [Usage](#usage) • [Features](#features) • [Testing](#testing) • [Contributing](#contributing) • [License](#license)

</div>

---

## 🚀 Problem Statement

For developers, frequent manual restarts of terminal applications during development can add up quickly, especially in complex Tkinter projects that require regular updates. `tkreload` provides a solution to this by automating the reload process, resulting in significant time savings.

### ⏳ Estimated Time Saved with tkreload

Imagine restarting your terminal application **15 times daily**, with each reload taking **30 seconds**. That’s approximately **7.5 minutes daily** or about **3 hours per month**. `tkreload` helps avoid this productivity drain.

---

## 🔍 Solution Overview

`tkreload` automates reloading for terminal-based Python applications, designed specifically for **Tkinter**. By eliminating the need for manual restarts, it streamlines the development process, saving developers valuable time and enhancing productivity.

**Without tkreload:**
![Without tkreload](https://github.com/iamDyeus/tkreload/blob/main/.assets/without.gif?raw=true)

**With tkreload:**
![With tkreload](https://github.com/iamDyeus/tkreload/blob/main/.assets/with.gif?raw=true)

---

## 🛠️ Getting Started

### Prerequisites
- **Python** 3.9+
- **pip** for dependency management

### Installation

#### 1. Clone the Repository
```sh
git clone https://github.com/iamDyeus/tkreload.git
cd tkreload
```
#### 2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install tkreload (in editable mode):
```sh
pip install -e.[test]
```

# Usage

To run the app with `tkreload`, use the following command in your terminal:

```bash
tkreload your_app.py
```

Now, whenever you save changes to your script, tkreload will automatically reload your application.

## 🌟 Features

- **Automatic Reloading:** Automatically restarts Tkinter apps upon file changes.
- **Command-Based Control:**
  - **`H`:** View help commands
  - **`R`:** Restart the application
  - **`A`:** Toggle auto-reload
  - **`Ctrl + C`:** Exit the application
- **Real-Time Feedback:** Uses `rich` for styled console feedback and progress indicators.



## Testing
To verify tkreload functionality, follow these steps:

1.Install Testing Dependencies: Make sure all testing libraries are installed as per the requirements.txt file.

2.Run Tests Using Pytest
```bash
pytest -v
```
This will run the test suite and confirm tkreload is working as expected.

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
