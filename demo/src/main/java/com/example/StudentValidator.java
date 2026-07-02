package com.example;

import java.util.regex.Pattern;

public class StudentValidator {
    private static final Pattern PHONE_PATTERN = Pattern.compile("^\\+?[0-9\\-\\s]{7,20}$");
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");

    public boolean isValidPhone(String phone) {
        return PHONE_PATTERN.matcher(phone).matches();
    }

    public boolean isValidEmail(String email) {
        return EMAIL_PATTERN.matcher(email).matches();
    }

    public boolean isValidInput(String value) {
        return value != null && !value.trim().isEmpty();
    }
}
