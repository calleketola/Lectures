import java.util.Random;

public class Student{
    private String name;
    private int studentID;
    private int[] grades;
    private String[] courses;

    public Student(String n, int sID){
        this.name = n;
        this.studentID = sID;
        this.grades = new int[4];
        this.courses = new String[4];
    }

    public void addCourse(String course){
        // Find free spot
        for (int i = 0; i < this.courses.length; i++){
            if (this.courses[i].equals("")){
                // Add course
                this.courses[i] = course;
                this.grades[i] = 0;
                return; // Avslutar metoden
            }
        }
    }

    public void attendClass(String course){
        // Find the course
        for (int i = 0; i < this.courses.length; i++){
            if (this.courses[i].equals(course)){
                this.grades[i]++;
                return; // Avslutar metoden
            }
        }
    } 

    public int takeTest(String course){
        Random r = new Random();
        int luck = r.nextInt(-10,25);
        int score = 0;
        // Find the course in array
        for (int i = 0; i < this.courses.length; i++){
            if (this.courses[i].equals(course)){
                score = this.grades[i];
                break; // Avslutar loopen
            }
        }
        score += luck;
        if (score < 0){
            score = 0;
        }
        return score;
    }
}