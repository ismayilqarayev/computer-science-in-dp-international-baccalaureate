package com.example;

public class GraduateStudent extends Student {
    private String university;

    public GraduateStudent(String name, String surname, String phoneNumber, String email, String university) {
        super(name, surname, phoneNumber, email);
        this.university = university;
    }

    public String getUniversity() {
        return university;
    }

    @Override
    public void showInfo() {
        System.out.println("Name: " + getName() + " " + getSurname());
        System.out.println("Phone: " + getPhoneNumber());
        System.out.println("Email: " + getEmail());
        System.out.println("University: " + university);
    }
}
