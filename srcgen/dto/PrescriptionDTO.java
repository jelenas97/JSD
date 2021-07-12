package srcgen.dto;

import java.util.*;
import srcgen.model.*;

public class PrescriptionDTO extends Prescription {
      private long id;
      private boolean valid;
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
