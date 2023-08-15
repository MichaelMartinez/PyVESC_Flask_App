
# PyVESC Flask App

This is a Flask web application to interact with VESC using the PyVESC library.

## Setup and Run

1. Install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if you haven't already.
2. Clone this repository and navigate to its root directory.
3. If you do not want to use serial communication, comment out `pyserial` in `requirements.txt`
4. Update the `serialport` variable in `app.py` to match your VESC's actual serial port.
5. Manually download [MVP.css](https://andybrewer.github.io/mvp/mvp.css) and place it in the `static` directory of the project... Or simply use `<link rel="stylesheet" href="https://unpkg.com/mvp.css">`
6. Create a new Conda environment:

   ```shell
   conda create --name pyvesc_flask python=3.10
   ```

7. Activate the Conda environment:

   ```shell
   conda activate pyvesc_flask
   ```

8. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

9. Run the Flask app:

   ```shell
   python app.py
   ```

Now, open your web browser and navigate to `http://127.0.0.1:5000/` to access the app.

---

## Setup and Run on Raspberry Pi

> *Note:* conda DOES NOT work with Raspberry Pi zero.

We need to install a virtual environment manager:

```shell
pip3 install virtualenv virtualenvwrapper
nano ~/.bashrc
```

Append the following lines to the bottom of the file:

```shell
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin
```

> *Note:* that if you use an older version of Raspbian, virtualenvwrapper is installed in /usr/local/bin/ instead so change lines 4 and 5 above accordingly.

Now reload `.bashrc`:

```shell
source ~/.bashrc
```

Now create a virtualenv

```shell
mkvirtualenv pyvesc_flask
workon pyvesc_flask
```

When you are done, simply type:

```shell
deactivate
```

---

### Libraries/Projects used to make this

1. [Flask](https://flask.palletsprojects.com/en/2.3.x/)
2. [pyserial](https://github.com/pyserial/pyserial)
3. [PyVESC](https://github.com/LiamBindle/PyVESC)
4. [MVP.css](https://andybrewer.github.io/mvp/)
