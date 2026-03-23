public class Store {

    private String address;
    private String name;
    private double[] coordinates;

    public Store(String name, String address, double[] coordinates){
        this.name = name;
        this.address = address;
        this.coordinates = coordinates;
    }

    public double[] getCoordinates(){
        return this.coordinates;
    }
}
