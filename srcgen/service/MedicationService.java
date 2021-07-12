package srcgen.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Collection;

import srcgen.service.MedicationService;
import srcgen.model.Medication;
import srcgen.repository.MedicationRepository;


@Service
public class MedicationServiceImpl implements MedicationService {

	@Autowired
	private MedicationRepository medicationRepository;

  @Override
  public Medication getById(long id) {
      return medicationRepository.getOne(id);
  }

  @Override
  public Collection<Medication> getAll() {
      return medicationRepository.findAll();
  }

}
