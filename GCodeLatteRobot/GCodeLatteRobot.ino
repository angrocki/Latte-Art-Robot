/**
 * G-Code for Latte Art Robot
 * Written by: An Grocki, Madie Tong, Allyson Hur
 * Created: 11/05/2022
 */
//------------------------------------------------------------------------------------
// LIBRARIES ~ LIBRARIES ~ LIBRARIES ~ LIBRARIES ~ LIBRARIES ~ LIBRARIES ~ LIBRARIES 
//------------------------------------------------------------------------------------
#include <Arduino.h>
#include "MultiDriver.h"                    // library for moving multiple motors in tandem
#include "A4988.h"                          // library for establishing motor objects using stepper driving type A4988


//------------------------------------------------------------------------------------
// CONSTANTS ~ CONSTANTS ~ CONSTANTS ~ CONSTANTS ~ CONSTANTS ~ CONSTANTS ~ CONSTANTS
//------------------------------------------------------------------------------------
#define BAUD                 (115200)       // How fast Arduino is talking
#define MAX_BUF               (64)          // Size of longest message Arduino can store


//------------------------------------------------------------------------------------
// GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS ~ GLOBALS
//------------------------------------------------------------------------------------
char buffer[MAX_BUF];                       // where we store the message until we get a ';'
int sofar;                                  // how much is in the buffer
char mode_abs=1;                            // absolute mode?
float default_speed = 10; 
float default_speed_z = 30;  
float current_speed = 10;
float current_speed_T = 10;
float current_speed_Z = 10;
float max_speed = 120; 
float stepmm = 9.375;
long line_number=0;
float feedrate = 200;
float step_delay = 0;


//----------------------------------------------------------------------------------
// LOCAL VARIABLES ~ LOCAL VARIABLES ~ LOCAL VARIABLES ~ LOCAL VARIABLES ~ LOCAL VARIABLES
//----------------------------------------------------------------------------------
// Local variables to track the axis limit switch values
int x_switch;
int y_switch;
int z_switch;
int steps_x = 1;
int steps_y = 1;


//----------------------------------------------------------------------------------
// POSITION TRACKING VARIABLES ~ POSITION TRACKING VARIABLES ~ POSITION TRACKING VARIABLES
//----------------------------------------------------------------------------------
float px = 0 ;   //Position X
float py = 0;    //Position Y
float pz = 0;    //Position Z
float pt = 0;    //Position T
float reset;


//---------------------------------------------------------------------------------
// STEPPER MOTOR ESTABLISHMENT ~ STEPPER MOTOR ESTABLISHMENT ~ STEPPER MOTOR ESTABLISHMENT
//---------------------------------------------------------------------------------
// SOLENOID PINS

#define SOLENOID_PIN       17
#define TEMP_SENSOR_BED     1


// STEPPER MOTOR PINS

// X Motor
#define X_STEP_PIN         A0
#define X_DIR_PIN          A1
#define X_ENABLE_PIN       38
#define X_MIN_PIN          18
#define X_MAX_PIN          -1 //PIN 2 is used

// Y Motor
#define Y_STEP_PIN         A6
#define Y_DIR_PIN          A7
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          -1 //PIN 15 is used

// Z Motor
#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN           3
#define Z_MAX_PIN          -1 //PIN 19 is used

// Tilt Motor
#define E0_STEP_PIN        26
#define E0_DIR_PIN         28
#define E0_ENABLE_PIN      24

// Second Y Motor
#define E1_STEP_PIN        36
#define E1_DIR_PIN         34
#define E1_ENABLE_PIN      30


// DEFAULT MOTOR OBJECT SETTINGS

#define MOTOR_STEPS       200
#define MICROSTEPS         16
#define RPM               120
#define MS1                10
#define MS2                11
#define MS3                12


// STEPPER MOTOR OBJECTS

A4988 X(MOTOR_STEPS, X_DIR_PIN, X_STEP_PIN, X_ENABLE_PIN, MS1, MS2, MS3);
A4988 Y_1(MOTOR_STEPS, Y_DIR_PIN, Y_STEP_PIN, Y_ENABLE_PIN, MS1, MS2, MS3);
A4988 Y_2(MOTOR_STEPS, E1_DIR_PIN, E1_STEP_PIN, E1_ENABLE_PIN, MS1, MS2, MS3);
A4988 Z(MOTOR_STEPS, Z_DIR_PIN, Z_STEP_PIN, Z_ENABLE_PIN, MS1, MS2, MS3);
A4988 T(MOTOR_STEPS, E0_DIR_PIN, E0_STEP_PIN, E0_ENABLE_PIN, MS1, MS2, MS3);

MultiDriver controller(X, Y_1, Y_2, Z, T);


