import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Prescription {
      @Id
      @GeneratedValue(strategy=GenerationType.IDENTITY)
      private long id;

      @Column
      private bool valid;

      @ManyToMany
      private List<Medication> medications;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
      }

      public bool getValid(){
        return this.valid;
      }

      public void setValid(bool valid){
        this.valid = valid;
      }
      public List<Medication> getMedications(){
         return this.medications;
      }

      public void setMedications(List<Medication> medications){
         this.medications = medications;
      }

}
