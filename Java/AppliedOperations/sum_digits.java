import java.util.Scanner;
/*The program to print the sum of digits in the variable input*/
public class sum_digits {
    public static void main(String[] args) {
        long number, sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        number = sc.nextInt();
        for (sum = 0; number!=0; number=number/10){
            sum = sum +number%10;
        }
        System.out.println("Sum of digits: "+ sum);
    }
}
