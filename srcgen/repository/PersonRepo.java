import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import model.Person;

@Repository
public interface PersonRepository extends JpaRepository<Person, Long> {
}