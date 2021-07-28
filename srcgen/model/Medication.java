package srcgen.model;

import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Medication {
      @Id
      @GeneratedValue(strategy=GenerationType.IDENTITY)
      private long id;

      @Column
      private String name;

      @Column
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
