public class Usuario {

    private String plano;
    private boolean isPremium;

    public Usuario(String plano, boolean isPremium) {
        this.plano = plano;
        this.isPremium = isPremium;
    }

    public String getPlano() {
        return plano;
    }

    public void setPlano(String plano) {
        this.plano = plano;
    }

    public boolean isPremium() {
        return isPremium;
    }

    public void setPremium(boolean premium) {
        isPremium = premium;
    }
}
