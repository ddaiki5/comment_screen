import processing.net.*;

int port = 49000; // 適当なポート番号を設定

Server server;
ArrayList<Message> ma;
PGraphics img;

void setup() {
  size(1000, 600);
  img = createGraphics(width, height);
  PFont font = createFont("MS Gothic", 32);
  textFont(font);
  ma = new ArrayList<Message>();
  server = new Server(this, port);
  println("server address: " + server.ip()); // IPアドレスを出力
}

void draw() {
  background(255);
  Client client = server.available();
  if (client !=null) {
    String whatClientSaid = client.readString();
    if (whatClientSaid != null) {
      println(whatClientSaid); // Pythonからのメッセージを出力
      ma.add(new Message(whatClientSaid));
    }
  } 
  for (int i=0; i<ma.size(); i++) {
    if (ma.get(i).getVanishFlag())ma.remove(i);
    else {
      ma.get(i).update();
      println(ma.get(i).t);
      println((int)ma.get(i).t.charAt(0));
    }
  }
}


class Message {
  private String t;
  private float x, y;
  private boolean vanishFlag;
  Message(String text) {
    this.t = text;
    x = width;
    y = random(height/4, height*3/4);
    vanishFlag = false;
  }

  public void update() {
    move();
    render();
  }

  private void render() {
    fill(0);
    text(t, x, y);
  }

  private void move() {
    x--;
    print(x);
    if (x<-50) {
      vanishFlag = true;
    }
  }

  public boolean getVanishFlag() {
    return vanishFlag;
  }
}
