//------------------------------------------------------------------------------
// G-Code for Latte Art Robot
// Goal: Create multiple latte Art designs controlled by serial communication with Python
// Created 11/05/2022
//------------------------------------------------------------------------------
#include <Arduino.h>
#include "MultiDriver.h"
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
float current_speed = 10;
float current_speed_T = 10;
float current_speed_Z = 10;
float max_speed = 120; 
float stepmm = 9.375;
long line_number=0;
float feedrate = 200;
float step_delay = 0;

//------------------------------------------------------------------------------
// LOCAL VARIABLES
//------------------------------------------------------------------------------

//axis limit switch local variables

int x_switch;
int y_switch;
int z_switch;
int steps_x = 1;
int steps_y = 1;

//------------------------------------------------------------------------------
// Postion 
//------------------------------------------------------------------------------

float px = 0 ;   //Position X
float py = 0;    //Position Y
float pz = 0;    //Position Y
float pt = 0;    //Position T
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
// INITIALIZING Solenoid
#define SOLENOID_PIN           32
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

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          -1 //PIN 19 is used

//extruder 1
#define E0_STEP_PIN        26
#define E0_DIR_PIN         28
#define E0_ENABLE_PIN      24

//extruder 2
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
A4988 Z(MOTOR_STEPS, Z_DIR_PIN, Z_STEP_PIN, Z_ENABLE_PIN, MS1, MS2, MS3);
A4988 T(MOTOR_STEPS, E0_DIR_PIN, E0_STEP_PIN, E0_ENABLE_PIN, MS1, MS2, MS3);

MultiDriver controller(X, Y_1, Y_2, Z, T);
//------------------------------------------------------------------------------


void motor_setup() {
  X.begin(default_speed, MICROSTEPS);
  Y_1.begin(default_speed, MICROSTEPS);
  Y_2.begin(default_speed, MICROSTEPS);
  Z.begin(default_speed, MICROSTEPS);
  T.begin(default_speed, MICROSTEPS);

  X.setEnableActiveState(LOW);
  Y_1.setEnableActiveState(LOW);
  Y_2.setEnableActiveState(LOW);
  Z.setEnableActiveState(LOW);
  T.setEnableActiveState(LOW);

  X.enable();
  Y_1.enable();
  Y_2.enable();
  Z.enable();
  T.disable();

  pinMode(X_MIN_PIN, INPUT);
  pinMode(Y_MIN_PIN, INPUT);
  pinMode(Z_MIN_PIN, INPUT);
  
}

void solenoid_setup(){
  pinMode(SOLENOID_PIN, OUTPUT);
  digitalWrite(SOLENOID_PIN, LOW);
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
    move_motors( parseNumber('X',px),
          parseNumber('Y',py),
          parseNumber('Z',pz),
          parseNumber('T',pt)
          );
    break;
   case 27: go_home(); break;
   case 28: cup_origin(); break;
   case 92: set_pos(parseNumber('X', px),
                  parseNumber('Y', py)); break;
   default:  break;
  }
    }
  cmd = parseNumber('M',-1);
  switch(cmd) {
  case  6: wait(parseNumber('S',0))
  case 10: enable_Z(); break;
  case 11: disable_Z(); break;
  case 12: enable_T(); break;
  case 13: disable_T(); break;
  case 14: enable_X(); break;
  case 15: disable_X(); break;
  case 16: enable_Y(); break;
  case 17: disable_Y(); break;
  case 220: set_speed(parseNumber('S',current_speed)); break;
  case 221: set_speed_Z(parseNumber('S',current_speed_Z)); break;
  case 222: set_speed_T(parseNumber('S',current_speed_T)); break;
  case 380: enable_solenoid(); break; 
  case 381: disable_solenoid(); break; 
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
  int dx = convert_mm(newx - px);
  int dy = convert_mm(newy - py);
  controller.rotate(dx, dy, dy, 0, 0);
  // Set new positions
  px = newx;
  py = newy;
}
void move_motors(int newx, int newy, int newz, int newt){
  int dx = convert_mm(newx) - px;
  int dy = convert_mm(newy) - py;
  int dz = convert_Z_mm(newz -pz);
  int dt = pt - newt;
  controller.rotate(dx, dy, dy, dz, dt);
   // Set new positions
  px = newx;
  py = newy;
  pz = newz;
  pt = newt;
  
}
int convert_mm(int dist) {
  // Converts a given distance (in mm) to degrees to rotate motors
  int degree = dist * 9.375;
  return degree;
}


