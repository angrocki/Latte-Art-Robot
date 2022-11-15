//------------------------------------------------------------------------------
// 4 LED G-Code Demo
// Goal: Test G-code structure with LED and Serial Communication with Python
// Created 11/05/2022
//------------------------------------------------------------------------------
#include <Arduino.h>
//------------------------------------------------------------------------------
// CONSTANTS
//------------------------------------------------------------------------------
#define BAUD                 (115200)                 // How fast Ardunio is talking
#define MAX_BUF               (64)                     // What is the longest message Arduino can store?
//------------------------------------------------------------------------------
// GLOBALS
//------------------------------------------------------------------------------

char buffer[MAX_BUF];  // where we store the message until we get a ';'
int sofar;  // how much is in the buffer
char mode_abs=1;  // absolute mode?
int motor_speed = 1;   
float stepmm = 9.375;
long line_number=0;
const uint8_t BLUE = 13; // BLUE is connected to D13
const uint8_t RED = 12; // RED is connected to D12
const uint8_t YELLOW = 11; // YELLOW is connected to D11
const uint8_t GREEN = 10; // GREEN is connected to D10

//------------------------------------------------------------------------------
// STRUCTS
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
// METHODS
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
// Processing G-Code
//------------------------------------------------------------------------------
// INITIALIZING MOTOR PINS 

#define MOTOR_STEPS 200
#define MICROSTEPS 16
#define RPM 120

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

#include "A4988.h"        // drivers type 
#define MS1 10
#define MS2 11
#define MS3 12

// STEPPER MOTOR OBJECTS
A4988 X(MOTOR_STEPS, X_DIR_PIN, X_STEP_PIN, X_ENABLE_PIN, MS1, MS2, MS3);
A4988 Y(MOTOR_STEPS, Y_DIR_PIN, Y_STEP_PIN, Y_ENABLE_PIN, MS1, MS2, MS3);
//------------------------------------------------------------------------------


void Motor_setup() {
  X.begin(RPM, MICROSTEPS);
  Y.begin(RPM, MICROSTEPS);

  X.setEnableActiveState(LOW);
  Y.setEnableActiveState(LOW);

  X.enable();
  Y.enable();
}



/**
 * prepares the input buffer to receive a new message and tells the serial connected device it is ready for more.
 */
void ready() {
  sofar=0;  // clear input buffer
  Serial.print(F(">"));  // signal ready to receive input
}

/**
 * Read the input buffer and find any recognized commands.  One G or M command per line.
 */
void processCommand() {
  int cmd = parseNumber('M',-1);
  switch(cmd) {
  case  1:  one_revX();  break;
  case  2:  one_revY(); break;
  case 3: move_X(parseNumber('X',0)); break;
  case 4: move_Y(parseNumber('Y', 0)); break;
  case  100:  help(); break;
  default:  break;
  }
}

/**
 * Look for character /code/ in the buffer and read the float that immediately follows it.
 * @return the value found.  If nothing is found, /val/ is returned.
 * @input code the character to look for.
 * @input val the return value if /code/ is not found.
 **/

float parseNumber(char code,float val) {
  char *ptr=buffer;  // start at the beginning of buffer
  while((long)ptr > 1 && (*ptr) && (long)ptr < (long)buffer+sofar) {  // walk to the end
    if(*ptr==code) {  // if you find code on your walk,
      return atof(ptr+1);  // convert the digits that follow into a float and return it
    }
    ptr=strchr(ptr,' ')+1;  // take a step from here to the letter after the next space
  }
  return val;  // end reached, nothing found, return default val.
}

/**
 * write a string followed by a float to the serial line.  Convenient for debugging.
 * @input code the string.
 * @input val the float.
 */


void output(char *code,float val) {
  Serial.print(code);
  Serial.print(val);
  Serial.print(" ");
}

//------------------------------------------------------------------------------
// G-Code Commands
//------------------------------------------------------------------------------

void pause(int S){
  delay(S);
}
void move_X( int x){
  X.rotate(x * stepmm);
}

void move_Y( int y){
  Y.rotate(y * stepmm);
}
void one_revX(){
  X.rotate(360);
}

void one_revY(){
  Serial.print("Move");
  Y.rotate(360);
  Serial.print("moved");
}



void blink_speed(int S){
  motor_speed = S;
}

/**
 * display helpful information
 */
void help() {
  Serial.print(F("Gcode LED DEMO "));
  Serial.println(F("Commands:"));
  Serial.println(F("M1; - one rev X"));
  Serial.println(F("M2; - one rev Y"));
  Serial.println(F("M3 X[]; - Move X steps X "));
  Serial.println(F("M4 Y[]; - Move Y steps Y"));
  Serial.println(F("M100; - this help message"));

}

//------------------------------------------------------------------------------
// Main Body
//------------------------------------------------------------------------------

void setup() {
//  LED_setup();
  Motor_setup();
  Serial.begin(BAUD);
  help();
  ready();
}

void loop() {
  // listen to serial commands
  while(Serial.available() > 0){
    char c = Serial.read(); 
    Serial.print(c); // Know that we got the message 
    if(sofar < (MAX_BUF-1)){
      buffer[sofar++]=c;
    }
    if(c=='\n') {
      // entire message received
      buffer[sofar]=0;  // end the buffer so string functions work right
      Serial.print(F("\r\n"));  // echo a return character for humans
      processCommand();  // do something with the command
      ready();
    }
    
  }

}
