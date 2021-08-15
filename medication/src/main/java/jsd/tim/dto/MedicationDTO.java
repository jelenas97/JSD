package jsd.tim.dto;

import java.util.*;
import jsd.tim.model.*;

public class MedicationDTO extends Medication {
      private long id;
      private String name;
      private String code;

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

      public String getCode(){
        return this.code;
      }

      public void setCode(String code){
        this.code = code;
      }

}
