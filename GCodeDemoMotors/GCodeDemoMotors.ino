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
float default_speed = 10;  
float max_speed = 120; 
float stepmm = 9.375;
long line_number=0;
float feedrate = 200;
float step_delay = 0;

//------------------------------------------------------------------------------
// Postion 
//------------------------------------------------------------------------------

float px = 0 ;   //Position X
float py = 0;    //Position Y
float reset;

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
  int cmd = parseNumber('G',-1);
  switch(cmd) {
  case  1: { // line
    line( parseNumber('X',px),
          parseNumber('Y',py ));
    break;
    default:  break;
  }
    }
  cmd = parseNumber('M',-1);
  switch(cmd) {
  case  1:  one_revX();  break;
  case  2:  one_revY(); break;
  case 3: move_X(parseNumber('X',px)); break;
  case 4: move_Y(parseNumber('Y', py)); break;
  case 5: set_pos(parseNumber('X', px),
                  parseNumber('Y', py)); break;
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
/**
  * Set feedrate and step_delay based on the value entered.
  * @param: fr float representing new feedrate
  */
void set_feedrate(float fr) {
  step_delay = 1000000.0/fr;
  feedrate = fr;
}
/**
  * Using ABSOLUTE positions, move to inputted x,y coordinates.
  * This is done using Breseham's Line Algorithm.
  *
  */
void line(int newx, int newy) {

  // Find relative distance to move
  float dx = newx - px;
  float dy = newy - py;

  int x_dir;
  int y_dir; 

  // Set direction of x movement
  if (newx > px) {
    x_dir = 1;
  } else {
    x_dir = -1;
  }
  // Set direction of y movement
  if (newy > py) {
    y_dir = 1;
  } else {
    y_dir = -1;
  }

  // Implement Breseham's Algorithm
  if (dx > dy) {
    reset = dx / 2;
    for (int i = 0; i < dx; i++) {
      one_stepX(x_dir);
      reset += dy;
      if (reset >= dx) {
        reset -= dx;
        one_stepY(y_dir);
      }
      pause(step_delay);
    }
  }
  else {
    reset = dy / 2;
    for (int i = 0; i < dy; i++) {
      one_stepY(y_dir);   
      reset += dx;
      if (reset >= dy) {
        reset -= dy;
        one_stepX(x_dir);
      }
      pause(step_delay);
    }
  }

  // Set new positions
  px = newx;
  py = newy;
}


void pause(int S){
  delay(S);
}
void move_X( int newx){
  float dx = newx-px;
  X.rotate(dx * stepmm);
  px = newx;
}

void move_Y( int newy){
  float dy = newy-py;
  Y.rotate(dy * stepmm);
  py = newy;
}
void one_revX(){
  X.rotate(360);
  px = px + 38.4;
}

void one_revY(){;
  Y.rotate(360);
  py = py + 38.4;
}

void one_stepX(int dir){
  X.rotate(stepmm * dir);
  px = px + 1;
}

void one_stepY(int dir){
  X.rotate(stepmm * dir);
  py = py + 1;
}

void set_pos(int newx, int newy){
  px = newx;
  py = newy;
}

void print_pos(){
  Serial.println(px);
  Serial.println(py);
}

/**
 * display helpful information
 */
void help() {
  Serial.print(F("Gcode LED DEMO "));
  Serial.println(F("Commands:"));
  Serial.println(F("M1; - one rev X"));
  Serial.println(F("M2; - one rev Y"));
  Serial.println(F("M3 X[]; - Move X steps "));
  Serial.println(F("M4 Y[]; - Move Y steps"));
  Serial.println(F("M5 X[] Y[]; - Set postition"));
  Serial.println(F("M6; - Print postition"));
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
