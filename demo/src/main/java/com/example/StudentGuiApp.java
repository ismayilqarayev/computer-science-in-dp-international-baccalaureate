package com.example;

import javax.swing.*;
import java.awt.*;
import java.util.LinkedHashMap;
import java.util.Map;

public class StudentGuiApp {
    private final StudentValidator validator = new StudentValidator();

    public void showWindow() {
        JFrame frame = new JFrame("Student Information System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(700, 650);
        frame.setLocationRelativeTo(null);

        JTabbedPane tabs = new JTabbedPane();
        tabs.addTab("Graduate Student", createGraduatePanel());
        tabs.addTab("PhD Student", createPhDPanel());

        frame.add(tabs);
        frame.setVisible(true);
    }

    private JPanel createGraduatePanel() {
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(6, 6, 6, 6);
        gbc.anchor = GridBagConstraints.WEST;

        Map<String, JTextField> fields = new LinkedHashMap<>();
        String[] labels = {"Name", "Surname", "Phone", "Email", "University"};
        for (int i = 0; i < labels.length; i++) {
            JLabel label = new JLabel(labels[i]);
            JTextField field = new JTextField(28);
            gbc.gridx = 0;
            gbc.gridy = i;
            panel.add(label, gbc);
            gbc.gridx = 1;
            panel.add(field, gbc);
            fields.put(labels[i], field);
        }

        JTextArea resultArea = new JTextArea(10, 36);
        resultArea.setLineWrap(true);
        resultArea.setWrapStyleWord(true);

        JButton button = new JButton("Show Graduate Student");
        button.addActionListener(e -> showGraduateResult(fields, resultArea));

        gbc.gridx = 0;
        gbc.gridy = labels.length;
        gbc.gridwidth = 2;
        panel.add(button, gbc);

        gbc.gridy = labels.length + 1;
        panel.add(new JScrollPane(resultArea), gbc);
        return panel;
    }

    private JPanel createPhDPanel() {
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(6, 6, 6, 6);
        gbc.anchor = GridBagConstraints.WEST;

        Map<String, JTextField> fields = new LinkedHashMap<>();
        String[] labels = {"Name", "Surname", "Phone", "Email", "University", "Research Topic"};
        for (int i = 0; i < labels.length; i++) {
            JLabel label = new JLabel(labels[i]);
            JTextField field = new JTextField(28);
            gbc.gridx = 0;
            gbc.gridy = i;
            panel.add(label, gbc);
            gbc.gridx = 1;
            panel.add(field, gbc);
            fields.put(labels[i], field);
        }

        JTextArea resultArea = new JTextArea(10, 36);
        resultArea.setLineWrap(true);
        resultArea.setWrapStyleWord(true);

        JButton button = new JButton("Show PhD Student");
        button.addActionListener(e -> showPhDResult(fields, resultArea));

        gbc.gridx = 0;
        gbc.gridy = labels.length;
        gbc.gridwidth = 2;
        panel.add(button, gbc);

        gbc.gridy = labels.length + 1;
        panel.add(new JScrollPane(resultArea), gbc);
        return panel;
    }

    private void showGraduateResult(Map<String, JTextField> fields, JTextArea resultArea) {
        Map<String, String> data = readValues(fields);
        if (!isValid(data)) {
            resultArea.setText("Please enter valid values.");
            return;
        }

        Student student = new GraduateStudent(
                data.get("Name"),
                data.get("Surname"),
                data.get("Phone"),
                data.get("Email"),
                data.get("University"));
        resultArea.setText(formatStudent(student));
    }

    private void showPhDResult(Map<String, JTextField> fields, JTextArea resultArea) {
        Map<String, String> data = readValues(fields);
        if (!isValid(data)) {
            resultArea.setText("Please enter valid values.");
            return;
        }

        Student student = new PhDStudent(
                data.get("Name"),
                data.get("Surname"),
                data.get("Phone"),
                data.get("Email"),
                data.get("University"),
                data.get("Research Topic"));
        resultArea.setText(formatStudent(student));
    }

    private boolean isValid(Map<String, String> data) {
        if (data.values().stream().anyMatch(value -> !validator.isValidInput(value))) {
            return false;
        }
        return validator.isValidPhone(data.get("Phone")) && validator.isValidEmail(data.get("Email"));
    }

    private String formatStudent(Student student) {
        return student instanceof PhDStudent
                ? "Name: " + student.getName() + " " + student.getSurname() + "\nPhone: " + student.getPhoneNumber() + "\nEmail: " + student.getEmail() + "\nUniversity: " + ((GraduateStudent) student).getUniversity() + "\nResearch Topic: " + ((PhDStudent) student).getResearchTopic()
                : "Name: " + student.getName() + " " + student.getSurname() + "\nPhone: " + student.getPhoneNumber() + "\nEmail: " + student.getEmail() + "\nUniversity: " + ((GraduateStudent) student).getUniversity();
    }

    private Map<String, String> readValues(Map<String, JTextField> fields) {
        Map<String, String> data = new LinkedHashMap<>();
        fields.forEach((key, field) -> data.put(key, field.getText().trim()));
        return data;
    }
}
