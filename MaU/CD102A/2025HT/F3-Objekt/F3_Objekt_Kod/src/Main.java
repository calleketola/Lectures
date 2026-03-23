public class Main{
    public static void main(String[] args) {
        MinKlass test = new MinKlass("C");
        test.printName();
    }

    public static void testBikeClass(){
        Bike myBike = new Bike("svart", 7);
        myBike.roll();

        Bike yourBike = new Bike("röd", 21);

        yourBike.brake();

        myBike.getColour();
        myBike.setColour("orange");
    }
}