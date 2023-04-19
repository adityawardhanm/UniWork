class dp{
    void department(){
        System.out.println("USCI");
        System.out.println("UID");
        System.out.println("KSD");
        System.out.println("USLM");
        System.out.println("UWSL");
    }
}
class USCI extends dp{
    void branches(){
        System.out.println("BSc");
        System.out.println("BTech");
    }
}
class subject extends USCI{
    void subjects(){
        System.out.println("Object Oriented Programming using Java");
        System.out.println("Probability and Statistics");
    }
}
public class multilevel_inheritance {
    public static void main(String[] args) {
        System.out.println("In Karnavati University");
        subject sb = new subject();
        System.out.println("\n");
        System.out.println("Department: ");
        sb.department();
        System.out.println("\n");
        System.out.println("Branches: ");
        sb.branches();
        System.out.println("\n");
        System.out.println("Subjects: ");
        sb.subjects();
    }
}
