class add{
    static int addition(int a, int b){return a+b;}
    static int addition(int a, int b, int c){return a+b+c;}
    }
public class compile_polymorphism {
    public static void main(String[] args) {
        System.out.println(add.addition(15,13));
        System.out.println(add.addition(12,13,14));
    }
}
