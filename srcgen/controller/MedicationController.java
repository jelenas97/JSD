package srcgen.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import java.util.Collection;
import java.util.List;

import srcgen.model.Medication;
import srcgen.dto.MedicationDTO;
import srcgen.service.MedicationService;

@Controller
@RequestMapping("/medication")
public class MedicationController{

	@Autowired
	private MedicationService medicationService;

  @GetMapping(value = "/new")
	public String create(Model model) {
		initModel(model);
		return "MedicationForm";
  }
  
  @PostMapping
  public ResponseEntity<Medication> save(@RequestBody MedicationDTO medication){
    try {
        medicationService.save(medication);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    catch(Exception e){
        return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }    
  }

  @PutMapping(value = "/{id}")
  public ResponseEntity<?> update(@PathVariable Long id, @RequestBody MedicationDTO medication) {
    try {
        medicationService.update(medication);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    catch (Exception e){
        return new ResponseEntity<>(e.getStackTrace(), HttpStatus.BAD_REQUEST);
    }
  }

  @DeleteMapping(value="/{id}")
  public ResponseEntity<Medication> delete(@PathVariable Long id) {
    Medication medication = medicationService.getById(id);
    try {
      medicationService.delete(medication);
      return new ResponseEntity<>(medication, HttpStatus.OK);
    }
    catch(Exception e) {
          return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

  @GetMapping(value = "/{id}")
  public ResponseEntity<MedicationDTO> getById(@PathVariable Long id){
    try {
        MedicationDTO medication = medicationService.getById(id);
        return new ResponseEntity<>(medication);
    }
    catch(Exception e){
        return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }    
  }

  @GetMapping
  public String getAll(Model model) {
    initModel(model);
    return "MedicationListView";
  }

  private void initModel(Model model) {
    model.addAttribute("Medication", new Medication());
    model.addAttribute("MedicationList", MedicationService.getAll());
  }
}
