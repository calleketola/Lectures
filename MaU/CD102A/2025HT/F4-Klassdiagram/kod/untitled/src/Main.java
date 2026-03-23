public class Main {

    public static void main(String[] args){
        Person peep1 = new Person("Calle", 1991);
        Person peep2 = new Person("Sebastian", 1988);

        // Places
        Workplace niagara = new Workplace("Niagara", "Nordenskiöldsgatan 1", new double[] {-0.4, 1.15});
        Home home1 = new Home("Lönngatan 44", new double[] {1.25,-1.64});
        Store sciFi = new Store("Science fiction-bokhandeln", "Södra Förstadsgatan 26", new double[] {0,0});

        Bike bike1 = new Bike("Black", "Skeppshult");

        peep1.addBike(bike1);
        peep1.changeWorkplace(niagara);
        peep1.changeHome(home1);

        peep1.travelHome();
        peep1.paintBike("red");
        peep1.travelToWork();
        peep1.travelToCoordinates(sciFi.getCoordinates());

        // Skapar olika instanser av Person
        Person teacher1 = new Person("Calle");
        Person teacher2 = new Person("Sebastian");
        Person teacher3 = new Person();
        // Anropar de olika instansternas "greeting"
        System.out.println(teacher1.greeting());
        System.out.println(teacher2.greeting());
        System.out.println(teacher3.greeting());
    }

}
