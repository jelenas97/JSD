package jsd.tim.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import java.util.Collection;
import java.util.List;

import jsd.tim.model.Prescription;
import jsd.tim.dto.PrescriptionDTO;
import jsd.tim.service.PrescriptionService;

@Controller
@RequestMapping("/prescription")
public class PrescriptionController{

	@Autowired
	private PrescriptionService prescriptionService;

  @GetMapping(value = "/new")
	public String create(Model model) {
		initModel(model);
		return "PrescriptionForm";
  }
  
  @PostMapping
  public ResponseEntity<Prescription> save(@RequestBody Prescription prescription){
    try {
        prescriptionService.save(prescription);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    catch(Exception e){
        return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }    
  }

  @PutMapping(value = "/{id}")
  public ResponseEntity<?> update(@PathVariable Long id, @RequestBody Prescription prescription) {
    try {
        prescriptionService.update(prescription);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    catch (Exception e){
        return new ResponseEntity<>(e.getStackTrace(), HttpStatus.BAD_REQUEST);
    }
  }

  @DeleteMapping(value="/{id}")
  public ResponseEntity<Prescription> delete(@PathVariable Long id) {
    Prescription prescription = prescriptionService.getById(id);
    try {
      prescriptionService.delete(prescription);
      return new ResponseEntity<>(prescription, HttpStatus.OK);
    }
    catch(Exception e) {
          return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

  @GetMapping(value = "/{id}")
  public ResponseEntity<Prescription> getById(@PathVariable Long id){
    try {
        Prescription prescription = prescriptionService.getById(id);
        return new ResponseEntity<>(prescription, HttpStatus.OK);
    }
    catch(Exception e){
        return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }    
  }

  @GetMapping
  public String getAll(Model model) {
    initModel(model);
    return "PrescriptionListView";
  }

  private void initModel(Model model) {
    model.addAttribute("Prescription", new Prescription());
    model.addAttribute("PrescriptionList", prescriptionService.getAll());
  }
}
