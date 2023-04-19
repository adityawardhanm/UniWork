import javax.swing.*;

public class Registration {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Registration Form");
        JLabel fnameLabel = new JLabel("First Name:");
        JTextField fnameField = new JTextField(30);
        JLabel lnameLabel = new JLabel("Last Name:");
        JTextField lnameField = new JTextField(30);
        JCheckBox subscribeCheckbox = new JCheckBox("Do you suffer from any stress?\n If yes subscribe to our newsletter");

        // Radio buttons
        JLabel genderLabel = new JLabel("Gender:");
        JRadioButton maleRadioButton = new JRadioButton("Male");
        JRadioButton femaleRadioButton = new JRadioButton("Female");
        JRadioButton transRadioButton = new JRadioButton("Rather not say");
        ButtonGroup genderButtonGroup = new ButtonGroup();
        genderButtonGroup.add(maleRadioButton);
        genderButtonGroup.add(femaleRadioButton);
        genderButtonGroup.add(transRadioButton);

        // Dropdown
        JLabel AgeLabel = new JLabel("Age:");
        String[] age = {"14-19", "19-25", "25-35", ">35"};
        JComboBox<String> ageComboBox = new JComboBox<>(age);

        JButton registerButton = new JButton("Register");

        JPanel panel = new JPanel();
        panel.add(fnameLabel);
        panel.add(fnameField);
        panel.add(lnameLabel);
        panel.add(lnameField);
        panel.add(subscribeCheckbox);
        panel.add(genderLabel);
        panel.add(maleRadioButton);
        panel.add(femaleRadioButton);
        panel.add(transRadioButton);
        panel.add(AgeLabel);
        panel.add(ageComboBox);
        panel.add(registerButton);

        frame.add(panel);
        frame.setSize(400, 300);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
