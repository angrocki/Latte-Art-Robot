//------------------------------------------------------------------------------
// 1 LED G-Code Demo
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

long line_number=0;
const uint8_t RED = 13; // RED Led is connected to D13

//------------------------------------------------------------------------------
// STRUCTS
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
// METHODS
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
// Processing G-Code
//------------------------------------------------------------------------------

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
  case  1: LED_enable(); break;
  case  2: LED_disable();break;
  }
 
  cmd = parseNumber('M',-1);
  switch(cmd) {
  case  1:  LED_blink_slow();  break;
  case  2:  LED_blink_fast();
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
 * Blinks LED every second (slow)
 */
void LED_blink_slow(){
  digitalWrite(RED, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(RED, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
  
}
/**
 * Blinks LED every half a second (fast)
 */
void LED_blink_fast(){
  digitalWrite(RED, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  digitalWrite(RED, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
  
}
/**
 * Turns on LED 
 */
void LED_enable(){
   digitalWrite(RED, HIGH);
}
/**
 * Turns off LED 
 */
void LED_disable(){
   digitalWrite(RED, LOW);
}

//------------------------------------------------------------------------------
// Main Body
//------------------------------------------------------------------------------

void setup() {
  pinMode(RED, OUTPUT);
  Serial.begin(BAUD);
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
