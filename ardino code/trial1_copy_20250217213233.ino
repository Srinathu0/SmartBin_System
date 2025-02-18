#include <Servo.h>

Servo servoRecyclable;
Servo servoHazardous;
Servo servoFood;

int binNumber;
bool binOpened = false;  // Flag to track if a bin is currently open

void setup() {
    servoRecyclable.attach(9);  // Attach servo for recyclable waste to pin 9
    servoHazardous.attach(10);   // Attach servo for hazardous waste to pin 10
    servoFood.attach(11);        // Attach servo for food waste to pin 11
    Serial.begin(9600);          // Initialize serial communication
    Serial.println("Setup complete. Ready for input.");  // Debug message
}

void loop() {
    if (Serial.available() > 0) {
        binNumber = Serial.parseInt(); // Read bin number from serial
        Serial.print("Received bin number: ");
        Serial.println(binNumber);
        openBin(binNumber);  // Call openBin function to open specified bin
    }
}

void openBin(int binNumber) {
    Serial.println("openBin function called"); // Debugging message

    // Close any open bins first before opening a new one
    if (binOpened) {
        Serial.println("Closing any previously opened bin.");
        closeOpenBins();
        binOpened = false;
    }

    // Open the specified bin based on binNumber
    if (binNumber == 1) {
        Serial.println("Opening hazardous waste bin");
        servoHazardous.write(0); // Open hazardous waste bin
        delay(5000);              // Delay to keep the bin open
        servoHazardous.write(90); // Close the bin
        binOpened = true;
        Serial.println("Hazardous waste bin closed");
    } else if (binNumber == 2) {
        Serial.println("Opening food waste bin");
        servoFood.write(0);       // Open food waste bin
        delay(5000);              // Delay to keep the bin open
        servoFood.write(90);      // Close the bin
        binOpened = true;
        Serial.println("Food waste bin closed");
    } else if (binNumber == 3) {
        Serial.println("Opening recyclable waste bin");
        servoRecyclable.write(0); // Open recyclable waste bin
        delay(5000);              // Delay to keep the bin open
        servoRecyclable.write(90); // Close the bin
        binOpened = true;
        Serial.println("Recyclable waste bin closed");
    } else {
        Serial.println("Invalid bin number received.");  // Message for invalid input
    }
}

void closeOpenBins() {
    servoRecyclable.write(90); // Close recyclable waste bin if open
    servoHazardous.write(90);  // Close hazardous waste bin if open
    servoFood.write(90);       // Close food waste bin if open
    Serial.println("All bins closed");
}

