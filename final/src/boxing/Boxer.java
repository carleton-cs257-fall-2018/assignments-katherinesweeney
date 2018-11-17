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
    private int cellCount = 80;
    private int health = 100;
    private int energy = 100;
    private boolean isRight;
    private boolean isPunching = false;
    private boolean isBlocking = false;
    private boolean isKicking = false;
    private boolean isHit = false;
    private int idle = 0;
    /**
     * Initializes a new boxer
     *
     * @param isRight boxer is the right boxer on screen
     * @param startPosition position boxer starts at
     * @param width width of the boxer on the screen
     */
    public Boxer(boolean isRight, int startPosition, int width) {
        this.position=startPosition;
        this.isRight = isRight;
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
        if(this.position+move < cellCount-6 && this.position+move > 0 && Math.abs(this.position+move-opponent.getPosition())>5) {
            this.position += move;
        }
    }

    /**
     * Returns position of the Boxer
     *
     * @return position of Boxer
     */
    public int getPosition() {
        return this.position; }

    /**
     * Executes a punch
     */
    public void punch() {
        if(!this.isPunching && !this.isKicking) {
            this.isBlocking = false;
            if (this.energy > 9) {
                opponent.getPunched();
                this.energy -= 10;
                this.isPunching = true;
            }
        }
    }

    /**
     * Executes a block
     */
    public void block() {
        if(!this.isBlocking) {
            this.isBlocking = true;
        }
        else{
            this.isBlocking = false;
        }
    }

    /**
     * Execute a kick
     */
    public void kick() {
        if(!this.isPunching && !this.isKicking) {
            this.isBlocking = false;
            if (this.energy > 24) {
                opponent.getKicked();
                this.energy -= 25;
                this.isKicking = true;
            }
        }
    }

    private void takeHealth(int health){
        this.health-=health;
        if (this.health < 0) {
            this.health = 0;
        }
    }

    /**
     * Called when in hit box of opponent's punch
     * and updates health
     */
    public void getPunched() {
        int moveDirection = -1;
        if(this.isRight){
            moveDirection = 1;
        }
        if (Math.abs(opponent.position-this.position)==8 || Math.abs(opponent.position-this.position)==9){
            if(this.isBlocking) {
                this.takeHealth(2);
                this.addEnergy(-5);
                this.isBlocking = false;
            }
            else{
                this.takeHealth(10);
                this.isHit = true;
            }
            this.move(moveDirection);
        }
        if (Math.abs(opponent.position-this.position)==6 || Math.abs(opponent.position-this.position)==7){
            if(!this.isBlocking) {
                this.takeHealth(6);
                this.isHit = true;
            }
            else{
                this.addEnergy(-5);
            }
            this.move(moveDirection);
        }
        if (Math.abs(opponent.position-this.position)==10 || Math.abs(opponent.position-this.position)==11){
            if(!this.isBlocking) {
                this.takeHealth(2);
            }
            else{
                this.addEnergy(-5);
            }
        }
    }

    /**
     * Called when in hit box of oppenent's kick
     * and updates health
     */
    public void getKicked() {
    }

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
    public int getEnergy() { return this.energy; }

    /**
     * Adds energy to Boxer's energy
     *
     * @param energy energy to add to Boxer
     */
    public void addEnergy(int energy) {
        this.energy+=energy;
        if(this.energy>100){
            this.energy = 100;
        }
        if(this.energy < 0){
            this.energy = 0;
        }
    }

    /**
     * Retreives the location of the image that represents the Boxer
     *
     * @return image file path
     */
    public String getImage () {
        String imagePath = "assets/";

        if (this.isRight){
            imagePath+="enemy";
        }
        else{
            imagePath+="player";
        }

        if (this.isPunching){
            imagePath+="Punch";
            this.isPunching = false;
        }
        else if (this.isBlocking){
            imagePath+="Block";
        }
        else if (this.isHit){
            imagePath+="Hit";
            this.isHit = false;
        }
        else{
            imagePath+="Idle";
            imagePath+=Integer.toString(this.idle);
            this.idle+=1;
            if(this.idle == 4){
                this.idle = 0;
            }
        }

        imagePath+=".png";
        return imagePath;
    }

    public boolean isBlocking(){
        return this.isBlocking;
    }

    public void setBlockingFalse(){
        this.isBlocking = false;
    }
}
