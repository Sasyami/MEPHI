public class Student{
    public String name;
    public String secondname;
    public double avgscore;
    
    public Student(String new_name, String new_secondname, double new_avgscore){
        name = new_name;
        secondname = new_secondname;
        avgscore = new_avgscore;

    }

    public int getScolarship(){
        if (avgscore == 5){
            return 80;
        }
        return 40;
    }
}

