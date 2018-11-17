package boxing;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;

import java.awt.*;
import java.util.Timer;
import java.util.TimerTask;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

/**
 * Controller.java
 * A Controller that takes keyboard inputs and interfaces with BoxerView and Boxer
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Controller implements EventHandler<KeyEvent> {
    @FXML private Label leftHealth;
    @FXML private Label rightHealth;
    @FXML private Label leftEnergy;
    @FXML private Label rightEnergy;
    @FXML private ImageView rightImageView;
    @FXML private ImageView leftImageView;
    @FXML private ImageView background;

    private Boxer boxerLeft;
    private Boxer boxerRight;
    private Timer timer;
    final private double FRAMES_PER_SECOND = 5.0;

    /**
     * Initializes controller
     */
    public Controller() {
        this.startTimer();
    }

    /**
     * Helper method that updates view
     */
    private void updateView() {
        this.leftHealth.setText(String.format("Health: %d", this.boxerLeft.getHealth()));
        this.rightHealth.setText(String.format("Health: %d", this.boxerRight.getHealth()));
        this.leftEnergy.setText(String.format("Energy: %d", this.boxerLeft.getEnergy()));
        this.rightEnergy.setText(String.format("Energy: %d", this.boxerRight.getEnergy()));


        Image leftImg = new Image("file:"+boxerLeft.getImage());
        this.leftImageView.setImage(leftImg);
        this.leftImageView.setX(15*boxerLeft.getPosition());
        this.leftImageView.setY(90);
        this.leftImageView.setFitHeight(2*leftImg.getHeight());
        this.leftImageView.setFitWidth(2*leftImg.getWidth());

        Image rightImg = new Image("file:"+boxerRight.getImage());
        this.rightImageView.setImage(rightImg);
        this.rightImageView.setX(15*boxerRight.getPosition());
        this.rightImageView.setY(90);
        if(rightImg.getWidth() == 75){
            this.rightImageView.setX(15*(boxerRight.getPosition()-4));
        }
        this.rightImageView.setFitHeight(2*rightImg.getHeight());
        this.rightImageView.setFitWidth(2*rightImg.getWidth());


    }

    /**
     * Calls the appropriate methods at different key events from the user
     *
     * @param keyEvent key pressed by user
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();

        if (code == KeyCode.A){
            boxerLeft.setBlockingFalse();
            boxerLeft.move(-1);
        }
        if (code == KeyCode.D){
            boxerLeft.setBlockingFalse();
            boxerLeft.move(1);
        }
        if (code == KeyCode.LEFT){
            boxerRight.setBlockingFalse();
            boxerRight.move(-1);
        }
        if (code == KeyCode.RIGHT){
            boxerRight.setBlockingFalse();
            boxerRight.move(1);
        }
        if (code == KeyCode.DIGIT1){
            boxerLeft.punch();
        }
        if (code == KeyCode.K){
            boxerRight.punch();
        }
        if (code == KeyCode.DIGIT2){
            boxerLeft.block();
        }
        if (code == KeyCode.L){
            boxerRight.block();
        }

    }

    public void initialize() {
        this.boxerLeft = new Boxer(false,5,5);
        this.boxerRight = new Boxer(true,70,5);

        this.boxerLeft.addOpponent(this.boxerRight);
        this.boxerRight.addOpponent(this.boxerLeft);

        this.updateView();
        Image backgroundImage = new Image("file:"+"assets/background.png");
        this.background.setImage(backgroundImage);
        this.background.setFitWidth(1200);
        this.background.setFitHeight(290);

    }

    private void startTimer() {
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                Platform.runLater(new Runnable() {
                    public void run() {
                        updateState();
                    }
                });
            }
        };

        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }

    private void updateState() {
        this.updateView();
        if(!boxerLeft.isBlocking()) {
            this.boxerLeft.addEnergy(1);
        }
        if(!boxerRight.isBlocking()){
            this.boxerRight.addEnergy(1);
        }

    }
}
