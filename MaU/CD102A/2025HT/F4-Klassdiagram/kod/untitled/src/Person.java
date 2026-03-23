public class Person{

    private int birthYear;
    private String name;

    private Bike myBike;

    private double[] currentPosition = {0,0};
    private Workplace workplace;
    private Home home;

    public Person(){
        this("Ingen", 0);
    }

    public Person(String name){
        this(name, 2000);
    }

    public Person(String name, int birthYear){
        this.name = name;
        this.birthYear = birthYear;
    }

    public void addBike(Bike newBike){
        this.myBike = newBike;
    }

    private void travel(double distance){
        System.out.printf("Rode my %s %s %.2f km %n", this.myBike.getColour(), this.myBike.getMaker(), distance);
    }

    public void changeWorkplace(Workplace newWorkplace){
        this.workplace = newWorkplace;
    }

    public void changeHome(Home newHome){
        this.home = newHome;
    }

    public String getHomeAddress(){
        return this.home.getAddress();
    }

    public void travelToWork(){
        this.travelToCoordinates(this.workplace.getCoordinates());
    }

    public void travelHome(){
        this.travelToCoordinates(this.home.getCoordinates());
    }

    public void travelToCoordinates(double[] destination){
        double x = Math.abs(this.currentPosition[0]-destination[0]);
        double y = Math.abs(this.currentPosition[1]-destination[1]);
        // We use the Manhattan distance i.e. x + y
        double distance = x + y;
        this.travel(distance);
        this.currentPosition = destination;
    }

    public void paintBike(String newColour){
        this.myBike.setColour(newColour);
    }

    public String greeting(){
        return "Hello my name is " + this.name;
    }

}

