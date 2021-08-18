package jsd.tim.service;

import java.util.*;
import jsd.tim.model.*;
import org.springframework.stereotype.Service;

@Service
public interface PrescriptionService {

    Prescription getById(Long id);
    List<Prescription> getAll();
    boolean updateValidity(Long id);
    boolean addMedication(Medication medication);
    boolean removeMedication(Long id);
    Prescription save(Prescription prescription);
    Prescription update(Prescription prescription);
    void delete(Prescription prescription);

}
