class usci extends hierarchial_inheritance{
    void branches(){
        System.out.println("BSc");
        System.out.println("BTech");
    }
}
class uid extends hierarchial_inheritance{
    void branches(){
        System.out.println("BDes");
        System.out.println("Mdes");

    }
}
public class hierarchial_inheritance {
    public static void main(String[] args) {
        usci us = new usci();
        uid ui = new uid();
        System.out.println("In Karnavati University");
        System.out.println("\n");
        System.out.println("USCI: ");
        us.branches();
        System.out.println("\n");
        System.out.println("UID: ");
        ui.branches();
        System.out.println("\n");
    }
}
