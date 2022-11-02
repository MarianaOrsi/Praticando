import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class animalTest {

    @Test
    public void SeOAnimalEPesado(){
        animal cavalo = new animal("Cavalo", "Grande",750);
        animal cachorro = new animal("Cachorro", "Pequeno",8);

        boolean ePesado = cachorro.Epesado();

        assertEquals(true, cavalo.Epesado());
        assertFalse(ePesado);
    }

}