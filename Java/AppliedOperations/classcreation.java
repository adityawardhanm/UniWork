/*Creation of classcreation class*/
public class classcreation {
    public static void main(String[] args) {
        Student Aditya = new Student();
        Aditya.setdata("21BTAI01","Aditya",90,92,93);
        Aditya.displaydata();
    }
}
/*Creation of final class to create methods setData and displaydata*/

final class  Student{
    private String StudentID;
    private String Name;
    private int PhyMarks;
    private int ChemMarks;
    private int MathMarks;

    public void setdata(String StudentID, String Name, int PhyMarks, int ChemMarks, int MathMarks) {
        this.StudentID = StudentID;
        this.Name = Name;
        this.PhyMarks = PhyMarks;
        this.ChemMarks = ChemMarks;
        this.MathMarks = MathMarks;
    }
  /*Following will only output 0 because the value are integers not float*/
    public void displaydata() {
        System.out.println("\n\n");
        System.out.println("Student ID :" + StudentID);
        System.out.println("Name       :" + Name);
        System.out.println("PhyMarks   :" + PhyMarks/100);
        System.out.println("ChemMarks  :" + ChemMarks/100);
        System.out.println("MathMarks  :" + MathMarks/100);
        System.out.println("Average    :" + ((PhyMarks+ChemMarks+MathMarks)/300));
    }
}
