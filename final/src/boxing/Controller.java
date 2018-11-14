package boxing;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

/**
 * Controller.java
 * A Controller that takes keyboard inputs and interfaces with BoxerView and Boxer
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Controller implements EventHandler<KeyEvent> {
    @FXML private BoxerView boxerView;
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
    }

    /**
     * Calls the appropriate methods at different key events from the user
     *
     * @param keyEvent key pressed by user
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();

        String s = code.getChar();
        if (s.length() > 0) {
            char theCharacterWeWant = s.charAt(0);
        }
        if (code == KeyCode.M){
            boxerLeft.move(1);
            boxerRight.move(-1);
        }
        this.updateView();
    }

    public double getBoardWidth() {
        return BoxerView.CELL_WIDTH * this.boxerView.getWidth();
    }

    public void initialize() {


        this.boxerLeft = new Boxer(true,10,5);
        this.boxerRight = new Boxer(false,40,5);
    }
}
