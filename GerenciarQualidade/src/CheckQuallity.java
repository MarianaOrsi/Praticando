public abstract class CheckQuallity {
    private CheckQuallity checkQuallitySeguinte;

    public CheckQuallity getCheckQuallitySeguinte(){
        return checkQuallitySeguinte;
    }

    public void setCheckQuallitySeguinte(CheckQuallity checkQuallitySeguinte) {
        this.checkQuallitySeguinte = checkQuallitySeguinte;
    }

    public abstract void verificar(Produto produto);
}
