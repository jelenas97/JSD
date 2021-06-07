import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import model.Address;

@Repository
public interface AddressRepository extends JpaRepository<Address, Long> {
}