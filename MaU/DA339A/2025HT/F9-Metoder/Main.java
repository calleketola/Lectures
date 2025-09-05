class Main{

    public static void main(String[] args){
        System.out.println(myMethod("hejsan"));
        System.out.println(secondMethod("wow", 'a'));
    }

    public static char myMethod(String s){
        return s.charAt(0);
    }

    public static String secondMethod(String s, char a){
        return s+a;
    }

    public double max(double a, double b){
    if (a>=b){return a;} // Vertical space is prime real estate
    else{return b;}
}
    public double max(double a, double b, double c){
        if (a>=b && a>=c){return a;}
        else if (b>=a && b>=c){return b;}
        else{return c;}
    }

}