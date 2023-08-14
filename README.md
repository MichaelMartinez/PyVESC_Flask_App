
# PyVESC Flask App

This is a Flask web application to interact with VESC using the PyVESC library.

## Setup and Run

1. Install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) if you haven't already.
2. Clone this repository and navigate to its root directory.
3. Update the `serialport` variable in `app.py` to match your VESC's actual serial port.
4. Manually download [MVP.css](https://andybrewer.github.io/mvp/mvp.css) and place it in the `static` directory of the project.
5. Create a new Conda environment:
   ```
   conda create --name pyvesc_flask_app python=3.8
   ```
6. Activate the Conda environment:
   ```
   conda activate pyvesc_flask_app
   ```
7. Install required packages:
   ```
   pip install -r requirements.txt
   ```
8. Run the Flask app:
   ```
   python app.py
   ```

Now, open your web browser and navigate to `http://127.0.0.1:5000/` to access the app.
