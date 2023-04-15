import java.util.Scanner;
public class BitwiseOp_Variable {
    public static void main(String[] args) {
        try {
            //Following is an Example of Bitwise Operator using User Input
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter number 1:");
            int a = sc.nextInt();
            System.out.println("Enter number 2:");
            int b = sc.nextInt();
            System.out.println("Enter number 3:");
            int c = sc.nextInt();
            System.out.println("a<b^a<c is " + (a<b^a<c));
            System.out.println("a<b|a<c is " + (a<b|a<c));
            System.out.println("a<b&a<c is " + (a<b&a<c));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
