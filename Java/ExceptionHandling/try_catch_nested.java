public class try_catch_nested {
    public static void main(String[] args) {
        int a = 3, b = 0;
        try{
            System.out.println("initial");
            int c;
            try {
                c = a/b;
                System.out.println("first nested try");
            }
            catch (Exception e1){
                System.out.println("Exception");
            }
            try {
                int d = a/b;
                System.out.println("second nested try");
            }
            catch (Exception e2){
                e2.printStackTrace();
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
        finally {
            System.out.println("Endline");
        }
    }
}
