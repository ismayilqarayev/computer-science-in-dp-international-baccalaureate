package com.example;

public class PhDStudent extends GraduateStudent {
    private String researchTopic;

    public PhDStudent(String name, String surname, String phoneNumber, String email, String university, String researchTopic) {
        super(name, surname, phoneNumber, email, university);
        this.researchTopic = researchTopic;
    }

    public String getResearchTopic() {
        return researchTopic;
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("Research Topic: " + researchTopic);
    }
}
