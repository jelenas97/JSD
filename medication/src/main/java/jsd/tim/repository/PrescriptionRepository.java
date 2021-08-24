package jsd.tim.repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import jsd.tim.model.Prescription;

@Repository
public interface PrescriptionRepository extends JpaRepository<Prescription, Long> {
}
