package boxing;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

/**
 * BoxerView.java
 * A View class that sets up the user's view
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class BoxerView{
    public final static double CELL_WIDTH = 5.0;
    public final static double CELL_HEIGHT = 75.0;
    @FXML private int cellCount;
    private Rectangle[] cellViews;

    /**
     * Initializes the BoxerView
     */
    public BoxerView() { }

    /**
     * Starts the fight from the title screen
     *
     * @param width width of the fighting screen
     * @param left Boxer on the left side
     * @param right Boxer on the right side
     * @param time timer value for the fight
     * @param startHealth initial health
     * @param startEnergy initial energy
     * @param energyRegen energy regeneration rate
     */
    public void startFight(int width, Boxer left, Boxer right, int time, int startHealth, int startEnergy, int energyRegen) { }

    /**
     * Gets width of fight screen
     */
    public int getWidth() { return this.cellCount; }

    public void setWidth(int cellCount) {
        this.cellCount = cellCount;
        this.initializeGame();
    }
    /**
     * Initializes game screen for user to character select screen
     */
    private void initializeGame() {
        if (this.cellCount > 0) {
            this.cellViews = new Rectangle[this.cellCount];
            for (int row = 0; row < this.cellCount; row++) {
                Rectangle rectangle = new Rectangle();
                rectangle.setX(CELL_HEIGHT/2); // FIX MAYBE TODO FIX ME
                rectangle.setY((double)row * CELL_WIDTH);
                rectangle.setWidth(CELL_WIDTH);
                rectangle.setHeight(CELL_HEIGHT);
                this.cellViews[row]= rectangle;
                this.getChildren().add(rectangle);
            }
        }
    }

    /**
     * Updates user view according to actions of Boxers
     *
     * @param left Boxer on the left side
     * @param right Boxer on the right side
     */
    public void update(Boxer left, Boxer right) { }
}
