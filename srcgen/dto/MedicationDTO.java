package srcgen.model;

import java.util.*;


public class MedicationDTO {
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
