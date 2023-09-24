public class PostGraduateStudent extends Student{
    
    public PostGraduateStudent(String new_name, String new_secondname, double new_avgscore){
        super(new_name,new_secondname,new_avgscore);

    }

    @Override
    public int getScolarship(){
        if (avgscore == 5){
            return 150;
        }
        return 100;
    }
}
