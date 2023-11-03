from http.server import BaseHTTPRequestHandler, HTTPServer
import serial

PORT_NUMBER = 8080  # Port for the HTTP server
SERIAL_PORT = '/dev/ttyUSB0'  # Your Arduino's serial port
ser = serial.Serial(SERIAL_PORT, 9600)  # Open the serial connection


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        # Set headers for CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send signal to the Arduino
        self.send_signal_to_arduino()

        # Send a response to the browser
        self.wfile.write(b"Signal sent to Arduino!")
        return

    @staticmethod
    def send_signal_to_arduino():
        ser.write(b'1')


if __name__ == '__main__':
    try:
        print(f'Started http server on port {PORT_NUMBER}')
        server = HTTPServer(('', PORT_NUMBER), RequestHandler)
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        ser.close()  # Close the serial connection when server is stopped
        server.socket.close()
