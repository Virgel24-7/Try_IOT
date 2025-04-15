void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();
    if (received == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (received == '0') {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
