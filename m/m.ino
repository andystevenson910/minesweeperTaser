const int ledPin = 12;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600); // Initialize serial communication at 9600 bps
}

void loop() {
  if (Serial.available() > 0) {  // Check if there's incoming data
    char inChar = Serial.read(); // Read a character from the serial port
    if (inChar == '1') {         // If the character is '1'
      digitalWrite(ledPin, HIGH); // Turn the LED on
      delay(50);                 // Wait for 0.5 seconds
      digitalWrite(ledPin, LOW);  // Turn the LED off
    }
  }
}
