import java.util.Date;

public class Pessoa {
    private String nome;
    private String sobrenome;
    private String rg;
    private Date dataLiberacaoVacina;
    private String nomeVacina;

    public Pessoa(String nome, String sobrenome, String rg, Date dataLiberacaoVacina, String nomeVacina) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.rg = rg;
        this.dataLiberacaoVacina = dataLiberacaoVacina;
        this.nomeVacina = nomeVacina;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public Date getDataLiberacaoVacina() {
        return dataLiberacaoVacina;
    }

    public void setDataLiberacaoVacina(Date dataLiberacaoVacina) {
        this.dataLiberacaoVacina = dataLiberacaoVacina;
    }

    public String getNomeVacina() {
        return nomeVacina;
    }

    public void setNomeVacina(String nomeVacina) {
        this.nomeVacina = nomeVacina;
    }
}