//---------------------------------------------------------------------------------
// SETUP FUNCTIONS ~ SETUP FUNCTIONS ~ SETUP FUNCTIONS ~ SETUP FUNCTIONS ~ SETUP FUNCTIONS
//---------------------------------------------------------------------------------
/** 
 *  A function that will establish the stepper motors' states before controls occur.
 */
void motor_setup() {
  // speed and step establishment
  X.begin(default_speed, MICROSTEPS);
  Y_1.begin(default_speed, MICROSTEPS);
  Y_2.begin(default_speed, MICROSTEPS);
  Z.begin(default_speed_z, MICROSTEPS);
  T.begin(default_speed, MICROSTEPS);

  // state establishment
  X.setEnableActiveState(LOW);
  Y_1.setEnableActiveState(LOW);
  Y_2.setEnableActiveState(LOW);
  Z.setEnableActiveState(LOW);
  T.setEnableActiveState(LOW);

  // 'on' establishment
  X.enable();
  Y_1.enable();
  Y_2.enable();
  Z.enable();
  T.disable();

  // limit switch establishment
  pinMode(X_MIN_PIN, INPUT);
  pinMode(Y_MIN_PIN, INPUT);
  pinMode(Z_MIN_PIN, INPUT); 
}

/** 
 *  A function that will establish the solenoid motor's state before controls occur.
 */
void solenoid_setup(){
  pinMode(SOLENOID_PIN, OUTPUT);
  digitalWrite(SOLENOID_PIN, LOW);
}

/**
 * A function that prepares the input buffer to receive a new message and tells the serial 
 * connected device it is ready for more.
 */
void ready() {
  sofar=0;  // clear input buffer
  Serial.print(F(">"));  // signal ready to receive input
}

/**
 * A function that reads the input buffer and find any recognized commands. One G or M command 
 * per line.
 */
