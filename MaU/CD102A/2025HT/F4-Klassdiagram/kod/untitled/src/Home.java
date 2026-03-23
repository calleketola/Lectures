public class Home {

    private String address;
    private double[] coordinates;

    public Home(String address, double[] coordinates){
        this.address = address;
        this.coordinates = coordinates;
    }

    public double[] getCoordinates(){
        return this.coordinates;
    }

    public String getAddress(){
        return this.address;
    }
}
