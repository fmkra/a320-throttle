#include "Communication.h"
#include <Arduino.h>

void Communication::registerUint10() {
  schema += (char)10;
}

void Communication::printSchema() {
  for(const char* p = schema.c_str(); *p; p++) {
    Serial.println(*p);
  }
}

void Communication::writeUint10(int value) {
  byte low5 = value & 0x1f;
  byte high5 = (value >> 5) & 0x1f;
  writeData(low5);
  writeData(high5);
}

void Communication::writeData(byte value) { // value has to be 7 bit
  Serial.write(value & 0x80);
}

void Communication::write(int data[]) {
  for(unsigned int i = 0; i < schema.length(); i++) {
    switch(schema[i]) {
      case '\0':
        Serial.write(0);
        return;
      case 10:
        writeUint10(data[i]);
        break;
    }  
  }
}