int convert_Z_mm(int dist) {
  // Converts a given distance (in mm) to degrees to rotate motors
  int degree = dist * 1.7;
  return degree;
}

void x_origin() {

  // MOVES TO ORIGIN
    X.rotate(convert_mm(-px));    
    px = 0;
}

void y_origin() {
    controller.rotate(0,convert_mm(-py),convert_mm(-py),0,0);
    py = 0; 
}

void go_home(){
    // Z-AXIS ZEROING
    z_switch = digitalRead(Z_MIN_PIN);                // reads the pin 
    while (z_switch == 1) {                           // while limit is inactivated 
        z_switch = digitalRead(Z_MIN_PIN);
        controller.rotate(0,0,0,-1,0);                // move z-axis motor
    }
    
    // X-AXIS ZEROING
    x_switch = digitalRead(X_MIN_PIN);                // reads the pin 
    while (x_switch == 1) {                           // while limit is inactivated 
      x_switch = digitalRead(X_MIN_PIN);
      controller.rotate(1,0,0,0,0);                   // move x-axis motor
    }
    
    // Y-AXIS ZEROING
    y_switch = digitalRead(Y_MIN_PIN);                // reads the pin 
    while (y_switch == 1) {                           // while limit is inactivated 
      y_switch = digitalRead(Y_MIN_PIN);
      controller.rotate(0,-1,-1,0,0);                 // move y-axis motors
    }
    px=40;
    py=-69;
    }
  void cup_origin(){
    x_origin();
    y_origin(); 
}



void pause(int S){
  delay(S);
}

void set_pos(int newx, int newy){
  px = newx;
  py = newy;
}

void print_pos(){
  Serial.println(px);
  Serial.println(py);
}

void enable_solenoid(){
  digitalWrite(SOLENOID_PIN, HIGH);
  
}
void disable_solenoid(){
  digitalWrite(SOLENOID_PIN, LOW);
  
}
void enable_Z(){
  Z.enable();
}

void disable_Z(){
  Z.disable();
}

void enable_T(){
  T.enable();
}

void disable_T(){
  T.disable();
  
}
void enable_X(){
  X.enable();
}

void disable_X(){
  X.disable();
  
}

void enable_Y(){
  Y_1.enable();
  Y_2.enable();
}

void disable_Y(){
  Y_1.disable();
  Y_2.disable();
  
}
void set_speed(int s) {
  if (s > max_speed) {
    current_speed = max_speed;
  }
  else if (s < 0) {
    current_speed = 0;
  }
  else{
    current_speed = s;
  }
  X.setRPM(s);
  Y_1.setRPM(s);
  Y_2.setRPM(s);
}
void set_speed_T(int s) {
  if (s > max_speed) {
    current_speed_T = max_speed;
  }
  else if (s < 0) {
    current_speed_T = 0;
  }
  else{
    current_speed_T = s;
  }
  T.setRPM(s); 
}

void set_speed_Z(int s) {
  if (s > max_speed) {
    current_speed_Z = max_speed;
  }
  else if (s < 0) {
    current_speed_Z = 0;
  }
  else{
    current_speed_Z = s;
  }
  Z.setRPM(s); 
}

void wait(int s){
  delay(s);
}
/** 
 *  To Do: 
 * Add G-Code for Tilt cup 
 * if turning on and off does not work do rapid movent (G0) with vaule off
 * Add G code for cup orgin 
 * Add Z in line / add z by itself (multiple modes way above + following flow rate
 * global varibles for z 
 * Add in sensor data / model flow rate
 * soft stop 
 */



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
  motor_setup();
  solenoid_setup();
  Serial.begin(BAUD);
  help();
  go_home();
  X.disable();
  Y_1.disable();
  Y_2.disable();
  Z.disable();
  T.disable();
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
      buffer[sofar]=0;  // end the buffer so string fu   nctions work right
      Serial.print(F("\r\n"));  // echo a return character for humans
      processCommand();  // do something with the command
      ready();
    }
    
  }

}
