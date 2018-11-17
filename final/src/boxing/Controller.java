package boxing;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Controller.java
 * A Controller that takes keyboard inputs and interfaces with BoxerView and Boxer
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Controller implements EventHandler<KeyEvent> {
    @FXML private BoxerView boxerView;
    @FXML private Label leftHealth;
    @FXML private Label rightHealth;
    @FXML private Label leftEnergy;
    @FXML private Label rightEnergy;
    private Boxer boxerLeft;
    private Boxer boxerRight;

    /**
     * Initializes controller
     */
    public Controller() {
    }

    /**
     * Helper method that updates view
     */
    private void updateView() {
        this.boxerView.update(boxerLeft, boxerRight);
        this.leftHealth.setText(String.format("Health: %d", this.boxerLeft.getHealth()));
        this.rightHealth.setText(String.format("Health: %d", this.boxerRight.getHealth()));
        this.leftEnergy.setText(String.format("Energy: %d", this.boxerLeft.getEnergy()));
        this.rightEnergy.setText(String.format("Energy: %d", this.boxerRight.getEnergy()));
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
            boxerLeft.move(-1);
        }
        if (code == KeyCode.D){
            boxerLeft.move(1);
        }
        if (code == KeyCode.LEFT){
            boxerRight.move(-1);
        }
        if (code == KeyCode.RIGHT){
            boxerRight.move(1);
        }
        if (code == KeyCode.DIGIT1){
            boxerLeft.punch();
        }
        if (code == KeyCode.L){
            boxerRight.punch();
        }
        this.updateView();
    }

    public double getBoardWidth() {
        return BoxerView.CELL_WIDTH * this.boxerView.getWidth();
    }

    public void initialize() {
        this.boxerLeft = new Boxer(true,10,5);
        this.boxerRight = new Boxer(false,40,5);

        this.boxerLeft.addOpponent(this.boxerRight);
        this.boxerRight.addOpponent(this.boxerLeft);

        this.updateView();
    }

//    private void startTimer() {
//        this.timer = new java.util.Timer();
//        TimerTask timerTask = new TimerTask() {
//            public void run() {
//                Platform.runLater(new Runnable() {
//                    public void run() {
//                        updateAnimation();
//                    }
//                });
//            }
//        };
//
//        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
//        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
//    }
}
