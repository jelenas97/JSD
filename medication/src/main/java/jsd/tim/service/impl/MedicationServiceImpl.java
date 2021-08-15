package jsd.tim.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jsd.tim.service.MedicationService;
import jsd.tim.model.*;
import jsd.tim.repository.MedicationRepository;


@Service
public class MedicationServiceImpl implements MedicationService {

	@Autowired
	private MedicationRepository medicationRepository;

  @Override
  public Medication save(Medication medication) {
      return medicationRepository.save(medication);
  }

  @Override
  public Medication update(Medication medication) {
      return medicationRepository.update(medication);
  }

  @Override
  public void delete(Medication medication) {
      medicationRepository.delete(medication);
  }

  @Override
  public Medication getById(Long id) {
      return medicationRepository.getOne(id);
  }

  @Override
  public List<Medication> getAll() {
      return medicationRepository.findAll();
  }

}
