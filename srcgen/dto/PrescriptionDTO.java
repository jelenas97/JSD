package srcgen.model;

import java.util.*;


public class PrescriptionDTO {
      private long id;
      private bool valid;
      private List<MedicationDTO> medications;

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

      public List<MedicationDTO> getMedications(){
         return this.medications;
      }

      public void setMedications(List<MedicationDTO> medications){
         this.medications = medications;
      }

}
