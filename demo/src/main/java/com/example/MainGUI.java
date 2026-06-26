package com.example;



import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

public class MainGUI extends Application {

    private static final String BG      = "#0f1117";
    private static final String PANEL   = "#1a1d27";
    private static final String ACCENT  = "#4f8ef7";
    private static final String ACCENT2 = "#7c3aed";
    private static final String TEXT    = "#e8eaf0";
    private static final String SUBTEXT = "#8b90a0";
    private static final String BORDER  = "#2a2d3e";
    private static final String SUCCESS = "#22c55e";
    private static final String ERROR   = "#ef4444";

    @Override
    public void start(Stage stage) {
        stage.setTitle("Student Information System");

        TabPane tabPane = new TabPane();
        tabPane.setTabClosingPolicy(TabPane.TabClosingPolicy.UNAVAILABLE);

        Tab gradTab = new Tab("🎓  Graduate Student", buildGraduateTab());
        Tab phdTab  = new Tab("🔬  PhD Student",      buildPhDTab());
        tabPane.getTabs().addAll(gradTab, phdTab);

        Label title = new Label("Student Information System");
        title.setFont(Font.font("Segoe UI", FontWeight.BOLD, 22));
        title.setTextFill(Color.web(TEXT));

        Label sub = new Label("Enter student details below");
        sub.setFont(Font.font("Segoe UI", 13));
        sub.setTextFill(Color.web(SUBTEXT));

        VBox header = new VBox(4, title, sub);
        header.setPadding(new Insets(24, 28, 12, 28));
        header.setStyle("-fx-background-color:" + BG + ";");

        VBox root = new VBox(header, tabPane);
        root.setStyle("-fx-background-color:" + BG + ";");

        Scene scene = new Scene(root, 560, 640);
        scene.getStylesheets().add(css());
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
    }

    // ── Graduate tab ──────────────────────────────────────────────────────────
    private VBox buildGraduateTab() {
        TextField tfName  = field("Ali");
        TextField tfSur   = field("Həsənov");
        TextField tfPhone = field("+994 50 123 45 67");
        TextField tfEmail = field("ali@example.com");
        TextField tfUni   = field("Bakı Dövlət Universiteti");

        Label result = resultLabel();
        Button btn   = submitBtn("Add Graduate Student");

        btn.setOnAction(e -> {
            String err = validateBase(tfName, tfSur, tfPhone, tfEmail);
            if (err != null)               { showError(result, err); return; }
            if (tfUni.getText().isBlank()) { showError(result, "University field is required."); return; }

            // ── Main.java-dakı GraduateStudent sinifi çağırılır ──
            GraduateStudent student = new GraduateStudent(
                tfName.getText().trim(),
                tfSur.getText().trim(),
                tfPhone.getText().trim(),
                tfEmail.getText().trim(),
                tfUni.getText().trim()
            );

            // showInfo() nəticəsi GUI-də göstərilir
            showSuccess(result, student.showInfo());
        });

        return formPane(
            row("First Name", tfName),
            row("Last Name",  tfSur),
            row("Phone",      tfPhone),
            row("Email",      tfEmail),
            row("University", tfUni),
            btn, result
        );
    }

    // ── PhD tab ───────────────────────────────────────────────────────────────
    private VBox buildPhDTab() {
        TextField tfName     = field("Leyla");
        TextField tfSur      = field("Məmmədova");
        TextField tfPhone    = field("+994 55 987 65 43");
        TextField tfEmail    = field("leyla@example.com");
        TextField tfUni      = field("ADNSU");
        TextField tfResearch = field("Artificial Intelligence in Education");

        Label result = resultLabel();
        Button btn   = submitBtn("Add PhD Student");

        btn.setOnAction(e -> {
            String err = validateBase(tfName, tfSur, tfPhone, tfEmail);
            if (err != null)                    { showError(result, err); return; }
            if (tfUni.getText().isBlank())      { showError(result, "University field is required."); return; }
            if (tfResearch.getText().isBlank()) { showError(result, "Research topic is required."); return; }

            // ── Main.java-dakı PhDStudent sinifi çağırılır ──
            PhDStudent student = new PhDStudent(
                tfName.getText().trim(),
                tfSur.getText().trim(),
                tfPhone.getText().trim(),
                tfEmail.getText().trim(),
                tfUni.getText().trim(),
                tfResearch.getText().trim()
            );

            // showInfo() nəticəsi GUI-də göstərilir
            showSuccess(result, student.showInfo());
        });

        return formPane(
            row("First Name",     tfName),
            row("Last Name",      tfSur),
            row("Phone",          tfPhone),
            row("Email",          tfEmail),
            row("University",     tfUni),
            row("Research Topic", tfResearch),
            btn, result
        );
    }

