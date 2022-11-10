//------------------------------------------------------------------------------
// 4 LED G-Code Demo
// Goal: Test G-code structure with LED and Serial Communication with Python
// Created 11/05/2022
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
int blink_time = 500;   

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


void LED_setup(){
  pinMode(BLUE, OUTPUT); // Configure BLUE LED pin as a digital output
  pinMode(RED, OUTPUT); // Configure RED LED pin as a digital output
  pinMode(YELLOW, OUTPUT); // Configure YELLOW LED pin as a digital output
  pinMode(GREEN, OUTPUT); // Configure GREEN LED pin as a digital output
  digitalWrite(BLUE, LOW); // Set BLUE LED low initially
  digitalWrite(RED, LOW); // Set RED LED low initially
  digitalWrite(YELLOW, LOW); // Set YELLO LED low initially
  digitalWrite(GREEN, LOW); // Set GREEN LED low initially
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
  case  1: LED_blink(parseNumber('X',0),
                     parseNumber('Y',0),
                     parseNumber('Z',0),
                     parseNumber('E',0));
  break;
  case  2: blink_RED(); break;
    /*
    parseNumber('X',0),
          parseNumber('Y',0),
          parseNumber('Z',0),
          parseNumber('E',0));
          */
        break;                
  default:  break;
  }
  cmd = parseNumber('M',-1);
  switch(cmd) {
  case  1:  LED_enable();  break;
  case  2:  LED_disable(); break;
  case  3:  blink_speed(parseNumber('S', 1000)); break; 
  case  4:  pause(parseNumber('S', 0)); break ;
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

void pause(int S){
  delay(S);
}
void output(char *code,float val) {
  Serial.print(code);
  Serial.print(val);
  Serial.print(" ");
}

//------------------------------------------------------------------------------
// G-Code Commands
//------------------------------------------------------------------------------
/**
 * Blinks LED X amount of times based on input 
 * 
 */
void LED_blink(int X, int Y, int Z, int E){
  for (int i = 0; i < X; i++){
    digitalWrite(BLUE, HIGH);
    delay(blink_time);
    digitalWrite(BLUE, LOW);
    delay(blink_time);
  }
  for (int i = 0; i < Y; i++){
    digitalWrite(RED, HIGH);
    delay(blink_time);
    digitalWrite(RED, LOW);
    delay(blink_time);
  }
  for (int i = 0; i < Z; i++){
    digitalWrite(YELLOW, HIGH);
    delay(blink_time);
    digitalWrite(YELLOW, LOW);
    delay(blink_time);
  }
  for (int i=0; i < E; i++){
    digitalWrite(GREEN, HIGH);
    delay(blink_time);
    digitalWrite(GREEN, LOW);
    delay(blink_time);
  }
}

/**
 * Blinks RED LED to test speed function  
 */
void blink_RED(){
  for (int i = 0; i < 10; i++){
    digitalWrite(RED, HIGH);
    delay(blink_time);
    digitalWrite(RED, LOW);
    delay(blink_time);
  }
}
/**
 * Turns on LED 
 */
void LED_enable(){
   digitalWrite(RED, HIGH);
   digitalWrite(BLUE, HIGH);
   digitalWrite(YELLOW, HIGH);
   digitalWrite(GREEN, HIGH);
}
/**
 * Turns off LED 
 */
void LED_disable(){
   digitalWrite(RED, LOW);
   digitalWrite(BLUE, LOW);
   digitalWrite(YELLOW, LOW);
   digitalWrite(GREEN, LOW);
}


void blink_speed(int S){
  blink_time = S;
}

/**
 * display helpful information
 */
void help() {
  Serial.print(F("Gcode LED DEMO "));
  Serial.println(F("Commands:"));
  Serial.println(F("G1 LED_BLINK X[]Y[]Z[]E[]"));
    Serial.println(F("G2 BLINK_RED"));
  Serial.println(F("M1; - LED ON"));
  Serial.println(F("M2; - LED OFF"));
  Serial.println(F("M3; - SPEED S[ms]"));
  Serial.println(F("M3; - PAUSE S[ms]"));
  Serial.println(F("M100; - this help message"));

}

//------------------------------------------------------------------------------
// Main Body
//------------------------------------------------------------------------------

void setup() {
  LED_setup();
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
