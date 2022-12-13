#include <Arduino.h>
#include "MultiDriver.h"

int MOTOR_STEPS = 200;
#define X_STEP_PIN         A0
#define X_DIR_PIN          A1
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN          -1 //PIN 2 is used

#define Y_STEP_PIN         A6
#define Y_DIR_PIN          A7
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          -1 //PIN 15 is used

#define E1_STEP_PIN        36
#define E1_DIR_PIN         34
#define E1_ENABLE_PIN      30

#include "A4988.h"        // drivers type 
#define MS1 10
#define MS2 11
#define MS3 12

// STEPPER MOTOR OBJECTS
A4988 X(MOTOR_STEPS, X_DIR_PIN, X_STEP_PIN, X_ENABLE_PIN, MS1, MS2, MS3);
A4988 Y_1(MOTOR_STEPS, Y_DIR_PIN, Y_STEP_PIN, Y_ENABLE_PIN, MS1, MS2, MS3);
A4988 Y_2(MOTOR_STEPS, E1_DIR_PIN, E1_STEP_PIN, E1_ENABLE_PIN, MS1, MS2, MS3);
//A4988 Z(MOTOR_STEPS, Z_DIR_PIN, Z_STEP_PIN, Z_ENABLE_PIN, MS1, MS2, MS3);
//A4988 T(MOTOR_STEPS, E0_DIR_PIN, E0_STEP_PIN, E0_ENABLE_PIN, MS1, MS2, MS3);

MultiDriver controller(X, Y_1, Y_2);

int steps = 0;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  X.begin(40, 16);
  Y_1.begin(20,16);
  Y_2.begin(20,16);

  X.setEnableActiveState(LOW);
  Y_1.setEnableActiveState(LOW);
  Y_2.setEnableActiveState(LOW);

  X.enable();
  Y_1.enable();
  Y_2.enable();
}





void loop() {
  // put your main code here, to run repeatedly:
  int deg = 1*9.375;
  controller.rotate(0,deg,deg,0,0);
  steps++;
  Serial.println(steps);
  delay(1000);
}
