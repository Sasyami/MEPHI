import java.util.Scanner;

public class lab {
    public static void main(String args[]){
        /* var vec1 = new MyVector(1,0,0);
        var vec0 = new MyVector(0, 0, 0);
        var vec2 = new MyVector(0, 1, 1);
        System.out.println(vec1.plus(vec2).toString());
        System.out.println(vec1.minus(vec2).toString());
        System.out.println(vec1.scalar(vec0));
        System.out.println(vec1.X(vec2).toString()); */

        
        Scanner in = new Scanner(System.in);
        /*int a= in.nextInt();
        System.out.println(ispoweroftwo(a));
        in.nextLine();
        for (int i=0;i<12;i++){
            System.out.print(twelveFib()[i]);
            System.out.print(", ");
        }
        System.out.print("\n");
        int size = in.nextInt();
        int [] array=new int[size];
        for (int i=0;i<size;++i){
            array[i]=in.nextInt();
        }
        nechet(array);
        in.nextLine();
        */
        String str= in.nextLine();
        System.out.println(n_words(str));
        /*
        m_length();
        String str = in.nextLine();
        
        System.out.println(ispalindrom(str));
        */
        //System.out.println(excersize7.exc7(str)); 
        in.close();
    }

    public static boolean ispoweroftwo(int value){
        return value!=0&(((value&(value-1))==0) || ((-value&(-value-1))==0));
    }

    public static int [] twelveFib(){
        int [] array=new int [12];
        array[0]=0;
        array[1]=1;
        for (int i=2;i<12;++i){
            array[i]=array[i-1]+array[i-2];
        }
        return array;
    }

    public static void nechet(int [] array){
        for (int i =0;i<array.length;++i){
            if (isodd(array[i])){
                System.out.print(array[i]);
                System.out.print(", ");
            }
        }
        System.out.print("\n");
    
    }

    public static boolean isodd(int a){
        return a%2!=0;
    }
    public static boolean ispalindrom(String str){
        StringBuilder str1 = new StringBuilder(str.toLowerCase());
        StringBuilder str2 = new StringBuilder(str.toLowerCase()).reverse();
        return str1.equals(str2);
    }
    public static void m_length(){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m_length = 0;
        String str;
        in.nextLine();
        for (int i=0;i<n;++i){
            str=in.nextLine();
            if (str.length()>m_length){
                m_length=str.length();
            }
        }
        System.out.println(m_length);
        in.close();

    }
    public static int n_words(String str){
        /* int start=0;
        int end=0;
        int count=0;
        while(start<str.length()&&end<str.length()){
            while ((start<str.length()) && (str.charAt(start)==' ' || str.charAt(start)=='\t' || str.charAt(start)=='\n')){
                ++start;
            }
            end=start;
            while((end<str.length()) && (str.charAt(end)!=' ' && str.charAt(end)!='\n' && str.charAt(end)!='\t')){
                ++end;
            }
            if (end>=str.length()){
                break;
            }

            if (str.substring(start, Math.min(end, str.length()-1)).matches("[a-zA-Z]+")){
                ++count;
            }
            start=end;

        } */
        int count = 0;
        String[] array = str.split(" ");
        for (var i =0; i<array.length; ++i){
            if (array[i].matches("[a-zA-z]+")){
                count++;
            }
        }
        return count;
    }

}