    // ── Yardımçı metodlar ─────────────────────────────────────────────────────

    private VBox formPane(javafx.scene.Node... nodes) {
        VBox box = new VBox(14);
        box.setPadding(new Insets(20, 28, 28, 28));
        box.setStyle("-fx-background-color:" + BG + ";");
        box.getChildren().addAll(nodes);
        return box;
    }

    private VBox row(String label, TextField tf) {
        Label lbl = new Label(label);
        lbl.setFont(Font.font("Segoe UI", FontWeight.SEMI_BOLD, 12));
        lbl.setTextFill(Color.web(SUBTEXT));
        return new VBox(5, lbl, tf);
    }

    private TextField field(String prompt) {
        TextField tf = new TextField();
        tf.setPromptText(prompt);
        tf.getStyleClass().add("my-field");
        return tf;
    }

    private Button submitBtn(String text) {
        Button b = new Button(text);
        b.getStyleClass().add("submit-btn");
        b.setMaxWidth(Double.MAX_VALUE);
        return b;
    }

    private Label resultLabel() {
        Label l = new Label();
        l.setWrapText(true);
        l.setFont(Font.font("Monospaced", 12));
        l.setPadding(new Insets(12));
        l.setMaxWidth(Double.MAX_VALUE);
        l.setVisible(false);
        return l;
    }

    private void showSuccess(Label lbl, String text) {
        lbl.setText("✅  " + text.replace("\n", "\n    "));
        lbl.setTextFill(Color.web(SUCCESS));
        lbl.setStyle("-fx-background-color:#0d2818; -fx-background-radius:8;" +
                     "-fx-border-color:#22c55e44; -fx-border-radius:8;");
        lbl.setVisible(true);
    }

    private void showError(Label lbl, String text) {
        lbl.setText("⚠️  " + text);
        lbl.setTextFill(Color.web(ERROR));
        lbl.setStyle("-fx-background-color:#2a0a0a; -fx-background-radius:8;" +
                     "-fx-border-color:#ef444444; -fx-border-radius:8;");
        lbl.setVisible(true);
    }

    private String validateBase(TextField name, TextField sur, TextField phone, TextField email) {
        if (name.getText().isBlank())  return "First name is required.";
        if (sur.getText().isBlank())   return "Last name is required.";
        if (!phone.getText().trim().matches("^\\+?[0-9\\-\\s]{7,20}$"))
            return "Invalid phone number. Example: +994 50 123 45 67";
        if (!email.getText().trim().matches("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$"))
            return "Invalid email format. Example: user@example.com";
        return null;
    }

    private String css() {
        String css =
            ".tab-pane { -fx-background-color:" + BG + "; }" +
            ".tab-pane .tab-header-area { -fx-background-color:" + PANEL + "; -fx-padding:4 0 0 4; }" +
            ".tab-pane .tab { -fx-background-color:" + PANEL + "; -fx-padding:8 18; }" +
            ".tab-pane .tab .tab-label { -fx-text-fill:" + SUBTEXT + "; -fx-font-size:13px; }" +
            ".tab-pane .tab:selected { -fx-background-color:" + BG + "; }" +
            ".tab-pane .tab:selected .tab-label { -fx-text-fill:" + TEXT + "; }" +
            ".my-field { -fx-background-color:" + PANEL + "; -fx-text-fill:" + TEXT + ";" +
            "  -fx-prompt-text-fill:" + BORDER + "; -fx-border-color:" + BORDER + ";" +
            "  -fx-border-radius:8; -fx-background-radius:8; -fx-padding:9 12; -fx-font-size:13px; }" +
            ".my-field:focused { -fx-border-color:" + ACCENT + "; }" +
            ".submit-btn { -fx-background-color:linear-gradient(to right," + ACCENT + "," + ACCENT2 + ");" +
            "  -fx-text-fill:white; -fx-font-size:13px; -fx-font-weight:bold;" +
            "  -fx-padding:11 0; -fx-background-radius:8; -fx-cursor:hand; }" +
            ".submit-btn:hover { -fx-opacity:0.88; }";
        try {
            java.io.File f = java.io.File.createTempFile("sis_style", ".css");
            f.deleteOnExit();
            java.nio.file.Files.writeString(f.toPath(), css);
            return f.toURI().toString();
        } catch (Exception ex) { return ""; }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
