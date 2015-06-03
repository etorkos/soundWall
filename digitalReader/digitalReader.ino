
 // Define hardware connections
//#define PIN_GATE_IN 2
//#define IRQ_GATE_IN  0
//#define PIN_LED_OUT 13
#define PIN_ANALOG_IN A0

void setup()
{
  Serial.begin(9600);
  Serial.println("Initialized");
}

void loop()
{
  int value;
  value = analogRead(PIN_ANALOG_IN);
  
  if((value/10) > 2 ){
    Serial.println(value/10);
  }  
  delay(100);
}
