# Minesweeper Monitor Project

This project connects [minesweeperonline.com](https://minesweeperonline.com) to an Arduino over serial.  
When you lose a Minesweeper game, the browser extension notifies a local Python server, which then sends a signal to the Arduino setting a stun gun off.

---

## Requirements

- Python 3.8+  
- Firefox
- Arduino board
- Modified Stun Gun Circuit
- Arduino IDE installed  

---

## Setup Instructions

### 1. Clone the repository

~~~bash
git git@github.com:andystevenson910/minesweeperTaser.git
cd minesweeperTaser
~~~

### 2. Set up Python environment

Create a virtual environment (optional but recommended):

~~~bash
python3 -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
~~~

Install dependencies:

~~~bash
pip install -r requirements.txt
~~~

Start the server:

~~~bash
python serverAndSerial.py
~~~

The server runs on [http://localhost:8080](http://localhost:8080).

---

### 3. Install the Firefox Extension

1. Open Firefox and go to `about:debugging#/runtime/this-firefox`.  
2. Click **"Load Temporary Add-on"**.  
3. Select the `manifest.json` file inside the `extension/` folder.  
   - The extension will now be loaded temporarily.  
   - To make it permanent, you’ll need to use the **signed .xpi** package.  

---

### 4. Install the Signed Add-on (.xpi) (Pending Approval)

Once we add the signed package from [addons.mozilla.org](https://addons.mozilla.org), you can install it:

- Open Firefox.  
- Drag the `.xpi` file into the browser window.  
- Confirm installation.  

---

### 5. Flash the Arduino

1. Open the Arduino IDE.  
2. Select your board and port under **Tools → Board** and **Tools → Port**.  
3. Open `arduino/arduino-sketch.ino`.  
4. Click **Upload**.  

Your Arduino is now ready to receive serial signals from the Python server.