void processCommand() {

  // Parsing Commands for 'G'
  int cmd = parseNumber('G',-1);
  switch(cmd) {
    case  1: {                                                          // case of G1: move motors to corresponding coordinates
      move_motors( parseNumber('X',px),
            parseNumber('Y',py),
            parseNumber('Z',pz),
            parseNumber('T',pt)
            );
      break;
     case 27: go_home(); break;                                         // case of G27: 'zero' motors by moving them to activate the limit switches
     case 28: cup_origin(); break;                                      // case of G28: move motors to hover over the center of the cup
     
     default:  break;
    }
  }

  // Parsing Commands for 'M'
  cmd = parseNumber('M',-1);
  switch(cmd) {
    case  6: wait(parseNumber('S',0)); break;                           // case of M6: delays the system at a specific part
    case 10: enable_Z(); break;                                         // case of M10: enables the Z-axis motor
    case 11: disable_Z(); break;                                        // case of M11: disables the Z-axis motor
    case 12: enable_T(); break;                                         // case of M12: enables the tilt motor
    case 13: disable_T(); break;                                        // case of M13: disables the tilt motor
    case 14: enable_X(); break;                                         // case of M14: enables the X-axis motor
    case 15: disable_X(); break;                                        // case of M15: disables the X-axis motor
    case 16: enable_Y(); break;                                         // case of M16: enables the Y-axis motor
    case 17: disable_Y(); break;                                        // case of M17: disables the Y-axis motor
    
    case 220: set_speed(parseNumber('S',current_speed)); break;         // case of M220: changes the speed of X/Y motors
    case 221: set_speed_Z(parseNumber('S',current_speed_Z)); break;     // case of M221: changes the speed of Z motor
    case 222: set_speed_T(parseNumber('S',current_speed_T)); break;     // case of M222: changes the speed of tilt motor
    case 380: enable_solenoid(); break;                                 // case of M380: enables the solenoid valve
    case 381: disable_solenoid(); break;                                // case of M381: disables the solenoid valve
    case  100:  help(); break;                                          // case of M100: prints available G-code commands in serial monitor
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


//---------------------------------------------------------------------------------
// G-CODE COMMANDS ~ G-CODE COMMANDS ~ G-CODE COMMANDS ~ G-CODE COMMANDS ~ G-CODE COMMANDS
//---------------------------------------------------------------------------------
/**
  * Set feedrate and step_delay based on the value entered.
  * @param: fr float representing new feedrate
  */
void set_feedrate(float fr) {
  step_delay = 1000000.0/fr;
  feedrate = fr;
}

/**
 * Converts given millimeters to number of steps motors must take to get to that given distance.
 */
void move_motors(int newx, int newy, int newz, int newt){
  int dx = convert_mm(newx - px);
  int dy = convert_mm(newy - py);
  int dz = convert_Z_mm(newz -pz);
  int dt = pt - newt;
  controller.rotate(dx, dy, dy, dz, dt);
  
  // Set new positions
  px = newx;
  py = newy;
  pz = newz;
  pt = newt;
}

/**
 * Converts a given distance (in mm) to degrees to rotate (non-Z axis) motors.
 */
int convert_mm(int dist) {
  // 
  int degree = dist * 9.375;
  return degree;
}

/**
 * Converts a given distance (in mm) to degrees to rotate Z-axis motor.
 */
int convert_Z_mm(int dist) {
  int degree = dist *51;
  return degree;
}

/**
 * Moves the x-axis motor to the origin.
 */
void x_origin() {

  // MOVES TO ORIGIN
    X.rotate(convert_mm(-px));    
    px = 0;
}

/**
 * Moves the y-axis motors to the origin.
 */
void y_origin() {
    controller.rotate(0,convert_mm(-py),convert_mm(-py),0,0);
    py = 0; 
}


/**
 * Moves each axis motor until it reaches the limit switch, at which point it is "zeroed."
 */
void go_home(){
     // Z-AXIS ZEROING
    z_switch = digitalRead(Z_MIN_PIN);                // reads the pin 
    Serial.println(z_switch);
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
    
   
    px=47;
    py=-39;
 }

 /**
  * Moves the x and y axis motors to set the gantry at the center of the cup.
  */
  void cup_origin(){
    set_speed(50);
    x_origin();
    y_origin(); 
}

/**
 * Prints the current global coordinates of the motors.
 */
void print_pos(){
  Serial.println(px);
  Serial.println(py);
}

/**
 * Turns the solenoid valve on.
 */
void enable_solenoid(){
  digitalWrite(SOLENOID_PIN, HIGH);
}

/**
 * Turns the solenoid valve off.
 */
void disable_solenoid(){
  digitalWrite(SOLENOID_PIN, LOW);  
}

/**
 * Enables the Z-axis motor.
 */
void enable_Z(){
  Z.enable();
}

/**
 * Disables the Z-axis motor.
 */
void disable_Z(){
  Z.disable();
}

/**
 * Enables the tilt motor.
 */
void enable_T(){
  T.enable();
}

/**
 * Disables the tilt motor.
 */
void disable_T(){
  T.disable();
}

/**
 * Enables the X-axis motor.
 */
void enable_X(){
  X.enable();
}

/**
 * Disables the X-axis motor.
 */
void disable_X(){
  X.disable();
}

/**
 * Enables the Y-axis motors.
 */
void enable_Y(){
  Y_1.enable();
  Y_2.enable();
}

/**
 * Disables the Y-axis motors.
 */
void disable_Y(){
  Y_1.disable();
  Y_2.disable(); 
}

/**
 * Sets the new speed of the X/Y motors to a given speed in RPM only if the speed is 
 * within the maximum and minimum limits.
 */
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

/**
 * Sets the new speed of the tilt motor to a given speed in RPM only if the speed is
 * within the maximum and iminimum limits.
 */
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

/**
 * Sets the new speed of the Z motor to a given speed in RPM only ifthe speed is
 * within the maximum and iminimum limits.
 */
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

/**
 * Delays the code by however many seconds given.
 */
void wait(int s){
  delay(s);
}

/**
 * Displays helpful G-Code Commands and their functions.
 */
void help() {
  Serial.print(F("G-Code Latte Commands"));
  Serial.println(F("Commands:"));
  Serial.println(F("G1 X[] Y[] Z[] T[]; - Move Motors"));
  Serial.println(F("G27; - Go Home"));
  Serial.println(F("G28; - Go to Cup Origin"));
  Serial.println(F("G92 X[] Y[]; - Set Position"));
  Serial.println(F("M6 S[]; - Delay"));
  Serial.println(F("M10; - Enable Z Motor"));
  Serial.println(F("M11; - Disable Z Motor"));
  Serial.println(F("M12; - Enable T Motor"));
  Serial.println(F("M13; - Disable T Motor"));
  Serial.println(F("M14; - Enable X Motor"));
  Serial.println(F("M15; - Disable X Motor"));
  Serial.println(F("M16; - Enable  Y Motor"));
  Serial.println(F("M17; - Disable Y Motor"));
  Serial.println(F("M220 S[]; - Set XY Motor Speeds"));
  Serial.println(F("M221 S[]; - Set Z Motor Speeds"));
  Serial.println(F("M22 S[]; - Set T Motor Speeds"));
  Serial.println(F("M380; - Enable Solenoid"));
  Serial.println(F("M381; - Disable Solenoid"));
  Serial.println(F("M100; - this help message"));
}


//---------------------------------------------------------------------------------
// MAIN BODY ~ MAIN BODY ~ MAIN BODY ~ MAIN BODY ~ MAIN BODY ~ MAIN BODY ~ MAIN BODY
//---------------------------------------------------------------------------------
void setup() {
  motor_setup();
  Serial.begin(BAUD);
  help();
  go_home();
  cup_origin();
  X.disable();
  Y_1.disable();
  Y_2.disable();
  Z.disable();
  T.disable();
  ready();
  solenoid_setup();
  disable_solenoid();
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
