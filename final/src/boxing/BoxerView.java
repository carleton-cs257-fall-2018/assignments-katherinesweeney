package boxing;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.ImagePattern;
import javafx.scene.image.PixelReader;
import javafx.scene.image.WritableImage;

import java.awt.*;
import java.io.FileInputStream;


/**
 * BoxerView.java
 * A View class that sets up the user's view
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class BoxerView extends Group {
    public final static double CELL_WIDTH = 25.0;
    public final static double CELL_HEIGHT = 150;
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
                rectangle.setFill(Color.WHITE);
                this.cellViews[row]= rectangle;

                this.getChildren().add(rectangle);
            }
        }
    }

    /**
     * Clears the images from the board
     */
    private void clearBoard() {
        for(Rectangle rectangle : this.cellViews){
            rectangle.setFill(Color.GRAY);
        }
    }

    /**
     * Updates user view according to actions of Boxers
     *
     * @param left Boxer on the left side
     * @param right Boxer on the right side
     */
    public void update(Boxer left, Boxer right){
        this.clearBoard();
        Image leftImg = new Image("file:assets/player.png");
        addImage(left.getPosition()-1, 3, leftImg);

        Image rightImg = new Image("file:assets/enemy.png");
        addImage(right.getPosition()-1, 3, rightImg);
    }

    public void addImage(int startPosition, int length, Image img){
        PixelReader reader = img.getPixelReader();
        int width = (int)(img.getWidth());
        int height = (int)(img.getHeight());

        for(int i = 0; i<length; i++){
            WritableImage imagePart = new WritableImage(reader, i*(width/length),0, width/length, height);
            cellViews[startPosition+i].setFill(new ImagePattern(imagePart));
        }

    }
}
