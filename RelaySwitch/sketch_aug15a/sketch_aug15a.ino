const int buttonPin = 7;  // Button connected to D7
const int relayPin = 6;   // Relay connected to D6
const int ledWarning = 4;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(relayPin, OUTPUT);
  pinMode(ledWarning, OUTPUT);
  digitalWrite(ledWarning, LOW);
  digitalWrite(relayPin, LOW);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  if (buttonState == LOW) {
    digitalWrite(relayPin, HIGH);
    digitalWrite(ledWarning,HIGH);
  } else {
    digitalWrite(relayPin, LOW);
    digitalWrite(ledWarning,LOW);
  }
}
