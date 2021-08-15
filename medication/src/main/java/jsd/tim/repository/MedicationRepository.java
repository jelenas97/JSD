package jsd.tim.repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import jsd.tim.model.Medication;

@Repository
public interface MedicationRepository extends JpaRepository<Medication, Long> {
    Medication update(Medication medication);
}
