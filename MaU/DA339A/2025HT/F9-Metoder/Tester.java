public class Tester {
// The indentation in this file is purposefully like this
// It makes it easier to paste
public static void Main(String[] args){
    // a^2+b^2=c^2 (Pythagoras sats)
    double a = 3;
    double b = 4;
    double c = Math.sqrt(Math.pow(a,2)+Math.pow(b,2));
    System.out.println(c);
}
public static double max(double a, double b){
    double greatest; // Initierar variabeln
    if (a >= b){
        greatest = a;
    }
    else{
        greatest = b;
    }
    return greatest;
}
double c = max(5.2, 7.9);
public static void main(String[] args) {
    String x = "All that is gold does not glitter";
    char a = myMethod(x); // Anropa metoden, spara svaret i a
    System.out.println(a);
}
public static char myMethod(String s){
    char firstLetter = s.charAt(0); // Hitta första bokstaven
    return firstLetter; // Skicka tillbaka första bokstaven
}
public static String secondMethod(String a, char b){
    String newString = a+b; // Konkatenerar texten
    return newString; // Returnerar vår nya sträng
}
public static void main(String[] args) {
    String s = secondMethod("Wow", 'a');
    System.out.println(s);    
}
public static void greet(String name, int age){
    System.out.println("Hello "+name+",it's so cool that you are "+age+"years old!");
}
public void checkSensors(){
    checkDoorSensors();
    checkStaircaseSensors();
    checkLobbySensors();
    checkOfficeSensors();
}
public double calculateSTD(double[] values){
    double sum = 0; // Härifrån
    for (int i = 0; i < values.length; i++){
        sum += values[i];
    } // Allt detta hade kunnat vara en egen metod, calculateMean
    double mean = sum/values.length; // Hit
    double s = 0;
    for (int i = 0; i < values.length; i++){
        s += Math.pow((values[i]-mean), 2);
    }
    double std = s/values.length;
    return std;
}
public static double max(double a, double b){
    if (a > b){
        return a; // Returnerar a
    }
    else{
        return b; // Returnerar b
    }
}
public double max(double a, double b){
    if (a>=b){return a;} // Vertical space är prime real estate
    else {return b;}
}
public double max(double a, double b, double c){
    if (a>=b && a>=c){return a;}
    else if (b>=a && b>= c){return b;}
    else {return c;}
}
max(1.0,3.0)
max(5.0.3.0,7.0)
public double max(double a, double b, double c){
    return max(a, max(b,c));
}
}

