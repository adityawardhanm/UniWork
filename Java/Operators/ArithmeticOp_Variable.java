import java.util.Scanner;
public class ArithmeticOp_Variable {
    public static void main(String[] args) {
        try {
            //Following is an Example of Arithmetic Operator using User Input
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter number 1:");
            int n1 = sc.nextInt();
            System.out.println("Enter number 2:");
            int n2 = sc.nextInt();
            System.out.println("Sum is" + (n1 + n2));
            System.out.println("Diff is" + (n1 - n2));
            System.out.println("Product is" + (n1 * n2));
            System.out.println("Quotient is" + (n1 / n2));
            System.out.println("Remainder is" + (n1 % n2));
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}
