
//--ENCODER VARIABLES
volatile unsigned ticksR = 0;
volatile unsigned ticksL =0;

//Encoder pins
int encoderR = 3;
int encoderL = 2;

//Ticks in disk
int N = 20; 

//MOTOR PINS
// Motor Left
int pwmL = 6;
int dir1L = 8;
int dir2L = 7;
 
// Motor Right
int pwmR = 11;
int dir1R = 9;
int dir2R = 10;

//int stby = 12;


//ROBOT PARAMETERS
float L = 0.125; //Meters
float diameter = 0.066; //Meters
float radius = diameter / 2;
float x = 0.0;
float y = 0.0;
float theta = 0.0;
float omegaR = 0.0;
float omegaL = 0.0;

//TIME Variables
unsigned long prevTime = 0;

// ROBOT STATES
enum RobotState {
  FORWARD,
  TURN
};

RobotState state = FORWARD;

float startX = 0.0;
float startY = 0.0;
float targetTheta = 0.0;

// SQUARE TRAJECTORU
int squareSide = 0;
int sideLength = 0.5; // Meters


void setup() {
  // set the encoder pin
  pinMode(encoderL, INPUT);
  pinMode(encoderR, INPUT);
  //Create Interruption
  attachInterrupt(digitalPinToInterrupt(encoderR), rightEncoderCallback, FALLING);
  attachInterrupt(digitalPinToInterrupt(encoderL), leftEncoderCallback, FALLING);
  
  // Motor pins
  pinMode(pwmR, OUTPUT);
  pinMode(dir1R, OUTPUT);
  pinMode(dir2R, OUTPUT);

  pinMode(pwmL, OUTPUT);
  pinMode(dir1L, OUTPUT);
  pinMode(dir2L, OUTPUT);

  //pinMode(stby, OUTPUT);
  //digitalWrite(stby, HIGH);
   
  //Serial Communication
  Serial.begin(9600);
}


void rightEncoderCallback() {
  ticksR += 1;
}


void leftEncoderCallback() {
  ticksL += 1;
}


void moveForward(){
    
    //Left Motor
    analogWrite(pwmL, 200);
    digitalWrite(dir2L, HIGH);
    digitalWrite(dir1L, LOW);
    
    //Right Motor
    analogWrite(pwmR, 225);
    digitalWrite(dir1R, HIGH);
    digitalWrite(dir2R, LOW);
}


void rotateLeft(){
  // Left Motor backward
  analogWrite(pwmL, 200);
  digitalWrite(dir1L, HIGH);
  digitalWrite(dir2L, LOW);

  // Right Motor forward
  analogWrite(pwmR, 225);
  digitalWrite(dir1R, HIGH);
  digitalWrite(dir2R, LOW);
}

void stopMotors(){
  // Left Motor
  analogWrite(pwmL, 0);

  // Right Motor 
  analogWrite(pwmR, 0);
}

void loop() {
  Serial.println(ticksL);

  moveForward();
  delay(2000);
  stopMotors();
  delay(1000);
  rotateLeft();
  delay(1000);
}