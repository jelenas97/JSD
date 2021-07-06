package srcgen.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import java.util.Collection;
import java.util.List;

import srcgen.model.Prescription;
import srcgen.dto.PrescriptionDTO;
import srcgen.service.PrescriptionService;

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
  public ResponseEntity<Prescription> save(@RequestBody PrescriptionDTO prescription){
    try {
        prescriptionService.save(prescription);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    catch(Exception e){
        return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }    
  }

  @PutMapping(value = "/{id}")
  public ResponseEntity<?> update(@PathVariable Long id, @RequestBody PrescriptionDTO prescription) {
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

  private void initModel(Model model) {
    model.addAttribute("Prescription", new Prescription());
    model.addAttribute("PrescriptionList", PrescriptionService.getAll());
  }
}
