package jsd.tim.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import java.util.Collection;
import java.util.List;

import jsd.tim.model.Patient;
import jsd.tim.dto.PatientDTO;
import jsd.tim.service.PatientService;

@Controller
@RequestMapping("/patient")
public class PatientController{

    @Autowired
    private PatientService patientService;
    @GetMapping(value = "/{id}")
    public ResponseEntity<Patient> getById(@PathVariable Long id){
        try {
            Patient patient = patientService.getById(id);
            return new ResponseEntity<>(patient, HttpStatus.OK);
    }
    catch(Exception e){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping
    public String getAll(Model model) {
        initModel(model);
        return "PatientView";
    }

    private void initModel(Model model) {
        model.addAttribute("patient", new PatientDTO());
        model.addAttribute("PatientList", patientService.getAll());
    }
}
