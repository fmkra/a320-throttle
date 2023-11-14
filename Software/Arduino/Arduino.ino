void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available()) {
    String data = Serial.readString();
    data.trim();
    if(data == "LED_ON") {
      digitalWrite(13, HIGH);
    } else if(data == "LED_OFF") {
      digitalWrite(13, LOW);
    } else {
      Serial.print("Unknown command ");
      Serial.println(data);
    }
  }
}
