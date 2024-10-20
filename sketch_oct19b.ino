#include <AccelStepper.h>
#include <MultiStepper.h>

AccelStepper stepper1(AccelStepper::FULL2WIRE, 2, 3);
AccelStepper stepper2(AccelStepper::FULL2WIRE, 8, 9);

MultiStepper steppers;

// const int speed = 2 * 1600;
const int speed = 1600;
const int length = 2 * 1600;
const int move = length / 2;

void setup() {
  Serial.begin(9600);

  // Configure each stepper
  stepper1.setMaxSpeed(speed);
  stepper2.setMaxSpeed(speed);

  // stepper1.setCurrentPosition(0);
  // stepper2.setCurrentPosition(0);

  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
}

void moveTo(int p1, int p2) {
  long positions[2] = {p1, p2};
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
  printLocation();
}

void printLocation() {
  Serial.print(stepper1.currentPosition());
  Serial.print(", ");
  Serial.println(stepper2.currentPosition());
}

void loop() {

  while (Serial.available() == 0);

  if (Serial.readString() == "start\n") {
    moveTo(0, 0);
    delay(1000);

    moveTo(move, move);
    delay(1000);

    moveTo(move, -1 * move);
    delay(1000);
    
    moveTo(-1 * move, -1 * move);
    delay(1000);
    
    moveTo(-1 * move, move);
    delay(1000);

    moveTo(0, 0);
    delay(1000);
  }
}
