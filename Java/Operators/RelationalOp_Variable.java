import java.util.Scanner;
public class RelationalOp_Variable {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter number 1:");
            int a = sc.nextInt();
            System.out.println("Enter number 2:");
            int b = sc.nextInt();
            System.out.println("a == b is " + (a == b));
            System.out.println("a != b is " + (a != b));
            System.out.println("a >  b is " + (a > b));
            System.out.println("a >= b is " + (a >= b));
            System.out.println("a <  b is " + (a < b));
            System.out.println("a <= b is " + (a <= b));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
