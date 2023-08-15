
from flask_socketio import SocketIO, emit
import eventlet

from flask import Flask, render_template, request, jsonify
import pyvesc
import serial

app = Flask(__name__)
socketio = SocketIO(app)

serialport = 'COM3'  # Placeholder. Update this with your VESC's serial port

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/get_values', methods=['GET', 'POST'])
def get_values():
    if request.method == 'POST':
        method_name = request.form.get('method_name')
        with serial.Serial(serialport, baudrate=115200, timeout=0.05) as ser:
            ser.write(pyvesc.encode_request(pyvesc.GetValues))
            if ser.in_waiting > 61:
                (response, consumed) = pyvesc.decode(ser.read(61))
                data_map = {
                    "get_rpm": response.rpm,
                    "get_current": response.current_motor,
                    "get_duty_cycle": response.duty_cycle,
                    "get_voltage": response.v_in
                    # You can extend this map for more fields as needed
                }
                return jsonify({'value': data_map.get(method_name, 'Unknown method or no response')})
    
    return render_template('get_values.html')

@app.route('/set_parameters', methods=['GET', 'POST'])
def set_parameters_route():
    if request.method == 'POST':
        set_rpm_value = request.form.get('set_rpm')
        # Set the ERPM of the VESC motor (Example for set_rpm)
        with serial.Serial(serialport, baudrate=115200, timeout=0.05) as ser:
            ser.write(pyvesc.encode(pyvesc.SetRPM(int(set_rpm_value))))
        return jsonify({'message': 'Parameters set successfully!'})
    
    return render_template('set_parameters.html')

def vesc_data_thread():
    while True:
        with serial.Serial(serialport, baudrate=115200, timeout=0.05) as ser:
            ser.write(pyvesc.encode_request(pyvesc.GetValues))
            if ser.in_waiting > 61:
                (response, consumed) = pyvesc.decode(ser.read(61))
                data_map = {
                    "get_rpm": response.rpm,
                    "get_current": response.current_motor,
                    "get_duty_cycle": response.duty_cycle,
                    "get_voltage": response.v_in
                }
                socketio.emit('vesc_data', data_map)
        eventlet.sleep(1)  # Read data every second

@socketio.event
def connect():
    print('Client connected')
    global thread
    if not thread.is_alive():
        thread = socketio.start_background_task(vesc_data_thread)

@socketio.event
def disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


