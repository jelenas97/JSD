package jsd.tim.dto;

import java.util.*;
import jsd.tim.model.*;

public class PrescriptionDTO extends Prescription {
      private long id;
      private String title;
      private String doctor;
      private boolean valid;
      private List<Medication> medications;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
      }

      public String getTitle(){
        return this.title;
      }

      public void setTitle(String title){
        this.title = title;
      }

      public String getDoctor(){
        return this.doctor;
      }

      public void setDoctor(String doctor){
        this.doctor = doctor;
      }

      public boolean getValid(){
        return this.valid;
      }

      public void setValid(boolean valid){
        this.valid = valid;
      }

      public List<Medication> getMedications(){
         return this.medications;
      }

      public void setMedications(List<Medication> medications){
         this.medications = medications;
      }

}
