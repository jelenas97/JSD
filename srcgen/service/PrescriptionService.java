package srcgen.service;

import java.util.*;
import srcgen.model.Prescription;
import org.springframework.stereotype.Service;

@Service
public interface PrescriptionService {

    bool updateValidity(Long id);

    bool addMedication(Medication medication);

    bool removeMedication(Long id);


}