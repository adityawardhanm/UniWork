public class try_catch_finally {
    public static void main(String[] args) {
        try{
            int a = 3, b = 0;
            int c = a/b;
        }
        catch (ArithmeticException e){
            e.printStackTrace();
        }
        finally {
            System.out.println("Endline");
        }
    }
}
