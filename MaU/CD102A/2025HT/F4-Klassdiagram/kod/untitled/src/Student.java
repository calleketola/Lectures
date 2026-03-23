public class Student {

    // Klassens attribut
    private String name;
    private String studentID;
    private int[] grades;
    private String[] courses;

    // Klassens kosntruktor
    public Student(String name, String studentID){
        this.name = name;
        this.studentID = studentID;

        this.grades = new int[12];
        this.courses = new String[12];
    }

    public void displayGrades(){
        // Logic goes here
    }

    public void attendClass(String course){

    }

    public int takeTest(String course){
        return 0;
    }

    public String getName(){
        return this.name;
    }

    public String getStudentID(){
        return this.studentID;
    }
}
