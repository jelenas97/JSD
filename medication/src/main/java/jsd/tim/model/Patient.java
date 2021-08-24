package jsd.tim.model;

import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Patient {
      @Id
      @GeneratedValue(strategy=GenerationType.IDENTITY)
      private long id;

      @Column
      private String firstName;

      @Column
      private String lastName;

      @Column
      private String city;

      @Column
      private String age;

      public long getId(){
        return this.id;
      }

      public void setId(long id){
        this.id = id;
      }

      public String getFirstname(){
        return this.firstName;
      }

      public void setFirstname(String firstName){
        this.firstName = firstName;
      }

      public String getLastname(){
        return this.lastName;
      }

      public void setLastname(String lastName){
        this.lastName = lastName;
      }

      public String getCity(){
        return this.city;
      }

      public void setCity(String city){
        this.city = city;
      }

      public String getAge(){
        return this.age;
      }

      public void setAge(String age){
        this.age = age;
      }

}
