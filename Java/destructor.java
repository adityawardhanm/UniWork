public class destructor
{
    public static void main(String[] args)
    {
        destructor d = new destructor();
        d.finalize();
        System.gc();
        System.out.println("hello world");
    }
    protected void finalize()
    {
        System.out.println("Bin Cleared");
    }
}
