package boxing;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

import java.awt.*;

public class BoxerView extends Group{
    @FXML private Label leftHealth;
    @FXML private Label rightHealth;
    @FXML private Label leftEnergy;
    @FXML private Label rightEnergy;
    @FXML private ImageView rightImageView;
    @FXML private ImageView leftImageView;
    @FXML private ImageView background;

    public BoxerView() {}

    public void update(Boxer boxerLeft, Boxer boxerRight){
        this.leftHealth.setText(String.format("Health: %d", boxerLeft.getHealth()));
        this.rightHealth.setText(String.format("Health: %d", boxerRight.getHealth()));
        this.leftEnergy.setText(String.format("Energy: %d", boxerLeft.getEnergy()));
        this.rightEnergy.setText(String.format("Energy: %d", boxerRight.getEnergy()));

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
}
