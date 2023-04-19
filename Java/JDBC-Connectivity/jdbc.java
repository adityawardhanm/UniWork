import java.sql.*;
public class jdbc {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/students", "root", "root");
            Statement stat = con.createStatement();
            ResultSet result = stat.executeQuery("select * from students.table_name");
            while (result.next()) {
                System.out.println(result.getString(1)+" "+result.getString(2)+" "+result.getString(3));
            }
        }
        catch (Exception e){
            e.printStackTrace();
            }
    }
}
