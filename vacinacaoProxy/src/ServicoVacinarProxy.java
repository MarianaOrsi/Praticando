import java.util.Date;

public class ServicoVacinarProxy implements Vacinar{
    @Override
    public void vacinarPessoa(Pessoa pessoa) {
        if(pessoa.getDataLiberacaoVacina().before(new Date(2022,10,20))){
            new ServicoVacinar().vacinarPessoa(pessoa);
        }else{
            System.out.println("Usuario(a) "+pessoa.getNome()+" ainda não pode ser vacinado");
        }
    }
}
