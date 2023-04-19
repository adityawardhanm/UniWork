class Us extends hybrid_inheritance{
    void name(){
        System.out.println("USCI \n");
    }
}
class Uid extends hybrid_inheritance{
    void names(){
        System.out.println("UID \n");

    }
}
class pro extends Us{
    void branches(){
        System.out.println("BSc");
        System.out.println("BTech");
    }
}
class sub extends pro{
    void subjects(){
        System.out.println("Object Oriented Programming using Java");
        System.out.println("Probability and Statistics");
    }
}
public class hybrid_inheritance {
    public static void main(String[] args) {
        sub sb = new sub();
        System.out.println("Karnavati University \n");
        sb.name();
        System.out.println("\n");
        sb.branches();
        System.out.println("\n");
        sb.subjects();
    }
}
