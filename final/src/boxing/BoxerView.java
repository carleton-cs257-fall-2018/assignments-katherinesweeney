package boxing;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

import java.awt.*;

/**
 * BoxerView.java
 * A View class that sets up the user's view
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class BoxerView extends Group {
    public final static double CELL_WIDTH = 20.0;
    public final static double CELL_HEIGHT = 300;
    @FXML private int cellCount = 50;
    private Rectangle[] cellViews;

    /**
     * Initializes the BoxerView
     */
    public BoxerView() { this.initializeGame();}

    public int getCellCount() {
        return this.cellCount;
    }

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
                rectangle.setX((double)row * CELL_WIDTH);
                rectangle.setY(0);
                rectangle.setWidth(CELL_WIDTH);
                rectangle.setHeight(CELL_HEIGHT);
                if (row%2==0){
                rectangle.setFill(Color.RED);}
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
    public void update(Boxer left, Boxer right) {
        this.cellViews[left.getPosition()].setFill(Color.WHITE);
        this.cellViews[right.getPosition()].setFill(Color.WHITE);
    }
}
