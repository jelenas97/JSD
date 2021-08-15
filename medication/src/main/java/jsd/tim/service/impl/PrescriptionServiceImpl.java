package jsd.tim.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jsd.tim.service.PrescriptionService;
import jsd.tim.model.*;
import jsd.tim.repository.PrescriptionRepository;


@Service
public class PrescriptionServiceImpl implements PrescriptionService {

	@Autowired
	private PrescriptionRepository prescriptionRepository;

  @Override
  public Prescription save(Prescription prescription) {
      return prescriptionRepository.save(prescription);
  }

  @Override
  public Prescription update(Prescription prescription) {
      return prescriptionRepository.update(prescription);
  }

  @Override
  public void delete(Prescription prescription) {
      prescriptionRepository.delete(prescription);
  }

  @Override
  public Prescription getById(Long id) {
      return prescriptionRepository.getOne(id);
  }

  @Override
  public List<Prescription> getAll() {
      return prescriptionRepository.findAll();
  }

  @Override
  public  boolean updateValidity(Long id) {
      return true;
  }

  @Override
  public  boolean addMedication(Medication medication) {
      return true;
  }

  @Override
  public  boolean removeMedication(Long id) {
      return true;
  }

}
