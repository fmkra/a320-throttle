#ifndef __A320_THROTTLE_Communication_h
#define __A320_THROTTLE_Communication_h

#include <Arduino.h>

class Communication {
  String schema;

  void writeData(byte value);
  void writeUint10(int value);

  public:
  void write(int data[]);

  void registerUint10();
  void printSchema();
};

#endif
