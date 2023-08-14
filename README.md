
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

> *Note*: conda is probably a bit to heavy to run on a raspberry pi zero, I suggest using anything that is built in when using SBC's.

1. Follow the directions in steps 2 - 5
2. `virtualenv pyvesc_flask`
3. `source pyvesc_flask/bin/activate`
4. `pip install -r requirements.txt`
5. `python app.py`

---

### Libraries/Projects used to make this

1. [Flask](https://flask.palletsprojects.com/en/2.3.x/)
2. [pyserial](https://github.com/pyserial/pyserial)
3. [PyVESC](https://github.com/LiamBindle/PyVESC)
4. [MVP.css](https://andybrewer.github.io/mvp/)
