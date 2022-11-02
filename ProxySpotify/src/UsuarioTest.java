import org.testng.annotations.Test;

import static org.junit.jupiter.api.Assertions.*;

public class UsuarioTest {

    @Test
    void usuario1() {
        Usuario usuario = new Usuario("Premium", true);
        new ServicoDownloadProxy().solicitarDowload(usuario);
    }

    @Test
    void usuario2() {
        Usuario usuario = new Usuario("Free", false);
        new ServicoDownloadProxy().solicitarDowload(usuario);
    }

}