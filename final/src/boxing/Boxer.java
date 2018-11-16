package boxing;



/**
 * Boxer.java
 * A Model class that represents the upderlying data for Boxers
 *
 * @author Owen Barnett, Justin Hahn, Kate Sweeney
 */
public class Boxer {
    private int position;
    private Boxer opponent;
    private int cellCount = 50;
    private int health = 100;
    /**
     * Initializes a new boxer
     *
     * @param isRight boxer is the right boxer on screen
     * @param startPosition position boxer starts at
     * @param width width of the boxer on the screen
     */
    public Boxer(boolean isRight, int startPosition, int width) {
        this.position=startPosition;
    }

    /**
     * Sets the opponent Boxer reference
     *
     * @param opponent Oponent Boxer object
     */
    public void addOpponent(Boxer opponent) {
        this.opponent = opponent;
    }

    /**
     * Updates Boxer position
     *
     * @param move distance Boxer moves right
     */
    public void move(int move) {
        if(this.position+move < cellCount-3 && this.position+move > 3 && Math.abs(this.position+move-opponent.getPosition())>2) {
            this.position += move;
        }
    }

    /**
     * Returns position of the Boxer
     *
     * @return position of Boxer
     */
    public int getPosition() { return this.position; }

    /**
     * Executes a punch
     */
    public void punch() {
        opponent.getPunched();
    }

    /**
     * Executes a block
     */
    public void block() { }

    /**
     * Execute a kick
     */
    public void kick() { }

    /**
     * Called when in hit box of opponent's punch
     * and updates health
     */
    public void getPunched() {
        if (Math.abs(opponent.position-this.position)==4){
            this.health-=10;
        }
        if (Math.abs(opponent.position-this.position)==3){
            this.health-=6;
        }
        if (Math.abs(opponent.position-this.position)==5){
            this.health-=2;
        }
    }

    /**
     * Called when in hit box of oppenent's kick
     * and updates health
     */
    public void getKicked() { }

    /**
     * Returns health of Boxer
     *
     * @return health of Boxer
     */
    public int getHealth() { return this.health; }

    /**
     * Returns energy of Boxer
     *
     * @return energy of Boxer
     */
    public int getEnergy() { return 1; }

    /**
     * Adds energy to Boxer's energy
     *
     * @param energy energy to add to Boxer
     */
    public void addEnergy(int energy) { }

    /**
     * Retreives the location of the image that represents the Boxer
     *
     * @return image file path
     */
    public String getImage () { return "Hello, world!"; }

}
