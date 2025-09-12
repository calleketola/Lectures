// Detta är en kommentar
/*
Detta är en lång kommentar
*/

public class test {
// These are purposefully dedented
int a = 5; // heltal
float b = 5.5f; // flyttal (32 bitar, 7 decimaler) notera f
double c = 5.5; // flyttal (64 bitar, 15-16 decimaler)
boolean d = true; // notera liten bokstav
String e = "hej"; // notera storbokstav och citattecken
char f = 'a'; // Notera apostrofer

// Java
Scanner input = new Scanner(System.in); // Nödvändig rad
System.out.print("Name: ");
String name = input.nextLine(); // Ta emot sträng
System.out.print("Age: ");
int age = input.nextInt(); // Ta emot heltal
System.out.println(name + " " + age);

Scanner input = new Scanner(System.in); // Skapar en läsare
String text = input.nextLine(); // Tar emot en sträng
int integer = input.nextInt(); // Tar emot ett heltal
double number = input.nextDouble(); // Tar emot ett flyttal

if (a == true && b == false){ // Notera parenteserna
    // Notera att && betyder och
}
else if (c == true || d == true){ // Vi skriver ut elif
    // Notera att || betyder eller
}
else{
    // Notera alla { } som markerar block
}
// En while-loop i Java
int i = 0;
while (i < 10){ // Notera återigen parenteserna
    System.out.println(i);
    i++; // Detta motsvarar i += 1
}
// For-loop i Java
for (int i = 0; i < 10; i++){ // Start, Stop, Steg
    System.out.println(i);
}

// Array i Java
int[] myArray = {3,1,4,1,5};
System.out.println(myArray[0]);

int[] anArray = new int[10]; // Skapar en tom array med 10 platser
anArray = new int[100]; // Skapar en ny tom array med 100 platser

    public static void main(String[] args){
        int[] hej = {0,1,2};
        myMethod(hej);
        System.out.println(hej[0]);
    }

public double myMethod(double par1, double par2){
    double result = par1+par2;
    return result;
}

public double myMethod(){
    return 0.0;
}
public double myMethod(double a){
    return 5*a;
}
public double myMethod(double a, double b){
    return 5*(a+b);
}
}