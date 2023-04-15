import java.util.Scanner;
public class UnaryOp_Variable {
    public static void main(String[] args) {
        try {
            //Following is an Example of Unary Operator using User Input
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter number 1:");
            int a = sc.nextInt();
            System.out.println("a++  is " + (a++));
            System.out.println("++a  is " + (++a));
            System.out.println("a-- is " + (a--));
            System.out.println("--a  is " + (--a));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
