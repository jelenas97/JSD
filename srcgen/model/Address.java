import javax.persistence.*;
import java.util.*;

@Entity
@Table
public class Address {

  @Id
  @GeneratedValue(strategy=GenerationType.IDENTITY)
  private long id;

  @Column
  private String street;

  @Column
  private String city;

  @Column
  private String country;

  public long getId(){
    return this.id;
  }

  public void setId(long new_value){
    this.id = new_value;
  }

  public String getStreet(){
    return this.street;
  }

  public void setStreet(String new_value){
    this.street = new_value;
  }

  public String getCity(){
    return this.city;
  }

  public void setCity(String new_value){
    this.city = new_value;
  }

  public String getCountry(){
    return this.country;
  }

  public void setCountry(String new_value){
    this.country = new_value;
  }

}
