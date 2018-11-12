package boxing;

import javafx.scene.input.KeyEvent;

/**
 * Controller.java
 * A Controller that takes keyboard inputs and interfaces with BoxerView and Boxer
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Controller implements EventHandler<KeyEvent> {

    /**
     * Initializes controller
     */
    public Controller() { }

    /**
     * Helper method that updates view
     */
    private void updateView() { }

    /**
     * Calls the appropriate methods at different key events from the user
     *
     * @param keyEvent key pressed by user
     */
    @Override
    public void handle(KeyEvent keyEvent) { }
}
