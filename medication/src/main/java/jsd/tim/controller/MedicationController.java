package jsd.tim.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.ui.Model;
import java.util.Collection;
import java.util.List;

import jsd.tim.model.Medication;
import jsd.tim.dto.MedicationDTO;
import jsd.tim.service.MedicationService;

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
    public String save(@ModelAttribute Medication medication, Model model){
        medicationService.save(medication);
        initModel(model);
        return "MedicationView";
    }

    @GetMapping(value = "/update/{id}")
    public String update(Model model, @PathVariable Long id) {
        setModel(model, id);
        Medication medication = medicationService.getById(id);
        medicationService.delete(medication);
        return "MedicationUpdateForm";
    }

    @PostMapping(value = "/update")
    public String update(@ModelAttribute Medication medication, Model model) {
        medicationService.update(medication);
        initModel(model);
        return "MedicationView";
    }

    @GetMapping(value="/delete/{id}")
    public String delete(@PathVariable Long id, Model model) {
        Medication medication = medicationService.getById(id);
        medicationService.delete(medication);
        initModel(model);
        return "MedicationView";
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Medication> getById(@PathVariable Long id){
        try {
            Medication medication = medicationService.getById(id);
            return new ResponseEntity<>(medication, HttpStatus.OK);
    }
    catch(Exception e){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping
    public String getAll(Model model) {
        initModel(model);
        return "MedicationView";
    }

    private void initModel(Model model) {
        model.addAttribute("medication", new MedicationDTO());
        model.addAttribute("MedicationList", medicationService.getAll());
    }

    private void setModel(Model model, Long id) {
        MedicationDTO toUpdate = new MedicationDTO();
        toUpdate.setId(id);
        model.addAttribute("medication", toUpdate);
    }
}
