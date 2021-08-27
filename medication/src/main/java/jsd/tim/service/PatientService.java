package jsd.tim.service;

import java.util.*;
import jsd.tim.model.*;
import org.springframework.stereotype.Service;

@Service
public interface PatientService {

    Patient getById(Long id);
    List<Patient> getAll();
    Patient save(Patient patient);
    Patient update(Patient patient);
    void delete(Patient patient);

}
