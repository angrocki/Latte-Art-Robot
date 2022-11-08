#include <Stepper.h>
//#include "A4899.h"

#define MOTOR_STEPS 200


// X Stepper Motor Pins
//const int stepX = 2;
//const int dirX = 5;
const int stepX = 24;
const int dirX = 30;

// Y Stepper Motor Pins
const int stepY = 3;
const int dirY = 6;

// Z Stepper Motor Pins
const int stepZ = 4;
const int dirZ = 7;
//const int limitZ = 11;

// init variables for loop
int steps = 1;
int value = 0;
int limit_snip = 0;
int counter = 0;
String limitt;
int x;

// 200 steps per revolution for our stepper motor type
Stepper motorX(200, stepX, dirX);
Stepper motorY(200, stepY, dirY);
Stepper motorZ(200, stepZ, dirZ);

void setup() {
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  
  pinMode(stepY, OUTPUT);
  pinMode(dirY, OUTPUT);
  
  pinMode(stepZ, OUTPUT);
  pinMode(dirZ, OUTPUT);
  
//  pinMode(limitZ, INPUT);
//  pinMode(LED_BUILTIN, OUTPUT); // for testing 

  Serial.begin(115200);
  motorX.setSpeed(20);
  motorZ.setSpeed(20);
  motorY.setSpeed(20);  // speed 20
}

void loop() {

  digitalWrite(dirY, HIGH);
  digitalWrite(dirX, HIGH);
  digitalWrite(dirZ, HIGH);
  motorY.step(1);

//  while (steps == 1) {
//    for (x=0; x < 200; x++) {
//          motorX.step(1);
//    }
//    for (x=0; x < 200; x++) {
//          motorY.step(1);
//    }
//    for (x=0; x < 200; x++) {
//          motorZ.step(1);
//    }
//    steps++;
    // read the limit switch 
//  }

}

//  int limit = digitalRead(limitZ);
//  Serial.println(limit);

  // while limit is off { move steppers all way to the left} 
  // move steppers to the right by two inches 
//  while (steps == 1) {
//
//    // continue moving to the left 
////    digitalWrite(dirY, HIGH);
//    for (x=0; x < 30; x++) {
//          motorX.step(1);
//    }
//    for (x=0; x < 30; x++) {
//          motorY.step(1);
//    }
//    for (x=0; x < 30; x++) {
//          motorZ.step(1);
//    }
//    steps++;
//    // read the limit switch 
//  }

    // track the print of limit switch 
  //  limitt += String(limit);
  //  int change = limitt.indexOf("0000000");
//    Serial.println(change);

    // if limit switch is activated, change directions 
//    if ((change)>-1) {
////        Serial.println(limit);
//        digitalWrite(dirY, LOW);
//
//        for (x=0; x < 800; x++){
//          motorY.step(1);
//        }
//        steps += 1;
//        Serial.write("FKJLASDFJ ALSKDF JALSKDFJ SLAJF ALSK ");
//    }
 // }

  

//  if (Serial.available()) {
//    int steps = Serial.parseInt();
//    Serial.print(steps);
//    
//  }
//  motorZ.step(steps);
//  while (steps == 1) {
//    motorY.step(400);
//    steps += 1;
//  }
//  motorY.step(1);
//
//  value++;
//  Serial.println(value);
  
//  int limit = digitalRead(limitZ);
//  Serial.println(limit);
//
//  if (limit == LOW) {
//      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//                    // wait for a second 
//  }
//    if (limit == HIGH) {
//      digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
//                    // wait for a second
