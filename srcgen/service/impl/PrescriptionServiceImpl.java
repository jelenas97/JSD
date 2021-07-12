package srcgen.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Collection;

import srcgen.service.PrescriptionService;
import srcgen.model.Prescription;
import srcgen.repository.PrescriptionRepository;


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
  public Prescription delete(Prescription prescription) {
      prescriptionRepository.delete(prescription);
  }

  @Override
  public void updateValidity() {
      return;
  }

  @Override
  public void addMedication() {
      return;
  }

  @Override
  public void removeMedication() {
      return;
  }

}
