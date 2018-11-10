package boxing;

/**
 * BoxerView.java
 * A View calss that sets up the user's view
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class BoxerView extends Group {

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
    public void getWidth() { }

    /**
     * Initializes game screen for user to character select screen
     */
    private void initializeGame() { }

    /**
     * Updates user view according to actions of Boxers
     *
     * @param left Boxer on the left side
     * @param right Boxer on the right side
     */
    public void update(Boxer left, Boxer right) { }
}
