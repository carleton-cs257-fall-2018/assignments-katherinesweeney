package boxing;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.WindowEvent;
import javafx.event.EventHandler;
import javafx.application.Platform;

/**
 * Main.java
 * Main class for boxing game. Initializes start up process
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Main extends Application {

    /**
     * Sets up stage.
     *
     * @param primaryStage main javafx stage for game
     * @throws Exception error in set up
     */
    @Override
    public void start(javafx.stage.Stage primaryStage) throws Exception{
        primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            @Override
            public void handle(WindowEvent t) {
                Platform.exit();
                System.exit(0);
            }
        });
        FXMLLoader loader = new FXMLLoader(getClass().getResource("boxing.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("Boxing");

        Controller controller = loader.getController();
        root.setOnKeyPressed(controller);
        double sceneWidth = 1200.0;
        double sceneHeight = 400.0;
        primaryStage.setScene(new Scene(root, sceneWidth, sceneHeight));
        primaryStage.show();
        root.requestFocus();
    }

    /**
     * Launches game
     *
     * @param args commandline arguments
     */
    public static void main(String[] args) { launch(args); }
}