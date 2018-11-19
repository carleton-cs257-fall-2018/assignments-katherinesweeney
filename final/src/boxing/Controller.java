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
import javafx.stage.WindowEvent;
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
    @FXML private Label restart;
    @FXML private ImageView rightImageView;
    @FXML private ImageView leftImageView;
    @FXML private ImageView background;

    private Boxer boxerLeft;
    private Boxer boxerRight;
    private Timer timer;
    private boolean isPaused;
    private boolean isOver = false;
    final private double FRAMES_PER_SECOND = 5.0;

    /**
     * Initializes controller
     */
    public Controller() {
        this.startTimer();
    }

    private void updateView() {
        this.leftHealth.setText(String.format("Health: %d", this.boxerLeft.getHealth()));
        this.rightHealth.setText(String.format("Health: %d", this.boxerRight.getHealth()));
        this.leftEnergy.setText(String.format("Energy: %d", this.boxerLeft.getEnergy()));
        this.rightEnergy.setText(String.format("Energy: %d", this.boxerRight.getEnergy()));

        this.addImage(boxerLeft, false, this.leftImageView);
        this.addImage(boxerRight, true, this.rightImageView);
    }

    private void addImage(Boxer boxer, boolean isRight, ImageView boxerImageView){
        Image img = new Image("file:"+boxer.getImage());
        boxerImageView.setImage(img);
        boxerImageView.setX(15*boxer.getPosition());
        if(isRight && img.getWidth() == 75){
            this.rightImageView.setX(15*(boxerRight.getPosition()-4));
        }
        boxerImageView.setY(90);
        boxerImageView.setFitHeight(2*img.getHeight());
        boxerImageView.setFitWidth(2*img.getWidth());
    }

    /**
     * Calls the appropriate methods at different key events from the user
     *
     * @param keyEvent key pressed by user
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();

        if(!this.isOver) {
            if (!this.isPaused) {
                if (code == KeyCode.A) {
                    boxerLeft.move(-1);
                }
                if (code == KeyCode.D) {
                    boxerLeft.move(1);
                }
                if (code == KeyCode.LEFT) {
                    boxerRight.move(-1);
                }
                if (code == KeyCode.RIGHT) {
                    boxerRight.move(1);
                }
                if (code == KeyCode.DIGIT1) {
                    boxerLeft.punch();
                }
                if (code == KeyCode.K) {
                    boxerRight.punch();
                }
                if (code == KeyCode.DIGIT2) {
                    boxerLeft.block();
                }
                if (code == KeyCode.L) {
                    boxerRight.block();
                }
                if (code == KeyCode.DIGIT3) {
                    boxerLeft.kick();
                }
                if (code == KeyCode.SEMICOLON) {
                    boxerRight.kick();
                }
            }
            if (code == KeyCode.SPACE) {
                if (this.isPaused == false) {
                    this.timer.cancel();
                    this.setBackground("assets/backgroundPaused.png");
                    this.isPaused = true;
                } else {
                    this.startTimer();
                    this.setBackground("assets/background.png");
                    this.isPaused = false;
                }
            }
        }
        else{
            if (code == KeyCode.R) {
                this.initialize();
                this.isOver = false;
                this.startTimer();
                this.restart.setText("Player 1: Move A D, Punch 1, Block 2, Kick 3 || Player 2: Move Left/Right Arrow, Punch K, Block L, Kick ; || Pause: Space");
            }
        }
    }

    /**
     * Initializes a game by creating the two boxers and setting the background
     */

    public void initialize() {
        this.boxerLeft = new Boxer(false,5,5);
        this.boxerRight = new Boxer(true,70,5);

        this.boxerLeft.addOpponent(this.boxerRight);
        this.boxerRight.addOpponent(this.boxerLeft);

        this.updateView();
        this.setBackground("assets/background.png");
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
        if(!this.isOver) {
            this.updateView();
            if (!boxerLeft.isBlocking()) {
                this.boxerLeft.addEnergy(1);
            }
            if (!boxerRight.isBlocking()) {
                this.boxerRight.addEnergy(1);
            }
            if (boxerRight.getHealth() < 1) {
                this.endGame("assets/backgroundPlayerWin.png");
            }
            else if (boxerLeft.getHealth() < 1) {
                this.endGame("assets/backgroundEnemyWin.png");
            }
        }
    }

    private void endGame(String victoryImagePath){
        this.timer.cancel();
        this.setBackground(victoryImagePath);
        this.isOver = true;
        this.restart.setText("Restart: R");
    }

    private void setBackground(String imagePath){
        Image backgroundImage = new Image("file:" + imagePath);
        this.background.setImage(backgroundImage);
        this.background.setFitWidth(1200);
        this.background.setFitHeight(290);
    }
}
