class constructor1{
    int x;
    constructor1(int i){
        x=i;
    }
}
public class constructor {
    public static void main(String[] args) {
        constructor1 obj1 = new constructor1(10);
        constructor1 obj2 = new constructor1(20);
        System.out.println(obj1.x+" "+ obj2.x);
    }
}
