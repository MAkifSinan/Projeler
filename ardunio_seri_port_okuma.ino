int veri1;
int veri2;
String veri3;
int random_verisi;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0,INPUT);
}

void loop() {
  random_verisi=analogRead(A0);
  
  veri1=random(0,random_verisi);
  veri2=random(random_verisi,random_verisi*2);
  veri3="veri3yazisi";

  
  String data = "";
  data += "x";
  data += "veri1=";
  data += veri1;
  data += "x";
  data += "veri2=";
  data += veri2;
  data += "x";
  data += "veri3=";
  data += veri3;
  data += "x";
  int len = data.length() + 1;
  char arr[len];
  data.toCharArray(arr, len);
  Serial.println(arr);
  delay(1000);
}
