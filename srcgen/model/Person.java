import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Person {

  @Id
  @GeneratedValue(strategy=GenerationType.IDENTITY)
  private long id;

  @Column
  private String name;

  @Column
  private Address address;

  @Column
  private int age;

  public long getId(){
    return this.id;
  }

  public void setId(long new_value){
    this.id = new_value;
  }

  public String getName(){
    return this.name;
  }

  public void setName(String new_value){
    this.name = new_value;
  }

  public Address getAddress(){
    return this.address;
  }

  public void setAddress(Address new_value){
    this.address = new_value;
  }

  public int getAge(){
    return this.age;
  }

  public void setAge(int new_value){
    this.age = new_value;
  }

}
