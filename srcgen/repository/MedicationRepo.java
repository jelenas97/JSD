import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import model.Medication;

@Repository
public interface MedicationRepository extends JpaRepository<Medication, Long> {
}