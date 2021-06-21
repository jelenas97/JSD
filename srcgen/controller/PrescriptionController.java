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
import srcgen.service.PrescriptionService;

@Controller
@RequestMapping("/prescription")
public class PrescriptionController{

	@Autowired
	private PrescriptionService prescriptionService;

  private void initModel(Model model) {
    model.addAttribute("Prescription", new Prescription());
    model.addAttribute("PrescriptionList", PrescriptionService.getAll());
  }
}
