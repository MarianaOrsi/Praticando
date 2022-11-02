public class animal {
    private String tipo;
    private String tamanho;
    private int peso;

    public animal(String tipo, String tamanho, int peso) {
        this.tipo = tipo;
        this.tamanho = tamanho;
        this.peso = peso;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getTamanho() {
        return tamanho;
    }

    public void setTamanho(String tamanho) {
        this.tamanho = tamanho;
    }

    public int getPeso() {
        return peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }

    public boolean Epesado(){
        return this.peso > 500 & this.tamanho.equals("Grande");
    }
}
