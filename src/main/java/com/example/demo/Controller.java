package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@Component
public class Controller {

    @Autowired
    Jdbc jdbc = new Jdbc();
    @PostMapping("/alarm/{signal}")
    public void insertIntoDatabase(@PathVariable String signal){
         jdbc.insertIntoDatabase(signal.equals("True"));
     }
     @GetMapping("/alarm")
    public String getSignale() {
          return jdbc.getFromDatabase() ? "True" : "False";
     }
}
