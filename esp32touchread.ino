int touchState[8] = {100,100,100,100};
int touchLastState[8] = {100,100,100,100};


int touchHigh = 40;
int touchLow = 20;


void setup(){
  Serial.begin(115200);
}

void loop()
{
  int del = 2;
  touchState[0] = touchRead(T3);	
  delay(del);
  touchState[1] = touchRead(T2);	
  delay(del);
    touchState[2] = touchRead(T0);
    delay(del);
  touchState[3] = touchRead(T4);	
  delay(del);
    touchState[4] = touchRead(T5);
  delay(del);
    touchState[5] = touchRead(T6);
  delay(del);
  touchState[6] = touchRead(T7);
  delay(del);
  
  for (int i = 0; i < 8; i++)
  {
    if ((touchState[i] < touchLow) && (touchLastState[i] > touchHigh))
    {
      Serial.println(i);
    }

    if ((touchState[i] < touchLow) || (touchState[i] > touchHigh))
      touchLastState[i] = touchState[i];
  }
  
}
