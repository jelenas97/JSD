package jsd.tim.dto;

import java.util.*;
import jsd.tim.model.*;

public class MedicationDTO extends Medication {
      private long id;
      private String code;
      private String name;
      private String type;
      private String description;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
      }

      public String getCode(){
        return this.code;
      }

      public void setCode(String code){
        this.code = code;
      }

      public String getName(){
        return this.name;
      }

      public void setName(String name){
        this.name = name;
      }

      public String getType(){
        return this.type;
      }

      public void setType(String type){
        this.type = type;
      }

      public String getDescription(){
        return this.description;
      }

      public void setDescription(String description){
        this.description = description;
      }

}
