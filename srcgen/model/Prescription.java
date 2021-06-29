package srcgen.model;

import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Prescription {
      @Id
      @GeneratedValue(strategy=GenerationType.IDENTITY)
      private long id;

      @Column
      private boolean valid;

      @ManyToMany
      private List<Medication> medications;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
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
