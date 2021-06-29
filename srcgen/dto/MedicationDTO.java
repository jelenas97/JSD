package srcgen.dto;

import java.util.*;
import srcgen.model.*;

public class MedicationDTO extends Medication {
      private long id;
      private String name;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
      }

      public String getName(){
        return this.name;
      }

      public void setName(String name){
        this.name = name;
      }

}
