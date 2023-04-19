class interest{
    float i(){return 0.02F;}
}
class SBI extends interest{
    float i(){return 0.011F;}
}
class ICICI extends interest{
    float i(){return 0.013F;}
}
class HDFC extends interest{
    float i(){return 0.03F;}
}
class runtime_polymorphism{
    public static void main(String[] args) {
        double p = 100000;
        interest j;
        j = new SBI();
        System.out.println("SBI Interest :"+p*j.i());
        j = new ICICI();
        System.out.println("ICICI Interest :"+p*j.i());
        j = new HDFC();
        System.out.println("HDFC Interest :"+p*j.i());

    }
}
