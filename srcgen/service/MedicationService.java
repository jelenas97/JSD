package srcgen.service;

import java.util.*;
import srcgen.model.Medication;
import org.springframework.stereotype.Service;

@Service
public interface MedicationService {

    Medication getById(Long id);

    List<Medication> getAll();

    bool save(Medication medication);

    bool update(Long id);

    bool delete(Long id);


}