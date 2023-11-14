#include "Communication.h"

const int throttleLeft = A0;
const int throttleRight = A1;

Communication communication;

void setup() {
  Serial.begin(9600);
  communication.registerUint10();
  communication.registerUint10();
}

void loop() {
  int data[2] = {
    analogRead(throttleLeft),
    analogRead(throttleRight)
  };
  communication.write(data);
  delay(10);
}
