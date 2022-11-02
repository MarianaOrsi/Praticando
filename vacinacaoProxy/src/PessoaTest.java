import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;

class PessoaTest {


    @Test
    void vacinar1(){
        Date data = new Date(2022,10,19);
        Pessoa pessoa = new Pessoa("Juca","Santos", "254987657",
                data, "Pfizer");
        new ServicoVacinarProxy().vacinarPessoa(pessoa);
    }
    @Test
    void vacinar2(){
        Date data = new Date(2022,10,21);
        Pessoa pessoa = new Pessoa("Maria","do Carmo", "987521145",
                data, "Coronavac");
        new ServicoVacinarProxy().vacinarPessoa(pessoa);
    }
}