interface games{
    void indoorgames();
}
interface outgames extends games{
    void outdoorgames();
}
class game implements outgames{
    public void outdoorgames() {
        System.out.println("Cricket");
        System.out.println("Football");
        System.out.println("Baskteball \n");
    }
    public void indoorgames() {
        System.out.println("Ludo");
        System.out.println("Carrom");
        System.out.println("Chess \n");
    }
}
class gaming implements outgames {
    public void indoorgames() {
        System.out.println("Hide and Seek \n");
    }
    public void outdoorgames() {
        System.out.println("Golf\n");
    }
}
public interface interface_example {
    public static void main(String[] args) {
        outgames og = new gaming();
        og.indoorgames();
        og.outdoorgames();
        outgames os = new game();
        os.indoorgames();
        os.outdoorgames();
    }
}

