package jsd.tim.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jsd.tim.service.PatientService;
import jsd.tim.model.*;
import jsd.tim.repository.PatientRepository;


@Service
public class PatientServiceImpl implements PatientService {

	@Autowired
	private PatientRepository patientRepository;

  @Override
  public Patient getById(Long id) {
      return patientRepository.getOne(id);
  }

  @Override
  public List<Patient> getAll() {
      return patientRepository.findAll();
  }

}
