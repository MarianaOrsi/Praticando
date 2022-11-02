public class CheckProduto {
    CheckQuallity checkQuallity;

    public CheckProduto(){
        this.checkQuallity = new CheckQuallityLote();
        CheckQuallity peso = new CheckQuallityPeso();
        CheckQuallity embalagem = new CheckQuallityEmbalagem();


        this.checkQuallity.setCheckQuallitySeguinte(peso);
        peso.setCheckQuallitySeguinte(embalagem);

    }

    public void Verificar(Produto produto){
        checkQuallity.verificar(produto);
    }
}
