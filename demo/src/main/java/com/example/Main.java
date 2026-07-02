package com.example;

import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        if (args.length > 0 && "--console".equalsIgnoreCase(args[0])) {
            new ConsoleStudentApp().run();
        } else {
            SwingUtilities.invokeLater(() -> new StudentGuiApp().showWindow());
        }
    }
}
