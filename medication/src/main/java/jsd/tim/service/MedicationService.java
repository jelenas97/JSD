package jsd.tim.service;

import java.util.*;
import jsd.tim.model.*;
import org.springframework.stereotype.Service;

@Service
public interface MedicationService {

    Medication getById(Long id);
    List<Medication> getAll();
    Medication save(Medication medication);
    Medication update(Medication medication);
    void delete(Medication medication);

}
