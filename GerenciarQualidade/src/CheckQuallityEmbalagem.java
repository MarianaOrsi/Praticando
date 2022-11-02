public class CheckQuallityEmbalagem extends CheckQuallity {
    @Override
    public void verificar(Produto produto) {
        if(produto.getEmbalagem().equalsIgnoreCase("Saudavel") || produto.getEmbalagem().equalsIgnoreCase("Quase Saudavel")){
            System.out.println("A embalagem do produto " + produto.getNome() + " foi aprovada! \n" + "O produto foi aprovado");
            if(this.getCheckQuallitySeguinte() != null){
                this.getCheckQuallitySeguinte().verificar(produto);
            }
        }else{
            System.out.println("Produto " + produto.getNome() + " Rejeitado! a embalagem " + produto.getEmbalagem() + " não se encontra adequada! \n");
        }
    }
}