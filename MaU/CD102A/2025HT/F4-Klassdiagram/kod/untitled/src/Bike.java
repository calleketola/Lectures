public class Bike{

    private String colour;
    private String maker;

    public Bike(String colour, String maker){
        this.colour = colour;
        this.maker = maker;
    }

    public String getColour(){
        return this.colour;
    }

    public String getMaker(){
        return this.maker;
    }

    public void setColour(String newColour){
        this.colour = newColour;
    }

}
