import java.util.Date;

public class ServicoVacinar implements Vacinar{
    @Override
    public void vacinarPessoa(Pessoa pessoa) {
        System.out.println("Usuario(a) "+pessoa.getNome()+ " vacinado(a) em "+ new Date() + " com sucesso");
    }
}
