public class excersize7 {
    public static boolean exc7(String str){
        if (!str.matches("([0-9]{1,3}\\.{1}){3}[0-9]{1,3}")){
                return false;
        }
        String[] array = str.split("\\.");
        for (int i=0;i<4;++i){
            if (array[i].length()>1 && array[i].startsWith("0")){
                return false;
            }
            if (array[i].length()<3){
                return true;
            }
            if(array[i].compareTo("256")>=0){
                return false;
            }
        }
        return true;
    }
}
