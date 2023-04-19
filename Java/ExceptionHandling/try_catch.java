public class try_catch {
    public static void main(String[] args) {
        try{
            int a = 3, b = 0;
            int c = a/b;
        }
        catch (ArithmeticException e){
            e.printStackTrace();
        }
    }
}
