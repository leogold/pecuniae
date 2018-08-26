#include <Stepper.h> 
#include <multiCameraIrControl.h>
char serialData;
const int stepsPerRevolution = 600; 

//Utilizando as portas digitais 08 a 11 para conexao ao motor
Stepper myStepper(stepsPerRevolution, 2,4,3,5); 
#define B_ent 12  // Enter Button
Canon T3i(9);

// Using http://slides.justen.eng.br/python-e-arduino as refference

void setup() {
    Serial.begin(9600);
     // Velocidade inicial do motor (MAX 100)
    myStepper.setSpeed(60);
    pinMode(B_ent, INPUT_PULLUP);

}

void loop() {
    if (Serial.available()) {
        serialData = Serial.read();
        if (serialData == '1') {
            //Gira o eixo do motor no sentido anti-horario - 120 graus
              delay(500);
              myStepper.step(682); 
        }
        else if (serialData == '0') {
            T3i.shutterNow();
        }
    }
    else if (digitalRead(B_ent) == 0)
    {
    //Gira o eixo do motor no sentido anti-horario - 120 graus
    for (int i = 0; i<=1; i++)
      {
      T3i.shutterNow();
      delay(500);
      myStepper.step(682); 
      delay(500);
      }
    T3i.shutterNow();
  }
}
