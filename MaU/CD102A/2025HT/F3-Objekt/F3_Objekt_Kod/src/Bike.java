public class Bike {

    private String colour ; // Attribut
    private int gears ; // Attribut

    public Bike(){
        this.colour = "svart";
        this.gears = 1;
    }

    public Bike (String colour, int gears){ // Konstruktor
        this.colour = colour;
        this.gears = gears;
    }

    public void roll(){ // Operation / metod
        System.out.println("Cykeln rullar");
    }

    public void brake (){ // Operation / metod
        System.out.println("Cykeln bromsar.");
    }

    public String getColour(){
        return this.colour;
    }

    public void setColour(String newColour){
        this.colour = newColour;
    }
}
