#include "Communication.h"

const int throttleLeft = A0;
const int throttleRight = A1;

Communication communication;

void setup() {
  Serial.begin(9600);
  communication.registerUint10();
  communication.registerUint10();

  communication.printSchema();
}

void loop() {
  Serial.println("=========");
  int data[2] = {
    analogRead(throttleLeft),
    analogRead(throttleRight)
  };
  communication.write(data);
}
