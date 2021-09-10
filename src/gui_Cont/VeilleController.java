/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gui_Cont;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.time.LocalDate;
import java.util.ResourceBundle;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.ComboBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import java.io.*;
import java.nio.charset.StandardCharsets;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TextField;

/**
 * FXML Controller class
 *
 * @author hiba
 */
public class VeilleController implements Initializable {

    @FXML
    private ComboBox<String> destination;
    @FXML
    private DatePicker dateDep;
    @FXML
    private DatePicker dateArr;
    @FXML
    private Label lblDestination;
    @FXML
    private Label lblDateDep;
    @FXML
    private Label lblDateArr;
    String date_depart;
    String date_arrive;
    String villeDestination;
    @FXML
    private AnchorPane Home;
    @FXML
    private TextField nomFichier;
    String Fichier ;


    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {

        addVille();
        dateDep.setValue(LocalDate.now());

        lblDestination.textProperty().bind(destination.getSelectionModel().selectedItemProperty());
        lblDateDep.textProperty().bind(dateDep.getEditor().textProperty());
        lblDateArr.textProperty().bind(dateArr.getEditor().textProperty());
        choisirDestination();
        choisirDateDepart();
        choisirDateDep();
        choisirDateArr();
       

    }

    public void addVille() {
        destination.getItems().add("Hammamet");
        destination.getItems().add("Tabarka");
        destination.getItems().add("Sousse");
        destination.getItems().add("Mahdia");
        destination.getItems().add("Monastir");
        destination.getItems().add("Djerba");
        destination.getItems().add("Tozeur");
        destination.getItems().add("Kelibia");
        destination.getItems().add("Sfax");
        destination.getItems().add("Tunis");
        destination.getItems().add("Douz");
        destination.getItems().add("Bizerte");
        destination.getItems().add("Ain Draham");
        destination.getItems().add("El Jem");
        destination.getItems().add("Gammarth");
        destination.getItems().add("Zarzis");
        destination.getItems().add("Kairouan");
        destination.getItems().add("Nabeul");
    }

    public void choisirDestination() {
        destination.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<String>() {

            @Override
            public void changed(ObservableValue<? extends String> selected, String oldDest, String newDest) {
                villeDestination = newDest;
                System.out.println("hehdi ville"+villeDestination);

            }
        });

    }
    public void choisirDateDep(){
     
             dateDep.getEditor().textProperty().addListener((o,oldValue,newValue) -> {
                  date_depart=newValue;
                  System.out.println("hedhi date dep"+date_depart);
             });
         
    
    }
       public void choisirDateArr(){
     
             dateArr.getEditor().textProperty().addListener((o,oldValue,newValue) -> {
                  date_arrive=newValue;
                  System.out.println("hedhi date arrive "+date_arrive);
             });
         
    
    }

    public String choisirDateDepart() {

        dateDep.valueProperty().addListener((ov, oldDate, newDate) -> {
            dateArr.setValue(newDate.plusDays(1));
            date_depart = dateDep.getValue().toString();
        }
        );
        return date_depart;
    }

  
 
    public class ScriptPython{
        Process mProcess;
    

    public void runScript (){

        Process process;
        try {
                     Fichier= nomFichier.getText();

            process= Runtime.getRuntime().exec(new String []{"python","C:\\veilleApp\\Travel.py",villeDestination,date_depart,date_arrive,Fichier});
            System.out.println(villeDestination);
            mProcess = process;
            System.out.println("done process");
        }catch(Exception e){
            System.out.println("Exception"+e.toString());
        }
        
        InputStream stdout = mProcess.getInputStream();
        BufferedReader reader = new BufferedReader (new InputStreamReader(stdout,StandardCharsets.UTF_8));
        
    }
    }
    public void test(){
        ScriptPython scriptPython = new ScriptPython();
        scriptPython.runScript();
    }
      
    
  @FXML
    private void confirmer(ActionEvent event) {
                   Fichier= nomFichier.getText();

                if (dateArr.getValue()==null){
            Alert alert = new Alert(AlertType.ERROR);
 
            alert.setTitle("Erreur Date Arrivée");
            alert.setContentText("Champ Date Arrivée ne peux pas être vide!");
 
            alert.showAndWait();
        }
             if (destination==null){
            Alert alert = new Alert(AlertType.ERROR);
 
            alert.setTitle("Erreur Destination");
            alert.setContentText("Champ Destination ne peux pas être vide! ");
 
            alert.showAndWait();
        }
                
               if (Fichier==null){
            Alert alert = new Alert(AlertType.ERROR);
 
            alert.setTitle("Erreur Nom fichier excel");
            alert.setContentText("Merci de donnez un nom à votre fichier ça va vous faciliter la recherche ! ");
 
            alert.showAndWait();
        }  
              test();
                
    }

    
@FXML
    private void finish(ActionEvent event) throws IOException {
       
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/gui_Cont/finish.fxml"));
        Node node = loader.load();
        Home.getChildren().add(node);

    }
}
