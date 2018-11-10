package boxing;


public class Boxer {

    /**
     * Initializes a new boxer
     *
     * @param isRight boxer is the right boxer on screen
     * @param start_position position boxer starts at
     * @param width width of the boxer on the screen
     */
    public boxer(boolean isRight, int start_position, int width) { }

    /**
     * Sets the opponent Boxer reference
     *
     * @param opponent Oponent Boxer object
     */
    public void addOpponent(Boxer opponent) { }

    /**
     * 
     *
     * @param moveRight
     */
    public void move(boolean moveRight) { }

    public int getPosition() { return 1 }

    public void punch() { }

    public void block() { }

    public void kick() { }

    public void getPunched() { }

    public void getKicked() { }

    public int getHealth() { return 1 }

    public int getEnergy() { return 1 }

    public void addEnergy(int energy) { }

}
