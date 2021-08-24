package jsd.tim.repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import jsd.tim.model.Patient;

@Repository
public interface PatientRepository extends JpaRepository<Patient, Long> {
}
