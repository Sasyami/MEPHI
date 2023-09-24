public class MyVector{
    public Integer x;
    public Integer y;
    public Integer z;
    
    public MyVector(int x1, int y1, int z1){
            x = x1;
            y = y1;
            z = z1;
    }

    public double length(){
        return Math.sqrt(x*x + y*y + z*z);
    }

    public MyVector X(MyVector vec1){

        return new MyVector(y*vec1.z - z*vec1.y, vec1.x*z-x*vec1.z, x*vec1.y - y*vec1.x);
    }

    public int scalar(MyVector vec1){
        int res = vec1.x*x + vec1.y*y + vec1.z*z;
        return res;
    }
    
    public MyVector minus(MyVector vec1){
        return new MyVector(x - vec1.x, y - vec1.y, z - vec1.z);
    }
    public MyVector plus(MyVector vec1){
        return new MyVector(x + vec1.x, y + vec1.y, z + vec1.z);
    }
    public String toString(){
        StringBuilder res_string = new StringBuilder();
        res_string.append(x.toString());
        res_string.append(" ");
        res_string.append(y.toString());
        res_string.append(" ");
        res_string.append(z.toString());
        return res_string.toString();

    }
    }
    

