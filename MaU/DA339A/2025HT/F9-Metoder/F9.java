/* *
 * Detta är JavaDoc. Ett verktyg för att skapa dokumentation
 * 
 * <p>
 * Vi tog inte upp det här i föreläsningen, men tydlighet i 
 * koden sträcker sig längre än själva koden. Det är också i 
 * kommentarerna. Därför har man utvecklat ett system för att 
 * standardisera vissa delar av domumentationen.
 * 
 * <p>
 * Jag har lagt till JavaDoc-dokumentation till varje metod
 * för att du ska kunna se hur det fungerar. Till detta ska 
 * jag också lägga upp vad som kan genereras utifrån 
 * dokumentationen.
 * 
 * @param variabelNamn Detta beskriver en av parametrarna som metoden tar emot
 * @param variabelNamn Detta beskriver en annan parameter
 * @return Detta beskriver vad som skickas tillbaka
 */
public class F9{
    // Denna fil innehåller det vi gjort under föreläsningen

    /**
     * Metod som ligger över allt annat.
     * <p>
     * Efter föreläsningen fick jag en fråga om man bara kan 
     * anropa metoder som ligger nedenför den metoden man är i, 
     * eller nedanför main(). Svaret är att metoden kan ligga 
     * var man vill. Men man brukar vilja ordna sina metoder så
     * att man själv, eller teamet, lätt kan hitta dem
     *  
     * @return Ett värde så att vi ser att det fungerar.
     */
    public static int hej(){
        System.out.println("Hej");
        return 0;
    }

    public static void main(String[] args){
        System.out.println("Jag hoppas att du antecknar och testar själv också");

        // Här skapar vi strängar för att testa metoden myMethod från presentationen
        // Det är pluspoäng om du vet var citaten kommer ifrån.         
        String words = "All that is gold does not glitter";
        String words2 = "Not all those who wander are lost";
        
        // Vi anropar funktionen myMethod()
        char first = myMethod(words);
        char first2 = myMethod(words2);

        // Vi skriver ut resultatet av myMethod()
        System.out.println(first);
        System.out.println(first2);

        // Här testar vi metoden greet.
        greet("Calle", 33);
        greet("Gunnel", 75);
        greet("Liam", 8);
        greet("Adam", 17);
        
       double a = f(4.0);
       System.out.println(a);

       //int b = max(5,3); // max() skickar tillbaka en double. Så detta fugnerar inte
       //System.out.println(b);
       
       double c = max(6.7,3.2,8.4);
       System.out.println(c);
    }

    /**
     * Matematiska funktioner fungerar också. Här har vi f(x)=3x+2
     * 
     * @param x Ett tal
     * @return f(x)
     */
    public static double f(double x){
        double y = 3*x+2;
        return y;
    }

    /**
     * Metod som fanns i presentationen. Hittar första bokstaven
     * 
     * @param s Strängen vi vill ha första bokstaven i
     * @return Den första bokstaven i strängen
     */
    public static char myMethod(String s){
        char firstLetter = s.charAt(0);
        return firstLetter;
    }

    /**
     * En metod som hälsar olika på en person beroende på ålder
     * 
     * <p>
     * Denna gjordes som svar på frågan: "Varför behövs en void 
     * funktion för att hälsa, det är ju bara en rad?" Så vi 
     * gjorde en lite mer komplicerad hälsning för att demonstrera.
     * 
     * @param name Personens namn
     * @param age Personens ålder 
     */
    public static void greet(String name, int age){
        if (age < 16) {
            System.out.println("Hej "+name+" du röstade inte igår.");
        }
        else if (age < 19){
            System.out.println("Hej "+name+" du går nog i gymnasiet");
        }
        else if (age >= 67){
            System.out.println("Hej "+name+" är du pensionär nu?");
        }
        else{
            System.out.println("Du är vuxen "+ name);
        }
    }

    /**
     * En metod som tar emot två tal och returnerar det största av talen
     * 
     * @param a ett tal
     * @param b ett tal
     * 
     * @return Det största av talen
     */
    public static double max(double a, double b){
        if (a>=b){
            return a;
        }
        else{
            return b;
        }
    }

    /**
     * Metod som tar emot tre tal och hittar det största
     * <p>
     * Den utkommenterade raden överst i metoden. Hur 
     * fungerar den tror du?
     * 
     * @param a Ett tal
     * @param b Ett till tal
     * @param c Ett tredje tal
     * @return Det största av talen
     */
    public static double max(double a, double b, double c){
        //return max(a, max(b,c)); // Vad händer här?
        if (a >= b && a >= c) {
            return a;
        }
        else if (b >= a && b >= c){
            return b;
        }
        else{
            return c;
        }
    }

/*
    // Denna bit kod var för att testa om 
    // det gick att ha en metod inuti en 
    // annan metod.  
    public void test(){
        String a = "Hejsan";
        public void testIgen(){
            System.out.println(a);
        }
    }*/
}