public class Workplace {

    private String address;
    private String name;
    private double[] coordinates;

    public Workplace(String name, String address, double[] coordinates){
        this.name = name;
        this.coordinates = coordinates;
        this.address = address;
    }

    public double[] getCoordinates(){
        return this.coordinates;
    }
}
